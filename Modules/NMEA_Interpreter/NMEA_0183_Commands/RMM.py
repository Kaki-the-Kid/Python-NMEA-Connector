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
# Title: NMEA 0183 RMM Command

# Description: RMM Command

# Generated: 2018-04-06 11:34:50.00000

# *******************************************************************************

from NMEA0183_Commands import NMEA0183_Command

# *******************************************************************************
# RMM - Recommended minimum navigation information
# *******************************************************************************
class RMM(NMEA_Command):
    
    class RMM:
    def __init__(self):
        self.__mode_indicator = None
        self.__cross_track_error = None
        self.__direction_to_steer = None
        self.__arrival_circle_entered = None
    
    def set_mode_indicator(self, mode_indicator):
        self.__mode_indicator = mode_indicator

    def get_mode_indicator(self):
        return self.__mode_indicator

    def set_cross_track_error(self, cross_track_error):
        self.__cross_track_error = cross_track_error

    def get_cross_track_error(self):
        return self.__cross_track_error

    def set_direction_to_steer(self, direction_to_steer):
        self.__direction_to_steer = direction_to_steer

    def get_direction_to_steer(self):
        return self.__direction_to_steer

    def set_arrival_circle_entered(self, arrival_circle_entered):
        self.__arrival_circle_entered = arrival_circle_entered

    def get_arrival_circle_entered(self):
        return self.__arrival_circle_entered



# Make setter and getter forr each field
    def __init__(self):
        self.__status = None
        self.__latitude = None
        self.__longitude = None
        self.__time_difference_A = None
        self.__time_difference_B = None
        self.__speed = None
        self.__course = None
        self.__magnetic_variation = None
        self.__mode = None
        
    @property   
    def status(self):
        return self.__status    
    
    @status.setter          
                    
                    
namespace NmeaParser.Messages
{
    
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
