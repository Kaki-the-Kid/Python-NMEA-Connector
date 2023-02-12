# Laser Range Measurement


class LaserRangeMessage( NMEAMessage ):

    def LaserRangeMessage( self, sentence ):
        sentence = sentence.split( ',' )
        if (sentence == null or sentence.Length < 9):
            raise Exception("Invalid Laser Range Message", "sentence")
        
        self._HorizontalVector        = sentence[0]
        self._HorizontalDistance      = float(sentence[1], CultureInfo.InvariantCulture)
        self._HorizontalDistanceUnits = sentence[2][0]
        self._HorizontalAngle         = float(sentence[3], CultureInfo.InvariantCulture)
        self._HorizontalAngleUnits    = sentence[4][0]
        self._VerticalAngle           = float(sentence[5], CultureInfo.InvariantCulture)
        self._VerticalAngleUnits      = sentence[6][0]
        self._SlopeDistance           = float(sentence[7], CultureInfo.InvariantCulture)
        self._SlopeDistanceUnits      = sentence[8][0]


    # Gets the horizontal vector.
    def HorizontalVector():
        return self._HorizontalVector

    #  Gets the horizontal distance.
    #  Gets the units of the <see cref="HorizontalDistance"/> value.
    def HorizontalDistanceUnits():
        return self._HorizontalDistanceUnits
        
    #  Gets the horizontal angle.
    def HorizontalAngle():
        return self._HorizontalAngle

    #         #  Gets the units of the <see cref="HorizontalAngle"/> value.
    def HorizontalAngleUnits():
        return self._HorizontalAngleUnits

    #  Gets the vertical angle.
    def VerticalAngle():
        return self._VerticalAngle

    #  Gets the units of the <see cref="VerticalAngle"/> value.
    def VerticalAngleUnits():
        return self._VerticalAngleUnits

    #  Gets the slope distance.
    def SlopeDistance():
        return self._SlopeDistance

    #  Gets the units of the <see cref="SlopeDistance"/> value.
    def SlopeDistanceUnits():
        return self._SlopeDistanceUnits
