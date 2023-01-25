/******************************************************************************
 * Sample Streams
 * These streams will be modified when a route is active with the inclusion
 * of route specific data.
 * @author      Karsten 'Kaki' Reitan Sørensen
 * @created     11. marts 2020
 ******************************************************************************/
using System;
using System.Collections;
using System.Collections.Generic;

namespace NMEA_connector.testsuite
{
    public class testSuite
    {
        /******************************************************************************
         * Garmin g12 sentences for version 4.57
         *
         * Here are some observations:
         * Notice the complete cycle shows an update interval of 2 seconds which is caused
         * by the fact that there is too much data to fit in one second at 4800 b/s.
         * Upping the b/s rate to 9600 will cause an update every second.
         *
         * Notice that the samples are in real time for each sentence because the GGA sentence
         * shows an update in the time of 1 second.
         *
         * It would be possible to provide update data every second by parsing more sentences
         * since the data is adjusted every second.
         *
         * Notice the gaps in the GSA message where the satellites in use are shown in a
         * there slots as compared to the GSV locations.Some tools do not decode this
         * configuration correctly.
         *
         * Note the GGA sentence starts the sequence every two seconds.
         *
         * This sample is similar for other Garmin receivers designed in the same time
         * frame as the G-12.
         *******************************************************************************/
        public IList<string> GarminG12 = new List<string>()
        {
            "$GPRMC,183729, A,3907.356, N,12102.482, W,000.0,360.0,080301,015.5, E*6F",
            "$GPRMB, A,,,,,,,,,,,, V*71",
            "$GPGGA,183730,3907.356, N,12102.482, W,1,05,1.6,646.4, M,-24.1, M,,*75",
            "$GPGSA, A,3,02,,,07,,09,24,26,,,,,1.6,1.6,1.0*3D",
            "$GPGSV,2,1,08,02,43,088,38,04,42,145,00,05,11,291,00,07,60,043,35*71",
            "$GPGSV,2,2,08,08,02,145,00,09,46,303,47,24,16,178,32,26,18,231,43*77",
            "$PGRME,22.0, M,52.9, M,51.0, M*14",
            "$GPGLL,3907.360, N,12102.481, W,183730, A*33",
            "$PGRMZ,2062, f,3*2D",
            "$PGRMM, WGS 84*06",
            "$GPBOD,, T,, M,,*47",
            "$GPRTE,1,1, c,0*07",
            "$GPRMC,183731, A,3907.482, N,12102.436, W,000.0,360.0,080301,015.5, E*67",
            "$GPRMB, A,,,,,,,,,,,, V*71"
        };


        /******************************************************************************
         * Garmin etrex summit outputs
         * Some observations as compared to the G-12:
         *
         * Information is buffered.It is all for the same second.
         * Information is only updated every two seconds at 4800 b/s.
         * Lat/Lon numbers have an extra digit.
         * This is NMEA 2.3 data as indicated by the extra A at the end of RMC, RMB and
         * GLL.
         *
         * Note that the satellites in use have been shoved to the left of the GSA message
         * instead of the slot location.
         *
         * The RMC sentence starts the sequence.
         * Note the HCHDG sentence for the built in compass.
         * Except for the compass output this sentence list is similar for most Garmin
         * units designed around the time of the Summit receivers, beginning with the emap.
         ***************************************************************************/
        public IList<string> testStringsGarminEtrexSummit = new List<string>
        {
            "$GPRMC,002454, A,3553.5295, N,13938.6570, E,0.0,43.1,180700,7.1, W, A*3F",
            "$GPRMB, A,,,,,,,,,,,, A, A*0B",
            "$GPGGA,002454,3553.5295, N,13938.6570, E,1,05,2.2,18.3, M,39.0, M,,*7F",
            "$GPGSA, A,3,01,04,07,16,20,,,,,,,,3.6,2.2,2.7*35",
            "$GPGSV,3,1,09,01,38,103,37,02,23,215,00,04,38,297,37,05,00,328,00*70",
            "$GPGSV,3,2,09,07,77,299,47,11,07,087,00,16,74,041,47,20,38,044,43*73",
            "$GPGSV,3,3,09,24,12,282,00*4D",
            "$GPGLL,3553.5295, N,13938.6570, E,002454, A, A*4F",
            "$GPBOD,, T,, M,,*47",
            "$GPRTE,1,1, c,*37",
            "$GPRMC,002456, A,3553.5295, N,13938.6570, E,0.0,43.1,180700,7.1, W, A*3D"
        };


