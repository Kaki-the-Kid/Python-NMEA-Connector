"""
This code creates a GUI with a label, an entry widget, a button, and a text widget. The user can 
enter an NMEA sentence in the entry widget and click the "Parse" button to parse the NMEA sentence. 
The parsed data is then displayed in the text widget. In this example, the parser handles two types 
of NMEA sentences: $GPGGA and $GPRMC. The parsing of each sentence can be extended as needed.

sumary_line


Keyword arguments:
argument -- description
Return: return_description
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
 
 
import tkinter as tk

class NMEAGui:
    def __init__(self, master):
        self.master = master
        self.master.title("NMEA0183 Parser")

        self.nmea_input = tk.StringVar()

        self.input_label = tk.Label(self.master, text="NMEA Input:")
        self.input_label.grid(row=0, column=0, padx=5, pady=5)

        self.input_entry = tk.Entry(self.master, textvariable=self.nmea_input)
        self.input_entry.grid(row=0, column=1, padx=5, pady=5)

        self.parse_button = tk.Button(self.master, text="Parse", command=self.parse_nmea)
        self.parse_button.grid(row=0, column=2, padx=5, pady=5)

        self.output_text = tk.Text(self.master, height=10, width=40)
        self.output_text.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

    def parse_nmea(self):
        nmea_sentence = self.nmea_input.get()
        # Parse the NMEA sentence
        try:
            # Split the sentence into fields
            fields = nmea_sentence.split(',')
            if fields[0] == '$GPGGA':
                # Parse GPGGA sentence
                # ...
                self.output_text.insert(tk.END, "GPGGA Sentence Parsed\n")
            elif fields[0] == '$GPRMC':
                # Parse GPRMC sentence
                # ...
                self.output_text.insert(tk.END, "GPRMC Sentence Parsed\n")
            else:
                self.output_text.insert(tk.END, "Unsupported NMEA Sentence\n")
        except Exception as e:
            self.output_text.insert(tk.END, "Error: " + str(e) + "\n")

if __name__ == "__main__":
    root = tk.Tk()
    nmea_gui = NMEAGui(root)
    root.mainloop()


       /****************************************************************************
         * PGRME -
         * The following are Garmin proprietary sentences.
         * "P" denotes proprietary,
         * "GRM" is Garmin's manufacturer code, and
         * "M" or "Z" indicates the specific sentence type.
         *
         * Note that the PGRME sentence is not set if the output is set to NMEA 1.5 mode.
         *
         * $PGRME,15.0,M,45.0,M,25.0,M*1C
         *
         * where:
         *     15.0,M       Estimated horizontal position error in meters (HPE)
         *     45.0,M       Estimated vertical error (VPE) in meters
         *     25.0,M       Overall spherical equivalent position error
         ****************************************************************************/
       public void CommandGarminPGRME()
       {
           int i = 0;
           double outEstimatedHorizontalPositionError = double.Parse(this.CommandParts[i++]); // 15.0,M Estimated horizontal position error in meters(HPE) 
           char outEstimatedHorizontalPositionErrorUnit = char.Parse(this.CommandParts[i++]);
           double outEstimatedVerticalError = double.Parse(this.CommandParts[i++]); // 45.0,M Estimated vertical error(VPE) in meters
           char outEstimatedVerticalErrorUnit = char.Parse(this.CommandParts[i++]);
           double outOverallSphericalEquivalentPositionError = double.Parse(this.CommandParts[i++]); // 25.0,M Overall spherical equivalent position error
           char outOverallSphericalEquivalentPositionErrorUnit = char.Parse(this.CommandParts[i++]);
       }
