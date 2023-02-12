# ****************************************************************************//*
# *   @project  Python NMEA Connector
# *   @file     GLL.py
# *   @brief    Geographic position, latitude / longitude.
# *   @author   Karsten Reitan Sørensen
# *   Date:     11-02-2023
# *******************************************************************************
# Latitude and Longitude of vessel position, time of position fix and status.

from NMEA0183_Commands import NMEA0183_Command as NMEAMessage


class GLL(NMEAMessage):

    def __init__(self, NMEAMessage):
        if (NMEAMessage == null or NMEAMessage.Length < 4):
            raise Exception("Invalid GLL: {}".NMEAMessage)
        
        # @brief Latitude
        self.__latitude = None
        #def float Latitude { get }
        self.__latitude_hemisphere = None
        #Latitude = NmeaMessage.StringToLatitude(message[0], message[1])
        
        #/ Longitude
        self.__longitude = None
        #def float Longitude { get }
        self.__longitude_hemisphere = None
        #Longitude = NmeaMessage.StringToLongitude(message[2], message[3])

        self.__time = None
        self.__status = None
        self.__mode = None


    @property
    def latitude(self):
        return self.__latitude

    @latitude.setter
    def latitude(self, value):
        self.__latitude = value

    @property
    def latitude_hemisphere(self):
        return self.__latitude_hemisphere

    @latitude_hemisphere.setter
    def latitude_hemisphere(self, value):
        self.__latitude_hemisphere = value

    @property
    def longitude(self):
        return self.__longitude

    @longitude.setter
    def longitude(self, value):
        self.__longitude = value

    @property
    def longitude_hemisphere(self):
        return self.__longitude_hemisphere

    @longitude_hemisphere.setter
    def longitude_hemisphere(self, value):
        self.__longitude_hemisphere = value

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, value):
        self.__time = value

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value

    @property
    def mode(self):
        return self.__mode

    @mode.setter
    def mode(self, value):
        self.__mode = value


    if (NMEAMessage.Length >= 5): #Some older GPS doesn't broadcast fix time
        FixTime = StringToTimeSpan(message[4])

    DataActive = (NMEAMessage.Length < 6 or NMEAMessage[5] == "A")
    ModeIndicator = Mode.Autonomous if DataActive else Mode.DataNotValid
    
        # Positioning system Mode Indicator
    # <seealso cref="Gll.ModeIndicator"/>
    from enum import Enum
    def Mode(Enum):
        # Autonomous mode
        Autonomous = 0
        # Differential mode
        Differential = 1
        # Estimated (dead reckoning) mode
        EstimatedDeadReckoning = 2
        # Manual input mode
        Manual = 3
        # Simulator mode
        Simulator = 4
        # Data not valid
        DataNotValid = 5

    if (NMEAMessage.Length > 6):
        match (NMEAMessage[6]):
            case "A": 
                ModeIndicator = Mode.Autonomous
            case "D": 
                ModeIndicator = Mode.DataNotValid
            case "E": 
                ModeIndicator = Mode.EstimatedDeadReckoning
            case "M": 
                ModeIndicator = Mode.Manual
            case "S": 
                ModeIndicator = Mode.Simulator
            case "N": 
                ModeIndicator = Mode.DataNotValid

    #/ Positioning system Mode Indicator
    def Mode ModeIndicator { get }


