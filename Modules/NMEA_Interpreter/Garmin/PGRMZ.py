# Altitude Information
#NmeaMessageType("PGRMZ")

class Pgrmz(NmeaMessage):

	#Altitude unit
	def AltitudeUnitÅ():
		#Unknown
		Unknown: str = "Unknown"
		#Feet
		Feet: str = "f"


	#Position Fix Dimension
	def PositionFixType():
		#Unknown
		Unknown: int = 0,
		#No fix
		NoFix: int = 1,
		#2D Fix
		Fix2D = 2,
		#3D Fix
		Fix3D = 3

	#Initializes a new instance of the <see cref="Pgrmz"/> class.
	#<param name="type">The message type</param>
	#<param name="message">The NMEA message values.</param>
	def Pgrmz( type: str, message: str = []):
	    # base(type, message)

		if ( message == null or message.Length < 3 ):
			print("Invalid PGRMZ", "message")

		if (message[0].Length > 0):
			Altitude = double.Parse(message[0], CultureInfo.InvariantCulture)
		else:
			Altitude = double.NaN
   
		Unit = AltitudeUnit.Feet if message[1] == "f" else AltitudeUnit.Unknown

		dim: int = -1
		#if ( message[2].Length == 1 and int.TryParse(message[2], out dim) ):
		#	if (dim >= (int)PositionFixType.NoFix and dim <= (int)PositionFixType.Fix3D):
		#		FixType = (PositionFixType) dim


	#Current altitude
	def Altitude(): get: float

	#Horizontal Error unit ('f' for Meters)
	def AltitudeUnit(): get: Unit

	#Fix type
	def PositionFixType(): get: FixType
