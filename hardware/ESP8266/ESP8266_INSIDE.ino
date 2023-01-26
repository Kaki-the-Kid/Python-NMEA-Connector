#include <ESP8266WiFi.h>
#include <Wire.h>
#include <SPI.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>
#include <Adafruit_INA219.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include "Adafruit_MQTT.h"
#include "Adafruit_MQTT_Client.h"

/************************* WiFi Access Point *********************************/

#define WLAN_SSID       "xxxxxxxx"
#define WLAN_PASS       "xxxxxxxx"

/************************* Adafruit.io Setup *********************************/

#define AIO_SERVER      "io.adafruit.com"
#define AIO_SERVERPORT  1883                   // use 8883 for SSL
#define AIO_USERNAME    "xxxxxxxx"
#define AIO_KEY         "xxxxxxxx"

/************ Setup WiFi ******************/

// Create an ESP8266 WiFiClient class to connect to the MQTT server.
WiFiClient client;
// or... use WiFiFlientSecure for SSL
//WiFiClientSecure client;

/****************************** MQTT ***************************************/

// Store the MQTT server, username, and password in flash memory.
// This is required for using the Adafruit MQTT library.
const char MQTT_SERVER[] PROGMEM    = AIO_SERVER;
const char MQTT_USERNAME[] PROGMEM  = AIO_USERNAME;
const char MQTT_PASSWORD[] PROGMEM  = AIO_KEY;

// Setup the MQTT client class by passing in the WiFi client and MQTT server and login details.
Adafruit_MQTT_Client mqtt(&client, MQTT_SERVER, AIO_SERVERPORT, MQTT_USERNAME, MQTT_PASSWORD);

/****************************** Feeds ***************************************/

// Notice MQTT paths for AIO follow the form: <username>/feeds/<feedname>
const char SENSORTEMPINSIDE[] PROGMEM = AIO_USERNAME "/feeds/sensortempinside";
Adafruit_MQTT_Publish sensortempinside = Adafruit_MQTT_Publish(&mqtt, SENSORTEMPINSIDE);

const char SENSORPRESSUREINSIDE[] PROGMEM = AIO_USERNAME "/feeds/sensorpressureinside";
Adafruit_MQTT_Publish sensorpressureinside = Adafruit_MQTT_Publish(&mqtt, SENSORPRESSUREINSIDE);

const char SENSORHUMIDITYINSDE[] PROGMEM = AIO_USERNAME "/feeds/sensorhumidityinside";
Adafruit_MQTT_Publish sensorhumidityinside = Adafruit_MQTT_Publish(&mqtt, SENSORHUMIDITYINSDE);

const char FEATHERBATTERYINSIDE[] PROGMEM = AIO_USERNAME "/feeds/featherbatteryinside";
Adafruit_MQTT_Publish featherbatteryinside = Adafruit_MQTT_Publish(&mqtt, FEATHERBATTERYINSIDE);

/************************* THingSpeak IO *********************************/

String apiKey = "xxxxxxxx";     // This WriteAPI key is generated by ThingSpeak.com for your channel
const char* server = "api.thingspeak.com";

/****************************** Display ***************************************/

#define OLED_RESET 3
Adafruit_SSD1306 display(OLED_RESET);

#define LOGO16_GLCD_HEIGHT 16
#define LOGO16_GLCD_WIDTH  16
static const unsigned char PROGMEM logo16_glcd_bmp[] =
{ B00000000, B11000000,
  B00000001, B11000000,
  B00000001, B11000000,
  B00000011, B11100000,
  B11110011, B11100000,
  B11111110, B11111000,
  B01111110, B11111111,
  B00110011, B10011111,
  B00011111, B11111100,
  B00001101, B01110000,
  B00011011, B10100000,
  B00111111, B11100000,
  B00111111, B11110000,
  B01111100, B11110000,
  B01110000, B01110000,
  B00000000, B00110000
};

/****************************** current sensor ***************************************/

Adafruit_INA219 ina219;

/****************************** Adafruit_BME280 ***************************************/

Adafruit_BME280 bme; // I2C

/*************************** Sketch Code ************************************/

// Bug workaround for Arduino 1.6.6, it seems to need a function declaration
// for some reason (only affects ESP8266, likely an arduino-builder bug).
void MQTT_connect();

