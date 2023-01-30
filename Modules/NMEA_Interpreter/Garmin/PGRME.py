"""
//  *******************************************************************************
//  *  Licensed under the Apache License, Version 2.0 (the "License");
//  *  you may not use this file except in compliance with the License.
//  *  You may obtain a copy of the License at
//  *
//  *  http://www.apache.org/licenses/LICENSE-2.0
//  *
//  *   Unless required by applicable law or agreed to in writing, software
//  *   distributed under the License is distributed on an "AS IS" BASIS,
//  *   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
//  *   See the License for the specific language governing permissions and
//  *   limitations under the License.
//  ******************************************************************************
"""

#  Recommended Minimum

[System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Naming", "CA1704:IdentifiersShouldBeSpelledCorrectly", MessageId = "Pgrme")]
[NmeaMessageType("PGRME")]

class Pgrme( NmeaMessage ):

	# Initializes a new instance of the <see cref="Pgrme"/> class.
	# <param name="type">The message type</param>
	# <param name="message">The NMEA message values.</param>
	# init string array	

	
	def Pgrme( type: str, message): 
		super( type, message )
	
		if ( message == None or message.Length < 6 ):
			print("Invalid PGRME", "message")
		
		HorizontalError      = float(message[0])
		HorizontalErrorUnits = message[1]
		VerticalError        = float(message[2])
		VerticalErrorUnits   = message[3]
		SphericalError       = float(message[4])
		SphericalErrorUnits  = message[5]

	# Estimated horizontal position error in meters (HPE)
	# <remarks>Range: 0.0 to 999.9 meters</remarks>
	def HorizontalError():
		get: float = 0.0

	# Horizontal Error unit ('M' for Meters)
	def HorizontalErrorUnits():
		get: str = ""

	# Estimated vertical position error in meters (VPE)
	# <remarks>Range: 0.0 to 999.9 meters</remarks>
	def VerticalError():
		get: float = 0.0

	# Vertical Error unit ('M' for Meters)
	def VerticalErrorUnits():
		get: str = ""

	# Overall spherical equivalent position error (EPE)
	# <remarks>Range: 0.0 to 999.9 meters</remarks>
	def SphericalError():
		get: float = 0.0

	# Spherical Error unit ('M' for Meters)
	def SphericalErrorUnits():
		get: str = ""
 