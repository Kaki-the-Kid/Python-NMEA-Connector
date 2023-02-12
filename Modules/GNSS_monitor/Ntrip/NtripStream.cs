#  Metadata on an NTRIP Data Stream
class NtripStream( NtripSource )
    def NtripStream(string[] d):

        Mountpoint = d[1];
        Identifier = d[2];
        Format = d[3];
        FormatDetails = d[4];
        if (int.TryParse(d[5], out int carrier))
            Carrier = (Carrier)carrier;
        else
        {

        }

        Network = d[7];
        CountryCode = d[8];
        Latitude = double.Parse(d[9], CultureInfo.InvariantCulture);
        Longitude = double.Parse(d[10], CultureInfo.InvariantCulture);
        SupportsNmea = d[11] == "1";
    }

    public string Mountpoint { get; }
    
    # Gets the unique identifier for the stream
    public string Identifier { get; }

    public string FormatDetails { get; }
    public Carrier Carrier { get; }
    
    public double Longitude { get; }