        /**************************************************************************
         * Garmin etrex Vista release 2.42 outputs
         *
         * Some observations as compared to the Summit:
         * Output still repeats at a rate of once every 2 seconds and is NMEA 2.3 Data
         * The satellite status sentences are interleaved.The GSV sentences are only sent one in each two second group. Note the example shows sentence two of three. Thus the complete cycle would take 6 seconds.
         * New sentence VTG.
         * The altitude in PGRMZ is from the altimeter while the altitude in the GGA is from the gps computation.
         * Note the HCHDG sentence for the built in compass and is missing for the Legend.
         **********************************************************************************/
        public List<string> testStringsGarminEtrexVista = new List<string>()
        {
            "$GPRMC,023042, A,3907.3837, N,12102.4684, W,0.0,156.1,131102,15.3, E, A*36",
            "$GPRMB, A,,,,,,,,,,,, A, A*0B",
            "$GPGGA,023042,3907.3837, N,12102.4684, W,1,04,2.3,507.3, M,-24.1, M,,*75",
            "$GPGSA, A,3,04,05,,,09,,,24,,,,,2.8,2.3,1.0*36",
            "$GPGSV,3,2,11,09,47,229,42,10,04,157,00,14,00,305,00,24,70,154,33*79",
            "$GPGLL,3907.3837, N,12102.4684, W,023042, A, A*5E",
            "$GPBOD,, T,, M,,*47",
            "$GPVTG,156.1, T,140.9, M,0.0, N,0.0, K*41",
            "$PGRME,8.4, M,23.8, M,25.7, M*2B",
            "$PGRMZ,1735, f*34",
            "$PGRMM, WGS 84*06",
            "$HCHDG,,,,15.3, E*30",
            "$GPRTE,1,1, c,*37",
            "$GPRMC,023044, A,3907.3840, N,12102.4692, W,0.0,156.1,131102,15.3, E, A*37"
        };


        /*******************************************
         * Garmin basic yellow etrex European version
         *
         * Some Ovservations:
         * The sentence sequence starts with RMC and repeats every 2 seconds.
         * The PGRMM sentence is missing so the datum is not identified.
         ******************************************************************************/
        public List<string> testStringsGarminBasicYellowEtrex = new List<string>()
            {
                "$GPRMC,152926, V,6027.8259, N,02225.6713, E,10.8,0.0,190803,5.9, E, S*22",
                "$GPRMB, V,,,,,,,,,,,, A, S*0E",
                "$GPGGA,152926,6027.8259, N,02225.6713, E,8,09,2.0,44.7, M,20.6, M,,*79",
                "$GPGSA, A,3,07,08,09,11,18,23,26,28,29,,,,6.6,2.0,3.0*38",
                "$GPGSV,3,1,09,07,29,138,44,08,22,099,42,09,30,273,44,11,07,057,35*75",
                "$GPGSV,3,2,09,18,28,305,43,23,14,340,39,26,64,222,49,28,60,084,49*7E",
                "$GPGSV,3,3,09,29,52,187,48*4E",
                "$GPGLL,6027.8259, N,02225.6713, E,152926, V, S*48",
                "$GPBOD,, T,, M,,*47",
                "$PGRME,15.0, M,22.5, M,15.0, M*1B",
                "$PGRMZ,147, f,3*19",
                "$GPRTE,1,1, c,*37",
                "$GPRMC,152928, V,6027.8319, N,02225.6713, E,10.8,0.0,190803,5.9, E, S*29"
            };


