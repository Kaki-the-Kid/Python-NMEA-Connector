# ****************************************************************************//*
# *   @project  Python NMEA Connector
# *   @file     GST.py
# *   @brief    Pseudorange error statistics
# *   @author   Karsten Reitan Sørensen
# *   Date:     11-02-2023
# *******************************************************************************

from NMEA0183_Commands import NMEA0183_Command as NMEAMessage


# Pseudorange error statistics
class GST(NMEAMessage):
    
    def __init__(self, NMEAMessage, time_of_day, rms_value, semi_major_deviation, semi_minor_deviation, semi_major_orientation, lat_error_deviation, lon_error_deviation, alt_error_deviation):
        self.__message = NMEAMessage
        
        if (NMEAMessage == None or NMEAMessage.Length < 8):
            raise Exception("Invalid GST: {}".NMEAMessage)
        
        # UTC of position fix
        FixTime = StringToTimeSpan(NMEAMessage[0])
        #public TimeSpan FixTime { get }
        
        def StringToTimeSpan():
            pass
        
        # RMS value of the standard deviation of the range inputs in the navigation process. Range inputs include pseudoranges and DGNSS corrections.
        Rms = float(NMEAMessage[1])
        #public double Rms { get }

        # Standard deviation of semi-major axis of error ellipse in meters.
        SemiMajorError = float(NMEAMessage[2])
        #public double SemiMajorError { get }

        # Standard deviation of semi-minor axis of error ellipse in meters.
        SemiMinorError = float(NMEAMessage[3])
        #public double SemiMinorError { get }
        
        # Orientation of semi-major axis of error ellipse (degrees from true north).
        ErrorOrientation = float(NMEAMessage[4])
        #public double ErrorOrientation { get }
        
        # Standard deviation of latitude error in meters.
        SigmaLatitudeError = float(NMEAMessage[5])
        #public double SigmaLatitudeError { get }
        
        # Standard deviation of longitude error in meters.
        SigmaLongitudeError = float(NMEAMessage[6])
        #public double SigmaLongitudeError { get }

        # Standard deviation of altitude error in meters.
        SigmaHeightError = float(NMEAMessage[7])
        #public double SigmaHeightError { get }
        

    @property
    def NMEAMessage(self):
        return self.__message

    @NMEAMessage.setter
    def NMEAMessage(self, value):
        self.__message = value

    @property
    def time_of_day(self):
        return self.__time_of_day

    @time_of_day.setter
    def time_of_day(self, value):
        self.__time_of_day = value

    @property
    def rms_value(self):
        return self.__rms_value

    @rms_value.setter
    def rms_value(self, value):
        self.__rms_value = value

    @property
    def semi_major_deviation(self):
        return self.__semi_major_deviation

    @semi_major_deviation.setter
    def semi_major_deviation(self, value):
        self.__semi_major_deviation = value

    @property
    def semi_minor_deviation(self):
        return self.__semi_minor_deviation

    @semi_minor_deviation.setter
    def semi_minor_deviation(self, value):
        self.__semi_minor_deviation = value

    @property
    def semi_major_orientation(self):
        return self.__semi_major_orientation

    @semi_major_orientation.setter
    def semi_major_orientation(self, value):
        self.__semi_major_orientation = value

    @property
    def latitude_error_deviation(self):
        return self.__latitude_error_deviation

    @latitude_error_deviation.setter
    def latitude_error_deviation(self, value):
        self.__latitude_error_deviation = value

    @property
    def longitude_error_deviation(self):
        return self.__longitude_error_deviation

    @longitude_error_deviation.setter
    def longitude_error_deviation(self, value):
        self.__longitude_error_deviation = value

    @property
    def altitude_error_deviation(self):
        return self.__altitude_error_deviation

    @altitude_error_deviation.setter
    def altitude_error_deviation(self, value):
        self.__altitude_error_deviation = value
