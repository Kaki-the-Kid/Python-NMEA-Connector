'''
******************************************************************************************
 * NMEA Controller
 * @file    Program.c     
 * @author  Karsten 'Kaki' Reitan Sørensen
 * @created 
 ******************************************************************************************
 * NMEA kommandoer er en fælles platform for at sende GPS data fra GPS moduler til andre 
 * Benytter Struct som holder alle live data overalt i projektet
 */
'''
import datetime
import StructGPSData


class GPSDataHandler:
	def __init__(self):
		self.GPSData = StructGPSData()
		self.GPSData.GPSAgeCorrection = 4.78
		self.GPSData.GPSTimestamp = "18:55:33 UTF"

	# What does this do?
	#	consol = ConsolUi()
	#	consol.GPSData = self.GPSData
	#	consol.ConsolInit()