        /***************************************************************************
         * Magellan GPS companion sentences
         *
         * Some observations:
         * Complete cycle takes two seconds.
         * RMC, GGA, GSA, and GLL are update every second.
         * GSV data is swapped with MGNST data every other second.
         * Time is shown to .xx and for GLL.xxx precision but the unit output is not
         * that accurate.Data seems asynchronous and not tied to top of any particular second.
         * Lat/Lon has an extra digit as compared to the Garmin G-12.
         * There is a third GSV sentence that is technically not required.
         * Notice that all the satellites used are shoved to the left in the GSA message.
         * No geoid corrections are shown in the GGA message.This indicates that altitude is
         * shown with respect to the ellipsoid instead of MSL.
         ****************************************************************************/
        public List<string> testStringsMagellanGPScompanion = new List<string>()
        {
            "$GPGGA,184050.84,3907.3839, N,12102.4772, W,1,05,1.8,00543, M,,,,*33",
            "$GPRMC,184050.84, A,3907.3839, N,12102.4772, W,00.0,000.0,080301,15, E*54",
            "$GPGSA, A,3,24,07,09,26,05,,,,,,,,03.6,01.8,03.1*05",
            "$PMGNST,02.12,3, T,534,05.0,+03327,00*40",
            "$GPGLL,3907.3839, N,12102.4771, W,184051.812, A*2D",
            "$GPGGA,184051.81,3907.3839, N,12102.4771, W,1,05,1.8,00543, M,,,,*34",
            "$GPRMC,184051.81, A,3907.3839, N,12102.4771, W,00.0,000.0,080301,15, E*53",
            "$GPGSA, A,3,24,07,09,26,05,,,,,,,,03.6,01.8,03.1*05",
            "$GPGSV,3,1,08,07,57,045,43,09,48,303,48,04,44,144,,02,39,092,*7F",
            "$GPGSV,3,2,08,24,18,178,44,26,17,230,41,05,13,292,43,08,01,147,*75",
            "$GPGSV,3,3,08,,,,,,,,,,,,,,,,*71",
            "$GPGLL,3907.3840, N,12102.4770, W,184052.812, A*21"
        };


        /***************************************************************************
         * Magellan 315 shown in simulation mode.
         *
         * Some observations:
         * This listing shows navigation sentences simulating a route between two locations,
         * SIM001 and SIM002.
         *
         * GLL starts the sequence and time stamp in the GLL message shows more precision.
         *
         * Update is every 2 seconds.
         * NMEA data is only transmitted in simulation mode or you have an actual fix.
         ****************************************************************************/
        public List<string> testStringsMagellan315 = new List<string>()
        {
            "$GPAPB, A, A,0.0, L, N,,,1.1, M, SIM002,1.1, M,,,*21",
            "$GPGSA, A,3,01,02,03,04,,,,,,,,,2.0,2.0,2.0*34",
            "$GPGSV,3,1,11,01,77,103,,13,53,215,,04,47,300,,20,47,090,*76",
            "$GPGSV,3,2,11,19,24,158,,07,21,237,,25,16,039,,24,11,315,*73",
            "$GPGSV,3,3,11,11,08,149,,27,00,179,,30,00,354,,,,,*46",
            "$GPGLL,5100.2111, N,00500.0006, E,104715.203, A*37",
            "$GPGGA,104715.20,5100.2111, N,00500.0006, E,1,04,2.0,-0047, M,,,,*39",
            "$GPRMB, A,0.00, L, SIM001, SIM002,5102.6069, N,00500.0000, E,002.4,000.,021.7, V*0D",
            "$GPRMC,104715.20, A,5100.2111, N,00500.0006, E,21.7,003.0,140801,01., W*70",
            "$GPAPB, A, A,0.0, L, N,,,1.1, M, SIM002,1.1, M,,,*21",
            "$GPGSA, A,3,01,02,03,04,,,,,,,,,2.0,2.0,2.0*34"
        };


        /***************************************************************************
         * Raytheon RN300 sentences:
         *
         * Some observations:
         * Complete cycle every second triggered off of GGA.
         * Date is NMEA 2.3 with integrity value added.
         * The proprietary raytheon sentences seems to be for WAAS SV #122.
         *
         * Note the new DTM sentences that permits conversion of NMEA datum being used to WGS84.
         * The satellites are listed in an arbitrary order, stacked to the left.
        ***************************************************************************/
        public List<string> testStringRaytheonRN300 = new List<string>()
        {
            "$GPGGA,171537,3350.975, N,11823.991, W,2,07,1.1,-25.8, M,, M,1.8,, D*17",
            "$GPGLL,3350.975, N,11823.991, W,171537, A, D*50",
            "$GPRMC,171537, A,3350.975, N,11823.991, W,0.0,096.5,060401,013.0, E, D*07",
            "$GPVTG,096.5, T,083.5, M,0.0, N,0.0, K, D*22",
            "$GPGSA, A,2,04,09,07,24,02,05,26,,,,,,,1.1,*3C",
            "$GPGSV,2,1,07,04,62,120,47,09,52,292,53,07,42,044,41,24,38,179,45*7B",
            "$GPGSV,2,2,07,02,34,101,43,05,18,304,40,26,09,223,36,,,,*48",
            "$PRAYA,6,1,122,0,0,2,36,1,1,,,,,*5A",
            "$GPDTM, W84,,0.000000, N,0.000000, E,0.0, W84*6F",
            "$GPGGA,171538,3350.974, N,11823.991, W,2,07,1.1,-25.8, M,, M,1.8,, D*19"
        };


