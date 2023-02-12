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
    # example usage
    #    hdt = HDT()
    #    print(hdt)
    #    hdt.set_heading(120.0)
    #    hdt.set_reference('M')
    #    print(hdt)
    
    class HDT:
    def __init__(self, heading=0.0, reference='T'):
        self.heading = heading
        self.reference = reference
        
    def get_heading(self):
        return self.heading
    
    def set_heading(self, heading):
        self.heading = heading
        
    def get_reference(self):
        return self.reference
    
    def set_reference(self, reference):
        self.reference = reference
        
    def __str__(self):
        return 'HDT: Heading: {}, Reference: {}'.format(self.heading, self.reference)



    
    # Dual Ground/Water Distance
    
    # <remarks>
    # The distance traveled, relative to the water and over the ground.
    # </remarks>
    [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Naming", "CA1704:IdentifiersShouldBeSpelledCorrectly", MessageId = "Dtm")]
    [NmeaMessageType("--VLW")]
    public class Vlw : NmeaMessage
    {
        
        # Initializes a new instance of the <see cref="Vlw"/> class.
        
        # <param name="type">The message type</param>
        # <param name="message">The NMEA message values.</param>
        public Vlw (string type, string[] message) : base(type, message)
        {
            if (message == null || message.Length < 7):
                raise Exception("Invalid VLW: {}".message)

            WaterDistanceCumulative = NmeaMessage.StringToDouble(message[0]);
            WaterDistanceSinceReset = NmeaMessage.StringToDouble(message[2]);
            GroundDistanceCumulative = NmeaMessage.StringToDouble(message[4]);
            GroundDistanceSinceReset = NmeaMessage.StringToDouble(message[6]);
        }
		
		Total cumulative water distance, nautical miles</summary>
        public double WaterDistanceCumulative { get; }
		
		Water distance since reset, nautical miles</summary>
        public double WaterDistanceSinceReset { get; }
		
		Total cumulative ground distance, nautical miles</summary>
        public double GroundDistanceCumulative { get; }
		
		Ground distance since reset, nautical miles</summary>
        public double GroundDistanceSinceReset { get; }
    }
}