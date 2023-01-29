'''
NMEA2000_Device_Properties.py
Interaction logic for NMEA2000_Device_Properties.xaml
'''

class NMEA2000_Device_Properties(Window):
    class DeviceProperties():
    __init__(self, device):
        self.device = device
        self.device_name = device.name
        self.device_type = device.type
        self.device_port = device.port
        self.device_baudrate = device.baudrate
        self.device_parity = device.parity
        self.device_stopbits = device.stopbits
        self.device_bytesize = device.bytesize
        self.device_timeout = device.timeout
        self.device_xonxoff = device.xonxoff
        self.device_rtscts = device.rtscts
        self.device_dsrdtr = device.dsrdtr
        self.device_write_timeout = device.write_timeout
        self.device_inter_byte_timeout = device.inter_byte_timeout
        
    def get_device_name(self):
    
    def __init__(self) -> None:
        super().__init__()
        object.__init__(self)
        self.InitializeComponent()
        
        sender@app.route("route")
        self.sender = sender
        self.e = e


    def TextBox_TextChanged(object sender, TextChangedEventArgs e):
        pass


    def Button_Click(object sender, RoutedEventArgs e):
        pass


    def TextBox_ProductCode(object sender, TextChangedEventArgs e):
        pass


    def TextBox_DatabaseVersion(object sender, TextChangedEventArgs e):
        pass


    def TextBox_ModelVersion(object sender, TextChangedEventArgs e):
        pass


    def TextBox_ModelID(object sender, TextChangedEventArgs e):
        pass


    def TextBox_SoftwareVersion(object sender, TextChangedEventArgs e):
        pass


    def TextBox_EquipmentSerial(object sender, TextChangedEventArgs e):
        pass    


    def TextBox_EquipmentCertification(object sender, TextChangedEventArgs e):
        pass


    def TextBox_EquipmentLEN(object sender, TextChangedEventArgs e):
        pass


    def TextBox_CAN1(object sender, TextChangedEventArgs e):
        pass


    def TextBox_CAN1Indicator(object sender, TextChangedEventArgs e):
        pass


    def TextBox_CAN2(object sender, TextChangedEventArgs e):
        pass


    def Button_RefreshAll(object sender, RoutedEventArgs e):
        pass


    def Button_UpdateConfigInfo(object sender, RoutedEventArgs e):
        pass


    def TextBox_TextChanged_1(object sender, TextChangedEventArgs e):
        pass



    def TextBox_CAN1Indicator(object sender, TextChangedEventArgs e):
        #throw new NotImplementedException()
        pass


    def TextBox_CAN2Indicator(object sender, TextChangedEventArgs e):
        #throw new NotImplementedException()
        pass
        
        
    def Button_AddressClaimUpdate(object sender, RoutedEventArgs e):
        pass


    def TextBox_InstallationDescription1(object sender, TextChangedEventArgs e):
        #throw new NotImplementedException()
        pass


    def TextBox_InstallationDescription2(object sender, TextChangedEventArgs e):
        #throw new NotImplementedException()
        pass


    def TextBox_ManufacturerInfo(object sender, TextChangedEventArgs e):
        #throw new NotImplementedException()
        pass


    def TextBox_EquipmentIdicator(object sender, TextChangedEventArgs e):
        #throw new NotImplementedException()
        pass


    def TextBox_EquipmentUpdate(object sender, TextChangedEventArgs e):
        #throw new NotImplementedException()
        pass


    def TextBox_CAN2Idicator(object sender, TextChangedEventArgs e):
        #throw new NotImplementedException()
        pass

    def Button_Click_1(object sender, RoutedEventArgs e):
        pass


 	#**********************************************************************/#
	# @class tDevice
	# @brief This class represents a N2k device
	#
	#/
	class tDevice:
		#protected:
		# @brief This object holds all necessary device informations*/
		tDeviceInformation DevI
		# @brief Timestamp when this device was created*/
		unsigned long CreateTime;
		# @brief Source address on bus for this device*/
		uint8_t Source;
			
		public:
			#*****************************************************************/#
			# @brief Construct a new Device object
			#
			# Initialize all the attributes of the device.
			#
			# @param _Name   Name of the device
			# @param _Source Source address on the bus (default = 255)
			#/
			tDevice(uint64_t _Name, uint8_t _Source=255) { Source=_Source; DevI.SetName(_Name); CreateTime=N2kMillis(); }
			#*****************************************************************/#
			# @brief Destroy the Device object#/
			virtual ~tDevice() {;}

			# @brief Returns the Source Address of this device*/
			uint8_t GetSource() const { return Source; }
			# @brief Returns the Time of Creation of this device*/
			unsigned long GetCreateTime() const { return CreateTime; }

			#****************************************************************/#
			# @brief Get the Name of this device
			# @return uint64_t
			#/
			inline uint64_t GetName() const { return DevI.GetName(); }
			#****************************************************************/#
		 # @brief Check if two devices are the same, by comparing the device name
		 # @param Other Name of th other device
		 # @return true
		 # @return false
		 #/
			inline bool IsSame(uint64_t Other) { return DevI.IsSame(Other); }
			#*****************************************************************/#
			# @brief Get the unique Number from the Device Information
			# @return uint32_t
			#/
			inline uint32_t GetUniqueNumber() const { return DevI.GetUniqueNumber(); }
			#*****************************************************************/#
		 # @brief Get the Manufacturer Code from the Device Information
		 # @return uint16_t
		 #/
			inline uint16_t GetManufacturerCode() const { return DevI.
			GetManufacturerCode(); }
			#*****************************************************************/#
			# @brief Get the Device Instance from the Device Information
			# @return unsigned char
			#/
			inline unsigned char GetDeviceInstance() const { return DevI.GetDeviceInstance(); }
			#*****************************************************************/#
			# @brief Get the Device Instance (lower bits) from the Device Information
			# @return unsigned char
			#/
			inline unsigned char GetDeviceInstanceLower() const { return DevI.GetDeviceInstanceLower(); }
			#*****************************************************************/#
			# @brief Get the Device Instance (upper bits) from the Device Information
			# @return unsigned char
			#/
			inline unsigned char GetDeviceInstanceUpper() const { return DevI.GetDeviceInstanceUpper(); }
			#*****************************************************************/#
			# @brief Get the Device Function from the Device Information
			# @return  unsigned char ->  Device function code, @ref
			# tDeviceInformation::tUnionDeviceInformation::DeviceFunction
			#/
			inline unsigned char GetDeviceFunction() const { return DevI.GetDeviceFunction(); }
			#*****************************************************************/#
			# @brief Get the Device Class from the Device Information
			# @return  unsigned char ->  Device class code, @ref
			# tDeviceInformation::tUnionDeviceInformation::DeviceClass
			#/
			inline unsigned char GetDeviceClass() const { return DevI.GetDeviceClass(); }
			#******************************************************************/#
			# @brief Get the Industry Group from the Device Information
			# @return unsigned char
			#/
			inline unsigned char GetIndustryGroup() const { return DevI.GetIndustryGroup(); }
			#******************************************************************/#
			# @brief Get the System Instance from the Device Information
			# @return unsigned char
			#/
			inline unsigned char GetSystemInstance() const { return DevI.GetSystemInstance(); }

			# Product information
			# @brief Get N2k Standard version  from the product information
			# of this device*/
			virtual unsigned short GetN2kVersion() const=0;
			# @brief Get the product code from the product information of
			# this device*/
			virtual unsigned short GetProductCode() const=0;
			# @brief Get the model ID  from the product information of this device*/
			virtual const char# GetModelID() const=0;
			# @brief Get the Software version code from the product
			# information of this device*/
			virtual const char# GetSwCode() const=0;
			# @brief Get the model version from the product information
			# of this device*/
			virtual const char# GetModelVersion() const=0;
			# @brief Get the model serial code from the product information
			# of this device*/
			virtual const char# GetModelSerialCode() const=0;
			# @brief Get the certification level from the product information
			# of this device*/
			virtual unsigned short GetCertificationLevel() const=0;
			# @brief Get the load equivalency from the product information
			# of this device*/
			virtual unsigned short GetLoadEquivalency() const=0;

			# Configuration information
			# @brief Get the installation description 1 from the configuration
			# information of this device*/
			virtual const char# GetInstallationDescription1() const { return 0; }
			# @brief Get the installation description 2 from the configuration
			# information of this device*/
			virtual const char# GetInstallationDescription2() const { return 0; }

			# @brief Get the list of transmitted PGNs from this device*/
			virtual const unsigned long# GetTransmitPGNs() const { return 0; }
			# @brief Get the list of received PGNs from this device*/
			virtual const unsigned long# GetReceivePGNs() const { return 0; }
	};


