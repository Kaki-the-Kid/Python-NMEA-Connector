# ****************************************************************************//*
# *   @project  Python NMEA Connector
# *   @file     BWC.py
# *   @brief    Cross Track Error, Measured
# *   @author   Karsten Reitan Sørensen
# *   Date:     11-02-2023
# *******************************************************************************

from NMEA0183_Commands import NMEA0183_Command


class BWC(NMEA0183_Command):
# *******************************************************************************
# *  Licensed under the Apache License, Version 2.0 (the "License")
# *  you may not use this file except in compliance with the License.
# *  You may obtain a copy of the License at
# *
# *  http://www.apache.org/licenses/LICENSE-2.0
# *
# *   Unless required by applicable law or agreed to in writing, software
# *   distributed under the License is distributed on an "AS IS" BASIS,
# *   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# *   See the License for the specific language governing permissions and
# *   limitations under the License.
# ******************************************************************************

from NMEA0183_Commands import NMEA0183_Command
    
# Routes

# <remarks>
# Waypoint identifiers, listed in order with starting waypoint first, for the identified route. Two modes of
# transmission are provided: 'c' indicates that the complete list of waypoints in the route are being
# transmitted 'w' indicates a working route where the first listed waypoint is always the last waypoint
# that had been reached (FROM), while the second listed waypoint is always the waypoint that the vessel is
# currently heading for (TO), the remaining list of waypoints represents the remainder of the route. 
# </remarks>
from Modules.NMEA_Interpreter.NMEA_0183_Commands.c_NMEA_Messages import NMEAMessage


class RTE(NMEAMessage):
    class ROT:
    def __init__(self):
        self.__rot = 0.0
    
    def set_rot(self, rot):
        self.__rot = rot
    
    def get_rot(self):
        return self.__rot
    
rot = ROT()

# set the rate of turn value
rot.set_rot(10.0)

# get the rate of turn value
print("Rate of Turn: ", rot.get_rot())

    
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