        /****************************************************************
         * NavMan 3400 (SiRF chipset sentences)
         *
         * Some observations:
         * A cycle is every second triggered off of GGA.
         * The GSA, GSV sentences are only sent every 4 seconds or so.The actual sentences sent and the rate is adjustable using proprietary NMEA commands.
         * Altitude is based on the ellipsoid model and is not corrected for geoid.Note that no geoid corrections are shown in GGA.
         * All headings are stated as true direction.There are no magnetic direction outputs.
         * The ,0000 at the end of GGA is non standard.
         * Lat/Lon has an extra digit as compared to the Garmin G-12.
         * The clock is shown with millisecond precision.
         * The Navman sends 10 lines of non-nmea ascii data when it is first turned on.Each line does begin with a $.
         * This is a sample sentence sequence. The Navman can be programmed to send less sentences or sentences at a different rate.
         * The Navman uses the SiRF chipset, see above for more data on this chipset.
         * Sentences are stated to be NMEA 2.2 based on documentation.
         *************************************************/
        public List<string> testStringNavMan3400 = new List<string>()
        {
            "$GPGGA,230611.016,3907.3813,N,12102.4635,W,0,04,5.7,507.9,M,,,,0000*11",
            "$GPGLL,3907.3813,N,12102.4635,W,230611.016,V*31",
            "$GPGSA,A,1,27,08,28,13,,,,,,,,,21.7,5.7,20.9*38",
            "$GPGSV,3,1,10,27,68,048,42,08,63,326,43,28,48,239,40,13,39,154,39*7E",
            "$GPGSV,3,2,10,31,38,069,34,10,23,282,,03,12,041,,29,09,319,*7C",
            "$GPGSV,3,3,10,23,07,325,,01,05,145,*7E",
            "$GPRMC,230611.016,V,3907.3813,N,12102.4635,W,0.14,136.40,041002,,*04",
            "$GPVTG,136.40,T,,M,0.14,N,0.3,K*66",
            "$GPGGA,230612.015,3907.3815,N,12102.4634,W,0,04,5.7,508.3,M,,,,0000*13"
        };


        /***************************************************************************
         * Earhmate with SiRF chipset (firmware 2.31)
         *
         * Some observations in comparison with the NavMan.
         * This unit show WAAS/EGNOS (WADGPS) in use.The GGA sentence shows a 2
         * indicating differential gps corrections. The 1.5 at the end shows the
         * age of the dgps correction signal.
         *
         * This is a new chipset firmware release and does support Geoid height in
         * the altitude as shown in the GGA sentence.
         *
         * The RMC sentences shows that there is no support for Magnetic headings.
         * When WAAS/EGNOS was not in use a GLL sentence showed up after the GGA.
         ***************************************************************************/
        public IList<string> testStringEarhmateSiRFChipset = new List<string>()
        {
            "$GPGGA,120557.916,5058.7456,N,00647.0515,E,2,06,1.7,108.5,M,47.6,M,1.5,0000*7A",
            "$GPGSA,A,3,20,11,25,01,14,31,,,,,,,2.6,1.7,1.9*3B",
            "$GPGSV,2,1,08,11,74,137,45,20,58,248,43,07,27,309,00,14,23,044,36*7A",
            "$GPGSV,2,2,08,01,14,187,41,25,13,099,39,31,11,172,37,28,09,265,*71",
            "$GPRMC,120557.916,A,5058.7456,N,00647.0515,E,0.00,82.33,220503,,*39",
            "$GPGGA,120558.916,5058.7457,N,00647.0514,E,2,06,1.7,109.0,M,47.6,M,1.5,0000*71"
        };


