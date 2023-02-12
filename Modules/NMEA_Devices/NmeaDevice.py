 class NmeaDevice():

    private readonly object m_lockObject = new object()
    private string m_message = ""
    private Stream? m_stream
    private CancellationTokenSource? m_cts
    private bool m_isOpening
    private Task? m_ParserTask


    def NmeaDevice(): pass


    # A task that represents the asynchronous action.
    def Task OpenAsync():
        lock (m_lockObject)
        {
            if (IsOpen or m_isOpening): return
            m_isOpening = true
        }

        m_cts = new CancellationTokenSource()
        m_stream = await OpenStreamAsync()
        StartParser(m_cts.Token)
        _lastMultiMessage = None

        lock (m_lockObject)
        {
            IsOpen = true
            m_isOpening = false
        }


    def StartParser(CancellationToken token):
        System.Diagnostics.Debug.WriteLine("Starting parser...")
        m_ParserTask = Task.Run(async () =>
        {
            byte[] buffer = new byte[1024]
            while (!token.IsCancellationRequested)
            {
                int readCount = 0
                try
                {
                    readCount = await ReadAsync(buffer, 0, 1024, token).ConfigureAwait(false)
                }
                catch { }
                if (token.IsCancellationRequested)
                    break
                if (readCount > 0)
                {
                    OnData(buffer, readCount)
                }
                await Task.Yield()
            }
        })
        pass

    # <param name="offset">The byte offset in buffer at which to begin writing data from the stream.</param>
    # <param name="count">The maximum number of bytes to read.</param>
    # <param name="cancellationToken">The token to monitor for cancellation requests. The default value is System.Threading.CancellationToken.None.</param>
    # <returns>
    # A task that represents the asynchronous read operation. The value of the TResult
    # parameter contains the total number of bytes read into the buffer. The result
    # value can be less than the number of bytes requested if the number of bytes currently
    # available is less than the requested number, or it can be 0 (zero) if the end
    # of the stream has been reached.
    # </returns>
    protected virtual Task<int> ReadAsync(byte[] buffer, int offset, int count, CancellationToken cancellationToken)
    {
        if (m_stream == None)
            return Task.FromResult(0)
        return m_stream.ReadAsync(buffer, 0, 1024, cancellationToken)
    }

    # protected abstract Task<Stream> OpenStreamAsync()
    # Closes the device.
    if (m_cts != None):
        {
            if (m_cts != None)
                m_cts.Cancel()
            m_cts = None
        }
        if (m_ParserTask != None && !m_ParserTask.IsCompleted)
        {
            await m_ParserTask
            /*try
            {
                await m_ParserTask.ConfigureAwait(false)
            }
            catch { } #Ignore any exit errors*/
        }
        if (m_stream != None)
            await CloseStreamAsync(m_stream).ConfigureAwait(false)
        _lastMultiMessage = None
        m_stream = None
        lock (m_lockObject)
        {
            m_isOpening = false
            IsOpen = false
        }
    }

s
    private void OnData(byte[] data, int count)
    {
        var nmea = System.Text.Encoding.UTF8.GetString(data, 0, count)
        List<string> lines = new List<string>()
        lock (m_lockObject)
        {
            m_message += nmea

            var lineEnd = m_message.IndexOf("\n", StringComparison.Ordinal)
            while (lineEnd > -1)
            {
                string line = m_message.Substring(0, lineEnd).Trim()
                m_message = m_message.Substring(lineEnd + 1)
                if (!string.IsNoneOrEmpty(line))
                    lines.Add(line)
                lineEnd = m_message.IndexOf("\n", StringComparison.Ordinal)
            }
        }
        foreach(var line in lines)
            ProcessMessage(line)
    }

    private IMultiSentenceMessage? _lastMultiMessage


    def void ProcessMessage(string p):
        try:
            if (p.Length == 0 || p[0] != '$'):
                return

            msg = NmeaMessage.Parse(p, _lastMultiMessage)

            if(msg is IMultiSentenceMessage multi):
                if (!multi.IsComplete):
                    _lastMultiMessage = multi //Keep it around until next time
                    return

            _lastMultiMessage = None
            if (msg != None):
                OnMessageReceived(msg)
        catch: pass

        pass


    private void OnMessageReceived(NmeaMessage msg)
    {
        if (msg == None)
            return

        MessageReceived?.Invoke(this, new NmeaMessageReceivedEventArgs(msg))
    }

    //private readonly Dictionary<string, Dictionary<int, Nmea.NmeaMessage>> MultiPartMessageCache = new Dictionary<string,Dictionary<int,Nmea.NmeaMessage>>()

    #         #         #         public event EventHandler<NmeaMessageReceivedEventArgs>? MessageReceived
#         #         public void Dispose()
    {
        Dispose(true)
        GC.SuppressFinalize(this)
    #
    #         #         #         #                 if (m_cts != None)
            {
                m_cts.Cancel()
                m_cts = None
            }
            CloseStreamAsync(m_stream)
            if (disposing && m_stream != None)
                m_stream.Dispose()
            m_stream = None
        }
    }

    #         # Gets a value indicating whether this device is open.
    #         # #         #         # Gets a value indicating whether this device supports writing
    # </summary>
    # <seealso cref="WriteAsync(byte[], int, int)"/>
    public virtual bool CanWrite { get => false }

    #         #         # Check the <see cref="CanWrite"/> property before calling this method.
    #         #         #         # <param name="length">The number of bytes to write.</param>
    #         #         #         {
        if (m_stream is None)
            throw new InvalidOperationException("Device not opened")
        if (!m_stream.CanWrite)
            throw new NotSupportedException()
        return m_stream.WriteAsync(buffer, offset, length)
    }


#     #     # </summary>
public sealed class NmeaMessageReceivedEventArgs : EventArgs
#     #     #             Message = message
# #         #     #         //#         # <val#         # The nmea message.
    # </value>
    public N#     }# }#
# 		#*****# 		# @bri# 		#
    # This function initializes the array @ref Devices with the size of
    # @ref DeviceCount and sets default device information.
    #
    # Default Device Info is:
    #  - Unique ID = Device Index +1 ==> 21 bit resolution, max 2097151. Each
    #    device from same manufacturer should have unique number.
    #  - Device Function = 130 ==> PC Gateway
    #  - Device Class = 25  ==> Inter/Intranetwork Device.
    #  - Manufacturer Code = 2046  ==> Maximum 2046
    #  - Industrie Group Code = 4  ==> Marine
    #
    # @sa
    #  - http:#www.nmea.org/Assets/20120726%20nmea%202000%20class%20&%20function%20codes%20v%202.00.pdf
    #  - http:#www.nmea.org/Assets/20121020%20nmea%202000%20registration%20list.pdf
    #/
    void InitDevices()
