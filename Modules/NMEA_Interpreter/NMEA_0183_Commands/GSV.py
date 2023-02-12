# ****************************************************************************//*
# *   @project  Python NMEA Connector
# *   @file     GSV.py
# *   @brief    GNSS Satellites in view
# *   @author   Karsten Reitan Sørensen
# *   Date:     11-02-2023
# *******************************************************************************

from NMEA0183_Commands import NMEA0183_Command as NMEAMessage


class GSV(NMEAMessage):
    
    def __init__(self, NMEAMessage n_messages, message_number, satellites_in_view, satellite_data):
        if (NMEAMessage == None or NMEAMessage.Length < 3):
            raise Exception("Invalid GSV: {}".NMEAMessage)
        
        self._n_messages = n_messages
        self._message_number = message_number
        self._satellites_in_view = satellites_in_view
        self._satellite_data = satellite_data
        
    @property
    def n_messages(self):
        return self._n_messages
    
    @n_messages.setter
    def n_messages(self, value):
        self._n_messages = value
        
    @property
    def message_number(self):
        return self._message_number
    
    @message_number.setter
    def message_number(self, value):
        self._message_number = value
        
    @property
    def satellites_in_view(self):
        return self._satellites_in_view
    
    @satellites_in_view.setter
    def satellites_in_view(self, value):
        self._satellites_in_view = value
        
    @property
    def satellite_data(self):
        return self._satellite_data
    
    @satellite_data.setter
    def satellite_data(self, value):
        self._satellite_data = value


   
    # GNSS Satellites in view
    # The GSV sentence provides the number of satellites (SV) in view, satellite ID numbers, elevation, azimuth, and SNR value.
    #private readonly List<SatelliteVehicle> svs = new List<SatelliteVehicle>()

    # <inheritdoc />
    #protected override int MessageCountIndex => 0

    # <inheritdoc />
    #protected override int MessageNumberIndex => 1

    # <inheritdoc />
    def ParseSentences(Talker talkerType, str[] NMEAMessage):
        satellites = int(NMEAMessage[2])

        if (SatellitesInView == -1):
            SatellitesInView = satellites
        elif ( satellites != SatellitesInView):
            return False # Messages do not match

        if ((NMEAMessage.Length - 3) % 4 == 1): # v4.1+ adds system id to the last NMEAMessage. Example L1=1, and L2=6 on GPS satellites
            id = NMEAMessage.Last()
            if (id.Length == 1):
                GnssSignalId = id[0]
        
        i = 3    
        for i in range(i < NMEAMessage.Length - 3):
            if (NMEAMessage[i].Length == 0):
                continue
            else:
                svs.Add(new SatelliteVehicle(talkerType, GnssSignalId, NMEAMessage, i))
                
            i = i + 4
        
        return True

        # Total number of satellite vehicles (SV) in view
        def int SatellitesInView:
            return _set

        # Satellite vehicles in this NMEAMessage part.
        def IReadOnlyList<SatelliteVehicle> SVs => svs.AsReadOnly()
        
        # Gets the GNSS Signal ID
        # System    Signal ID   Signal Channel
        # GPS		
        #           0		    All signals</td></tr>
        # 			1			L1 C/1</td></tr>
        # 			2			L1 P(Y)</td></tr>
        # 			3			L1 M</td></tr>
        # 			4			L2 P(Y)</td></tr>
        # 			5			L2C-M</td></tr>
        # 			6			L2C-L</td></tr>
        # 			7			L5-I</td></tr>
        # 			8			L5-Q</td></tr>
        # 			9-F			Reserved</td></tr>
        # GLONASS	
        #           0			All signals</td></tr>
        # 			1			G1 C/A</td></tr>
        # 			2			G1 P</td></tr>
        # 			3			G2 C/A</td></tr>
        # 			4			GLONASS (M) G2 P</td></tr>
        # 			5-F			Reserved</td></tr>
        # GALILEO	
        #           0	    	All signals</td></tr>
        # 			1			E5a</td></tr>
        # 			2			E5b</td></tr>
        # 			3			E5 a+b</td></tr>
        # 			4			E6-A</td></tr>
        # 			5			E6-BC</td></tr>
        # 		    6			L1-A</td></tr>
        # 			7			L1-BC</td></tr>
        # 			8-F			Reserved</td></tr>
        # BeiDou System
        #           0		All signals</td></tr>
        # 			1			B1I</td></tr>
        # 			2			B1Q</td></tr>
        # 			3			B1C</td></tr>
        # 			4			B1A</td></tr>
        # 			5			B2-a</td></tr>
        # 			6			B2-b</td></tr>
        # 			7			B2 a+b</td></tr>
        # 			8			B3I</td></tr>
        # 			9			B3Q</td></tr>
        # 			A			B3A</td></tr>
        # 			B			B2I</td></tr>
        # 			C			B2Q</td></tr>
        # 			D-F			Reserved</td></tr>
        # QZSS
        #           0		All signals</td></tr>
        # 	    	1		L1 C/A</td></tr>
        # 	    	2		L1C (D)</td></tr>
        # 	    	3		L1C (P)</td></tr>
        # 	    	4		LIS</td></tr>
        # 	    	5		L2C-M</td></tr>
        # 	    	6		L2C-L</td></tr>
        # 	    	7		L5-I</td></tr>
        # 	    	8		L5-Q</td></tr>
        # 		    9		L6D</td></tr>
        # 	    	A		L6E</td></tr>
        # 	    	B-F		Reserved</td></tr>
        # NavIC (IRNSS)
        #           0		All signals</td></tr>
        # 	    	1		L5-SPS</td></tr>
        # 	    	2		S-SPS</td></tr>
        # 	    	3		L5-RS</td></tr>
        # 	    	4		S-RS</td></tr>
        # 	    	5		L1-SPS</td></tr>
        # 	    	6-F		Reserved</td></tr>
        def char GnssSignalId { get private set } = '0'

        
        # Returns an enumerator that iterates through the collection.
        # <returns> A System.Collections.Generic.IEnumerator{SatelliteVehicle} that can be used to iterate through the collection.</returns>
        def IEnumerator<SatelliteVehicle> GetEnumerator()
        {
            foreach (var sv in SVs)
                yield return sv
        }

        
        # Returns an enumerator that iterates through a collection.
        # <returns> An System.Collections.IEnumerator object that can be used to iterate through the collection.</returns>
        System.Collections.IEnumerator System.Collections.IEnumerable.GetEnumerator()
        {
            return GetEnumerator()
        }
    }
    
    # Satellite vehicle
    class SatelliteVehicle():

        internal SatelliteVehicle(Talker talker, char signalId, string[] NMEAMessage, int startIndex)
        {
            Id = int.Parse(NMEAMessage[startIndex], CultureInfo.InvariantCulture)
            if (double.TryParse(NMEAMessage[startIndex + 1], NumberStyles.AllowDecimalPoint, CultureInfo.InvariantCulture, out double e))
                Elevation = e
            if (double.TryParse(NMEAMessage[startIndex + 2], NumberStyles.AllowDecimalPoint, CultureInfo.InvariantCulture, out double a))
                Azimuth = a
            int snr = -1
            if (int.TryParse(NMEAMessage[startIndex + 3], out snr))
                SignalToNoiseRatio = snr
            GnssSignalId = signalId
            TalkerId = talker
        }

        
        # Gets the talker ID for this vehicle
        def Talker TalkerId { get }

        # Gets the GNSS Signal ID.
        # <seealso cref="Gsv.GnssSignalId"/>
        def char GnssSignalId { get }

        # Satellite ID number
        def int Id { get }

        # Elevation in degrees, 90 maximum
        def double Elevation { get } = double.NaN

        # Azimuth, degrees from true north, 000 to 359
        def double Azimuth { get } = double.NaN
        
        # Signal-to-Noise ratio, 0-99 dB (-1 when not tracking) 
        def int SignalToNoiseRatio { get } = -1

        
        # Satellite system
        def SatelliteSystem System
        {
            get
            {
                if (Id >= 1 && Id <= 32)
                    return SatelliteSystem.Gps
                if (Id >= 33 && Id <= 64)
                    return SatelliteSystem.Waas
                if (Id >= 65 && Id <= 96)
                    return SatelliteSystem.Glonass
                return SatelliteSystem.Unknown
            }
        }

        
    }

    # Returns a string that represents the satellite vehicle.
    # <returns>A string that represents the satellite vehicle.</returns>
    def override ToString():
        match TalkerId:
            case Talker.GlobalPositioningSystem:
                return $"GPS{Id}"
            case Talker.GlonassReceiver: 
                return $"GLO{Id}"
            case Talker.GalileoPositioningSystem: 
                return $"GAL{Id}"
            case Talker.BeiDouNavigationSatelliteSystem: 
                return $"BEI{Id}"
            _:
                return Id.ToString()
    
    # Satellite system
    def SatelliteSystem(Enum):
        # Unknown
        Unknown,
        # GPS - Global Positioning System (NAVSTAR)
        Gps,
        # WAAS - Wide Area Augmentation System
        Waas,
        # GLONASS - Globalnaya navigatsionnaya sputnikovaya sistema
        Glonass,
        # Galileo
        Galileo
