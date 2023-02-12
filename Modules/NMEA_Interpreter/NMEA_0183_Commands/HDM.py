# ****************************************************************************//*
# *   @project  Python NMEA Connector
# *   @file     HDM.py
# *   @brief    Heading, Magnetic
# *   @author   Karsten Reitan Sørensen
# *   Date:     11-02-2023
# *******************************************************************************
# Dual Ground/Water Distance
# The distance traveled, relative to the water and over the ground.
# Initializes a new instance of the see VLV class.
#
#
# Here is an example of the HDM NMEA command:
#
# $IIHDM,123.4,M*22
# 
# In this example, "II" is the Talker ID, indicating that the source of the command is 
# integrated instrumentation. The "HDM" is the sentence identifier for the Heading Magnetic 
# command. The 123.4 is the heading in degrees magnetic, and the "M" indicates that the 
# heading is in magnetic units. The "*22" is the checksum, used to verify the integrity of 
# the transmission.
# *******************************************************************************

from NMEA0183_Commands import NMEA0183_Command as NMEAMessage


class HDM(NMEAMessage):

    def __init__(self, sentence):
        self._sentence = sentence
        self._datasentence = sentence.split(',')
        if (_datasentence == null or _datasentence.Length < 7):
            raise Exception("Invalid HDM: {}".sentence)
        
        self._talker_id = NMEAMessage[1:3]
        self._heading_magnetic = float(NMEAMessage[3:9])

    def get_talker_id(self):
        return self._talker_id

    def set_talker_id(self, _talker_id):
        self._talker_id = _talker_id

    def get_heading_magnetic(self):
        return self._heading_magnetic

    def set_heading_magnetic(self, _heading_magnetic):
        self._heading_magnetic = _heading_magnetic    

    def __str__(self):
        return 'HDM: Heading: {}, Reference: {}'.format(self.__heading, self.__reference)
    
    def NMEAtest():
        teststring= []
        teststring.append("$IIHDM,123.4,M*22")
        teststring.append("$GPHDM,100.0,M*15")
        
        super.test(teststring)
