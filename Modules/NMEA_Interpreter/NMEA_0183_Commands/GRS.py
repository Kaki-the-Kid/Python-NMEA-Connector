# ****************************************************************************//*
# *   @project  Python NMEA Connector
# *   @file     GRS.py
# *   @brief    GNSS Range Residuals
# *   @author   Karsten Reitan Sørensen
# *   Date:     11-02-2023
# *******************************************************************************
# GNSS Range Residuals
# <remarks>
# <para>
# This sentence is used to support Receiver Autonomous Integrity Monitoring (RAIM). Range residuals can be
# computed in two ways for this process. The basic measurement integration cycle of most navigation filters
# generates a set of residuals and uses these to update the position state of the receiver.
# </para>
# <para>
# These residuals can be reported with GRS, but because of the fact that these were used to generate the navigation
# solution they should be recomputed using the new solution in order to reflect the residuals for the position solution in
# the GGA or GNS sentence.
# </para>
# <para>
# The MODE field should indicate which computation method was used. An integrity process that uses these
# range residuals would also require GGA or GNS, GSA, and GSV sentences to be sent.
# </para>
# <para>
# If only GPS, or GLONASS, or Galileo, or BDS, or QZSS, or NavIC (IRNSS)is used for the reported position
# solution, the talker ID is GP, GL, GA, GB, GQ, GI respectively and the range residuals pertain to the individual
# system.
# </para>
# <para>
# If GPS, GLONASS, Galileo, BDS, QZSS, NavIC (IRNSS) are combined to obtain the position solution multiple
# GRS sentences are produced, one with the GPS satellites, another with the GLONASS satellites, etc. Each of these
# GRS sentences shall have talker ID �GN�, to indicate that the satellites are used in a combined solution. The GNSS
# System ID data field identifies the specific satellite system. It is important to distinguish the residuals from those that
# would be produced by a GPS-only, GLONASS-only, etc. position solution. In general, the residuals for a combined
# solution will be different from the residual for a GPS-only, GLONASS-only, etc. solution.
# </para>
# <para>
# When multiple GRS sentences are necessary, use of the NMEA TAG Block structure (� 7) and the TAG Block
# Sentence-grouping Parameter (� 7.9.3) reliably links the related sentences together over any transport medium.
# </para>
# <para>
# When GRS sentences are provided with related GSA and/or GSV sentences, use of the NMEA TAG Block structure
# (� 7) and the TAG Block Sentence-grouping Parameter (� 7.9.3) reliably links the related (different sentence
# formatters) sentences together over any transport medium.
# </para>
# </remarks>

from NMEA0183_Commands import NMEA0183_Command as NMEAMessage


class GRS(NMEAMessage):
    # sg = GRS()
    # g.set_grs_data(
        # {
            # 'Sentence ID': 'GRS', 
            # 'Residual': '2.1', 
            # 'Range': '123.4', 
            # 'GPS Range Residuals': '1.0', 
            # 'Mode': '1'
        #})
    # print(g.get_grs_data())
    
    def __init__(self, NMEAMessage):
        if (NMEAMessage == null or NMEAMessage.Length < 8):
            raise Exception("Invalid Grs", NMEAMessage)
        
        self._grs_data = {}
        self._sentence_id = 'GRS'

        # Range residuals in meters for satellites used in the navigation solution
        # Order must match order of the satellite ID3 numbers in GSA. When GRS is used GSA and GSV are generally required
        #
        # Notes:
        # - If the range residual exceeds +99.9 meters, then the decimal part is dropped, 
        #   resulting in an integer (-103.7 becomes -103).
        #   The maximum value for this field is +999.
        # - The sense or sign of the range residual is determined by the order of parameters 
        #   used in the calculation. The expected order is as follows: range residual = 
        #   calculated range - measured range.
        # - When multiple GRS sentences are being sent then their order of transmission must 
        #   match the order of corresponding GSA sentences.Listeners shall keep track of pairs 
        #   of GSA and GRS sentences and discard data if pairs are incomplete.
        self._residual = '2.1'
        def double[] Residuals { get }
        
        self._range = '123.4'
        self._gps_range_residuals = '1.0'
        
        # Residual calculation mode
        self._mode = '1'
        #def GrsMode Mode { get }
        
    def set_grs_data(self, data):
        self._grs_data = data

    def get_grs_data(self):
        return self._grs_data

    # Determines the way the <see cref="Grs"/> residuals were calculated.
    def GrsMode(Enum):
        # Residuals were used to calculate the position given in the matching GGA or GNS sentence
        UsedForPosition = 0,
        # Residuals were recomputed after the GGA or GNS position was computed
        RecomputedFromPosition = 1


        FixTime = StringToTimeSpan(NMEAMessage[0])
        Mode = GrsMode.RecomputedFromPosition if (NMEAMessage[1] == "1") else GrsMode.UsedForPosition
        double[] residuals = new double[NMEAMessage.Length - 2]

        for (int i = 2 i < NMEAMessage.Length i++)
            residuals[i-2] = NMEAMessage.StringToDouble(NMEAMessage[i])

        Residuals = residuals

        # UTC time of the GGA or GNS fix associated with this sentence 
        def TimeSpan FixTime { get }

        TimeSpan ITimestampedMessage.Timestamp => FixTime
