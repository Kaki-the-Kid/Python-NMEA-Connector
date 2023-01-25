#include <string.h>
#include <catch.hpp>
#include <N2kMessages.h>

# This is a test file for checking N2k message syntax.
# Each test case deals with a single PGN type.
# Test case sets arbitrary parameter values and checks if the same values are parsed back. Not all messages are tested.

class TEST_CASE():
	#region Test_vars
	msg = "PGN129039 AIS Class B Position"
	N2kMsg       = "" #tN2kMsg 
	MessageID    = [5,0] # uint8_t
	Repeat       = [N2kaisr_Final, N2kaisr_Final] # tN2kAISRepeat
	AISTransceiverInformation    = [N2kaischannel_B_VDL_transmission,N2kaischannel_B_VDL_transmission] # tN2kAISTransceiverInformation
 
	
	UserID       = [7,0] # uint32_t
	Latitude     = [-33.0,0]   # double
	Longitude    = [151.0,0]  # double
	Accuracy     = [true,true] # bool
	RAIM         = [false,false]   # bool
	Seconds      = [4,0]     # uint8_t
	COG          = [0.1,0]   # double
	SOG          = [2.,0]    # double
	Heading      = [0.15, 0] #double
	Unit         = [N2kaisunit_ClassB_CS,N2kaisunit_ClassB_CS] #tN2kAISUnit
	Display      = [true,true] # bool
	DSC          = [false,false] # bool
	Band         = [false,false] # bool
	Msg22        = [true,true] # bool
	Mode         = [N2kaismode_Assigned,N2kaismode_Assigned] # tN2kAISMode 
	State        = [true,true] # bool
	#endregion


	def SetN2kAISClassBPosition(N2kMsg,
		MessageID[0],
		Repeat[0],
		UserID[0],
		Latitude[0],
		Longitude[0],
		Accuracy[0],
		RAIM[0],
		Seconds[0],
		COG[0],
		SOG[0],
		AISTransceiverInformation[0],
		Heading[0],
		Unit[0],
		Display[0],
		DSC[0],
		Band[0],
		Msg22[0],
		Mode[0],
		State[0]):
		return 0
	

	def ParseN2kAISClassBPosition(N2kMsg,
		MessageID[1],
		Repeat[1],
		UserID[1],
		Latitude[1],
		Longitude[1],
		Accuracy[1],
		RAIM[1],
		Seconds[1],
		COG[1],
		SOG[1],
		AISTransceiverInformation[1],
		Heading[1],
		Unit[1],
		Display[1],
		DSC[1],
		Band[1],
		Msg22[1],
		Mode[1],
		State[1]):
		return
 

	# use previous version calls to check for backwards compatibility
	def SetN2kAISClassBPosition(N2kMsg,
		MessageID[0],
		Repeat[0],
		UserID[0],
		Latitude[0],
		Longitude[0],
		Accuracy[0],
		RAIM[0],
		Seconds[0],
		COG[0],
		SOG[0],
		Heading[0],
		Unit[0],
		Display[0],
		DSC[0],
		Band[0],
		Msg22[0],
		Mode[0],
		State[0]):


	def ParseN2kAISClassBPosition(N2kMsg,
		MessageID[1],
		Repeat[1],
		UserID[1],
		Latitude[1],
		Longitude[1],
		Accuracy[1],
		RAIM[1],
		Seconds[1],
		COG[1],
		SOG[1],
		Heading[1],
		Unit[1],
		Display[1],
		DSC[1],
		Band[1],
		Msg22[1],
		Mode[1],
		State[1]):




