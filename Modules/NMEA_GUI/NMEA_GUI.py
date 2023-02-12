# a tkinter gui for the NMEA class taking input for a NMEA0183 unit
# and displaying the output in a tkinter window with a text widget  
# and a button to send the data to the NMEA class   
#   

import tkinter as tk
#import NMEA

class NMEA_GUI(tk.Frame):        
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        self.nmea = NMEA.NMEA()
        
    ""
    def createWidgets(self):
        self.text = tk.Text(self, height=20, width=80)
        self.text.pack()
        self.text.insert(tk.END, "NMEA0183 data goes here")         # insert some text into the text widget
        self.send = tk.Button(self) 
        self.send["text"] = "Send"
        self.send["command"] = self.sendData
        self.send.pack(side="top")
        self.quit = tk.Button(self, text="QUIT", fg="red",
                                command=root.destroy)
        self.quit.pack(side="bottom")

    def sendData(self):
        self.nmea.parse(self.text.get("1.0", tk.END))           # get the text from the text widget and send it to the NMEA class       
        
root = tk.Tk()                  
app = NMEA_GUI(master=root)
app.mainloop()
root.destroy()

# Path: Modules\NMEA_Interpreter\NMEA_Interpreter.py
# Compare this snippet from Modules\NMEA_Interpreter\NMEA_Interpreter.py:
#   



           import tkinter as tk

class NMEAGui:
    def __init__(self, master):
        self.master = master
        self.master.title("NMEA0183 GUI")

        self.nmea_input = tk.StringVar()

        self.input_label = tk.Label(self.master, text="NMEA Input:")
        self.input_label.grid(row=0, column=0, padx=5, pady=5)

        self.input_entry = tk.Entry(self.master, textvariable=self.nmea_input)
        self.input_entry.grid(row=0, column=1, padx=5, pady=5)

        self.send_button = tk.Button(self.master, text="Send", command=self.send_nmea)
        self.send_button.grid(row=0, column=2, padx=5, pady=5)

        self.output_text = tk.Text(self.master, height=10, width=40)
        self.output_text.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

    def send_nmea(self):
        nmea_data = self.nmea_input.get()
        # Call the NMEA class to process the NMEA data
        # ...
        # Update the output text widget with the processed NMEA data
        self.output_text.insert(tk.END, nmea_data)

if __name__ == "__main__":
    root = tk.Tk()
    nmea_gui = NMEAGui(root)
    root.mainloop()
 import tkinter as tk

class NMEA2000Display(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("NMEA 2000 Data")

        self.text = tk.Text(self, wrap=tk.WORD, font=("TkDefaultFont", 12))
        self.text.pack(fill=tk.BOTH, expand=True)

        self.update_button = tk.Button(self, text="Update Data", command=self.update_data)
        self.update_button.pack()

    def update_data(self):
        # Replace this with code to retrieve NMEA 2000 data
        data = [
            "Vessel Heading: 123.4 degrees",
            "Rate of Turn: 2.3 degrees/second",
            "Attitude: Roll: 1.2 degrees, Pitch: 3.4 degrees",
        ]

        self.text.delete("1.0", tk.END)
        for line in data:
            self.text.insert(tk.END, line + "\n")

if __name__ == "__main__":
    app = NMEA2000Display()
    app.mainloop()
