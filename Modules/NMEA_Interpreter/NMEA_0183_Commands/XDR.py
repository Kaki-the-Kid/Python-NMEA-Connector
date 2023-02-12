# ****************************************************************************//*
# *   @project  Python NMEA Connector
# *   @file     XDR.py
# *   @brief    Cross Track Error, Measured
# *   @author   Karsten Reitan Sørensen
# *   Date:     11-02-2023
# *******************************************************************************

from NMEA0183_Commands import NMEA0183_Command


class XDR(NMEA0183_Command):
    
    def __init__(self):
        self.transducer_type = None
        self.measurement_data = None
        self.unit_of_measurement = None
        self.name_of_transducer = None

    def set_transducer_type(self, transducer_type):
        self.transducer_type = transducer_type

    def get_transducer_type(self):
        return self.transducer_type

    def set_measurement_data(self, measurement_data):
        self.measurement_data = measurement_data

    def get_measurement_data(self):
        return self.measurement_data

    def set_unit_of_measurement(self, unit_of_measurement):
        self.unit_of_measurement = unit_of_measurement

    def get_unit_of_measurement(self):
        return self.unit_of_measurement

    def set_name_of_transducer(self, name_of_transducer):
        self.name_of_transducer = name_of_transducer

    def get_name_of_transducer(self):
        return self.name_of_transducer
