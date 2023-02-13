# ****************************************************************************//*
# *   @project  Python NMEA Connector
# *   @file     RTE.py
# *   @brief    Routes
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

        /************************************************************************
         * RTE - Routes
         * RTE is sent to indicate the names of the waypoints used in an active route.
         * There are two types of RTE sentences. This route sentence can list all of
         * the waypoints in the entire route or it can list only those still ahead.
         * Because an NMEA sentence is limited to 80 characters there may need to be
         * multiple sentences to identify all of the waypoints. The data about the
         * waypoints themselves will be sent in subsequent WPL sentences which will
         * be sent in future cycles of the NMEA data.
         *
         *        1   2   3 4    5           x    n
         *        |   |   | |    |           |    |
         * $--RTE,x.x,x.x,a,c--c,c--c, ..... c--c*hh<CR><LF>
         *
         * Field Number:
         *
         * 1. Total number of RE sentences being transmitted
         * 2. Sentence Number
         * 3. Sentence mode
         *      c = complete route, all waypoints
         *      w = working route, the waypoint you just left, the waypoint
         *          you’re heading to, then all the rest
         * 4. Route ID
         * 5. Waypoint ID
         * x. Additiobal waypint IDs
         * More waypoints follow. Last field is a checksum as usual.
         *
         * The Garmin 65 and possibly other units report a $GPR00 in the same format.
         *
         * Example: $GPRTE,1,1,c,0*07
         *
         ************************************************************************/
        public void commandGarminRTE()
        {
            //
        }



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
