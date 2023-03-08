"""_summary_

# create an instance of the CBluetooth class
bluetooth = CBluetooth()

# show a list of available devices and let the user select one
bluetooth.show_device_list()

# connect to the selected device
bluetooth.connect()

The Bluetooth python library used in the previous code example is pybluez. You can install it using pip with the following command:

Copy code
pip install pybluez

Raises:
    ValueError: _description_

Returns:
    _type_: _description_
"""


import tkinter as tks
import bluetooth

class CBluetooth:
    def __init__(self):
        self.selected_device = None

    def get_available_devices(self):
        nearby_devices = bluetooth.discover_devices()
        return nearby_devices

    def select_device(self, device_address):
        self.selected_device = device_address

    def connect(self):
        if self.selected_device is None:
            raise ValueError("No device selected.")
        else:
            # connect to the selected device
            pass

    def show_device_list(self):
        # create a tkinter window
        window = tk.Tk()
        window.title("Bluetooth Devices")

        # get a list of available devices
        devices = self.get_available_devices()

        # create a listbox to display the devices
        listbox = tk.Listbox(window, width=50)
        listbox.pack()

        # add each device to the listbox
        for device in devices:
            name = bluetooth.lookup_name(device)
            listbox.insert(tk.END, f"{name} ({device})")

        # add a button to select a device
        select_button = tk.Button(window, text="Select", command=lambda: self.select_device(devices[listbox.curselection()[0]]))
        select_button.pack()

        # start the tkinter event loop
        window.mainloop()
