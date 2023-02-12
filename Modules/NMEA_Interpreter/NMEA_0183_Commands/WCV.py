# ****************************************************************************//*
# *   @project  Python NMEA Connector
# *   @file     BWC.py
# *   @brief    Cross Track Error, Measured
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


class WCV(NMEAMessage):
    
    def __init__(self):
        self.__speed = None
        self.__speed_unit = None
        self.__waypoint_id = None
        self.__status = None

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        self.__speed = speed

    @property
    def speed_unit(self):
        return self.__speed_unit

    @speed_unit.setter
    def speed_unit(self, speed_unit):
        self.__speed_unit = speed_unit

    @property
    def waypoint_id(self):
        return self.__waypoint_id

    @waypoint_id.setter
    def waypoint_id(self, waypoint_id):
        self.__waypoint_id = waypoint_id

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status


    
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
