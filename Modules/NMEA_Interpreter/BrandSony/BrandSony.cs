using System;

namespace NMEA_connector.brands
{
    public class BrandSony
    {
        public String[] CommandParts
        {
            get
            {
                return CommandParts;
            }
            set
            {
                if (value.Length == 0)
                    throw new ArgumentException(@"Value cannot be an empty collection.", nameof(value));
                else
                    CommandParts = value;
            }
        }


        /* Sony
         * The Sony interface uses a proprietary sentence that looks like:
         *
         * $PSNY,0,00,05,500,06,06,06,06*14
         *
         * where:
         *    PSNY
         *    0          Preamp (external antenna) status
         *               0 = Normal
         *               1 = Open
         *               2 = shorted
         *    00         Geodesic system (datum) 0-25, 0 = WGS84
         *    05	      Elevation mask in degrees
         *    500	      Speed Limit in Km
         *    06         PDOP limit with DGPS on
         *    06	      HDOP limit with DGPS on
         *    06	      PDOP limit with DGPS off
         *    06	      HDOP limit with DGPS off
         *    *14	      Checksum
         */
        internal static void entryHandleCommand(string commandLine)
        {
            throw new NotImplementedException();
        }
    }
}