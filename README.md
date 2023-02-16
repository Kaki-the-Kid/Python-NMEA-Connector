# Python-NMEA-Connector

Python version  Csharp-NMEA-Connector

## Wishlist

- [ ] NMEA0183→NMEA2000 software converter
- [ ] NMEA2000→NMEA0183 software converter

Objektorienteret NMEA2000-bibliotek til Teensy, ESP, Arduino, MBED og Rasberry type boards. Disse korttyper er blevet testet, men biblioteket kan også bruges i andre systemer ved at skrive kompatibel CAN-driver og indpakning til andre hw-specifikke funktioner.

Bibliotek giver dig nem måde at lave forskellige slags NMEA2000-busenheder som sensortransducere (batteri, temperatur, vind, motor osv.), NMEA2000 informationsskærme, NMEA2000→PC-interface (som Actisense NGT1), NMEA0183→NMEA2000 eller NMEA2000→NMEA2000→NMEA konverter.

Bibliotek opfylder NMEA 2000 obligatoriske funktioner og adfærd. Enheder, der bruger bibliotek, kan bestå NMEA2000-certificeringstests. Bibliotek har været brugt i flere kommercielle certificerede produkter.

## Feature wishlist

### Features

- Most common NMEA messages fully supported
  - GNSS: BOD, GGA, GLL, GNS, GSA, GST, GSV, RMB, RMA, RMB, RMC, RTE, VTG, ZDA
  - Garmin Proprietary: PGRME, PGRMZ
  - Trimble Laser Range Finder: PTNLA, PTNLB
  - TruePulse Laser Range Finder: PLTIT
- Automatic merging of multi-sentence messages for simplified usage.
- Extensible with custom NMEA messages see here
- Multiple input devices out of the box
  - System.IO.Stream (all platforms)
  - Emulation from NMEA log file (all platforms)
  - Serial Device: .NET Framework, .NET Core (Windows, Linux, Mac) and Windows Universal.
  - Bluetooth: Windows Universal and Android. .NET Core/.NET Framework is supported using the bluetooth device via the   SerialPortDevice.

## Requirements

- tzlocal
- pytz
- flask
- requests
- blinkt
- pillow
- unicornhat
- unicornhathd
- numpy

## Referencer og kilder

<https://github.com/ttlappalainen/NMEA2000>

## Installation

### Requirements

- Python 3.6 or later
- nmeaserver nmea-0.1.4 
- numpy-1.24.2

# NMEA Server

Using the NMEA Server, you can connect to a NMEA 0183 device and send the data to a NMEA 2000 network. The NMEA Server is a Python application that runs on a Raspberry Pi or other Linux computer. It uses the NMEA 2000 library to send the data to the NMEA 2000 network. The NMEA Server can be used to connect to a NMEA 0183 device that does not have a NMEA 2000 interface. The NMEA Server can also be used to connect to a NMEA 0183 device that has a NMEA 2000 interface, but does not support the NMEA 2000 network that you want to connect to.

Reference: https://pypi.org/project/nmea/

## Module Installation

```bash 
pip install nmea
``` 

## Usage

```python
from nmea import server, formatter

# Creates a nmeaserver
nmeaserver = server.NMEAServer()

# Create a message handler that receives all messages with the sentence ID: 'RXTST'
@nmeaserver.message('RXTST')
def tst_handler(self, context, message):
    return formatter.format('TXTST,Message Received!')

# Starts the server
nmeaserver.start()
```
