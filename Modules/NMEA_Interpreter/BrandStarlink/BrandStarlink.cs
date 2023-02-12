using System;

namespace NMEA_connector.brands
{
    public class BrandStarlink
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


        internal static void entryHandleCommand(string commandLine)
        {
            throw new NotImplementedException();
        }
    }
}