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
