#**********************************************************************/#
# @enum    tN2kMode
# @brief   System mode. Meaning how the device will behave on the
#          NMEA2000 bus
#/
typedef enum {
    # Default mode. Listen bus and forwards messages to default
    # port in Actisense format. You can not send any data to the bus.
    #/
    N2km_ListenOnly,
    # This is for devices, which only sends data to the bus e.g.
    # RPM or temperature monitor. Remember to set right device
    # information first.
    #/
    N2km_NodeOnly,
    # In this mode, device can be e.g. temperature monitor and
    # as N2km_ListenOnly.
    #/
    N2km_ListenAndNode,
    #  Only for message sending. Device will not inform itself
    # to the bus. Messages will not be forwarded to the stream.
    # By setting message handler, you can still read messages
    # and handle them by yourself.
    #/
    N2km_SendOnly,
    # Listen bus and forwards messages to default port in
    # Actisense format. Messages can be send. Device will not
    # inform itself to the bus.
    #/
    N2km_ListenAndSend
    
} tN2kMode;


#if !defined(N2K_NO_ISO_MULTI_PACKET_SUPPORT)
		#*******************************************************************/#
		# @brief Send a Product Information message
		#
		# This is automatically used by class. You only need to use this, if
		# you want to write your own behavior for providing product information.
		#
		# @param Destination   Destination address
		# @param DeviceIndex   index of the device on @ref Devices
		# @param UseTP         use multi packet message
		# @return true         -> Success
		# @return false
		#/
		bool SendProductInformation(unsigned char Destination, int DeviceIndex, bool UseTP);


		#*******************************************************************/#
		# @brief Set the Device Information
		#
		# If you are using device modes tNMEA2000::N2km_NodeOnly or
		# tNMEA2000::N2km_ListenAndNode, it is critical that you set this
		# information.
		#
		# Device information will be used to choose right address for your
		# device (also called node) on the bus. Each device must have an own
		# address. Library will do this automatically, so it is enough that
		# you call this function on setup to define your device.
		#
		# For keeping defaults use 0xffff/0xff for int/char values and
		# nul ptr for pointers.
		#
		# @note You should set information so that it is unique over the
		# world! Well if you are making device only for your own yacht N2k
		# bus, it is enough to be unique there. So e.g. if you have two
		# temperature monitors made by this library, you have to set at
		# least first parameter UniqueNumber different for both of them.
		#
		# I just decided to use number below for ManufacturerCode as Open
		# Source devices - this is not any number given by NMEA.
		#
		# @param _UniqueNumber     Default=1. 21 bit resolution, max 2097151.
		#                          Each device from same manufacturer should
		#                          have unique number.
		# @param _DeviceFunction   Default=130, PC Gateway. See codes on
		#  http:#www.nmea.org/Assets/20120726%20nmea%202000%20class%20&%20function%20codes%20v%202.00.pdf
		# @param _DeviceClass      Default=25, Inter/Intranetwork Device.
		#                          See codes on
		# http:#www.nmea.org/Assets/20120726%20nmea%202000%20class%20&%20function%20codes%20v%202.00.pdf
		# @param _ManufacturerCode Default=2046. Maximum 2046. See the
		#                          list of codes on
		# http:#www.nmea.org/Assets/20140409%20nmea%202000%20registration%20list.pdf
		# @param _IndustryGroup    Default=4, Marine.
		# @param iDev    index of the device on @ref Devices
		#/
		void SetDeviceInformation(unsigned long _UniqueNumber,
            unsigned char _DeviceFunction=0xff,
            unsigned char _DeviceClass=0xff,
            uint16_t _ManufacturerCode=0xffff,
            unsigned char _IndustryGroup=4,
            int iDev=0
            );

