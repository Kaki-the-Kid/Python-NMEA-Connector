# ****************************************************************************//*
# *   @project  Python NMEA Connector
# *   @file     HDG.py
# *   @brief    Heading - Deviation & Variation
# *   @author   Karsten Reitan Sørensen
# *   Date:     11-02-2023
# *******************************************************************************
# GNSS Satellites in view
# The GSV sentence provides the number of satellites (SV) in view, satellite ID numbers, 
# elevation, azimuth, and SNR value.
# *******************************************************************************

from NMEA0183_Commands import NMEA0183_Command as NMEAMessage


class HDG(NMEAMessage):
    def __init__(self):
        self.heading = 0.0
        self.deviation = 0.0
        self.variation = 0.0
        self.direction_of_deviation = ''
    
    def set_heading(self, heading):
        self.heading = heading

    def get_heading(self):
        return self.heading

    def set_deviation(self, deviation):
        self.deviation = deviation

    def get_deviation(self):
        return self.deviation

    def set_variation(self, variation):
        self.variation = variation

    def get_variation(self):
        return self.variation

    def set_direction_of_deviation(self, direction_of_deviation):
        self.direction_of_deviation = direction_of_deviation

    def get_direction_of_deviation(self):
        return self.direction_of_deviation
