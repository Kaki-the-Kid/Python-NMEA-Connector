# ****************************************************************************//*
# *   @project  Python NMEA Connector
# *   @file     ZDA.py
# *   @brief    Date and time of fix
# *   @author   Karsten Reitan Sørensen
# *   Date:     11-02-2023
# *******************************************************************************


from NMEA0183_Commands import NMEA0183_Command as NMEAMessage


class ZDA(NMEAMessage):
    
    def __init__(self, NMEAMessage):
        if (NMEAMessage.Length != 6):
            raise Exception("Invalid ZDA: {}".nameof(NMEAMessage) )
        
        self.time = None
        self.day = None
        self.month = None
        self.year = None
        self.local_hour_offset = None
        self.local_minute_offset = None

    def set_time(self, time):
        self.time = time
    
    def get_time(self):
        return self.time

    def set_day(self, day):
        self.day = day
    
    def get_day(self):
        return self.day

    def set_month(self, month):
        self.month = month
    
    def get_month(self):
        return self.month

    def set_year(self, year):
        self.year = year
    
    def get_year(self):
        return self.year

    def set_local_hour_offset(self, local_hour_offset):
        self.local_hour_offset = local_hour_offset
    
    def get_local_hour_offset(self):
        return self.local_hour_offset

    def set_local_minute_offset(self, local_minute_offset):
        self.local_minute_offset = local_minute_offset
    
    def get_local_minute_offset(self):
        return self.local_minute_offset
