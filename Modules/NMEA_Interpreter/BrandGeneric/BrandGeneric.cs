/********************************************************************************//*
 * Fil med fortolkning af almindelige NMEA kommandoer
 * Lige til at starte med er alle kommandoer lagt i sin egen funktion
 ***********************************************************************************/

using System;
using System.Collections.Generic;
using System.Linq;


namespace NMEA_connector.brands
{
    public class BrandGeneric
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

  
        // Lægger op til at der kan laves en sprogoversættelse
        public IDictionary<string, string> NmeaCommandsClearText = new Dictionary<string, string>()
        {
            {"AAM", "Waypoint Arrival Alarm"},
            {"ALM", "Almanac data"},
            {"APA", "Auto Pilot A sentence"},
            {"APB", "Auto Pilot B sentence"},
            {"BOD", "Bearing Origin to Destination"},
            {"BWC", "Bearing using Great Circle route"},
            {"DTM", "Datum being used."},
            {"GGA", "Fix information"},
            {"GLL", "Lat/Lon data"},
            {"GRS", "S Range Residuals"},
            {"GSA", "Overall Satellite data"},
            {"GST", "S Pseudorange Noise Statistics"},
            {"GSV", "Detailed Satellite data"},
            {"MSK", "send control for a beacon receiver"},
            {"MSS", "Beacon receiver status information."},
            {"RMA", "recommended Loran data"},
            {"RMB", "recommended navigation data for gps"},
            {"RMC", "recommended minimum data for gps"},
            {"RTE", "route message"}, // Only when there is an active route. (this is sometimes bidirectional)
            {"TRF", "Transit Fix Data"},
            {"STN", "Multiple Data ID"},
            {"VBW", "dual Ground / Water Spped"},
            {"VTG", "Vector track an Speed over the Ground"},
            {"WCV", "Waypoint closure velocity (Velocity Made Good)"},
            {"WPL", "Waypoint Location information"}, // Only when there is an active route (this is sometimes bidirectional)
            {"XTC", "cross track error"},
            {"XTE", "measured cross track error"},
            {"ZTG", "Zulu (UTC) time and time to go (to destination)"},
            {"ZDA", "Date and Time"}
        };

        internal static void entryHandleCommand(string commandLine)
        {
            throw new NotImplementedException();
        }

        /************************************************************************
         * Funktion som oversætter den enkelte sætning til streng for NMEA log
         * General command prefixes:
         * $GP*** Sentence Titles
         * Selve fortolkning af de enkelte sætning er inddelt i selvstændidge
         * funktion, såder er mulighed for at kompensere for forskellige mærker
         * og standarder. NMEA1.5, NMEA2.0 og NMEA2.3
         ************************************************************************/
        void HandleCommand( string nmeaCommand )
        {
            /***********************************************************************
             * Ex: $GPGGA,181908.00,3404.7041778,N,07044.3966270,W,4,13,1.00,495.
             * 144,M,29.200,M,0.10,0000*40
             *
             * All NMEA messages start with the $ character, and each data field is
             * separated by a comma.
             *
             * GP represent that it is a GPS position (GL would denote GLONASS).
             ***********************************************************************/
            /// \todo Tjek at rækkefølge er korrekt på TrimStart kommandoer
            nmeaCommand = nmeaCommand.TrimStart('G').TrimStart('P');
            this.CommandParts = nmeaCommand.Split(',');

            // Pluk checksum fra kommando sætning i det sidste element
            String[] tmp = this.CommandParts.Last().Split('*');
            int len = this.CommandParts.GetLength(1);
            this.CommandParts[len-1] = tmp[0];
            this.CommandChecksum = int.Parse(tmp[1]);
            tmp = null;

            switch (this.CommandParts.First())
            {
                // Navigation
                case "AAM": // Command GPAAM;
                    GenericNmeaCommandGpaam();
                    break;
                case "APB": // Command GPAPB;
                    GenericNmeaCommandGpapb();
                    break;
                case "BOD": // Command GPBOD;
                    GenericNmeaCommandGpbod();
                    break;
                case "BWC": // Command GPBWC;
                    GenericNmeaCommandGpbwc();
                    break;
                case "RMB": // Command GPRMB;
                    GenericNmeaCommandGprmb();
                    break;
                case "RTE": // Command GPRTE;
                    GenericNmeaCommandGprte();
                    break;
                case "XTE": // Command GPXTE;
                    GenericNmeaCommandGpxte();
                    break;
                case "WPL": // Command GPWPL;
                    GenericNmeaCommandGpwpl();
                    break;

                // Position
                case "GGA": // CommandGGA();
                    GenericNmeaCommandGpgga();
                    break;
                case "GSA": // CommandGSA();
                    GenericNmeaCommandGpgsa();
                    break;
                case "GSV": // CommandGSV();
                    GenericNmeaCommandGpgsv();
                    break;
                case "RMC": // CommandRMC();
                    GenericNmeaCommandGprmc();
                    break;
                case "GLL": // CommandGLL();
                    GenericNmeaCommandGpgll();
                    break;
                case "VTG": //CommandVTG();
                    GenericNmeaCommandGpvtg();
                    break;

                // Other
                case "ALM": // CommandALM();
                    GenericNmeaCommandGpalm();
                    break;
                case "ZDA": // CommandZDA();
                    GenericNmeaCommandGpzda();
                    break;
                case "MSK": // CommandMSK();
                    GenericNmeaCommandGpmsk();
                    break;
                case "MSS": // CommandMSS();
                    GenericNmeaCommandGpmss();
                    break;
                default:
                    // Jeg forstod ikke kommandoen
                    // \todo Registrering af kommandoer som ikke er forstået som starter med $GP
                    Console.WriteLine(@"Didn't understand the $GP command");
                    break;

            }
        }

