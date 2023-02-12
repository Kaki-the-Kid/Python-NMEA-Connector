# ****************************************************************************//*
# *   @project  Python NMEA Connector
# *   @file     RTZ
# *   @brief    Return To Base Track Made Good and Ground Speed
# *   @author   Karsten Reitan Sørensen
# *   Date:     11-02-2023
# *******************************************************************************
# The NMEA 0183 RTZ (Return to Base Track Made Good and Ground Speed) Command is 
# a specific type of NMEA 0183 message that provides information on the vessel's 
# progress towards its base (starting) track and its ground speed. 
#
# The RTZ Command is used to provide information on the vessel's progress towards 
# its base (starting) track and its ground speed. This information can be used to 
# improve navigation accuracy and to monitor the vessel's performance. The RTZ 
# Command can also be used to alert the operator if the vessel deviates from its 
# intended course, helping to ensure that the vessel stays on course and arrives 
# at its destination safely.
# 
# The RTZ Command contains the following attributes:
#
# - Message ID: 
#   A two-letter identifier that indicates the type of message being sent. For the 
#   RTZ Command, the Message ID is "RT".
# - Status: 
#   A single-letter identifier that indicates the status of the RTZ data, either "A" 
#   for valid or "V" for invalid.
# - Track Made Good:
#   The track made good towards the base (starting) track, in degrees.
# - Base Track Course:
#   The course of the base (starting) track, in degrees.
# - Ground Speed: 
#   The speed of the vessel over the ground, in knots.
# - Date:
#   The date of the RTZ Command, in the format DDMMYY.
#
# Example:
# $GPRTZ
# *****************************************************************************



from NMEA0183_Commands import NMEA0183_Command as  NMEAMessage


class RTE(NMEAMessage):
    
    def __init__(self, NMEAMessage):
        if (NMEAMessage == null or NMEAMessage.Length < 4):
            raise Exception("Invalid RTE: {}".NMEAMessage)
        
        self._message_type = "$GPRTE"
        self._total_messages = None
        self._message_number = None
        self._route_type = None
        self._route_waypoint_ids = []
        
        ListType = WaypointListType.CompleteWaypointsList if (NMEAMessage[2] == "c") else WaypointListType.RemainingWaypointsList
        RouteId = NMEAMessage[3]

    @property
    def message_type(self):
        return self._message_type

    @message_type.setter
    def message_type(self, value):
        self._message_type = value

    @property
    def total_messages(self):
        return self._total_messages

    @total_messages.setter
    def total_messages(self, value):
        self._total_messages = value

    @property
    def message_number(self):
        return self._message_number

    @message_number.setter
    def message_number(self, value):
        self._message_number = value

    @property
    def route_type(self):
        return self._route_type

    @route_type.setter
    def route_type(self, value):
        self._route_type = value

    @property
    def route_waypoint_ids(self):
        return self._route_waypoint_ids

    @route_waypoint_ids.setter
    def route_waypoint_ids(self, value):
        self._route_waypoint_ids = value

    
    _waypoints = []

    # Waypoint tpe   
    def WaypointListType(Enum):
        CompleteWaypointsList  = [], # Complete list of waypoints
        RemainingWaypointsList = [], # List of remaining waypoints


    def ParseSentences( talker, NMEAMessage = [] ):
        global _waypoints
        
        if ( self.MessageParts[2] != NMEAMessage[2] or self.MessageParts[3] != NMEAMessage[3] ):
            return False
            
        _waypoints.AddRange(NMEAMessage.Skip(4))
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
