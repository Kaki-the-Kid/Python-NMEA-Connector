# NMEA 2000 Commands

NMEA 2000 is a communication standard used in marine electronics, such as GPS, sonar, and other navigation and positioning equipment. It defines a set of messages, or PGNs (Parameter Group Numbers), which are used to communicate different types of data between devices on the network.

## The NMEA 2000 Commands

Here's a full list of NMEA 2000 PGNs:

ISO Address Claim (PGN 60928)
ISO Request (PGN 59904)
ISO Command (PGN 60960)
Product Information (PGN 60945)
DC Electrical Power (PGN 126208)
Battery Status (PGN 127505)
Engine Parameters Rapid Update (PGN 126993)
Engine Parameters Dynamic (PGN 127488)
Propulsion System Information (PGN 128259)
Vessel Heading (PGN 127250)
Rate of Turn (PGN 127251)
Attitude (PGN 127257)
GNSS Position Data (PGN 129025)
GNSS DOPs (PGN 129539)
GNSS Satellites in View (PGN 129540)
Environmental Parameters (PGN 130311)
Wind Data (PGN 130306)
Depth Data (PGN 128267)
Water Temperature (PGN 130314)

## The NMEA 2000 Command Structure

Each NMEA 2000 command is a JSON object with the following structure:

```json
{
  "PGN": 0,
  "Priority": 0,
  "Source": 0,
  "Destination": 255,
  "Data": []
}
```

### PGN

The PGN is the Parameter Group Number, which is a unique identifier for each type of message. The PGN is a 16-bit integer, and is required for all NMEA 2000 commands.

### Priority

The Priority is a 3-bit integer that determines the priority of the message. The higher the priority, the more important the message is. The priority is required for all NMEA 2000 commands.

### Source

The Source is a 8-bit integer that identifies the source of the message. The source is required for all NMEA 2000 commands. The source is usually the device's unique ID.

### Destination

The Destination is a 8-bit integer that identifies the destination of the message. The destination is required for all NMEA 2000 commands. The destination is usually 255, which means that the message is broadcast to all devices on the network.

### Data

The Data is an array of 8-bit integers that contains the data to be sent. The data is required for all NMEA 2000 commands. The data is usually a list of bytes that are interpreted by the receiving device.

## The NMEA 2000 Command Examples
