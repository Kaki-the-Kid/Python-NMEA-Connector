#**********************************************************************/#
# @class tNMEA2000
# @brief NMEA2000 device class definition.
# @ingroup group_core
#
# With NMEA2000 device class you can send, read and forward messages to
# NMEA2000 bus. As default library creates a system, which acts like Actisense
# NGT NMEA2000->PC interface forwarding all messages from bus to PC. By
# hanging mode to N2km_NodeOnly, one can make e.g. temperature source
# device to NMEA2000 bus.
#
# @note Each device on NMEA2000 bus should have own address on range 0-253.
#
# This class uses J1939 automatic address claiming (or dynamic addressing).
# So that you can start your device with some address set by method
# @ref tNMEA2000::SetMode(). It is also important to set your device
# "name" with method @ref tNMEA2000::SetDeviceInformation() so that
# it would be unique.
#
# If you do not set "name" to unique, you devices changes address on start
# randomly. In principle they should still work fine.
# It is also good idea to save device address to the EEPROM. In this way if
# you connect two of your devices to the bus, they will do the automatic
# address claiming. If later save address to the EEPROM and use that on next
# start, they does not need to change address anymore. See also method
# @ref tNMEA2000::ReadResetAddressChanged().


#**********************************************************************/#
# @class tMsgHandler
# @brief Message handler class
#
#/
class tCANSendFrame(tNMEA2000):
	#*******************************************************************/#
	# @struct  tCANSendFrame
	# @brief   Structure holds all the data needed for a valide CAN-Message
	#/
	class tCANSendFrame():
		# @brief  ID of the CAN Message*/
		id: int
		# @brief  Length of carried data of the CAN Message*/
		len: int
		# @brief  Data payload for the CAN Message*/
		buf[8]: str
		# @brief  Has the CAN Message to wait before sending*/
		wait_sent: bool

		# Clears all the fieds of the CAN Message#/
		def Clear():
			id=0
			len=0
      
			for i in range<8:
				buf[i] = 0


	# @brief Buffer for received messages#/
	N2kCANMsgBuf: tN2kCANMsg
 
	# @brief Max number CAN messages that can go to the buffer
	#          @ref N2kCANMsgBuf#/
	MaxN2kCANMsgs: int

	# @brief Buffer for ssend out CAN messages#/
	CANSendFrameBuf: tCANSendFrame

	# @brief Max number of send out CAN messages that can go to the buffer
	#          @ref CANSendFrameBuf
	# @sa @ref InitCANFrameBuffers()*/
	MaxCANSendFrames: int
 
	# @brief  In,dex for the CAN message Send buffer
	# @todo Please double check Docu
	#/
	CANSendFrameBufferWrite: int
 
	# @brief  Index for the CAN message Send buffer
	# @todo Please double check Docu
	#/
	CANSendFrameBufferRead: int
 
	# @brief Max number received CAN messages that can go to the buffer
	# @sa @ref InitCANFrameBuffers()
	#/
	MaxCANReceiveFrames: int

	# @brief ???
	# @todo Better documentation needed#/
	#void (*OnOpen)();
			
	# @brief Handler callbacks for normal messages#/
	#void (*MsgHandler)(const tN2kMsg &N2kMsg);
	
 	# @brief Handler callbacks for 'ISORequest' messages#/
	#bool (*ISORqstHandler)(unsigned long RequestedPGN, unsigned char Requester, int DeviceIndex);


	#*******************************************************************/#
	# @brief Send a CAN Frame
	#
	# This Virtual function will be overridden by a derived class for
	# specific interfaces according to the hardware which is used.
	# Currently there are own classes like NMEA2000_Teensyx, NMEA2000_teensy,
	# NMEA2000_esp32, NMEA2000_due, NMEA2000_mcp, NMEA2000_avr, NMEA2000_mbed
	# and NMEA2000_socketCAN.
	#
	# @sa @ref secHWlib
	#
	# @param id        ID of the CAN frame
	# @param len       length of payload for the message
	# @param buf       buffer with the payload
	# @param wait_sent   Has the message to wait before sending
	#
	# @return true   -> Success
	# @return false  -> there is no space in the queue
	#/
	def CANSendFrame( id: int, len: int, buf: int, wait_sent: bool = True ): return False


	#*******************************************************************/#
	# @brief Open the CAN Interface
	#
	# This Virtual function will be overridden by a derived class for
	# specific interfaces according to the hardware which is used.
	# Currently there are own classes like NMEA2000_Teensyx, NMEA2000_teensy,
	# NMEA2000_esp32, NMEA2000_due, NMEA2000_mcp, NMEA2000_avr, NMEA2000_mbed
	# and NMEA2000_socketCAN.
	#
	# @sa @ref secHWlib
	#
	# @return true   -> Success
	# @return false  -> currently prevent accidental by second instance.
	#                   Maybe possible in future.
	#/
	def CANOpen(): return False


	#*******************************************************************/#
	# @brief Get a CAN Frame
	#
	# This Virtual function will be overridden by a derived class for
	# specific interfaces according to the hardware which is used.
	# Currently there are own classes like NMEA2000_Teensyx, NMEA2000_teensy,
	# NMEA2000_esp32, NMEA2000_due, NMEA2000_mcp, NMEA2000_avr, NMEA2000_mbed
	# and NMEA2000_socketCAN.
	#
	# @sa @ref secHWlib
	#
	# @return true   -> Ther is a new frame
	# @return false  ->
	#/
	def CANGetFrame( id , len, buf): return False

	
	#*******************************************************************/#
	# @brief Initialize CAN Frame buffers
	#
	# This will be called on @ref tNMEA2000::Open() before any other
	# initialization. Inherit this, if buffers can be set for the driver
	# and you want to change size of library send frame buffer size. See e.g.
	# NMEA2000_teensy.cpp.
	#/
	def InitCANFrameBuffers(): pass


	#********************************************************************/#
	# @brief Sends pending all frames
	#
	# @return true   -> Success
	# @return false  -> Message could not be send out
	#/
	def SendFrames(): return False


	#********************************************************************/#
	# @brief Sends a single CAN frame
	#
	# This function sends a CAN Message to the buffer, if we can not sent
	# frame immediately via @ref CANSendFrame()
	#
	# @param id {type}
	# @param len {type}
	# @param buf {type}
	# @param wait_sent {type}
	#
	# @return true   -> success
	# @return false  -> failed
	#/
	def SendFrame( id, len, buf, wait_sent: bool = true ): return False


	#*******************************************************************/#
	# @brief Get the Next Free CAN Frame  from @ref CANSendFrameBuf
	# @return tCANSendFrame*
	#/
	tCANSendFrame#GetNextFreeCANSendFrame();


	#*******************************************************************/#
	# @brief Send ISO AddressClaim, Product Information and Config
	#        Information
	#
	# Currently Product Information and Configuration Information will we
	# pended on ISO request. This is because specially for broadcasted
	# response it may take a while, when higher priority devices sends
	# their response.
	# @sa  @ref SendIsoAddressClaim(), @ref SendProductInformation(),
	#      @ref SendConfigurationInformation()
	#/
	def SendPendingInformation(): pass


	#*******************************************************************/#
	# @brief Determines if the CAN BUS is already initialized
	# @return true
	# @return false
	#/
	def IsInitialized(): return (bool)(N2kCANMsgBuf!=0)


	#*******************************************************************/#
	# @brief Function handles received CAN frame and adds it to tN2kCANMsg
	#
	# This function returns Index to a ready @ref tN2kCANMsg on buffer
	# @ref N2kCANMsgBuf (max @ref MaxN2kCANMsgs),
	# if we skipped the frame or message is not ready (fast packet or
	# ISO Multi-Packet)
	#
	# @param canId     ID of CAN message
	# @param len       length of payload
	# @param buf       buffer for payload of message
	# @return uint8_t  -> Index of the CAN message on @ref N2kCANMsgBuf
	#/
	def SetN2kCANBufMsg( canId, len, buf): pass