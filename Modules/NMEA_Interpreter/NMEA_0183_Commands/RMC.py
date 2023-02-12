# ****************************************************************************//*
# *   @project  Python NMEA Connector
# *   @file     BWC.py
# *   @brief    Cross Track Error, Measured
# *   @author   Karsten Reitan Sørensen
# *   Date:     11-02-2023
# *******************************************************************************

from NMEA0183_Commands import NMEA0183_Command


class BWC(NMEA0183_Command):
#  *******************************************************************************
#  *  Licensed under the Apache License, Version 2.0 (the "License");
#  *  you may not use this file except in compliance with the License.
#  *  You may obtain a copy of the License at
#  *
#  *  http://www.apache.org/licenses/LICENSE-2.0
#  *
#  *   Unless required by applicable law or agreed to in writing, software
#  *   distributed under the License is distributed on an "AS IS" BASIS,
#  *   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  *   See the License for the specific language governing permissions and
#  *   limitations under the License.
#  ******************************************************************************

from NMEA0183_Commands import NMEA0183_Command

using System;
using System.Globalization;

namespace NmeaParser.Messages
{
    class RMC:
    def __init__(self):
        self.time = None
        self.status = None
        self.latitude = None
        self.latitude_direction = None
        self.longitude = None
        self.longitude_direction = None
        self.speed = None
        self.track_angle = None
        self.date = None
        self.magnetic_variation = None
        self.magnetic_variation_direction = None
        self.mode_indicator = None
        
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
        return self.mode_indicator

    class RMC:
    def __init__(self):
        self.time = ""
        self.status = ""
        self.latitude = 0.0
        self.latitude_direction = ""
        self.longitude = 0.0
        self.longitude_direction = ""
        self.speed = 0.0
        self.course = 0.0
        self.date = ""
        self.magnetic_variation = 0.0
        self.magnetic_variation_direction = ""
        self.mode = ""

    # setters
    def set_time(self, time):
        self.time = time

    def set_status(self, status):
        self.status = status

    def set_latitude(self, latitude):
        self.latitude = latitude

    def set_latitude_direction(self, latitude_direction):
        self.latitude_direction = latitude_direction

    def set_longitude(self, longitude):
        self.longitude = longitude

    def set_longitude_direction(self, longitude_direction):
        self.longitude_direction = longitude_direction

    def set_speed(self, speed):
        self.speed = speed

    def set_course(self, course):
        self.course = course

    def set_date(self, date):
        self.date = date

    def set_magnetic_variation(self, magnetic_variation):
        self.magnetic_variation = magnetic_variation

    def set_magnetic_variation_direction(self, magnetic_variation_direction):
        self.magnetic_variation_direction = magnetic_variation_direction

    def set_mode(self, mode):
        self.mode = mode

    # getters
    def get_time(self):
        return self.time

    def get_status(self):
        return self.status

    def get_latitude(self):
        return self.latitude

    def get_latitude_direction(self):
        return self.latitude_direction

    def get_longitude(self):
        return self.longitude

    def get_longitude_direction(self):
        return self.longitude_direction

    def get_speed(self):
        return self.speed

    def get_course(self):
        return self.course

    def get_date(self):
        return self.date

    def get_magnetic_variation(self):
        return self.magnetic_variation

    def get_magnetic_variation_direction(self):
        return self.magnetic_variation_direction

    def get_mode(self):
        return self.mode

    
    # Recommended Minimum specific GNSS data
    
    # <remarks>
    # <para>Time, date, position, course and speed data provided by a GNSS navigation receiver. This sentence is
    # transmitted at intervals not exceeding 2-seconds and is always accompanied by <see cref="Rmb"/> when a destination waypoint
    # is active.</para>
    # <para><see cref="Rmc"/> and <see cref="Rmb"/> are the recommended minimum data to be provided by a GNSS receiver.</para>
    # </remarks>
    [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Naming", "CA1704:IdentifiersShouldBeSpelledCorrectly", MessageId = "Gprmc")]
    [NmeaMessageType("--RMC")]
    public class Rmc : NmeaMessage, ITimestampedMessage, IGeographicLocation
    {
        
        # Initializes a new instance of the <see cref="Rmc"/> class.
        
        # <param name="type">The message type</param>
        # <param name="message">The NMEA message values.</param>
        public Rmc(string type, string[] message) : base(type, message)
        {
            if (message == null || message.Length < 11):
                raise Exception("Invalid RMC: {}".message)
            
            if (message[8].Length == 6 && message[0].Length >= 6)
            {
                FixTime = new DateTimeOffset(int.Parse(message[8].Substring(4, 2), CultureInfo.InvariantCulture) + 2000,
                                       int.Parse(message[8].Substring(2, 2), CultureInfo.InvariantCulture),
                                       int.Parse(message[8].Substring(0, 2), CultureInfo.InvariantCulture),
                                       int.Parse(message[0].Substring(0, 2), CultureInfo.InvariantCulture),
                                       int.Parse(message[0].Substring(2, 2), CultureInfo.InvariantCulture),
                                       0, TimeSpan.Zero).AddSeconds(double.Parse(message[0].Substring(4), CultureInfo.InvariantCulture));
            }
            Active = (message[1] == "A");
            Latitude = NmeaMessage.StringToLatitude(message[2], message[3]);
            Longitude = NmeaMessage.StringToLongitude(message[4], message[5]);
            Speed = NmeaMessage.StringToDouble(message[6]);
            Course = NmeaMessage.StringToDouble(message[7]);
            MagneticVariation = NmeaMessage.StringToDouble(message[9]);            
            if (!double.IsNaN(MagneticVariation) && message[10] == "W")
                MagneticVariation *= -1;
        }

        
        # Fix Time
        
        public DateTimeOffset FixTime { get; }

        
        # Gets a value whether the device is active
        
        public bool Active { get; }

        
        # Latitude
        
        public double Latitude { get; }

        
        # Longitude
        
        public double Longitude { get; }

        
        # Speed over the ground in knots
        
        public double Speed { get; }

        
        # Track angle in degrees True
        
        public double Course { get; }

        
        # Magnetic Variation
        
        public double MagneticVariation { get; }

        TimeSpan ITimestampedMessage.Timestamp => FixTime.TimeOfDay;
    }
}