void setup() {
  // beginn
  Serial.begin(115200);
  delay(10);

  Serial.println("\nFeather Huzzah ESP8266 + FeatherWing OLED + BME280 + INA219");

  Serial.println("\nESP8266 in normal mode");

  // Connect to WiFi access point.
  Serial.print("\nConnecting to ");
  Serial.println(WLAN_SSID);

  WiFi.begin(WLAN_SSID, WLAN_PASS);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println();
  Serial.println("\nWiFi connected");
  Serial.print("\nIP address: "); Serial.println(WiFi.localIP());

  // init the sensor
  if (!bme.begin()) {
    Serial.println("Could not find a valid BME280 sensor, check wiring!");
    while (1);
  }

  // Initialize the INA219.
  ina219.begin();

  // by default, we'll generate the high voltage from the 3.3v line internally! (neat!)
  display.begin(SSD1306_SWITCHCAPVCC, 0x3C);  // initialize with the I2C addr 0x3C (for the 128x32)
  // init done

  // Clear the buffer.
  display.clearDisplay();
  display.setTextSize(1);
  display.setTextColor(WHITE);

  // define the led's
  pinMode(0, OUTPUT); // red LED
  pinMode(2, OUTPUT); // blue LED

  // Ensure the connection to the MQTT server is alive (this will make the first
  // connection and automatically reconnect when disconnected).  See the MQTT_connect
  // function definition further below.
  MQTT_connect();

  float temp = bme.readTemperature();
  float pressure = bme.readPressure() / 100.0F;
  float humidity = bme.readHumidity();

  float shuntvoltage = 0;
  float busvoltage = 0;
  float current_mA = 0;
  float loadvoltage = 0;

  shuntvoltage = ina219.getShuntVoltage_mV();
  busvoltage = ina219.getBusVoltage_V();
  current_mA = ina219.getCurrent_mA();
  loadvoltage = busvoltage + (shuntvoltage / 1000);

  // print to console

  Serial.println("\nWrite to Console");

  Serial.println("\nMeasuring temp, pressure and humidity with BME280 ...");

  Serial.print("\nTemperatur = "); Serial.print(temp); Serial.println(" *C");
  Serial.print("Luftdruck = "); Serial.print(pressure); Serial.println(" hPa");
  Serial.print("Luftfeuchtigkeit = "); Serial.print(humidity); Serial.println(" %");

  Serial.println("\nMeasuring voltage and current with INA219 ...");

  Serial.print("\nBus Voltage:   "); Serial.print(busvoltage); Serial.println(" V");
  Serial.print("Shunt Voltage: "); Serial.print(shuntvoltage); Serial.println(" mV");
  Serial.print("Load Voltage:  "); Serial.print(loadvoltage); Serial.println(" V");
  Serial.print("Current:       "); Serial.print(current_mA); Serial.println(" mA");

  blink_red();

  // print to display

  Serial.println("\nWrite to Display");

  display.setCursor(0, 0);
  display.print("Temperatur = "); display.print(temp, 2); display.println(" *C");

  display.setCursor(0, 8);
  display.print("Luftdruck  = "); display.print(pressure, 0); display.println(" hPa");

  display.setCursor(0, 16);
  display.print("rLF        = "); display.print(humidity, 2); display.println(" %");

  display.setCursor(0, 24);
  display.print("Spannung   = "); display.print(busvoltage, 2); display.println(" V");

  display.display();

  blink_red();

  // write stuff to adafruit.io

  Serial.println("\nSend data to adafruit.io");

  // Now we can publish stuff!
  Serial.print(F("\nSending SensorTempInside val "));
  Serial.print(temp, 2);
  Serial.print("...");
  if (! sensortempinside.publish(temp, 2)) {
    Serial.println("Failed");
  } else {
    Serial.println("OK!");
  }

  blink_blue();

  Serial.print(F("Sending SensorPressureInside val "));
  Serial.print(pressure, 1);
  Serial.print("...");
  if (! sensorpressureinside.publish(pressure, 2)) {
    Serial.println("Failed");
  } else {
    Serial.println("OK!");
  }

  blink_blue();

  Serial.print("Sending SensorHumidityInside val ");
  Serial.print(humidity, 2);
  Serial.print("...");
  if (! sensorhumidityinside.publish(humidity, 2)) {
    Serial.println(F("Failed"));
  } else {
    Serial.println("OK!");
  }

  blink_blue();

  Serial.print(F("Sending FeatherBatteryInside val "));
  Serial.print(busvoltage, 2);
  Serial.print("...");
  if (! featherbatteryinside.publish(busvoltage, 2)) {
    Serial.println("Failed");
  } else {
    Serial.println("OK!");
  }

  blink_blue();

  // write stuff to thingspeak

  if (client.connect(server, 80)) { // "184.106.153.149" or api.thingspeak.com  // Connect to the ThingsSpeak.com website

    String postStr = apiKey;        // Build the update string

    postStr += "&field5=";
    postStr += String(temp, 2);

    postStr += "&field6=";
    postStr += String(pressure, 2);

    postStr += "&field7=";
    postStr += String(humidity, 2);

    postStr += "&field8=";
    postStr += String(busvoltage, 2);

    client.print("POST /update HTTP/1.1\n");
    client.print("Host: api.thingspeak.com\n");
    client.print("Connection: close\n");
    client.print("X-THINGSPEAKAPIKEY: " + apiKey + "\n");
    client.print("Content-Type: application/x-www-form-urlencoded\n");
    client.print("Content-Length: ");
    client.print(postStr.length());
    client.print("\n\n");
    client.print(postStr);
    client.stop();

    Serial.println("\nSend data to thingspeak: ");
    Serial.println();
    Serial.println(postStr);

  }

  blink_blue();

  WiFi.disconnect();
  Serial.println("\nWifi disconnected");

  // going to deep sleep to save battery
  // Time to sleep (in seconds):
  const int sleepTimeS = 100;

  // Sleep
  Serial.println("\nESP8266 in sleep mode");
  ESP.deepSleep(sleepTimeS * 1000000);
  delay(100); // this seems to be important, otherwise the board will not go into deep sleep

}

void blink_blue() {

  digitalWrite(2, LOW);
  delay(200);
  digitalWrite(2, HIGH);
  delay(200);

}

void blink_red() {

  digitalWrite(0, LOW);
  delay(200);
  digitalWrite(0, HIGH);
  delay(200);

}

// Function to connect and reconnect as necessary to the MQTT server.
// Should be called in the loop function and it will take care if connecting.
void MQTT_connect() {
  int8_t ret;

  // Stop if already connected.
  if (mqtt.connected()) {
    return;
  }

  Serial.print("\nConnecting to MQTT... ");

  uint8_t retries = 3;
  while ((ret = mqtt.connect()) != 0) { // connect will return 0 for connected
    Serial.println(mqtt.connectErrorString(ret));
    Serial.println("Retrying MQTT connection in 5 seconds...");
    mqtt.disconnect();
    delay(5000);  // wait 5 seconds
    retries--;
    if (retries == 0) {
      // basically die and wait for WDT to reset me
      while (1);
    }
  }
  Serial.println("MQTT Connected!");
}

void loop() {

  // loop

}