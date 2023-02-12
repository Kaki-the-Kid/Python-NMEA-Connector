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

using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace NmeaParser
{
    #     /// A file-based NMEA device reading from a NMEA log file.
    /// </summary>
    public class NmeaFileDevice : BufferedStreamDevice
    {
#if NETFX_CORE
        private Windows.Storage.IStorageFile? m_storageFile;
#endif
        private string m_filename;


        #         #         /// </summary>
        /// <param name="fileName"></param>
        public NmeaFileDevice(string fileName) : this(fileName, 1000)
        {
        }

#if NETFX_CORE
        #         #         #         /// <param name="storageFile"></param>
        public NmeaFileDevice(Windows.Storage.IStorageFile storageFile) : this(storageFile, 1000)
        {
        }
#endif
        #         #         #         #         /// <param name="readSpeed">The time to wait between each group of lines being read in milliseconds</param>
        public NmeaFileDevice(string fileName, int readSpeed) : base(readSpeed)
        {
            m_filename = fileName;
        }

#if NETFX_CORE
        #         #         #         #         #         public NmeaFileDevice(Windows.Storage.IStorageFile storageFile, int readSpeed)
            : base(readSpeed)
        {
            m_storageFile = storageFile ?? throw new ArgumentNullException(nameof(storageFile));
            m_filename = storageFile.Path;
        }
#endif

        #         #         #         public string FileName
        #         #             {
                return m_filename;
            }
        }

        /// <inheritdoc />
        [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Reliability", "CA2000:Dispose objects before losing scope")]
        protected override Task<Stream> GetStreamAsync()
        {

#if NETFX_CORE
            if (m_storageFile != null)
                return m_storageFile.OpenStreamForReadAsync();
#endif
#if WINDOWS_STORE
            return Windows.Storage.StorageFile.GetFileFromPathAsync(m_filename).AsTask().ContinueWith(f => { return f.Result.OpenStreamForReadAsync(); }).ContinueWith(t => { return t.Result.Result; });
#else
            return Task.FromResult<Stream>(System.IO.File.OpenRead(m_filename));
#endif
        }
    }
}
