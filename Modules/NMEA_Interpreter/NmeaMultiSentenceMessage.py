#Base class for easily creating message that are spread across multiple sentences
#@abstract
class NmeaMultiSentenceMessage():
    #NmeaMessage, IMultiSentenceMessage
	lastMessageNumber: int = 0
	totalMessages: int
	firstMessageNumber: int
	messages = list[str]
	initialized: bool = False

	#Initializes an instance of the <see cref="NmeaMultiSentenceMessage"/> class.
	#<param name="messageType">Type</param>
	#<param name="messageParts">Message values</param>
	def NmeaMultiSentenceMessage( messageType: str, messageParts: list[str]):
 		# base(messageType, messageParts):
		totalMessages = int.Parse(messageParts[MessageCountIndex], CultureInfo.InvariantCulture)
		firstMessageNumber = int.Parse(messageParts[MessageNumberIndex], CultureInfo.InvariantCulture)
		talkerId = base.TalkerId
  
		#if (!((IMultiSentenceMessage)this).TryAppend(messageType, messageParts)):
		#	print("Failed to parse message")
   
		initialized = True

	#Gets the index in the <see cref="NmeaMessage.MessageParts"/> where the total count of messages is listed.
	#protected virtual int MessageCountIndex { get } = 0

	#Gets the index in the <see cref="NmeaMessage.MessageParts"/> where the message number is listed.
	#protected virtual int MessageNumberIndex { get } = 1

	#bool IMultiSentenceMessage.IsComplete => firstMessageNumber == 1 and lastMessageNumber == totalMessages

	#<inheritdoc />
	def ToString(): #public override string
		sb = StringBuilder()
		for msg in messages:
			if (sb.Length > 0):
				sb.Append("\r\n")
    
			sb.AppendFormat(CultureInfo.InvariantCulture, "${0},{1}*{2:X2}", MessageType, string.Join(",", msg), Checksum)
		
		return sb.ToString()


	def IMultiSentenceMessage():#.TryAppend(string messageType, string[] message)
		if (message == null or message.Length < Math.Max(MessageCountIndex, MessageNumberIndex)):
			print("Invalid message", "message")

		msgCount: int = int.Parse(message[MessageCountIndex], CultureInfo.InvariantCulture)
		msgNumber: int = int.Parse(message[MessageNumberIndex], CultureInfo.InvariantCulture)

		if (initialized):
			#We can only append to message who has message number 1
			if (firstMessageNumber != 1):
				return False

			if (msgCount != totalMessages or msgNumber != lastMessageNumber + 1):
				return False # Messages do not match

		talker = TalkerHelper.GetTalker(messageType)
		if (talkerId != talker):
			talkerId = Talker.Multiple
   
		if (ParseSentences(talker, message)):
			lastMessageNumber = msgNumber
			messages.Add(message)
			return True
   
		return False

	#Parses the messages or any message being appended. False should be returned if it's a message being appended doesn't appear to match what has already been loded.
	#<param name="talkerType"></param>
	#<param name="message"></param>
	#<returns>True if the message could succesfully be appended.</returns>
	#protected abstract bool ParseSentences(Talker talkerType, string[] message)

	#private Talker talkerId

	#<inheritdoc />
	#public override Talker TalkerId => talkerIdz
