# ****************************************************************************//*
# *   @project  Python NMEA Connector
# *   @file     RMA.py
# *   @brief    Recommended minimum navigation information
# *   @author   Karsten Reitan Sørensen
# *   Date:     11-02-2023
# *******************************************************************************
# Recommended minimum specific Loran-C Data
# Position, course and speed data provided by a Loran-C receiver. Time differences A and B are 
# those used in computing latitude/longitude. # This sentence is transmitted at intervals not 
# exceeding 2-seconds and is always accompanied by RMB when a destination waypoint is active.
#
# Examples
# $GPRMA,A,4917.24,N,12310.6,W,002.5,054.7,191194,004.2,W*72
# In this example, the RMA command provides information about the recommended minimum 
# navigation information. The first field, "A", indicates that the data is valid. The second 
# and third fields give the latitude and longitude of the navigation target, respectively. 
# The fourth field is the navigation target bearing in true degrees, the fifth field is the 
# navigation target speed in knots, and the sixth field is the UTC date of the fix. The seventh 
# field gives the magnetic variation, and the last field gives the direction of magnetic variation.
#
# $GPRMA,V,4917.24,N,12310.6,W,002.5,054.7,191194,004.2,W*6A
# In this example, the first field "V" indicates that the data is invalid. This means that the 
# navigation target information provided in the rest of the fields should be ignored.
# 
# $GPRMA,A,5017.89,N,07902.14,W,013.7,051.3,010795,001.5,W*75
# In this example, the RMA command provides similar information to the first example, but with 
# different values for the attributes. The first field is "A", indicating that the data is valid. 
# The second and third fields give the latitude and longitude of the navigation target, respectively. 
# The fourth field is the navigation target bearing in true degrees, the fifth field is the 
# navigation target speed in knots, and the sixth field is the UTC date of the fix. The seventh 
# field gives the magnetic variation, and the last field gives the direction of magnetic variation.
# *******************************************************************************

from NMEA0183_Commands import NMEA0183_Command


class RMA(NMEA0183_Command):
    
    def __init__(self, sentence):
        self._datasentence = sentence.split(",")
        if (self._datasentence == None or self._datasentence.Length < 12):
            raise Exception("Invalid RMA: {}".sentence)

        # Positioning system mode indicator
        # Positioning system status
        self.status = status
        Status = self._datasentence[0] == "A" ? PositioningStatus.Autonomous : (self._datasentence[0] == "D" ? PositioningStatus.Differential : PositioningStatus.Invalid)
        # Positioning system status field
        def PositioningStatus(Enum):
            # Data not valid
            Invalid = 0,
            # Autonomous
            Autonomous = 1,
            # Differential
            Differential = 2,
        #def PositioningStatus Status { get }
        
        # Positioning system mode indicator
        match self._datasentence[11]:
            case "A": Mode = PositioningMode.Autonomous
            case "D": Mode = PositioningMode.Autonomous
            case "E": Mode = PositioningMode.Estimated
            case "M": Mode = PositioningMode.Manual
            case "S": Mode = PositioningMode.Simulator
            case "N":
                Mode = PositioningMode.Autonomous
            case _:
                Mode = PositioningMode.Autonomous
        self.pos_mode = pos_mode
        
        def PositioningMode(Enum):
            # Data not valid
            NotValid = 0,
            # Autonomous mode
            Autonomous = 1,
            # Differential mode
            Differential = 2,
            # Estimated (dead reckoning) mode
            Estimated = 3,
            # Manual input mode
            Manual = 4,
            # Simulator mode
            Simulator = 5,
        #def PositioningMode Mode { get }
        
        # Latitude
        self.lat = lat
        self.lat_dir = lat_dir
        Latitude = NmeaMessage.StringToLatitude(self._datasentence[1], self._datasentence[2])
        #def double Latitude { get }
        
        # Longitude
        self.lon = lon
        self.lon_dir = lon_dir
        Longitude = NmeaMessage.StringToLongitude(self._datasentence[3], self._datasentence[4])
        #def double Longitude { get }
        
        # Time difference A
        TimeDifferenceA = TimeSpan.FromMilliseconds( float(self._datasentence[5]) / 1000)
        #def TimeSpan TimeDifferenceA { get }

        # Time difference B
        TimeDifferenceB = TimeSpan.FromMilliseconds( float(self._datasentence[6]) / 1000 )
        #def TimeSpan TimeDifferenceB { get }

        # Speed over ground in knots.
        Speed = float(self._datasentence[7])
        self.sog = sog
        #def double Speed { get }
        
        # Course over ground in degrees from true north
        if ( float(self._datasentence[8], out tmp) ):
            Course = tmp
        else:
            Course = double.NaN
        self.cog = cog
        #def double Course { get }
        
        self.hdg = hdg
        
        # Magnetic variation in degrees.
        if ( float(self._datasentence[9], out tmp) ):
            MagneticVariation = tmp * (self._datasentence[10] == "E" ? -1 : 1)
        else:
            MagneticVariation = double.NaN
        self.mv = mv
        #def double MagneticVariation { get }
        self.mv_dir = mv_dir

    def get_status(self):
        return self.status
    
    def set_status(self, status):
        self.status = status
    
    def get_pos_mode(self):
        return self.pos_mode
    
    def set_pos_mode(self, pos_mode):
        self.pos_mode = pos_mode
    
    def get_lat(self):
        return self.lat
    
    def set_lat(self, lat):
        self.lat = lat
    
    def get_lat_dir(self):
        return self.lat_dir
    
    def set_lat_dir(self, lat_dir):
        self.lat_dir = lat_dir
    
    def get_lon(self):
        return self.lon
    
    def set_lon(self, lon):
        self.lon = lon
    
    def get_lon_dir(self):
        return self.lon_dir
    
    def set_lon_dir(self, lon_dir):
        self.lon_dir = lon_dir
    
    def get_sog(self):
        return self.sog
    
    def set_sog(self, sog):
        self.sog = sog
    
    def get_cog(self):
        return self.cog
    
    def set_cog(self, cog):
        self.cog = cog
    
    def get_hdg(self):
        return self.hdg
    
    def set_hdg(self, hdg):
        self.hdg = hdg
    
    def get_mv(self):
        return self.mv
    
    def set_mv(self, mv):
        self.mv = mv
    
    def get_mv_dir(self):
        return self.mv_dir
    
    def set_mv_dir(self, mv_dir):
        self.mv_dir = mv_dir

    def get_command(self):
        return "$GPRMA"
    
    def test_command(self):
        _teststring =[]
        _teststring.append("$GPRMA,A,4917.24,N,12310.6,W,002.5,054.7,191194,004.2,W*72")
        _teststring.append("$GPRMA,V,4917.24,N,12310.6,W,002.5,054.7,191194,004.2,W*6A")
        _teststring.append("$GPRMA,A,5017.89,N,07902.14,W,013.7,051.3,010795,001.5,W*75")
        
        return _teststring
