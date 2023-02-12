using System;
using System.Collections.Generic;
using System.Linq;

namespace NMEA_connector.brands
{
    public class BrandGarmin
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


        /// <summary>
        /// Public variable that holds the checksum for the last NMEA command
        /// </summary>
        public int CommandChecksum { get; set; }


        public IDictionary<string, string> NmeaCommandsClearText = new Dictionary<string, string>()
        {
            {"HCHDG", "Compass output"},
            {"PGRME", "(estimated error) - not sent if set to 0183 1.5"},
            {"PGRMZ", "(altitude)"},
            {"PSLIB", "Remote Control for a DGPS receiver (beacon receiver control)"},
            {"PGRMM","(map datum)" }
        };

        public void HandleCommand(string nmeaCommand)
        {
            /// \todo Tjek at rækkefølge er korrekt på TrimStart kommandoer
            nmeaCommand = nmeaCommand.TrimStart('G').TrimStart('P');
            this.CommandParts = nmeaCommand.Split(',');

            // Pluk checksum fra kommando sætning i det sidste element
            String[] tmp = this.CommandParts.Last().Split('*');
            int len = this.CommandParts.GetLength(1);
            this.CommandParts[len - 1] = tmp[0];
            this.CommandChecksum = int.Parse(tmp[1]);
            tmp = null;

            switch (this.CommandParts.First())
            {
                //Garmin
                case "HCHDG":
                    CommandGarminHCHDG();
                    break;
                case "PGRME":
                    CommandGarminPGRME();
                    break;
                case "PGRMZ":
                    CommandGarminPGRMZ();
                    break;
                case "PSLIB":
                    CommandGarminPSLIB();
                    break;
                case "PGRMM":
                    commandGarminPGRMM();
                    break;
                default:
                    // Jeg forstod ikke kommandoen
                    // \todo Registrering af kommandoer som ikke er forstået som starter med $GP
                    Console.WriteLine(@"Didn't understand the $GP command");
                    break;
            }
        }


        /* HCHDG - Compass output is used on Garmin
         * etrex summit, vista , and 76S receivers to output the value of the
         * internal flux-gate compass. Only the magnetic heading and magnetic
         * variation is shown in the message.
         *
         * $HCHDG,101.1,,,7.1,W*3C
         *
         * where:
         *     HCHDG    Magnetic heading, deviation, variation
         *     101.1    heading
         *     ,,       deviation (no data)
         *     7.1,W    variation
         */
        public void CommandGarminHCHDG()
        {
            ;
        }

        internal static void entryHandleCommand(string commandLine)
        {
            throw new NotImplementedException();
        }


        /****************************************************************************
         * PGRME -
         * The following are Garmin proprietary sentences.
         * "P" denotes proprietary,
         * "GRM" is Garmin's manufacturer code, and
         * "M" or "Z" indicates the specific sentence type.
         *
         * Note that the PGRME sentence is not set if the output is set to NMEA 1.5 mode.
         *
         * $PGRME,15.0,M,45.0,M,25.0,M*1C
         *
         * where:
         *     15.0,M       Estimated horizontal position error in meters (HPE)
         *     45.0,M       Estimated vertical error (VPE) in meters
         *     25.0,M       Overall spherical equivalent position error
         ****************************************************************************/
       public void CommandGarminPGRME()
       {
           int i = 0;
           double outEstimatedHorizontalPositionError = double.Parse(this.CommandParts[i++]); // 15.0,M Estimated horizontal position error in meters(HPE) 
           char outEstimatedHorizontalPositionErrorUnit = char.Parse(this.CommandParts[i++]);
           double outEstimatedVerticalError = double.Parse(this.CommandParts[i++]); // 45.0,M Estimated vertical error(VPE) in meters
           char outEstimatedVerticalErrorUnit = char.Parse(this.CommandParts[i++]);
           double outOverallSphericalEquivalentPositionError = double.Parse(this.CommandParts[i++]); // 25.0,M Overall spherical equivalent position error
           char outOverallSphericalEquivalentPositionErrorUnit = char.Parse(this.CommandParts[i++]);
       }

