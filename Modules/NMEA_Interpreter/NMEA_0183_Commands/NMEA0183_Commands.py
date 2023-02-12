# Tabel 1. Send
# Sætning Beskrivelse
# DSC Oplysninger om digitalt selektivt opkald (DSC)
# DSE Udvidet digitalt selektivt opkald
# VDM (kun AIS modeller) AIS VHF datalink-besked

#Tabel 2. Modtag
# Sætning Beskrivelse
# DTM Datumreference
# GGA Global Positioning System-datarettelse
# GLL Geografisk position (breddegrad/længdegrad)
# GNS GNSS datarettelse
# RMA Anbefalet minimum for specifikke Loran-C-data
# RMC Anbefalet minimum for specifikke GNSS data
# VTG Kurs og hastighed over jorden

from datetime import timedelta
from BOD import BOD

class NMEA0183_Command():
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
     
    
    
    def send(self, command: str, data: str) -> str:
        return f"{command},{data}"      
    
    def receive(self, data: str) -> str:
        return data
    
    def checksum(self, data: str) -> str:
        return data 
    
    def validate(self, data: str) -> bool:
        return True
    
    def parse(self, data: str) -> str:
        return data
    
    def __str__(self) -> str:
        return f"NMEA0183_Command"
    
    def __str__(self):
        return self.message
    
    def __repr__(self) -> str:
        return f"NMEA0183_Command()"

    def __repr__(self):
        return self.message
    
    def GGAMessage(self):
        return self.gga
    
    def GGAMessage(self):
        return self.gga
        
    def RMCMessage(self):
        return self.rmc
    
    def VTGMessage(self):
        return self.vtg
    

    def StringToTimeSpan(span):
        # span = "40:00"
        # ts = StringToTimeSpan(span)
        # print(ts)
        # print(f"{int(ts.total_seconds() # 3600)}:{int(ts.total_seconds() % 3600 # 60):02d}")

        # ts1 = timedelta.fromisoformat("05:30")
        # print((ts - ts1).total_seconds() / 3600)
        ts = timedelta(hours=int(span.split(":")[0]), minutes=int(span.split(":")[1]))
        return ts

    # @returns A System.Collections.Generic.IEnumerator{T} that can be used to iterate through the collection.</returns>
    #def IEnumerator<str> IEnumerable<str>.GetEnumerator()
    #    foreach (str waypoint in Waypoints)
    #        yield return waypoint