        /***************************************************************************
         * Evermore GM-305
         *
         * Some observations
         * This chipset is used in the Deluo universal mouse gps.
         * Update is every second by default.
         *
         * Actual sentences are programmable using proprietary interface. GLL and
         * VTG can be added and others removed.The update interval can be modified.
         * Altitude is given relative to MSL (Geoid height) in GGA
         * Magnetic and True headings are supported.
         ***************************************************************************/
        public IList<string> testStringEvermoreGM305 = new List<string>()
        {
            "$GPGGA,001430.003,3907.3885, N,12102.4767, W,1,05,02.1,00545.6, M,-26.0, M,,*5F",
            "$GPGSA, A,3,15,18,14,,,31,,,23,,,,04.5,02.1,04.0*0F",
            "$GPGSV,3,1,10,15,48,123,35,18,36,064,36,14,77,186,39,03,36,239,29*7A",
            "$GPGSV,3,2,10,09,08,059,,31,35,276,35,17,10,125,,11,08,306,*79",
            "$GPGSV,3,3,10,23,41,059,37,25,06,173,*70",
            "$GPRMC,001430.003, A,3907.3885, N,12102.4767, W,000.0,175.3,220403,015.4, E*71",
            "$GPGGA,001431.003,3907.3885, N,12102.4767, W,1,05,02.1,00545.5, M,-26.0, M,,*5D"
        };


        /***************************************************************************
         * Sony
         *
         * Some observations
         * This is the format of Digittraveler from RadioShack.
         *
         * If batteries are removed for 5 minutes on the Digitraveler the data is wrong.
         * The Sony proprietary message is described above.
         * Altitude is Ellipsoid, not MSL.
         * Heading is True only, Magnetic variation is not provided.
         * VTG, GGA, GLL, RMC, ZDA output every second. GSA and PSNY are alternated
         * with GSV data.
         ***************************************************************************/
        public IList<string> testStringSony = new List<string>()
        {
            "$GPVTG,139.7, T,, M,010.3, N,019.1, K*67",
            "$GPGGA,050306,4259.8839, N,07130.3922, W,0,00,99.9,0010, M,, M,000,0000*66",
            "$GPGLL,4259.8839, N,07130.3922, W,050306, V*20",
            "$GPRMC,050306, V,4259.8839, N,07130.3922, W,010.3,139.7,291003,,*10",
            "$GPZDA,050306,29,10,2003,,*43",
            "$GPGSA, A,1,,,,,,,,,,,,,99.9,99.9,99.9*09",
            "$PSNY,0,00,05,500,06,06,06,06*14"
        };


        /***************************************************************************
         * UBlox
         *
         * Some observations
         * This is a 16 channel unit and shows up to 4 GSV sentences.
         * The sentences were captured at 9600 b/s, some are missing at 4800.
         * WAAS satellites can be used for ranging even if WAAS is turned off.
         ****************************************************************************/
        public IList<string> testStringUBlox = new List<string>()
        {
            "$GPRMC,162254.00, A,3723.02837, N,12159.39853, W,0.820,188.36,110706,,, A*74",
            "$GPVTG,188.36, T,, M,0.820, N,1.519, K, A*3F",
            "$GPGGA,162254.00,3723.02837, N,12159.39853, W,1,03,2.36,525.6, M,-25.6, M,,*65",
            "$GPGSA, A,2,25,01,22,,,,,,,,,,2.56,2.36,1.00*02",
            "$GPGSV,4,1,14,25,15,175,30,14,80,041,,19,38,259,14,01,52,223,18*76",
            "$GPGSV,4,2,14,18,16,079,,11,19,312,,14,80,041,,21,04,135,25*7D",
            "$GPGSV,4,3,14,15,27,134,18,03,25,222,,22,51,057,16,09,07,036,*79",
            "$GPGSV,4,4,14,07,01,181,,15,25,135,*76",
            "$GPGLL,3723.02837, N,12159.39853, W,162254.00, A, A*7C",
            "$GPZDA,162254.00,11,07,2006,00,00*63"
        };
    }
}