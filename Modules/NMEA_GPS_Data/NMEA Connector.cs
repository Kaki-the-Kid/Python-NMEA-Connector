/******************************************************************************************
 * NMEA Controller
 * @file    Program.c     
 * @author  Karsten 'Kaki' Reitan Sørensen
 * @created 
 ******************************************************************************************
 * NMEA kommandoer er en fælles platform for at sende GPS data
 *
 * 
 */
using System;
using System.Collections.Generic;

namespace NMEA_connector
{
	class Program
	{
		/************************************************************
		 * Struct som holder alle live data overalt i projektet
		 ************************************************************/
		static void Main(string[] args)
		{
			var GPSData = new StructGPSData();

			GPSData.GPSAgeCorrection = 4.78;
			GPSData.GPSTimestamp = "18:55:33 UTF";

			var consol = new ConsolUi();
			consol.GPSData = GPSData;

			consol.ConsolInit();
		}
	}
}
