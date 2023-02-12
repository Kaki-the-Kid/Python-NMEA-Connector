# ***************************************************************************//*
# @project  Python NMEA Connector
# @file     XTE.py
# @brief    Cross Track Error, Measured
# @author   Karsten Reitan Sørensen
# @Date:    11-02-2023
# *******************************************************************************
# @brief    Local geodetic datum and datum offsets from a reference datum.
# @details  This sentence is used to define the datum to which a position location and geographic 
#           locations in subsequent sentences, is referenced. Latitude, longitude and altitude 
#           offsets from the reference datum, and the selection of reference datum, are also 
#           provided.
# @param    This sentence is used to define the datum to which a position location and geographic
#           locations in subsequent sentences, is referenced. Latitude, longitude and altitude 
#           offsets from the reference datum, and the selection of reference datum, are also 
#           provided.
# @param    The datum sentence should be transmitted immediately prior to every positional sentence 
#           (e.g., <c>GLL</c>, <c>BWC</c>, <c>WPL</c>) that is referenced to a datum other than 
#           WGS84, which is the datum recommended by IMO.
# @param    For all datums the DTM sentence should be transmitted prior to any datum change and 
#           periodically at intervals of not greater than 30 seconds.
# *******************************************************************************

from NMEA0183_Commands import NMEA0183_Command


class DBT(NMEA0183_Command):

    def __init__(self, depth=None, depth_feet=None, offset=None):
        self.depth = depth
        self.depth_feet = depth_feet
        self.offset = offset
    
    @property
    def depth(self):
        return self._depth
    
    @depth.setter
    def depth(self, depth):
        self._depth = depth
    
    @property
    def depth_feet(self):
        return self._depth_feet
    
    @depth_feet.setter
    def depth_feet(self, depth_feet):
        self._depth_feet = depth_feet
    
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
        return f"NMEA0183_Command_DTM"
    
    def __repr__(self) -> str:
        return f"NMEA0183_Command_DTM()"
