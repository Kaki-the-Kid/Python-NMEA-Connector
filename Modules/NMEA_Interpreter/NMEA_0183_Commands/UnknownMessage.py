# ****************************************************************************//*
# *   @project  Python NMEA Connector
# *   @file     UnknownMessage.py
# *   @brief    Unknown message type
# *   @author   Karsten Reitan Sørensen
# *   Date:     11-02-2023
# *******************************************************************************

from NMEA0183_Commands import NMEA0183_Command as NMEAMessage


class UnknownMessage(NMEAMessage):

    # Represents an unknown message type
    def UnknownMessage(string type, string[] messageParts):
        pass

    # Gets the nmea value array.
    def IReadOnlyList():
        return MessageParts
