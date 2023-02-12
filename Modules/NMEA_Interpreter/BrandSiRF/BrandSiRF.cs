/******************************************************************************************
 * SiRF
 * The SiRF line of chips support several input sentences that permit
 * the user to customize the way the chip behaves. In addition SiRF has
 * a binary protocol that is even more powerful permitting different
 * implementations to behave entirely differently. However, most
 * applications do not attempt to customize the behavior so a user will
 * need to make sure that the any customization is compatible with the
 * application they are planning to use. There are 5 input sentences
 * defined that begin with $PSRF which is followed by three digits.
 * Each sentence takes a fix amount of input fields which must exist,
 * no null fields, and is terminated with the standard CR/LF sequence.
 * The checksum is required.
 *
 * The sentences 100 and 102 set the serial ports. 100 sets the main
 * port A while 102 sets the DGPS input port B. 100 has an extra field
 * that can be used to switch the interface to binary mode. Binary mode
 * requires 8 bits, 1 stop bit, no parity. There is a command in binary
 * mode that will switch the interface back to NMEA. Do not use the
 * NMEA command to switch to binary mode unless you have the ability to
 * switch it back. You could render your gps inoperative.
 ******************************************************************************************/

using System;
using System.Diagnostics;
using System.Dynamic;
using NMEA_connector;
using NMEA_connector.Properties;

namespace NMEA_connector.brands
{
    public class BrandSiRf
    {
        public static void EntryHandleCommand(string commandLine)
        {
            throw new NotImplementedException();

            switch (commandLine)
            {
                //SiRF Chipset
                case "PSRF100":
                    //SiRfNMEACommand100();
                    break;
                case "PSRF101":
                    //SiRfNMEACommand100();
                    break;
                case "PSRF102":
                    //SiRfNMEACommand102();
                    break;
                case "PSRF103":
                    //SiRfNMEACommand104();
                    break;
                case "PSRF104":
                    //SiRfNMEACommand104();
                    break;
                case "PSRF105":
                    //SiRfNMEACommand105();
                    break;
                default:
                    Console.WriteLine("Ingen registreret NMEA kommando\n");
                    break;
            }
        }


        /****************************************************************************
        * $PSRF100
        * 0          0=SiRF, 1=NMEA  - This is where the protocol is changed.
        * 9600       b/s rate 4800, 9600, 19200, 38400
        * 8          7, 8 Databits
        * 1          0, 1 Stopbits
        * 0          0=none, 1=odd, 2=even Parity
        * *0C        checksum
        *
        * The sentences 101 and 104 can be used to initialize values to be used
        * by the gps. Supplying these values can shorten the initial lock time.
        * If the clock offset is set to 0 then an internal default will be used.
        * Sentence 101 supplies data in the internal ECEF (Earth centered, Earth
        * Fixed) format in meters while sentence 104 supplies the data in the
        * traditional Lat / Lon format.
        *
        * $PSRF100,0,9600,8,1,0*0C
        */
        public void SiRfNMEACommand100()
        {

        }

        /*
         * $PSRF101,-2686700,-4304200,3851624,95000,497260,921,12,3*22
         */
        public void SiRfNMEACommand101()
        {

        }

        /****************************************************************************
         * $PSRF102,9600,8,1,0*3C*
         ***************************************************************************/
        public void SiRfNMEACommand102()
        {

        }

        /****************************************************************************
         * The sentence 103 is used to control which NMEA sentences are to be
         * sent and how often. Each sentence type is controlled individually.
         * If the query bit is set then the gps responds by sending this message
         * in the next second no matter what the rate is set to. Note that if
         * trickle power is in use (can only be set in binary mode) then the
         * actual update rate will be the selected update rate times the trickle
         * rate which could mean that the data will be sent less frequently than
         * was set here.
         *
         * $PSRF103,05,00,01,01*20
         *
         * where:
         * $PSRF103
         * 05         00=GGA
         *            01=GLL
         *            02=GSA
         *            03=GSV
         *            04=RMC
         *            05=VTG
         * 00         mode, 0=set rate, 1=query
         * 01         rate in seconds, 0-255
         * 01         checksum 0=no, 1=yes
         * 20         checksum
         ****************************************************************************/
        public void SiRfNMEACommand103()
        {
            // $PSRF103 
            // 05         00 = GGA
            // 01 = GLL
            // 02 = GSA
            // 03 = GSV
            // 04 = RMC
            // 05 = VTG
            // 00         mode, 0 = set rate, 1 = query
            // 01         rate in seconds, 0 - 255
            // 01         checksum 0 = no, 1 = yes
            // 20        checksum
        }

        /****************************************************************************
         * $PSRF104
         * 37.3875111 Latitude in degrees
         * -121.97232 Longitude in degrees
         * 0          Ellipsoid Altitude in meters
         * 95000      Clock offset
         * 237759     GPS Time of Week in seconds
         * 922        GPS Week Number
         * 12         Channel count (1 to 12)
         * 3          Reset config where
         *              1 = warm start, ephemeris valid
         *              2 = clear ephemeris, warm start (First Fix)
         *              3 = initialize with data, clear ephemeris
         *              4 = cold start, clear all data
         *              8 = cold start, set factory defaults
         * *3A        checksum
         *
         * Example:
         * $PSRF104,37.3875111,-121.97232,0,95000,237759,922,12,3*3A
         ****************************************************************************/
        public void SiRfNMEACommand104()
        {

        }


        /****************************************************************************
         * The 105 sentence controls a debug mode which causes the gps to
         * report any errors it finds with the input data. $PSRF105,1*3E would
         * turn debug on while $PSRF105,0*3F would turn it off.
         ****************************************************************************/
        public void SiRfNMEACommand105()
{

}
}
}
