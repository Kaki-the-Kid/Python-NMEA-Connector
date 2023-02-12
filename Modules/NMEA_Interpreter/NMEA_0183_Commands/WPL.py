# ****************************************************************************//*
# *   @project  Python NMEA Connector
# *   @file     WPL.py
# *   @brief    Waypoint Location
# *   @author   Karsten Reitan Sørensen
# *   Date:     11-02-2023
# *******************************************************************************
# Routes

# <remarks>
# Waypoint identifiers, listed in order with starting waypoint first, for the identified route. Two modes of
# transmission are provided: 'c' indicates that the complete list of waypoints in the route are being
# transmitted 'w' indicates a working route where the first listed waypoint is always the last waypoint
# that had been reached (FROM), while the second listed waypoint is always the waypoint that the vessel is
# currently heading for (TO), the remaining list of waypoints represents the remainder of the route. 
# </remarks>

from NMEA0183_Commands import NMEA0183_Command as NMEAMessage


class WPL(NMEAMessage):
    def __init__(self):
        self.__latitude = None
        self.__longitude = None
        self.__waypoint_id = None
        self.__waypoint_name = None

    def get_latitude(self):
        return self.__latitude
    
    def set_latitude(self, latitude):
        self.__latitude = latitude
    
    def get_longitude(self):
        return self.__longitude
    
    def set_longitude(self, longitude):
        self.__longitude = longitude
    
    def get_waypoint_id(self):
        return self.__waypoint_id
    
    def set_waypoint_id(self, waypoint_id):
        self.__waypoint_id = waypoint_id
    
    def get_waypoint_name(self):
        return self.__waypoint_name
    
    def set_waypoint_name(self, waypoint_name):
        self.__waypoint_name = waypoint_name


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

    
    # Waypoints
    #def IReadOnlyList<str> Waypoints => _waypoints.AsReadOnly()

    
    # @brief    Returns an enumerator that iterates through the collection.
    # @returns A System.Collections.Generic.IEnumerator{T} that can be used to iterate through the collection.</returns>
    #def IEnumerator<str> IEnumerable<str>.GetEnumerator()
    #    foreach (str waypoint in Waypoints)
    #        yield return waypoint

    
    # Returns an enumerator that iterates through a collection.
    # @returns An System.Collections.IEnumerator object that can be used to iterate through the collection.</returns>
    #def System.Collections.IEnumerator System.Collections.IEnumerable.GetEnumerator()
    #    return self.GetEnumerator()
