# ****************************************************************************//*
# *   @project  Python NMEA Connector
# *   @file     VLW.py
# *   @brief    Dual Ground/Water Distance
# *   @author   Karsten Reitan Sørensen
# *   Date:     11-02-2023
# *******************************************************************************
# The distance traveled, relative to the water and over the ground.

from NMEA0183_Commands import NMEA0183_Command as NMEAMessage

class VLW(NMEAMessage):
    
    def __init__(self, NMEAMmessage):
        if (NMEAMmessage == null or NMEAMmessage.Length < 7):
            raise Exception("Invalid VLW: {}".NMEAMmessage)
        
        # Total cumulative water distance, nautical miles
        # public double WaterDistanceCumulative { get; }
        self.__TripLog = 0.0
        self.__CumulativeLog = 0.0

    def set_TripLog(self, tripLog):
        self.__TripLog = tripLog

    def get_TripLog(self):
        return self.__TripLog

    def set_CumulativeLog(self, cumulativeLog):
        self.__CumulativeLog = cumulativeLog

    def get_CumulativeLog(self):
        return self.__CumulativeLog

    #Water distance since reset, nautical miles
    #public double WaterDistanceSinceReset { get; }
    WaterDistanceCumulative = NMEAMmessage.StringToDouble(NMEAMmessage[0])
    WaterDistanceSinceReset = NMEAMmessage.StringToDouble(NMEAMmessage[2])
    
    #Total cumulative ground distance, nautical miles
    #public double GroundDistanceCumulative { get; }
    GroundDistanceCumulative = NMEAMmessage.StringToDouble(NMEAMmessage[4])

    #Ground distance since reset, nautical miles
    #public double GroundDistanceSinceReset { get; }
    GroundDistanceSinceReset = NMEAMmessage.StringToDouble(NMEAMmessage[6])
