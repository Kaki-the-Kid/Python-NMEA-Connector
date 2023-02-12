# NMEA 0183 Commands

NMEA 0183 is a standard for communicating with marine electronic devices and is widely used for GPS, sonar, and other navigation and positioning equipment. The standard defines a number of sentences, each starting with a "$" symbol and ending with a carriage return and line feed sequence. Here are some of the most common NMEA 0183 sentences:

## BOD (\$GPBOD) - Bearing - Origin to Destination

Provides information about the bearing from the vessel to a destination waypoint.

The BOD (Bearing, Origin to Destination) command is used to convey bearing information from one point to another. The attributes of the BOD command are:

The BOD class has four attributes:

* Waypoint ID of the origin: A character string that identifies the origin of the bearing information.
* Waypoint ID of the destination: A character string that identifies the destination of the bearing information.
* True bearing in degrees: A decimal number that represents the true bearing from the origin to the destination, in degrees.
* Magnetic variation in degrees: A decimal number that represents the magnetic variation at the origin, in degrees.
* Magnetic variation direction: A character indicating whether the magnetic variation is East (E) or West (W).
* Magnetic variation direction: A character indicating whether the magnetic variation is East (E) or West (W).
* Mode indicator: A character indicating the navigation mode (autonomous, differential, estimated, manual input, simulated, or not valid).

Example: $BOD,123456,654321,123.4,5.6,E,A*15

* bearing
* bearing_type
* destination
* and origin

The bearing attribute represents the bearing from the origin to the destination. The bearing_type attribute represents the type of bearing, such as true or magnetic. The destination and origin attributes represent the destination and origin waypoints, respectively. The class implements getters and setters for each attribute to allow for easy access and modification of the attributes.

## BWC (\$GPBWC) - Bearing and Distance to Waypoint - Great Circle

Provides information about the bearing and distance from the vessel to a destination waypoint.

The BWC class has five attributes:

* bearing
* bearing_type
* destination
* time
* and to

The bearing attribute represents the bearing from the current position to the destination waypoint. The bearing_type attribute represents the type of bearing, such as true or magnetic. The destination attribute represents the destination waypoint. The time attribute represents the estimated time of arrival at the destination waypoint. The to attribute represents the name of the destination waypoint. The class implements getters and setters for each attribute to allow for easy access and modification of the attributes.

## DBT (\$GPDBT) - Depth Below Transducer

Provides information about the depth of the vessel below the transducer.

The DBT class has four attributes:

* depth
* depth_unit
* depth_offset
* and depth_offset_unit

The depth attribute represents the water depth below the transducer. The depth_unit attribute represents the unit of measurement for the depth, such as feet or meters. The depth_offset attribute represents the depth offset, which is used to correct the depth measurement. The depth_offset_unit attribute represents the unit of measurement for the depth offset. The class implements getters and setters for each attribute to allow for easy access and modification of the attributes.

## DPT (\$GPDPT) - Depth of Water

Provides information about the depth of the vessel below the surface of the water.

The DPT class has two attributes:

* depth
* offset

The depth attribute represents the water depth below the transducer. The offset attribute represents the depth offset, which is used to correct the depth measurement. The class implements getters and setters for each attribute to allow for easy access and modification of the attributes.

## DSC (\$IIDSC) - Digital Selective Calling

Provides information about the vessel's DSC status.

The DSC class has two attributes:

* mmsi
* message_type

The mmsi attribute represents the Maritime Mobile Service Identity of the vessel that is calling. The message_type attribute represents the type of DSC message being sent. The class implements getters and setters for each attribute to allow for easy access and modification of the attributes.

## DSE (\$GPDSE) - Distance to Waypoint - Elipsoidal

Provides information about the distance from the vessel to a destination waypoint.

The DSE class has four attributes:

* total_number_of_sentences
* sentence_number
* command
* and data

The total_number_of_sentences attribute represents the total number of sentences in a multi-sentence message. The sentence_number attribute represents the sentence number for the current sentence. The command attribute represents the command being sent. The data attribute represents the data being sent. The class implements getters and setters for each attribute to allow for easy access and modification of the attributes.

