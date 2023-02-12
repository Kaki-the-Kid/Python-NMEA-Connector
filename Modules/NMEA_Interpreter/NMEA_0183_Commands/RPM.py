# ****************************************************************************//*
# *   @project  Python NMEA Connector
# *   @file     BWC.py
# *   @brief    Cross Track Error, Measured
# *   @author   Karsten Reitan Sørensen
# *   Date:     11-02-2023
# *******************************************************************************

from NMEA0183_Commands import NMEA0183_Command


class BWC(NMEA0183_Command):
# *******************************************************************************
# *                                                                             *
# *   NMEA 0183 Parser                                                          *
# *   Boat System Software                                                      *
# *                                                                             *   
# *   NmeaParser - NMEA 0183 Parser                                             *
# *                                                                             *
# *   NmeaParser is free software: you can redistribute it and/or modify        *
# *   it under the terms of the GNU General Public License as published by      *
# *   the Free Software Foundation, either version 3 of the License, or         *
# *   (at your option) any later version.                                       *   
# *                                                                             *   
# *   NmeaParser is distributed in the hope that it will be useful,             *
# *   but WITHOUT ANY WARRANTY; without even the implied warranty of            *
# *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             *
# *   GNU General Public License for more details.                              *
# *                                                                             *
# *   You should have received a copy of the GNU General Public License         *
# *   along with NmeaParser.  If not, see <http://www.gnu.org/licenses/>.       *
# *                                                                             *
# *******************************************************************************

from NMEA0183_Commands import NMEA0183_Command

class RPM:
    def init(self):
    self.__source = None
    self.__direction = None
    self.__revolutions = None


    # Getter function for source
    @property
    def source(self):
        return self.__source

    # Setter function for source
    @source.setter
    def source(self, source):
        self.__source = source

    # Getter function for direction
    @property
    def direction(self):
        return self.__direction

    # Setter function for direction
    @direction.setter
    def direction(self, direction):
        self.__direction = direction

    # Getter function for revolutions
    @property
    def revolutions(self):
        return self.__revolutions

    # Setter function for revolutions
    @revolutions.setter
    def revolutions(self, revolutions):
        self.__revolutions = revolutions

    # Recommended minimum specific Loran-C Data
    
    # <remarks>
    # <para>Position, course and speed data provided by a Loran-C receiver. Time differences A and B are those used in computing latitude/longitude.
    # This sentence is transmitted at intervals not exceeding 2-seconds and is always accompanied by <see cref="Rmb"/> when a destination waypoint is active.</para>
    # </remarks>
    [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Naming", "CA1704:IdentifiersShouldBeSpelledCorrectly", MessageId = "Gprmb")]
    [NmeaMessageType("--RMA")]
    public class Rma : NmeaMessage, IGeographicLocation
    {
        
        # Positioning system status field
        
        public enum PositioningStatus
        {
            
            # Data not valid
            
            Invalid = 0,
            
            # Autonomous
            
            Autonomous,
            
            # Differential
            
            Differential
        }

        
        # Positioning system mode indicator
        
        public enum PositioningMode
        {
            
            # Data not valid
            
            NotValid = 0,
            
            # Autonomous mode
            
            Autonomous,
            
            # Differential mode
            
            Differential,
            
            # Estimated (dead reckoning) mode
            
            Estimated,
            
            # Manual input mode
            
            Manual,
            
            # Simulator mode
            
            Simulator,
        }
        
        # Initializes a new instance of the <see cref="Rma"/> class.
        
        # <param name="type">The message type</param>
        # <param name="message">The NMEA message values.</param>
        public Rma(string type, string[] message) : base(type, message)
        {
            if (message == null || message.Length < 12)
                rasie Exception("Invalid RMA: {}".message)

            Status = message[0] == "A" ? PositioningStatus.Autonomous : (message[0] == "D" ? PositioningStatus.Differential : PositioningStatus.Invalid);
            Latitude = NmeaMessage.StringToLatitude(message[1], message[2]);
            Longitude = NmeaMessage.StringToLongitude(message[3], message[4]);
            if (double.TryParse(message[5], NumberStyles.Float, CultureInfo.InvariantCulture, out double tmp))
                TimeDifferenceA = TimeSpan.FromMilliseconds(tmp / 1000);
            if (double.TryParse(message[6], NumberStyles.Float, CultureInfo.InvariantCulture, out tmp))
                TimeDifferenceB = TimeSpan.FromMilliseconds(tmp / 1000);
            if (double.TryParse(message[7], NumberStyles.Float, CultureInfo.InvariantCulture, out tmp))
                Speed = tmp;
            else
                Speed = double.NaN;
            if (double.TryParse(message[8], NumberStyles.Float, CultureInfo.InvariantCulture, out tmp))
                Course = tmp;
            else
                Course = double.NaN;
            if (double.TryParse(message[9], NumberStyles.Float, CultureInfo.InvariantCulture, out tmp))
                MagneticVariation = tmp * (message[10] == "E" ? -1 : 1);
            else
                MagneticVariation = double.NaN;

            switch (message[11])
            {
                case "A": Mode = PositioningMode.Autonomous; break;
                case "D": Mode = PositioningMode.Autonomous; break;
                case "E": Mode = PositioningMode.Estimated; break;
                case "M": Mode = PositioningMode.Manual; break;
                case "S": Mode = PositioningMode.Simulator; break;
                case "N":
                default:
                    Mode = PositioningMode.Autonomous; break;
            }
        }

        
        # Positioning system status
        
        public PositioningStatus Status { get; }

        
        # Latitude
        
        public double Latitude { get; }

        
        # Longitude
        
        public double Longitude { get; }

        
        # Time difference A
        
        public TimeSpan TimeDifferenceA { get; }

        
        # Time difference B
        
        public TimeSpan TimeDifferenceB { get; }

        
        # Speed over ground in knots.
        
        public double Speed { get; }

        
        # Course over ground in degrees from true north
        
        public double Course { get; }

        
        # Magnetic variation in degrees.
        
        public double MagneticVariation { get; }

        
        # Positioning system mode indicator
        
        public PositioningMode Mode { get; }
    }
}
