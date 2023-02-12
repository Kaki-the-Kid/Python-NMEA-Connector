/*
 * Pilot GPS Plugin Module
 * https://docs.pilotnexus.io/docs/Hardware/Modules/GPS.html
 */
using System;

namespace NMEA_connector.brands
{
    public class BrandPilotGPS
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


        // [TODO] Funktion som håndterer kommandoer specielt for Pilot GPS enhed
        internal static void entryHandleCommand(string commandLine)
        {
            throw new NotImplementedException();
        }
    }
}