# ****************************************************************************//*
# *   @project  Python NMEA Connector
# *   @file     BWC.py
# *   @brief    Cross Track Error, Measured
# *   @author   Karsten Reitan Sørensen
# *   Date:     11-02-2023
# *******************************************************************************

from NMEA0183_Commands import NMEA0183_Command as NMEAMessage


class BWC(NMEA0183_Command):
# *******************************************************************************

from NMEA0183_Commands import NMEA0183_Command

namespace NmeaParser.Messages
{
    class NMEA0183:
    def __init__(self):
        self._MWV_Wind_Speed = 0.0
        self._MWV_Wind_Angle = 0.0
        self._MWV_Reference = ''
    
    @property
    def MWV_Wind_Speed(self):
        return self._MWV_Wind_Speed

    @MWV_Wind_Speed.setter
    def MWV_Wind_Speed(self, value):
        self._MWV_Wind_Speed = float(value)

    @property
    def MWV_Wind_Angle(self):
        return self._MWV_Wind_Angle

    @MWV_Wind_Angle.setter
    def MWV_Wind_Angle(self, value):
        self._MWV_Wind_Angle = float(value)

    @property
    def MWV_Reference(self):
        return self._MWV_Reference

    @MWV_Reference.setter
    def MWV_Reference(self, value):
        self._MWV_Reference = value

    # Course over ground and ground speed
    
    # <remarks>
    # The actual course and speed relative to the ground.
    # </remarks>
    [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Naming", "CA1704:IdentifiersShouldBeSpelledCorrectly", MessageId = "GPVTG")]
    [NmeaMessageType("--VTG")]
    public class Vtg : NmeaMessage
    {
        
        # Initializes a new instance of the <see cref="Vtg"/> class.
        
        # <param name="type">The message type</param>
        # <param name="message">The NMEA message values.</param>
        public Vtg(string type, string[] message) : base(type, message)
        {
            if (message == null || message.Length < 7)
                raise Exception("Invalid VTG: {}".message)

            CourseTrue = NmeaMessage.StringToDouble(message[0]);
            CourseMagnetic = NmeaMessage.StringToDouble(message[2]);
            SpeedKnots = NmeaMessage.StringToDouble(message[4]);
            SpeedKph = NmeaMessage.StringToDouble(message[6]);
        }

        
        #  Course over ground relative to true north
        
        public double CourseTrue { get; }

        
        #  Course over ground relative to magnetic north
        
        public double CourseMagnetic { get; }

        
        # Speed over ground in knots
        
        public double SpeedKnots { get; }

        
        # Speed over ground in kilometers/hour
        
        public double SpeedKph { get; }
    }
}