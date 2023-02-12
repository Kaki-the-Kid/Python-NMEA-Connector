# ****************************************************************************//*
# *   @project  Python NMEA Connector
# *   @file     BWC.py
# *   @brief    Cross Track Error, Measured
# *   @author   Karsten Reitan Sørensen
# *   Date:     11-02-2023
# *******************************************************************************
# @brief    Local geodetic datum and datum offsets from a reference datum.
# @details  This sentence is used to define the datum to which a position location and geographic 
#           locations in subsequent sentences, is referenced. Latitude, longitude and altitude 
#            offsets from the reference datum, and the selection of reference datum, are also 
#           provided.
# @param    This sentence is used to define the datum to which a position location and geographic
#           locations in subsequent sentences, is referenced. Latitude, longitude and altitude offsets
#            from the reference datum, and the selection of reference datum, are also provided.
# @param    The datum sentence should be transmitted immediately prior to every positional sentence (e.g., <c>GLL</c>, 
# <c>BWC</c>, <c>WPL</c>) that is referenced to a datum other than WGS84, which is the datum recommended by IMO.
# </para>
# @param    For all datums the DTM sentence should be transmitted prior to any datum change and periodically at
#           intervals of not greater than 30 seconds.

from NMEA0183_Commands import NMEA0183_Command


class DTM(NMEA0183_Command):
    
    def __init__(self, NMEA0183_Command, total_number_of_sentences=None, sentence_number=None, command=None, date=None, local_datum=None, latitude_offset=None, longitude_offset=None):
        if (NMEA0183_Command == None or NMEA0183_Command.Length < 8):
            raise Exception("Invalid DTM: {}".NMEA0183_Command)
        
        self.total_number_of_sentences = total_number_of_sentences
        self.sentence_number = sentence_number
        self.command = command
        self.date = date
        # Local datum code
        # @param    Three character alpha code for local datum. If not one of the listed earth-centered 
        #           datums, or <c>999</c> for user defined datum, use IHO datum code from International 
        #           Hydrographic Organization Publication S-60 
        #           Appendices B and C. String.Empty if unknown.
        # @param    Users should be aware that chart transformations based on IHO S60 parameters may 
        #           result in significant positional errors when applied to chart data.
        # Common known datum codes are:
        # <table>
        #   <tr>
        #     <th>Code</th>
        #     <th>Datum</th>
        #   </tr>
        #   <tr><td><c>W84</c></td><td>WGS 84</td></tr>
        #   <tr><td><c>W72</c></td><td>WGS 72</td></tr>
        #   <tr><td><c>S85</c></td><td>SGS 85</td></tr>
        #   <tr><td><c>P90</c></td><td>PE 90</td></tr>
        #   <tr><td><c>999</c></td><td>User Defined</td></tr>
        #   <tr><td><c>Others</c></td><td>IHO Datum Code</td></tr>
        # </table>
        # </para>
        # </remarks>
        #str LocalDatumCode():
        #    return self._localDatumCode
        self.local_datum = local_datum
        
        # <summary>
        # Latitude Offset, decimal degrees
        # </summary>
        # <remarks>
        # Latitude and longitude offsets are positive numbers, the altitude offset may be negative. Offsets
        # change with position; position in the local datum is offset from the position in the reference datum in the directions 
        # indicated:
        # <c>P_local_datum = P_ref_datum + offset</c>
        # </remarks>
        #float LatitudeOffset():         
        #    return self._latitudeOffset
        self.latitude_offset = latitude_offset
        LatitudeOffset = NmeaMessage.StringToDouble(message[2]) *  ( -1 if message[3] == "S" else 1 )
        
        # <summary>
        # Longitude Offset in minutes
        # </summary>
        # <remarks>
        # Latitude and longitude offsets are positive numbers, the altitude offset may be negative. Offsets
        # change with position; position in the local datum is offset from the position in the reference datum in the directions 
        # indicated:
        # <c>P_local_datum = P_ref_datum + offset</c>
        # </remarks>
        #float LongitudeOffset():
        #    return self._longitudeOffset
        self.longitude_offset = longitude_offset
        LongitudeOffset = NmeaMessage.StringToDouble(message[4]) * ( -1 if message[5] == "W" else 1 )
        
        # <summary>
        # Altitude Offset in minutes
        # </summary>
        # <remarks>
        # Latitude and longitude offsets are positive numbers, the altitude offset may be negative. Offsets
        # change with position; position in the local datum is offset from the position in the reference datum in the directions 
        # indicated:
        # <c>P_local_datum = P_ref_datum + offset</c>
        # </remarks>
        #public double AltitudeOffset { get; }
        #AltitudeOffset = NmeaMessage.StringToDouble(message[6])

        # <summary>
        # Reference datum code
        # </summary>        
        # <remarks>
        # @param
        # Common known datum codes are:
        # <table>
        #   <tr>
        #     <th>Code</th>
        #     <th>Datum</th>
        #   </tr>
        #   <tr><td><c>W84</c></td><td>WGS 84</td></tr>
        #   <tr><td><c>W72</c></td><td>WGS 72</td></tr>
        #   <tr><td><c>S85</c></td><td>SGS 85</td></tr>
        #   <tr><td><c>P90</c></td><td>PE 90</td></tr>
        # </table>
        # </para>
        # </remarks>
        #str ReferenceDatumCode():     
        #    return self._referenceDatumCode
        #ReferenceDatumCode = message[7]

    
    @property
    def total_number_of_sentences(self):
        return self._total_number_of_sentences
    
    @total_number_of_sentences.setter
    def total_number_of_sentences(self, total_number_of_sentences):
        self._total_number_of_sentences = total_number_of_sentences
    
    @property
    def sentence_number(self):
        return self._sentence_number
    
    @sentence_number.setter
    def sentence_number(self, sentence_number):
        self._sentence_number = sentence_number
    
    @property
    def command(self):
        return self._command
    
    @command.setter
    def command(self, command):
        self._command = command
    
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date):
        self._date = date
    
    @property
    def local_datum(self):
        return self._local_datum
    
    @local_datum.setter
    def local_datum(self, local_datum):
        self._local_datum = local_datum
    
    @property
    def latitude_offset(self):
        return self._latitude_offset
    
    @latitude_offset.setter
    def latitude_offset(self, latitude_offset):
        self._latitude_offset = latitude_offset
    
    @property
    def longitude_offset(self):
        return self._longitude_offset
    
    @longitude_offset.setter
    def longitude_offset(self, longitude_offset):
        self._longitude_offset = longitude_offset
