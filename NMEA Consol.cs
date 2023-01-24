using System;
using System.Dynamic;
using NMEA_connector;
using NMEA_connector.Properties;


namespace NMEA_connector
{
    class ConsolUi : Program
    {
        private StructGPSData _GPSData; // field
        public StructGPSData GPSData { get; set; }


        public static string[] FixQuality =
            new string[]
            {
                "invalid",
                "GPS fix(SPS)",
                "DGPS fix",
                "PPS fix",
                "Real Time Kinematic",
                "Float RTK",
                "estimated(dead reckoning) (2.3 feature)",
                "Manual input mode",
                "Simulation mode"
            };
        

        public void ConsolInit()
        {
            int keyPressed = 0;

            // The placeholder for calculated GPS data
            // Ex: $GPGGA,181908.00,3404.7041778,N,07044.3966270,W,4,13,1.00,495.144,M,29.200,M,0.10,0000*40
            _GPSData.GPSTimestamp = "181908.00";

            _GPSData.GPSLatitudeDegree = 340;       // Latitude in the DDMM.MMMMM,Direction
            _GPSData.GPSLatitudeMins = 4.7041778;
            _GPSData.GPSLatitudeDirection = "N";
            _GPSData.GPSLatitudeString = "";

            _GPSData.GPSLongitudeDegree = 070;       // Longitude in the DDMM.MMMMM,Direction
            _GPSData.GPSLongitudeMins = 44.3966270;
            _GPSData.GPSLongitudeDirection = "W";
            _GPSData.GPSLongitudeString="";

            _GPSData.GPSQuality = 4;
            _GPSData.GPSQualityText = FixQuality[4]; //4 = Real Time Kinematic
             
            _GPSData.GPSNumberSatelites = 13;
            _GPSData.GPSHdop = 1.00;

            _GPSData.GPSAntenneAltitude = 495.144;
            _GPSData.GPSAntennaAltitudemf = "M";

            _GPSData.GPSGeoidalSeparation = 29.200;
            _GPSData.GPSGeoidalSeparationmf = "M";

            _GPSData.GPSAgeCorrection = 0.10;
            _GPSData.GPSStationId = "0000";
            _GPSData.GPSLastChecksum = "*40";


            while (keyPressed != 9)
            {
                Console.Clear();
                Console.WriteLine("GPS Menu");
                Console.WriteLine("1 Run_GPS_command");
                Console.WriteLine("2 Show_GPS_Time");
                Console.WriteLine("3 Show_GPS_Longitude_Latitude");
                Console.WriteLine("4 Print_out_GPS_data");
                Console.WriteLine("9 Exit");

                keyPressed = Convert.ToInt32(Console.ReadLine());

                switch (keyPressed)
                {
                    case 1:
                        Console.Clear();
                        Console.WriteLine("Type in GPS sentence");
                        var command = Console.ReadLine()?.ToString().ToUpper();
                        ParseGpsCommand(command);
                        break;
                    case 2:
                        Console.Clear();
                        Console.WriteLine("GPS Time is {0}", "timestamp");
                        Console.ReadKey();
                        break;
                    case 3:
                        Console.Clear();
                        Console.WriteLine("GPS position");
                        Console.WriteLine("latitude: {0} deg {1}' {2}, longitude: {3} deg {4}' {5}", "48", "07.038", "E", "11", "31.000", "E");
                        Console.ReadKey();
                        break;
                    case 9:
                        break;
                    default:
                        Console.WriteLine("Not a valid command");
                        Console.ReadKey();
                        break;
                }
            }

        }

        public static void ParseGpsCommand(string gpsString)
        {

        }

        public static void PrintOutGpsData()
        {
            //Latitude
            //Longitude
            //Altitude
            //PDOP
            //HDOP
            //VDOP
            //Satellites Tracked
            //Satellites in View
        }


        public int GpsChecksum(string s)
        {
            int checksum = 0;
            int chars = 0;

            while (chars < s.Length)
            {
                checksum ^= s[chars++];
            }

            return checksum;
        }


        /* The checksum at the end of each sentence is the XOR of all of the bytes in the sentence,
         * excluding the initial dollar sign. The following C code generates a checksum for the
         * string entered as "mystring" and prints it to the output stream. In the example, a
         * sentence from the sample file is used.*/
        int GpsChecksumMain()
        {
            string mystring = "GPRMC,092751.000,A,5321.6802,N,00630.3371,W,0.06,31.66,280511,,,A";
            Console.WriteLine("String: {0}", mystring);
            Console.WriteLine("Checksum: {0}", GpsChecksum(mystring));
            return 0;
        }
    }
}
