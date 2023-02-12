# ****************************************************************************//*
# *   @project  Python NMEA Connector
# *   @file     RSD.py
# *   @brief    Radar System Data
# *   @author   Karsten Reitan Sørensen
# *   Date:     11-02-2023
# *******************************************************************************
# <para>Position, course and speed data provided by a Loran-C receiver. Time differences A and B are those used in computing latitude/longitude.
# This sentence is transmitted at intervals not exceeding 2-seconds and is always accompanied by <see cref="Rmb"/> when a destination waypoint is active.</para>

from NMEA0183_Commands import NMEA0183_Command as NmeaMessage


class RSD(NmeaMessage):
    
    def __init__(self, NMEAMessage):
        self.__data = {
            "sensor_id": None,
            "data_valid": None,
            "speed": None,
            "course": None,
            "range": None,
            "bearing": None
        }
        # Positioning system status
        public PositioningStatus Status { get; }

        # Latitude
        public double Latitude { get; }

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

    
    @property
    def sensor_id(self):
        return self.__data["sensor_id"]
    
    @sensor_id.setter
    def sensor_id(self, sensor_id):
        self.__data["sensor_id"] = sensor_id
        
    @property
    def data_valid(self):
        return self.__data["data_valid"]
    
    @data_valid.setter
    def data_valid(self, data_valid):
        self.__data["data_valid"] = data_valid
        
    @property
    def speed(self):
        return self.__data["speed"]
    
    @speed.setter
    def speed(self, speed):
        self.__data["speed"] = speed
        
    @property
    def course(self):
        return self.__data["course"]
    
    @course.setter
    def course(self, course):
        self.__data["course"] = course
        
    @property
    def range(self):
        return self.__data["range"]
    
    @range.setter
    def range(self, range):
        self.__data["range"] = range
        
    @property
    def bearing(self):
        return self.__data["bearing"]
    
    @bearing.setter
    def bearing(self, bearing):
        self.__data["bearing"] = bearing



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


    # Positioning system status field
    def PositioningStatus(Enum):
        # Data not valid
        Invalid = 0,
        # Autonomous
        Autonomous,
        # Differential
        Differential

    # Positioning system mode indicator
    def PositioningMode(Enum):
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






    # Recommended minimum specific Loran-C Data
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
