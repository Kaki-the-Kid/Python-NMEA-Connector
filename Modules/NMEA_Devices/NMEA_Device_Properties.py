class DeviceProperties():
    __init__(self, device):
        self.device = device
        self.device_name = device.name
        self.device_type = device.type
        self.device_port = device.port
        self.device_baudrate = device.baudrate
        self.device_parity = device.parity
        self.device_stopbits = device.stopbits
        self.device_bytesize = device.bytesize
        self.device_timeout = device.timeout
        self.device_xonxoff = device.xonxoff
        self.device_rtscts = device.rtscts
        self.device_dsrdtr = device.dsrdtr
        self.device_write_timeout = device.write_timeout
        self.device_inter_byte_timeout = device.inter_byte_timeout
        
    def get_device_name(self):