        /// Navigation related NMEA command


        /****************************************************************************
         * AAM - Waypoint Arrival Alarm is generated by some units to indicate the
         * Status of arrival (entering the arrival circle, or passing the perpendicular
         * of the course line) at the destination waypoint.
         *
         * $--AAM,A,A,x.x,N,c--c*hh<CR><LF>
         *
         * Eks.:
         * $GPAAM,A,A,0.10,N,WPTNME*32
         *
         * Where:
         * AAM    Arrival Alarm
         * A      Status, BOOLEAN, A = Arrival circle entered, V = not passed
         * A      Status, BOOLEAN, A = perpendicular passed at waypoint, V = not passed
         * 0.10   Circle radius, Arrival circle radius
         * N      Units of radius, nautical miles
         * WPTNME Waypoint name
         * *32    Checksum data
         ****************************************************************************/
        public void GenericNmeaCommandGpaam()
        {
            int i = 0;
            string outCommandText = this.CommandParts[i];
            string outCommandClearText = this.NmeaCommandsClearText[this.CommandParts[i++]];
            bool outArrivalCircleEntered = (this.CommandParts[i++] == "A") ? true : false;
            bool outPerpendicularPassed = (this.CommandParts[i++]  == "A") ? true : false;
            double outCircleRadius = double.Parse(this.CommandParts[i++]);
            string outRadiusUnit = this.CommandParts[i++];
            String[] tmp = this.CommandParts[i].Split('*');
            string outWaypointId = tmp[0];
            string outChecksumData = tmp[1];

            /** \todo Kontrol valid data med checksum */
        }


        /************************************************************************
         * APB - Autopilot Sentence "B"
         * This is a fixed form of the APA sentence with some ambiguities removed.
         *
         * Note: Some autopilots, Robertson in particular, misinterpret "bearing
         * from origin to destination" as "bearing from present position to
         * destination". This is likely due to the difference between the APB
         * sentence and the APA sentence. for the APA sentence this would be the
         * correct thing to do for the data in the same field. APA only differs
         * from APB in this one field and APA leaves off the last two fields where
         * this distinction is clearly spelled out. This will result in poor
         * performance if the boat is sufficiently off-course that the two bearings
         * are different. 13 15
         *
         *        1 2 3   4 5 6 7 8   9 10   11  12|   14|
         *        | | |   | | | | |   | |    |   | |   | |
         * $--APB,A,A,x.x,a,N,A,A,x.x,a,c--c,x.x,a,x.x,a*hh<CR><LF>
         *
         * Field Number:
         * 1.  Loran-C blink/SNR warning, general warning , status A = DAta valid V = warning
         *     or other navigation systems when a reliable fix is not available
         * 2.  Loran-C cycle warning, V = Loran-C Cycle Lock warning flag A = OK or not used
         * 3.  Cross Track Error Magnitude
         * 4.  Direction to steer, L or R
         * 5.  Cross Track Units, N = Nautical Miles K = K for kilometers
         * 6.  Status A = Arrival Circle Entered
         * 7.  Status A = Perpendicular passed at waypoint
         * 8.  Bearing origin to destination
         * 9.  M = Magnetic, T = True
         * 10. Destination Waypoint ID
         * 11. Bearing, present position to Destination
         * 12. M = Magnetic, T = True
         * 13. Heading to steer to destination waypoint
         * 14. M = Magnetic, T = True
         * 15. Checksum
         *
         * Example: $GPAPB,A,A,0.10,R,N,V,V,011,M,DEST,011,M,011,M*82
         *
         ************************************************************************/
        public void GenericNmeaCommandGpapb()
         {
            int i = 0;
            string outCommandText = this.NmeaCommandsClearText[this.CommandParts[i++]];
            bool outAutoPilotDataValid = (CommandParts[i++] == "A")?true:false;
            bool outLockWarning = (CommandParts[i++] == "V") ? true : false;
            double outCrossTrackErrorMagnitude = double.Parse(this.CommandParts[i++]);
            char outDirectionToSteer = char.Parse(this.CommandParts[i++]);
            char outCrossTrackUnits = char.Parse(this.CommandParts[i++]);
            char outArrivalCircleEntered = char.Parse(this.CommandParts[i++]);
            char outPerpendicularPassedAtWaypoint = char.Parse(this.CommandParts[i++]);
            string outBearingOriginToDestination = this.CommandParts[i++];
            char outBearingOriginMagnetic = char.Parse(this.CommandParts[i++]); //M = Magnetic, T = True
            string outDestinationWaypointId = this.CommandParts[i++];
            string outBearingPresentPositionToDestination = this.CommandParts[i++];
            char outBearingPresentPositionMagnetic = char.Parse(this.CommandParts[i++]); // M = Magnetic, T = True
            string outHeadingToSteerToDestinationWaypoint = this.CommandParts[i++];
            char outHeadingToSteerMagnetic = char.Parse(this.CommandParts[i++]); // 14. M = Magnetic, T = True

            /** \todo react to new navigation information */
            /** \todo Kontrol valid data med checksum */
        }


