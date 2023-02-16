import tkinter as tk

class NMEA2000GUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        pass
#         tk.Tk.__init__(self, *args, **kwargs)
#         self.title("NMEA 2000 Data")

#         self.text = tk.Text(self, wrap=tk.WORD, font=("TkDefaultFont", 12))
#         self.text.pack(fill=tk.BOTH, expand=True)

#         self.update_button = tk.Button(self, text="Update Data", command=self.update_data)
#         self.update_button.pack()

#     def update_data(self):
#         # Replace this with code to retrieve NMEA 2000 data
#         data = [
#             "Vessel Heading: 123.4 degrees",
#             "Rate of Turn: 2.3 degrees/second",
#             "Attitude: Roll: 1.2 degrees, Pitch: 3.4 degrees",
#         ]

#         self.text.delete("1.0", tk.END)
#         for line in data:
#             self.text.insert(tk.END, line + "\n")

# if __name__ == "__main__":
#     app = NMEA2000GUI()
#     app.mainloop()
