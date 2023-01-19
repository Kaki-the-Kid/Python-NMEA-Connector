class NMEAMessage(object):
    def __init__(self, message):
        self.message = message
        self.message_type = message[3:6]
        self.message_data = message[7:]
        self.message_data = self.message_data.split(',')
        self.message_data = [x.strip() for x in self.message_data]
        self.message_data = [x.strip('*') for x in self.message_data]
        self.message_data = [x.strip() for x in self.message_data]
        self.message_data = [x.strip('\'') for x in self.message_data]
        
        if self.message_type == 'GGA':
            self.gga = GGA(self.message_data)
        elif self.message_type == 'RMC':
            self.rmc = RMC(self.message_data)
        elif self.message_type == 'VTG':
            self.vtg = VTG(self.message_data)
        elif self.message_type == 'GSA':
            self.gsa = GSA(self.message_data)
        elif self.message_type == 'GSV':
            self.gsv = GSV(self.message_data)
        elif self.message_type == 'GLL':
            self.gll = GLL(self.message_data)
        elif self.message_type == 'ZDA':
            self.zda = ZDA(self.message_data)
        elif self.message_type == 'PGRME':
            self.pgrme = PGRME(self.message_data)
        elif self.message_type == 'PGRMZ':
            self.pgrmz = PGRMZ(self.message_data)
        elif self.message_type == 'PGRMM':
            self.pgrmm = PGRMM(self.message_data)
        elif self.message_type == 'PGRME':
            self.pgrme = PGRME(self.message_data)
        else:
            print('Unknown message type: {}'.format(self.message_type))
            
    def __str__(self):
        return self.message
    
    def __repr__(self):
        return self.message
    
        
                
            
        
        
        
    
    