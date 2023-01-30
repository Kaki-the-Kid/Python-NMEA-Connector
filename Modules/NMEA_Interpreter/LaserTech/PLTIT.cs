
namespace NmeaParser.Messages.LaserTech
{
    /// <summary>
    /// Laser Range 
    /// </summary>
    [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Naming", "CA1704:IdentifiersShouldBeSpelledCorrectly", MessageId = "Pltit")]
    [NmeaMessageType("PLTIT")]
    public class Pltit : LaserRangeMessage
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="Pltit"/> class.
        /// </summary>
        /// <param name="type">The message type</param>
        /// <param name="message">The NMEA message values.</param>
        public Pltit(string type, string[] message) : base(type, message) { }
    }
}
