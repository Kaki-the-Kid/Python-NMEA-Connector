#using NmeaParser.Messages

# Helper class for monitoring GNSS messages and combine them into a single useful location info
class GnssMonitor():

    bool: m_supportGGaMessages = False # If device support GGA, ignore RMC for location
    m_allMessages = { str: key = "", str: NmeaMessage = None } # All messages received from the device
    
    object: m_lock = new object()
    bool: m_isLearning = True #Indicates that we still haven't seen a full round of location messages yet

    def GnssMonitor( NmeaDevice: device = None):
        if (device == None):
            raise Exception(device)
            
        _device = device
        _device.MessageReceived += NmeaMessageReceived
        SynchronizationContext = SynchronizationContext.Current

    # Gets or sets the syncronization context that <see cref="PropertyChanged"/> should be fired on
    # The default is the context this thread was created monitor was created on, but for use in UI applications, 
    # it can be beneficial to ensure this is the UI Thread. You can also set this to <c>null</c> for best performance
    @property
    def get_SynchronizationContext(self):
        return self._SynchronizationContext
    
    @setter.SynchronizationContext
    def set_SynchronizationContext(self, value):
        self._SynchronizationContext = value

    # Gets the NMEA device that is being monitored
    @property
    def get_device():
        return self.device

    def NmeaMessageReceived(object sender, NmeaParser.NmeaMessageReceivedEventArgs e):
        OnMessageReceived(e.Message)
        pass

    # Called when a message is received.
    # <param name="message">The NMEA message that was received</param>
    def OnMessageReceived(NmeaMessage message):
        bool:  isNewFix = False
        bool.  lostFix = False
        float: lat = 0.0
        float: lon = 0.0
        
        # Make a list of string called properties
        properties = [str]

        if (m_isLearning and message is IGeographicLocation and m_allMessages.ContainsKey(message.MessageType)):
            m_isLearning = false #We've received a full round of messages. Now start report locations
        
        def lock (m_lock):
            msgid = str( message.MessageType )
            if ( message is Gsv gsv and gsv.GnssSignalId != '0' ):
                msgid = msgid + "|" + gsv.GnssSignalId
                
                if (m_allMessages.ContainsKey(msgid) and m_allMessages[msgid].Equals(message)):
                    return #Nothing to update/notify
                
            m_allMessages[msgid] = message
        
        properties.Add(nameof(AllMessages))
        if(message.TalkerId != NmeaParser.Talker.GlobalNavigationSatelliteSystem and !(message is Gsv) and message.MessageType.Length > 2):
            #If device supports combined GN*** messages, ignore non-GN messages, except for Gsv
            if (m_allMessages.ContainsKey("GN" + message.MessageType.Substring(2))):
                pass
        
        if (message is NmeaParser.Messages.Garmin.Pgrme rme):
            if (rme.HorizontalError != HorizontalError)
                properties.Add(nameof(HorizontalError))
                HorizontalError = rme.HorizontalError
                
            if (rme.VerticalError != VerticalError):
                VerticalError = rme.VerticalError
                properties.Add(nameof(VerticalError))
                
        elif (message is Gst gst):
            Gst = gst
            properties.Add(nameof(Gst))
            
            var error = Math.Round(Math.Sqrt(Gst.SigmaLatitudeError * Gst.SigmaLatitudeError + Gst.SigmaLongitudeError * Gst.SigmaLongitudeError), 3)
            if (error != HorizontalError):
                HorizontalError = error
                properties.Add(nameof(HorizontalError))
                
            if (VerticalError != gst.SigmaHeightError):
                VerticalError = gst.SigmaHeightError
                properties.Add(nameof(VerticalError))
                
        elif (message is Rmc rmc):
        
            if (Speed != rmc.Speed)
                properties.Add(nameof(Speed))
                
            if (Course != rmc.Course)
                properties.Add(nameof(Course))
                
            Rmc = rmc
            properties.Add(nameof(Rmc))
            if (!m_supportGGaMessages):
                if (Rmc.Active):
                    lat = Rmc.Latitude
                    lon = Rmc.Longitude
                    
                    if (FixTime != Rmc.FixTime.TimeOfDay):
                        FixTime = Rmc.FixTime.TimeOfDay
                        properties.Add(nameof(FixTime))
                        
                    isNewFix = true
                else:
                    lostFix = true
        elif: (message is Dtm dtm):
            if (Dtm?.Checksum != dtm.Checksum):
                #Datum change
                Dtm = dtm
                properties.Add(nameof(Dtm))
                Latitude = double.NaN
                Longitude = double.NaN
                IsFixValid = false
                properties.Add(nameof(Dtm))
                properties.Add(nameof(Datum))
                properties.Add(nameof(Latitude))
                properties.Add(nameof(Longitude))
                properties.Add(nameof(IsFixValid))
        elif (message is Gga gga):
            if (gga.Hdop != Hdop):
                properties.Add(nameof(Hdop))
                
            if (gga.Quality != FixQuality):
                properties.Add(nameof(FixQuality))
                
            Gga = gga
            properties.Add(nameof(Gga))
            m_supportGGaMessages = true
            if (gga.Quality != Gga.FixQuality.Invalid):
                lat = gga.Latitude
                lon = gga.Longitude
                GeoidHeight = gga.GeoidalSeparation
                properties.Add(nameof(GeoidHeight))
                Altitude = gga.Altitude + gga.GeoidalSeparation # Convert to ellipsoidal height
                properties.Add(nameof(Altitude))
                
            if (gga.Quality == Gga.FixQuality.Invalid or gga.Quality == Gga.FixQuality.Estimated):
                lostFix = True
                
            if (FixTime != Gga.FixTime):
                FixTime = Gga.FixTime
                properties.Add(nameof(FixTime))
                
            isNewFix = True
        elif (message is Gsa gsa):
            if (gsa.Hdop != Hdop):
                properties.Add(nameof(Hdop))
                
            if (gsa.Pdop != Pdop):
                properties.Add(nameof(Pdop))
                
            if (gsa.Vdop != Vdop):
                properties.Add(nameof(Vdop))
                
            Gsa = gsa
            properties.Add(nameof(Gsa))
        elif (message is Vtg vtg):
            if (Speed != vtg.SpeedKnots):
                properties.Add(nameof(Speed))
                
            Vtg = vtg
            properties.Add(nameof(Vtg))
        elif (message is Gsv):
            properties.Add(nameof(Satellites))
            properties.Add(nameof(SatellitesInView))

        if (lostFix):
            if (!IsFixValid)
                IsFixValid = false
                properties.Add(nameof(IsFixValid))
                properties.Add(nameof(FixQuality))
                LocationLost?.Invoke(this, EventArgs.Empty)
        if (isNewFix):
            if (Latitude != lat):
                properties.Add(nameof(Latitude))
                Latitude = lat
                
            if (Longitude != lon):
                properties.Add(nameof(Longitude))
                Longitude = lon
                
            if (!IsFixValid):
                properties.Add(nameof(IsFixValid))
                if (Gga == null):
                    properties.Add(nameof(FixQuality))
                IsFixValid = true
                
            if (!m_isLearning):
                LocationChanged?.Invoke(this, EventArgs.Empty)
                
        if (properties.Count > 0):
            OnPropertyChanged(properties)

        pass

    # Gets a value indicating whether the current fix is valid.
    # If false the provided values like <see cref="Latitude"/> and 
    # <see cref="Longitude"/> are no longer current and reflect the last 
    # known location. <seealso cref="LocationLost"/>
    def bool IsFixValid { get private set }

    # Gets the latitude for the current or last known location.
    # <seealso cref="IsFixValid"/> 
    # <seealso cref="Longitude"/>
    def double Latitude { get private set } = double.NaN

    # Gets the longitude for the current or last known location.
    # <seealso cref="IsFixValid"/>
    # <seealso cref="Latitude"/>
    def double Longitude { get private set } = double.NaN

    # Gets the geight above the ellipsoid
    def double Altitude { get private set } = double.NaN
    # Gets the Geoid Height. Add this value to <see cref="Altitude"/> to get the 
    # Geoid heights which is roughly MSL heights.
    def double GeoidHeight { get private set } = double.NaN

    # Gets the speed in knots
    def double Speed => Rmc?.Speed ?? Vtg?.SpeedKnots ?? double.NaN

    # Gets the current cource
    def double Course => Rmc?.Course ?? double.NaN

    # Gets an estimate of the horizontal error in meters
    def double HorizontalError { get private set } = double.NaN

    # Gets an estimate of the vertical error in meters
    def double VerticalError { get private set } = double.NaN

    # Gets the horizontal dilution of precision
    def double Hdop => Gsa?.Hdop ?? Gga?.Hdop ?? double.NaN

    # Gets the 3D point dilution of precision
    def double Pdop => Gsa?.Pdop ?? double.NaN

    # Gets the vertical dilution of precision
    def double Vdop => Gsa?.Vdop ?? double.NaN

    # Gets the latest known GSA message.
    def Gsa? Gsa { get private set }

    # Gets the latest known GGA message.
    def Gga? Gga { get private set }

    # Gets the latest known RMC message.
    def Rmc? Rmc { get private set }

    # Gets the latest known GST message.
    def Gst? Gst { get private set }

    # Gets the latest known DTM message.
    def Dtm? Dtm { get private set }

    # Gets the latest known VTG message.
    def Vtg? Vtg { get private set }

    # Gets the current fix time
    def TimeSpan? FixTime { get private set }

    # Gets a list of satellite vehicles in the sky
    def IEnumerable<SatelliteVehicle> Satellites():
        return m_allMessages.Values.OfType<Gsv>().SelectMany(s => s.SVs).ToArray()

    # Gets the number of satellites in the sky
    def int SatellitesInView():
        return m_allMessages.Values.OfType<Gsv>().Sum(s => s.SatellitesInView)

    # Gets the quality of the current fix
    def Gga.FixQuality FixQuality => !IsFixValid ? Gga.FixQuality.Invalid : (Gga?.Quality ?? Gga.FixQuality.GpsFix)

    # Gets a list of all NMEA messages currently part of this location
    def IEnumerable<KeyValuePair<str, NmeaMessage>> AllMessages
        return m_allMessages.ToArray()

    # Gets a value indicating the current Datum being used.
    def str Datum():
        if (Dtm == null):
            return "WGS84"
        
        match (Dtm.ReferenceDatumCode):
            case "W84": return "WGS84"
            case "W72": return "WGS72"
            case "S85": return "SGS85"
            case "P90": return "PE90"
            case _: return Dtm.ReferenceDatumCode

    # Raised when a new location has been updated
    def event EventHandler? LocationChanged

    # Raised if location tracking was lost
    # <seealso cref="IsFixValid"/>
    def event EventHandler? LocationLost

    # Occurs when a property value changes.</summary>
    def event PropertyChangedEventHandler? PropertyChanged

    def void OnPropertyChanged(IEnumerable<str> properties):
        if (PropertyChanged == None):
            return
        
        if (SynchronizationContext != null):
            SynchronizationContext.Post((d) =>
            {
                foreach (str propertyName in (IEnumerable<str>)d)
                    PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(propertyName))
            }, properties)
        else:
            foreach (str propertyName in properties)
                PropertyChanged.Invoke(this, new PropertyChangedEventArgs(propertyName))
        
        pass


# Enumeration for the carrier used by the <see cref="NtripStream"/>
def Carrier(Enum):
    #  None / unknown
    None = 0,
    #  L1 wave
    L1 = 1,
    #  L1 and L2 waves
    L1L2 = 2,
