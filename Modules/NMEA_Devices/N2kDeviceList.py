'''
N2kDeviceList.cpp

Copyright (c) 2015-2022 Timo Lappalainen, Kave Oy, www.kave.fi

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the
Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''


#include "NMEA2000.h"

# Maximum allowed number of devices on the CAN BUS bus system is 254
N2kMaxBusDevices = 254

# Time in ms for first request after device has been noticed on the bus
N2kDL_TimeForFirstRequest = 1000 

# Time in ms between product information requests
N2kDL_TimeBetweenPIRequest  = 1000

# Time in ms between configuration information requests
N2kDL_TimeBetweenCIRequest = 1000 

#************************************************************************#***
#* \class   tN2kDeviceList
#* \brief   class thats holding a list of all devices on the bus
#* \ingroup group_helperClass
#* 
#*  This class is derived from \ref tNMEA2000::tMsgHandler.
#*/
class tN2kDeviceList : public tNMEA2000::tMsgHandler {
  protected:
    #**********************************************************************#***
    #* \class   tInternalDevice
    #* \brief   This class represents an internal device
    #*
    #*  This class is derived from \ref tNMEA2000::tDevice
    #*/
    class tInternalDevice : public tNMEA2000::tDevice {
    protected:
      #** \brief Product Infomation has bee loaded#*/
      bool ProdILoaded;
      #** \brief Product Information of this device*/
      tNMEA2000::tProductInformation ProdI;

      #** \brief Product Infomation has bee loaded#*/
      bool ConfILoaded;
      #** \brief Size of the Config Information (number of bytes)*/
      uint16_t ConfISize;
      #** \brief Size of the Manufacturer Information (number of bytes)#*/
      uint16_t ManISize;
      #** \brief Size of the Installation Description 1 (number of bytes)#*/
      uint16_t InstDesc1Size;
      #** \brief Size of the Installation Description 2 (number of bytes)#*/
      uint16_t InstDesc2Size;

      #** \brief Pointer to the Config Information#*/
      char#*ConfI;
      #** \brief Pointer to the Manufacturer Information#*/
      char#*ManufacturerInformation;
      #** \brief Pointer to the Installation Description 1#*/
      char#*InstallationDescription1;
      #** \brief Pointer to the Installation Description 2#*/
      char#*InstallationDescription2;

      #** \brief Size of the transmitted PGN (number of bytes)*/
      uint8_t TransmitPGNsSize;
      #** \brief Transmitted PGNs*/
      unsigned long#*TransmitPGNs;
      #** \brief Size of the received PGN (number of bytes)*/
      uint8_t ReceivePGNsSize;
      #** \brief Received PGNs*/
      unsigned long#*ReceivePGNs;

      public:
        #** \brief How many times we have requested the name.*/
        uint8_t nNameRequested; 
        #** \brief Time for last request on the Product Information*/
        unsigned long ProdIRequested; 
        #** \brief How many times we have requested the Product
        #*         information#*/
        uint8_t nProdIRequested; 
        #** \brief Time for last request on the Config Information*/
        unsigned long ConfIRequested; 
        #** \brief How many times we have requested the Config
        #*          information#*/
        uint8_t nConfIRequested; 
        #** \brief Time for last request on the PGN#*/
        unsigned long PGNsRequested; 
        #** \brief How many times we have requested the PGN*/
        uint8_t nPGNsRequested; 
        
        #** \brief Time of the last message*/
        unsigned long LastMessageTime;

      public:
        #******************************************************************#***
        #* \brief Construct a new Internal Device object
        #* 
        #* Init all the variables of the Internal device.
        #*
        #* \param _Name   Name of the device
        #* \param _Source Source address of this device on the bus
        #*/
        tInternalDevice(uint64_t _Name, uint8_t _Source=255);
        #**********************************************#*******************#***
        #* \brief Destroy the Internal Device object
        #* Clean up all the memory.
        #*/
        ~tInternalDevice();
        
        #******************************************************************#***
        #* \brief Set the Source address of the device
        #*
        #* \param _Source   Source address of this device
        #*/
        void SetSource(uint8_t _Source) { Source=_Source; }

        #******************************************************************#***
        #* \brief Set the Device Information 
        #*
        #* \param _Name   Name of the device
        #*/
        void SetDeviceInformation(uint64_t _Name) { DevI.SetName(_Name); }

        #*******************************************************************#***
        #* \brief Set the Product Information of the device
        #*
        #* \param _ModelSerialCode  Default="". Max 32 chars. Manufacturer's 
        #*                          Model serial code
        #* \param _ProductCode      Default=666. Manufacturer's product code
        #* \param _ModelID          Default="". Max 33 chars. Manufacturer's 
        #*                          Model ID
        #* \param _SwCode           Default="". Max 40 chars. Manufacturer's 
        #*                          software version code
        #* \param _ModelVersion     Default="". Max 24 chars. Manufacturer's 
        #*                          Model version
        #* \param _LoadEquivalency  Default=1. x#* 50 mA
        #* \param _N2kVersion       Default=1300
        #* \param _CertificationLevel Default=1
        #*/
        void SetProductInformation(const char#*_ModelSerialCode, 
                                   unsigned short _ProductCode=0xffff,  
                                   const char#*_ModelID=0, 
                                   const char#*_SwCode=0, 
                                   const char#*_ModelVersion=0, 
                                   unsigned char _LoadEquivalency=0xff,  
                                   unsigned short _N2kVersion=0xffff, 
                                   unsigned char _CertificationLevel=0xff 
                                  ) {
          ProdI.Set(_ModelSerialCode,_ProductCode,_ModelID,_SwCode,_ModelVersion,_LoadEquivalency,_N2kVersion,_CertificationLevel);
          ProdILoaded=true;
        }

        #******************************************************************#***
        #* \brief Has the Product Information for the device already been loaded
        #* \return true 
        #* \return false 
        #*/
        bool HasProductInformation() const { return ProdILoaded; }
        #******************************************************************#***
        #* \brief Get the N2k version of this device
        #* \return unsigned short
        #*/
        unsigned short GetN2kVersion() const { return ProdI.N2kVersion; }
        #******************************************************************#***
        #* \brief Get the Product code of this device
        #* \return unsigned short
        #*/
        unsigned short GetProductCode() const { return ProdI.ProductCode; }
        #******************************************************************#***
        #* \brief Get the Model ID of this device
        #* \return const char#*
        #*/
        const char#* GetModelID() const { return ProdI.N2kModelID; }
        #******************************************************************#***
        #* \brief Get the Software Code of this device
        #* \return const char#*
        #*/
        const char#* GetSwCode() const { return ProdI.N2kSwCode; }
        #******************************************************************#***
        #* \brief Get the Model Version of this device
        #* \return const char#*
        #*/
        const char#* GetModelVersion() const { return ProdI.N2kModelVersion; }
        #******************************************************************#***
        #* \brief Get the Model Serial Code of this device
        #* \return const char#*
        #*/
        const char#* GetModelSerialCode() const { return ProdI.N2kModelSerialCode; }
        #******************************************************************#***
        #* \brief Get the Certification Level of this device
        #* \return unsigned short
        #*/
        unsigned short GetCertificationLevel() const { return ProdI.CertificationLevel; }
        #******************************************************************#***
        #* \brief Get the Load Equivalency  (x#* 50 mA) of this device
        #* \return unsigned short
        #*/
        unsigned short GetLoadEquivalency() const { return ProdI.LoadEquivalency; }

        #******************************************************************#***
        #* \brief Has the Configuration  Information for the device 
        #*        already been loaded
        #* \return true 
        #* \return false 
        #*/
        bool HasConfigurationInformation() const { return ConfILoaded; }
        #******************************************************************#***
        #* \brief Get the Manufacturer Information of this device
        #* \return const char#*
        #*/
        const char#* GetManufacturerInformation() const { return ManufacturerInformation; }
        #******************************************************************#***
        #* \brief Get the Installation Description 1 of this device
        #* \return const char#*
        #*/
        const char#* GetInstallationDescription1() const { return InstallationDescription1; }
        #******************************************************************#***
        #* \brief Get the Installation Description 2 of this device
        #* \return const char#*
        #*/
        const char#* GetInstallationDescription2() const { return InstallationDescription2; }

        #******************************************************************#***
        #* \brief Initialize the Configuration Information of this device 
        #* 
        #* This function gives back an empty string for the Configuration 
        #* Information. Adequate memory has been allocated and the leading 
        #* character ('\0' terminators ) have been added.
        #* 
        #* \param _ManISize       Size of the Manufacturer Information 
        #* \param _InstDesc1Size  Size of the Install Description 1
        #* \param _InstDesc2Size  Size of the Install Description 2
        #* 
        #* \return char* ->  empty Configuration Information
        #*/
        char#* InitConfigurationInformation(size_t &_ManISize, size_t &_InstDesc1Size, size_t &_InstDesc2Size);
        
        #******************************************************************#***
        #* \brief Get the Manufacturer Information of this device
        #* \return char#*
        #*/
        char#* GetManufacturerInformation() { return ManufacturerInformation; }
        #******************************************************************#***
        #* \brief Get the Installation Description 1 of this device
        #* \return char#*
        #*/
        char#* GetInstallationDescription1() { return InstallationDescription1; }
        #******************************************************************#***
        #* \brief Get the Installation Description 2 of this device
        #* \return char#*
        #*/
        char#* GetInstallationDescription2() { return InstallationDescription2; }

        #******************************************************************#***
        #* \brief Get the transmitted PGNs of this device
        #* \return const unsigned long#*
        #*/
        const unsigned long#* GetTransmitPGNs() const { return TransmitPGNs; }
        #******************************************************************#***
        #* \brief Get the received PGNs of this device
        #* \return const unsigned long#*
        #*/
        const unsigned long#* GetReceivePGNs() const { return ReceivePGNs; }

        #******************************************************************#***
        #* \brief Initialize an array for transmitted PGNs
        #* This functions frees if needed old reservation and reserves new 
        #* memory for requested number of PGNs
        #* \param count   Number of Transmitted PGNs to be handled
        #* \return unsigned long#*
        #*/
        unsigned long#* InitTransmitPGNs(uint8_t count);

        #******************************************************************#***
        #* \brief Initialize an array for received PGNs
        #* This functions frees if needed old reservation and reserves new 
        #* memory for requested number of PGNs
        #* \param count   Number of Transmitted PGNs to be handled
        #* \return unsigned long#*
        #*/
        unsigned long#* InitReceivePGNs(uint8_t count);

        #******************************************************************#***
        #* \brief Should the Device Name be requested
        #* As long as the device name is not set yet and the number of
        #* requests is smaller than 20, the name should be requested once more.
        #* \return true 
        #* \return false 
        #*/
        bool ShouldRequestName() { return GetName()==0 && nNameRequested<20; }
        #****************************************************************#***
        #* \brief Increments the Number of how often the name has already 
        #*        been requested#*/
        void SetNameRequested() { nNameRequested++; }
        #****************************************************************#***
        #*  \brief  Resets the Product Information Loaded values of 
        #*          the device#*/        
        void ClearProductInformationLoaded() { ProdILoaded=false; ProdIRequested=0; nProdIRequested=0; }
        #****************************************************************#***
        #*  \brief  Clears the Product Information the device#*/        
        void ClearProductInformation() { ProdI.Clear(); ClearProductInformationLoaded(); }
        #******************************************************************#***
        #* \brief Should the Device Product Information be requested
        #* As long as the device Product Information is not set yet and the 
        #* number of requests is smaller than 4, the name should be 
        #* requested once more.
        #* \return true 
        #* \return false 
        #*/
        bool ShouldRequestProductInformation() { return ( !ProdILoaded && nProdIRequested<4 ); } 
        #******************************************************************#***
        #* \brief Ready for the next request of Device Product Information
        #* 
        #* There must be a minimum interval between two requests for 
        #* product information. see \ref N2kDL_TimeBetweenPIRequest
        #* 
        #* \return true 
        #* \return false 
        #*/
        bool ReadyForRequestProductInformation() { return ( ShouldRequestProductInformation() && N2kHasElapsed(ProdIRequested,N2kDL_TimeBetweenPIRequest) && N2kHasElapsed(GetCreateTime(),N2kDL_TimeForFirstRequest) ); }
        #****************************************************************#***
        #* \brief Increments the Number of how often the Product Information
        #*         has already been requested and stores the timestamp*/
        void SetProductInformationRequested() { ProdIRequested=N2kMillis(); nProdIRequested++; }
        #****************************************************************#***
        #* \brief Compares two Product Informations
        #* \return true
        #* \return false
        #*#*/
        bool IsSameProductInformation(tNMEA2000::tProductInformation &Other) {
            if (ProdI.IsSame(Other)) {
              ProdILoaded=true; return true;
            } else {
              return false;
            }
          }
        
        #****************************************************************#***
        #*  \brief  Resets the Configuration Information Loaded values of 
        #*          the device#*/        
        void ClearConfigurationInformationLoaded() { ConfILoaded=false; ConfIRequested=0; nConfIRequested=0; }
        #******************************************************************#***
        #* \brief Should the Device Configuration Information be requested
        #* As long as the device Configuration Information is not set yet 
        #* and the number of requests is smaller than 4, the name should be 
        #* requested once more.
        #* \return true 
        #* \return false 
        #*/
        bool ShouldRequestConfigurationInformation() { return ( !ConfILoaded && nConfIRequested<4 ); } 
        #******************************************************************#***
        #* \brief Ready for the next request of Device Configuration
        #*        Information
        #* 
        #* There must be a minimum interval between two requests for 
        #* product information. see \ref N2kDL_TimeBetweenCIRequest
        #* 
        #* \return true 
        #* \return false 
        #*/
        bool ReadyForRequestConfigurationInformation() { return ( ShouldRequestConfigurationInformation() && millis()-ConfIRequested>N2kDL_TimeBetweenCIRequest && millis()-GetCreateTime()>N2kDL_TimeForFirstRequest ); }
        #****************************************************************#***
        #* \brief Increments the Number of how often the Configuration 
        #*        Information has already been requested and stores the 
        #*        timestamp*/
        void SetConfigurationInformationRequested() { ConfIRequested=millis(); nConfIRequested++; }

        #****************************************************************#***
        #*  \brief  Resets the PGN List Loaded values of 
        #*          the device#*/        
        void ClearPGNListLoaded() { PGNsRequested=0; nPGNsRequested=0; }
        #******************************************************************#***
        #* \brief Should the Device PGN List be requested
        #* As long as the device PGN List is not set yet 
        #* and the number of requests is smaller than 4, the name should be 
        #* requested once more.
        #* \return true 
        #* \return false 
        #*/
        bool ShouldRequestPGNList() { return ( ((TransmitPGNs==0) || (ReceivePGNs==0))  && nPGNsRequested<4 ); } // We do not have it and not tried enough
        #****************************************************************#***
        #* \brief Increments the Number of how often the PGN List 
        #*        has already been requested and stores the 
        #*        timestamp*/
        void SetPGNListRequested() { PGNsRequested=N2kMillis(); nPGNsRequested++; }
        #******************************************************************#***
        #* \brief Ready for the next request of Device PGN List
        #* 
        #* There must be a minimum interval between two requests for 
        #* product information. see \ref N2kDL_TimeForFirstRequest
        #* 
        #* \return true 
        #* \return false 
        #*/
        bool ReadyForRequestPGNList() { return ( ShouldRequestPGNList() && N2kHasElapsed(PGNsRequested,1000) && N2kHasElapsed(GetCreateTime(),N2kDL_TimeForFirstRequest) ); }
    }; // tInternalDevice

  protected:
    #********************************************************************#***
    #* \brief List of NMEA2000 devices found on the bus
    #*/
    tInternalDevice#* Sources[N2kMaxBusDevices];  
    #** \brief Number of NMEA2000 devices stored in \ref Sources*/
    uint8_t MaxDevices;
    #** \brief The list of devices has been updated*/
    bool ListUpdated;
    #** \brief There are still requests pending*/
    bool HasPendingRequests;

  protected:
    #********************************************************************#***
    #* \brief Handle Iso Address Claim Message - PGN 60928
    #* 
    #* This function handle an iso address claim message. It check whether 
    #* the caller device is already listed at \ref Sources or not.
    #* If it is already listed, it checks also if the name at this source 
    #* position still matches. When the name doesn't match, it moves the 
    #* "old" device to a free spot in \ref Sources.
    #* 
    #* If the caller is completely unknown, a new device will be placed in 
    #* \ref Sources.
    #*
    #* \param N2kMsg    Reference to a N2kMsg Object, 
    #*/
    void HandleIsoAddressClaim(const tN2kMsg &N2kMsg);

    #********************************************************************#***
    #* \brief Handle a Product Information message - PGN 126996
    #* 
    #* The message provides product information onto the network that 
    #* could be important for determining quality of data coming from 
    #* this product. The message is parsed and all data is stored 
    #* in \ref tInternalDevice::ProdI
    #* 
    #* \param N2kMsg    Reference to a N2kMsg Object, 
    #*/
    void HandleProductInformation(const tN2kMsg &N2kMsg);
    #********************************************************************#***
    #* \brief Handle a Configuration Information message - PGN 126998
    #* 
    #* The message contains free-form alphanumeric fields describing the 
    #* installation (e.g., starboard engine room location) of the device 
    #* and installation notes (e.g., calibration data).
    #* It is parsed and all data is stored in the internal device
    #* 
    #* \param N2kMsg    Reference to a N2kMsg Object, 
    #*/
    void HandleConfigurationInformation(const tN2kMsg &N2kMsg);
    #********************************************************************#***
    #* \brief Handle a Product Information message - PGN 126464
    #*  
    #* The PGN 126464 message consists the group function type defined 
    #* by the first field. The message will be either a Transmit PGNs or 
    #* a Receive PGNs group function that identifies the PGNs transmitted 
    #* from or received by a node.
    #* This function determines if the PGNs are receive or transmit PGN
    #* (see \ref tN2kPGNList) an the stores the PGNs to the corresponding 
    #* internal device in \ref Sources.
    #* 
    #* \param N2kMsg    Reference to a N2kMsg Object, 
    #*/
    void HandleSupportedPGNList(const tN2kMsg &N2kMsg); 
    #********************************************************************#***
    #* \brief Handles all Other messages
    #* 
    #* If request is pending ( \ref HasPendingRequests == true) it requires
    #* a name for every device, then loads product + config informations 
    #* and supported PGN lists as needed.
    #*
    #* \param N2kMsg    Reference to a N2kMsg Object, 
    #*/
    void HandleOther(const tN2kMsg &N2kMsg);
    #********************************************************************#***
    #* \brief Find a device in \ref Sources by the source address
    #*
    #* \param Source  Source address of the device to be searched for
    #* \return tN2kDeviceList::tInternalDevice* 
    #*/
    tN2kDeviceList::tInternalDevice#* LocalFindDeviceBySource(uint8_t Source) const;
    #********************************************************************#***
    #* \brief Find a device in \ref Sources by the name of the device
    #*
    #* \param Name  Name of the device to be searched for
    #* \return tN2kDeviceList::tInternalDevice* 
    #*/
    tN2kDeviceList::tInternalDevice#* LocalFindDeviceByName(uint64_t Name) const;
    #********************************************************************#***
    #* \brief Find a device in \ref Sources by the manufacturer code and
    #*        unique ID
    #*
    #* \param ManufacturerCode  Manufacturer code of the device to be 
    #*                          searched for
    #* \param UniqueNumber      Unique ID of the device to be searched for
    #* \return tN2kDeviceList::tInternalDevice* 
    #*/
    tN2kDeviceList::tInternalDevice#* LocalFindDeviceByIDs(uint16_t ManufacturerCode, uint32_t UniqueNumber) const;
    #********************************************************************#***
    #* \brief Find a device in \ref Sources by the manufacturer and product
    #*        code
    #* 
    #* \param ManufacturerCode  Manufacturer code of the device to be 
    #*                          searched for
    #* \param ProductCode       Product code of the device to be 
    #*                          searched for
    #* \param Source  Source address of the device to be searched for
    #* \return tN2kDeviceList::tInternalDevice* 
    #*/
    tN2kDeviceList::tInternalDevice#* LocalFindDeviceByProduct(uint16_t ManufacturerCode, uint16_t ProductCode, uint8_t Source=0xff) const;
    #********************************************************************#***
    #* \brief Request the product information of a specific device on the bus
    #* 
    #* This function sends out an Iso Request message in order to obtain
    #* more information about a specific device on the bus.
    #*
    #* \param Source  Destination address of the target device
    #* \return true   -> Message was sended successfully
    #* \return false 
    #*/
    bool RequestProductInformation(uint8_t Source);
    #********************************************************************#***
    #* \brief Request the configuration information of a specific 
    #*        device on the bus
    #* 
    #* This function sends out an Iso Request message in order to obtain
    #* more information about a specific device on the bus.
    #*
    #* \param Source  Destination address of the target device
    #* \return true   -> Message was sended successfully
    #* \return false 
    #*/
    bool RequestConfigurationInformation(uint8_t Source);
    #********************************************************************#***
    #* \brief Request the supported PGNs of a specific device on the bus
    #* 
    #* This function sends out an Iso Request message in order to obtain
    #* more information about a specific device on the bus.
    #*
    #* \param Source  Destination address of the target device
    #* \return true   -> Message was sended successfully
    #* \return false 
    #*/
    bool RequestSupportedPGNList(uint8_t Source);
    #********************************************************************#***
    #* \brief Request the ISO AddressClaim for a specific device on the bus
    #*
    #* \param Source  Destination address of the target device
    #* \return true   -> Message was sended successfully
    #* \return false 
    #*/
    bool RequestIsoAddressClaim(uint8_t Source);
    #********************************************************************#***
    #* \brief Adds a device to \ref Sources
    #*
    #* \param Source Source address of the device
    #*/
    void AddDevice(uint8_t Source);
    #********************************************************************#***
    #* \brief Saves a device to \ref Sources
    #*
    #* \param pDevice Pointer to a device
    #* \param Source Source address of the device
    #*/
    void SaveDevice(tInternalDevice#*pDevice, uint8_t Source);

  public:
    #********************************************************************#***
    #* \brief Constructor for the class
    #*
    #* Initialize all the attributes of the class
    #* 
    #* \param _pNMEA2000    Pointer to an \ref NMEA2000 object
    #*/
    tN2kDeviceList(tNMEA2000#*_pNMEA2000);
    #********************************************************************#***
    #* \brief Handle NMEA2000 messages 
    #* 
    #* Depending on the message PGN the correct handler (see \ref 
    #* HandleIsoAddressClaim, \ref HandleProductInformation, 
    #* \ref HandleConfigurationInformation, \ref HandleSupportedPGNList, 
    #* \ref HandleOther) is chosen. 
    #* If ther e is now device with this source address is listed in \ref 
    #* Sources, a new device is added ( \ref AddDevice).
    #*
    #* \param N2kMsg    Reference to a N2kMsg Object, 
    #*/
    void HandleMsg(const tN2kMsg &N2kMsg);

    // 
    #********************************************************************#***
    #* \brief Return device by it's bus source address
    #* 
    #* Return device by it's bus source address. If there is no device 
    #* with given source, function returns nul
    #* \param Source  Source address of the device to be searched for
    #* \return const tNMEA2000::tDevice* 
    #*/
    const tNMEA2000::tDevice#* FindDeviceBySource(uint8_t Source) const { return LocalFindDeviceBySource(Source); }

    // Return device last message time in milliseconds.
    unsigned long GetDeviceLastMessageTime(uint8_t Source) const {
      tN2kDeviceList::tInternalDevice#*dev=LocalFindDeviceBySource(Source);
      return ( dev!=0?dev->LastMessageTime:0 );
    }

    // 
    #********************************************************************#***
    #* \brief Find a device in \ref Sources by the name of the device
    #*
    #* Return device by it's name. Device name is complete device 
    #* information data, which is unique for all registered devices and 
    #* should be unique for own made devices on own bus. Name will be 
    #* matched according to matching parameter. If there is no device with
    #* given name, function returns null.
    #* 
    #* \param Name  Name of the device to be searched for
    #* \return tN2kDeviceList::tInternalDevice* 
    #*/
    const tNMEA2000::tDevice#* FindDeviceByName(uint64_t Name) const { return LocalFindDeviceByName(Name); }
    
    #********************************************************************#***
    #* \brief Find a device in \ref Sources by the manufacturer code and
    #*        unique ID
    #* 
    #* Return device by manufacturer identification. Each device should have 
    #* manufacturer id and unique ID.
    #* 
    #* \param ManufacturerCode  Manufacturer code of the device to be 
    #*                          searched for
    #* \param UniqueNumber      Unique ID of the device to be searched for
    #* \return tN2kDeviceList::tInternalDevice* 
    #*/
    const tNMEA2000::tDevice#* FindDeviceByIDs(uint16_t ManufacturerCode, uint32_t UniqueNumber) const { return LocalFindDeviceByIDs(ManufacturerCode, UniqueNumber); }
    
    #********************************************************************#***
    #* \brief Find a device in \ref Sources by the manufacturer and product
    #*        code
    #* 
    #* Return device by manufacturer product code. Each device should 
    #* have product code given by NMEA2000 organization. Search with 
    #* source = 0xff finds first device. To find all devices with given
    #* manufacturer product code, repeat search with found 
    #* device source until device will not be found.
    #* 
    #* \param ManufacturerCode  Manufacturer code of the device to be 
    #*                          searched for
    #* \param ProductCode       Product code of the device to be 
    #*                          searched for
    #* \param Source  Source address of the device to be searched for
    #* \return tN2kDeviceList::tInternalDevice* 
    #*/
    const tNMEA2000::tDevice#* FindDeviceByProduct(uint16_t ManufacturerCode, uint16_t ProductCode, uint8_t Source=0xff) const { return LocalFindDeviceByProduct(ManufacturerCode, ProductCode, Source); }
    
    #************************************************************************#***
    #* \brief Check if device list has updated.
    #* 
    #* Device list will be automatically updated. In stable system list 
    #* should be ready and stable in few seconds. If you add device on the
    #* fly, list will be updated as soon as it start to send data to the bus.
    #* 
    #* \return true 
    #* \return false 
    #*/
    bool ReadResetIsListUpdated() { if ( ListUpdated ) { ListUpdated=false; return true; } else { return false; } }

    #************************************************************************#***
    #* \brief Return number of known devices in \ref Sources
    #*
    #* \return Number of devices
    #*/
    uint8_t Count() const;
};

#endif




#include <stdlib.h>
#include "N2kDeviceList.h"

/#*define N2kDeviceList_HANDLE_IN_DEBUG

#if defined(N2kDeviceList_HANDLE_IN_DEBUG)
#define DebugStream Serial
# define N2kHandleInDbg(fmt, args...)     DebugStream.print (fmt , ## args)
# define N2kHandleInDbgln(fmt, args...)   DebugStream.println (fmt , ## args)
#else
# define N2kHandleInDbg(fmt, args...)
# define N2kHandleInDbgln(fmt, args...)
#endif

#******************************************************************************
tN2kDeviceList::tN2kDeviceList(tNMEA2000#*_pNMEA2000) : tNMEA2000::tMsgHandler(0,_pNMEA2000) {
  for (uint8_t i=0; i<N2kMaxBusDevices; i++) Sources[i]=0;
  MaxDevices=0;
  ListUpdated=false;
  HasPendingRequests=true;
}

#******************************************************************************
tN2kDeviceList::tInternalDevice#* tN2kDeviceList::LocalFindDeviceBySource(uint8_t Source) const {
  if ( Source>=N2kMaxBusDevices ) return 0;

  return Sources[Source];
}

#******************************************************************************
tN2kDeviceList::tInternalDevice#* tN2kDeviceList::LocalFindDeviceByName(uint64_t Name) const {
  tInternalDevice#*result=0;

    for (uint8_t i=0; i<MaxDevices && result==0; i++) {
      if ( Sources[i]!=0 && Sources[i]->IsSame(Name) ) result=Sources[i];
    }

    return result;
}

#******************************************************************************
tN2kDeviceList::tInternalDevice#* tN2kDeviceList::LocalFindDeviceByIDs(uint16_t ManufacturerCode, uint32_t UniqueNumber) const {
  tInternalDevice#*result=0;

    if ( ManufacturerCode==N2kUInt16NA && UniqueNumber==N2kUInt32NA ) return result;

    for (uint8_t i=0; i<MaxDevices && result==0; i++) {
      if ( Sources[i]!=0 &&
           (ManufacturerCode==N2kUInt16NA || Sources[i]->GetManufacturerCode()==ManufacturerCode) &&
           (UniqueNumber==N2kUInt32NA || Sources[i]->GetUniqueNumber()==UniqueNumber) ) result=Sources[i];
    }

    return result;
}

#******************************************************************************
tN2kDeviceList::tInternalDevice#* tN2kDeviceList::LocalFindDeviceByProduct(uint16_t ManufacturerCode, uint16_t ProductCode, uint8_t Source) const {
  tInternalDevice#*result=0;

    if ( Source<MaxDevices ) { Source++; } else { Source=0; }

    if ( ManufacturerCode==N2kUInt16NA || ProductCode==N2kUInt16NA ) return result;

    for (uint8_t i=Source; i<MaxDevices && result==0; i++) {
      if ( Sources[i]!=0 &&
           Sources[i]->GetManufacturerCode()==ManufacturerCode &&
           Sources[i]->GetProductCode()==ProductCode ) result=Sources[i];
    }

    return result;
}

#******************************************************************************
bool tN2kDeviceList::RequestProductInformation(uint8_t Source) {
  tN2kMsg N2kMsg;

    SetN2kPGNISORequest(N2kMsg,Source,N2kPGNProductInformation);
    return GetNMEA2000()->SendMsg(N2kMsg);
}

#******************************************************************************
bool tN2kDeviceList::RequestConfigurationInformation(uint8_t Source) {
  tN2kMsg N2kMsg;

    SetN2kPGNISORequest(N2kMsg,Source,N2kPGNConfigurationInformation);
    return GetNMEA2000()->SendMsg(N2kMsg);
}

#******************************************************************************
bool tN2kDeviceList::RequestSupportedPGNList(uint8_t Source) {
  tN2kMsg N2kMsg;

    SetN2kPGNISORequest(N2kMsg,Source,126464L);
    return GetNMEA2000()->SendMsg(N2kMsg);
}

#******************************************************************************
bool tN2kDeviceList::RequestIsoAddressClaim(uint8_t Source) {
  tN2kMsg N2kMsg;

    SetN2kPGNISORequest(N2kMsg,Source,N2kPGNIsoAddressClaim);
    return GetNMEA2000()->SendMsg(N2kMsg);
}

#******************************************************************************
void tN2kDeviceList::HandleMsg(const tN2kMsg &N2kMsg) {
  if ( N2kMsg.Source>=N2kMaxBusDevices ) return;

  if ( Sources[N2kMsg.Source]==0 ) {
    switch ( N2kMsg.PGN ) {
      case N2kPGNIsoAddressClaim:break; // fall to default handler
      case N2kPGNProductInformation:
      case N2kPGNConfigurationInformation:
      case 126464L: AddDevice(N2kMsg.Source); break; // Create device and fall to default handler
      default: AddDevice(N2kMsg.Source); return;
    }
  }

  switch ( N2kMsg.PGN ) {
    case N2kPGNIsoAddressClaim: HandleIsoAddressClaim(N2kMsg); break;
    case N2kPGNProductInformation: HandleProductInformation(N2kMsg); break;
    case N2kPGNConfigurationInformation: HandleConfigurationInformation(N2kMsg); break;
    case 126464L: HandleSupportedPGNList(N2kMsg); break;
    default: HandleOther(N2kMsg);
  }

  if ( Sources[N2kMsg.Source]!=0 ) {
    // If device has been off and appears again and we still do not have name,
    // start request sequence again
    if ( Sources[N2kMsg.Source]->GetName()==0 &&
         Sources[N2kMsg.Source]->nNameRequested>0 && 
         N2kHasElapsed(Sources[N2kMsg.Source]->LastMessageTime,60000) ) {
      Sources[N2kMsg.Source]->nNameRequested=0;
      HasPendingRequests=true;
    }
    Sources[N2kMsg.Source]->LastMessageTime=N2kMillis();
  }
}

#******************************************************************************
void tN2kDeviceList::HandleOther(const tN2kMsg &N2kMsg) {
  if ( N2kMsg.Source>=N2kMaxBusDevices ) return;

//  N2kHandleInDbg(N2kMillis()); N2kHandleInDbg(" PGN: "); N2kHandleInDbgln(N2kMsg.PGN);

  if ( !HasPendingRequests ) return;

  HasPendingRequests=false;

  // Require name for every device.
  if ( Sources[N2kMsg.Source]->ShouldRequestName() && RequestIsoAddressClaim(N2kMsg.Source) ) {
    Sources[N2kMsg.Source]->SetNameRequested();
    HasPendingRequests=true;
  }

  // First we try to request product information for all devices
  for ( int i=0; i<MaxDevices; i++) {
    if ( Sources[i]!=0 ) {
      // Test do we need product information for this device
      if ( Sources[i]->ReadyForRequestProductInformation() ) {
        if ( RequestProductInformation(Sources[i]->GetSource()) ) {
          N2kHandleInDbg(N2kMillis()); N2kHandleInDbg(" Request product information for source: "); N2kHandleInDbgln(Sources[i]->GetSource());
          Sources[i]->SetProductInformationRequested();
          HasPendingRequests=true;
          return;
        }
      } else {
        HasPendingRequests|=Sources[i]->ShouldRequestProductInformation();
      }
    }
  }
  if ( HasPendingRequests ) return;
  // We come up to here, if have requested all product infromation
  // Start to request configuration information for devices.
  for ( int i=0; i<MaxDevices; i++) {
    if ( Sources[i]!=0 ) {
      // Test do we need product information for this device
      if ( Sources[i]->ReadyForRequestConfigurationInformation() ) {
        if ( RequestConfigurationInformation(Sources[i]->GetSource()) ) {
          N2kHandleInDbg(N2kMillis()); N2kHandleInDbg(" Request configuration information for source: "); N2kHandleInDbgln(Sources[i]->GetSource());
          Sources[i]->SetConfigurationInformationRequested();
          HasPendingRequests=true;
          return;
        }
      } else {
        HasPendingRequests|=Sources[i]->ShouldRequestConfigurationInformation();
      }
    }
  }
  if ( HasPendingRequests ) return;

  // Finally query supported PGN lists
  for ( int i=0; i<MaxDevices; i++) {
    if ( Sources[i]!=0 ) {
      // Test do we need product information for this device
      if ( Sources[i]->ReadyForRequestPGNList() ) {
        if ( RequestSupportedPGNList(Sources[i]->GetSource()) ) {
          N2kHandleInDbg(N2kMillis()); N2kHandleInDbg(" Request supported PGN lists for source: "); N2kHandleInDbgln(Sources[i]->GetSource());
          Sources[i]->SetPGNListRequested();
          HasPendingRequests=true;
          return;
        }
      } else {
        HasPendingRequests|=Sources[i]->ShouldRequestPGNList();
      }
    }
  }
}

#******************************************************************************
void tN2kDeviceList::AddDevice(uint8_t Source){
  if ( RequestIsoAddressClaim(Source) ) {  // Request device information
    SaveDevice(new tInternalDevice(0),Source); // We have now device on this source, so we will not do continuos query.
    HasPendingRequests=true;
  }
}

#******************************************************************************
void tN2kDeviceList::SaveDevice(tInternalDevice#*pDevice, uint8_t Source) {
  if ( Source>=N2kMaxBusDevices ) return;

  pDevice->SetSource(Source);
  Sources[Source]=pDevice;
  if ( Source>=MaxDevices ) MaxDevices=Source+1;
}

#******************************************************************************
void tN2kDeviceList::HandleIsoAddressClaim(const tN2kMsg &N2kMsg) {
  if ( N2kMsg.PGN!=N2kPGNIsoAddressClaim ) return;

  int Index=0;
  uint64_t CallerName=N2kMsg.GetUInt64(Index);
  tInternalDevice#*pDevice=0;

  // First check do we already have recorded caller
  if ( N2kMsg.Source<N2kMaxBusDevices && Sources[N2kMsg.Source]!=0 ) {
    pDevice=Sources[N2kMsg.Source];
    N2kHandleInDbg("ISO address claim. Caller:"); N2kHandleInDbg((uint32_t)CallerName); N2kHandleInDbg(", uniq:" ); N2kHandleInDbgln(pDevice->GetUniqueNumber());
    if ( pDevice->GetName()==0 ) {  // Device reservation made by HandleMsg, Name has not set yet
      tInternalDevice#*pDevice2=LocalFindDeviceByName(CallerName); // Find does this actually exist with other source
      if ( pDevice2!=0 ) { // We have already seen that message on other address, so move it here
        delete pDevice;
        Sources[pDevice2->GetSource()]=0;
        SaveDevice(pDevice2,N2kMsg.Source);
        pDevice=pDevice2;
      } else {
        pDevice->SetDeviceInformation(CallerName);
        ListUpdated=true;
        N2kHandleInDbg("Saving name for source:"); N2kHandleInDbgln(N2kMsg.Source);
      }
    } else if (!pDevice->IsSame(CallerName) ) { // exists, but name does not match. So device on this source position has claimed address and this has taken its place
      // Just move old device to some empty place
      uint8_t i;
      for (i=0; i<N2kMaxBusDevices && Sources[i]!=0; i++);
      // If we found empty place, move it there.
      if ( i<N2kMaxBusDevices ) {
        SaveDevice(pDevice,i);
        RequestIsoAddressClaim(0xff);  // Request addresses for all nodes.
      } else { // If not, we just delete device, since we can not do much with it. This would be extremely unexpected.
        delete pDevice;
      }
      Sources[N2kMsg.Source]=0;
      pDevice=0;
    } else { // Name is caller -> we have device on list on its place.
      return;
    }
  }

  if ( pDevice==0 ) {
    // New or changed source
    pDevice=LocalFindDeviceByName(CallerName);
    if ( pDevice!=0 ) { // Address changed, simply move device to new place.
      Sources[pDevice->GetSource()]=0;
      SaveDevice(pDevice,N2kMsg.Source);
      N2kHandleInDbg("Source updated: "); N2kHandleInDbgln(pDevice->GetSource());
    } else { // New device
      pDevice=new tInternalDevice(CallerName);
      SaveDevice(pDevice,N2kMsg.Source);
    }
  }

  // In any address change, we request information again.
  pDevice->ClearProductInformationLoaded();
  HasPendingRequests=true;

  ListUpdated=true;
}

#******************************************************************************
void tN2kDeviceList::HandleProductInformation(const tN2kMsg &N2kMsg) {
  tNMEA2000::tProductInformation ProdI;
//  unsigned long t1=micros();

  if ( N2kMsg.Source>=N2kMaxBusDevices || Sources[N2kMsg.Source]==0 ) return;

  tInternalDevice#*pDevice=Sources[N2kMsg.Source];

  N2kHandleInDbg(" Handle product information for source: "); N2kHandleInDbgln(N2kMsg.Source);

  if ( !pDevice->HasProductInformation() &&
       ParseN2kPGN126996(N2kMsg,ProdI.N2kVersion,ProdI.ProductCode,
                         sizeof(ProdI.N2kModelID),ProdI.N2kModelID,sizeof(ProdI.N2kSwCode),ProdI.N2kSwCode,
                         sizeof(ProdI.N2kModelVersion),ProdI.N2kModelVersion,sizeof(ProdI.N2kModelSerialCode),ProdI.N2kModelSerialCode,
                         ProdI.CertificationLevel,ProdI.LoadEquivalency) ) {
    if ( !pDevice->IsSameProductInformation(ProdI) ) {
      pDevice->SetProductInformation(ProdI.N2kModelSerialCode,ProdI.ProductCode,ProdI.N2kModelID,ProdI.N2kSwCode,ProdI.N2kModelVersion,
                                     ProdI.LoadEquivalency,ProdI.N2kVersion,ProdI.CertificationLevel);
      ListUpdated=true;
    }
  }

//  unsigned long t2=micros();
//  if ( ListUpdated ) { Serial.print("  Updated source: "); Serial.println(N2kMsg.Source); }
//  Serial.print(" - 126996 elapsed: "); Serial.println(t2-t1);
}

#******************************************************************************
void tN2kDeviceList::HandleConfigurationInformation(const tN2kMsg &N2kMsg) {

  if ( N2kMsg.Source>=N2kMaxBusDevices || Sources[N2kMsg.Source]==0 ) return;

//  unsigned long t1=micros();
  size_t ManISize;
  size_t InstDesc1Size;
  size_t InstDesc2Size;

  tInternalDevice#*pDevice=Sources[N2kMsg.Source];

  N2kHandleInDbg(" Handle configuration information for source: "); N2kHandleInDbgln(N2kMsg.Source);

  if ( ParseN2kPGN126998(N2kMsg,ManISize,0,InstDesc1Size,0,InstDesc2Size,0) ) { // First query required size
    pDevice->InitConfigurationInformation(ManISize,InstDesc1Size,InstDesc2Size);
    int TotalSize=ManISize+InstDesc1Size+InstDesc2Size;
    if ( TotalSize>0 ) {
      ParseN2kPGN126998(N2kMsg,
                        ManISize,pDevice->GetManufacturerInformation(),
                        InstDesc1Size,pDevice->GetInstallationDescription1(),
                        InstDesc2Size,pDevice->GetInstallationDescription2());
    }
    ListUpdated=true;
  }

//  unsigned long t2=micros();
//  if ( ListUpdated ) { Serial.print("  Updated source: "); Serial.println(N2kMsg.Source); }
//  Serial.print(" - 126996 elapsed: "); Serial.println(t2-t1);
}

#******************************************************************************
void tN2kDeviceList::HandleSupportedPGNList(const tN2kMsg &N2kMsg) {

  if ( N2kMsg.Source>=N2kMaxBusDevices || Sources[N2kMsg.Source]==0 ) return;

  int Index=0;
  tN2kPGNList N2kPGNList=(tN2kPGNList)N2kMsg.GetByte(Index);
  uint8_t PGNCount=(N2kMsg.DataLen-Index)/3;
  tInternalDevice#*pDevice=Sources[N2kMsg.Source];
  unsigned long#* PGNList=0;
  uint8_t iPGN;

  switch (N2kPGNList) {
    case N2kpgnl_transmit:
      PGNList=pDevice->InitTransmitPGNs(PGNCount);
      break;
    case N2kpgnl_receive:
      PGNList=pDevice->InitReceivePGNs(PGNCount);
      break;
  }
  if ( PGNList!=0 ) {
    for (iPGN=0; iPGN<PGNCount; iPGN++) { PGNList[iPGN]=N2kMsg.Get3ByteUInt(Index); }
    PGNList[iPGN]=0;
  }

  ListUpdated=true;
}

#******************************************************************************
uint8_t tN2kDeviceList::Count() const {
  uint8_t ret=0;

  for ( size_t i=0; i<MaxDevices; i++ ) if ( Sources[i]!=0 ) ret++;

  return ret;
}

// tN2kDeviceList::tInternalDevice

#******************************************************************************
tN2kDeviceList::tInternalDevice::tInternalDevice(uint64_t _Name, uint8_t _Source) : tNMEA2000::tDevice(_Name,_Source) {
  ProdI.Clear(); ProdILoaded=false; ConfILoaded=false;
  ConfI=0; ConfISize=0; ManufacturerInformation=0; InstallationDescription1=0; InstallationDescription2=0;
  TransmitPGNsSize=0; TransmitPGNs=0; ReceivePGNsSize=0; ReceivePGNs=0;
  nNameRequested=0;
  ClearProductInformationLoaded();
  ClearConfigurationInformationLoaded();
  ClearPGNListLoaded();
}

#******************************************************************************
tN2kDeviceList::tInternalDevice::~tInternalDevice() {
  if ( ConfI!=0 ) free(ConfI);
  if ( TransmitPGNs!=0 ) free(TransmitPGNs);
  if ( ReceivePGNs!=0 ) free(ReceivePGNs);
}

#******************************************************************************
char#* tN2kDeviceList::tInternalDevice::InitConfigurationInformation(size_t &_ManISize, size_t &_InstDesc1Size, size_t &_InstDesc2Size) {
  if ( _ManISize>0 ) _ManISize++; // Reserve '/0' terminator
  if ( _InstDesc1Size>0 ) _InstDesc1Size++; // Reserve '/0' terminator
  if ( _InstDesc2Size>0 ) _InstDesc2Size++; // Reserve '/0' terminator
  uint16_t _ConfISize=_ManISize+_InstDesc1Size+_InstDesc2Size;
  if ( ConfI!=0 && ConfISize<_ConfISize ) { // We can not fit new data, so release mem.
    free(ConfI); ConfI=0; ConfISize=0;
  }
  if ( ConfI==0 ) {
    ConfISize=_ConfISize;
    ConfI=(char*)(ConfISize>0?malloc(ConfISize):0);
    if ( _ManISize>0 ) {
      ManufacturerInformation=ConfI;
      ManufacturerInformation[0]='\0';
    } else ManufacturerInformation=0;
    if ( _InstDesc1Size>0 ) {
      InstallationDescription1=ConfI+_ManISize;
      InstallationDescription1[0]='\0';
    } else InstallationDescription1=0;
    if ( _InstDesc2Size>0 ) {
      InstallationDescription2=ConfI+_ManISize+_InstDesc1Size;
      InstallationDescription2[0]='\0';
    } else InstallationDescription2=0;
  }
  ConfILoaded=true;
  return ConfI;
}

#******************************************************************************
unsigned long#* tN2kDeviceList::tInternalDevice::InitTransmitPGNs(uint8_t count) {
  if (TransmitPGNs!=0 && TransmitPGNsSize<count ) { free(TransmitPGNs); TransmitPGNs=0; TransmitPGNsSize=0; } // Free old reservation
  if (TransmitPGNs==0) { TransmitPGNs=(unsigned long#*)malloc((count+1)*sizeof(unsigned long)); TransmitPGNsSize=count; }
  if (TransmitPGNs!=0) TransmitPGNs[0]=0;
  return TransmitPGNs;
}

#******************************************************************************
unsigned long#* tN2kDeviceList::tInternalDevice::InitReceivePGNs(uint8_t count) {
  if (ReceivePGNs!=0 && ReceivePGNsSize<count ) { free(ReceivePGNs); ReceivePGNs=0; ReceivePGNsSize=0; } // Free old reservation
  if (ReceivePGNs==0) { ReceivePGNs=(unsigned long#*)malloc((count+1)*sizeof(unsigned long)); ReceivePGNsSize=count; }
  if (ReceivePGNs!=0) ReceivePGNs[0]=0;
  return ReceivePGNs;
}
