#*************************************************************************#\**
# @file  ActisenseReader.h
# @brief This File contains a class for reading Actisense format messages
# 
# This is class for reading Actisense format messages from given stream.
# 
# @note There is an unresolved problem to use programming port with reading 
# data. Read works fine for a while, but then stops. With e.g. Arduino Due
# USB port there is no problem.
# 
# include "N2kMsg.h"
# include "N2kStream.h"


class tActisenseReader():
	#*******************************************************************#\**
	# @brief Constructor for the class
	# Initialize all class attributes and clear the buffer
	#
	def __init__(self, 
              StartOfTextReceived, 
              MsgIsComing, 
              EscapeReceived, 
              byteSum, 
              MsgBuf, 
              MsgWritePos, 
              DefaultSource, 
              ReadStream, 
              MsgHandler
              ):
		StartOfTextReceived = False
		MsgIsComing    = False
		EscapeReceived = False
		byteSum        = 0		
		MsgBuf         = [0] * 300
		MsgWritePos    = 0
		DefaultSource  = 65
		ReadStream     = None
		MsgHandler     = None
							

	#*******************************************************************#\**
	# @brief Reads a message from the stream 
	#* @brief Maximum length of the stream message buffer*/
	MAX_STREAM_MSG_BUF_LEN = 300
	#* @brief Buffer for incoming messages from stream*/
	MsgBuf = [MAX_STREAM_MSG_BUF_LEN] #unsigned char 
	#* @brief Start of text has been received*/
	StartOfTextReceived = False
	#* @brief A Message is coming*/
	MsgIsComing = False
	#* @brief Escape character has been received*/
	EscapeReceived = False
	#* @brief Sum of all bytes is used as kind of check sum*/
	byteSum = 0
	#* @brief Current write position inside the buffer#
	MsgWritePos = 0
	#* @brief Default source of the N2k message*/
	DefaultSource = 0 #unsigned char 
	#* @brief Stream to read from*/
	N2kStream* ReadStream
	# Handler callback
	#void (*MsgHandler)(const tN2kMsg &N2kMsg)


	# *******************************************************************#\**
	# @brief Adds a new Byte to the buffer
	#
	# @param NewByte   new Byte to be added
	# @return True	 -> Success
	# @return False	-> Buffer is full
	# *******************************************************************#\**
	def AddByteToBuffer(NewByte): #bool 
		return
 
	#*******************************************************************#\**
	# @brief Clears the buffer
	#*******************************************************************#\**
	def ClearBuffer(): #void
		return
	
	#*******************************************************************#\**
	# @brief Checks if a message is valide
	#
	# @param N2kMsg	Reference to a N2kMsg Object
	#
	# @return True	 
	# @return False	-> Length does not match. Add type, length and crc
	# @return False	-> Checksum does not match
	# @return False	-> data length greater then tN2kMsg::MaxDataLen
	#*******************************************************************#\**
	def CheckMessage(tN2kMsg &N2kMsg):
		pass


	#********************************************************************#\**
	# @brief Set the Read Stream object
	# 
	# Set stream, which would be used for reading messages. You have to
	# open stream first, so e.g. for SerialUSB call begin first.
	# 
	# @param _stream   Stream to read from
	# ********************************************************************#\**
	def SetReadStream(N2kStream* _stream): #void 
		ReadStream=_stream


	#*******************************************************************#\**
	# @brief Set the default source address for the messages
	#
	# If you use an application, which sends data by using Actisense data 
	# request type, the source set by this function will be set as source. 
	# Default=65
	# 
	# @param source Source address to be used
	#*******************************************************************#\**
	def SetDefaultSource(source): #void #unsigned char 
		DefaultSource = source


	#*******************************************************************#\**
	# @brief Read Actisense formatted NMEA2000 message from stream
	# 
	# You can either call this or ParseMessages periodically.
	# 
	# Read Actisense formatted NMEA2000 message from stream
	# Actisense Format:
	# <10><02><93><length (1)><priority (1)><PGN (3)><destination (1)><source (1)><time (4)><len (1)><data (len)><CRC (1)><10><03>
	# or
	# <10><02><94><length (1)><priority (1)><PGN (3)><destination (1)><len (1)><data (len)><CRC (1)><10><03>
	# @param N2kMsg	Reference to a N2kMsg Object  
	# @param ReadOut   
	# 
	# @return True 
	# @return False  -> if (ReadStream==0)
	#*******************************************************************#\**
	def GetMessageFromStream(tN2kMsg &N2kMsg, ReadOut = True): #bool
		pass


	#********#*********************************************************#\**
	# @brief Checks if character is start
	#
	# @param ch	character
	# @return True	 -> if (ch==Escape)
	# @return False 
	#********#*********************************************************#\**
	def IsStart(char ch): #bool 
    	Return False

	#*******************************************************************#\**
	# @brief Parse messages
	#
	# Set message handler with SetMsgHandler and then call this 
	# periodically or use GetMessageFromStream
	#*******************************************************************#\**
	def ParseMessages():
		pass

	#*******************************************************************#\**
	# @brief Set the Msg Handler object
	#
	# Set message handler to be used in ParseMessages, when message has
	# been received.
	# 
	# @param _MsgHandler {type} 
	#*******************************************************************#\**
	def SetMsgHandler(void (*_MsgHandler)(const tN2kMsg &N2kMsg)):
     	MsgHandler=_MsgHandler
		pass

	#*#****************************************************************#\**
	# @brief Indicates if still message handling is needed
	# @return True
	# @return False
	#
	bool Handling() const { return MsgIsComing || EscapeReceived || StartOfTextReceived }




	'''
	#*******************************************************************\\*

	This is class for reading Actisense format messages from given stream.
	*/
	'''
	#include "ActisenseReader.h"
	#include <string.h>
	#include "N2kTimer.h"

	#*******************************************************************\\*
	def tActisenseReader(tActisenseReader):
		DefaultSource=65
		ReadStream=0
		ClearBuffer()


	#*******************************************************************\\*
	def tActisenseReader(ClearBuffer):
		MsgWritePos         = 0
		byteSum             = 0
		StartOfTextReceived = False
		MsgIsComing         = False
		EscapeReceived      = False


	#*******************************************************************\\*
	def tActisenseReader( AddByteToBuffer(NewByte) ):
		if ( MsgWritePos >= MAX_STREAM_MSG_BUF_LEN ):
			return False

		MsgBuf[MsgWritePos] = NewByte
		MsgWritePos += 1

		if ( MsgBuf[1]+3!=MsgWritePos ):
			byteSum = byteSum + NewByte # !Do not add CRC to byteSum
			return True


	#define Escape 0x10
	#define StartOfText 0x02
	#define EndOfText 0x03
	#define MsgTypeN2kData 0x93
	#define MsgTypeN2kRequest 0x94

	#\*****************************************************************************
	def tActisenseReader( CheckMessage(tN2kMsg &N2kMsg) ):  #bool 
		N2kMsg.Clear()

		if (MsgWritePos!=MsgBuf[1]+3):
			return False # Length does not match. Add type, length and crc

		CheckSum = ( (byteSum == 0) ? 0 : (256 - byteSum))

		if ( CheckSum!=MsgBuf[MsgWritePos-1] ):
			return False # Checksum does not match

		i = 2
		N2kMsg.Priority=MsgBuf[ i+=1 ]
		N2kMsg.PGN=GetBuf3ByteUInt(i,MsgBuf)
		N2kMsg.Destination=MsgBuf[ i+=1 ]

		if ( MsgBuf[0]==MsgTypeN2kData ):
			N2kMsg.Source=MsgBuf[i+=1]
			N2kMsg.MsgTime=GetBuf4ByteUInt(i,MsgBuf)
		else:
			N2kMsg.Source=DefaultSource
			N2kMsg.MsgTime=N2kMillis()

		N2kMsg.DataLen=MsgBuf[i+=1]

		if ( N2kMsg.DataLen>tN2kMsg::MaxDataLen ):
			N2kMsg.Clear()
			return False # Too long data

		J=0
		for i in range(MsgWritePos - 1):
			N2kMsg.Data[j] = MsgBuf[i]
			i = i+1
			j = j+1
   
		return True


	#\*****************************************************************************
	def tActisenseReader( IsStart(ch) ):
		return (ch==Escape)


	#**************************************************************************//*
	# Read Actisense formatted NMEA2000 message from stream
	# Actisense Format:
	# <10><02><93><length (1)><priority (1)><PGN (3)><destination (1)><source (1)><time (4)><len (1)><data (len)><CRC (1)><10><03>
	# or
	# <10><02><94><length (1)><priority (1)><PGN (3)><destination (1)><len (1)><data (len)><CRC (1)><10><03>
	#**************************************************************************//*
	def tActisenseReader(GetMessageFromStream(tN2kMsg &N2kMsg, bool ReadOut)): #bool
		result = False

		if (ReadStream==0):
			return False

		NewByte = 0
		ContinueLoopAvailable = True
  
		'''
		while ((NewByte = ReadStream->peek()) != -1 && !result && ContinueLoopAvailable):
			# Serial.println((char)NewByte,HEX)
			if (MsgIsComing):
				ReadStream->read()
				if (EscapeReceived):
					switch (NewByte): 
						case Escape: # Escaped Escape
							EscapeReceived = False
							if (!AddByteToBuffer(NewByte)):
								ClearBuffer()
							break
						case EndOfText: // Message ready
							switch (MsgBuf[0]) {
								case MsgTypeN2kData:
								case MsgTypeN2kRequest:
								result=CheckMessage(N2kMsg)
								break
								default:
									result=False
							}
							ClearBuffer()
							break
							case StartOfText: // Start new message
							ClearBuffer()
							StartOfTextReceived=True
							break
						default: # Error
							ClearBuffer()
				else:
					if (NewByte==Escape):
						EscapeReceived=True
					else:
						if (!AddByteToBuffer(NewByte)) ClearBuffer()
			else:
				switch (NewByte):
					case StartOfText:
						StartOfTextReceived=False
						if (EscapeReceived):
							ReadStream->read() // Read ch out
							ClearBuffer()
							StartOfTextReceived=True
						break
					default:
						EscapeReceived=(NewByte==Escape)
						if (StartOfTextReceived):
							ReadStream->read() // Read ch out
							StartOfTextReceived=False
							MsgIsComing=True
							AddByteToBuffer(NewByte)
						else:
							if ( EscapeReceived || ReadOut ) ReadStream->read() # Read ch out

		ContinueLoopAvailable=ReadOut || Handling()

		return result
		'''

		#***
		while ((NewByte := ReadStream.read(1)) != b'' and not result and ContinueLoopAvailable):
			if MsgIsComing:
				if EscapeReceived:
					if NewByte == Escape: # Escaped Escape
						EscapeReceived = False
						if not AddByteToBuffer(NewByte):
							ClearBuffer()
					elif NewByte == EndOfText: # Message ready
						if MsgBuf[0] in [MsgTypeN2kData, MsgTypeN2kRequest]:
							result = CheckMessage(N2kMsg)
						else:
							result = False
						ClearBuffer()
					elif NewByte == StartOfText: # Start new message
						ClearBuffer()
						StartOfTextReceived = True
					else: # Error
						ClearBuffer()
				else:
					if NewByte == Escape:
						EscapeReceived = True
					else:
						if not AddByteToBuffer(NewByte):
							ClearBuffer()
			else:
				if NewByte == StartOfText:
					StartOfTextReceived = False
					if EscapeReceived:
						ClearBuffer()
						StartOfTextReceived = True
				else:
					EscapeReceived = (NewByte == Escape)
					if StartOfTextReceived:
						StartOfTextReceived = False
						MsgIsComing = True
						AddByteToBuffer(NewByte)
					else:
						if EscapeReceived or ReadOut:
							pass # Read ch out

		ContinueLoopAvailable = ReadOut or Handling()

		return result
		#***


		#\*****************************************************************************
		def tActisenseReader(ParseMessages):
			tN2kMsg N2kMsg

			while (GetMessageFromStream(N2kMsg)):
				if (MsgHandler!=0):
					MsgHandler(N2kMsg)
				else:
					ParseMessages(N2kMsg)
