# ****************************************************************************//*
# *   @project  Python NMEA Connector
# *   @file     GNS.py
# *   @brief    GNSS fix data
# *   @author   Karsten Reitan Sørensen
# *   Date:     11-02-2023
# ****************************************************************************************//*
# Fixes data for single or combined (GPS, GLONASS, possible future satellite systems, and 
# systems combining these) satellite navigation systems

# This sentence provides fix data for GPS, GLONASS, BDS, QZSS, NavIC (IRNSS) and possible future satellite systems, and systems combining these.
# This sentence could be used with the talker identification of <see cref="Talker.GlobalPositioningSystem"/> for GPS, <see cref="Talker.GlonassReceiver"/> for GLONASS,
# <see cref="Talker.GalileoPositioningSystem"/> for Galileo, <see cref="Talker.BeiDouNavigationSatelliteSystem"/> for BDS, <see cref="Talker.QuasiZenithSatelliteSystem"/> for QZSS,
# <see cref="Talker.IndianRegionalNavigationSatelliteSystem"/> for NavIC (IRNSS), and <see cref="Talker.GlobalNavigationSatelliteSystem"/> for GNSS combined systems, as well as future identifiers.
# 
# If a GNSS receiver is capable simultanously of producing a position using combined satellite systems, as well as a position using only one of the satellite systems, then separate GNS sentences
# with different <see cref="NmeaMessage.TalkerId"/> may be used to report the data calculated from the individual systems.
# 
# If a GNSS receiver is set up to use more than one satellite system, but for some reason one or more of the systems are not available, then it may continue to report the positions
# using <c>GNGNS</c>, and use the <see cref="GpsModeIndicator"/> to show which satellit esystems are being used.
# 
# Example of GNS messages:
# $GNGNS,014035.00,4332.69262,S,17235.48549,E,RR,13,0.9,25.63,11.24,,*70   //GLONASS
# $GPGNS,014035.00,,,,,,8,,,,1.0,23*76                                     //GPS
# $GLGNS,014035.00,,,,,,5,,,,1.0,23*67                                     //GALILEO
# $GNGNS,014035.00,,,,,,8,,,,1.0,23*6A                                     //GNSS
#
# *******************************************************************************

from NMEA0183_Commands import NMEA0183_Commandb as NMEAMessage


