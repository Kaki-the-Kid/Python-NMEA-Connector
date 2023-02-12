# ****************************************************************************//*
# *   @project  Python NMEA Connector
# *   @file     RSD.py
# *   @brief    Radar System Data
# *   @author   Karsten Reitan Sørensen
# *   Date:     11-02-2023
# *******************************************************************************

from NMEA0183_Commands import NMEA0183_Command as NMEAMessage


class GGA(NMEAMessage):
    
    def __init__(self, NMEAMessage):
        if (NMEAMessage == null or NMEAMessage.Length < 14):
            raise Exception("Invalid GGA: {}".NMEAMessage)
        
        self._time = None
        
        #/ Latitude
        self.__latitude = None
        #def double Latitude { get }
        
        Latitude = NMEAMessage.StringToLatitude(NMEAMessage[1], NMEAMessage[2])
        self.__latitude_indicator = None

        #/ Longitude
        self.__longitude = None
        Longitude = NMEAMessage.StringToLongitude(NMEAMessage[3], NMEAMessage[4])
        #def double Longitude { get }

        self.__longitude_indicator = None
        
        # Fix Quality
        self.__fix_quality = None
        if (not string.IsNullOrEmpty(NMEAMessage[5])):
            Quality =  (Gga.FixQuality)int.Parse(NMEAMessage[5], CultureInfo.InvariantCulture)
        #def Gga.FixQuality Quality { get }

        self.__number_of_satellites = None
        if (mot string.IsNullOrEmpty(NMEAMessage[6])):
            NumberOfSatellites = int.Parse(NMEAMessage[6], CultureInfo.InvariantCulture)
        self.__horizontal_dilution = None
        Hdop = NMEAMessage.StringToDouble(NMEAMessage[7])
        self.__altitude = None
        Altitude = NMEAMessage.StringToDouble(NMEAMessage[8])
        self.__altitude_unit = None
        AltitudeUnits = NMEAMessage[9]
        self.__geoidal_separation = None
        GeoidalSeparation = NMEAMessage.StringToDouble(NMEAMessage[10])
        self.__geoidal_separation_unit = None
        GeoidalSeparationUnits = NMEAMessage[11]            
        self.__age_of_dgps_data = None
        if (not double.IsNaN(timeInSeconds)):
            TimeSinceLastDgpsUpdate = TimeSpan.FromSeconds(timeInSeconds)
        else:
            TimeSinceLastDgpsUpdate = null
        self.__dgps_station_id = None
        if (NMEAMessage[13].Length > 0):
            DgpsStationId = int.Parse(NMEAMessage[13], CultureInfo.InvariantCulture)
        else:
            DgpsStationId = -1




    #/ Number of satellites being tracked
    def int NumberOfSatellites { get }

    #/ Horizontal Dilution of Precision
    [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Naming", "CA1704:IdentifiersShouldBeSpelledCorrectly", MessageId = "Hdop")]
    def double Hdop { get }

    #/ Altitude
    def double Altitude { get }

    #/ Altitude units ('M' for Meters)
    def string AltitudeUnits { get }

    #/ Geoidal separation: the difference between the WGS-84 earth ellipsoid surface and mean-sea-level (geoid) surface.
    #/ <remarks>
    #/ A negative value means mean-sea-level surface is below the WGS-84 ellipsoid surface.
    #/ </remarks>
    #/ <seealso cref="GeoidalSeparationUnits"/>
    def double GeoidalSeparation { get }

    #/ <summary>
    #/ Altitude units ('M' for Meters)
    #/ </summary>
    def string GeoidalSeparationUnits { get }

    #/ <summary>
    #/ Time since last DGPS update (ie age of the differential GPS data)
    #/ </summary>
    def TimeSpan? TimeSinceLastDgpsUpdate { get }

    #/ <summary>
    #/ Differential Reference Station ID
    #/ </summary>
    def int DgpsStationId { get }

            
        FixTime = StringToTimeSpan(NMEAMessage[0])
        timeInSeconds = StringToDouble(NMEAMessage[12])
        
            
    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        self._time = value

    @property
    def latitude(self):
        return self.__latitude

    @latitude.setter
    def latitude(self, value):
        self.__latitude = value

    @property
    def latitude_indicator(self):
        return self.__latitude_indicator

    @latitude_indicator.setter
    def latitude_indicator(self, value):
        self.__latitude_indicator = value

    @property
    def longitude(self):
        return self.__longitude

    @longitude.setter
    def longitude(self, value):
        self.__longitude = value

    @property
    def longitude_indicator(self):
        return self.__longitude_indicator

    @longitude_indicator.setter
    def longitude_indicator(self, value):
        self.__longitude_indicator = value

    @property
    def fix_quality(self):
        return self.__fix_quality

    @fix_quality.setter
    def fix_quality(self, value):
        self.__fix_quality = value

    @property
    def number_of_satellites(self):
        return self.__number_of_satellites

    @number_of_satellites.setter
    def number_of_satellites(self, value):
        self.__number_of_satellites = value

    @property
    def horizontal_dilution(self):
        return self.__horizontal_dilution

    @horizontal_dilution.setter
    def horizontal_dilution(self, value):
        self.__horizontal_dilution = value

    @property
    def altitude(self):
        return self.__altitude

    @altitude.setter
    def altitude(self, value):
        self.__altitude = value

    @property
    def altitude_unit(self):
        return self.__altitude_unit

    @altitude_unit.setter
    def altitude_unit(self, value):
        self.__altitude_unit = value

    @property
    def geoidal_separation(self):
        return self.__


    #/ Time of day fix was taken
    def TimeSpan FixTime { get }

    TimeSpan ITimestampedMessage.Timestamp => FixTime

    #/ <summary>
    #/ Fix quality indicater
    #/ </summary>
    def FixQuality(Enum):
        #/ <summary>Fix not available or invalid</summary>
        Invalid = 0,
        #/ <summary>GPS SPS Mode, fix valid</summary>
        GpsFix = 1,
        #/ <summary>Differential GPS, SPS Mode, or Satellite Based Augmentation System (SBAS), fix valid</summary>
        [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Naming", "CA1704:IdentifiersShouldBeSpelledCorrectly", MessageId = "Dgps")]
        DgpsFix = 2,
        #/ <summary>GPS PPS (Precise Positioning Service) mode, fix valid</summary>
        [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Naming", "CA1704:IdentifiersShouldBeSpelledCorrectly", MessageId = "Pps")]
        PpsFix = 3,
        #/ <summary>Real Time Kinematic (Fixed). System used in RTK mode with fixed integers</summary>
        [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Naming", "CA1704:IdentifiersShouldBeSpelledCorrectly", MessageId = "Rtk")]
        Rtk = 4,
        #/ <summary>Real Time Kinematic (Floating). Satellite system used in RTK mode, floating integers</summary>
        [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Naming", "CA1704:IdentifiersShouldBeSpelledCorrectly", MessageId = "Rtk")]
        FloatRtk = 5,
        #/ <summary>Estimated (dead reckoning) mode</summary>
        Estimated = 6,
        #/ <summary>Manual input mode</summary>
        ManualInput = 7,
        #/ <summary>Simulator mode</summary>
        Simulation = 8