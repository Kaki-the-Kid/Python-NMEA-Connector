/***************************************************************************************************
 * @file    NMEALibrary.cs
 * @author  Karsten 'Kaki' Reitan Sørensen
 * @created 25. december 2019
 * @updated 09. september 2020
 * @brief   Funktioner som fortolker en NMEA sætning. Behandler ikke selve input fra
 *          enheder på seriel forbindelsen.
 * @param nmeaCommands  Indeholder de forskellige kommandoer i klar tekst
 ***************************************************************************************************/

using System;
using System.Collections.Generic;
using System.Linq;

namespace NMEA_connector.library {

    // List used to explain commands in log view and other places
    public class NmeaLibrary
    {
        /************************************************************************
         * Funktion som oversætter den enkelte sætning til streng for NMEA log
         * General command prefixes:
         * $GP*** Sentence Titles
         ************************************************************************/
        public void ResolveCommand(string commandLine = null) {

            if (commandLine == null) 
                throw new ArgumentNullException(nameof(commandLine));
            if (string.IsNullOrEmpty(commandLine))
                throw new ArgumentException(@"Value cannot be null or empty.", nameof(commandLine));

            commandLine = commandLine.TrimStart('$');

            if (commandLine.StartsWith("GP")) // Ordinary GPS sentence
            {
                brands.BrandGeneric.entryHandleCommand(commandLine);
            } 
            else if (commandLine.Contains("PG")) // Garmin proprietary sentences
            {
                brands.BrandGarmin.entryHandleCommand(commandLine);
            } 
            else if (commandLine.Contains("PS")) // Starlink proprietary sentences
            {
                brands.BrandStarlink.entryHandleCommand(commandLine);
            } 
            else if (commandLine.Contains("PMG")) // Magellan proprietary sentences
            {
                brands.BrandMagellan.entryHandleCommand(commandLine);
            } 
            else if (commandLine.Contains("PM")) // Motorola proprietary sentences
            {
                brands.BrandMotorola.entryHandleCommand(commandLine);
            } 
            else if (commandLine.Contains("PRWI")) // Rockwell proprietary sentences
            {
                brands.BrandRockwell.entryHandleCommand(commandLine);
            } 
            else if (commandLine.Contains("PSRF"))  // SiRF Chipset proprietary sentences
            {
                brands.BrandSiRf.EntryHandleCommand(commandLine);
            } 
            else if (commandLine.Contains("PMVXG")) // Magnavox system proprietary sentences
            {
                brands.BrandMagnavox.entryHandleCommand(commandLine);
            } 
            else if (commandLine.Contains("PSNY"))  // Sony proprietary sentences
            {
                brands.BrandSony.entryHandleCommand(commandLine);
            }
            else if (commandLine.Contains("PPLT"))  // Pilot proprietary sentences
            {
                brands.BrandPilotGPS.entryHandleCommand(commandLine);
            }
            else  // Kender ikke denne kommando start
            {
                Console.WriteLine("Didn't recognize NMEA $ command: {1}", commandLine.ToString());
            }
        }

        
        public void TransmitJsonCommand() {
        }


        public void ReceiveJsonCommand() {
        }


        // Test streng til beregning af checksum
        public const string testString = "GPRMC,092751.000,A,5321.6802,N,00630.3371,W,0.06,31.66,280511,,,A";


        /*************************************************************************//**
         * Funktion der beregner og returnerer checksum for samlet NMEA kommando
         * @author      Kaki
         * @param       nmeaString
         * @returns     beregnede checksum af givet NMEA streng
         *****************************************************************************/
        public int CalculateChecksum(string nmeaString)
        {
            int csum = 0;

            // Hvis den bliver kaldt med tom værdi bruger vi teststreng
            if (string.IsNullOrEmpty(nmeaString))
                nmeaString = testString;

            //Gennemgå strengen tegn for tegn og XOR enkelte tegns værdi
            foreach (char c in nmeaString)
            {
                csum ^= c;
            }

            Console.WriteLine("{0},*{1}", nmeaString, csum);
            return csum;
        }


        public int ReturnChecksum(string nmeaString)
        {
            var commandLine = nmeaString.Split('*');

            return 0;
        }
    }
}
