# ****************************************************************************//*
# *   @project  Python NMEA Connector
# *   @file     RPM.py
# *   @brief    RPM Command provides information on rpm of a vessel's propellers
# *   @author   Karsten Reitan Sørensen
# *   Date:     11-02-2023
# *******************************************************************************
# RPM (Revolutions) Command is a specific type of NMEA 0183 message that provides 
# information on the revolutions per minute (RPM) of a vessel's propellers, which 
# can be used to help other devices determine the vessel's speed and improve 
# navigation accuracy. It can also be used to monitor the performance of the vessel's 
# propulsion system and to detect faults or problems. The information contained in 
# the RPM Command is critical for safe navigation, as it allows other devices on 
# the network to determine the vessel's speed and respond accordingly.
# 
# The RPM Command contains the following attributes:
#
# - Message ID: 
#   A two-letter identifier that indicates the type of message being sent. For the 
#   RPM Command, the Message ID is "AP".
# - Source ID:
#   A single-letter identifier that indicates the source of the RPM data, either "P" 
#   for port or "S" for starboard.
# - Engine Speed:
#   The speed of the engine, in revolutions per minute.
# - Propulsion Flag:
#   A single-letter identifier that indicates the propulsion status of the engine,
#   either "F" for forward or "R" for reverse.
# - Status:
#   An indicator of the status of the RPM data, either "A" for valid or "V" for
#   invalid.
#
# *******************************************************************************

from NMEA0183_Commands import NMEA0183_Command


class RPM(NMEA0183_Command):
    
    def init(self, sentence):
        self._datasentence = sentence.split(',')
        
        # - Message ID: 
        if (self._datasentence.length < 5):
            raise Exception("Invalid RPM sentence: {}".sentence)
            
        self._messageid = self._datasentence[0]
        # - Source ID:
        self._sourceid = self._datasentence[1]
        # - Engine Speed:
        self._enginespeed = self._datasentence[2]
        # - Propulsion Flag:
        self._propulsion = self._datasentence[3]        
        # - Status:
        self._status = self._datasentence[4]
        
    # Getter function for source
    @property
    def source(self):
        return self.__source

    # Setter function for source
    @source.setter
    def source(self, source):
        self.__source = source

    # Getter function for direction
    @property
    def direction(self):
        return self.__direction

    # Setter function for direction
    @direction.setter
    def direction(self, direction):
        self.__direction = direction

    # Getter function for revolutions
    @property
    def revolutions(self):
        return self.__revolutions

    # Setter function for revolutions
    @revolutions.setter
    def revolutions(self, revolutions):
        self.__revolutions = revolutions

