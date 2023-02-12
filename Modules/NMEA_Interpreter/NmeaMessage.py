# ****************************************************************************//*
# *   @project  Python NMEA Connector
# *   @file     BWC.py
# *   @brief    Cross Track Error, Measured
# *   @author   Karsten Reitan Sørensen
# *   Date:     11-02-2023
# *******************************************************************************

from NMEA0183_Commands import NMEA0183_Command as NMEAMessage


'''
# <summary>
# Nmea message attribute type used on concrete <see cref="NmeaMessage"/> implementations.
# </summary>
# <remarks>
# The 5-character <see cref="NmeaType"/> indicates which message the class is meant to parse.
# Set the first two characters to <c>--</c> to make the message talker-independent.
# </remarks>
# <seealso cref="NmeaMessage.RegisterAssembly(Assembly, bool)"/>
# <seealso cref="NmeaMessage.RegisterNmeaMessage(TypeInfo, string, bool)"/>
[AttributeUsage(AttributeTargets.Class, AllowMultiple = False)]
'''

class NmeaMessageTypeAttribute( Attribute ):
	def __init__(self, NmeaType: str):
		self._NmeaType = NmeaType

	# Initializes a new instance of the <see cref="NmeaMessageTypeAttribute"/> class.
	# <param name="nmeaType">The 5-character NMEA type name, for instance <c>GPRMC</c>, or <c>--RMC</c> to make it apply to all talkers.</param>
	def NmeaMessageTypeAttribute( nmeaType: str ):
		NmeaType = nmeaType

	# Gets the NMEA message type name.
	# <remarks>
	# If the type name starts with <c>--</c>, this message can apply to all talker types.
	# </remarks>
	NmeaType: str
	_NmeaType: str = field(init=False, repr=False)

	@property
	def NmeaType(self) -> str:
			return self._NmeaType

	@NmeaType.setter
	def NmeaType(self, NmeaType: str):
		self._NmeaType = NmeaType