class GNS(NMEAMessage):
    
    def __init__(self, NMEAMessage):
        self._NMEAMessage = NMEAMessage
        if (NMEAMessage == None or NMEAMessage.Length < 12):
            raise Exception("Invalid GNS: {}".NMEAMessage)
        
        FixTime = StringToTimeSpan(NMEAMessage[0])
        Latitude = NmeaMessage.StringToLatitude(NMEAMessage[1], NMEAMessage[2])
        Longitude = NmeaMessage.StringToLongitude(NMEAMessage[3], NMEAMessage[4])
        ModeIndicators = NMEAMessage[5].Select(t => ParseModeIndicator(t)).ToArray()
        NumberOfSatellites = int.Parse(NMEAMessage[6], CultureInfo.InvariantCulture)
        Hdop = NmeaMessage.StringTofloat(NMEAMessage[7])
        OrthometricHeight = NmeaMessage.StringTofloat(NMEAMessage[8])
        GeoidalSeparation = NmeaMessage.StringTofloat(NMEAMessage[9])
        var timeInSeconds = StringTofloat(NMEAMessage[10])
        
        if (not float.IsNaN(timeInSeconds)):
            TimeSinceLastDgpsUpdate = TimeSpan.FromSeconds(timeInSeconds)
        else:
            TimeSinceLastDgpsUpdate = null
            
        if (NMEAMessage[11].Length > 0):
            DgpsStationId = NMEAMessage[11]

        if (NMEAMessage.Length > 12):
            match (NMEAMessage[12]):
                case "S": 
                    Status = NavigationalStatus.Safe 

                case "C": 
                    Status = NavigationalStatus.Caution 

                case "U": 
                    Status = NavigationalStatus.Unsafe 

                case "V":
                    Status = NavigationalStatus.NotValid 

                case _: 
                    Status = NavigationalStatus.NotValid 
    # Latitude
    def float Latitude { get }

    # Longitude
    def float Longitude { get }

    # Mode indicator for GPS
    def Mode GpsModeIndicator => ModeIndicators.Length > 0 ? ModeIndicators[0] : Mode.NoFix

    # Mode indicator for GLONASS
    def Mode GlonassModeIndicator => ModeIndicators.Length > 1 ? ModeIndicators[1] : Mode.NoFix

    # Mode indicator for Galileo
    def Mode GalileoModeIndicator => ModeIndicators.Length > 2 ? ModeIndicators[2] : Mode.NoFix

    # Mode indicator for Beidou (BDS)
    def Mode BDSModeIndicator => ModeIndicators.Length > 3 ? ModeIndicators[3] : Mode.NoFix

    # Mode indicator for QZSS
    def Mode QZSSModeIndicator => ModeIndicators.Length > 4 ? ModeIndicators[4] : Mode.NoFix

    # Mode indicator for NavIC (IRNSS)
    def Mode NavICModeIndicator => ModeIndicators.Length > 5 ? ModeIndicators[5] : Mode.NoFix

    # Mode indicator for future constallations
    def Mode[] ModeIndicators { get }

    # Number of satellites (SVs) in use
    def int NumberOfSatellites { get }

    # Horizontal Dilution of Precision (HDOP), calculated using all the satellites (GPS, GLONASS, and any future satellites) used in computing the solution reported in each GNS sentence.
    [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Naming", "CA1704:IdentifiersShouldBeSpelledCorrectly", MessageId = "Hdop")]
    def float Hdop { get }

    # Orthometric height in meters (MSL reference)
    def float OrthometricHeight { get }

    # Geoidal separation in meters - the difference between the earth ellipsoid surface and mean-sea-level (geoid) surface defined by the reference datum used in the position solution<br/>
    # '-' = mean-sea-level surface below ellipsoid.
    def float GeoidalSeparation { get }

    #  Age of differential data - <see cref="TimeSpan.MaxValue"/> if talker ID is GN, additional GNS messages follow with GP and/or GL Age of differential data
    def TimeSpan? TimeSinceLastDgpsUpdate { get }

    # eference station ID1, range 0000-4095 - Null if talker ID is GN, additional GNS messages follow with GP and/or GL Reference station ID
    def str DgpsStationId { get }

    # Navigational status
    def NavigationalStatus Status { get }

    @property
    def time(self):
        return self.data[0]
    
    @time.setter
    def time(self, value):
        self.data[0] = value
        
    @property
    def lat(self):
        return self.data[1]
    
    @lat.setter
    def lat(self, value):
        self.data[1] = value
        
    @property
    def lat_dir(self):
        return self.data[2]
    
    @lat_dir.setter
    def lat_dir(self, value):
        self.data[2] = value
        
    @property
    def lon(self):
        return self.data[3]
    
    @lon.setter
    def lon(self, value):
        self.data[3] = value
        
    @property
    def lon_dir(self):
        return self.data[4]
    
    @lon_dir.setter
    def lon_dir(self, value):
        self.data[4] = value
        
    @property
    def mode_indicator(self):
        return self.data[5]
    
    @mode_indicator.setter
    def mode_indicator(self, value):
        self.data[5] = value
        
    @property
    def total_satellites_used(self):
        return self.data[6]
    
    @total_satellites_used.setter
    def total_satellites_used(self, value):
        self.data[6] = value
        
    @property
    def HDOP(self):
        return self.data[7]
    
    @HDOP.setter
    def HDOP(self, value):
        self.data[7] = value
        
    @property
    def altitude(self):
        return self.data[8]
    
    @altitude.setter
    def altitude(self, value):
        self.data[8] = value
        
    @property
    def altitude_units(self):
        return self.data[9]
    
    @altitude_units.setter
    def altitude_units(self, value):
        self.data[9] = value
        
    @property
    def geoidal_separation(self):
        return self.data[10]
    
    @geoidal_separation.setter
    def geoidal_separation(self, value):
        self.data[10] = value
        
    @property
    def geoidal_separation_units(self):
        return self.data[11]
    
    @geoidal_separation_units.setter
    def geoidal_separation_units(self, value):
        self.data[11] = value
        
    @property
    def age_of_differential_data(self):
        return self.data[12]
    



    # GNS Mode Indicator
    def Mode(Enum):
        # No fix. Satellite system not used in position fix, or fix not valid
        NoFix,
        # Autonomous. Satellite system used in non-differential mode in position fix
        Autonomous,
        # Differential (including all OmniSTAR services). Satellite system used in differential mode in position fix
        Differential,
        # Precise. Satellite system used in precision mode. Precision mode is defined as no deliberate degradation (such as Selective Availability) and higher resolution code (P-code) is used to compute position fix.
        Precise,
        #  Real Time Kinematic. Satellite system used in RTK mode with fixed integers
        RealTimeKinematic,
        # Float RTK. Satellite system used in real time kinematic mode with floating integers
        FloatRtk,
        # Estimated (dead reckoning) mode
        Estimated,
        # Manual input mode
        Manual,
        # Simulator mode

    # Navigational status
    def NavigationalStatus(Enum):
        # Navigational status not valid, equipment is not providing navigational status indication.
        NotValid = 0,
        # Safe: When the estimated positioning accuracy (95% confidence) is within the selected accuracy level corresponding
        # to the actual navigation mode, and integrity is available and within the requirements for the actual navigation mode,
        # and a new valid position has been calculated within 1s for a conventional craft, and 0.5s for a high speed craft.
        Safe = 3,
        # Caution: When integrity is not available
        Caution = 2,
        # Unsafe When the estimated positioning accuracy (95% confidence) is less than the selected accuracy level corresponding
        # to the actual navigation mode, and integrity is available and within the requirements for the actual navigation mode,
        # and/or a new valid position has not been calculated within 1s for a conventional craft, and 0.5s for a high speed craft.
        Unsafe = 1

    @staticmethod
    def ParseModeIndicator(c):
        match c:
            case 'A': return Mode.Autonomous
            case 'D': return Mode.Differential
            case 'P': return Mode.Precise
            case 'R': return Mode.RealTimeKinematic
            case 'F': return Mode.FloatRtk
            case 'E': return Mode.Estimated
            case 'M': return Mode.Manual
            case 'S': return Mode.Simulator
            case 'N': return Mode.NoFix
            case _:   return Mode.NoFix


    def GNS(str type, str[] NMEAMessage): pass
    # Time of day fix was taken
    def TimeSpan FixTime { get }
    

    TimeSpan ITimestampedMessage.Timestamp => FixTime
