# GPS Data Structure



from dataclasses import field, dataclass


@dataclass
class StructGPSData:
	def __init__(
		self, 
		GPSTimestamp: str,
		GPSLatitudeDegree: str,
		GPSLatitudeMins: str,
		GPSLatitudeDirection: str,
		GPSLatitudeString: str,
		GPSLongitudeDegree: str,
		GPSLongitudeMins: str,
		GPSLongitudeDirection: str,
		GPSLongitudeString: str,
		GPSQuality: int,
		GPSQualityText: str,
		GPSNumberSatelites: int,
		GPSHdop: float,
		GPSAntenneAltitude: float,
		GPSAntennaAltitudemf: str,
		GPSGeoidalSeparation: float,
		GPSGeoidalSeparationmf: str,
		GPSAgeCorrection: str,
		GPSStationId: str,
		GPSLastChecksum: str,
		GPSLastChecksumOK: bool
		):
		self._GPSTimestamp = GPSTimestamp
		self._GPSLatitudeDegree = GPSLatitudeDegree
		self._GPSLatitudeMins = GPSLatitudeMins
		self._GPSLatitudeDirection = GPSLatitudeDirection
		self._GPSLatitudeString = GPSLatitudeString
		self._GPSLongitudeDegree = GPSLongitudeDegree
		self._GPSLongitudeMins = GPSLongitudeMins
		self._GPSLongitudeDirection = GPSLongitudeDirection
		self._GPSLongitudeString = GPSLongitudeString
		self._GPSQuality = GPSQuality
		self._GPSQualityText = GPSQualityText
		self._GPSNumberSatelites = GPSNumberSatelites
		self._GPSHdop = GPSHdop
		self._GPSAntenneAltitude = GPSAntenneAltitude
		self._GPSAntennaAltitudemf = GPSAntennaAltitudemf
		self._GPSGeoidalSeparation = GPSGeoidalSeparation
		self._GPSGeoidalSeparationmf = GPSGeoidalSeparationmf
		self._GPSAgeCorrection = GPSAgeCorrection
		self._GPSStationId = GPSStationId
		self._GPSLastChecksum = GPSLastChecksum
		self._GPSLastChecksumOK = GPSLastChecksumOK


	# region GPSTimestamp
	# Timestamp: UTC time in hours, minutes and seconds.
	# Ex.181908.000 denotes 18 hours, 19 minutes and 08 seconds.
	GPSTimestamp:  str
	_GPSTimestamp: str = field(init=False, repr=False)
 
	@property
	def GPSTimestamp(self) -> str:
		return self._GPSTimestamp

	@GPSTimestamp.setter
	def GPSTimestamp(self, GPSTimestamp: str):
		self._GPSTimestamp = GPSTimestamp

	# endregion GPSTimestamp


	# region GPSLatitudeDegree
 	# Latitude in the DDMM.MMMMM format.Decimal places are variable.
	# N denotes north latitude.
	GPSLatitudeDegree:  str
	_GPSLatitudeDegree: str = field(init=False, repr=False)
 
	@property
	def GPSLatitudeDegree(self) -> str:
		return self._GPSLatitudeDegree

	@GPSLatitudeDegree.setter
	def GPSLatitudeDegree(self, GPSLatitudeDegree: str):
		self._GPSLatitudeDegree = GPSLatitudeDegree

	# endregion GPSLatitudeDegree


	# region GPSLatitudeMins
	# Latitude in the DDMM.MMMMM format.Decimal places are variable.
	GPSLatitudeMins:  str
	_GPSLatitudeMins: str = field(init=False, repr=False)

	@property
	def GPSLatitudeMins(self) -> str:
		return self._GPSLatitudeMins

	@GPSLatitudeMins.setter
	def GPSLatitudeMins(self, GPSLatitudeMins: str):
		self._GPSLatitudeMins = GPSLatitudeMins

	# endregion GPSLatitudeMins


	# region GPSLatitudeDirection
	# Latitude direction N denotes north latitude.
	GPSLatitudeDirection:  str
	_GPSLatitudeDirection: str = field(init=False, repr=False)

	@property
	def GPSLatitudeDirection(self) -> str:
		return self._GPSLatitudeDirection

	@GPSLatitudeDirection.setter
	def GPSLatitudeDirection(self, GPSLatitudeDirection: str):
		self._GPSLatitudeDirection = GPSLatitudeDirection

	# endregion GPSLatitudeDirection


	# region GPSLatitudeString
	GPSLatitudeString:  str
	_GPSLatitudeString: str = field(init=False, repr=False)
 
	@property
	def GPSLatitudeString(self) -> str:
		return self.GPSLatitudeString

	@GPSLatitudeString.setter
	def GPSLatitudeString(self, GPSLatitudeString: str):
		self._GPSLatitudeString = GPSLatitudeString
  
	# endregion GPSLatitudeString


	# region GPSLongitudeDegree
	# Longitude in the DDDMM.MMMMM format. Decimal places are variable. W denotes west longitude.
	# 07044.3966270 is the same as 070° 44.3966270' W
	GPSLongitudeDegree:  str
	_GPSLongitudeDegree: str = field(init=False, repr=False)
 
	@property
	def GPSLongitudeDegree(self) -> str:
		return self._GPSLongitudeDegree

	@GPSLongitudeDegree.setter
	def GPSLongitudeDegree(self, GPSLongitudeDegree: str):
		self._GPSLongitudeDegree = GPSLongitudeDegree
  
	# endregion GPSLongitudeDegree
 

	# region GPSLongitudeMins
	# Longitude in the DDDMM.MMMMM format. Decimal places are variable. W denotes west longitude.
	# 07044.3966270 is the same as 070° 44.3966270' W
	GPSLongitudeMins:  str
	_GPSLongitudeMins: str = field(init=False, repr=False)

	@property
	def GPSLongitudeMins(self) -> str:
		return self._GPSLongitudeMins

	@GPSLongitudeMins.setter
	def GPSLongitudeMins(self, GPSLongitudeMins: str):
		self._GPSLongitudeMins = GPSLongitudeMins

	# endregion GPSLongitudeMins


	# region GPSLongitudeDirection
	# Longitude in the DDDMM.MMMMM format. Decimal places are variable. W denotes west longitude.
	GPSLongitudeDirection:  str
	_GPSLongitudeDirection: str = field(init=False, repr=False)
 
	@property
	def GPSLongitudeDirection(self) -> str:
		return self._GPSLongitudeDirection

	@GPSLongitudeDirection.setter
	def GPSLongitudeDirection(self, GPSLongitudeDirection: str):
		self._GPSLongitudeDirection = GPSLongitudeDirection

	# endregion GPSLongitudeDirection
 
 
	# region GPSLongitudeString
	# Longitude in the DDDMM.MMMMM format. Decimal places are variable. W denotes west longitude.
	GPSLongitudeString:  str
	_GPSLongitudeString: str = field(init=False, repr=False)
 
	@property
	def GPSLongitudeString(self) -> str:
		return self._GPSLongitudeString

	@GPSLongitudeString.setter
	def GPSLongitudeString(self, GPSLongitudeString: str):
		self._GPSLongitudeString = GPSLongitudeString

	# endregion GPSLongitudeString
 

	# region GPSAltitude
	# denotes the Quality Indicator: 0 = Invalid, 1 = GPS fix, 2 = DGPS fix.
	GPSQuality:  int
	_GPSQuality: int = field(init=False, repr=False)
 
	@property
	def GPSQuality(self) -> int:
		return self._GPSQuality

	@GPSQuality.setter
	def GPSQuality(self, GPSQuality: int):
		self._GPSQuality = GPSQuality

	# endregion GPSQuality


	# region GPSQualityText
	# denotes the Quality Indicator: 0 = Invalid, 1 = GPS fix, 2 = DGPS fix.
	GPSQualityText:  str
	_GPSQualityText: str = field(init=False, repr=False)
 
	@property
	def GPSQualityText(self) -> str:
		return self._GPSQualityText

	@GPSQualityText.setter
	def GPSQualityText(self, GPSQualityText: str):
		self._GPSQualityText = GPSQualityText

	# endregion GPSQualityText


	# region GPSNumberSatelites
	# 13 denotes number of satellites used in the coordinate.
	GPSNumberSatelites:  int
	_GPSNumberSatelites: int = field(init=False, repr=False)
 
	@property
	def GPSNumberSatelites(self) -> int:
		return self._GPSNumberSatelites

	@GPSNumberSatelites.setter
	def GPSNumberSatelites(self, GPSNumberSatelites: int):
		self._GPSNumberSatelites = GPSNumberSatelites

	# endregion GPSNumberSatelites


	# region GPSHdop
	# 1.00 denotes the HDOP (horizontal dilution of precision).
	GPSHdop:  float
	_GPSHdop: float = field(init=False, repr=False)
 
	@property
	def GPSHdop(self) -> float:
		return self._GPSHdop

	@GPSHdop.setter
	def GPSHdop(self, GPSHdop: float):
		self._GPSHdop = GPSHdop
  
	# endregion GPSHdop


	# region GPSAltitude
	# 0.0 denotes the altitude of the antenna in meters.
	# 495.144 denotes altitude of the antenna.
	GPSAntenneAltitude:  float
	_GPSAntenneAltitude: float = field(init=False, repr=False)
 
	@property
	def GPSAntenneAltitude(self) -> float:
		return self._GPSAntenneAltitude

	@GPSAntenneAltitude.setter
	def wheels(self, GPSAntenneAltitude: float):
		self._GPSAntenneAltitude = GPSAntenneAltitude
  
	# endregion GPSAltitude


	# region GPSAntennaAltitudemf
	# M denotes the units used by the altitude of the antenna.
	# M denotes units of altitude ( eg. Meters or Feet )
	GPSAntennaAltitudemf:  str
	_GPSAntennaAltitudemf: str = field(init=False, repr=False)
 
	@property
	def GPSAntennaAltitudemf(self) -> str:
		return self._GPSAntennaAltitudemf

	@GPSAntennaAltitudemf.setter
	def GPSAntennaAltitudemf(self, GPSAntennaAltitudemf: str):
		self._GPSAntennaAltitudemf = GPSAntennaAltitudemf

	# endregion GPSAntennaAltitudemf


	# region GPSGeoidalSeparation
	# 0.0 denotes the geoidal separation in meters.
	# 29.200 denotes the geoidal separation(subtract this from the altitude of the antenna 
	# to arrive at the Height Above Ellipsoid (HAE).
	GPSGeoidalSeparation:  float
	_GPSGeoidalSeparation: float = field(init=False, repr=False)
 
	@property
	def GPSGeoidalSeparation(self) -> float:
		return self._GPSGeoidalSeparation

	@GPSGeoidalSeparation.setter
	def GPSGeoidalSeparation(self, GPSGeoidalSeparation: float):
		self._GPSGeoidalSeparation = GPSGeoidalSeparation
  
	# endregion GPSGeoidalSeparation
 
 
	# region GPSGeoidalSeparationmf
	# M denotes the units used by the geoidal separation.
	# M denotes units of geoidal separation ( eg. Meters or Feet )
	GPSGeoidalSeparationmf:  str
	_GPSGeoidalSeparationmf: str = field(init=False, repr=False)
 
	@property
	def GPSGeoidalSeparationmf(self) -> str:
		return self._GPSGeoidalSeparationmf

	@GPSGeoidalSeparationmf.setter
	def GPSGeoidalSeparationmf(self, GPSGeoidalSeparationmf: str):
		self._GPSGeoidalSeparationmf = GPSGeoidalSeparationmf
  
	# endregion GPSGeoidalSeparationmf
 

	# region GPSAgeCorrection
	# 0.0 denotes the age of differential GPS data in seconds.
	# 1.0 denotes the age of the correction (if any).
	GPSAgeCorrection:  float
	_GPSAgeCorrection: float = field(init=False, repr=False)
 
	@property
	def GPSAgeCorrection(self) -> float:
		return self._GPSAgeCorrection

	@GPSAgeCorrection.setter
	def GPSAgeCorrection(self, GPSAgeCorrection: float):
		self._GPSAgeCorrection = GPSAgeCorrection
  
	# endregion GPSAgeCorrection


	# region GPSStationId
	# 0000 denotes the correction station ID (if any)
	GPSStationId:  str
	_GPSStationId: str = field(init=False, repr=False)
 
	@property
	def GPSStationId(self) -> str:
		return self._GPSStationId

	@GPSStationId.setter
	def GPSStationId(self, GPSStationId: str):
		self._GPSStationId = GPSStationId
  
	# endregion GPSStationId


	# region GPSLastChecksum
 	# *40 denotes the checksum.
	GPSLastChecksum:  str
	_GPSLastChecksum: str = field(init=False, repr=False)
 
	@property
	def GPSLastChecksum(self) -> str:
		return self._GPSLastChecksum

	@GPSLastChecksum.setter
	def GPSLastChecksum(self, GPSLastChecksum: str):
		self._GPSLastChecksum = GPSLastChecksum

	# endregion GPSLastChecksum


	# region GPSLastChecksumOK
	# *40 denotes the checksum.
	GPSLastChecksumOK:  str
	_GPSLastChecksumOK: str = field(init=False, repr=False) 
 
	@property
	def GPSLastChecksumOK(self) -> str:
		return self._GPSLastChecksumOK

	@GPSLastChecksumOK.setter
	def GPSLastChecksumOK(self, GPSLastChecksumOK: str):
		self._GPSLastChecksumOK = GPSLastChecksumOK

	# endregion GPSLastChecksumOK