       /****************************************************************************
        * $PGRMZ,93,f,3*21
        *
        * where:
        *     93,f         Altitude in feet
        *     3            Position fix dimensions 2 = user altitude
        *                                          3 = GPS altitude
        *     This sentence shows in feet, regardless of units shown on the display.
        *     Note that for units with an altimeter this will be altitude computed
        *     by the internal altimeter.
        ****************************************************************************/
        public void CommandGarminPGRMZ()
        {
            int i = 0;
            double outAltitude = double.Parse(this.CommandParts[i++]);  // Altitude in feet
            char outAltitudeUnit = char.Parse(this.CommandParts[i++]); // f = feet
            int outPositionFixDimensions = int.Parse(this.CommandParts[i++]);  // 3 Position fix dimensions 2 = user altitude, 3 = GPS altitude
        }


        /****************************************************************************
         * PSLIB
         * Proprietary sentences are used to control a Starlink differential
         * beacon receiver. (Garmin's DBR is Starlink compatible as are many
         * others.) When the GPS receiver is set to change the DBR frequency
         * or b/s rate, the "J" sentence is replaced (just once) by (for example):
         *
         * $PSLIB,320.0,200*59 to set the DBR to 320 KHz, 200 b/s.
         *
         * $PSLIB,,,J*22   Status request
         * $PSLIB,,,K*23   configuration request
         *
         * These two sentences are normally sent together in each group of
         * sentences from the GPS. The three fields are: Frequency, bit Rate,
         * Request Type. The value in the third field may be:
         * J = status request,
         * K = configuration request,
         * or null (blank) = tuning message.
         *
         * The correct values for frequency range from 283.5-325.0 KHz while
         * the bit rate can be set to 0, 25, 50, 100 or 200 bps.
         ****************************************************************************/
        public void CommandGarminPSLIB()
        {
            int i = 0;
            char out1 = char.Parse(this.CommandParts[i++]); // ,
            char out2 = char.Parse(this.CommandParts[i++]); // ,
            char out3 = char.Parse(this.CommandParts[i++]); //,J = Status request, K = configuration request
            
            /** todo checksum */
        }


        /****************************************************************************
         * * $PGRMM,NAD27 Canada*2F
         *
         *     Currently active horizontal datum
         ****************************************************************************/
        public void commandGarminPGRMM()
        {

        }


        /************************************************************************
         * RTE - Routes
         * RTE is sent to indicate the names of the waypoints used in an active route.
         * There are two types of RTE sentences. This route sentence can list all of
         * the waypoints in the entire route or it can list only those still ahead.
         * Because an NMEA sentence is limited to 80 characters there may need to be
         * multiple sentences to identify all of the waypoints. The data about the
         * waypoints themselves will be sent in subsequent WPL sentences which will
         * be sent in future cycles of the NMEA data.
         *
         *        1   2   3 4    5           x    n
         *        |   |   | |    |           |    |
         * $--RTE,x.x,x.x,a,c--c,c--c, ..... c--c*hh<CR><LF>
         *
         * Field Number:
         *
         * 1. Total number of RE sentences being transmitted
         * 2. Sentence Number
         * 3. Sentence mode
         *      c = complete route, all waypoints
         *      w = working route, the waypoint you just left, the waypoint
         *          you’re heading to, then all the rest
         * 4. Route ID
         * 5. Waypoint ID
         * x. Additiobal waypint IDs
         * More waypoints follow. Last field is a checksum as usual.
         *
         * The Garmin 65 and possibly other units report a $GPR00 in the same format.
         *
         * Example: $GPRTE,1,1,c,0*07
         *
         ************************************************************************/
        public void commandGarminRTE()
        {
            //
        }
    }
}