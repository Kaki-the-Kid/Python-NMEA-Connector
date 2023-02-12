# ****************************************************************************//*
# *   @project  Python NMEA Connector
# *   @file     VHW.py
# *   @brief    Water speed and heading
# *   @author   Karsten Reitan Sørensen
# *   Date:     11-02-2023
# *******************************************************************************
# <remarks>
# Waypoint identifiers, listed in order with starting waypoint first, for the identified route. Two modes of
# transmission are provided: 'c' indicates that the complete list of waypoints in the route are being
# transmitted 'w' indicates a working route where the first listed waypoint is always the last waypoint
# that had been reached (FROM), while the second listed waypoint is always the waypoint that the vessel is
# currently heading for (TO), the remaining list of waypoints represents the remainder of the route. 
# </remarks>

from NMEA0183_Commands import NMEA0183_Command as NMEAMessage


class VHW(NMEAMessage):
    
    def __init__(self):
        self._heading_degrees_true = None
        self._speed_knots = None
        self._speed_kph = None

    @property
    def heading_degrees_true(self):
        return self._heading_degrees_true

    @heading_degrees_true.setter
    def heading_degrees_true(self, value):
        self._heading_degrees_true = value

    @property
    def speed_knots(self):
        return self._speed_knots

    @speed_knots.setter
    def speed_knots(self, value):
        self._speed_knots = value

    @property
    def speed_kph(self):
        return self._speed_kph

    @speed_kph.setter
    def speed_kph(self, value):
        self._speed_kph = value


    _waypoints = []

    # Waypoint tpe   
    def WaypointListType(Enum):
        CompleteWaypointsList,# Complete list of waypoints
        RemainingWaypointsList# List of remaining waypoints

    
    
