# ****************************************************************************//*
# *   @project  Python NMEA Connector
# *   @file     GBS.py
# *   @brief    GNSS Satellite Fault Detection
# *   @author   Karsten Reitan Sørensen
# *   Date:     11-02-2023
# *******************************************************************************
# @brief    GNSS Satellite Fault Detection
# @param    <1> UTC of position fix
#           This sentence is used to support Receiver Autonomous Integrity Monitoring (RAIM). 
#           Given that a GNSS receiver is tracking enough satellites to perform integrity checks 
#           of the positioning quality of the position solution a sentence is needed to report 
#           the output of this process to other systems to advise the system user. With the RAIM 
#           in the GNSS receiver, the receiver can isolate faults to individual satellites and not
#           use them in its position and velocity calculations.Also, the GNSS receiver can still 
#           track the satellite and easily judge when it is back within tolerance.This sentence 
#           shall be used for reporting this RAIM information. To perform this integrity function, 
#           the GNSS receiver must have at least two observables in addition to the minimum required 
#           for navigation.Normally these observables take the form of additional
#           redundant satellites.
# @param    If only GPS, GLONASS, Galileo, BDS, QZSS, NavIC (IRNSS) is used for the reported position 
#           solution the talker ID is GP, GL, GA, GB, GQ, GI respectively and the errors pertain to 
#           the individual system.If satellites from multiple systems are used to obtain the reported 
#           position solution the talker ID is GN and the errors pertain to the combined solution.


from NMEA0183_Commands import NMEA0183_Command as NMEAMessage


class GBS(NMEAMessage):

    def __init__(self):
        self.__UTCtime = None
        if (NMEAMessage == None or NMEAMessage.Length < 8):
            raise Exception("Invalid GBS: {}".NMEAMessage)
        FixTime = ToTimeSpan(NMEAMessage[0])

        # @brief    Expected Error in latitude
        # Expected error in meters due to bias, with noise = 0
        self.__errorLatitude = None
        LatitudeError = NMEAMessage.ToDouble(NMEAMessage[1])
        #def float LatitudeError():
        #    return LatitudeError

        # @brief    Expected Error in longitude
        # Expected error in meters due to bias, with noise = 0
        self.__errorLongitude = None
        LongitudeError = NMEAMessage.ToDouble(NMEAMessage[2])
        #def float LongitudeError():
        #    return self._LongitudeError

        # @brief    Expected Error in altitude
        # Expected error in meters due to bias, with noise = 0
        self.__errorAltitude = None
        AltitudeError = NMEAMessage.ToDouble(NMEAMessage[3])
        #def float AltitudeError():
        #    return AltitudeError
    
        # @brief    ID number of most likely failed satellite
        # <para>
        # Satellite ID numbers. To avoid possible confusion caused by repetition of satellite ID numbers when using
        # multiple satellite systems, the following convention has been adopted: 
        # <ul>
        # <li>a) GPS satellites are identified by their PRN numbers, which range from 1 to 32.</li>
        # <li>b) The numbers 33-64 are reserved for SBAS satellites. The SBAS system PRN numbers are 120-138.
        # The offset from NMEA SBAS SV ID to SBAS PRN number is 87. A SBAS PRN number of 120
        # minus 87 yields the SV ID of 33. The addition of 87 to the SV ID yields the SBAS PRN number.</li>
        # <li>c) The numbers 65-96 are reserved for GLONASS satellites. GLONASS satellites are identified by
        # 64+satellite slot number.The slot numbers are 1 through 24 for the full GLONASS constellation
        # of 24 satellites, this gives a range of 65 through 88. The numbers 89 through 96 are available if
        # slot numbers above 24 are allocated to on-orbit spares.
        # </li>
        # <li>See Note 3 for other GNSS not listed in a), b), or c) above to determine meaning of satellite ID when Talker ID GN is used</li>
        # </ul>
        # </para>
        # 
        # </remarks>
        self.__satelliteID = None
        SatelliteId = int(NMEAMessage[4])
        #def int SatelliteId():
        #        return SatelliteId

        self.__probability = None
        MissedDetectionProbability = float(NMEAMessage[5])
        # @brief    Probability of missed detection for most likely failed satellite
        #def float MissedDetectionProbability():
        #    return MissedDetectionProbability 

        self.__badSatCount = None

        # @brief    Estimate of bias in meters on most likely failed satellite
        BiasEstimate = NMEAMessage.ToDouble(NMEAMessage[6])
        #def float BiasEstimate():
        #    return BiasEstimate

        # @brief    Standard deviation of bias estimate
        StandardDeviation = NMEAMessage.ToDouble(NMEAMessage[7])
        #def float StandardDeviation():
        #    return StandardDeviation


    def set_UTCtime(self, UTCtime):
        self.__UTCtime = UTCtime

    def get_UTCtime(self):
        return self.__UTCtime

    def set_errorLatitude(self, errorLatitude):
        self.__errorLatitude = errorLatitude

    def get_errorLatitude(self):
        return self.__errorLatitude

    def set_errorLongitude(self, errorLongitude):
        self.__errorLongitude = errorLongitude

    def get_errorLongitude(self):
        return self.__errorLongitude

    def set_errorAltitude(self, errorAltitude):
        self.__errorAltitude = errorAltitude

    def get_errorAltitude(self):
        return self.__errorAltitude

    def set_satelliteID(self, satelliteID):
        self.__satelliteID = satelliteID

    def get_satelliteID(self):
        return self.__satelliteID

    def set_probability(self, probability):
        self.__probability = probability

    def get_probability(self):
        return self.__probability

    def set_badSatCount(self, badSatCount):
        self.__badSatCount = badSatCount

    def get_badSatCount(self):
        return self.__badSatCount


    # @brief    UTC time of the GGA or GNS fix associated with this sentence.
    # @return   The fix time.
    # TimeSpan ITimestampedMessage.Timestamp => FixTime
    def FixTime(): 
        return FixedTime

