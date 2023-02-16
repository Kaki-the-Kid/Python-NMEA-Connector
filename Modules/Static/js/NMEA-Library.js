/*
<div style="margin:1em; padding: 2em; background: #ddddff;">
    <form onsubmit="document.getElementById('commandfld').select(); return false;">
        <table>
            <tbody>
                <tr><th align="right">Command:</th><td><tt>$<input id="commandfld" type="text" onchange="updateChecksum(this.value);" value="PFEC,GPint,RMC05">*</tt></td></tr>
                <tr><th align="right">With checksum:</th><td><span id="output" style="font-family: monospace;">$PFEC,GPint,RMC05*2D</span></td></tr>
            </tbody>
        </table>
    </form>
</div>
*/

<
script > updateChecksum(document.getElementById("commandfld").value); < /script>

<
script > <!--

    // Compute the MTK checksum and display it
    function updateChecksum(cmd) {
        // Compute the checksum by XORing all the character values in the string.
        var checksum = 0;
        for (var i = 0; i < cmd.length; i++) {
            checksum = checksum ^ cmd.charCodeAt(i);
        }

        // Convert it to hexadecimal (base-16, upper case, most significant nybble first).
        var hexsum = Number(checksum).toString(16).toUpperCase();
        if (hexsum.length < 2) {
            hexsum = ("00" + hexsum).slice(-2);
        }

        // Display the result
        settext(document.getElementById("output"), "$" + cmd + "*" + hexsum);
    }

// Helper function to set the contents of the SPAN to some text
function settext(span, text) {
    if (!span.hasChildNodes()) {
        span.appendChild(span.ownerDocument.createTextNode(text));
        return;
    } else {
        span.firstChild.nodeValue = text;
    }
}

-->
< /script>