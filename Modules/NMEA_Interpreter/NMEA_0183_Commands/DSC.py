# ****************************************************************************//*
# @project  Python NMEA Connector
# @file     DSC.py
# @brief    
# @author   Karsten Reitan Sørensen
# @date:     11-02-2023
# *******************************************************************************

from NMEA0183_Commands import NMEA0183_Command as NMEAMessage


class DSC(NMEAMessage):

    def __init__(self, mmsi=None, message_type=None):
        self.mmsi = mmsi
        self.message_type = message_type
    
    @property
    def mmsi(self):
        return self._mmsi
    
    @mmsi.setter
    def mmsi(self, mmsi):
        self._mmsi = mmsi
    
    @property
    def message_type(self):
        return self._message_type
    
    @message_type.setter
    def message_type(self, message_type):
        self._message_type = message_type

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
        return f"NMEA0183_Command_DSC"
    
    def __repr__(self) -> str:
        return f"NMEA0183_Command_DSC()"
