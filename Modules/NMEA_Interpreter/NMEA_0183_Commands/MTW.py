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

namespace NmeaParser.Messages
{
    class MTW:
    def __init__(self):
        self.__WaterTemperature = 0.0
        
    def setWaterTemperature(self, temperature):
        self.__WaterTemperature = temperature
        
    def getWaterTemperature(self):
        return self.__WaterTemperature
    
    WaterTemperature = property(getWaterTemperature, setWaterTemperature)

# MTW command attributes
# 1. Water temperature (C)
#     - The water temperature measurement, in degrees Celsius. 
#     - The value can range from -273 to 65535, with a resolution of 0.1 degrees Celsius.

# Example usage:
mtw = MTW()
mtw.WaterTemperature = 22.3
print(mtw.WaterTemperature) # Output: 22.3

    
    # Course over ground and ground speed
    
    # <remarks>
    # The actual course and speed relative to the ground.
    # </remarks>
    [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Naming", "CA1704:IdentifiersShouldBeSpelledCorrectly", MessageId = "GPVTG")]
    [NmeaMessageType("--VTG")]
    public class Vtg : NmeaMessage
    {
        
        # Initializes a new instance of the <see cref="Vtg"/> class.
        
        # <param name="type">The message type</param>
        # <param name="message">The NMEA message values.</param>
        public Vtg(string type, string[] message) : base(type, message)
        {
            if (message == null || message.Length < 7)
                raise Exception("Invalid VTG: {}".message)

            CourseTrue = NmeaMessage.StringToDouble(message[0]);
            CourseMagnetic = NmeaMessage.StringToDouble(message[2]);
            SpeedKnots = NmeaMessage.StringToDouble(message[4]);
            SpeedKph = NmeaMessage.StringToDouble(message[6]);
        }

        
        #  Course over ground relative to true north
        
        public double CourseTrue { get; }

        
        #  Course over ground relative to magnetic north
        
        public double CourseMagnetic { get; }

        
        # Speed over ground in knots
        
        public double SpeedKnots { get; }

        
        # Speed over ground in kilometers/hour
        
        public double SpeedKph { get; }
    }
}