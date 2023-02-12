# ****************************************************************************//*
# *   @project  Python NMEA Connector
# *   @file     XTE.py
# *   @brief    Cross Track Error, Measured
# *   @author   Karsten Reitan Sørensen
# *   Date:     11-02-2023
# *******************************************************************************

from NMEA0183_Commands import NMEA0183_Command


class XTE(NMEA0183_Command):
    def __init__(self, NMEAMessage):
        self.__status = ""
        self.__cross_track_error_magnitude = 0.0
        self.__direction_to_steer = ""
        self.__cross_track_unit = ""

    # Getter for status
    @property
    def status(self):
        return self.__status
    
    # Setter for status
    @status.setter
    def status(self, status):
        self.__status = status

    # Getter for cross_track_error_magnitude
    @property
    def cross_track_error_magnitude(self):
        return self.__cross_track_error_magnitude
    
    # Setter for cross_track_error_magnitude
    @cross_track_error_magnitude.setter
    def cross_track_error_magnitude(self, cross_track_error_magnitude):
        self.__cross_track_error_magnitude = cross_track_error_magnitude

    # Getter for direction_to_steer
    @property
    def direction_to_steer(self):
        return self.__direction_to_steer
    
    # Setter for direction_to_steer
    @direction_to_steer.setter
    def direction_to_steer(self, direction_to_steer):
        self.__direction_to_steer = direction_to_steer

    # Getter for cross_track_unit
    @property
    def cross_track_unit(self):
        return self.__cross_track_unit
    
    # Setter for cross_track_unit
    @cross_track_unit.setter
    def cross_track_unit(self, cross_track_unit):
        self.__cross_track_unit = cross_track_unit

    # Recommended minimum specific Loran-C Data
    # Position, course and speed data provided by a Loran-C receiver. Time differences A and B are 
    # those used in computing latitude/longitude.
    # This sentence is transmitted at intervals not exceeding 2-seconds and is always accompanied 
    # by <see cref="Rmb"/> when a destination waypoint is active.
        
        # Positioning system status field
        def PositioningStatus(Enum):
            # Data not valid
            Invalid = 0
            # Autonomous
            Autonomous = 1
            # Differential
            Differential = 2
            # Estimated (dead reckoning)
            Estimated = 6
        
        # Positioning system mode indicator
        def PositioningMode(Enum):
            # Data not valid
            NotValid = 0,
            # Autonomous mode
            Autonomous = 1,
            # Differential mode
            Differential = 2,
            # Estimated (dead reckoning) mode
            Estimated = 6,
            # Manual input mode
            Manual = 8,
            # Simulator mode
            Simulator = 9,
        