#**********************************************************************/#
# @struct  tProductInformation
# @brief   Structure that holds all the product information
#
# It is importend that every device has proper product information
# available. This struct holds all the data and provides several
# helper functions.
@dataclass
class tProductInformation():
	# @brief Version of NMEA2000 Standard that is supported
	N2kVersion = "" #unsigned short
	
	# @brief Product Code of the device
	ProductCode = "" #unsigned short
	
	# @brief Max length of ModelID
	# Note that we reserve one extra char for null termination
	N2kModelID[Max_N2kModelID_len + 1] #char
	
	# @brief Max length of Software Code
	# Note that we reserve one extra char for null termination
	N2kSwCode[Max_N2kSwCode_len + 1] #char
	
	# @brief Max length of Model Version
	# Note that we reserve one extra char for null termination
	N2kModelVersion[Max_N2kModelVersion_len + 1] #char
	
	# @brief Max length of Serial Code
	# Note that we reserve one extra char for null termination
	N2kModelSerialCode[Max_N2kModelSerialCode_len + 1] #char

	# @brief Certification level of the device*/
	CertificationLevel = "" #unsigned char
	
	# @brief Load Equivalency of the device
	# A Load Equivalence Number express the amount of current that
	# is drawn from an NMEA 2000 network. 1 equals to 50mA. If
	# a device draws 151mA of current from the network, then its
	# LEN is 4 (151/50 = 3.02, rounded up to 4).
	LoadEquivalency = "" #unsigned char

	#******************************************************************/#
	# @brief Set all the product infomation data of the structure
	#
	# @param _ModelSerialCode        Manufacturer's Model serial code,
	#                                default="". Max 32 chars.
	# @param _ProductCode            Manufacturer's product code,
	#                                default=666
	# @param _ModelID                Manufacturer's  Model ID,
	#                                default="". Max 33 chars
	# @param _SwCode                 Manufacturer's software version code,
	#                                default="". Max 40 chars
	# @param _ModelVersion           Manufacturer's Model version
	#                                default="". Max 24 chars
	# @param _LoadEquivalency        Load equivalency ( x# 50mA, default=1)
	# @param _N2kVersion             N2k Standard version, default=2101
	# @param _CertificationLevel     Certification level, default=0
	def Set(
		_ModelSerialCode, 
		_ProductCode=0xffff, 
		_ModelID=0, 
		_SwCode=0, 
		_ModelVersion=0, 
		_LoadEquivalency=0xff, 
		_N2kVersion=0xffff, 
		_CertificationLevel=0xff 
		):
		N2kVersion  = _N2kVersion if (_N2kVersion!=0xffff) else 2101
		ProductCode = _ProductCode
		#ClearSetCharBuf(_ModelID, sizeof(N2kModelID),N2kModelID )
		#ClearSetCharBuf(_SwCode, sizeof(N2kSwCode),N2kSwCode )
		#ClearSetCharBuf(_ModelVersion,sizeof(N2kModelVersion),N2kModelVersion )
		#ClearSetCharBuf(_ModelSerialCode, sizeof(N2kModelSerialCode),N2kModelSerialCode )
		CertificationLevel = _CertificationLevel if (_CertificationLevel!=0xff) else 0
		LoadEquivalency = _LoadEquivalency if (_LoadEquivalency!=0xff) else 1
	

	#*****************************************************************//*
	# @brief Clears out all data
	def Clear():
		pass


	#*****************************************************************//*
	# @brief Compares two product information structures
	#
	# @param Other An other product information structure
	# @return true
	# @return false
	def IsSame(const tProductInformation &Other): #bool
		pass	


	#********************************************************************/#
	# @class tDeviceInformation
	# @brief Class that holds all the device informations and several
	#        helper functions to that
	#/
	class tDeviceInformation {
	protected:
		#******************************************************************/#
		# @union   tUnionDeviceInformation
		# @brief   Union that holds the device informations
		#
		#/
		typedef union {
			# @brief Devicename#/
			uint64_t Name;
			#****************************************************************/#
		
			# @brief Structure for device information
			#/
			struct {
				# @brief  32 bit number carrying Unique Number and Manufacturer
				# Code
				#
				# ManufacturerCode 11 bits , UniqueNumber 21 bits
				#/
				uint32_t UnicNumberAndManCode; #
				# @brief  Device instance number#/
				unsigned char DeviceInstance;
				# @brief  Device function code
				#
				# see for Details: [NMEA2000 Device and Function Codes](https:#www.nmea.org/Assets/20120726%20nmea%202000%20class%20&%20function%20codes%20v%202.00.pdf)
				#
			 #/
				unsigned char DeviceFunction;
				# @brief  Device class
				#
				# see for Details: [NMEA2000 Device and Function Codes](https:#www.nmea.org/Assets/20120726%20nmea%202000%20class%20&%20function%20codes%20v%202.00.pdf)
				#
				#/
				unsigned char DeviceClass;
				
				# @brief  Industrie Group and System Instance (each 4bits)
				#
				# I found document:
				# http:#www.novatel.com/assets/Documents/Bulletins/apn050.pdf it
				# says about next fields:
				# The System Instance Field can be utilized to facilitate multiple
				# NMEA 2000 networks on these larger marine platforms. NMEA 2000
				# devices behind a bridge, router, gateway, or as part of some
				# network segment could all indicate this by use and application
				# of the System Instance Field. DeviceInstance and SystemInstance
				# fields can be now changed by function
				# @ref SetDeviceInformationInstances or by NMEA 2000 group
				# function. Group function handling is build in the library.
			 #/
				unsigned char IndustryGroupAndSystemInstance;
			};
		} tUnionDeviceInformation;

		# @brief Union that contains all the Device Information #/
		tUnionDeviceInformation DeviceInformation;

	public:
		#*****************************************************************/#
		# @brief Construct a new empty Device Information object
		#/
		tDeviceInformation() { DeviceInformation.Name=0; }

		#*****************************************************************/#
		# @brief Set a unique Number to the Device Information
		# @param _UniqueNumber   a unique number for the device (max 21.bits)
		#/
		void SetUniqueNumber(uint32_t _UniqueNumber) { DeviceInformation.UnicNumberAndManCode=(DeviceInformation.UnicNumberAndManCode&0xffe00000) | (_UniqueNumber&0x1fffff); }

		#*****************************************************************/#
		# @brief Get the unique Number from the Device Information
		# @return uint32_t
		#/
		uint32_t GetUniqueNumber() const { return DeviceInformation.UnicNumberAndManCode&0x1fffff; }
		
		#*****************************************************************/#
		# @brief Set the Manufacturer Code to the Device Information
		# @param _ManufacturerCode Manufacturer Code (max 11bits)
		#/
		void SetManufacturerCode(uint16_t _ManufacturerCode) { DeviceInformation.UnicNumberAndManCode=(DeviceInformation.UnicNumberAndManCode&0x1fffff) | (((unsigned long)(_ManufacturerCode&0x7ff))<<21); }

		#*****************************************************************/#
		# @brief Get the Manufacturer Code from the Device Information
		# @return uint16_t
		#/
		uint16_t GetManufacturerCode() const { return DeviceInformation.UnicNumberAndManCode>>21; }

		#*****************************************************************/#
		# @brief Set the Device Instance to the Device Information
		# @param _DeviceInstance   Instance for the device
		#/
		void SetDeviceInstance(unsigned char _DeviceInstance) { DeviceInformation.DeviceInstance=_DeviceInstance; }

		#*****************************************************************/#
		# @brief Get the Device Instance from the Device Information
		# @return unsigned char
		#/
		unsigned char GetDeviceInstance() const { return DeviceInformation.DeviceInstance; }

		#*****************************************************************/#
		# @brief Get the Device Instance (lower bits) from the Device Information
		# @return unsigned char
		#/
		unsigned char GetDeviceInstanceLower() const { return DeviceInformation.DeviceInstance & 0x07; }
		#*****************************************************************/#
		# @brief Get the Device Instance (upper bits) from the Device Information
		# @return unsigned char
		#/
		unsigned char GetDeviceInstanceUpper() const { return (DeviceInformation.DeviceInstance>>3) & 0x1f; }

		#*****************************************************************/#
		# @brief Set the Device Function to the Device Information
		# @param _DeviceFunction   Device function code, @ref
		# tDeviceInformation::tUnionDeviceInformation::DeviceFunction
		#/
		void SetDeviceFunction(unsigned char _DeviceFunction) { DeviceInformation.DeviceFunction=_DeviceFunction; }

		#*****************************************************************/#
		# @brief Get the Device Function from the Device Information
		# @return  unsigned char ->  Device function code, @ref
		# tDeviceInformation::tUnionDeviceInformation::DeviceFunction
		#/
		unsigned char GetDeviceFunction() const { return DeviceInformation.DeviceFunction; }
		
		#*****************************************************************/#
		# @brief Set the Device Class to the Device Information
		# @param _DeviceClass   Device class code, @ref
		# tDeviceInformation::tUnionDeviceInformation::DeviceClass
		#/
		void SetDeviceClass(unsigned char _DeviceClass) { DeviceInformation.DeviceClass=((_DeviceClass&0x7f)<<1); }
				
		#*****************************************************************/#
		# @brief Get the Device Class from the Device Information
		# @return  unsigned char ->  Device class code, @ref
		# tDeviceInformation::tUnionDeviceInformation::DeviceClass
		#/
		unsigned char GetDeviceClass() const { return DeviceInformation.DeviceClass>>1; }

		#******************************************************************/#
		# @brief Set the Industry Group to the Device Information
		# @param _IndustryGroup    Industry Group
		#/
		void SetIndustryGroup(unsigned char _IndustryGroup) { DeviceInformation.IndustryGroupAndSystemInstance=(DeviceInformation.IndustryGroupAndSystemInstance&0x0f) | (_IndustryGroup<<4) | 0x80; }
		
		#******************************************************************/#
		# @brief Get the Industry Group from the Device Information
		# @return unsigned char
		#/
		unsigned char GetIndustryGroup() const { return (DeviceInformation.IndustryGroupAndSystemInstance>>4) & 0x07; }

		#******************************************************************/#
		# @brief Set the System Instance to the Device Information
		# @param _SystemInstance    System Instance
		#/
		void SetSystemInstance(unsigned char _SystemInstance) { DeviceInformation.IndustryGroupAndSystemInstance=(DeviceInformation.IndustryGroupAndSystemInstance&0xf0) | (_SystemInstance&0x0f); }
		
		#******************************************************************/#
		# @brief Get the System Instance from the Device Information
		# @return unsigned char
		#/
		unsigned char GetSystemInstance() const { return DeviceInformation.IndustryGroupAndSystemInstance&0x0f; }
		#*#***************************************************************/#
		# @brief Get the Name from the Device Information
		# @return uint64_t
		#/
		uint64_t GetName() const { return DeviceInformation.Name; }
		#******************************************************************/#
		# @brief Set the Name to the Device Information
		# @param _Name  Nmae of the device
		#/
		void SetName(uint64_t _Name) { DeviceInformation.Name=_Name; }
		#******************************************************************/#
		# @brief Check if two devices are the same, by comparing the device name
		# @param Other Name of th other device
		# @return true
		# @return false
		#/
		inline bool IsSame(uint64_t Other) { return GetName()==Other; }




	

		#*******************************************************************/#
		# @brief Get the Device Information
		#
		# With this function you can read current device information. Normally
		# device information contains what you have set during initializing
		# with @ref SetDeviceInformation and @ref SetDeviceInformationInstances
		# functions.
		#
		# @note Device information instances can be changed by the NMEA 2000
		# group function by e.g. using system configuration device. So you
		# should time to time check if they have changed and save changed
		# data to e.g. EEPROM for use on startup.
		#
		# See @ref tNMEA2000::ReadResetDeviceInformationChanged
		#
		# @param iDev    index of the device on @ref Devices
		#
		# @return const tDeviceInformation
		#/
		const tDeviceInformation GetDeviceInformation(int iDev=0) { if (iDev<0 || iDev>=DeviceCount) return tDeviceInformation(); return Devices[iDev].DeviceInformation; }


		#*******************************************************************/#
		# @brief Send a Config Information message
		#
		# This is automatically used by class. You only need to use this, if
		# you want to write your own behavior for providing config information.
		#
		# @param Destination   Destination address
		# @param DeviceIndex   index of the device on @ref Devices
		# @param UseTP         use multi packet message
		# @return true         -> Success
		# @return false
		#/
		bool SendConfigurationInformation(unsigned char Destination, int DeviceIndex, bool UseTP);


		#********************************************************************/#
		# @brief Get the Product Information of the device
		#
		# @param iDev        index of the device on @ref Devices
		# @param IsProgMem   Program memory has been used for the data
		# @return const tNMEA2000::tProductInformation*
		#/
		const tNMEA2000::tProductInformation# GetProductInformation(int iDev, bool &IsProgMem) const;

		#********************************************************************/#
		# @brief Get the N2k standard version of the device
		#
		# @param iDev      index of the device on @ref Devices
		# @return unsigned short
		#/
		unsigned short GetN2kVersion(int iDev=0) const;

		#********************************************************************/#
		# @brief Get the Product Code of the device
		#
		# @param iDev      index of the device on @ref Devices
		# @return unsigned short
		#/
		unsigned short GetProductCode(int iDev=0) const;

		#********************************************************************/#
		# @brief Get the ModelID of the device
		#
		# @param buf       Buffer to hold the information
		# @param max_len   Maximum size of the buffer
		# @param iDev      index of the device on @ref Devices
		#/
		void GetModelID(char#buf, size_t max_len, int iDev=0) const;

		#********************************************************************/#
		# @brief Get the Sw Code of the device
		#
		# @param buf       Buffer to hold the information
		# @param max_len   Maximum size of the buffer
		# @param iDev      index of the device on @ref Devices
		#/
		void GetSwCode(char#buf, size_t max_len, int iDev=0) const;

		#********************************************************************/#
		# @brief Get the Model Version of the device
		#
		# @param buf       Buffer to hold the information
		# @param max_len   Maximum size of the buffer
		# @param iDev      index of the device on @ref Devices
		#/
		void GetModelVersion(char#buf, size_t max_len, int iDev=0) const;

		#********************************************************************/#
		# @brief Get the Model Serial of the device
		#
		# @param buf       Buffer to hold the information
		# @param max_len   Maximum size of the buffer
		# @param iDev      index of the device on @ref Devices
		#/
		void GetModelSerialCode(char#buf, size_t max_len, int iDev=0) const;

		#********************************************************************/#
		# @brief Get the Certification Level of the device
		#
		# @param iDev      index of the device on @ref Devices
		# @return unsigned char
		#/
		unsigned char GetCertificationLevel(int iDev=0) const;

		#*******************************************************************/#
		# @brief Get the Load Equivalency of this device
		#
		# A Load Equivalence Number express the amount of current that
		# is drawn from an NMEA 2000 network. 1 equals to 50mA. If
		# a device draws 151mA of current from the network, then its
		# LEN is 4
		#
		# @param iDev      index of the device on @ref Devices
		# @return unsigned char
		#/
		unsigned char GetLoadEquivalency(int iDev=0) const;
		
		#*******************************************************************/#
		# @brief Set the Installation Description 1 of this device
		#
		# This is automatically used by class. You only need to use this, if you
		# want to write your own behavior.
		#
		# @param InstallationDescription1 Description
		#/
		void SetInstallationDescription1(const char#InstallationDescription1);
		
		#*******************************************************************/#
		# @brief Set the Installation Description 2 of this device
		#
		# This is automatically used by class. You only need to use this, if you
		# want to write your own behavior.
		#
		# @param InstallationDescription2 Description
		#/
		void SetInstallationDescription2(const char#InstallationDescription2);
		
		#*******************************************************************/#
		# @brief Get the Install Description 1 of this device
		#
		# @param buf       Buffer in memory for the description
		# @param max_len   Max size of the buffer
		#
		#/
		void GetInstallationDescription1(char#buf, size_t max_len);
		
		#*******************************************************************/#
		# @brief Get the Install Description 2 of this device
		#
		# @param buf       Buffer in memory for the description
		# @param max_len   Max size of the buffer
		#
		#/
		void GetInstallationDescription2(char#buf, size_t max_len);
		
		#*******************************************************************/#
		# @brief Get the Manufacturer Information of this device
		#
		# @param buf       Buffer in memory for the description
		# @param max_len   Max size of the buffer
		#
		#/
		void GetManufacturerInformation(char#buf, size_t max_len);
		
