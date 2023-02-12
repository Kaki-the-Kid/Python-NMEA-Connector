# ****************************************************************************//*
# @project  Python NMEA Connector
# @file     VTG.py
# @brief    Course over ground and ground speed
# @brief    The actual course and speed relative to the ground.
# @author   Karsten Reitan Sørensen
# Date:     11-02-2023
# *******************************************************************************

from NMEA0183_Commands import NMEA0183_Command as NMEAMessage


class VTG(NMEAMessage):
    
    def __init__(self, NMEAMessage):
        if ( NMEAMessage == None or NMEAMessage.Length < 7 ):
            raise Exception("Invalid VTG: {}".NMEAMessage)
        
        # Course over ground relative to true north
        CourseTrue = NMEAMessage.StringToDouble(NMEAMessage[0])
        self.__TrueTrackMadeGood = None
        # public double CourseTrue { get }

        #  Course over ground relative to magnetic north
        CourseMagnetic = NMEAMessage.StringToDouble(NMEAMessage[2])
        self.__MagneticTrackMadeGood = None
        # public double CourseMagnetic { get }

        # Speed over ground in knots
        SpeedKnots = NMEAMessage.StringToDouble(NMEAMessage[4])
        self.__GroundSpeedKnots = None
        #public double SpeedKnots { get }
        
        # Speed over ground in kilometers/hour
        SpeedKph = NMEAMessage.StringToDouble(NMEAMessage[6])
        self.__GroundSpeedKmh = None
        #public double SpeedKph { get }
        
        
    def setTrueTrackMadeGood(self, TrueTrackMadeGood):
        self.__TrueTrackMadeGood = TrueTrackMadeGood
    
    def getTrueTrackMadeGood(self):
        return self.__TrueTrackMadeGood

    def setMagneticTrackMadeGood(self, MagneticTrackMadeGood):
        self.__MagneticTrackMadeGood = MagneticTrackMadeGood
    
    def getMagneticTrackMadeGood(self):
        return self.__MagneticTrackMadeGood

    def setGroundSpeedKnots(self, GroundSpeedKnots):
        self.__GroundSpeedKnots = GroundSpeedKnots
    
    def getGroundSpeedKnots(self):
        return self.__GroundSpeedKnots

    def setGroundSpeedKmh(self, GroundSpeedKmh):
        self.__GroundSpeedKmh = GroundSpeedKmh
    
    def getGroundSpeedKmh(self):
        return self.__GroundSpeedKmh
