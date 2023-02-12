//  *******************************************************************************
//  *  Licensed under the Apache License, Version 2.0 (the "License");
//  *  you may not use this file except in compliance with the License.
//  *  You may obtain a copy of the License at
//  *
//  *  http://www.apache.org/licenses/LICENSE-2.0
//  *
//  *   Unless required by applicable law or agreed to in writing, software
//  *   distributed under the License is distributed on an "AS IS" BASIS,
//  *   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
//  *   See the License for the specific language governing permissions and
//  *   limitations under the License.
//  ******************************************************************************

namespace NmeaParser.Messages.Trimble
{
    /// <summary>
    /// Laser Range Burden finder
    /// </summary>
    [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Naming", "CA1704:IdentifiersShouldBeSpelledCorrectly", MessageId = "Ptnla")]
    [NmeaMessageType("PTNLA")]
    public class Ptnla : LaserRangeMessage
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="Ptnla"/> class.
        /// </summary>
        /// <param name="type">The message type</param>
        /// <param name="message">The NMEA message values.</param>
        public Ptnla(string type, string[] message) : base(type, message) { }
    }
    
    [TestMethod]
    public void TestPtlna()
    {
        string input = "$PTNLA,HV,002.94,M,288.1,D,008.6,D,002.98,M*74";
        var msg = NmeaMessage.Parse(input);
        Assert.IsInstanceOfType(msg, typeof(NmeaParser.Messages.Trimble.Ptnla));
        Assert.AreEqual(Talker.ProprietaryCode, msg.TalkerId);
        NmeaParser.Messages.Trimble.Ptnla ptlna = (NmeaParser.Messages.Trimble.Ptnla)msg;
        Assert.AreEqual(2.94, ptlna.HorizontalDistance);
        Assert.AreEqual('M', ptlna.HorizontalDistanceUnits);
        Assert.AreEqual(288.1, ptlna.HorizontalAngle);
        Assert.AreEqual('D', ptlna.HorizontalAngleUnits);
        Assert.AreEqual(8.6, ptlna.VerticalAngle);
        Assert.AreEqual('D', ptlna.VerticalAngleUnits);
        Assert.AreEqual(2.98, ptlna.SlopeDistance);
        Assert.AreEqual('M', ptlna.SlopeDistanceUnits);
    }
}


