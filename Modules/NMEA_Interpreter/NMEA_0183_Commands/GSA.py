# ****************************************************************************//*
# *   @project  Python NMEA Connector
# *   @file     BWC.py
# *   @brief    Cross Track Error, Measured
# *   @author   Karsten Reitan Sørensen
# *   Date:     11-02-2023
# *******************************************************************************
# @brief    Global Positioning System DOP and active satellites
# *******************************************************************************

from NMEA0183_Commands import NMEA0183_Command as NMEAMessage


class GSA(NMEAMessage):

    def __init__(self, NMEAMessage, mode, fix_type, sv_ids, pdop, hdop, vdop):
        if (NMEAMessage == null or NMEAMessage.Length < 17):
            raise Exception("Invalid GSA", "NMEAMessage")
        
        self._mode = mode
        Mode = GSA.ModeSelection.Auto if (NMEAMessage[0] == "A") else GSA.ModeSelection.Manual
        
        self._fix_type = fix_type
        Fix = (GSA.FixType)int.Parse(NMEAMessage[1], CultureInfo.InvariantCulture)
        
        # @brief    ID numbers of satellite vehicles used in the solution.
        # 
        #- GPS satellites are identified by their PRN numbers, which range from 1 to 32.
        #- The numbers 33-64 are reserved for SBAS satellites. The SBAS system PRN numbers are 120-138. The offset from NMEA SBAS SB ID to SBAS PRN number is 87.
        #A SBAS PRN number of 120 minus 87 yields the SV ID of 33. The addition of87 to the SVID yields the SBAS PRN number.
        #- The numbers 65-96 are reserved for GLONASS satellites. GLONASS satellites are identified by 64+satellite slot number.
        #</remarks>
        self._sv_ids = sv_ids
        def int[] SatelliteIDs { get }
        List<int> svs = new List<int>()
        for (int i = 2 i < 14 i++)
        {
            int id = -1
            if (NMEAMessage[i].Length > 0 && int.TryParse(NMEAMessage[i], out id))
                svs.Add(id)
        }
        SatelliteIDs = svs.ToArray()

        #Dilution of precision
        self._pdop = pdop
        #def float Pdop { get }
        float: tmp = 0
        if ( float(NMEAMessage[14]) ):
            Pdop = tmp
        else:
            Pdop = None

        
        #Horizontal dilution of precision
        #def float Hdop { get }
        self._hdop = hdop
        if ( float( NMEAMessage[15]) ):
            Hdop = tmp
        else:
            Hdop = float.NaN
            
        #Vertical dilution of precision
        # MessageId = "Vdop")]
        #def float Vdop { get }
        self._vdop = vdop
        if ( float(NMEAMessage[16]) ):
            Vdop = tmp
        else:
            Vdop = float.NaN

    
    # Getter method for mode
    @property
    def mode(self):
        return self._mode
    
    # Setter method for mode
    @mode.setter
    def mode(self, mode):
        self._mode = mode
        
    # Getter method for fix_type
    @property
    def fix_type(self):
        return self._fix_type
    
    # Setter method for fix_type
    @fix_type.setter
    def fix_type(self, fix_type):
        self._fix_type = fix_type
        
    # Getter method for sv_ids
    @property
    def sv_ids(self):
        return self._sv_ids
    
    # Setter method for sv_ids
    @sv_ids.setter
    def sv_ids(self, sv_ids):
        self._sv_ids = sv_ids
        
    # Getter method for pdop
    @property
    def pdop(self):
        return self._pdop
    
    # Setter method for pdop
    @pdop.setter
    def pdop(self, pdop):
        self._pdop = pdop
        
    # Getter method for hdop
    @property
    def hdop(self):
        return self._hdop
    
    # Setter method for hdop
    @hdop.setter
    def hdop(self, hdop):
        self._hdop = hdop
        
    # Getter method for vdop
    @property
    def vdop(self):
        return self._vdop
    
    # Setter method for vdop
    @vdop.setter
    def vdop(self, vdop):
        self._vdop = vdop

    



    #Mode
    def Mode():
        return ModeSelection(self._mode)

    #Mode
    def Fix():
        return FixType(self._fix_type)

    #Mode selection
    def ModeSelection(Enum):
        Auto,   #Automatic, allowed to automatically switch 2D/3D
        Manual, #Manual mode

    #Fix Mode
    #Enum values matches NMEA spec
    def FixType(Enum):
        NotAvailable = 1,#Not available
        Fix2D = 2, #2D Fix
        Fix3D = 3  #3D Fix


        [TestMethod]
        public void TestGpgsa_Empty()
        {
            string input = "$GPGSA,A,3,,,,,,16,18,,22,24,,,,,*14";
            var msg = NmeaMessage.Parse(input);
            Assert.IsInstanceOfType(msg, typeof(Gsa));
            Gsa gsa = (Gsa)msg;
            Assert.AreEqual(Gsa.ModeSelection.Auto, gsa.Mode);
            Assert.AreEqual(Gsa.FixType.Fix3D, gsa.Fix);
            Assert.AreEqual(4, gsa.SatelliteIDs.Length);
            Assert.AreEqual(16, gsa.SatelliteIDs[0]);
            Assert.AreEqual(18, gsa.SatelliteIDs[1]);
            Assert.AreEqual(22, gsa.SatelliteIDs[2]);
            Assert.AreEqual(24, gsa.SatelliteIDs[3]);
            Assert.AreEqual(double.NaN, gsa.Pdop);
            Assert.AreEqual(double.NaN, gsa.Hdop);
            Assert.AreEqual(double.NaN, gsa.Vdop);
        }
