class IoTFunctions:
    def __init__(self, client):
        self.client = client
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_publish = self.on_publish
        self.client.on_subscribe = self.on_subscribe
        self.client.on_log = self.on_log
        self.client.on_disconnect = self.on_disconnect
        self.client.on_unsubscribe = self.on_unsubscribe

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        client.subscribe("iot-2/type/+/id/+/evt/+/fmt/+")

    def on_message(self, client, userdata, msg):
        print(msg.topic+" "+str(msg.payload))

    def on_publish(self, client, userdata, mid):
        print("mid: "+str(mid))

    def on_subscribe(self, client, userdata, mid, granted_qos):
        print("Subscribed: "+str(mid)+" "+str(granted_qos))

    def on_log(self, client, userdata, level, buf):
        print("log: "+buf)

    def on_disconnect(self, client, userdata, rc):
        if rc != 0:
            print("Unexpected disconnection.")

    def on_unsubscribe(self, client, userdata, mid):
        print("Unsubscribed: "+str(mid))
    
    