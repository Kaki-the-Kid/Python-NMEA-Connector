# ****************************************************************************//*
# *   @project  Python NMEA Connector
# *   @file     ROT.py
# *   @brief    Rate of Turn
# *   @author   Karsten Reitan Sørensen
# *   Date:     11-02-2023
# *******************************************************************************
# The ROT Command is used to provide information on the rate of turn of a vessel, 
# which can be used to help other devices determine the vessel's course and improve 
# navigation accuracy. It can also be used to provide information on the vessel's 
# stability and to detect the presence of rogue waves. The information contained in 
# the ROT Command is critical for safe navigation, as it allows other devices on the 
# network to determine the vessel's turn rate and respond accordingly.
# 
# The NMEA 0183 ROT (Rate of Turn) Command is a specific type of NMEA 0183 
# message that provides information on the rate of turn of a vessel. The ROT 
# Command contains the following attributes:
#
# - Message ID: 
#   A two-letter identifier that indicates the type of message being sent. For the ROT Command, the Message ID is "AP".
# - Rate of Turn: 
#   The rate of turn of the vessel, in degrees per minute, where positive values indicate a turn to starboard and negative values indicate a turn to port.
# - Status: 
#   An indicator of the status of the rate of turn data, either "A" for valid or "V" for invalid.
#
# *******************************************************************************

from NMEA0183_Commands import NMEA0183_Command


class ROT(NMEAMessage):
    
    def __init__(self, sentence):
        self._datasentence = sentence.split(',')
        if (self._datasentence.lenght != 3): # Check if the sentence is valid
            raise Exception("Invalid ROT sentence: {}".sentence)
            self._valid = False
        # Message ID: 
        self._messageid = self._datasentence[0]
        # Rate of Turn: 
        self._rot = self._datasentence[1]
        # Status: 
        self._status = self._datasentence[2]
    
    
    def set_messageid(self, messageid):
        self._messageid = messageid
        
    def get_messageid(self):
        return self._messageid
        
    def set_rot(self, rot):
        self._rot = rot
    
    def get_rot(self):
        return self._rot
    
    def set_status(self, status):
        self._status = status
        
    def get_status(self):
        return self._status

    def test_code():
        # create a new rate of turn object
        rot = ROT()

        # set the rate of turn value
        rot.set_rot(10.0)

        # get the rate of turn value
        print("Rate of Turn: ", rot.get_rot())
        
    def test_command():
        testsentence = []
        # Here are three examples of NMEA 0183 ROT Command messages:
        
        testsentence.append("$APROT,0.03,A*29")
        # This message indicates that the vessel is turning at a rate of 0.03 degrees 
        # per minute to starboard, and the data is valid.

        testsentence.append("$APROT,-0.02,A*2B")
        # This message indicates that the vessel is turning at a rate of -0.02 degrees 
        # per minute to port, and the data is valid.

        testsentence.append("$APROT,0.00,V*3C")
        # This message indicates that the vessel is not turning, and the data is invalid.
        
        return testsentence
