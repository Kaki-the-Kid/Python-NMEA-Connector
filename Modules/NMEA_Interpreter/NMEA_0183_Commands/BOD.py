# *************************************************************************************************
# (BOD) message class
# @brief    Bearing - Origin to Destination (BOD) message class
# @brief    Bearing - Origin to Destination 
# Path: Modules\NMEA_Interpreter\NMEA_0183_Commands\BOD.py
#
# Bearing angle of the line, calculated at the origin waypoint, extending to the destination
# waypoint from the origin waypoint for the active navigation leg of the journey
# This sentence is transmitted at intervals not exceeding 2-seconds and is always accompanied by 
# <see cref="Rmb"/> when a destination waypoint is active.
# **********************************************************************************************//*

from NMEA0183_Commands import NMEA0183_Command


class BOD(NMEAMessage):

    # @brief    Initializes a new instance of the <see cref="Bod"/> class.
    # @param    name="type"    The message type
    # @param    name="message" The NMEA message values.
    # @exception    name="ValueError"    Thrown when one or more arguments have unsupported or  illegal values.
    def __init__(self, 
                 TrueBearing     = None, 
                 MagneticBearing = None, 
                 DestinationId   = None, 
                 OriginId        = None
                 ):
        self.TrueBearing = TrueBearing
        self.MagneticBearing = MagneticBearing
        self.DestinationId = DestinationId
        self.OriginId = OriginId
    
    # True Bearing in degrees from start to destination
    @property
    def TrueBearing(self):
        return self._TrueBearing
    
    @TrueBearing.setter
    def TrueBearing(self, TrueBearing):
        self._TrueBearing = TrueBearing

    # Magnetic Bearing in degrees from start to destination
    @property
    def MagneticBearing(self):
        return self._MagneticBearing
    
    @MagneticBearing.setter
    def MagneticBearing(self, MagneticBearing):
        self._MagneticBearing = MagneticBearing
    
    # Name of destination waypoint ID
    @property
    def DestinationId(self):
        return self._DestinationId
    
    @DestinationId.setter
    def DestinationId(self, DestinationId):
        self._DestinationId = DestinationId
    
    # Name of origin waypoint ID
    @property
    def OriginId(self):
        return self._OriginId
    
    @OriginId.setter
    def OriginId(self, OriginId):
        self._OriginId = OriginId

    
    
    def __init__(self, type, message):
        if (message == None or len(message) < 3):
            raise ValueError("Invalid BOD", "message")
        
        if (len(message[0]) > 0):
            self.TrueBearing = float(message[0])
        else:
            self.TrueBearing = float('nan')
            
        if (len(message[2]) > 0):
            self.MagneticBearing = float(message[2])
        else:
            self.MagneticBearing = float('nan')
            
        if (len(message) > 4 and message[4] != None):
            self.DestinationId = message[4]
            
        if (len(message) > 5 and message[5] != None):
            self.OriginId = message[5]
    


