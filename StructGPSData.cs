namespace NMEA_connector
{
    public struct StructGPSData
    {
        /** 181908.00 is the time stamp: UTC time in hours, minutes and seconds.*/
        public string GPSTimestamp { get; set; }
        public int    GPSLatitudeDegree { get; set; }       // Latitude in the DDMM.MMMMM format.Decimal places are variable. N denotes north latitude.
        public double GPSLatitudeMins { get; set; }         //
        public string GPSLatitudeDirection { get; set; }    //
        public string GPSLatitudeString { get; set; }
        public int    GPSLongitudeDegree { get; set; }      // 07044.3966270 is the longitude in the DDDMM.MMMMM format. Decimal places are variable. W denotes west longitude.
        public double GPSLongitudeMins { get; set; }        //
        public string GPSLongitudeDirection { get; set; }   //
        public string GPSLongitudeString { get; set; }      //
        public int    GPSQuality { get; set; }              // denotes the Quality Indicator:
        public string GPSQualityText { get; set; }
        public int    GPSNumberSatelites { get; set; }      // 13 denotes number of satellites used in the coordinate.
        public double GPSHdop { get; set; }                 // 1.00 denotes the HDOP (horizontal dilution of precision).
        public double GPSAntenneAltitude { get; set; }      // 495.144 denotes altitude of the antenna.
        public string GPSAntennaAltitudemf { get; set; }    // M denotes units of altitude(eg.Meters or Feet)
        public double GPSGeoidalSeparation { get; set; }    // 29.200 denotes the geoidal separation(subtract this from the altitude of the antenna to arrive at the Height Above Ellipsoid (HAE).
        public string GPSGeoidalSeparationmf { get; set; }  // M denotes the units used by the geoidal separation.
        public double GPSAgeCorrection { get; set; }        // 1.0 denotes the age of the correction (if any).
        public string GPSStationId { get; set; }            // 0000 denotes the correction station ID(if any).
        public string GPSLastChecksum { get; set; }         // *40 denotes the checksum.
    }
}