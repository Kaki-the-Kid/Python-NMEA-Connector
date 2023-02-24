#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from Modules.NMEA_GPS_Data.NMEA_GPS_Data import *
from Modules.NMEA_GPS_Data.StructGPSData import *


class ConsolUi():
	# The placeholder for calculated GPS data
	# Ex: $GPGGA,181908.00,3404.7041778,N,07044.3966270,W,4,13,1.00,495.144,M,29.200,M,0.10,0000*40
	 # default constructor
	def __init__(self):
		self.classname: str = "ConsulUi"
		self.GPSData        = StructGPSData()
		
	#public static string[]
	FixQuality: list(
			"GPS fix(SPS)",
			"DGPS fix",
			"PPS fix",
			"Real Time Kinematic",
			"Float RTK",
			"estimated(dead reckoning) (2.3 feature)",
			"Manual input mode",
			"Simulation mode"
		)


	def ParseGpsCommand(gpsString: str = ""):
		pass
	

	def ConsolInit():
		"""
		<value>GPS Menu</value>
		<value>GPS_menu</value>
		<value>1. Kør GPS kommando</value>
		<value>1. Run GPS command</value>
		<value>2. Vis GPS Tid</value>
		<value>2. Show GPS Time</value>
		<value>3. Vis GPS Longitude-Latitude</value>
		<value>3. Show GPS Longitude-Latitude</value>
		<value>4. Udskriv GPS data</value>
		<value>4. Print out GPS data</value>
		<value>5. NMEA og enheds konfiguration</value>
		<value>5. NMEA og Device config</value>
		<value>6. GPS enhed</value>
		<value>6. GPS device</value>
		<value>9. Afslut</value>
		<value>9. Exit</value>
		""" 
     
		keyPressed: int = 0

		while keyPressed != 9:
			os.system('cls')
			print("GPS Menu")
			print("1 Run_GPS_command")
			print("2 Show_GPS_Time")
			print("3 Show_GPS_Longitude_Latitude")
			print("4 Print_out_GPS_data")
			print("9 Exit")

			keyPressed = input()

			match keyPressed:
				case "1":
					os.system('cls')
					print("Type in GPS sentence")
					GPS_Command = str(input())
					self.ParseGpsCommand(GPS_Command)
					break
				case "2":
					os.system('cls')
					print("GPS Time is {0}", "timestamp")
					input()
					break
				case "3":
					os.system('cls')
					print("GPS position")
					print("latitude: {0} deg {1}' {2}, longitude: {3} deg {4}' {5}", "48", "07.038", "E", "11", "31.000", "E");
					input()
					break
				case "9":
					break
				case _:
					print("Not a valid command")
					input()
					break
	

	@staticmethod
	def PrintOutGpsData():
		pass
		#Latitude
		#Longitude
		#Altitude
		#PDOP
		#HDOP
		#VDOP
		#Satellites Tracked
		#Satellites in View


	def GpsChecksum(s: str = ""):
		checksum: int = 0
		chars: int    = 0

		while chars < s.Length:
			chars += 1
			checksum ^= s[chars]

		return checksum


	'''
	The checksum at the end of each sentence is the XOR of all of the bytes in the sentence,
	excluding the initial dollar sign. The following C code generates a checksum for the
	string entered as "mystring" and prints it to the output stream. In the example, a
	sentence from the sample file is used.*/
	'''
	def GpsChecksumMain():
		mystring: str = "GPRMC,092751.000,A,5321.6802,N,00630.3371,W,0.06,31.66,280511,,,A"

		print("String: {0}", mystring)
		print("Checksum: {0}", GpsChecksum(mystring))
  
