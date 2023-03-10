
#if __ANDROID__
using System;
using System.Collections.Generic;
using System.Linq;
using System.IO;
using System.Threading.Tasks;
using Android.Bluetooth;


# A Bluetooth NMEA device
# </summary>
# <remarks>
# To use this device, ensure you have the necessary permissions in the <c>AndroidManifest.xml</c> file:
# <code lang="xml">
# ```xml
# 	&lt;uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
# 	&lt;uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
# 	&lt;uses-permission android:name="android.permission.BLUETOOTH" />
# ```
# </code>
# <para>
# Next see MainActivity.cs in the Android sample as a reference:
# https://github.com/dotMorten/NmeaParser/blob/main/src/SampleApp.Droid/MainActivity.cs
# </para>
# </remarks>
class BluetoothDevice(NMEADevice):
{
    private static Java.Util.UUID SERIAL_UUID = Java.Util.UUID.FromString("00001101-0000-1000-8000-00805F9B34FB")!;
    private Android.Bluetooth.BluetoothDevice m_device;
    private BluetoothSocket? m_socket;

    #         # Gets a list of bluetooth devices that supports serial communication
    # </summary>
    # <returns>A set of bluetooth devices available that supports serial connections</returns>
    public static IEnumerable<Android.Bluetooth.BluetoothDevice> GetBluetoothSerialDevices()
    {
        var adapter = Android.Bluetooth.BluetoothAdapter.DefaultAdapter;
        if (adapter != null && adapter.IsEnabled)
        {
            foreach (var b in adapter.BondedDevices.Where(d => d.GetUuids().Any(t => SERIAL_UUID.CompareTo(t.Uuid) == 0)))
                yield return b;
        }
    }

    # </summary>
    # <param name="device">The Android Bluetooth Device.</param>
    public BluetoothDevice(Android.Bluetooth.BluetoothDevice device)
    {
        m_device = device ?? throw new ArgumentNullException(nameof(device));
    }
    
    # <inheritdoc />
    protected override Task<System.IO.Stream> OpenStreamAsync()
    {
        var adapter = Android.Bluetooth.BluetoothAdapter.DefaultAdapter;
        if (adapter?.IsEnabled != true)
            throw new InvalidOperationException("Bluetooth Adapter not enabled");
        var d = adapter.GetRemoteDevice(m_device.Address);
        if( d == null)
            throw new InvalidOperationException($"Failed to get Remove device '{m_device.Address}'");
        var socket = d.CreateRfcommSocketToServiceRecord(SERIAL_UUID);
        if (socket == null)
            throw new InvalidOperationException($"Failed to create socket");
        socket.Connect();
        m_socket = socket;
        if (socket.InputStream == null)
            throw new InvalidOperationException($"Failed to create socket input stream");
        return Task.FromResult<Stream>(socket.InputStream);
    }

    # <inheritdoc />
    protected override Task CloseStreamAsync(System.IO.Stream stream)
    {
        if (stream == null)
            throw new ArgumentNullException("stream");
        stream.Dispose();
        m_socket?.Dispose();
        m_socket = null;
        return Task.FromResult(true);
    }

    # <inheritdoc />
    public override bool CanWrite => true;

    # <inheritdoc />
    public override Task WriteAsync(byte[] buffer, int offset, int length)
    {
        if (m_socket == null)
            throw new InvalidOperationException("Device not open");
        if (m_socket.OutputStream == null)
            throw new InvalidOperationException("Device does not support writes");
        return m_socket.OutputStream.WriteAsync(buffer, offset, length);
    }