class myTEST_CASE():
	#region Test_vars
	msg = "PGN130323 Meteorlogical Station Data"
	tN2kMsg                      = N2kMsg
	tN2kMeteorlogicalStationData = data_tx
	data_tx.Mode                 = N2kaismode_Assigned
	data_tx.SystemDate           = 10
	data_tx.SystemTime           = 10.8
	data_tx.Latitude             = -33.1
	data_tx.Longitude            = 151.6
	data_tx.WindSpeed            = 12.3
	data_tx.WindDirection        = 2.1
	data_tx.WindReference        = N2kWind_True_North
	data_tx.WindGusts            = 12.3
	data_tx.AtmosphericPressure  = 100
	data_tx.OutsideAmbientAirTemperature= 19.1
	data_tx.SetStationID("AX12")
	data_tx.SetStationName("StationName")
	#endregion
	
	def SetN2kPGN130323(N2kMsg, data_tx):

	tN2kMeteorlogicalStationData data_rx
	ParseN2kPGN130323(N2kMsg, data_rx)




class TEST_CASE_AIS_AtoN():
	#region Test_vars3
	msglf = "PGN129041 AIS AtoN Navigation Report"
	tN2kMsg 							N2kMsg
	tN2kAISAtoNReportData 				data_tx
	
	data_tx.MessageID                   = 5
	data_tx.Repeat                      = N2kaisr_Final
	data_tx.UserID                      = 7
	data_tx.Longitude                   = -33.0
	data_tx.Latitude                    = 151.0
	data_tx.Accuracy                    = true
	data_tx.RAIM                        = true
	data_tx.Seconds                     = 4
	data_tx.Length                      =  52.5
	data_tx.Beam                        = 21.5
	data_tx.PositionReferenceStarboard  = 3.6
	data_tx.PositionReferenceTrueNorth  = 7.2
	data_tx.AtoNType                    = N2kAISAtoN_beacon_isolated_danger
	data_tx.OffPositionIndicator        = true
	data_tx.VirtualAtoNFlag             = true
	data_tx.AssignedModeFlag            = true
	data_tx.GNSSType                    = N2kGNSSt_Chayka
	data_tx.AtoNStatus                  = 0x00
	data_tx.AISTransceiverInformation   = N2kaischannel_B_VDL_transmission
	data_tx.SetAtoNName("BINGBONG")
	#endregion

	def SetN2kAISAtoNReport(N2kMsg, data_tx):
		return

	AtoNName_RX[34] #char array
	tN2kAISAtoNReportData data_rx
	ParseN2kAISAtoNReport(N2kMsg, data_rx)




class TEST_CASE_PGN(Direction):
	msg = "PGN130577 Direction Data"

	DataMode          = [N2kDD025_Simulator,N2kDD025_Simulator] #tN2kDataMode
	CogReference      = [N2khr_magnetic,N2khr_magnetic] #tN2kHeadingReference
	SID               = [3,0]    #unsigned char 
	COG               = [0.1,0]  #double
	SOG               = [5.0,0]  #double
	Heading           = [0.2,0]  #double
	SpeedThroughWater = [10.0,0] #double
	Set               = [0.15,0] #double
	Drift             = [3.0,0]  #double

	def SetN2kDirectionData(
		N2kMsg,
		DataMode[0],
		CogReference[0],
		SID[0],
		COG[0],
		SOG[0],
		Heading[0],
		SpeedThroughWater[0],
		Set[0],
		Drift[0]):


	def ParseN2kDirectionData(
		N2kMsg,
		DataMode[1],
		CogReference[1],
		SID[1],
		COG[1],
		SOG[1],
		Heading[1],
		SpeedThroughWater[1],
		Set[1],
		Drift[1]):




