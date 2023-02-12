using System;

namespace NMEA_connector.brands
{
    public class BrandRockwell
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


        /*
         *                 //Rockwell International();
                case "PRWIRID":
                    //CommandPRWIRID();
                    break;
                case "PRWIILOG":
                    //CommandPRWIILOG();
                    break;
                case "PRWIINIT":
                    //CommandPRWIINIT();
                    break;
         */
        /* Rockwell International
         * The Rockwell chipset is used on a number of gps receivers. It outputs
         * some proprietary sentences with the PRWI prefix and accepts input from
         * some special sentences similar to the approach used by Magellan. It can
         * also be switched to a separate binary mode using a proprietary sentence.
         * The input sentence most used to initialize the unit is $PRWIINIT and one
         * output sentence is $PRWIRID
         *
         * $PRWIRID,12,01.83,12/15/97,0003,*42
         *
         * where:
         *     $PRWIRID
         *     12         12 channel unit
         *     01.83      software version
         *     12/15/97   software date
         *     0003       software options (HEX value)
         *                Bit 0 minimize ROM usage
         *                Bit 1 minimize RAM usage
         *     *42        checksum
         *
         * An input sentence that will define which NMEA sentences are to be output
         * from the Rockwell unit is:
         *
         * $PRWIILOG,GGA,A,T,1,0
         *
         * where:
         *    $PRWIILOG
         *    GGA        type of sentence
         *    A          A=activate, V=deactivate
         *    T          cyclic
         *    1          every 1 second
         *    0          ??
         *
         * The initialization sentence which can be input to speed up acquisition looks like:
         *
         * $PRWIINIT,V,,,4308.750,N,07159.791,W,100.0,0.0,M,0.0,T,175244,230503*77
         *
         * where:
         *    $PRWIINIT     INIT = initialization
         *    V             V = reset, A = no reset
         *    ,,		 Reserved for future use
         *    4308.750      Latitude
         *    N             N = North, S = South
         *    07159.791     Longitude
         *    W             W = West, E = East
         *    100.0         Altitude in meters
         *    0.0           Speed
         *    M             M = m/s, N = knots, K = km/hr
         *    0.0           Heading
         *    T             T = True, M = Magnetic
         *    175244	 UTC time (hour, min, sec)
         *    230503        UTC date (day, month, year)
         *    *77           Checksum
         *
         * Note: Commas may be used to signify using existing data. If units
         * are supplied then the data must be present. Speed and direction must
         * be supplied together. Lat/Lon must be supplied together. UTC time and
         * date must be supplied together. If heading is magnetic then lat/lon
         * needs to be supplied along with UTC time and date.
         *
         * The sentences available for the Rockwell Jupiter chipset are:
         * GGA, GSA, GSV, VTG, RMC and some proprietary sentences.
         */
        internal static void entryHandleCommand(string commandLine)
        {
            throw new NotImplementedException();
        }
    }
}