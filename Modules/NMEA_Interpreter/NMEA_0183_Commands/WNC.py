# ****************************************************************************//*
# *   @project  Python NMEA Connector
# *   @file     WNC.py
# *   @brief    Waypoint Next Command
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


class WNC(NMEAMessage):
    def __init__(self, nmea_string: str):
        self.nmea_string = nmea_string
        self.command = "WNC"
        self.data = self.nmea_string.split(',')

    def set_nmea_string(self, nmea_string: str):
        self.nmea_string = nmea_string
        self.data = self.nmea_string.split(',')

    def get_nmea_string(self):
        return self.nmea_string

    def set_distance(self, distance: float):
        self.data[1] = distance

    def get_distance(self):
        return float(self.data[1])

    def set_waypoint_to(self, waypoint_to: str):
        self.data[2] = waypoint_to

    def get_waypoint_to(self):
        return self.data[2]

    def set_waypoint_from(self, waypoint_from: str):
        self.data[3] = waypoint_from

    def get_waypoint_from(self):
        return self.data[3]

    def set_bearing_true(self, bearing_true: float):
        self.data[4] = bearing_true

    def get_bearing_true(self):
        return float(self.data[4])

    def set_bearing_magnetic(self, bearing_magnetic: float):
        self.data[5] = bearing_magnetic

    def get_bearing_magnetic(self):
        return float(self.data[5])

    def set_mode_indicator(self, mode_indicator: str):
        self.data[6] = mode_indicator

    def get_mode_indicator(self):
        return self.data[6]


    
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