# NMEA Message base class.
class NmeaMessage(): #IEquatable<NmeaMessage>

	messageTypes: dict = dict(str, ConstructorInfo) #

	@staticmethod
	def NmeaMessage():
		messageTypes = dict( Dictionary<string, ConstructorInfo>() )
		typeinfo = typeof(NmeaMessage).GetTypeInfo()
		RegisterAssembly(typeinfo.Assembly)
  
	# Initializes an instance of the NMEA message
	# <param name="messageType">Type</param>
	# <param name="messageParts">Message values</param>
	def NmeaMessage( messageType: str, messageParts: str = [] ):
		MessageType = messageType
		MessageParts = messageParts
		Timestamp = System.Diagnostics.Stopwatch.GetTimestamp() * 1000 / System.Diagnostics.Stopwatch.Frequency

	# Gets a relative timestamp in milliseconds indicating the time the message was created.
	# <remarks>
	# This value is deduced from <c>System.Diagnostics.Stopwatch.GetTimestamp() * 1000d / System.Diagnostics.Stopwatch.Frequency</c>.
	# You can use it to calculate the age of the message in milliseconds by calculating the difference between the timestamp and the above expression
	# </remarks>
	Timestamp: float
	_Timestamp: float = field(init=False, repr=False)

	def __init__(self, Timestamp: float):
		self._Timestamp = Timestamp

	@property
	def Timestamp(self) -> float:
		return self._Timestamp

	@Timestamp.setter
	def Timestamp(self, Timestamp: float):
		self._Timestamp = Timestamp

	# Gets the NMEA message parts.
	MessageParts: str
	_MessageParts: str = field(init=False, repr=False)

	def __init__(self, MessageParts: str):
		self._MessageParts = MessageParts

	@property
	def MessageParts(self) -> str:
			return self._MessageParts

	@MessageParts.setter
	def MessageParts(self, MessageParts: str):
		self._MessageParts = MessageParts
  
	# Gets the NMEA type id for the message.
	# <value>The 5 character string that identifies the message type</value>
	MessageType: str
	_MessageType: str = field(init=False, repr=False)

	def __init__(self, MessageType: str):
		self._MessageType = MessageType

	@property
	def MessageType(self) -> str:
			return self._MessageType

	@MessageType.setter
	def MessageType(self, MessageType: str):
		self._MessageType = MessageType

	# Gets the talker ID for this message (
	#public virtual Talker TalkerId => TalkerHelper.GetTalker(MessageType)

	# Gets a value indicating whether this message type is proprietary
	#public bool IsProprietary => MessageType[0] == 'P' # Appendix B


	# Registers messages from a different assembly
	# <remarks>
	# The custom message MUST have a constructor taking a <c>string</c> as first parameter (message type name) and a <c>str[]</c> (message parts) as the second.
	# In addition the class must have the <see cref="NmeaMessageTypeAttribute" /> defind on the class.
	# </remarks>
	# <param name="assembly">The assembly to load custom message types from</param>
	# <param name="replace">Set to <c>true</c> if you want to replace already registered type. Otherwise this method will throw.</param>
	# <returns>Number of message types found.</returns>
	@staticmethod
	def RegisterAssembly( assembly: Assembly, replace: bool = False):
		count: int = 0

		#foreach subclass in assembly.DefinedTypes.Where(t => t.IsSubclassOf(typeof(NmeaMessage)) and not t.IsAbstract):
		#	attr = subclass.GetCustomAttribute<NmeaMessageTypeAttribute>(False)
   
		#	if (attr != null):
		#		RegisterNmeaMessage(subclass, attr.NmeaType, replace)
		#		count += 1
  
		return count


	# Registers a specific NMEA Message type
	# <param name="typeInfo">TypeInfo for the class being registered</param>
	# <param name="nmeaType">The 5-character NMEA Type name (eg <c>GPGLL</c>). If <c>null</c>, it'll expect the <see cref="NmeaMessageTypeAttribute" /> to be declared on the class. </param>
	# <param name="replace">Set to <c>true</c> if you want to replace already registered type. Otherwise this method will throw.</param>
	@staticmethod
	def RegisterNmeaMessage( typeInfo: TypeInfo, nmeaType: str = "", replace: bool = False):
		if ( nmeaType is empty or Null ):
			attr = typeInfo.GetCustomAttribute<NmeaMessageTypeAttribute>(False)
   
			if (attr == null):
				print("Message does not have a NmeaMessageTypeAttribute and no type name was specified.")

			nmeaType = attr.NmeaType

			if (string.IsNullOrEmpty(nmeaType)):
				print("No NmeaType declared on the NmeaMessageTypeAttribute.")

		for c in typeInfo.DeclaredConstructors:
			pinfo: any = c.GetParameters()
   
			if (pinfo.Length == 2
       			and pinfo[0].ParameterType == type(str) 
          		and pinfo[1].ParameterType == type([])
            	):
				if (not replace and messageTypes.ContainsKey(nmeaType)):
					print("Message type {nmeaType} declared in {typeInfo.FullName} is already registered by {messageTypes[nmeaType].DeclaringType.FullName}")
     
				messageTypes[nmeaType] = c
				return False

		print("Type does not have a constructor with parameters (string,str[])")
		return False


	def PickError(): pass


	# Parses the specified NMEA message.
	# <param name="message">The NMEA message string.</param>
	# <param name="previousSentence">The previously received message (only used if parsing multi-sentence messages)</param>
	# <param name="ignore,Checksum">If <c>true</c> ignores the checksum completely, if <c>False</c> validates the checksum if present.</param>
	# <returns>The nmea message that was parsed.</returns>
	# <exception cref="System.ArgumentException">
	# Invalid nmea message: Missing starting character '$'
	# or checksum failure
	# </exception>
	@staticmethod
	def Parse( 
				message: str, 
				previousSentence: IMultiSentenceMessage = None, 
				ignoreChecksum: bool = False
			):
		if (string.IsNullOrEmpty(message)):
			print(nameof(message))

		checksum: int = -1
		if (message[0] != '$'):
			print("Invalid NMEA message: Missing starting character '$'")
   
		idx: int = message.IndexOf('*')
		if (idx >= 0):
			if (message.Length > idx + 1): pass
				# if (int.parse
        		# 		TryParse(
               	# 			message.Substring(idx + 1), 
                #     		NumberStyles.HexNumber, 
                #     		CultureInfo.InvariantCulture, 
                #       		out int c
				# 		)
           		# 	):
				# 	checksum = c
				# else:
				# 	print("Invalid checksum string")

			message = message.Substring(0, message.IndexOf('*'))

		if ( not ignoreChecksum and checksum > -1 ):
			checksumTest: int = 0
   
			for i in message.Length:
				c = message[i]
				if (c < 0x20 or c > 0x7E):
					print("NMEA Message contains invalid characters")
     
				checksumTest ^= Convert.ToByte(c)
   
			if (checksum != checksumTest):
				print(string.Format(CultureInfo.InvariantCulture, "Invalid NMEA message: Checksum failure. Got {0:X2}, Expected {1:X2}", checksum, checksumTest))
		else:
			for i in message.Length:
				if (message[i] < 0x20 or message[i] > 0x7E):
					print("NMEA Message contains invalid characters")

		# Split the message into parts
		parts: list[str] = message.split( ',' )
		MessageType: str = parts[0].Substring(1)
		if (MessageType == string.Empty):
			print("Missing NMEA Message Type")
   
		#MessageParts: list[str] = parts.Skip(1).ToArray()
		if NmeaMessageTypeAttribute:#((previousSentence == pmsg:) and (pmsg.MessageType.Substring(2) == MessageType.Substring(2))):
			if (previousSentence.TryAppend(MessageType, MessageParts)):
				return pmsg

		if (messageTypes.ContainsKey(MessageType)):
			return #(NmeaMessage)messageTypes[MessageType].Invoke(new object[] { MessageType, MessageParts })
		elif (messageTypes.ContainsKey("--" + MessageType.Substring(2))):
			return #(NmeaMessage)messageTypes["--" + MessageType.Substring(2)].Invoke(new object[] { MessageType, MessageParts })
		else:
			return #new UnknownMessage(MessageType, MessageParts)
  
		return NmeaMessage #public static NmeaMessage 


	# Returns the original NMEA string that represents this message.
	# <returns>An original NMEA string that represents this message.</returns>
	def ToString():
		return string.Format(CultureInfo.InvariantCulture, "${0},{1}*{2:X2}", MessageType, string.Join(",", MessageParts), Checksum)


	# Gets the checksum value of the message.
	def GetChecksum(messageType: str, messageParts = "" ):
		checksumTest: int = 0

		j:int = -1
		for j in messageParts.Count:
			message: str = messageType if j < 0 else messageParts[j]
			if (j >= 0):
				checksumTest ^= 0x2C #Comma separator
    
			for i in message.Length:
				c: any = message[i]
				if (c < 256):
					checksumTest ^= Convert.ToByte(c)
  
		return Convert.ToByte(checksumTest) #internal static byte 


	def StringToLatitude( value: str, ns: str ):
		if (value == null or value.Length < 3):
			return double.NaN
   
		latitude: float = int.Parse(value.Substring(0, 2), CultureInfo.InvariantCulture) + double.Parse(value.Substring(2), CultureInfo.InvariantCulture) / 60
  
		if (ns == "S"):
			latitude *= -1
   
		return latitude #internal static double


	def StringToLongitude( value: str, ew: str):
		if ( value == None or value.Length < 4):
			return double.NaN
   
		longitude: float = int.Parse(value.Substring(0, 3), CultureInfo.InvariantCulture) + double.Parse(value.Substring(3), CultureInfo.InvariantCulture) / 60
  
		if (ew == "W"):
			longitude *= -1
   
		return longitude #internal static double 


	def StringToDouble( value: str ):
		if True:#(value != null and double.TryParse(value, NumberStyles.Any, CultureInfo.InvariantCulture, out double result)):
			return result

		return double.NaN #internal static double


	def StringToTimeSpan( value: str ):
		if (value != null and value.Length >= 6): pass
			#return new TimeSpan(int.Parse(value.Substring(0, 2), CultureInfo.InvariantCulture),
			#					int.Parse(value.Substring(2, 2), CultureInfo.InvariantCulture), 0)
			#					.Add(TimeSpan.FromSeconds(double.Parse(value.Substring(4), CultureInfo.InvariantCulture)))
  
		return TimeSpan.Zero #internal static TimeSpan 


	# Indicates whether the current object is equal to another object of the same type.
	# <param name="other">An object to compare with this object.</param>
	# <returns><c>true</c> if the current object is equal to the other parameter otherwise, <c>False</c>.</returns>
	def Equals( other: NmeaMessage):
		if (other.MessageType != MessageType):
			return False

		if (other.MessageParts.Count != MessageParts.Count):
			return False

		for i in MessageParts.Count:
			if (other.MessageParts[i] != MessageParts[i]):
				return False
  
		return true #public bool
