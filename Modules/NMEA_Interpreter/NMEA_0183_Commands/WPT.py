# ****************************************************************************//*
# *   @project  Python NMEA Connector
# *   @file     WPT.py
# *   @brief    Waypoint list
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

from NMEA0183_Commands import NMEA0183_Command


class WPT(NMEA0183_Command):
    
    def __init__(self):
        self.latitude = None
        self.longitude = None
        self.name = None
        self.waypoint_id = None

    # Setter method for latitude
    def set_latitude(self, latitude):
        self.latitude = latitude

    # Getter method for latitude
    def get_latitude(self):
        return self.latitude

    # Setter method for longitude
    def set_longitude(self, longitude):
        self.longitude = longitude

    # Getter method for longitude
    def get_longitude(self):
        return self.longitude

    # Setter method for name
    def set_name(self, name):
        self.name = name

    # Getter method for name
    def get_name(self):
        return self.name

    # Setter method for waypoint_id
    def set_waypoint_id(self, waypoint_id):
        self.waypoint_id = waypoint_id

    # Getter method for waypoint_id
    def get_waypoint_id(self):
        return self.waypoint_id


    list: _waypoints = []

    # Waypoint tpe   
    def WaypointListType(Enum):
        CompleteWaypointsList,# Complete list of waypoints
        RemainingWaypointsList# List of remaining waypoints

    
    # Initializes a new instance of the <see cref="Rte"/> class.
    
    # <param name="type">The message type</param>
    # <param name="message">The NMEA message values.</param>
    def RTE(str: type, message = []):
        if (message == null or message.Length < 4):
            raise Exception("Invalid RTE", "message")
        
        ListType = WaypointListType.CompleteWaypointsList if (message[2] == "c") else WaypointListType.RemainingWaypointsList
        RouteId = message[3]
        pass

    # <inheritdoc />
    def ParseSentences( talker, message = [] ):
        if ( self.MessageParts[2] != message[2] or self.MessageParts[3] != message[3] ):
            return False
            
        _waypoints.AddRange(message.Skip(4))
        return True

    
    # Gets the type of the list.
    def ListType(): # WaypointListType
        return self.ListType

    
    # Gets the route identifier.
    def RouteId(): 
        return self.RouteId
