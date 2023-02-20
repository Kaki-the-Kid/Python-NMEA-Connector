#!/usr/bin/python
# -*- coding: utf-8 -*-

#[SOFTWARE]
SOFTWARE_VERSION   = "0.1.0-prototype"
WINDOW_NAME        = "NMEA Suite - " + SOFTWARE_VERSION

#[NMEA0183]
NMEA0183_VERSION   = "0.1.0"

NMEA0183_DEVICE    = "/dev/ttyUSB0"
NMEA0183_BAUDRATE  = 4800
NMEA0183_DATA_BITS = 8
NMEA0183_PARITY    = "None"
NMEA0183_STOP_BITS = 1
NMEA0183_HANDSHAKE = "None"

NMEA0183_LOG_LEVEL = "DEBUG"
NMEA0183_LOG_FILE  = "/logs/nmea0183.log"


#[NMEA2000]
N2K_VERSION        = "4.1"

N2K_DEVICE         = "/dev/ttyUSB0"
N2K_BAUDRATE       = 250000             #115200
N2K_DATA_BITS      = 8
N2K_PARITY         = "None"
N2K_STOP_BITS      = 1
N2K_HANDSHAKE      = "None"

N2K_LOG_LEVEL = "DEBUG"
N2K_LOG_FILE  = "/logs/N2K.log"


#[Hardware]
ARDUINO = "0.1.0"