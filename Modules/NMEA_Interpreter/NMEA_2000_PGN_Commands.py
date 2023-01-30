class tNMEA2000():

	# region global_variables

	# @brief Pointer to a message handler
	pNext: tMsgHandler


	# Parameter Group Number*/
	PGN:  int = 0

	# PGN for an Iso Address Claim message
	N2kPGNIsoAddressClaim: int = 60928

	# PGN for a Production Information message
	N2kPGNProductInformation: int = 126996

	# PGN for an Configuration Information message
	N2kPGNConfigurationInformation: int = 126998

	# Document says for lenghts 33,40,24,32, but then values
	# has not been translated right on devices.
	# @brief Max length of ModelID
	#  Document says for leghts 33 but then values has not
	#  been translated right on devices.#/
	Max_N2kModelID_len: int = 32

	# @brief Max length of Software Code
	#  Document says for leghts 40 but then values has not
	#  been translated right on devices.
	Max_N2kSwCode_len: int = 32

	# @brief Max length of Model Version
	#  Document says for leghts 24 but then values has not
	#  been translated right on devices.
	Max_N2kModelVersion_len: int = 32

	# @brief Max length of SerialCode
	#  Document says for leghts 32 but then values has not
	#  been translated right on devices.
	Max_N2kModelSerialCode_len = 32

	# @brief Define length of longest info string
	# Define length of longest info string (from @ref
	# Max_N2kModelID_len, @ref Max_N2kSwCode_len, @ref
	# Max_N2kModelVersion_len, @ref Max_N2kModelSerialCode_len)
	# + 1 termination char
	Max_N2kProductInfoStrLen = 33

	#**********************************************************************/#
	# @brief Max length of Configuration Info Fields
	#
	# I do not know what standard says about max field length, but according
	# to tests NMEAReader crashed with lenght >=90. Some device was reported
	# not to work string length over 70.
	Max_N2kConfigurationInfoField_len = 71  # 70 + '/0'

	# @brief Message buffer time
	Max_N2kMsgBuf_Time = 100

	# @brief Number of message groups
	N2kMessageGroups = 2

	# @brief Max CAN Bus Address given by the library
	N2kMaxCanBusAddress = 251

	# @brief Null Address (???)
	N2kNullCanBusAddress = 254

	# endregion global_variables


	# region Send_NMEA2000_PGN_oplysninger #Tabel 1.
	# region PGN_59392 Message "ISO Acknowledgement"

	#**********************************************************************/#
	# @brief Setting up PGN 59392 Message "ISO Acknowledgement"
	#
	# This message is provided by ISO 11783 for a handshake mechanism
	# between transmitting and receiving devices. This message
	# is the possible response to acknowledge the reception of a “normal
	# broadcast” message or the response to a specific command to indicate
	# compliance or failure.
	#
	# @param N2kMsg		  Reference to a N2kMsg Object, ready to be send
	# @param Control		 Control Byte
	# @param GroupFunction   Group Function value
	# @param PGN			 PGN of requested Information
	#
	# 059392 ISO-bekræftelse
	def SetN2kPGN59392(
					N2kMsg: tN2kMsg,
					Control: int,
					GroupFunction: int,
					PGN: int
				):
		N2kMsg.SetPGN() #59392L
		N2kMsg.Priority=6
		N2kMsg.AddByte(Control)
		N2kMsg.AddByte(GroupFunction)
		N2kMsg.Add4ByteUInt(PGN)

		return True


	#**********************************************************************/#
	# @brief Setting up Message "ISO Acknowledgement" - PGN 59392
	#
	# Alias of PGN 59392. This alias was introduced to improve the readability
	# of the source code. See parameter details on @ref SetN2kPGN59392
	def SetN2kPGNISOAcknowledgement(
					N2kMsg: tN2kMsg,
					Control: int,
					GroupFunction: int,
					PGN: str
				):
		SetN2kPGN59392(N2kMsg,Control,GroupFunction,PGN)
		return True

	# endregion PGN_59392


	# region PGN_60928 ISO-adressekrav
	#**********************************************************************/#
	# 060928 ISO-adressekrav
	# @brief Setting up PGN 60928 Message "ISO Address Claim"
	#
	# This network management message is used to claim a network address and
	# to respond with device information (NAME) requested by the ISO Request
	# or Complex Request Group Function. This PGN contains several fields
	# that are Request Parameters that can be used to control the expected
	# response to requests for this PGN.
	#
	# @param N2kMsg			Reference to a N2kMsg Object, ready to be send
	# @param UniqueNumber	  Unique Number (ISO Identity Number)
	# @param ManufacturerCode  Manufacturer Code
	# @param DeviceFunction	Device Function (ISO Function)
	# @param DeviceClass	   Device Class
	# @param DeviceInstance	Device Instance
	# @param SystemInstance	System Instance (ISO Device Class Instance)
	# @param IndustryGroup	 Industry Group
	#/
	def SetN2kPGN60928(
					N2kMsg: tN2kMsg,
					UniqueNumber: int,
					ManufacturerCode: int,
					DeviceFunction: int,
					DeviceClass: int,
					DeviceInstance: int = 0,
					SystemInstance: int = 0,
					IndustryGroup: int = 4
					):
		return 0


	#**********************************************************************/#
	# @brief Setting up PGN 60928 Message "ISO Address Claim"
	#
	# This network management message is used to claim a network address and
	# to respond with device information (NAME) requested by the ISO Request
	# or Complex Request Group Function. This PGN contains several fields
	# that are Request Parameters that can be used to control the expected
	# response to requests for this PGN.
	#
	# @param N2kMsg			Reference to a N2kMsg Object, ready to be send
	# @param Name			  Name of the device
	#/
	def SetN2kPGN60928(N2kMsg: tN2kMsg, Name: str):
		return 0


	#**********************************************************************/#
	# @brief Setting up Message "ISO Address Claim" - PGN 60928
	#
	# Alias of PGN 60928. This alias was introduced to improve the readability
	# of the source code. See parameter details on @ref SetN2kPGN60928
	#/
	def SetN2kISOAddressClaim(
					N2kMsg: tN2kMsg,
					UniqueNumber: int,
					ManufacturerCode: int,
					DeviceFunction: int = 0,
					DeviceClass: int = 0,
					DeviceInstance: int = 0,
					SystemInstance: int = 0,
					xIndustryGroup: int = 4
				):
		SetN2kPGN60928(
			N2kMsg,
			UniqueNumber,
			ManufacturerCode,
			DeviceFunction,
			DeviceClass,
			DeviceInstance,
			SystemInstance,
			IndustryGroup
			)

		return 0


	#**********************************************************************/#
	# @brief Setting up Message "ISO Address Claim" - PGN 60928
	#
	# Alias of PGN 60928. This alias was introduced to improve the readability
	# of the source code. See parameter details on @ref SetN2kPGN60928
	def SetN2kISOAddressClaim(N2kMsg, Name):
		SetN2kPGN60928(N2kMsg, Name)

	# endregion PGN_60928


	# region PGN_126208 NMEA® anmod om gruppefunktion
	# 126208 NMEA® anmod om gruppefunktion
	# endregion PGN_126208


	# region PGN_126464 #PGN's gruppefunktion

	#**********************************************************************/#
	# 126464 PGN's gruppefunktion
	#
	# @brief Setting up PGN 126464 Message "PGN List - Transmit PGNs group
	#		function"
	#
	# The PGN List group function type is defined by the first field. The
	# message will be either a Transmit PGNs or a Receive PGNs group function
	# that identifies the PGNs transmitted from or received by a node.
	#
	# @note List of PGNs must be null terminated and defined as PROGMEM e.g.
	#		const  TransmitMessages[] PROGMEM={130310L,0};
	#
	# @param N2kMsg		  Reference to a N2kMsg Object, ready to be send
	# @param Destination	 Address of the destination
	# @param tr			  Transmit or Receive, see @ref tN2kPGNList
	# @param PGNs			List of PGNs
	#/
	def SetN2kPGN126464(
					N2kMsg,
					Destination: int,
					tr: tN2kPGNList,
					PGNs: str
				):
		pass


	#**********************************************************************/#
	# @brief Setting up Message "PGN List - Transmit PGNs group
	#		function" - PGN 126464
	#
	# Alias of PGN 126464. This alias was introduced to improve the readability
	# of the source code. See parameter details on @ref SetN2kPGN126464
	#/
	def SetN2kPGNTransmitList(
					N2kMsg,
					Destination: int,
					PGNs: str
				):
		SetN2kPGN126464( N2kMsg, Destination, N2kpgnl_transmit, PGNs )
		pass

	# endregion PGN_126464


	# region PGN_126720 Hurtig pakke, ejendomsbeskyttet
	# 126720 Hurtig pakke, ejendomsbeskyttet
	# endregion PGN_126720


	# region PGN_126992 PGN-liste
	# 126992 PGN-liste
	# *****************************************************************************
	# System time
	def SetN2kPGN126992(
				N2kMsg: tN2kMsg,
				SID: int,
				SystemDate: str,
				SystemTime: float,
				TimeSource: tN2kTimeSource = N2kts_GPS
			):
		N2kMsg.SetPGN() #126992L
		N2kMsg.Priority: int = 3
		N2kMsg.AddByte( SID )
		N2kMsg.AddByte( (TimeSource & 0x0f) | 0xf0 )
		N2kMsg.Add2ByteUInt( SystemDate )
		N2kMsg.Add4ByteUDouble( SystemTime,0.0001 )
		pass


	def ParseN2kPGN126992(
				N2kMsg: tN2kMsg,
				SID: int,
				SystemDate: int,
				SystemTime: float,
				TimeSource: tN2kTimeSource):
		if ( N2kMsg.PGN != 126992):
			return false

		Index: int = 0

		SID=N2kMsg.GetByte(Index)
		TimeSource=(tN2kTimeSource)(N2kMsg.GetByte(Index) & 0x0f)
		SystemDate=N2kMsg.Get2ByteUInt(Index)
		SystemTime=N2kMsg.Get4ByteUDouble(0.0001,Index)

		return True


	#*******************************************************************/#
	# @brief Send a list with all supported Receive messages
	#
	# This function sends a PGN 126464 message consisting of all messages
	# supported by this device for reception.
	#
	# @param Destination   Destination address
	# @param DeviceIndex   index of the device on @ref Devices
	# @param UseTP		 use multi packet message, default = false
	#/
	def SendTxPGNList( Destination: str, DeviceIndex: int ): pass
	def SendRxPGNList( Destination: str, DeviceIndex: int ): pass

	# endregion PGN_126992


	# region PGN_126993 #Message "Heartbeat"
	#**********************************************************************/#
	# 126993 Puls
	# @brief Setting up PGN 126993 Message "Heartbeat"
	#
	# This PGN shall be transmitted by all NMEA devices. Reception of this
	# PGN confirms that a device is still present on the network. Reception
	# of this PGN may also be used to maintain an address to NAME association
	# table within the receiving device.
	#
	# @param N2kMsg			Reference to a N2kMsg Object, ready to be send
	# @param timeInterval_ms   time interval in msec (0.01 - 655.32s )
	# @param sequenceCounter   Sequence counter
	#/
	def SetN2kPGN126993(
					N2kMsg: tN2kMsg,
					timeInterval_ms: int,
					sequenceCounter: int
				):
		pass


	#**********************************************************************/#
	# @brief Setting up Message "Heartbeat" - PGN 126993
	#
	# Alias of PGN 126993. This alias was introduced to improve the readability
	# of the source code. See parameter details on @ref SetN2kPGN126993
	#/
	def SetHeartbeat(
					N2kMsg: tN2kMsg,
					timeInterval_ms: int,
					sequenceCounter: int
					):
		SetN2kPGN126993(N2kMsg, timeInterval_ms, sequenceCounter)
		pass


	#*******************************************************************/#
	# @brief Set the Heartbeat Interval and Offset for a device
	#
	# According to document [NMEA Heartbeat Corrigendum]
	# (https:#www.nmea.org/Assets/20140102%20nmea-2000-126993%20heartbeat%20pgn%20corrigendum.pdf)
	# all NMEA devices shall transmit heartbeat PGN 126993. With this
	# function you can set transmission interval in ms (range 1000-655320ms
	# , default 60000). Set <1000 to disable it.
	# You can temporally change interval by setting SetAsDefault parameter
	# to false. Then you can restore default interval with interval
	# parameter value 0xfffffffe
	#
	# Function allows to set interval over 60 s or 0 to disable sending fr test purposes.
	#
	# @param interval	  Heartbeat Interval in ms
	# @param offset		Heartbeat Offset in ms
	# @param iDev		  index of the device on @ref Devices
	#/
	def SetHeartbeatIntervalAndOffset(
							interval: int,
							offset: int = 0,
							iDev: int = -1
							):
		if ( iDev<0 or iDev >= DeviceCount ):
			return 0

		#Devices[iDev].HeartbeatScheduler.SetPeriod(interval,offset)


	#*******************************************************************/#
	# @brief Get the Heartbeat Interval of a device
	#
	# Heartbeat interval may be changed by e.g. MFD by group function. I
	# have not yet found should changed value be saved for next
	# startup or not.
	#
	# @param iDev		  index of the device on @ref Devices
	# @return uint_32  -> Device heartbeat interval in ms
	#/
	def GetHeartbeatIntervaliDev( iDev: int = 0 ):
		if ( iDev<0 or iDev>=DeviceCount ):
			return 60000

		return Devices[iDev].HeartbeatScheduler.GetPeriod()


	#*******************************************************************/#
	# @brief Get the Heartbeat Offset of a device
	#
	# Heartbeat Offset may be changed by e.g. MFD by group function. I
	# have not yet found should changed value be saved for next
	# startup or not.
	#
	# @param iDev		  index of the device on @ref Devices
	# @return uint_32  -> Device heartbeat Offset in ms
	#/
	def GetHeartbeatOffset( iDev: int = 0 ):
		if ( iDev<0 or iDev>=DeviceCount ):
			return 0

		return Devices[iDev].HeartbeatScheduler.GetOffset()


	#*******************************************************************/#
	# @brief Send heartbeat for specific device.
	#
	# @param iDev		  index of the device on @ref Devices
	#/
	def SendHeartbeat( iDev: int = -1):
		if ( iDev<0 or iDev>=DeviceCount ):
			return

		Devices[iDev].HeartbeatScheduler.ForceSend()


	#*******************************************************************/#
	# @brief Send Heartbeat for all devices
	#
	# Library will automatically send heartbeat, if interval is >0. You
	# can also manually send it any time or force sent, if interval=0;
	#
	# @param force True will send Heartbeat immediately, default = false
	#/
	def SendHeartbeat( force: bool = False ):
		#for (int i=0; i<DeviceCount; i++)
		#	if (force or Devices[i].HeartbeatScheduler.GetPeriod()>0):
		#		Devices[i].HeartbeatScheduler.ForceSend()
		pass

	# endregion PGN_126993 #Message "Heartbeat"


	# region PGN_126996 #Message "Product information"
	# 126996 Produktoplysninger
	#**********************************************************************/#
	# @brief Setting up PGN 126996 Message "Product information"
	#
	# Provides product information onto the network that could be important
	# for determining quality of data coming from this product.
	#
	# @param N2kMsg			  Reference to a N2kMsg Object, ready to be send
	# @param N2kVersion		  NMEA Network Message Database Version
	# @param ProductCode		 NMEA Manufacturer's Product Code
	# @param ModelID			 Manufacturer's Model ID
	# @param SwCode			  Manufacturer's Software Version Code
	# @param ModelVersion		Manufacturer's Model Version
	# @param ModelSerialCode	 Manufacturer's Model Serial Code
	# @param CertificationLevel  NMEA 2000 Certification Level
	# @param LoadEquivalency	 Load Equivalency
	#/
	def SetN2kPGN126996(
					N2kMsg: tN2kMsg,
					N2kVersion: int,
					ProductCode: int,
					ModelID: str,
					SwCode: str,
					ModelVersion: str,
					ModelSerialCode: str,
					CertificationLevel: int = 1,
					LoadEquivalency: int = 1
				):
		pass


	#**********************************************************************/#
	# @brief Setting up Message "Product information" - PGN 126996
	#
	# Alias of PGN 126996. This alias was introduced to improve the readability
	# of the source code. See parameter details on @ref SetN2kPGN126996
	#/
	def SetN2kProductInformation(
						N2kMsg: tN2kMsg,
						N2kVersion: int,
						ProductCode: int,
						ModelID: str,
						SwCode: str,
						ModelVersion: str,
						ModelSerialCode: str,
						CertificationLevel: int = 1,
						LoadEquivalency: int = 1
					):
		SetN2kPGN126996(
				N2kMsg,
			N2kVersion,
		ProductCode,
		ModelID,
	SwCode,
	ModelVersion,
					ModelSerialCode,
				CertificationLevel,
			LoadEquivalency
	)


	#**********************************************************************/#
	# @brief  Parsing the content of message PGN 126996 "Product information"
	#
	# Provides product information onto the network that could be important
	# for determining quality of data coming from this product.
	#
	# @param N2kMsg			  Reference to a N2kMsg Object, ready to be send
	# @param N2kVersion		  NMEA Network Message Database Version
	# @param ProductCode		 NMEA Manufacturer's Product Code
	# @param ModelIDSize		 Size of ModelID
	# @param ModelID			 Manufacturer's Model ID
	# @param SwCodeSize		  Size of Software Version Code
	# @param SwCode			  Manufacturer's Software Version Code
	# @param ModelVersionSize	Size of Model Version
	# @param ModelVersion		Manufacturer's Model Version
	# @param ModelSerialCodeSize Size of Model Serial Code
	# @param ModelSerialCode	 Manufacturer's Model Serial Code
	# @param CertificationLevel  NMEA 2000 Certification Level
	# @param LoadEquivalency	 Load Equivalency
	#
	# @return true	 Parsing of PGN Message successful
	# @return false	Parsing of PGN Message aborted
	#/
	def ParseN2kPGN126996(
					N2kMsg: tN2kMsg,
					N2kVersion: str,
					ProductCode: str,
					ModelIDSize: int,
					ModelID: str,
				SwCodeSize: int,
			SwCode,
					ModelVersionSize: int,
					ModelVersion,
					ModelSerialCodeSize: int,
					ModelSerialCode: str,
					CertificationLevel: str,
					LoadEquivalency: str
				): pass

	# endregion PGN_126996 #Message "Product information"


	# region PGN_126998 #Message "Configuration information"
	# 126998 Konfigurationsoplysninger
	#**********************************************************************/#
	# @brief Setting up PGN 126998 Message "Configuration information"
	#
	# Free-form alphanumeric fields describing the installation (e.g.,
	# starboard engine room location) of the device and installation
	# notes (e.g., calibration data).
	#
	# @param N2kMsg			  Reference to a N2kMsg Object, ready to be send
	# @param ManufacturerInformation   Manufacturer Information
	# @param InstallationDescription1  Installation Description, Field 1
	# @param InstallationDescription2  Installation Description, Field 2
	# @param UsePgm			  Use program memory, default = false
	#/
	def SetN2kPGN126998(
					N2kMsg: tN2kMsg,
					ManufacturerInformation: int = 0,
					InstallationDescription1: int = 0,
					InstallationDescription2: int = 0,
					UsePgm: bool = False
				):
		pass


	#**********************************************************************/#
	# @brief Setting up Message "Configuration information" - PGN 126998
	#
	# Alias of PGN 126998. This alias was introduced to improve the readability
	# of the source code. See parameter details on @ref SetN2kPGN126998
	#/
	def SetN2kConfigurationInformation(
								N2kMsg: tN2kMsg,
								ManufacturerInformation: int,
								InstallationDescription1 = 0,
								InstallationDescription2 = 0,
								UsePgm: bool = false
							):
		SetN2kPGN126998(
			N2kMsg,
			ManufacturerInformation,
			InstallationDescription1,
			InstallationDescription2,
			UsePgm)
		return True


	#**********************************************************************/#
	# @brief Parsing the content of message PGN 126998
	#	"Configuration information"
	#
	# Free-form alphanumeric fields describing the installation (e.g.,
	# starboard engine room location) of the device and installation
	# notes (e.g., calibration data).
	#
	# @param N2kMsg			Reference to a N2kMsg Object
	# @param ManufacturerInformationSize Size off Manufacturer Information
	# @param ManufacturerInformation	 Manufacturer Information
	# @param InstallationDescription1Size Size off Installation Description
	# @param InstallationDescription1	Installation Description, Field 1
	# @param InstallationDescription2Size Size off Installation Description
	# @param InstallationDescription2	Installation Description, Field 2
	#
	# @return true	 Parsing of PGN Message successful
	# @return false	Parsing of PGN Message aborted
	#
	#/
	def ParseN2kPGN126998(
				N2kMsg: tN2kMsg,
					ManufacturerInformationSize,
					ManufacturerInformation: str,
					InstallationDescription1Size,
					InstallationDescription1: str,
					InstallationDescription2Size,
					InstallationDescription2: str
				):
		pass

	# endregion PGN_126998 #Message "Configuration information"


	# region PGN_129799
	# 129799 Radiofrekvens/-tilstand/-effekt
	# endregion PGN_129799


	# region PGN_129808
	# 129808 DSC-opkaldsoplysninger
	# endregion PGN_129808

	# endregion Send_NMEA2000_PGN_oplysninger


	# region Modtag_NMEA2000_PGN_Oplysninger #Tabel 2. Modtag
	# region PGN_059392 ISO-bekræftelse
	# 059392 ISO-bekræftelse
	# endregion PGN_059392


	# region PGN_059904 ISO-anmodning
	#**********************************************************************/#
	# 059904 ISO-anmodning
	# @brief Setting up PGN 59904 Message "ISO request"
	#
	# As defined by ISO, this message has a data length of 3 bytes with no
	# padding added to complete the single frame. The appropriate response
	# to this message is based on the PGN being requested, and whether the
	# receiver supports the requested PGN.
	#
	# @param N2kMsg			Reference to a N2kMsg Object, ready to be send
	# @param Destination	   Address of the destination
	# @param RequestedPGN	  PGN being requested
	#/
	def SetN2kPGN59904(
				N2kMsg: tN2kMsg,
			Destination,
		RequestedPGN
	):
		pass

	#**********************************************************************/#
	# @brief Setting up Message "ISO request" - PGN 59904
	#
	# Alias of PGN 59904. This alias was introduced to improve the readability
	# of the source code. See parameter details on @ref SetN2kPGN59904
	#/
	def SetN2kPGNISORequest(
					N2kMsg: tN2kMsg,
				Destination: int,
			RequestedPGN: int
	):
		SetN2kPGN59904( N2kMsg, Destination, RequestedPGN )
		pass

	#**********************************************************************/#
	# @brief Parsing the content of message PGN 59904 "ISO request"
	#
	# As defined by ISO, this message has a data length of 3 bytes with no
	# padding added to complete the single frame. The appropriate response
	# to this message is based on the PGN being requested, and whether the
	# receiver supports the requested PGN.
	#
	# @param N2kMsg		Reference to a N2kMsg Object
	# @param RequestedPGN  PGN being requested
	#
	# @return true	 Parsing of PGN Message successful
	# @return false	Parsing of PGN Message aborted
	#/
	def ParseN2kPGN59904(N2kMsg: tN2kMsg, RequestedPGN: int):
		pass


	#**********************************************************************/#
	# @brief Parsing the content of a "ISO request"
	#		message - PGN 59904
	#
	# Alias of PGN 59904. This alias was introduced to improve the readability
	# of the source code. See parameter details on @ref ParseN2kPGN59904
	#/
	def ParseN2kPGNISORequest(
						N2kMsg: tN2kMsg,
						RequestedPGN: int
						):
		return bool( ParseN2kPGN59904(N2kMsg, RequestedPGN) )

	# endregion PGN_059392 ISO-bekræftelse


	# region PGN_060160 #ISO-transportprotokol, dataoverførsel
	# 060160 ISO-transportprotokol, dataoverførsel
	# endregion PGN_060160


	# region PGN_060416 #ISO-transportprotokol, administration af tilslutning
	#*******************************************************************/#
	# 060416 ISO-transportprotokol, administration af tilslutning – RTS gruppefunktion
	# @brief   Send ISO Transport Protocol message RTS
	#
	# @param iDev	index of the device on @ref Devices
	#
	# @return true
	# @return false
	#/
	def SendTPCM_RTS( iDev: int):
		return False


	#*******************************************************************/#
	# @brief   Send ISO Transport Protocol message CTS
	#
	# @param PGN				 PGN
	# @param Destination		 Destination address
	# @param iDev	index of the device on @ref Devices
	# @param nPackets			Number of packets
	# @param NextPacketNumber	Number of the next packet
	#
	#/
	def SendTPCM_CTS(PGN: int, Destination: int, iDev: int, nPackets: int, NextPacketNumber: int):
		pass


	#********************************************************************/#
	# @brief Send ISO Transport Protocol message End Acknowledge
	#
	# @param PGN				 PGN
	# @param Destination		 Destination address
	# @param iDev	index of the device on @ref Devices
	# @param nBytes			  Number of bytes
	# @param nPackets			Number of packets
	#/
	def SendTPCM_EndAck( PGN: int, Destination: int, iDev: int, nBytes: int, nPackets: int):
		pass


	#*******************************************************************/#
	# @brief Send ISO Transport Protocol message Abort
	#
	# @param PGN			   PGN
	# @param Destination	   Destination address
	# @param iDev	index of the device on @ref Devices
	# @param AbortCode		 Abort Code
	#/
	def SendTPCM_Abort( PGN: int, Destination: int, iDev: int, AbortCode: int ):
		pass


	#*******************************************************************/#
	# @brief Ends sending of ISO-TP message
	#
	# @param iDev	index of the device on @ref Devices
	#/
	def EndSendTPMessage( iDev: int ):
		pass


	#*******************************************************************/#
	# @brief Send pending ISO-TP Messages
	#
	# @param iDev	index of the device on @ref Devices
	#/
	def SendPendingTPMessage( iDev: int ):
		pass


	#********************************************************************/#
	# @brief Check if this message is a Transmit message of this device
	#
	# @param PGN	 PGN to be checked
	# @param iDev	index of the device on @ref Devices
	# @return true
	# @return false
	#/
	def IsTxPGN( PGN: int, iDev: int = 0 ):
		pass

	# endregion PGN_060416


	# region PGN_060928 #ISO-adressekrav
	#*******************************************************************/#
	# 060928 ISO-adressekrav
	# @brief Send an IsoAddressClaim message
	#
	# This is automatically used by class. You only need to use this, if
	# you want to write your own behavior for address claiming.
	#
	# @param Destination	 Destination address for the message
	# @param DeviceIndex	 index of the device on @ref Devices
	# @param FromNow		 optional time delay from now in ms
	#/
	def SendIsoAddressClaim(
						Destination: int = 0xff,
					DeviceIndex: int = 0,
				FromNow: int = 0):
		pass

	# endregion PGN_060928 #ISO-adressekrav


	# 061184 Enkelt, ejendomsbeskyttet
	#**********************************************************************/#
	# @brief Check if the given PGN is proprietary
	#
	# PGNs that are proprietary by definition: 61184, 65280 - 65535, 126720,
	# 130816 - 131071
	#
	# @param PGN PGN to be checked
	# @return true -> for PGNs:
	#	- 126720L
	#	- 130816L
	#	- 131071L
	#	- 65280L ... 65535L
	# @return false
	# @see IsProprietaryMessage
	#
	@staticmethod
	def IsProprietaryMessage(PGN): #
		return





	# 065240 ISO kommandoadresse
	#*******************************************************************/#
	# @brief Starting the ISO Address Claim for a device
	#
	# @param iDev		  index of the device on @ref Devices
	#/
	def StartAddressClaim( iDev: int ):
		pass


	#*******************************************************************/#
	# @brief Starting the ISO Address Claim for all devices
	#
	#/
	def StartAddressClaim():
		pass


	#*******************************************************************/#
	# @brief Checks if the IsoAddressClaim is already started
	#
	# @param iDev		  index of the device on @ref Devices
	# @return true
	# @return false
	#/
	def IsAddressClaimStarted( iDev: int ): pass


	#********************************************************************/#
	# @brief Handles an IsoAddressClaim
	#
	# @param N2kMsg		Reference to a N2kMsg Object
	#/
	def HandleISOAddressClaim( N2kMsg: tN2kMsg ): pass


	#********************************************************************/#
	# @brief Handles if we get commanded to set a new address
	#
	# @param CommandedName   Device name that have been commanded to set
	#						new address
	# @param NewAddress	  new address for the device
	# @param iDev		  index of the device on @ref Devices
	#/
	def HandleCommandedAddress( CommandedName: str, NewAddress: int, iDev: int ): pass


	#********************************************************************/#
	# @brief Handles if we get commanded to set a new address
	#
	# @param N2kMsg		Reference to a N2kMsg Object
	#/
	def HandleCommandedAddress( N2kMsg: tN2kMsg ): pass


	#********************************************************************/#
	# @brief Get the next free address for the device
	#
	# @param DeviceIndex	 index of the device on @ref Devices
	# @param RestartAtEnd	Restart the search from the beginning if the
	#						search for the free source has reached
	#						@ref N2kNullCanBusAddress
	#/
	def GetNextAddress( DeviceIndex: int, RestartAtEnd = false ): pass


	#********************************************************************/#
	# @brief Checks if the source belongs to a device on @ref Devices
	#
	# @param Source Source address
	# @return true
	# @return false
	#/
	def IsMySource( Source: int): pass


	#********************************************************************/#
	# @brief Finds a device on @ref Devices by its source address
	#
	# @param Source Source address of the device
	# @return int DeviceIndex, not found = -1
	#/
	def FindSourceDeviceIndex( Source ): pass


	#********************************************************************/#
	# @brief Get the Sequence Counter for the PGN
	#
	# @param PGN	 PGN
	# @param iDev	index of the device on @ref Devices
	# @return int	Sequence Counter, non valid iDEV = 0
	#/
	def GetSequenceCounter( PGN, iDev: int ): pass


	# 126208 NMEA anmod om gruppefunktion
	#*******************************************************************/#
	# @brief Respond to an Group Function
	#
	#
	# Document https:#www.nmea.org/Assets/20140109%20nmea-2000-corrigendum-tc201401031%20pgn%20126208.pdf
	# defines that systems should respond to NMEA Request/Command/Acknowledge
	# group function PGN 126208. Here we first call callback and if that will
	# not handle function, we use default handler.
	#
	# @param N2kMsg		Reference to a N2kMsg Object
	# @param GroupFunctionCode
	# @param PGNForGroupFunction
	# @param iDev		  index of the device on @ref Devices
	#/
	def RespondGroupFunction(N2kMsg: tN2kMsg, GroupFunctionCode: tN2kGroupFunctionCode, PGNForGroupFunction: int, iDev: int): pass


	#*******************************************************************/#
	# @brief Handles a Group Function
	#
	# Document https:#www.nmea.org/Assets/20140109%20nmea-2000-corrigendum-tc201401031%20pgn%20126208.pdf
	# defines that systems should respond to NMEA Request/Command/Acknowledge
	# group function PGN 126208. On the document it is not clear can request
	# be send as broadcast, so we handle it, if we can.
	#
	# @param N2kMsg		Reference to a N2kMsg Object
	#/
	def HandleGroupFunction( N2kMsg: tN2kMsg): pass


	#*******************************************************************/#
	# @brief   Send ISO Transport Protocol message BAM
	#
	# This is used for Broadcast messages
	#
	# @param iDev	index of the device on @ref Devices
	#
	# @return true
	# @return false
	#/
	def SendTPCM_BAM( iDev: int): pass


	# 126720 Hurtig pakke, ejendomsbeskyttet
	#*******************************************************************/#
	# @brief Get the Fast Packet Tx PGN Count
	#
	# @param iDev	index of the device on @ref Devices
	# @return size_t
	#/
	def GetFastPacketTxPGNCount( iDev: int ): pass


	#*******************************************************************/#
	# @brief ISO Transport Protocol handlers for multi packet support
	#
	# @param PGN		   PGN
	# @param Source		Source address
	# @param Destination   Destination address
	# @param len		   len of the data payload
	# @param buf		   pointer to a byte buffer for the
	# @param MsgIndex	  MsgIndex for @ref N2kCANMsgBuf
	#
	# @return true
	# @return false
	#/
	def TestHandleTPMessage(
					PGN: int,
					Source,
					Destination,
					len,
				buf: str,
					MsgIndex: int
			): return False


	#*******************************************************************/#
	# @brief Check if this PNG is a fast packet message
	#
	# Determines if this given PGN belongs to a fast packet message by
	# checking if a corresponding message is listed on @ref
	# FastPacketMessages[]
	#
	# @param N2kMsg Reference to a N2kMsg Object
	# @return true
	# @return false
	#/
	def IsFastPacket( N2kMsg ): return False


	#*******************************************************************/#
	# @brief Check if this PNG is a fast packet message
	#
	# Determines if this given PGN belongs to a fast packet message by
	# checking if a corresponding message is listed on @ref
	# FastPacketMessages[]
	#
	# @param PGN	 PGN to be checked
	# @return true
	# @return false
	#/
	def IsFastPacketPGN( PGN ): return False


	#*******************************************************************/#
	# @brief Respond to an ISO request
	#
	# If there is now IsoAdressClaim procedure started for this device, we
	# respond for the requested PGN with sending IsoAddressClaim, Tx/Rx PGN
	# lists, Product- / Config informations or an user defined ISORqstHandler.
	#
	# If non of this fits the RequestedPGN, we directly respond to the
	# requester NAK. ( @ref SetN2kPGNISOAcknowledgement)
	#
	# @param N2kMsg		Reference to a N2kMsg Object
	# @param RequestedPGN  Requested PGN
	# @param iDev		  index of the device on @ref Devices
	#/
	def RespondISORequest( N2kMsg,  RequestedPGN, iDev: int): pass


	#*******************************************************************/#
	# @brief Handles an Iso Request
	#
	# The function determines if the request is for us (Broadcast message or
	# device in our list) and responds to the request.
	#
	# @param N2kMsg		Reference to a N2kMsg Object
	#/
	def HandleISORequest( N2kMsg): pass


	# 129026 COG og SOG, hurtig opdatering


	# 129029 GNSS-positionsdata


	# 129044 Referencepunkt

	# endregion Modtag_NMEA2000_PGN_Oplysninger #Tabel 2. Modtag


	# region AIS_Commands
	# region AIS_ClassA_Static_and_Voyage_Related_Data
	# 129038 AIS Klasse A - positionsrapport
	# endregion AIS_ClassA_Static_and_Voyage_Related_Data


	# region AIS_ClassB_Static_and_Voyage_Related_Data
	# 129039 AIS Klasse B - positionsrapport
	# endregion AIS_ClassB_Static_and_Voyage_Related_Data


	# region AIS_Aid_to_Navigation_Report
	# 129040 AIS Klasse B - udvidet positionsrapport
	# endregion AIS_Aid_to_Navigation_Report


	# region AIS_Aid_to_Navigation_Report
	# 129041 AIS navigationshjælpemidler (AtoN) rapport
	# endregion AIS_Aid_to_Navigation_Report


	# region AIS_ClassA_Statistic_and_Voyage_Related_Data
	# 129794 AIS Klasse A - statiske og trafikrelaterede data
	# endregion AIS_ClassA_Statistic_and_Voyage_Related_Data


	# region AIS_SAR_Aircraft_Position_Report
	# 129798 AIS SAR flyposition
	# endregion AIS_SAR_Aircraft_Position_Report


	# region PGN_129802 #AIS Safety Related Broadcast Message
	# 129802 AIS sikkerhedsrelateret meddelelse
	#*****************************************************************************
	# AIS Safety Related Broadcast Message
	#*****************************************************************************
	def SetN2kPGN129802(
				N2kMsg: tN2kMsg,
				MessageID: int,
				Repeat: tN2kAISRepeat,
				SourceID: int,
				AISTransceiverInformation: tN2kAISTransceiverInformation,
				SafetyRelatedText: int
			):
		N2kMsg.SetPGN() #129802L
		N2kMsg.Priority=5
		N2kMsg.AddByte( (Repeat & 0x03)<<6 | (MessageID & 0x3f) )
		N2kMsg.Add4ByteUInt( 0xc0000000 | (SourceID & 0x3fffffff) )
		N2kMsg.AddByte( 0xe0 | (0x1f & AISTransceiverInformation) )
		N2kMsg.AddVarStr( SafetyRelatedText )


	def ParseN2kPGN129802(
					N2kMsg: tN2kMsg,
					MessageID,
					Repeat,
					SourceID,
					AISTransceiverInformation: tN2kAISTransceiverInformation,
					SafetyRelatedText,
					SafetyRelatedTextMaxSize
				):
		if ( N2kMsg.PGN != 129802 ):
			return False

		Index: int = 0
		vb: int = 0

		vb = N2kMsg.GetByte( Index )
		MessageID=( vb & 0x3f )
		Repeat= (tN2kAISRepeat)(vb>>6 & 0x03)
		SourceID = N2kMsg.Get4ByteUInt(Index) & 0x3fffffff
		AISTransceiverInformation = (tN2kAISTransceiverInformation)(N2kMsg.GetByte(Index) & 0x1f)
		N2kMsg.GetVarStr(SafetyRelatedTextMaxSize, SafetyRelatedText, Index)

		return True

	# endregion PGN_129802


	# region PGN_129809 #AIS Class B Static Data Part A
	# 129809 AIS Klasse B "CS" – statiske data, del
	# endregion PGN_129809


	# region PGN_129810 #AIS Class B Static Data Part B
	# 129810 AIS Klasse B "CS" – statiske data, del B
	# endregion PGN_129810


	#*******************************************************************/#
	# @brief Send a list with all supported Transmit messages
	#
	# This function sends a PGN 126464 message consisting of all messages
	# supported by this device for transmission.
	#
	# @param Destination   Destination address
	# @param DeviceIndex   index of the device on @ref Devices
	# @param UseTP		 use multi packet message, default = false
	#/
	def SendTxPGNList(Destination: str, DeviceIndex: int, UseTP: bool = False ):
		pass


	#*******************************************************************/#
	# @brief Checks if the device is ready to send a message
	#
	# @return true
	# @return false
	#/
	def IsReadyToSend():
		return ( (OpenState==os_Open or dbMode!=dm_None) and
						(N2kMode!=N2km_ListenOnly) and
						(N2kMode!=N2km_SendOnly) and
						(N2kMode!=N2km_ListenAndSend)
				)


	#*******************************************************************/#
	# @brief Handles a received system message
	#
	# If the node is not @ref N2km_SendOnly or @ref N2km_ListenAndSend this
	# function chooses the correct handler for the given system message.
	#
	# @sa  @ref HandleISORequest,  @ref HandleISOAddressClaim,
	#	  @ref HandleCommandedAddress, @ref HandleCommandedAddress
	#
	# @param MsgIndex  Message Index on @ref N2kCANMsgBuf
	# @return true	 -> message was handled
	# @return false
	#/
	def HandleReceivedSystemMessage( MsgIndex: int):
		return False


	#*******************************************************************/#
	# @brief Check if this Message is known to the system
	#
	# Determines wether this message is known to the system, either by beeing
	# a default, mandatory or system message or this specific message which is
	# listed in @ref SingleFrameMessages @@ @ref FastPacketMessages.
	#
	# @sa @ref IsDefaultSingleFrameMessage, @ref IsMandatoryFastPacketMessage,
	#	  @ref IsDefaultFastPacketMessage, @ref IsSingleFrameSystemMessage,
	#	  @ref IsFastPacketSystemMessage,
	#
	# @param PGN			 PGN to be checked
	# @param SystemMessage   Flag system message
	# @param FastPacket	  Flag fast packet
	# @return true
	# @return false
	#/
	def CheckKnownMessage(PGN: int, SystemMessage: bool, FastPacket: bool ):
		return False


	#*****************************************************************/#
	# @brief Return the PGN that is handled by this message handler
	# @return
	#/
	def GetPGN():
		return PGN


	#****************************************************************//*
	# @brief Construct a new Message Handler object
	#
	# Attaches this message handler to a tNMEA2000 object.
	#
	# @param _PGN		PGN of the message that should be handled
	# @param _pNMEA2000  Pointer to tNMEA2000 object, where the handle
	#					should be attached
	#/
	def tMsgHandler( _PGN: int = 0, _pNMEA2000: tNMEA2000 = 0 ):
		PGN=_PGN
		pNext=0
		pNMEA2000=0

		if ( _pNMEA2000 != 0 ):
			#_pNMEA2000->AttachMsgHandler(this)
			pass

	# endregion AIS_Commands