class TEST_CASE_PGB127233_MOB():
	#region Test_vars
	msg                     = "PGN127233 MOB"
	tN2kMsg                 = N2kMsg
	SID                     = [1,0]     #unsigned char 
	MobEmitterId            = [2,0]     #uint32_t
	MOBStatus               = [MOBNotActive,MOBNotActive] #tN2kMOBStatus
	ActivationTime          = [10.0,0]  #double
	PositionSource          = [PositionReportedByMOBEmitter,PositionReportedByMOBEmitter]#tN2kMOBPositionSource
	PositionDate            = [20,0]    # uint16_t
	PositionTime            = [30.0,0]  # double
	Latitude                = [-33.0,0] # double
	Longitude               = [151.0,0] # double
	COGReference            = [N2khr_error,N2khr_error]#;tN2kHeadingReference
	COG                     = [0.1,0]   # double
	SOG                     = [10.0,0]  # double
	MMSI                    = [1234,0]  # uint32_t
	MOBEmitterBatteryStatus = [Low,Low] # tN2kMOBEmitterBatteryStatus
 	#endregion

	def SetN2kMOBNotification(
		N2kMsg,
		SID[0],
		MobEmitterId[0],
		MOBStatus[0],
		ActivationTime[0],
		PositionSource[0],
		PositionDate[0],
		PositionTime[0],
		Latitude[0],
		Longitude[0],
		COGReference[0],
		COG[0],
		SOG[0],
		MMSI[0],
		MOBEmitterBatteryStatus[0]):
	 
	def ParseN2kMOBNotification(
		N2kMsg,
		SID[1],
		MobEmitterId[1],
		MOBStatus[1],
		ActivationTime[1],
		PositionSource[1],
		PositionDate[1],
		PositionTime[1],
		Latitude[1],
		Longitude[1],
		COGReference[1],
		COG[1],
		SOG[1],
		MMSI[1],
		MOBEmitterBatteryStatus[1]):




class TEST_CASE_PGN127237_HeadingTrackControl():
	#region Test_vars
	msg = "PGN127237 HeadingTrackControl"
	tN2kMsg = N2kMsg
	RudderLimitExceeded      = [N2kOnOff_On,N2kOnOff_On]  #tN2kOnOff
	OffHeadingLimitExceeded  = [N2kOnOff_Off,N2kOnOff_Off]  #tN2kOnOff
	OffTrackLimitExceeded    = [N2kOnOff_On,N2kOnOff_On]  #tN2kOnOff
	Override                 = [N2kOnOff_Off,N2kOnOff_Off]  #tN2kOnOff
	SteeringMode             = [N2kSM_FollowUpDevice,N2kSM_FollowUpDevice]  #tN2kSteeringMode
	TurnMode                 = [N2kTM_RadiusControlled,N2kTM_RadiusControlled]  #tN2kTurnMode
	HeadingReference         = [N2khr_Unavailable,N2khr_Unavailable]  #tN2kHeadingReference
	CommandedRudderDirection = [N2kRDO_Unavailable,N2kRDO_Unavailable]  #tN2kRudderDirectionOrder
	CommandedRudderAngle     = [0.1,0.0]  #double
	HeadingToSteerCourse     = [0.2,0.0]  #double
	Track                    = [0.3,0.0]  #double
	RudderLimit              = [0.4,0.0]  #double
	OffHeadingLimit          = [0.5,0.0]  #double
	RadiusOfTurnOrder        = [10,0.0]  #double
	RateOfTurnOrder          = [0.7,0.0]  #double
	OffTrackLimit            = [4,0.0]  #double
	VesselHeading            = [0.9,0.0]  #double
	#endregion


	def SetN2kHeadingTrackControl(N2kMsg,
		RudderLimitExceeded[0],
		OffHeadingLimitExceeded[0],
		OffTrackLimitExceeded[0],
		Override[0],
		SteeringMode[0],
		TurnMode[0],
		HeadingReference[0],
		CommandedRudderDirection[0],
		CommandedRudderAngle[0],
		HeadingToSteerCourse[0],
		Track[0],
		RudderLimit[0],
		OffHeadingLimit[0],
		RadiusOfTurnOrder[0],
		RateOfTurnOrder[0],
		OffTrackLimit[0],
		VesselHeading[0]):


	def ParseN2kHeadingTrackControl(N2kMsg,
		RudderLimitExceeded[1],
		OffHeadingLimitExceeded[1],
		OffTrackLimitExceeded[1],
		Override[1],
		SteeringMode[1],
		TurnMode[1],
		HeadingReference[1],
		CommandedRudderDirection[1],
		CommandedRudderAngle[1],
		HeadingToSteerCourse[1],
		Track[1],
		RudderLimit[1],
		OffHeadingLimit[1],
		RadiusOfTurnOrder[1],
		RateOfTurnOrder[1],
		OffTrackLimit[1],
		VesselHeading[1]):




