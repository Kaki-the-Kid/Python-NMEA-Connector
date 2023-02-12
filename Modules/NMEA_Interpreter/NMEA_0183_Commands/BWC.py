# ****************************************************************************//*
# *   @project  Python NMEA Connector
# *   @file     BWC.py
# *   @brief    Cross Track Error, Measured
# *   @author   Karsten Reitan Sørensen
# *   Date:     11-02-2023
# *******************************************************************************

from NMEA0183_Commands import NMEA0183_Command


class BWC(NMEA0183_Command):
    # @brief    Initializes a new instance of the <see cref="BWC"/> class.
    # @param    name="bearing"       The bearing.
    # @param    name="bearing_type"  Type of the bearing.
    # @param    name="destination"   The destination.
    # @param    name="time"          The time.
    # @param    name="to"            To.
    # @exception    name="ValueError"    Thrown when one or more arguments have unsupported or  illegal values.
            
    def __init__(self, bearing=None, bearing_type=None, destination=None, time=None, to=None):
        self.bearing = bearing
        self.bearing_type = bearing_type
        self.destination = destination
        self.time = time
        self.to = to
    
    @property
    def bearing(self):
        return self._bearing
    
    @bearing.setter
    def bearing(self, bearing):
        self._bearing = bearing
    
    @property
    def bearing_type(self):
        return self._bearing_type
    
    @bearing_type.setter
    def bearing_type(self, bearing_type):
        self._bearing_type = bearing_type
    
    @property
    def destination(self):
        return self._destination
    
    @destination.setter
    def destination(self, destination):
        self._destination = destination
    
    @property
    def time(self):
        return self._time
    
    @time.setter
    def time(self, time):
        self._time = time
    
    @property
    def to(self):
        return self._to
    
    @to.setter
    def to(self, to):
        self._to = to
