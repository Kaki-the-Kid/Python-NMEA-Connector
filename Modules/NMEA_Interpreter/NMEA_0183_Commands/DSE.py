# ****************************************************************************//*
# *   @project  Python NMEA Connector
# *   @file     DSE.py
# *   @brief    DSE - Distance to Waypoint, Loran-C
# *   @author   Karsten Reitan Sørensen
# *   Date:     11-02-2023
# *******************************************************************************

from NMEA0183_Commands import NMEA0183_Command as NMEAMessage


class DSE(NMEAMessage):
    
    def __init__(self, NMEAMessage) -> None:
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
        return f"NMEA0183_Command_DSE"
    
    def __repr__(self) -> str:
        return f"NMEA0183_Command_DSE()"