class TEST_CASE_PGN_R_WP_Info():
	#region Test_vars
	msg = "PGN129285 Route/WP information"
	N2kMsg1 = ""  #tN2kMsg
	N2kMsg2 = ""  #tN2kMsg
	Start = 1  #uint16_t
	Database = 2  #uint16_t
	Route = 3  #uint16_t
	NavDirectiont =  N2kdir_reverse  #tN2kNavigationDirection
	SupplementaryData = true  #bool
	RouteName = "test route"  #const char*
	#endregion

	SetN2kPGN129285(N2kMsg1, Start, Database, Route, NavDirectiont, (char*)RouteName, N2kDD002_Yes ):

	SetN2kRouteWPInfo(N2kMsg2, Start, Database, Route, NavDirectiont, (char*)RouteName, N2kDD002_Yes ):




class TEST_CASE_PGN_AIS_safety_broadcast():
	#region Test_vars
	msg = "PGN129802 AIS Safety Related Broadcast Message"
	N2kMsg                    = ""  #tN2kMsg 
	MessageID                 = [27, 27]  #uint8_t 
	Repeat                    = [N2kaisr_First, N2kaisr_First]  #tN2kAISRepeat 
	SourceID                  = [2, 2]  #uint32_t 
	AISTransceiverInformation = [N2kaischannel_B_VDL_transmission, N2kaischannel_B_VDL_transmission]  #tN2kAISTransceiverInformation 
	SafetyRelatedText_TX      = "MOB"  #const char * 
	buflen                    = 36  #size_t 
	SafetyRelatedText_RX[buflen]  #char 
	#endregion

	SetN2kAISSafetyRelatedBroadcastMsg(N2kMsg, MessageID[0], Repeat[0], SourceID[0], AISTransceiverInformation[0], (char*)SafetyRelatedText_TX):
	
	
	ParseN2kAISSafetyRelatedBroadcastMsg(N2kMsg, MessageID[1], Repeat[1], SourceID[1], AISTransceiverInformation[1], SafetyRelatedText_RX, buflen)  #




