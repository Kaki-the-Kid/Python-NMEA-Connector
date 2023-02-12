# ****************************************************************************//*
# @project  Python NMEA Connector
# @file     VWR.py
# @brief    Relative Wind Speed and Angle
# @author   Karsten Reitan Sørensen
# @Date:    11-02-2023
# *******************************************************************************
# @Description: VWR - Relative Wind Speed and Angle
#           ,$--VWR,x.x,a,x.x,a*hh<CR><LF>
#           1) Wind direction magnitude in degrees0 to 360 degrees
#           2) Reference, R = Relative Always R
#           3) Wind speed magnitude 3) 0.0 to 99.9 knots
#           4) Wind speed units, (K)nots/M/N
#           5) Status, A = Data Valid
#           6) Checksum
# 
# Example: $IIVWR,054.7,R,03.5,N,A*3C     054.7 degrees, 3.5 knots, Relative  
# ****************************************************************************//*

from NMEA0183_Commands import NMEA0183_Command as NMEAMessage


class VWR(NMEAMessage):
    
    def __init__(self, raw_sentence):
        self.talker_id = raw_sentence[1:3]
        self.sentence_id = raw_sentence[3:6]
        self.direction_of_wind = raw_sentence[6:7]
        self.speed = raw_sentence[7:12]
        self.speed_unit = raw_sentence[12:13]
        self.reference_speed = raw_sentence[13:18]
        self.reference_speed_unit = raw_sentence[18:19]
    
    def get_talker_id(self):
        return self.talker_id
    
    def set_talker_id(self, talker_id):
        self.talker_id = talker_id
    
    def get_sentence_id(self):
        return self.sentence_id
    
    def set_sentence_id(self, sentence_id):
        self.sentence_id = sentence_id
    
    def get_direction_of_wind(self):
        return self.direction_of_wind
    
    def set_direction_of_wind(self, direction_of_wind):
        self.direction_of_wind = direction_of_wind
    
    def get_speed(self):
        return self.speed
    
    def set_speed(self, speed):
        self.speed = speed
    
    def get_speed_unit(self):
        return self.speed_unit
    
    def set_speed_unit(self, speed_unit):
        self.speed_unit = speed_unit
    
    def get_reference_speed(self):
        return self.reference_speed
    
    def set_reference_speed(self, reference_speed):
        self.reference_speed = reference_speed
    
    def get_reference_speed_unit(self):
        return self.reference_speed_unit
    
    def set_reference_speed_unit(self, reference_speed_unit):
        self.reference_speed_unit = reference_speed_unit