        /*****************************************************************************
         * BOD - Bearing - Waypoint to Waypoint
         *        1   2 3   4 5    6    7
         *        |   | |   | |    |    |
         * $--BOD,x.x,T,x.x,M,c--c,c--c*hh<CR><LF>
         *
         * Field Number:
         * 1. Bearing Degrees, True
         * 2. T = True
         * 3. Bearing Degrees, Magnetic
         * 4. M = Magnetic
         * 5. Destination Waypoint
         * 6. Origin Waypoint
         * 7. Checksum
         *
         * Example 1: $GPBOD,099.3,T,105.6,M,POINTB,*01
         *
         * Waypoint ID: "POINTB" Bearing 99.3 True, 105.6 Magnetic This sentence is transmitted
         * in the GOTO mode, without an active route on your GPS. WARNING: this is the bearing
         * from the moment you press enter in the GOTO page to the destination waypoint and is
         * NOT updated dynamically! To update the information, (current bearing to waypoint),
         * you will have to press enter in the GOTO page again.
         *
         * Example 2: $GPBOD,097.0,T,103.2,M,POINTB,POINTA*52
         *
         * This sentence is transmitted when a route is active. It contains the active leg information:
         * origin waypoint "POINTA" and destination waypoint "POINTB", bearing between the two
         * points 97.0 True, 103.2 Magnetic. It does NOT display the bearing from current location
         * to destination waypoint! WARNING Again this information does not change until you are on
         * the next leg of the route. (The bearing from POINTA to POINTB does not change during the
         * time you are on this leg.)
         *
         * This sentence has been replaced by BWW in NMEA 4.00 (and posssibly earlier versions) [ANON].
         ************************************************************************/
        public void GenericNmeaCommandGpbod()
        {
            int i = 0;
            string output = this.NmeaCommandsClearText[this.CommandParts[i++]];
            double outBearingDegreesTrue = double.Parse(this.CommandParts[i++]);
            char outBearingDegreesTrueStatus = char.Parse(this.CommandParts[i++]); // T = True
            double outBearingDegreesMagnetic = double.Parse(this.CommandParts[i++]);
            char outBearingDegreesBMagnetic = char.Parse(this.CommandParts[i++]); // M = Magnetic
            string outDestinationWaypoint = this.CommandParts[i++];
            string outOriginWaypoint = this.CommandParts[i++];
            this.CommandChecksum = int.Parse(this.CommandParts[i++]);

            // \todo react to navigation data
        }

        
        /************************************************************************
         * BWC - Bearing & Distance to Waypoint using a Great Circle route.
         * Time (UTC) and distance & bearing to, and location of, a specified waypoint
         * from present position along the great circle path.
         *
         *                                                         12
         *        1         2       3 4        5 6   7 8   9 10  11|    13 14
         *        |         |       | |        | |   | |   | |   | |    |   |
         * $--BWC,hhmmss.ss,llll.ll,a,yyyyy.yy,a,x.x,T,x.x,M,x.x,N,c--c,m,*hh<CR><LF>
         *
         * Field Number:
         * 1.  UTC Time or observation
         * 2.  Waypoint Latitude
         * 3.  N = North, S = South
         * 4.  Waypoint Longitude
         * 5.  E = East, W = West
         * 6.  Bearing, degrees True
         * 7.  T = True
         * 8.  Bearing, degrees Magnetic
         * 9.  M = Magnetic
         * 10. Distance, Nautical Miles
         * 11. N = Nautical Miles
         * 12. Waypoint ID
         * 13. FAA mode indicator (NMEA 2.3 and later, optional)
         * 14. Checksum
         *
         * Example 1: $GPBWC,081837,,,,,,T,,M,,N,*13
         * Example 2: GPBWC,220516,5130.02,N,00046.34,W,213.8,T,218.0,M,0004.6,N,EGLM*11
         ************************************************************************/
        public void GenericNmeaCommandGpbwc()
        {
            int i = 0;
            string output = this.NmeaCommandsClearText[this.CommandParts[i++]];
            string outUTCTimeOrObservation = this.CommandParts[i++]; // 1. UTC Time or observation
            string outWaypointLatitude = this.CommandParts[i++]; // 2. Waypoint Latitude
            char outoutWaypointLatitudeBearing = char.Parse(this.CommandParts[i++]); // 3.N = North, S = South
            string outWaypointLongitude = this.CommandParts[i++]; // 4. Waypoint Longitude
            char outWaypointLongitudeBearing = char.Parse(this.CommandParts[i++]); // 5. E = East, W = West
            string outBearingToWaypointDegreesTrue = this.CommandParts[i++]; // 6. Bearing to waypoint, degrees true
            char outBearingToWaypointDegreesT = char.Parse(this.CommandParts[i++]); // 7. T = True
            string outBearingToWaypointDegreesMagnetic = this.CommandParts[i++]; // 8. Bearing to waypoint, degrees magnetic
            char outBearingToWaypointDegreesM = char.Parse(this.CommandParts[i++]); // 9. M = Magnetic
            string outDistanceToWaypoint = this.CommandParts[i++]; // 10. Distance to waypoint, Nautical miles (or kilometer)
            char outDistanceToWaypointStatus = char.Parse(this.CommandParts[i++]); // 11. N = Nautical Miles, K = Kilometer
            string outWaypointID = this.CommandParts[i++]; // 12. Waypoint ID
            //13.FAA mode indicator(NMEA 2.3 and later, optional)

            /** \todo Check values against Command data */
            /** \todo React to navigation data */
        }


