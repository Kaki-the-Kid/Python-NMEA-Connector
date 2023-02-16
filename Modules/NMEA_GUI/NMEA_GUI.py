# ****************************************************************************//*
# @file     NMEA_GUI.py
# @brief    A tkinter gui for the NMEA class taking input for a NMEA0183 unit
#           and displaying the output in a tkinter window with a text widget
#           and a button to send the data to the NMEA class
#
# @author   Karsten Reitan Sørensen - karsten.reitan@gmail.com
# @date     16-02-2023 (d-m-y)
# @version  0.1-prototype (0.1)
# @note     This is a prototype and not a finished product
# ****************************************************************************//*

import config.config as config
import tkinter as tk
from tkinter import ttk
#from nmea_server import server, formatter
import Modules.NMEA_GUI.NMEA0183GUI as NMEA0183GUI
import Modules.NMEA_GUI.NMEA2000GUI as NMEA2000GUI



class NMEA_GUI(tk.Frame):        
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()


# This will create a window with two tabs named "NMEA0183" and "NMEA2000". You can add 
# your own widgets and functionality to each tab by modifying the code inside the 
# respective ttk.Frame widgets.


# In this code, we first import the tkinter module and the ttk (themed Tkinter) module 
# for the notebook widget. We then create the main window using the Tk() constructor 
# and set its title to "NMEA".

# Create the main window
root = tk.Tk()
root.geometry("800x600")
root.title("NMEA Connector - {}".WINDOW_NAME)

# Next, we create the ttk.Notebook widget to hold the tabs, and two ttk.Frame widgets for 
# the NMEA0183 and NMEA2000 tabs. We add the frames to the notebook using the add() method, 
# and set the text for each tab using the text parameter.

# Create a notebook with tabs
notebook = ttk.Notebook(root)

# Create the NMEA0183 tab
nmea0183_frame = ttk.Frame(notebook)
notebook.add(nmea0183_frame, text="NMEA0183")

# Create the NMEA2000 tab
nmea2000_frame = ttk.Frame(notebook)
notebook.add(nmea2000_frame, text="NMEA2000")

# Finally, we pack the notebook using the pack() method with the options expand=1 
# and fill="both" to make the notebook fill the entire window. We then start the 
# main loop using the mainloop() method of the Tk() object.

# Pack the notebook
notebook.pack(expand=1, fill="both")

# Start the main loop
root.mainloop()
