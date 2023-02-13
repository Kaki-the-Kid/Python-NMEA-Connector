# Altitude Information
#NmeaMessageType("PGRMZ")
# PG is the property vendor id of

class PGRMZ(NMEAMessage):

		def __init__(self, sentence):
			self._datasentence =  sentence
			if(self._datasentence.length > 3):
				raise Exception("Invalid PGRMZ sentence: {}".sentence)
			
			self._pgrmz = 0

		@property
		def pgrmz(self):
			return self._pgrmz

		@pgrmz.setter
		def pgrmz(self, value):
			if isinstance(value, int) and 0 <= value <= 999:
				self._pgrmz = value
			else:
				raise ValueError("PGRMZ must be an integer between 0 and 999")

	#Altitude unit
	def AltitudeUnit():
		#Unknown
		Unknown: str = "Unknown"
		#Feet
		Feet: str = "f"


	#Position Fix Dimension
	def PositionFixType():
		#Unknown
		Unknown = 0,
		#No fix
		NoFix = 1,
		#2D Fix
		Fix2D = 2,
		#3D Fix
		Fix3D = 3


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


       /****************************************************************************
        * $PGRMZ,93,f,3*21
        *
        * where:
        *     93,f         Altitude in feet
        *     3            Position fix dimensions 2 = user altitude
        *                                          3 = GPS altitude
        *     This sentence shows in feet, regardless of units shown on the display.
        *     Note that for units with an altimeter this will be altitude computed
        *     by the internal altimeter.
        ****************************************************************************/
        public void CommandGarminPGRMZ()
        {
            int i = 0;
            double outAltitude = double.Parse(this.CommandParts[i++]);  // Altitude in feet
            char outAltitudeUnit = char.Parse(this.CommandParts[i++]); // f = feet
            int outPositionFixDimensions = int.Parse(this.CommandParts[i++]);  // 3 Position fix dimensions 2 = user altitude, 3 = GPS altitude
        }
