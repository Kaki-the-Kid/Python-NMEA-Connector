# *************************************************************************************************
# (BOD) message class
# @brief    Bearing - Origin to Destination (BOD) message class
# @brief    Bearing - Origin to Destination 
# Path: Modules\NMEA_Interpreter\NMEA_0183_Commands\BOD.py
#
# Bearing angle of the line, calculated at the origin waypoint, extending to the destination
# waypoint from the origin waypoint for the active navigation leg of the journey
# This sentence is transmitted at intervals not exceeding 2-seconds and is always accompanied by 
# <see cref="Rmb"/> when a destination waypoint is active.
# **********************************************************************************************//*
# @brief    Local geodetic datum and datum offsets from a reference datum.
# @details  This sentence is used to define the datum to which a position location and geographic 
#           locations in subsequent sentences, is referenced. Latitude, longitude and altitude 
#            offsets from the reference datum, and the selection of reference datum, are also 
#           provided.
# @param    This sentence is used to define the datum to which a position location and geographic
#           locations in subsequent sentences, is referenced. Latitude, longitude and altitude offsets
#            from the reference datum, and the selection of reference datum, are also provided.
# @param    The datum sentence should be transmitted immediately prior to every positional sentence (e.g., <c>GLL</c>, 
# <c>BWC</c>, <c>WPL</c>) that is referenced to a datum other than WGS84, which is the datum recommended by IMO.
# </para>
# @param    For all datums the DPT sentence should be transmitted prior to any datum change and periodically at
#           intervals of not greater than 30 seconds.

from NMEA0183_Commands import NMEA0183_Command


class DPT(NMEA0183_Command):
    
    def __init__(self, depth=None, offset=None, NMEA0183_Command=None):
        if (NMEA0183_Command == None or NMEA0183_Command.Length < 8):
            raise Exception("Invalid DPT: {}".NMEA0183_Command)

        self.depth = depth
        self.offset = offset
    
    @property
    def depth(self):
        return self._depth
    
    @depth.setter
    def depth(self, depth):
        self._depth = depth
    
    @property
    def offset(self):
        return self._offset
    
    @offset.setter
    def offset(self, offset):
        self._offset = offset

    def __init__(self) -> None:
        super().__init__()
        
    def send(self, command: str, data: str) -> str:
        return super().send(command, data)
    
    def receive(self, data: str) -> str:
        return super().receive(data)
    
    def checksum(self, data: str) -> str:
        return super().checksum(data)
    
    def validate(self, data: str) -> bool:
        return super().validate(data)
    
    def parse(self, data: str) -> str:
        return super().parse(data)
    
    def __str__(self) -> str:
        return f"NMEA0183_Command_DPT"
    
    def __repr__(self) -> str:
        return f"NMEA0183_Command_DPT()"