## DTM (\$GPDTM) - Datum Reference

Provides information about the datum used to calculate the position.

The DTM class has seven attributes:

* total_number_of_sentences
* sentence_number
* command
* date
* local_datum
* latitude_offset
* longitude_offset

The total_number_of_sentences attribute represents the total number of sentences in a multi-sentence message. The sentence_number attribute represents the sentence number for the current sentence. The command attribute represents the command being sent. The date attribute represents the date. The local_datum attribute represents the local datum reference. The latitude_offset attribute represents the latitude offset for the local datum reference. The `long

## GBS (\$GPGBS) - GPS/GNSS Satellite Fault Detection

Provides information about the GPS receiver's ability to calculate the position.

This class defines the properties of a GBS command and provides setter and getter methods for each property. You can use these methods to set and retrieve the values of the GBS command's properties.

## GGA - Global Positioning System Fix Data

\$GPGGA: Global Positioning System Fix Data. Provides information about the GPS receiver's current position, including latitude, longitude, altitude, time, and the number of satellites being used to calculate the position.

The GGA (Global Positioning System Fix Data) command is a sentence from the National Marine Electronics Association (NMEA) 0183 protocol. It is used to provide essential fix data for a GPS receiver. The GGA sentence includes the following attributes:

* Time: The time of the fix, in the format of hhmmss.
* Latitude: The latitude of the fix, in decimal degrees.
* Latitude Hemisphere: Indicates whether the latitude is North or South.
* Longitude: The longitude of the fix, in decimal degrees.
* Longitude Hemisphere: Indicates whether the longitude is East or West.
* Fix Quality: A number indicating the quality of the fix.
* Number of Satellites: The number of satellites being tracked.
* HDOP (Horizontal Dilution of Precision): A measure of the fix accuracy.
* Altitude: The altitude of the receiver, above mean sea level.
* Altitude Units: The units for the altitude, either meters or feet.
* Geoidal Separation: The difference between the WGS-84 earth ellipsoid and the mean sea level.
* Separation Units: The units for the geoidal separation, either meters or feet.
* Age of Differential GPS Data: The time elapsed since the last DGPS update.
* Differential Reference Station ID: The ID number of the differential reference station.

These are the basic attributes of the GGA command. There may be additional attributes in some implementations, depending on the GPS receiver being used.

## GLL (\$GPGLL) - Geographic Position - Latitude/Longitude

Provides information about the GPS receiver's current latitude and longitude.

In this class, the GLL command attributes are represented as class variables and accessed using getter and setter methods. The @property decorator is used to define getter methods, while the @attribute name.setter decorator is used to define setter methods. The setter methods allow you to update the values of the class variables, while the getter methods allow you to retrieve their values.

## GNS (\$GPGNS) - GNSS Fix Data

Provides information about the GPS receiver's current position, including latitude, longitude, altitude, time, and the number of satellites being used to calculate the position.

## GRS - GPS Range Residuals

\$GPGRS: GPS Range Residuals. Provides information about the GPS receiver's ability to calculate the position.

In this code, the class GRS has a private variable __grs_data to store the GRS data and two methods: set_grs_data to set the GRS data and get_grs_data to get the GRS data. The setter method takes in a dictionary as an argument and sets the__grs_data variable, and the getter method returns the value stored in the __grs_data variable.

## GSA - GPS DOP and Active Satellites

\$GPGSA: GPS DOP and Active Satellites. Provides information about the dilution of precision (DOP) and the satellites being used to calculate the position.

In this code, the class GSA has a private variable __gsa_data to store the GSA data and two methods: set_gsa_data to set the GSA data and get_gsa_data to get the GSA data. The setter method takes in a dictionary as an argument and sets the__gsa_data variable, and the getter method returns the value stored in the __gsa_data variable.

## GST (\$GPGST) - GPS Pseudorange Noise Statistics

Provides information about the GPS receiver's ability to calculate the position.

The class takes the NMEA0183 GST message as an input, and has getters and setters for all the attributes of the message, including time of day, RMS value, semi-major deviation, semi-minor deviation, semi-major orientation, latitude error deviation, longitude error deviation, and altitude error deviation.

## GSV - GPS Satellites in View

\$GPGSV: GPS Satellites in View. Provides information about the satellites in view, including their ID, elevation, azimuth, and signal strength.

The n_messages attribute holds the number of messages the GSV command will be split into. The message_number attribute holds the current message number. The satellites_in_view attribute holds the number of satellites in view. The satellite_data attribute holds a list of dictionaries, each containing information about a single satellite, including its PRN number, elevation, azimuth, and signal-to-noise ratio.

## HDG - Heading - Deviation & Variation

\$GPHDG: Heading - Deviation & Variation. Provides information about the vessel's heading, including magnetic deviation and variation.

## HDM (\$GPHDM) - Heading - Magnetic

Provides information about the vessel's heading, including magnetic deviation and variation.

The HDM (Heading Magnetic) command provides information about the magnetic heading of a vessel. The HDM command consists of the following attributes:

Talker ID: A two-character identifier that specifies the source of the sentence. For example, "GP" for GPS.

Heading: The magnetic heading of the vessel in degrees.

Units: The unit of measurement for the heading, either "M" for degrees magnetic or "T" for degrees true.

Example: $GPHDM,100.0,M*15

In this example, the Talker ID is "GP" (GPS), the heading is 100.0 degrees magnetic, and the unit of measurement is "M".

## HDT (\$GPHDT) - Heading - True

Provides information about the vessel's heading, including magnetic deviation and variation.

The HDT command includes the following attributes:

* Heading: The true heading in degrees.
* Reference: The reference for the heading, either 'T' for True or 'M' for Magnetic.

The get_heading and set_heading methods allow you to retrieve and set the heading attribute, respectively. The get_reference and set_reference methods allow you to retrieve and set the reference attribute, respectively. The __str__ method allows you to print a human-readable representation of the object.

## MDA (\$IIMDA) - Meteorological Composite

Provides information about the vessel's current weather conditions.

The MDA command stands for Meteorological Composite Data and is a proprietary NMEA0183 command that provides various meteorological data. Some common attributes of the MDA command include:

* Barometric Pressure: It gives the barometric pressure in millibars
* Air Temperature: It gives the air temperature in degrees Celsius
* Water Temperature: It gives the water temperature in degrees Celsius
* Relative Humidity: It gives the relative humidity percentage
* Dew Point: It gives the dew point temperature in degrees Celsius
* Wind Speed: It gives the wind speed in knots
* Wind Direction: It gives the wind direction in degrees
* True Wind Speed: It gives the true wind speed in knots
* True Wind Direction: It gives the true wind direction in degrees
* Apparent Wind Speed: It gives the apparent wind speed in knots
* Apparent Wind Direction: It gives the apparent wind direction in degrees

## MTW (\$IIMTW) - Water Temperature

Provides information about the water temperature.

The MTW command has the following attributes:

* Water temperature (C)
  * The water temperature measurement, in degrees Celsius.
  * The value can range from -273 to 65535, with a resolution of 0.1 degrees Celsius.

## MWV (\$IIMWV) - Wind Speed and Angle

Provides information about the vessel's wind speed and angle.

The attributes for the MWV command are:

* Wind Speed: The speed of the wind in knots.
* Wind Angle: The direction of the wind in degrees True.
* Reference: Whether the Wind Angle is given as "R" (Relative) or "T" (True).

The function and value of these attributes in the MWV command are used to communicate wind speed and direction information to other devices on the NMEA 0183 network.

## R00 (\$GPR00) (Waypoint Arrival Alarm)

Provides information about the vessel's current route.

## RMA (\$GPRMA) - Recommended Minimum Navigation Information

The RMA command provides information about the GPS receiver's current position, speed, and course, as well as the current date and time.

Recommended Minimum Navigation Information. The attributes include:

* Talker ID: This is a 2 character identifier that indicates the source of the sentence.
* Status: This is a single character field that indicates the status of the navigation system. Possible values are "A" for valid and "V" for warning.
  Status of the position fix
  * A = Autonomous
  * D = Differential
  * E = Estimated
  * N = Not valid
  * S = Simulator
* Latitude: This is the latitude in decimal degrees, with the hemisphere being either "N" for north or "S" for south.
* Longitude: This is the longitude in decimal degrees, with the hemisphere being either "E" for east or "W" for west.
* Speed over ground: This is the speed of the vessel over the ground in knots.
* Course over ground: This is the direction of the vessel over the ground in degrees.
* Variation: This is the magnetic variation in degrees, with the direction being either "E" for east or "W" for west.
* Mode indicator: This is a single character field that indicates the mode of the navigation system. Possible values are "A" for autonomous, "D" for differential, and "E" for estimated.
* pos_mode: Mode of the position fix
  * 1 = Autonomous
  * 2 = Differential
  * 3 = Estimated
  * 4 = Manual Input
  * 5 = Simulated
* Checksum: This is a 2 character field that contains a checksum of the sentence to ensure its accuracy.

## RMB (\$GPRMB) - Recommended Minimum Navigation Information

Provides information about the GPS receiver's current position, speed, and course, as well as the current date and time.

The RMB (recommended minimum navigation information) message is a navigation sentence that provides information about the recommended navigation to a

The RMB (Recommended Minimum Navigation Information) sentence is one of the NMEA 0183 standard sentences used for navigation information. The RMB sentence provides navigation information such as the status of a route, the estimated time of arrival, cross-track error, and other related information.

The attributes of the RMB sentence include:

* Status: This field indicates the status of a route. It can be either "A" for active or "V" for void.
* Cross-Track Error (XTE): This field provides information about the cross-track error in nautical miles.
* Direction to Steer (DTW): This field provides information about the direction to steer to correct the cross-track error.
* Destination Waypoint ID: This field provides the ID of the destination waypoint.
* Destination Latitude: This field provides the latitude of the destination waypoint.
* Destination Longitude: This field provides the longitude of the destination waypoint.
* Range to Destination: This field provides the range in nautical miles to the destination waypoint.
* Bearing to Destination: This field provides the bearing in degrees to the destination waypoint.
* Destination Closing Velocity: This field provides the closing velocity in knots to the destination waypoint.
* Arrival Status: This field provides information about the arrival status at the destination waypoint. It can be either "A" for arrival or "V" for not arrived.
* Date: The date of the navigation information in the format DDMMYY.
* Magnetic variation: The magnetic variation at the destination waypoint in degrees and minutes.
* Mode indicator: The mode indicator for the navigation information.
  It can be one of the following:
  * 'A' (autonomous)
  * 'D' (differential)
  * 'E' (estimated)
  * 'M' (manual)
  * 'S' (simulator)

## RMC (\$GPRMC) - Recommended Minimum Specific GPS/Transit Data

Provides information about the GPS receiver's current position, speed, and course, as well as the current date and time. The RMC command is the most important command in the NMEA 0183 standard. It provides the most basic information about the vessel's position, speed, and course. It is also the only command that provides the current date and time. The RMC command is the only command that is required to be implemented by all GPS receivers.

The RMC command has the following attributes:

The attributes for the RMC command include:

* time: The time of the fix in UTC (Coordinated Universal Time).
* status: The status of the fix. It can be either "A" for active or "V" for void.
* latitude: The latitude of the fix in degrees and minutes.
* longitude: The longitude of the fix in degrees and minutes.
* speed: The speed of the vessel in knots.
* course: The course of the vessel in degrees True.
* date: The date of the fix in the format DDMMYY.
* magnetic variation: The magnetic variation at the fix in degrees and minutes.
* mode indicator: The mode indicator for the fix. It can be one of the following:
  * 'A' (autonomous)
  * 'D' (differential)
  * 'E' (estimated)
  * 'M' (manual)
  * 'S' (simulator)

## RMM (\$GPRMM) - Recommended Minimum Navigation Information

The RMM command is used to provide recommended navigation information. The attributes of this command include:

* mode_indicator: This is the operating mode of the electronic navigation equipment. It can be A for autonomous or D for differential.
* cross_track_error: This is the cross-track error, which is the difference between the actual and desired track, relative to the ship's current position. The value is measured in nautical miles.
* direction_to_steer: This attribute indicates the direction to steer to correct for the cross-track error. The value can be L for left or R for right.
* arrival_circle_entered: This attribute indicates whether the ship has entered an arrival circle, with A for arrived and V for not arrived.

## ROT (\$GPROT) - Rate of Turn

Provides information about the vessel's rate of turn.

The attributes of the ROT command are as follows:

* ROT: rate of turn, in degrees per minute
* status: status of the rate of turn
  * A = Data Valid
  * V = Data Invalid

The rate of turn value in the ROT command indicates the rate of change of the vessel's heading, with positive values indicating a turn to starboard (right) and negative values indicating a turn to port (left).

## RPM (\$GPRPM) - Revolutions

Provides information about the vessel's engine speed.
The RPM command consists of the following attributes:

* source: the source of the revolution data, represented as a single character
* direction: the direction of rotation, represented as either 'R' for right or 'L' for left
revolutions: the number of revolutions per minute
* status: the status of the revolution data, represented as either 'A' for valid or 'V' for invalid

## RSD (\$GPRSD) - RADAR System Data

Provides information about the vessel's radar system.

The attributes of the RSD command are as follows:

* range: the range of the radar system, in nautical miles
* bearing: the bearing of the radar system, in degrees
* range_resolution: the range resolution of the radar system, in nautical miles
* bearing_resolution: the bearing resolution of the radar system, in degrees
* range_units: the units of the range, represented as either 'N' for nautical miles or 'M' for meters
* bearing_units: the units of the bearing, represented as either 'D' for degrees or 'R' for radians

* sensor_id: The identifier of the radar sensor.
* data_valid: A Boolean value indicating if the data is valid.
* speed: The speed of the target relative to the ownship, in knots.
* course: The course of the target relative to the ownship, in degrees.
* range: The range of the target relative to the ownship, in nautical miles.
* bearing: The bearing of the target relative to the ownship, in degrees.

## RTE (\$GPRTE) - Routes

Provides information about the vessel's current route.

The RTE command has the following attributes:

* message_type: The type of NMEA 0183 message, which is always "$GPRTE".
* total_messages: The total number of RTE messages being transmitted.
* message_number: The current RTE message number.
* route_type: The type of route. This can be either "Active route" or "Waypoint list".
* route_waypoint_ids: A list of the waypoint IDs that make up the route.

## VDM (\$GPVDM) - VHF Data Link Message

Provides information about the vessel's VHF data link.

The attributes of the VDM command are:

* message_id: a 1-character field representing the type of the sentence.
* total_number_of_sentences: a 1-character field indicating the total number of sentences needed to transmit the entire message.
* sentence_number: a 1-character field indicating the sequence number of the current sentence.
* sequential_message_id: a 2-character field indicating the type of message being transmitted.
* data: a variable-length field that contains the actual message data.
* checksum: a 2-character field that contains a checksum of the sentence.

## VHW (\$GPVHW) - Water Speed and Heading

Provides information about the vessel's speed and heading.

The VHW command is used to indicate the vessel's heading and speed information. The following are the attributes of the VHW command:

* heading_degrees_true: This represents the vessel's heading in true degrees.
* speed_knots: This represents the vessel's speed in knots.
* speed_kph: This represents the vessel's speed in kilometers per hour.

## VLW (\$GPVLW) - Distance Traveled through Water

Provides information about the distance traveled through water.

The attributes of the NMEA 0183 VLW command are:

* Trip Log: The distance traveled since the log was last reset.
* Cumulative Log: The total distance traveled since the device was turned on.

## VTG (\$GPVTG) - Track Made Good and Ground Speed

Provides information about the vessel's course over ground (COG) and speed over ground (SOG).

The attributes of the VTG command are:

* True Track Made Good: The course made good by the vessel in degrees true.
* Magnetic Track Made Good: The course made good by the vessel in degrees magnetic.
* Ground Speed Knots: The ground speed of the vessel in knots.
* Ground Speed Km/h: The ground speed of the vessel in kilometers per hour.

## VWR (\$GPVWR) - Relative Wind Speed and Angle

Provides information about the vessel's relative wind speed and angle.

The VWR command provides information about wind speed and direction.

Attributes:

talker_id: 2 character identifier for the device sending the sentence.
sentence_id: 3 character identifier for the sentence type.
direction_of_wind: The wind direction in degrees relative to the true north.
speed: Wind speed in knots.
speed_unit: Unit of speed measurement, in this case "N" for knots.
reference_speed: Reference speed in knots.
reference_speed_unit: Unit of reference speed measurement, in this case "N" for knots.

## WCV (\$GPWCV) - Waypoint Closure Velocity

Provides information about the vessel's current route.

The WCV command includes the following attributes:

* speed: The speed towards a waypoint, in knots.
* speed_unit: The unit of the speed, always "N".
* waypoint_id: The ID of the waypoint being approached.
* status: A status character indicating the validity of the data, either "A" for valid or "V" for invalid.

## WNC (\$GPWNC) - Distance - Waypoint to Waypoint

Provides information about the vessel's current route.

The WNC command includes the following attributes:

* distance: The distance between two waypoints, in nautical miles.
* distance_unit: The unit of the distance, always "N".
* waypoint_id_1: The ID of the first waypoint.
* waypoint_id_2: The ID of the second waypoint.
* status: A status character indicating the validity of the data, either "A" for valid or "V" for invalid.

The attributes of the WNC command are as follows:

* Distance to waypoint (distance): the distance to a waypoint, in nautical miles.
* Waypoint to (waypoint_to): the identifier of the waypoint to navigate to.
* Waypoint from (waypoint_from): the identifier of the current waypoint.
* Bearing, true (bearing_true): the bearing to the waypoint, in degrees true.
* Bearing, magnetic (bearing_magnetic): the magnetic bearing to the waypoint, in degrees magnetic.
* Mode indicator (mode_indicator): indicates the operational mode of the device that transmitted the command. The value can be either 'A' (autonomous) or 'D' (differential).

## WPL (\$GPWPL) - Waypoint Location

Provides information about the vessel's current route.

Attributes of the WPL (Waypoint Location) command:

* latitude: Latitude of the waypoint in decimal degrees, North is positive
* longitude: Longitude of the waypoint in decimal degrees, East is positive
* waypoint_id: The identifier for the waypoint, encoded as a character string
* waypoint_name: The name of the waypoint, encoded as a character string

## WPT (\$GPWPT) - Waypoint Information

Provides information about the vessel's current route.

The attributes of the WPT command are:

* Latitude: The latitude of the waypoint, in degrees.
* Longitude: The longitude of the waypoint, in degrees.
* Name: The name of the waypoint.
* Waypoint ID: A unique identifier for the waypoint.

## XDR (Transducer Measurements)

Explanation of Attributes:

* transducer_type: Type of transducer (sensor) generating the measurement data.
* measurement_data: The actual measurement data generated by the transducer.
* unit_of_measurement: Unit of measurement for the measurement_data.
* name_of_transducer: The name or identifier of the transducer generating the measurement data.

## XTE (\$GPXTE) - Cross-Track Error - Measured

Provides information about the vessel's cross-track error.

The XTE class has the following attributes:

* status: The status of the XTE command, either "A" for active or "V" for void.
* cross_track_error_magnitude: The magnitude of the cross track error in nautical miles.
* direction_to_steer: The direction to steer, either "L" for left or "R" for right.
* cross_track_unit: The unit of the cross track error, either "N" for nautical miles or "K" for kilometers.

## ZDA (\$GPZDA) - Time & Date - UTC, day, month, year and local time zone

Provides information about the current date and time.

The ZDA command contains the following attributes:

* time: The time of the measurement in hhmmss format.
* day: The day of the month.
* month: The month of the year.
* year: The year.
* local_hour_offset: The hour offset from UTC, range from -12 to +12.
* local_minute_offset: The minute offset from UTC, range from 0 to 59.
