# ****************************************************************************//*
# @project  Python NMEA Connector
# @file     DSC.py
# @brief    Digital Selective Calling
# @author   Karsten Reitan Sørensen
# @date:     11-02-2023
# *******************************************************************************
# <remarks>
# <para>Navigation data from present position to a destination waypoint provided by a Loran-C, GNSS, DECCA, navigation computer
# or other integrated navigation system.</para>
# <para>
# This sentence always accompanies <see cref="Rma"/> and <see cref="Rmc"/> sentences when a destination is active when provided by a Loran-C or GNSS receiver,
# other systems may transmit <see cref="Rmb"/> without <see cref="Rma"/> or <see cref="Rmc"/>.
# </para>
# </remarks>

from NMEA0183_Commands import NMEA0183_Command as NMEAMessage


class RMB(NMEAMessage):
    
    def __init__(self, NMEAMessage=None):
        if (NMEAMessage == null or NMEAMessage.Length < 13):
            raise Exception("Invalid RMB: {}".NMEAMessage)

        # Data Status
        #public DataStatus Status { get; }
        self.status = ""
        Status = NMEAMessage[0] == DataStatus.Ok if "A" else Rmb.DataStatus.Warning

        # Cross-track error (steer left when negative, right when positive)
        #public double CrossTrackError { get; }
        self.cross_track_error = 0.0
        if ( double.TryParse(
                            NMEAMessage[1], 
                            NumberStyles.Float, 
                            CultureInfo.InvariantCulture, 
                            out tmp)
            ):
            CrossTrackError = tmp

            if (NMEAMessage[2] == "L"): #Steer left
                CrossTrackError = CrossTrackError * -1
        else:
            CrossTrackError = double.NaN
            
        
        self.direction_to_steer = ""
        
        # Origin waypoint ID
        #public double OriginWaypointId { get; }
        self.to_waypoint_id = ""
        if (NMEAMessage[3].Length > 0):
            OriginWaypointId = int.Parse(NMEAMessage[3], CultureInfo.InvariantCulture)
        
        # Destination waypoint ID
        #public double DestinationWaypointId { get; }
        if (NMEAMessage[3].Length > 0):
            DestinationWaypointId = int.Parse(NMEAMessage[4], CultureInfo.InvariantCulture)
        
        # Destination Latitude
        #public double DestinationLatitude { get; }
        self.destination_latitude = 0.0
        DestinationLatitude = NmeaMessage.StringToLatitude(NMEAMessage[5], NMEAMessage[6])
        
        # Destination Longitude
        #public double DestinationLongitude { get; }
        self.destination_longitude = 0.0
        DestinationLongitude = NmeaMessage.StringToLongitude(NMEAMessage[7], NMEAMessage[8])
        
        # Range to destination in nautical miles
        #public double RangeToDestination { get; }
        self.range_to_destination = 0.0
        if ( double.TryParse(
                        NMEAMessage[9], 
                        NumberStyles.Float, 
                        CultureInfo.InvariantCulture, 
                        out tmp
                        )
            ):
            RangeToDestination = tmp
        else:
            RangeToDestination = double.NaN
        
        # True bearing to destination
        #public double TrueBearing { get; }
        self.bearing_to_destination = 0.0
        if ( double.TryParse(
                        NMEAMessage[10], 
                        NumberStyles.Float, 
                        CultureInfo.InvariantCulture, 
                        out tmp
                        )
            ):
            TrueBearing = tmp
        else:
            TrueBearing = double.NaN
        
        # Velocity towards destination in knots
        #public double Velocity { get; }
        self.destination_closing_velocity = 0.0
        if ( double.TryParse(
                        NMEAMessage[11], 
                        NumberStyles.Float, 
                        CultureInfo.InvariantCulture, 
                        out tmp
                    )
            ):
            Velocity = tmp
        else:
            Velocity = double.NaN
        
        # Arrived (<c>true</c> if arrived)
        #public bool Arrived { get; }
        self.arrival_status = ""
        Arrived = NMEAMessage[12] == "A"
        
        
    def set_status(self, status):
        self.status = status

    def get_status(self):
        return self.status

    def set_cross_track_error(self, cross_track_error):
        self.cross_track_error = cross_track_error

    def get_cross_track_error(self):
        return self.cross_track_error

    def set_direction_to_steer(self, direction_to_steer):
        self.direction_to_steer = direction_to_steer

    def get_direction_to_steer(self):
        return self.direction_to_steer

    def set_to_waypoint_id(self, to_waypoint_id):
        self.to_waypoint_id = to_waypoint_id

    def get_to_waypoint_id(self):
        return self.to_waypoint_id

    def set_destination_latitude(self, destination_latitude):
        self.destination_latitude = destination_latitude

    def get_destination_latitude(self):
        return self.destination_latitude

    def set_destination_longitude(self, destination_longitude):
        self.destination_longitude = destination_longitude

    def get_destination_longitude(self):
        return self.destination_longitude

    def set_range_to_destination(self, range_to_destination):
        self.range_to_destination = range_to_destination

    def get_range_to_destination(self):
        return self.range_to_destination

    def set_bearing_to_destination(self, bearing_to_destination):
        self.bearing_to_destination = bearing_to_destination

    def get_bearing_to_destination(self):
        return self.bearing_to_destination

    def set_destination_closing_velocity(self, destination_closing_velocity):
        self.destination_closing_velocity = destination_closing_velocity

    def get_destination_closing_velocity(self):
        return self.destination_closing_velocity

    def set_arrival_status(self, arrival_status):
        self.arrival_status = arrival_status

    def get_arrival_status(self):
        return self.arrival_status

    # Recommended minimum navigation information
    
    # Data status
    def DataStatus(Enum):
        # Ok
        Ok,
        # Warning
        Warning,


        public void TestGprmb_Empty()
        {
            string input = "$GPRMB,A,,,,,,,,,,,,A,A*0B";
            var msg = NmeaMessage.Parse(input);
            Assert.IsInstanceOfType(msg, typeof(Rmb));
            Rmb rmb = (Rmb)msg;
            Assert.AreEqual(true, rmb.Arrived);
            Assert.AreEqual(double.NaN, rmb.CrossTrackError);
            Assert.AreEqual(double.NaN, rmb.DestinationLatitude);
            Assert.AreEqual(double.NaN, rmb.DestinationLongitude);
            Assert.AreEqual(0, rmb.DestinationWaypointId);
            Assert.AreEqual(0, rmb.OriginWaypointId);
            Assert.AreEqual(double.NaN, rmb.RangeToDestination);
            Assert.AreEqual(Rmb.DataStatus.Ok, rmb.Status);
            Assert.AreEqual(double.NaN, rmb.TrueBearing);
            Assert.AreEqual(double.NaN, rmb.Velocity);
        }

        [TestMethod]
        public void TestGprmb()
        {
            string input = "$GPRMB,A,0.66,L,003,004,4917.24,S,12309.57,W,001.3,052.5,000.5,V*3D";
            var msg = NmeaMessage.Parse(input);
            Assert.IsInstanceOfType(msg, typeof(Rmb));
            Rmb rmb = (Rmb)msg;
            Assert.AreEqual(Rmb.DataStatus.Ok, rmb.Status);
            Assert.AreEqual(-.66, rmb.CrossTrackError);
            Assert.AreEqual(3, rmb.OriginWaypointId);
            Assert.AreEqual(4, rmb.DestinationWaypointId);
            Assert.AreEqual(-49.287333333333333333, rmb.DestinationLatitude);
            Assert.AreEqual(-123.1595, rmb.DestinationLongitude);
            Assert.AreEqual(1.3, rmb.RangeToDestination);
            Assert.AreEqual(52.5, rmb.TrueBearing);
            Assert.AreEqual(.5, rmb.Velocity);
            Assert.AreEqual(false, rmb.Arrived);
        }