        /************************************************************************
         * RMB - Recommended Minimum Navigation Information -
         * The recommended minimum navigation sentence is sent whenever a route or a goto is
         * active. On some systems it is sent all of the time with null data. The Arrival alarm
         * flag is similar to the arrival alarm inside the unit and can be decoded to drive an
         * external alarm. Note the use of leading zeros in this message to preserve the
         * character spacing. This is done, I believe, because some autopilots may depend on
         * exact character spacing.
         *
         * To be sent by a navigation receiver when a destination waypoint is active.
         *
         *                                                            14
         *        1 2   3 4    5    6       7 8        9 10  11  12  13|  15
         *        | |   | |    |    |       | |        | |   |   |   | |   |
         * $--RMB,A,x.x,a,c--c,c--c,llll.ll,a,yyyyy.yy,a,x.x,x.x,x.x,A,m,*hh<CR><LF>
         *
         * Field Number:
         * 1.  Status, A = Active, V = Invalid
         * 2.  Cross Track error - nautical miles
         * 3.  Direction to Steer, Left or Right
         * 4.  Origin Waypoint ID
         * 5.  Destination Waypoint ID
         * 6.  Destination Waypoint Latitude
         * 7.  N or S
         * 8.  Destination Waypoint Longitude
         * 9.  E or W
         * 10. Range to destination in nautical miles
         * 11. Bearing to destination in degrees True
         * 12. Destination closing velocity in knots
         * 13. Arrival Status, A = Arrival Circle Entered. V = not entered/passed
         * 14. FAA mode indicator (NMEA 2.3 and later)
         * 15. Checksum
         *
         * Example: $GPRMB,A,0.66,L,003,004,4917.24,N,12309.57,W,001.3,052.5,000.5,V*0B
         *************************************************************************/
        public void GenericNmeaCommandGprmb()
        {
            int i = 0;
            string output = this.NmeaCommandsClearText[this.CommandParts[i++]];
            char outRecommendedMinimumStatus = char.Parse(this.CommandParts[i++]); // 1. Status, A = Active, V = Invalid A,
            double outCrossTrackError = double.Parse(this.CommandParts[i++]); // 2. Cross Track error -nautical miles 0.66,
            char outDirectionToSteer = char.Parse(this.CommandParts[i++]); // 3. Direction to Steer, Left or Right L,
            string outOriginWaypointId = this.CommandParts[i++]; // 4. Origin Waypoint ID 003,
            string outDestinationWaypointId = this.CommandParts[i++]; // 5. Destination Waypoint ID 004,
            double outDestinationWaypointLatitude = double.Parse(this.CommandParts[i++]); // 6. Destination Waypoint Latitude 4917.24,
            char outDestinationWaypointLatitudeDir = char.Parse(this.CommandParts[i++]); // 7. N or S N,
            double outDestinationWaypointLongitude = double.Parse(this.CommandParts[i++]); // 8. Destination Waypoint Longitude 12309.57,
            char outDestinationWaypointLongitudeDir = char.Parse(this.CommandParts[i++]); // 9. E or W W,
            double outRangeToDestination = double.Parse(this.CommandParts[i++]); // 10. Range to destination in nautical miles 001.3,
            double outBearingToDestination = double.Parse(this.CommandParts[i++]); // 11. Bearing to destination in degrees True 052.5,
            double outDestinationClosingVelocity = double.Parse(this.CommandParts[i++]); // 12. Destination closing velocity in knots 000.5,
            char outArrivalStatus = char.Parse(this.CommandParts[i++]); // 13. Arrival Status, A = Arrival Circle Entered. V = not entered / passedV
            // 14. FAA mode indicator(NMEA 2.3 and later)
            // 15. Checksum *0B
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
        public void GenericNmeaCommandGprte()
        {
            int i = 0;
            string output = this.NmeaCommandsClearText[this.CommandParts[i++]];

            // 1. Total number of RE sentences being transmitted
            // 2. Sentence Number
            // 3. Sentence mode
            // c = complete route, all waypoints
            // w = working route, the waypoint you just left, the waypoint you’re heading to, then all the rest
            // 4. Route ID
            // 5. Waypoint ID
        }

        
        /************************************************************************
         * XTE - Cross-Track Error, Measured
         * Measured cross track error is a small subset of the RMB message for
         * compatibility with some older equipment designed to work with Loran.
         * Note that the same limitations apply to this message as the ones in the
         * RMB since it is expected to be decoded by an autopilot.
         *
         *        1 2 3   4 5 6   7
         *        | | |   | | |   |
         * $--XTE,A,A,x.x,a,N,m,*hh<CR><LF>
         *
         * Field Number:
         *
         * 1. Status
         *    A - Valid
         *    V = Loran-C Blink or SNR warning
         *    V = general warning flag or other navigation systems when a reliable fix is not available
         * 2. Status
         *    V = Loran-C Cycle Lock warning flag
         *    A = Valid
         * 3. Cross Track Error Magnitude
         * 4. Direction to steer, L or R
         * 5. Cross Track Units, N = Nautical Miles
         * 6. FAA mode indicator (NMEA 2.3 and later, optional)
         * 7. Checksum
         *
         * Example: $GPXTE,V,V,,,N,S*43
         *************************************************************************/
        public void GenericNmeaCommandGpxte()
        {
            int i = 0;
            string output = this.NmeaCommandsClearText[this.CommandParts[i++]];

            char outGeneralWarningFlag = char.Parse(this.CommandParts[i++]); // 1. Status A - Valid, V = Loran - C Blink or SNR warning, V = general warning flag or other navigation systems when a reliable fix is not available
            char outLoranCCycleLockFlag = char.Parse(this.CommandParts[i++]); // 2. Status V = Loran - C Cycle Lock warning flag, A = Valid
            string outCrossTrackErrorMagnitude = this.CommandParts[i++]; // 3. Cross Track Error Magnitude
            char outDirectionToSteer = char.Parse(this.CommandParts[i++]); // 4. Direction to steer, L or R
            char outCrossTrackUnits = char.Parse(this.CommandParts[i++]); // 5. Cross Track Units, N = Nautical Miles
            //char out = char.Parse(this.CommandParts[i++]); // 6. FAA mode indicator(NMEA 2.3 and later, optional)
            // 7.Checksum
        }


        /************************************************************************
         * WPL - Waypoint Location
         * Waypoint Location data provides essential waypoint data. It is output when
         * navigating to indicate data about the destination and is sometimes supported
         * on input to redefine a waypoint location. Note that waypoint data as defined
         * in the standard does not define altitude, comments, or icon data. When a route
         * is active, this sentence is sent once for each waypoint in the route, in
         * sequence. When all waypoints have been reported, the RTE sentence is sent in
         * the next data set. In any group of sentences, only one WPL sentence, or an RTE
         * sentence, will be sent.
         *
         *        1       2 3        4 5    6
         *        |       | |        | |    |
         * $--WPL,llll.ll,a,yyyyy.yy,a,c--c*hh<CR><LF>
         *
         * Field Number:
         *
         * 1. Latitude
         * 2. N or S (North or South)
         * 3. Longitude
         * 4. E or W (East or West)
         * 5. Waypoint name
         * 6. Checksum
         *
         * Ex. $GPWPL,4807.038,N,01131.000,E,WPTNME*5C
         ************************************************************************/
        public void GenericNmeaCommandGpwpl()
        {
            int i = 0;
            string output = this.NmeaCommandsClearText[this.CommandParts[i++]];
            double outLatitude; // 1. Latitude
            char outoutLatitudeDir = char.Parse(this.CommandParts[i++]); // 2.N or S (North or South)
            double outLongitude = double.Parse(this.CommandParts[i++]); // 3. Longitude
            char outLongitudeDir = char.Parse(this.CommandParts[i++]); // 4. E or W(East or West)
            string outWaypoint = this.CommandParts[i++]; // 5. Waypoint name
            // 6. Checksum
        }


        // Position
        /************************************************************************
         * GGA - Global Positioning System Fix Data
         * This is one of the sentences commonly emitted by GPS units.
         *
         * Time, Position and fix related data for a GPS receiver.
         *
         *                                                      11
         *        1         2       3 4        5 6 7  8   9  10 |  12 13  14   15
         *        |         |       | |        | | |  |   |   | |   | |   |    |
         * $--GGA,hhmmss.ss,llll.ll,a,yyyyy.yy,a,x,xx,x.x,x.x,M,x.x,M,x.x,xxxx*hh<CR><LF>
         *
         * Field Number:
         *
         * 1. UTC of this position report
         * 2. Latitude
         * 3. N or S (North or South)
         * 4. Longitude
         * 5. E or W (East or West)
         * 6. GPS Quality Indicator (non null)
         *    0 - fix not available,
         *    1 - GPS fix,
         *    2 - Differential GPS fix (values above 2 are 2.3 features)
         *    3 = PPS fix
         *    4 = Real Time Kinematic
         *    5 = Float RTK
         *    6 = estimated (dead reckoning)
         *    7 = Manual input mode
         *    8 = Simulation mode
         * 7. Number of satellites in use, 00 - 12
         * 8. Horizontal Dilution of precision (meters)
         * 9. Antenna Altitude above/below mean-sea-level (geoid) (in meters)
         * 10. Units of antenna altitude, meters
         * 11. Geoidal separation, the difference between the WGS-84 earth ellipsoid and mean-sea-level (geoid), "-" means mean-sea-level below ellipsoid
         * 12. Units of geoidal separation, meters
         * 13. Age of differential GPS data, time in seconds since last SC104 type 1 or 9 update, null field when DGPS is not used
         * 14. Differential reference station ID, 0000-1023
         * 15. Checksum
         *
         * Example:
         * $GNGGA,001043.00,4404.14036,N,12118.85961,W,1,12,0.98,1113.0,M,-21.3,M,,*47
         *
         * If the height of geoid is missing then the altitude should be suspect. Some non-standard implementations report altitude with respect to the ellipsoid rather than geoid altitude. Some units do not report negative altitudes at all. This is the only sentence that reports altitude.
         *************************************************************************/
        public void GenericNmeaCommandGpgga()
        {
            int i = 0;
            string output = this.NmeaCommandsClearText[this.CommandParts[i++]];

            string outUTCPositionReport = this.CommandParts[i++]; // 123519       Fix taken at 12:35:19 UTC
            string outReportLatitude = this.CommandParts[i++]; // 4807.038: Latitude 48 deg 07.038' N
            char outReportLatitudeDir = char.Parse(this.CommandParts[i++]); // N  
            string outReportLongitude = this.CommandParts[i++];  // 01131.000 Longitude 11 deg 31.000' E
            char outReportLongitudeDir = char.Parse(this.CommandParts[i++]); // E 
            // 1 Fix quality:
            //   0 = invalid
            //   1 = GPS fix(SPS)
            //   2 = DGPS fix
            //   3 = PPS fix
            //   4 = Real Time Kinematic
            //   5 = Float RTK
            //   6 = estimated(dead reckoning)(2.3 feature)
            //   7 = Manual input mode
            //   8 = Simulation mode
            int outReportNumberSatellites = int.Parse(this.CommandParts[i++]);  // 08  Number of satellites being tracked
            double outReportHorizontalDillusion = double.Parse(this.CommandParts[i++]); // 0.9  Horizontal Dilution of precision (meters)
            double outAntennaAltitude = double.Parse(this.CommandParts[i++]); // 545.4 Antenna Altitude above/below mean-sea-level (geoid) (in meters)
            char outAntennaAltitudeUnits = char.Parse(this.CommandParts[i++]);  // Units of antenna altitude, meters
            // 46.9,M Height of geoid(mean sea level) above WGS84 ellipsoid
            // (empty field) time in seconds since last DGPS update
            // (empty field) DGPS station ID number
            // *47          the checksum data, always begins with *
        }


        /************************************************************************
         * GSA - GPS DOP and active satellites
         * GPS DOP and active satellites. This sentence provides details on the nature
         * of the fix. It includes the numbers of the satellites being used in the
         * current solution and the DOP. DOP (dilution of precision) is an indication
         * of the effect of satellite geometry on the accuracy of the fix. It is a
         * unitless number where smaller is better. For 3D fixes using 4 satellites
         * a 1.0 would be considered to be a perfect number, however for overdetermined
         * solutions it is possible to see numbers below 1.0.
         *
         * There are differences in the way the PRN's are presented which can effect the
         * ability of some programs to display this data. For example, in the example
         * shown below there are 5 satellites in the solution and the null fields are
         * scattered indicating that the almanac would show satellites in the null
         * positions that are not being used as part of this solution. Other receivers
         * might output all of the satellites used at the beginning of the sentence with
         * the null field all stacked up at the end. This difference accounts for some
         * satellite display programs not always being able to display the satellites
         * being tracked. Some units may show all satellites that have ephemeris data
         * without regard to their use as part of the solution but this is non-standard.
         *
         * This is one of the sentences commonly emitted by GPS units.
         *
         *        1 2 3                        14 15  16  17  18
         *        | | |                         |  |   |   |   |
         * $--GSA,a,a,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x.x,x.x,x.x*hh<CR><LF>
         *
         * Field Number:
         *
         * 1. Selection mode: M=Manual, forced to operate in 2D or 3D, A=Automatic, 2D/3D
         * 2. Mode (1 = no fix, 2 = 2D fix, 3 = 3D fix)
         * 3. ID of 1st satellite used for fix
         * 4. ID of 2nd satellite used for fix
         * 5. ID of 3rd satellite used for fix
         * 6. ID of 4th satellite used for fix
         * 7. ID of 5th satellite used for fix
         * 8. ID of 6th satellite used for fix
         * 9. ID of 7th satellite used for fix
         * 10. ID of 8th satellite used for fix
         * 11. ID of 9th satellite used for fix
         * 12. ID of 10th satellite used for fix
         * 13. ID of 11th satellite used for fix
         * 14. ID of 12th satellite used for fix
         * 15. PDOP
         * 16. HDOP
         * 17. VDOP
         * 18. Checksum
         *
         * Example:
         * $GNGSA,A,3,80,71,73,79,69,,,,,,,,1.83,1.09,1.47*17
         *
         * Note: NMEA 4.1+ systems (in particular u-blox 9) emit an extra field
         * just before the checksum.
         *
         * 1 = GPS L1C/A, L2CL, L2CM
         * 2 = GLONASS L1 OF, L2 OF
         * 3 = Galileo E1C, E1B, E5 bl, E5 bQ
         * 4 = BeiDou B1I D1, B1I D2, B2I D1, B2I D12
         *************************************************************************/
        public void GenericNmeaCommandGpgsa()
        {
            int i = 0;
            string output = this.NmeaCommandsClearText[this.CommandParts[i++]];

            // 1.Selection mode: M = Manual, forced to operate in 2D or 3D, A = Automatic, 2D / 3D
            // 2.Mode(1 = no fix, 2 = 2D fix, 3 = 3D fix)
            string outSatellite1 = this.CommandParts[i++]; // 3.ID of 1st satellite used for fix
            string outSatellite2 = this.CommandParts[i++]; // 4.ID of 2nd satellite used for fix
            string outSatellite3 = this.CommandParts[i++]; // 5.ID of 3rd satellite used for fix
            string outSatellite4 = this.CommandParts[i++]; // 6.ID of 4th satellite used for fix
            string outSatellite5 = this.CommandParts[i++]; // 7.ID of 5th satellite used for fix
            string outSatellite6 = this.CommandParts[i++];// 8.ID of 6th satellite used for fix
            string outSatellite7 = this.CommandParts[i++];// 9.ID of 7th satellite used for fix
            string outSatellite8 = this.CommandParts[i++];// 10.ID of 8th satellite used for fix
            string outSatellite9 = this.CommandParts[i++];// 11.ID of 9th satellite used for fix
            string outSatellite10 = this.CommandParts[i++];// 12.ID of 10th satellite used for fix
            string outSatellite11 = this.CommandParts[i++];// 13.ID of 11th satellite used for fix
            string outSatellite12 = this.CommandParts[i++]; // 14.ID of 12th satellite used for fix
            string outDilutionPrecision = this.CommandParts[i++]; // 15.PDOP (dilution of precision)
            string outHorizDilutionPrecision = this.CommandParts[i++]; // 16.HDOP (Horizontal dilution of precision) 
            string outVerticalDilutionPrecision = this.CommandParts[i++]; // 17.VDOP (Vertical dilution of precision)

            /*
             * Note: NMEA 4.1+ systems (in particular u-blox 9) emit an extra field
             *just before the checksum.
             */

            // 1 = GPS L1C / A, L2CL, L2CM
            // 2 = GLONASS L1 OF, L2 OF
            // 3 = Galileo E1C, E1B, E5 bl, E5 bQ
            // 4 = BeiDou B1I D1, B1I D2, B2I D1, B2I D12
            if (i < this.CommandParts.Length)
            {
                string outEkstra = this.CommandParts[i++];
            }

            /// \todo tjek værdier med checksum
        }

        
        /************************************************************************
         * GSV - Satellites in View
         * shows data about the satellites that the unit might be able to find
         * based on its viewing mask and almanac data. It also shows current
         * ability to track this data. Note that one GSV sentence only can provide
         * data for up to 4 satellites and thus there may need to be 3 sentences
         * for the full information. It is reasonable for the GSV sentence to contain
         * more satellites than GGA might indicate since GSV may include satellites
         * that are not used as part of the solution. It is not a requirment that
         * the GSV sentences all appear in sequence. To avoid overloading the data
         * bandwidth some receivers may place the various sentences in totally
         * different samples since each sentence identifies which one it is.
         *
         * The field called SNR (Signal to Noise Ratio) in the NMEA standard is often
         * referred to as signal strength. SNR is an indirect but more useful value
         * that raw signal strength. It can range from 0 to 99 and has units of dB
         * according to the NMEA standard, but the various manufacturers send different
         * ranges of numbers with different starting numbers so the values themselves
         * cannot necessarily be used to evaluate different units. The range of working
         * values in a given gps will usually show a difference of about 25 to 35 between
         * the lowest and highest values, however 0 is a special case and may be shown on
         * satellites that are in view but not being tracked.
         *
         * $GPGSV,2,1,08,01,40,083,46,02,17,308,41,12,07,344,39,14,22,228,45*75
         *
         * where:
         *     GSV          Satellites in view
         *     2           Number of sentences for full data
         *     1            sentence 1 of 2
         *     08           Number of satellites in view
         *     01           Satellite PRN number
         *     40           Elevation, degrees
         *     083          Azimuth, degrees
         *     46           SNR - higher is better
         *                  for up to 4 satellites per sentence
         *     *75          the checksum data, always begins with *
         *************************************************************************/
        public void GenericNmeaCommandGpgsv()
        {
            int i = 0;
            string output = this.NmeaCommandsClearText[this.CommandParts[i++]];
        }


        /************************************************************************
         * RMC - NMEA has its own version of essential gps pvt (position, velocity, time) data.
         * It is called RMC, The Recommended Minimum, which will look similar to:
         *
         * $GPRMC,123519,A,4807.038,N,01131.000,E,022.4,084.4,230394,003.1,W*6A
         * where:
         *     RMC          Recommended Minimum sentence C
         *     123519       Fix taken at 12:35:19 UTC
         *     A            Status A=active or V=Void.
         *     4807.038,N   Latitude 48 deg 07.038' N
         *     01131.000,E  Longitude 11 deg 31.000' E
         *     022.4        Speed over the ground in knots
         *     084.4        Track angle in degrees True
         *     230394       Date - 23rd of March 1994
         *     003.1,W      Magnetic Variation
         *     *6A          The checksum data, always begins with *
         *
         * Note that, as of the 2.3 release of NMEA, there is a new field in the
         * RMC sentence at the end just prior to the checksum. For more information
         * on this field see here.
          ************************************************************************/
        public void GenericNmeaCommandGprmc()
        {
            int i = 0;
            string output = this.NmeaCommandsClearText[this.CommandParts[i++]];
        }

        
        /************************************************************************
         * GLL - Geographic Latitude and Longitude
         * is a holdover from Loran data and some old units may not send the time
         * and data active information if they are emulating Loran data. If a gps
         * is emulating Loran data they may use the LC Loran prefix instead of GP.
         *
         * $GPGLL,4916.45,N,12311.12,W,225444,A,*1D
         *
         * where:
         *     GLL          Geographic position, Latitude and Longitude
         *     4916.46,N    Latitude 49 deg. 16.45 min. North
         *     12311.12,W   Longitude 123 deg. 11.12 min. West
         *     225444       Fix taken at 22:54:44 UTC
         *     A            Data Active or V (void)
         *     *iD          checksum data
         *
         * Note that, as of the 2.3 release of NMEA, there is a new field in the GLL
         * sentence at the end just prior to the checksum. For more information on
         * this field see here.
          ************************************************************************/
        public void GenericNmeaCommandGpgll()
        {
            int i = 0;
            string output = this.NmeaCommandsClearText[this.CommandParts[i++]];
        }

        
        /************************************************************************
         * VTG - Velocity made good.
         * The gps receiver may use the LC prefix instead of GP if it is emulating
         * Loran output.
         *
         * $GPVTG,054.7,T,034.4,M,005.5,N,010.2,K*48
         *
         * where:
         *     VTG          Track made good and ground speed
         *     054.7,T      True track made good (degrees)
         *     034.4,M      Magnetic track made good
         *     005.5,N      Ground speed, knots
         *     010.2,K      Ground speed, Kilometers per hour
         *     *48          Checksum
         *
         * Note that, as of the 2.3 release of NMEA, there is a new field in the
         * VTG sentence at the end just prior to the checksum. For more information
         * on this field see here.
         *
         * Receivers that don't have a magnetic deviation (variation) table built
         * in will null out the Magnetic track made good.
          ************************************************************************/
        public void GenericNmeaCommandGpvtg()
        {
            int i = 0;
            string output = this.NmeaCommandsClearText[this.CommandParts[i++]];
        }


        /************************************************************************
         * ALM - GPS Almanac Data
         * contains GPS week number, satellite health and the complete almanac
         * data for one satellite. Multiple messages may be transmitted, one for
         * each satellite in the GPS constellation, up to maximum of 32 messages.
         * Note that these sentences can take a long time to send so they are not
         * generally sent automatically by the gps receiver. (Sorry I don't have
         * an exact example of the sentence.) Note that this sentence breaks the
         * 80 character rule. Also note that this sentence is often accepted as
         * input so that you can preload a new almanac in a receiver.
         *
         * $GPALM,A.B,C.D,E,F,hh,hhhh,...
         *
         * where:
         *     ALM   Almanac Data being sent
         *     A     Total number of messages
         *     B     Message number
         *     C     Satellite PRN number
         *     D     GPS week number (0-1023)
         *     E     Satellite health (bits 17-24 of message)
         *     F     eccentricity
         *     hh    t index OA, almanac reference time
         *     hhhh  sigma index 1, inclination angle
         *     ...   OMEGADOT rate of right ascension
         *           SQRA(A) root of semi-major axis
         *           Omega, argument of perigee
         *           Omega index 0, longitude of ascension node
         *           M index 0, mean anomaly
         *           a index f0, clock parameter
         *           a index f1, clock parameter
          ************************************************************************/
        public void GenericNmeaCommandGpalm()
        {
            int i = 0;
            string output = this.NmeaCommandsClearText[this.CommandParts[i++]];
            //     ALM   Almanac Data being sent
            //     A     Total number of messages
            //     B     Message number
            //     C     Satellite PRN number
            //     D     GPS week number (0-1023)
            //     E     Satellite health (bits 17-24 of message)
            //     F     eccentricity
            //     hh    t index OA, almanac reference time
            //     hhhh  sigma index 1, inclination angle
            //     ...   OMEGADOT rate of right ascension
            //           SQRA(A) root of semi-major axis
            //           Omega, argument of perigee
            //           Omega index 0, longitude of ascension node
            //           M index 0, mean anomaly
            //           a index f0, clock parameter
            //           a index f1, clock parameter
        }

        
        /************************************************************************
        /* ZDA - Data and Time
         *
         * $GPZDA,hhmmss.ss,dd,mm,yyyy,xx,yy*CC
         * $GPZDA,201530.00,04,07,2002,00,00*60
         *
         * where:
         *     hhmmss    HrMinSec(UTC)
         *     dd,mm,yyy Day,Month,Year
         *     xx        local zone hours -13..13
         *     yy        local zone minutes 0..59
         *     *CC       checksum
         *
         ************************************************************************/
        public void GenericNmeaCommandGpzda()
        {
            int i = 0;
            string output = this.NmeaCommandsClearText[this.CommandParts[i++]];
        }

        
        /************************************************************************
        /* MSK - Control for a Beacon Receiver
         *
         * $GPMSK,318.0,A,100,M,2*45
         *
         * where:
         *     318.0      Frequency to use
         *     A          Frequency mode, A=auto, M=manual
         *     100        Beacon bit rate
         *     M          Bitrate, A=auto, M=manual
         *     2          frequency for MSS message status (null for no status)
         *     *45        checksum
         *
         ************************************************************************/
        public void GenericNmeaCommandGpmsk()
        {
            int i = 0;
            string output = this.NmeaCommandsClearText[this.CommandParts[i++]];
        }

        
        /************************************************************************
         * MSS - Beacon Receiver Status
         *
         * $GPMSS,55,27,318.0,100,*66
         *
         * where:
         *     55         signal strength in dB
         *     27         signal to noise ratio in dB
         *     318.0      Beacon Frequency in KHz
         *     100        Beacon bitrate in bps
         *     *66        checksum
          ************************************************************************/
        public void GenericNmeaCommandGpmss()
        {
            int i = 0;
            string output = this.NmeaCommandsClearText[this.CommandParts[i++]];
        }
    }
}
