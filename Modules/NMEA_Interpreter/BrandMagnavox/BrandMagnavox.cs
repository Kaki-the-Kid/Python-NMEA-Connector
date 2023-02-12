using System;

namespace NMEA_connector.brands
{
    public class BrandMagnavox
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


        /* Magnavox
         * The old Magnavox system used mostly proprietary sentences.
         * The Magnavox system was acquired by Leica Geosystems in 1994.
         * Information on this system can be found at this site. The NMEA
         * sentences themselves are described here. They all use the MVX
         * prefix and include:
         *
         * Control Port Input sentences
         *
         * $PMVXG,000 Initialization/Mode Control - Part A
         * $PMVXG,001 Initialization/Mode Control - Part B
         * $PMVXG,007 Control Port Configuration
         * $PMVXG,023 Time Recovery Configuration
         * $CDGPQ,YYY Query From a Remote Device / Request to Output a Sentence
         *
         * Control Port Output Sentences
         *
         * $PMVXG,000 Receiver Status
         * $PMVXG,021 Position, Height, Velocity
         * $PMVXG,022 DOPs
         * $PMVXG,030 Software Configuration
         * $PMVXG,101 Control Sentence Accept/Reject
         * $PMVXG,523 Time Recovery Configuration
         * $PMVXG,830 Time Recovery Results
         */
        internal static void entryHandleCommand(string commandLine)
        {
            throw new NotImplementedException();
        }
    }
}