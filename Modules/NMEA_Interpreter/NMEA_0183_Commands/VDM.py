# ****************************************************************************//*
# *   @project  Python NMEA Connector
# *   @file     BWC.py
# *   @brief    Cross Track Error, Measured
# *   @author   Karsten Reitan Sørensen
# *   Date:     11-02-2023
# *******************************************************************************

from NMEA0183_Commands import NMEA0183_Command as NMEAMessage


class VDM(NMEAMessage):
    
    def __init__(self, NMEAMessage):
        
        self.__message_id = ""
        self.__total_number_of_sentences = 0
        self.__sentence_number = 0
        self.__sequential_message_id = 0
        self.__data = ""
        self.__checksum = ""
    
    def get_message_id(self):
        return self.__message_id
    
    def set_message_id(self, message_id):
        self.__message_id = message_id
    
    def get_total_number_of_sentences(self):
        return self.__total_number_of_sentences
    
    def set_total_number_of_sentences(self, total_number_of_sentences):
        self.__total_number_of_sentences = total_number_of_sentences
    
    def get_sentence_number(self):
        return self.__sentence_number
    
    def set_sentence_number(self, sentence_number):
        self.__sentence_number = sentence_number
    
    def get_sequential_message_id(self):
        return self.__sequential_message_id
    
    def set_sequential_message_id(self, sequential_message_id):
        self.__sequential_message_id = sequential_message_id
    
    def get_data(self):
        return self.__data
    
    def set_data(self, data):
        self.__data = data
    
    def get_checksum(self):
        return self.__checksum
    
    def set_checksum(self, checksum):
        self.__checksum = checksum
    
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
        return f"NMEA0183_Command_VDM"
    
    def __repr__(self) -> str:
        return f"NMEA0183_Command_VDM()"
