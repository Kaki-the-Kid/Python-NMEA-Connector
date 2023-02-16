# Path: Modules\NMEA_Interpreter\NMEA_Interpreter.py
# Compare this snippet from Modules\NMEA_Interpreter\NMEA_Interpreter.py:
#   

# import tkinter as tk

class NMEA0183GUI:
    def __init__(self, master):
        self.master.title("NMEA0183 GUI")
        
        self.createWidgets()
        #self.nmea = NMEA.NMEA()
        

    def sendData(self):
        self.nmea.parse(self.text.get("1.0", tk.END))           # get the text from the text widget and send it to the NMEA class       


#         self.nmea_input = tk.StringVar()

#         self.input_label = tk.Label(self.master, text="NMEA Input:")
#         self.input_label.grid(row=0, column=0, padx=5, pady=5)

#         self.input_entry = tk.Entry(self.master, textvariable=self.nmea_input)
#         self.input_entry.grid(row=0, column=1, padx=5, pady=5)

#         self.send_button = tk.Button(self.master, text="Send", command=self.send_nmea)
#         self.send_button.grid(row=0, column=2, padx=5, pady=5)

#         self.output_text = tk.Text(self.master, height=10, width=40)
#         self.output_text.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

#     def send_nmea(self):
#         nmea_data = self.nmea_input.get()
#         # Call the NMEA class to process the NMEA data
#         # ...
#         # Update the output text widget with the processed NMEA data
#         self.output_text.insert(tk.END, nmea_data)

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

# if __name__ == "__main__":
#     root = tk.Tk()
#     nmea_gui = NMEA0183GUI(root)
#     root.mainloop()
