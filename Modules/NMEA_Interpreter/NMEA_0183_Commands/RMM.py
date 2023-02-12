# ****************************************************************************//*
# @project  Python NMEA Connector
# @title:   NMEA0183 RMM Command
# @file     RMM.py
# @brief    Recommended minimum navigation information
# @author   Karsten Reitan Sørensen
# @created: 11-02-2023
# *******************************************************************************
# The RMM Command is used to share navigation information between devices on 
# the network and can be used to help other devices determine their position 
# and improve navigation accuracy.
# *******************************************************************************
# NMEA 0183 is a standard for communicating marine data between various navigation 
# devices and systems. The RMM (Recommended Minimum Navigation Information) Command 
# is a specific type of NMEA 0183 message that provides navigation information to 
# other devices on the network. The RMM Command contains the following attributes:
#
# * Message ID: 
#   A two-letter identifier that indicates the type of message being sent. For the RMM Command, 
#   the Message ID is "AP".
# * UTC Time:
#   The Coordinated Universal Time (UTC) of the device sending the message.
# * Latitude:
#   The latitude of the device sending the message, in decimal degrees.
# * Latitude Hemisphere: 
#   The hemisphere in which the latitude is located, either "N" for North or "S" for South.
# * Longitude:
#   The longitude of the device sending the message, in decimal degrees.
# * Longitude Hemisphere:
#   The hemisphere in which the longitude is located, either "E" for East or "W" for West.
# * Speed Over Ground:
#   The speed of the device over the ground, in knots.
# * Course Over Ground:
#   The course of the device over the ground, in degrees.
# * Variation:
#   The magnetic variation at the device's location, in degrees.
# * Variation Hemisphere:
#   The hemisphere in which the variation is located, either "E" for East or "W" for West.
# * Mode Indicator:
#   An indicator of the device's navigation mode, either "A" for autonomous, "D" for 
#   differential, or "E" for estimated.
#
# Example:
# $GPRMM,A,4916.45,N,12311.12,W,225444,A*35
# *******************************************************************************

from NMEA0183_Commands import NMEA0183_Command


class RMM(NMEA0183_Command):
    
    def __init__(self, sentence):
        self._datasentence = sentence.split(',')
        
        self.__mode_indicator = None
        self.__cross_track_error = None
        self.__direction_to_steer = None
        self.__arrival_circle_entered = None
        
        
        
    # Make setter and getter for each field
    def __init__(self):
        self.__status = None
        self.__latitude = None
        self.__longitude = None
        self.__time_difference_A = None
        self.__time_difference_B = None
        self.__speed = None
        self.__course = None
        self.__magnetic_variation = None
        self.__mode = None
        
        
        #   A two-letter identifier that indicates the type of message being sent. For the RMM Command, 
        # * Message ID: the Message ID is "AP".
        
        # * UTC Time:
        #   The Coordinated Universal Time (UTC) of the device sending the message.
        
        # * Latitude:
        #   The latitude of the device sending the message, in decimal degrees.

        # * Latitude Hemisphere: 
        #   The hemisphere in which the latitude is located, either "N" for North or "S" for South.

        # * Longitude:
        #   The longitude of the device sending the message, in decimal degrees.

        # * Longitude Hemisphere:
        #   The hemisphere in which the longitude is located, either "E" for East or "W" for West.

        # * Speed Over Ground:
        #   The speed of the device over the ground, in knots.

        # * Course Over Ground:
        #   The course of the device over the ground, in degrees.

        # * Variation:
        #   The magnetic variation at the device's location, in degrees.

        # * Variation Hemisphere:
        #   The hemisphere in which the variation is located, either "E" for East or "W" for West.

        # * Mode Indicator:
        #   An indicator of the device's navigation mode, either "A" for autonomous, "D" for 
        #   differential, or "E" for estimated.
    
    def set_mode_indicator(self, mode_indicator):
        self.__mode_indicator = mode_indicator

    def get_mode_indicator(self):
        return self.__mode_indicator

    def set_cross_track_error(self, cross_track_error):
        self.__cross_track_error = cross_track_error

    def get_cross_track_error(self):
        return self.__cross_track_error

    def set_direction_to_steer(self, direction_to_steer):
        self.__direction_to_steer = direction_to_steer

    def get_direction_to_steer(self):
        return self.__direction_to_steer

    def set_arrival_circle_entered(self, arrival_circle_entered):
        self.__arrival_circle_entered = arrival_circle_entered

    def get_arrival_circle_entered(self):
        return self.__arrival_circle_entered

    @property   
    def status(self):
        return self.__status    
    
    @status.setter
    def status(self, value):
        self.__status = value       

    def test_command():
        testsentence = []
        testsentence.append("$GPRMM,A,4916.45,N,12311.12,W,225444,A*35")
        
        return testsentence