class Test_case_GVTG():
	#region Test_vars
	title   = "PGN129026 GVTG"
	N2kMsg  = ""  #tN2kMsg
	CourseOverGroundTrue     = [0.1, 0.1]  #double
	CourseOverGroundMagnetic = [0.2, 0.2]  #double
	SpeedOverGroundKnots     = [0.3, 0.3]  #double
	SpeedOverGroundKmh       = [0.4, 0.4]  #double
	#endregion

	SetN2kPGN129026(N2kMsg, CourseOverGroundTrue[0], CourseOverGroundMagnetic[0], SpeedOverGroundKnots[0], SpeedOverGroundKmh[0]):

	ParseN2kPGN129026(N2kMsg, CourseOverGroundTrue[1], CourseOverGroundMagnetic[1], SpeedOverGroundKnots[1], SpeedOverGroundKmh[1]):
     
    #list test_msg = []
	msg_sequence = list(msg, N2kMsg, CourseOverGroundTrue, CourseOverGroundMagnetic, SpeedOverGroundKnots, SpeedOverGroundKmh)
    test_msg = dict()
    
	
 '''
	$ GPVTG, 15,5, T ,, M, 1273,9, K, 2359,2, N * 50)
	$ GPVTG, 15,5, T ,, M, 1273,9, K, 2359,2, N * 50)
	$ GPRMC, -002, APRMC, -0002,2,3. N, 92220.232, E, 1273.9,15.5,211015 ,, * 17)
	$ GPVTG, 15.5, T ,, M, 1273.9, K, 2359.2, N * 50 )
	$ GPVTG, 15.5, T 2, 7, 9, 5, 2, 3, 9, 9, 2, 3, 9, 2, 3 N * 50)
	$ GPVTG, 15,5, T ,, M, 1273,9, K, 2359,2, N * 50)
	$ GPVTG, 15,5, T ,, M, 1273,9, K, 2359,2, N * 50)
	$ GPVTG, 15,5, T , 1273,9, K, 2359,2, N * 50)
	$ GPRMC, -00.000,00, A, 21444,902, N, 21444,902, E, 1273.9,15.5.211015 ,, * 17)
	$ GPVTG, 15,5, T ,, M, 1273,9, K, 2359,2 , N * 50)
	$ GPVTG, 15,5, T ,, M, 1273,9, K, 2359,2, N * 50)
	$ GPVTG, 15,5, T ,, M, 1273,9, K, 2359,2, N * 50)
	$ GPVTG, 15,5. M, 1273,9, K, 2359,2, N * 50)
	$ GPRMC, -00000,00, A, 21444,902, N, 21444,902, E, 1273,9,15,5,211015 ,, * 17)
	$ GPVTG, 15,5, T ,, M, 1273,9, K, 2359,2, N * 50)
	$ GPVTG, 15,5, T ,, M, 1273,9, K, 2359,2, N * 50
	$ GPVTG, 15,5, T ,,, MP. K, 2359.2, N * 50)
	$ GPVTG, 15.5, T ,, M, 1273.9, K, 2359.2, N * 50)
	$ GPRMC, -00000.00, A, 21444.902, N, 21444.901, * 21444.9105 E, 9121, * 17)
	$ GPVTG, 15.5, T ,, M, 1273.9, K, 2359.2, N * 50)
	$ GPVTG, 15.5, T ,, M, 1273.9, K, 2359.2, N * 50)
	$ GPVTG, 15.5, T 1, 27, T 1,. , K, 2359.2, N * 50)
	$ GPVTG, 15.5, T ,, M, 1273.9, K, 2359.2, N * 50)
	$ GPRMC, -00000.00, A, 21444.902, N, 21444.907, 9,125, 9,127, E, 9127, 9,125. * 17)
	$ GPVTG, 15,5, T ,, M, 1273,9, K, 2359,2, N * 50)
	$ GPVTG, 15,5, T ,, M, 1273,9, K, 2359,2, N * 50)
	$ GPVTG, 15,5, T ,, T , 1273,9, K, 2359,2, N * 50)
	$ GPVTG, 15,5, T ,, M, 1273,9, K, 2359,2, N * 50)
	$ GPRMC, -00000,00, A, 21444,902, N, 9120,4, 91204, N, 9121,4, 9121,4, 91204, , * 17)
	$ GPVTG, 15,5, T ,, M, 1273,9, K, 2359,2, N * 50)
	$ GPVTG, 15,5, T ,, M, 1273,9, K, 2359,2, N * 50)
	$ GPVTG, 15,5, T ,,, MP. K, 2359.2, N * 50)
	$ GPVTG, 15.5, T ,, M, 1273.9, K, 2359.2, N * 50)
	$ GPRMC, -00000.00, A, 21444.902, N, 21444.901, * 21444.9105 E, 9121, * 17)
	$ GPVTG, 15.5, T ,, M, 1273.9, K, 2359.2, N * 50)
	$ GPVTG, 15.5, T ,, M, 1273.9, K, 2359.2, N * 50)
	$ GPVTG, 15.5, T 1, 27, T 1,. , K, 2359.2, N * 50)
	$ GPVTG, 15.5, T ,, M, 1273.9, K, 2359.2, N * 50)
	$ GPRMC, -00000.00, A, 21444.902, N, 21444.907, 9,125, 9,127, E, 9127, 9,125. * 17)
	$ GPVTG, 15,5, T ,, M, 1273,9, K, 2359,2, N * 50)
	$ GPVTG, 15,5, T ,, M, 1273,9, K, 2359,2, N * 50)
	$ GPVTG, 15,5, T ,, T , 1273,9, K, 2359,2, N * 50)
	$ GPVTG, 15,5, T ,, M, 1273,9, K, 2359,2, N * 50)
	$ GPRMC, -00000,00, A, 21444,902, N, 9120,4, 91204, N, 9121,4, 9121,4, 91204, , * 17)
	$ GPVTG, 15,5, T ,, M, 1273,9, K, 2359,2, N * 50)

	#Initialiser buffere
	$ GPVTG, 15,5, T ,, M, 1273,9, K, 2359,2, N * 50)
	$ GPRMC, -002, APRMC, -002,2,3 N, 92220.232, E, 1273.9,15.5,211015 ,, * 17)
	$ GPVTG, 15.5, T ,, M, 1273.9, K, 2359.2, N * 50)
	$ GPVTG, 15.5, T 2, 7, 9, 5, 2, 3, 9, 9, 2, 3, 9, 2, 3 N * 50)
	$ GPVTG, 15,5, T ,, M, 1273,9, K, 2359,2, N * 50)
	$ GPVTG, 15,5, T ,, M, 1273,9, K, 2359,2, N * 50)
	$ GPVTG, 15,5, T , 1273,9, K, 2359,2, N * 50)
	$ GPRMC, -00.000,00, A, 21444,902, N, 21444,902, E, 1273.9,15.5.211015 ,, * 17)
	$ GPVTG, 15,5, T ,, M, 1273,9, K, 2359,2 , N * 50)
	$ GPVTG, 15,5, T ,, M, 1273,9, K, 2359,2, N * 50)
	$ GPVTG, 15,5, T ,, M, 1273,9, K, 2359,2, N * 50)
	$ GPVTG, 15,5. M, 1273,9, K, 2359,2, N * 50)
	$ GPRMC, -00000,00, A, 21444,902, N, 21444,902, E, 1273,9,15,5,211015 ,, * 17)
	$ GPVTG, 15,5, T ,, M, 1273,9, K, 2359,2, N * 50)
	$ GPVTG, 15,5, T ,, M, 1273,9, K, 2359,2, N * 50)
	$ GPVTG, 15,5, T ,,, MP. K, 2359,2, N * 50)
	$ GPVTG, 15,5, T ,, M, 1273,9, K, 2359,2, N * 50)
	'''

