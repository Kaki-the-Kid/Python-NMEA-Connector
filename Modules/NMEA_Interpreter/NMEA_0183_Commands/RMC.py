# ****************************************************************************//*
# *   @project  Python NMEA Connector
# *   @file     BWC.py
# *   @brief    Cross Track Error, Measured
# *   @author   Karsten Reitan Sørensen
# *   Date:     11-02-2023
# *******************************************************************************

from NMEA0183_Commands import NMEA0183_Command


class RMC(NMEA0183_Command):

    def __init__(self, sentence):
        self._datasentence = sentence.split(",")
        if (message == null or message.Length < 11):
            raise Exception("Invalid RMC: {}".message)

        if (message[8].Length == 6 and message[0].Length >= 6):
            FixTime = new DateTimeOffset(int.Parse(message[8].Substring(4, 2), CultureInfo.InvariantCulture) + 2000,
                                    int.Parse(message[8].Substring(2, 2), CultureInfo.InvariantCulture),
                                    int.Parse(message[8].Substring(0, 2), CultureInfo.InvariantCulture),
                                    int.Parse(message[0].Substring(0, 2), CultureInfo.InvariantCulture),
                                    int.Parse(message[0].Substring(2, 2), CultureInfo.InvariantCulture),
                                    0, TimeSpan.Zero).AddSeconds(double.Parse(message[0].Substring(4), CultureInfo.InvariantCulture))
        
        self.time = ""
        self.status = ""
        float: self.latitude = 0.0
        # Latitude
        Latitude = NmeaMessage.StringToLatitude(message[2], message[3])
        self.latitude_direction = ""
        # Longitude
        float: self.longitude = 0.0
        Longitude = NmeaMessage.StringToLongitude(message[4], message[5])
        self.longitude_direction = ""
        # Speed over the ground in knots
        self.speed = 0.0
        Speed = NmeaMessage.StringToDouble(message[6])
        # Track angle in degrees True
        float: self.course = 0.0 #track_angle
        Course = NmeaMessage.StringToDouble(message[7])
        self.date = ""
        # Magnetic Variation
        float: self.magnetic_variation = 0.0
        MagneticVariation = NmeaMessage.StringToDouble(message[9])
        self.magnetic_variation_direction = ""
        if (not double.IsNaN(MagneticVariation) and message[10] == "W")
            MagneticVariation *= -1
        # Mode indicator
        self.mode_indicator = ""

        Active = (message[1] == "A")


    def set_time(self, time):
        self.time = time

    def get_time(self):
        return self.time

    def set_status(self, status):
        self.status = status

    def get_status(self):
        return self.status

    def set_latitude(self, latitude):
        self.latitude = latitude

    def get_latitude(self):
        return self.latitude

    def set_latitude_direction(self, latitude_direction):
        self.latitude_direction = latitude_direction

    def get_latitude_direction(self):
        return self.latitude_direction

    def set_longitude(self, longitude):
        self.longitude = longitude

    def get_longitude(self):
        return self.longitude

    def set_longitude_direction(self, longitude_direction):
        self.longitude_direction = longitude_direction

    def get_longitude_direction(self):
        return self.longitude_direction

    def set_speed(self, speed):
        self.speed = speed

    def get_speed(self):
        return self.speed

    def set_track_angle(self, track_angle):
        self.track_angle = track_angle

    def get_track_angle(self):
        return self.track_angle

    def set_date(self, date):
        self.date = date

    def get_date(self):
        return self.date

    def set_magnetic_variation(self, magnetic_variation):
        self.magnetic_variation = magnetic_variation

    def get_magnetic_variation(self):
        return self.magnetic_variation

    def set_magnetic_variation_direction(self, magnetic_variation_direction):
        self.magnetic_variation_direction = magnetic_variation_direction

    def get_magnetic_variation_direction(self):
        return self.magnetic_variation_direction

    def set_mode_indicator(self, mode_indicator):
        self.mode_indicator = mode_indicator

    def get_mode_indicator(self):
        # Fix Time
        public DateTimeOffset FixTime { get }

        # Gets a value whether the device is active
        public bool Active { get }

        TimeSpan ITimestampedMessage.Timestamp => FixTime.TimeOfDay


    #TestMethod
    def TestCodeGPRMC():
        str input = "$GPRMC,123519,A,4807.038,S,01131.000,W,022.4,084.4,230313,003.1,W*6A"
        var msg = NmeaMessage.Parse(input)
        Assert.IsInstanceOfType(msg, typeof(Rmc))
        Rmc rmc = (Rmc)msg
        Assert.AreEqual(new DateTimeOffset(2013, 03, 23, 12, 35, 19, TimeSpan.Zero), rmc.FixTime)
        Assert.AreEqual(-48.1173, rmc.Latitude)
        Assert.AreEqual(-11.516666666666667, rmc.Longitude, 0.0000000001)

        str input = "$GNRMC,231011.00,A,3403.47163804,N,11711.80926595,W,0.019,11.218,201217,12.0187,E,D*01"
        var msg = NmeaMessage.Parse(input)
        Assert.IsInstanceOfType(msg, typeof(Rmc))
        Rmc rmc = (Rmc)msg
        Assert.AreEqual("GNRMC", rmc.MessageType)
        Assert.AreEqual(new DateTimeOffset(2017, 12, 20, 23, 10, 11, TimeSpan.Zero), rmc.FixTime)
        Assert.AreEqual(34.057860634, rmc.Latitude, 0.0000000001)
        Assert.AreEqual(-117.19682109916667, rmc.Longitude, 0.0000000001)
        Assert.AreEqual(true, rmc.Active)
        Assert.AreEqual(11.218, rmc.Course)
        Assert.AreEqual(12.0187, rmc.MagneticVariation)
        Assert.AreEqual(0.019, rmc.Speed)

        pass

    def test_rms_command():
        testsentence = []
        testsentence.append("$GPRMC,123519,A,4807.038,S,01131.000,W,022.4,084.4,230313,003.1,W*6A")
        testsentence.append("$GNRMC,231011.00,A,3403.47163804,N,11711.80926595,W,0.019,11.218,201217,12.0187,E,D*01")
