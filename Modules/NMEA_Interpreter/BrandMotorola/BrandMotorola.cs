using System;

namespace NMEA_connector.brands
{
    public class BrandMotorola
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
         *                //Motorola
                case "PMOTG":
                    //CommandPMOTG();
                    break;
         */
        /* Motorola
         * The PMOTG is used by Motorola Oncore receivers to send a command to
         * the receiver. This command is used to set the output of the sentence
         * to a particular frequency in seconds (or to 0) or to switch the output
         * formula to motorola binary, gps, or loran.
         *
         * $PMOTG,xxx,yyyy
         *
         * where:
         *     xxx    the sentence to be controlled
         *     yyyy   the time interval (0-9999 seconds)
         *
         * or $PMOTG,FOR,y
         *
         * where:
         *     y    MPB=0, GPS=1, Loran=2
         */
        internal static void entryHandleCommand(string commandLine)
        {
            throw new NotImplementedException();
        }
    }
}