'''
This application can send NMEA 0183 version 2.30 sentences through a Serial Device with default 4800 baud according to the NMEA specification. It may be
needed to scroll down in the list of usable items, to find the desired Serial Device. This depends on the configuration of the computer
The NMEA sentences that can be choosen to send is RMC. GGA. GU., GSA, VTG, ZDA and a custom-made
Additional NMEA sentences will be added later
GPS-Simulator can be used by technicians from RDN to simulate the NMEA output from the Mil GPS
'''
# GGA example: 
# $GPGGA, 123519.4807.038,N,01131.000,E. 1,08,0.9,20,M,47,M,.*47
# RMC example: 
# $GPRMC.123519.A.4807.038,N,01131.000,E,022.4,084.4,230994,003.1,W,A *6A
# Gll example: 
# $GPGLL.5601.7919,N, 1116.972,E,212436.39,A,A*6C
# GSA example: 
# $GPGSA.A.3, 17, 15, 19,24,32, 10, 12.25,..,, 1.77, 1.00, 1.46*09
# VTG example: 
# $GPVTG,36.4,T.36.4,M, 1.00,N, 1.85,K*4E
# ZDA example: 
# $GPZDA.072727.68,02, 12,2019,00,00, *48

''' 
Custom: Copy/Paste, or manually write, a NMEA-sentence in the box to be send
The area that show the sentences that have been sent will be reset for every 50 repeatations to avoid overflow of the TextBlock
If too many sentences are chosen and repetition period is too small compared to the baud rate, the sentences doesn't have time to be sent before a new
update is called.This can confuse the serial device and the program can suddently stop.
Magnetic course is set to the same as true course
Some parametres of the NMEA entences are fixed That is for the moment Fixed Quality = 1 Number of satellites being tracked = 8: Horizontal dilution of
position = 0; Altitude in meters =20; Height of geoid in meters = O; Magnetic Variation = 0; GSA sentence is  atwa¥S fixed

In setup it is possible to change the baud rate from 4800 (default) to 9600 or 38400
'''