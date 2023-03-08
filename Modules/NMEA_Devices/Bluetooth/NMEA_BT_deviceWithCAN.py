"""_summary_

# create an instance of the CBluetooth class
bluetooth = CBluetooth()

# show a list of available devices and let the user select one
bluetooth.show_device_list()

# connect to the selected device
bluetooth.connect()

The Bluetooth python library used in the previous code example is pybluez. You can install it using pip with the following command:

# send a CAN message
bluetooth.send_message(0x123, [0x01, 0x02, 0x03])

# receive a CAN message
message = bluetooth.receive_message()
print(message)

Copy code
pip install pybluez
pip install python-can-bluetooth==0.1.1

Raises:
    ValueError: _description_

Returns:
    _type_: _description_
"""


import tkinter as tk
import can
from can.interfaces.bluetooth import BluetoothSocketCAN

class CBluetooth:
    def __init__(self):
        self.selected_device = None
        self.bus = None

    def get_available_devices(self):
        # get a list of available Bluetooth devices
        nearby_devices = BluetoothSocketCAN.find_devices()
        return nearby_devices

    def select_device(self, device_address):
        self.selected_device = device_address

    def connect(self):
        if self.selected_device is None:
            raise ValueError("No device selected.")
        else:
            # create a BluetoothSocketCAN connection to the selected device
            bt_socket = BluetoothSocketCAN(self.selected_device)
            bt_socket.connect()

            # create a CAN bus on the BluetoothSocketCAN connection
            self.bus = can.interface.Bus(channel=None, bustype='bluetooth', socketcan=bt_socket)

    def send_message(self, message_id, data):
        # create a CAN message and send it on the bus
        message = can.Message(arbitration_id=message_id, data=data)
        self.bus.send(message)

    def receive_message(self):
        # receive a CAN message from the bus
        message = self.bus.recv()
        return message

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
            name = device[1]
            listbox.insert(tk.END, f"{name} ({device[0]})")

        # add a button to select a device
        select_button = tk.Button(window, text="Select", command=lambda: self.select_device(devices[listbox.curselection()[0]][0]))
        select_button.pack()

        # start the tkinter event loop
        window.mainloop()
