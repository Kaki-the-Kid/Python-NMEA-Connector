class tNMEA2000():
	# PGN for an Iso Address Claim message
	N2kPGNIsoAddressClaim = 60928
	
	# PGN for a Production Information message
	N2kPGNProductInformation = 126996

	# PGN for an Configuration Information message
	N2kPGNConfigurationInformation = 126998

	# Document says for lenghts 33,40,24,32, but then values
	# has not been translated right on devices.
	# @brief Max length of ModelID
	#  Document says for leghts 33 but then values has not
	#  been translated right on devices.#/
	Max_N2kModelID_len = 32

	# @brief Max length of Software Code
	#  Document says for leghts 40 but then values has not
	#  been translated right on devices.
	Max_N2kSwCode_len = 32

	# @brief Max length of Model Version
	#  Document says for leghts 24 but then values has not
	#  been translated right on devices.
	Max_N2kModelVersion_len = 32

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





	# NMEA 2000 PGN oplysninger
	# Tabel 1. Send
	# PGN Beskrivelse


	#**********************************************************************/#
	# @brief Setting up PGN 59392 Message "ISO Acknowledgement"
	#
	# This message is provided by ISO 11783 for a handshake mechanism
	# between transmitting and receiving devices. This message
	# is the possible response to acknowledge the reception of a “normal
	# broadcast” message or the response to a specific command to indicate
	# compliance or failure.
	#
	# @param N2kMsg          Reference to a N2kMsg Object, ready to be send
	# @param Control         Control Byte
	# @param GroupFunction   Group Function value
	# @param PGN             PGN of requested Information
	#
	# 059392 ISO-bekræftelse
	def SetN2kPGN59392(
    				tN2kMsg &N2kMsg, 
        			unsigned char Control, 
           			unsigned char GroupFunction, 
              		unsigned long PGN
                ):
		N2kMsg.SetPGN(59392L)
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
     				tN2kMsg &N2kMsg, 
         			unsigned char Control, 
            		unsigned char GroupFunction, 
              		unsigned long PGN
                ):
		SetN2kPGN59392(N2kMsg,Control,GroupFunction,PGN)


	# 060928 ISO-adressekrav
	#**********************************************************************/#
	# @brief Setting up PGN 60928 Message "ISO Address Claim"
	#
	# This network management message is used to claim a network address and
	# to respond with device information (NAME) requested by the ISO Request
	# or Complex Request Group Function. This PGN contains several fields
	# that are Request Parameters that can be used to control the expected
	# response to requests for this PGN.
	#
	# @param N2kMsg            Reference to a N2kMsg Object, ready to be send
	# @param UniqueNumber      Unique Number (ISO Identity Number)
	# @param ManufacturerCode  Manufacturer Code
	# @param DeviceFunction    Device Function (ISO Function)
	# @param DeviceClass       Device Class
	# @param DeviceInstance    Device Instance
	# @param SystemInstance    System Instance (ISO Device Class Instance)
	# @param IndustryGroup     Industry Group
	#/
	def SetN2kPGN60928(
     				tN2kMsg &N2kMsg, 
         			unsigned long UniqueNumber, 
            		int ManufacturerCode,
					unsigned char DeviceFunction, 
     				unsigned char DeviceClass,
					unsigned char DeviceInstance=0, 
     				unsigned char SystemInstance=0, 
         			unsigned char IndustryGroup=4
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
	# @param N2kMsg            Reference to a N2kMsg Object, ready to be send
	# @param Name              Name of the device
	#/
	def SetN2kPGN60928(tN2kMsg &N2kMsg, uint64_t Name):
		return 0


	#**********************************************************************/#
	# @brief Setting up Message "ISO Address Claim" - PGN 60928
	#
	# Alias of PGN 60928. This alias was introduced to improve the readability
	# of the source code. See parameter details on @ref SetN2kPGN60928
	#/
	def SetN2kISOAddressClaim(
     				tN2kMsg &N2kMsg, 
					unsigned long UniqueNumber, 
					int ManufacturerCode,
					unsigned char DeviceFunction, 
     				unsigned char DeviceClass,
					unsigned char DeviceInstance=0, 
     				unsigned char SystemInstance=0, 
         			unsigned char IndustryGroup=4
				):
		SetN2kPGN60928( N2kMsg, UniqueNumber, ManufacturerCode, DeviceFunction, DeviceClass,
									DeviceInstance, SystemInstance, IndustryGroup):
		return 0
	
 
	#**********************************************************************/#
	# @brief Setting up Message "ISO Address Claim" - PGN 60928
	#
	# Alias of PGN 60928. This alias was introduced to improve the readability
	# of the source code. See parameter details on @ref SetN2kPGN60928
	def SetN2kISOAddressClaim(N2kMsg, Name):
		SetN2kPGN60928(N2kMsg, Name)


 
 
# 061184 Enkelt, ejendomsbeskyttet
# 126208 NMEA® anmod om gruppefunktion


	# 126464 PGN's gruppefunktion
	#**********************************************************************/#
	# @brief Setting up PGN 126464 Message "PGN List - Transmit PGNs group
	#        function"
	#
	# The PGN List group function type is defined by the first field. The
	# message will be either a Transmit PGNs or a Receive PGNs group function
	# that identifies the PGNs transmitted from or received by a node.
	#
	# @note List of PGNs must be null terminated and defined as PROGMEM e.g.
	#        const unsigned long TransmitMessages[] PROGMEM={130310L,0};
	#
	# @param N2kMsg          Reference to a N2kMsg Object, ready to be send
	# @param Destination     Address of the destination
	# @param tr              Transmit or Receive, see @ref tN2kPGNList
	# @param PGNs            List of PGNs
	#/
	def SetN2kPGN126464(
					tN2kMsg &N2kMsg, 
					uint8_t Destination, 
					tN2kPGNList tr, 
					const unsigned long#PGNs
				):

	#**********************************************************************/#
	# @brief Setting up Message "PGN List - Transmit PGNs group
	#        function" - PGN 126464
	#
	# Alias of PGN 126464. This alias was introduced to improve the readability
	# of the source code. See parameter details on @ref SetN2kPGN126464
	#/
	def SetN2kPGNTransmitList(
					tN2kMsg &N2kMsg, 
					uint8_t Destination, 
					const unsigned long#PGNs
				):
		SetN2kPGN126464(N2kMsg,Destination,N2kpgnl_transmit,PGNs)



# 126720 Hurtig pakke, ejendomsbeskyttet
# 126992 PGN-liste

	# 126993 Puls
	#**********************************************************************/#
	# @brief Setting up PGN 126993 Message "Heartbeat"
	#
	# This PGN shall be transmitted by all NMEA devices. Reception of this
	# PGN confirms that a device is still present on the network. Reception
	# of this PGN may also be used to maintain an address to NAME association
	# table within the receiving device.
	#
	# @param N2kMsg            Reference to a N2kMsg Object, ready to be send
	# @param timeInterval_ms   time interval in msec (0.01 - 655.32s )
	# @param sequenceCounter   Sequence counter
	#/
	void SetN2kPGN126993(tN2kMsg &N2kMsg, uint32_t timeInterval_ms, uint8_t sequenceCounter);

	#**********************************************************************/#
	# @brief Setting up Message "Heartbeat" - PGN 126993
	#
	# Alias of PGN 126993. This alias was introduced to improve the readability
	# of the source code. See parameter details on @ref SetN2kPGN126993
	#/
	inline void SetHeartbeat(tN2kMsg &N2kMsg, uint32_t timeInterval_ms, uint8_t sequenceCounter) {
		SetN2kPGN126993(N2kMsg, timeInterval_ms, sequenceCounter);
	}
 




	# 126996 Produktoplysninger
	#**********************************************************************/#
	# @brief Setting up PGN 126996 Message "Product information"
	#
	# Provides product information onto the network that could be important
	# for determining quality of data coming from this product.
	#
	# @param N2kMsg              Reference to a N2kMsg Object, ready to be send
	# @param N2kVersion          NMEA Network Message Database Version
	# @param ProductCode         NMEA Manufacturer's Product Code
	# @param ModelID             Manufacturer's Model ID
	# @param SwCode              Manufacturer's Software Version Code
	# @param ModelVersion        Manufacturer's Model Version
	# @param ModelSerialCode     Manufacturer's Model Serial Code
	# @param CertificationLevel  NMEA 2000 Certification Level
	# @param LoadEquivalency     Load Equivalency
	#/
	def SetN2kPGN126996(
     				tN2kMsg &N2kMsg, 
         			unsigned int N2kVersion, 
         			unsigned int ProductCode,
					const char#ModelID, 
					const char#SwCode,
					const char#ModelVersion, 
           			const char#ModelSerialCode,
					unsigned char CertificationLevel=1, 
           			unsigned char LoadEquivalency=1
				):


	#**********************************************************************/#
	# @brief Setting up Message "Product information" - PGN 126996
	#
	# Alias of PGN 126996. This alias was introduced to improve the readability
	# of the source code. See parameter details on @ref SetN2kPGN126996
	#/
	def SetN2kProductInformation(
					tN2kMsg &N2kMsg, 
					unsigned int N2kVersion, 
					unsigned int ProductCode,
					const char#ModelID, const char#SwCode,
					const char#ModelVersion, const char#ModelSerialCode,
					unsigned char CertificationLevel=1, 
					unsigned char LoadEquivalency=1
     			):
		SetN2kPGN126996(N2kMsg,N2kVersion,ProductCode, ModelID,SwCode, ModelVersion,
                  ModelSerialCode, CertificationLevel,LoadEquivalency)
	
 
	#**********************************************************************/#
	# @brief  Parsing the content of message PGN 126996 "Product information"
	#
	# Provides product information onto the network that could be important
	# for determining quality of data coming from this product.
	#
	# @param N2kMsg              Reference to a N2kMsg Object, ready to be send
	# @param N2kVersion          NMEA Network Message Database Version
	# @param ProductCode         NMEA Manufacturer's Product Code
	# @param ModelIDSize         Size of ModelID
	# @param ModelID             Manufacturer's Model ID
	# @param SwCodeSize          Size of Software Version Code
	# @param SwCode              Manufacturer's Software Version Code
	# @param ModelVersionSize    Size of Model Version
	# @param ModelVersion        Manufacturer's Model Version
	# @param ModelSerialCodeSize Size of Model Serial Code
	# @param ModelSerialCode     Manufacturer's Model Serial Code
	# @param CertificationLevel  NMEA 2000 Certification Level
	# @param LoadEquivalency     Load Equivalency
	#
	# @return true     Parsing of PGN Message successful
	# @return false    Parsing of PGN Message aborted
	#/
	def ParseN2kPGN126996(
					const tN2kMsg& N2kMsg, 
     				unsigned short &N2kVersion, 
					unsigned short &ProductCode,
					int ModelIDSize, 
					char#ModelID, int SwCodeSize, char#SwCode,
					int ModelVersionSize, 
					char# ModelVersion, 
					int ModelSerialCodeSize, 
					char#ModelSerialCode,
					unsigned char &CertificationLevel, 
					unsigned char &LoadEquivalency
				):


	# 126998 Konfigurationsoplysninger
	#**********************************************************************/#
	# @brief Setting up PGN 126998 Message "Configuration information"
	#
	# Free-form alphanumeric fields describing the installation (e.g.,
	# starboard engine room location) of the device and installation
	# notes (e.g., calibration data).
	#
	# @param N2kMsg              Reference to a N2kMsg Object, ready to be send
	# @param ManufacturerInformation   Manufacturer Information
	# @param InstallationDescription1  Installation Description, Field 1
	# @param InstallationDescription2  Installation Description, Field 2
	# @param UsePgm              Use program memory, default = false
	def SetN2kPGN126998(
					tN2kMsg &N2kMsg,
					const char#ManufacturerInformation,
					const char#InstallationDescription1=0,
					const char#InstallationDescription2=0,
					bool UsePgm=false
				):


	#**********************************************************************/#
	# @brief Setting up Message "Configuration information" - PGN 126998
	#
	# Alias of PGN 126998. This alias was introduced to improve the readability
	# of the source code. See parameter details on @ref SetN2kPGN126998
	#/
	def SetN2kConfigurationInformation(
					tN2kMsg &N2kMsg,
					const char#ManufacturerInformation,
					const char#InstallationDescription1=0,
					const char#InstallationDescription2=0,
					bool UsePgm=false
           ):
		SetN2kPGN126998(
         	N2kMsg,
			ManufacturerInformation,
			InstallationDescription1,
			InstallationDescription2,
			UsePgm)
	

	#**********************************************************************/#
	# @brief Parsing the content of message PGN 126998
	#    "Configuration information"
	#
	# Free-form alphanumeric fields describing the installation (e.g.,
	# starboard engine room location) of the device and installation
	# notes (e.g., calibration data).
	#
	# @param N2kMsg            Reference to a N2kMsg Object
	# @param ManufacturerInformationSize Size off Manufacturer Information
	# @param ManufacturerInformation     Manufacturer Information
	# @param InstallationDescription1Size Size off Installation Description
	# @param InstallationDescription1    Installation Description, Field 1
	# @param InstallationDescription2Size Size off Installation Description
	# @param InstallationDescription2    Installation Description, Field 2
	#
	# @return true     Parsing of PGN Message successful
	# @return false    Parsing of PGN Message aborted
	#
	#/
	bool ParseN2kPGN126998(const tN2kMsg& N2kMsg,
												size_t &ManufacturerInformationSize, char#ManufacturerInformation,
												size_t &InstallationDescription1Size, char#InstallationDescription1,
												size_t &InstallationDescription2Size, char#InstallationDescription2);








# 129799 Radiofrekvens/-tilstand/-effekt
# 129808 DSC-opkaldsoplysninger



	# Tabel 2. Modtag
	# PGN Beskrivelse

	# 059392 ISO-bekræftelse
 
 
	# 059904 ISO-anmodning 
	#**********************************************************************/#
	# @brief Setting up PGN 59904 Message "ISO request"
	#
	# As defined by ISO, this message has a data length of 3 bytes with no
	# padding added to complete the single frame. The appropriate response
	# to this message is based on the PGN being requested, and whether the
	# receiver supports the requested PGN.
	#
	# @param N2kMsg            Reference to a N2kMsg Object, ready to be send
	# @param Destination       Address of the destination
	# @param RequestedPGN      PGN being requested
	#/
	void SetN2kPGN59904(tN2kMsg &N2kMsg, uint8_t Destination, unsigned long RequestedPGN);

	#**********************************************************************/#
	# @brief Setting up Message "ISO request" - PGN 59904
	#
	# Alias of PGN 59904. This alias was introduced to improve the readability
	# of the source code. See parameter details on @ref SetN2kPGN59904
	#/
	inline void SetN2kPGNISORequest(tN2kMsg &N2kMsg, uint8_t Destination, unsigned long RequestedPGN) {
		SetN2kPGN59904(N2kMsg,Destination,RequestedPGN);
	}

	#**********************************************************************/#
	# @brief Parsing the content of message PGN 59904 "ISO request"
	#
	# As defined by ISO, this message has a data length of 3 bytes with no
	# padding added to complete the single frame. The appropriate response
	# to this message is based on the PGN being requested, and whether the
	# receiver supports the requested PGN.
	#
	# @param N2kMsg        Reference to a N2kMsg Object
	# @param RequestedPGN  PGN being requested
	#
	# @return true     Parsing of PGN Message successful
	# @return false    Parsing of PGN Message aborted
	#/
	bool ParseN2kPGN59904(const tN2kMsg &N2kMsg, unsigned long &RequestedPGN);

	#**********************************************************************/#
	# @brief Parsing the content of a "ISO request"
	#        message - PGN 59904
	#
	# Alias of PGN 59904. This alias was introduced to improve the readability
	# of the source code. See parameter details on @ref ParseN2kPGN59904
	#/
	inline bool ParseN2kPGNISORequest(const tN2kMsg &N2kMsg, unsigned long &RequestedPGN) {
		return ParseN2kPGN59904(N2kMsg, RequestedPGN);
	}


 
 
 
 
 
 
 
 
	# 060160 ISO-transportprotokol, dataoverførsel


	# 060416 ISO-transportprotokol, administration af tilslutning – RTS gruppefunktion


	# 060928 ISO-adressekrav


	#**********************************************************************/#
	# @brief Check if the given PGN is proprietary
	#
	# PGNs that are proprietary by definition: 61184, 65280 - 65535, 126720,
	# 130816 - 131071
	#
	# @param PGN PGN to be checked
	# @return true -> for PGNs:
	#    - 126720L
	#    - 130816L
	#    - 131071L
	#    - 65280L ... 65535L
	# @return false
	# @see IsProprietaryMessage
	#
	# 061184 Enkelt, ejendomsbeskyttet
	@staticmethod
	def IsProprietaryMessage(PGN): #unsigned long
		return





	# 065240 ISO kommandoadresse
 
 
	# 126208 NMEA anmod om gruppefunktion
 
 
	# 126720 Hurtig pakke, ejendomsbeskyttet
 
 
	# 129026 COG og SOG, hurtig opdatering
 
 
	# 129029 GNSS-positionsdata
 
 
	# 129044 Referencepunkt


	# Tabel 3. Transmitter (kun AIS-modeller)
	# PGN Beskrivelse

	# 129038 AIS Klasse A - positionsrapport
 
 
	# 129039 AIS Klasse B - positionsrapport
 
 
	# 129040 AIS Klasse B - udvidet positionsrapport
 
 
	# 129041 AIS navigationshjælpemidler (AtoN) rapport
 
 
	# 129794 AIS Klasse A - statiske og trafikrelaterede data
 
 
	# 129798 AIS SAR flyposition
 
 
	# 129802 AIS sikkerhedsrelateret meddelelse
 
 
	# 129809 AIS Klasse B "CS" – statiske data, del A
 
 
	# 129810 AIS Klasse B "CS" – statiske data, del B

