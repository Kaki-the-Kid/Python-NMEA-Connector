# ****************************************************************************//*
# *   @project  Python NMEA Connector
# *   @file     MWV.py
# *   @brief    MWV Command provides information on wind speed and angle
# *   @author   Karsten Reitan Sørensen
# *   Date:     11-02-2023
# *******************************************************************************
# The NMEA 0183 MWV (Wind Speed and Angle) Command is a specific type of NMEA 0183 
# message that provides information on the speed and angle of the wind. The MWV 
# Command contains the following attributes:
#
# - Message ID: 
#   A two-letter identifier that indicates the type of message being sent. For the 
#   MWV Command, the Message ID is "MW".
# - Wind Angle:
#   The angle of the wind, in degrees.
# - Reference:
#   A single-letter identifier that indicates the reference for the wind angle,
#   either "R" for relative or "T" for true.
# - Wind Speed:
#   The speed of the wind, in knots.
# - Unit of Speed:
#   A single-letter identifier that indicates the units of the wind speed, either
#   "N" for knots or "K" for kilometers per hour.
# - Status:
#   An indicator of the status of the wind data, either "A" for valid or "V" for
#   invalid.
#   
# Example: $IIMWV,054.7,R,003.3,N,A*3D
# *******************************************************************************

from NMEA0183_Commands import NMEA0183_Command


class MWV(NMEA0183_Command):
    
    def __init__(self, sentence):
        self._datasentence = sentence.split(',')
        # Message ID: "MW".
        self._message_id = self._datasentence[0]
        if(self._message_id != '$IIMWV' or self._message_id < 6):
            raise Exception('Invalid MWV Sentece: {}'.self._datasentence)
        
        # Wind Angle: The angle of the wind, in degrees.
        self._wind_angle = self._datasentence[1]
        
        # Reference: single-letter identifier reference wind angle, "R" for relative or "T" for true
        self._reference_wind_angle = self._datasentence[2]
        
        # Wind Speed: The speed of the wind, in knots.
        self._wind_speed = self._datasentence[3]
        
        # Unit of Speed: single-letter identifier "N" knots or "K" km/h
        self._unit_speed = self._datasentence[4]
        
        # Status: the status of the wind data, either "A" valid or "V" invalid.
        self._status_wind_data = self._datasentence[5]

        
    @property
    def get_message_id(self):
        return self._message_id
    
    @message_id.setter
    def set_message_id(self, message_id):
        self._message_id = message_id
        
    
    
    
 



    def test_code(self):
        self.MWV_Wind_Speed = 3.3
        self.MWV_Wind_Angle = 54.7
        self.MWV_Reference = 'R'
        self.test_code() 
        
        print("MWV_Wind_Speed: ", self.MWV_Wind_Speed)
        print("MWV_Wind_Angle: ", self.MWV_Wind_Angle)
        print("MWV_Reference: ", self.MWV_Reference)
        
    def __str__(self):
        return "MWV_Wind_Speed: " + str(self.MWV_Wind_Speed) + " MWV_Wind_Angle: " + str(self.MWV_Wind_Angle) + " MWV_Reference: " + str(self.MWV_Reference)
   
    def test_command(self):
        
        testsentence = []
        
        # Here are three examples of NMEA 0183 MWV Command messages:
        testsentence.append("$IIMWV,054.7,R,003.3,N,A*3D")
        
        testsentence.append("$WIMWV,275,T,7.5,N,A*1D")
        # This message indicates that the wind is coming from a true angle of 
        # 275 degrees, with a speed of 7.5 knots, and the data is valid.
        
        testsentence.append("$WIMWV,135,R,8.3,K,A*26")
        # This message indicates that the wind is coming from a relative angle of
        # 135 degrees, with a speed of 8.3 kilometers per hour, and the data is
        # valid.

        testsentence.append("$WIMWV,0,R,0,N,V*34")
        # This message indicates that the wind is coming from a relative angle of 
        # 0 degrees, with a speed of 0 knots, and the data is invalid.
        
        return testsentence
