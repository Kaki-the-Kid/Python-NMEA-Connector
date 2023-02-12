'''
/************************************************************************//**
 * \file    N2kGroupFunction.h
 * \brief   This File contains the definition of the GroupFunctionHandler
 * 
 * Group functions can be used on the bus, to organize the devices on 
 * the network (e.g. setting a device’s PGN instances)
 * 
 * \todo Please double check and give maybe some more context
 * 
 * \sa [NMEA2000 Documentation PGN 126208 ] (https://www.nmea.org/Assets/20140109%20nmea-2000-corrigendum-tc201401031%20pgn%20126208.pdf)
 * ********************************************************************/
'''

"""
The NMEA 2000 group function is a way of grouping related data within the NMEA 2000 
communication standard. NMEA 2000 defines a set of messages, or Parameter Group Numbers (PGNs), 
that are used to communicate different types of data between devices on the network.

The group function provides a way of grouping similar PGNs into functional groups, making it 
easier for devices to identify and process the data they need. For example, the group function 
can be used to group PGNs related to vessel heading, rate of turn, and attitude into a single 
functional group.

Each PGN in NMEA 2000 is assigned a group function code, which is used to specify the functional 
group to which the PGN belongs. The group function code is a 3-bit field within the PGN, and there 
are eight possible group function codes defined in the standard.

The group function helps to ensure that devices on the network are able to efficiently and 
effectively process the data they need, while ignoring other data that is not relevant to their 
operation. This helps to reduce the amount of unnecessary data on the network and improve overall 
performance.
"""







'''
/************************************************************************//**
 * \enum  tN2kGroupFunctionCode
 * \brief FunctionCode for the group function
 * 
 * There are seven group functions associated with PGN 126208.  
 * The Write Fields group function may be used to modify a device's
 * factory default PGN instances to create a unique device with unique 
 * PGN instance numbers.  
 * The Read Fields group function can be similarly used to interrogate 
 * the current PGN instance values of any PGNs not being sent periodically.
 *
 */
 '''
enum tN2kGroupFunctionCode {
        '''/**
         * This message requests the transmission of a specific set of data 
         * in a Parameter Group by setting variable parameters within 
         * theParameter Group specified by the field number. Field number 
         * and parameter value may appear in any order in this message. 
         * When multiple fields and parameters are specified the request is 
         * treated as an "AND" function. This PGN may be used to set the 
         * transmission interval and the delay before the first transmission.
         */'''
        N2kgfc_Request=0,
        /**
         * The Command Group Function message is directed to a specific 
         * address, the Global Address (255) shall not be used. This command 
         * sets the value of one, some or all parameters in a Parameter Group. 
         * The number of parameters to set is in field 5, then follows the 
         * field number and the new value repeated for each of them. A 
         * Parameter Group may contain one group of parameters out of multiple 
         * instances where the instance number of the group is given in one 
         * field. A command to set any parameter of such a group must contain 
         * the field number and value of the group instance number.
         */
        N2kgfc_Command=1,
        /**
         * The Acknowledgement reply is transmitted in response to a Request, 
         * Command, Read or Write Group Function Message. The Acknowledge Group 
         * Function shall be transmitted in response to every Command Message 
         * received, indicating acknowledgement or containing the appropriate 
         * Error Code. The Acknowledge Group Function is only required in 
         * response to a Request, Read orWrite Group Function that cannot be 
         * satisfied. The Acknowledge Group function shall transmit all fields 
         * applicable to the Group Function being acknowledged, fields where 
         * the error does not exist are set to 0x0 (No Error/Acknowledge).
         */
        N2kgfc_Acknowledge=2,
        /**
         * This Read Fields Group Function provides a means to read specific 
         * fields in a PGN. When Field 2 (PGN number) contains a 
         * non-proprietary PGN number, field 3, field 4 and field 5 are not 
         * included in this message. If the receiver of this message can 
         * comply, the receiver will send to the transmitter a Read Fields 
         * Reply Group Function. If the receiver cannot comply, an Acknowledge 
         * Group Function shall be sent.
         */
        N2kgfc_Read=3,
        /**
         * The Read Fields Reply Group Function is a reply to the Read Fields 
         * Group Function. When the Read Fields Group Function is received, if 
         * the receiver can comply, the Read Fields Reply Group Function will 
         * be transmitted with the resulting read values.
         */
        N2kgfc_ReadReply=4,
        /**
         * This Write Group Function is especially useful when configuring an 
         * instance or reference to be used by a node when transmitting a PGN 
         * such as PGN 127508. Use Fields 7, 9 and 10 to identify the currently 
         * assigned instance value. Use Fields 8, 13 and 14 to identify the new 
         * assigned instance value. When Field 2 (PGN number) contains a 
         * non-proprietary PGN number, field 3, field 4 and field 5 are not 
         * included in this message. If the receiver of this message can 
         * comply, the receiver will send to the transmitter a Write Fields 
         * Reply Group Function. If the receiver cannot comply, an Acknowledge 
         * Group Function shall be sent.
         */
        N2kgfc_Write=5,
        /**
         * The Write Fields Reply Group Function is a reply to the Write Fields 
         * Group Function. When the Write Fields Group Function is received, if 
         * the receiver can comply, the Write Fields Reply Group Function will 
         * be transmitted with the resulting values. If a parameter value is 
         * accepted then the modified value will be returned. If a parameter 
         * value is not accepted, the original value will be returned.
         */
        N2kgfc_WriteReply=6
      };

/************************************************************************//**
 * \enum  tN2kGroupFunctionPGNErrorCode
 * \brief PGN error code used by acknowledge group function
 * 
 * This error code carried inside the acknowledge group function gives 
 * information, if the Request, Command, Read or Write Group Function 
 * Message can be satisfied by the receiving device.
 */
enum tN2kGroupFunctionPGNErrorCode {
                            /** Acknowledge positiv, no error */
                            N2kgfPGNec_Acknowledge=0,
                            /** PGN is not supported */
                            N2kgfPGNec_PGNNotSupported=1,
                            /** PGN is temporarily not available */
                            N2kgfPGNec_PGNTemporarilyNotAvailable=2,
                            /** Access denied */
                            N2kgfPGNec_AccessDenied=3,
                            /** Request or Command is not supported */
                            N2kgfPGNec_RequestOrCommandNotSupported=4,
                            /** Definer Tag is not supported */
                            N2kgfPGNec_DefinerTagNotSupported=5,
                            /** Read or Write is not supported */
                            N2kgfPGNec_ReadOrWriteNotSupported=6
                          };

/************************************************************************//**
 * \enum  tN2kGroupFunctionTransmissionOrPriorityErrorCode
 * \brief Error codes Transmit interval used by acknowledge group function
 * 
 * This error code carried inside the acknowledge group function gives 
 * information, if the Request, Command, Read or Write Group Function 
 * Message can be satisfied by the receiving device.
 */
enum tN2kGroupFunctionTransmissionOrPriorityErrorCode {
                            /** Acknowledge positiv, no error */
                            N2kgfTPec_Acknowledge=0,
                            /** Transmit Interval /Priority not supported */
                            N2kgfTPec_TransmitIntervalOrPriorityNotSupported=1,
                            /** Transmit interval is less than measurement/
                             * calculation interval */
                            N2kgfTPec_TransmitIntervalIsLessThanMeasurementInterval=2,
                            /** Access denied */
                            N2kgfTPec_AccessDenied=3,
                            /** Request is not supported */
                            N2kgfTPec_RequestNotSupported=4
                          };

/************************************************************************//**
 * \enum  tN2kGroupFunctionParameterErrorCode
 * \brief Error Codes Command used by acknowledge group function
 * 
 * This error code carried inside the acknowledge group function gives 
 * information, if the Request, Command, Read or Write Group Function 
 * Message can be satisfied by the receiving device.
 */
enum tN2kGroupFunctionParameterErrorCode {
                            /** Acknowledge positiv, no error */
                            N2kgfpec_Acknowledge=0,
                            /** Invalid request or command parameter field */
                            N2kgfpec_InvalidRequestOrCommandParameterField=1,
                            /** Temporarily unable to comply */
                            N2kgfpec_TemporarilyUnableToComply=2,
                            /** Request or command parameter out-of-range */
                            N2kgfpec_RequestOrCommandParameterOutOfRange=3,
                            /** Access denied */
                            N2kgfpec_AccessDenied=4,
                            /** Request or Command is not supported */
                            N2kgfpec_RequestOrCommandNotSupported=5,
                            /** Read or Write is not supported */
                            N2kgfpec_ReadOrWriteIsNotSupported=6
                          };

class tNMEA2000;
/************************************************************************//**
 * \class   tN2kGroupFunctionHandler
 * \brief   Handler class for Group Functions
 * \ingroup group_coreSupplementary
 * 
 * This class handles all functions which are needed to respond to group 
 * function messages. NMEA 2000 definition requires that devices should 
 * respond group function messages. This class is default handler, which 
 * simply responds “unsupported” for all queries. 
 * 
 * \todo More description is needed, please review
 *
 */
class tN2kGroupFunctionHandler {
  public:
    /**********************************************************************//**
     * \brief 
     * 
     * \todo Add a proper documentation
     * 
     * \tparam T          
     * \param FieldVal 
     * \param MatchVal 
     * \param Mask 
     * \param Match 
     * \param ErrorCode 
     */
    template <typename T> void MatchRequestField(T FieldVal, T MatchVal, T Mask, bool &Match, tN2kGroupFunctionParameterErrorCode &ErrorCode)
    {
      if ( (FieldVal&Mask)!=MatchVal ) {
        ErrorCode=N2kgfpec_RequestOrCommandParameterOutOfRange;
        Match=false;
      } else ErrorCode=N2kgfpec_Acknowledge;
    }

    /*********************************************************************//**
     * \brief 
     *
     * \todo Add a proper documentation
     *
     * \param FieldVal {type} 
     * \param MatchVal {type} 
     * \param Match {type} 
     * \param ErrorCode {type} 
     */
    void MatchRequestField(const char * FieldVal, const char * MatchVal, bool &Match, tN2kGroupFunctionParameterErrorCode &ErrorCode)
    {
      Match&=(strcmp(FieldVal,MatchVal)==0);
      ErrorCode = ( Match ? N2kgfpec_Acknowledge : N2kgfpec_RequestOrCommandParameterOutOfRange );
    }

  private:
    /** \brief Pointer to the Group function handler */
    tN2kGroupFunctionHandler *pNext;
    friend class tNMEA2000;

  protected:
    /** \brief Parameter Group Number (PGN) of this Group Function*/
    unsigned long PGN;
    /** \brief Flag, if the Parameter Group is proprietary   */
    bool Proprietary;
    /** \brief NMEA2000 object in order to send messages to the bus   */
    tNMEA2000 *pNMEA2000;

  protected:
    // deprecated! Use new version with offset test too.
    // deprecated attribute does not work with overrided methods, so easier just force users to update code.
    // virtual tN2kGroupFunctionTransmissionOrPriorityErrorCode GetRequestGroupFunctionTransmissionOrPriorityErrorCode(uint32_t TransmissionInterval) __attribute__ ((deprecated));
  
    /**********************************************************************//**
     * \brief Get the Request Group Function Transmission Or Priority Error 
     *        Code object
     * 
     * This is default handler for Complex Request transmission interval 
     * setting. Overwrite it, if your PGN will support changing interval.  
     * If you support changing interval and offset for your PGN, you can
     * either overwrite function or set UseLimits and provide interval
     * and offset limits.
     * 
     * \note see Code  In NMEA tests "C.3.13.2  Expanded Acknowledgment 
     * Message Timing" tool is Old and does not know interval 
     * 0xFFFFFFFE=Restore Default Interval. So to pass that test, that has
     * to be commented out.
     *  
     * \param TransmissionInterval    Interval for Transmission
     * \param TransmissionIntervalOffset Offset for Transmission Interval
     * \param UseIntervalLimits       Use the Intervall limits  
     * \param IntervalMax             Maximum Interval
     * \param IntervalMin             Minimum Interval
     * \param UseOffsetLimits         Use Offset limits 
     * \param OffsetMax               Maximum offset
     * 
     * \return N2kgfTPec_Acknowledge -> if TransmissionInterval = 0xFFFFFFFF 
     *                                or TransmissionInterval = 0xFFFFFFFE
     *                                (Restore Default Interval)
     * \return N2kgfTPec_TransmitIntervalOrPriorityNotSupported -> all other
     *                                                            intervals
     */
     virtual tN2kGroupFunctionTransmissionOrPriorityErrorCode GetRequestGroupFunctionTransmissionOrPriorityErrorCode(
                              uint32_t TransmissionInterval,
                              uint16_t TransmissionIntervalOffset,
                              bool UseIntervalLimits=false,
                              uint32_t IntervalMax=N2k_MAX_TRANSMISSION_INTERVAL,
                              uint32_t IntervalMin=50,
                              bool UseOffsetLimits=false,
                              uint16_t OffsetMax=N2k_MAX_TRANSMISSION_INTERVAL_OFFSET
                              );
    
    /**********************************************************************//**
     * \brief Default request handler for group function requests for PGN.
     *
     * Default response is "not supported". Certified devices must respond
     * to requests!
     * 
     * \param N2kMsg      Reference to a N2kMsg Object, 
     *                    Output: NMEA2000 message ready to be send.
     * \param TransmissionInterval    Transmission interval [ms]
     * \param TransmissionIntervalOffset  Offset to the transmission 
     *                                    interval [10ms]
     * \param NumberOfParameterPairs  Number of parameter pairs contained
     *                                inside the group function message
     * \param iDev        Index off the device in \ref tNMEA2000::Devices
     * 
     * \return true -> always returns true
     */
    virtual bool HandleRequest(const tN2kMsg &N2kMsg,
                               uint32_t TransmissionInterval,
                               uint16_t TransmissionIntervalOffset,
                               uint8_t  NumberOfParameterPairs,
                               int iDev);
                               
    /**********************************************************************//**
     * \brief Handle the response to Group Function "Command"
     *
     * Default response is "not supported". 
     *  
     * \param N2kMsg      Reference to a N2kMsg Object, 
     *                    Output: NMEA2000 message ready to be send.
     * \param PrioritySetting     Priority Setting
     * \param NumberOfParameterPairs  Number of parameter pairs contained
     *                                inside the group function message
     * \param iDev        Index off the device in \ref tNMEA2000::Devices
     * 
     * \return true -> always returns true
     */
    virtual bool HandleCommand(const tN2kMsg &N2kMsg, uint8_t PrioritySetting, uint8_t NumberOfParameterPairs, int iDev);

    /**********************************************************************//**
     * \brief Default handle function for Acknowledge a Group Function
     * 
     * This function handles Acknowledge group function, which is response 
     * for Request, Command, ReadFields or WriteFields group function. 
     * 
     * \note As default, this simply returns true meaning that received
     *       acknowledge has been handled. So you need to override this,
     *        if your device will send one of those commands.
     * 
     * \param N2kMsg      Reference to a N2kMsg Object, 
     *                    Output: NMEA2000 message ready to be send.
     * \param PGNErrorCode  PGN Error Code, see 
     *                      \ref tN2kGroupFunctionPGNErrorCode
     * \param TransmissionOrPriorityErrorCode   see 
     *                  \ref tN2kGroupFunctionTransmissionOrPriorityErrorCode
     * \param NumberOfParameterPairs     Number of parameter pairs contained
     *                                   inside the group function message
     * \param iDev        Index off the device in \ref tNMEA2000::Devices
     * 
     * \return true -> As default, simply return true meaning that received
     *                acknowledge has been handled
     *
     */
    virtual bool HandleAcknowledge(const tN2kMsg &N2kMsg,
                                   tN2kGroupFunctionPGNErrorCode PGNErrorCode,
                                   tN2kGroupFunctionTransmissionOrPriorityErrorCode TransmissionOrPriorityErrorCode,
                                   uint8_t NumberOfParameterPairs,
                                   int iDev);

    /**********************************************************************//**
     * \brief Handle the response to Group Function "Read Fields"
     *
     * 
     * 
     * \param N2kMsg      Reference to a N2kMsg Object, 
     *                    Output: NMEA2000 message ready to be send.
     * \param ManufacturerCode    Manufacturer Code, This will be set to 
     *                            0xffff for non-propprietary PNGs
     * \param IndustryGroup       Industry Group Code, This will be set to 
     *                            0xff for non-propprietary PNGs
     * \param UniqueID            Unique ID for the device
     * \param NumberOfSelectionPairs   Number of Selection pairs contained
     *                                 inside the group function message
     * \param NumberOfParameterPairs   Number of parameter pairs contained
     *                                 inside the group function message
     * \param iDev          Index off the device in \ref tNMEA2000::Devices
     * 
     * \return true   ->  always returns true
     * 
     */
    virtual bool HandleReadFields(const tN2kMsg &N2kMsg,
                                  uint16_t ManufacturerCode, 
                                  uint8_t IndustryGroup,
                                  uint8_t UniqueID,
                                  uint8_t NumberOfSelectionPairs,
                                  uint8_t NumberOfParameterPairs,
                                  int iDev);
    
    /**********************************************************************//**
     * \brief Handle the response to Group Function "Read Fields Reply"
     *
     * \warning Under construction! No real code inside, always returns true!
     * 
     * \param N2kMsg      Reference to a N2kMsg Object, 
     *                    Output: NMEA2000 message ready to be send.
     * \param iDev          Index off the device in \ref tNMEA2000::Devices
     * 
     * \return true -> Always
     */
    virtual bool HandleReadFieldsReply(const tN2kMsg &N2kMsg,int iDev);

    /**********************************************************************//**
     * \brief Handle the response to Group Function "Write Fields"
     *
     * 
     * 
     * \param N2kMsg      Reference to a N2kMsg Object, 
     *                    Output: NMEA2000 message ready to be send.
     * \param ManufacturerCode    Manufacturer Code, This will be set to 
     *                            0xffff for non-propprietary PNGs
     * \param IndustryGroup       Industry Group Code, This will be set to 
     *                            0xff for non-propprietary PNGs
     * \param UniqueID            Unique ID for the device
     * \param NumberOfSelectionPairs   Number of Selection pairs contained
     *                                 inside the group function message
     * \param NumberOfParameterPairs   Number of parameter pairs contained
     *                                 inside the group function message
     * \param iDev          Index off the device in \ref tNMEA2000::Devices
     * 
     * \return true   ->  always returns true
     * 
     */
    virtual bool HandleWriteFields(const tN2kMsg &N2kMsg,
                                  uint16_t ManufacturerCode, 
                                  uint8_t IndustryGroup, 
                                  uint8_t UniqueID,
                                  uint8_t NumberOfSelectionPairs,
                                  uint8_t NumberOfParameterPairs,
                                  int iDev);

    /**********************************************************************//**
     * \brief Handle the response to Group Function "Write Fields Reply"
     *
     * \warning Under construction! No real code inside, always returns true!
     * 
     * \param N2kMsg      Reference to a N2kMsg Object, 
     *                    Output: NMEA2000 message ready to be send.
     * \param iDev          Index off the device in \ref tNMEA2000::Devices
     * 
     * \return true -> Always
     */
    virtual bool HandleWriteFieldsReply(const tN2kMsg &N2kMsg,int iDev);

  public:
    /**********************************************************************//**
     * \brief Construct a new t N2k Group Function Handler object
     *
     * \param _pNMEA2000  Pointer to an NMEA2000 object, see \ref tNMEA2000
     * \param _PGN        Parameter Group Number associated with this 
     *                    Group function
     */
    tN2kGroupFunctionHandler(tNMEA2000 *_pNMEA2000, unsigned long _PGN);

    /**********************************************************************//**
     * \brief Handle for a Group Function
     *
     * \param N2kMsg      Reference to a N2kMsg Object, 
     *                    This message is an Group function message
     * \param GroupFunctionCode     Code for Group Function, see 
     *                              \ref tN2kGroupFunctionCode
     * \param PGNForGroupFunction    PGN for the Group function
     * \param iDev          Index off the device in \ref tNMEA2000::Devices
     * 
     * \return true   -> Group Function was handled properly 
     * \return false  -> if (PGN!=PGNForGroupFunction && PGN!=0)
     */
    virtual bool Handle(const tN2kMsg &N2kMsg, tN2kGroupFunctionCode GroupFunctionCode, unsigned long PGNForGroupFunction, int iDev);

    /**********************************************************************//**
     * \brief Get the PGN for the Group Function out of a n2k message
     * 
     * This is a static function for PGN 126208 handling. The 
     * function extracts the PGN (as 3 bytes) from the given 
     * N2K message.
     *
     * \param N2kMsg      Reference to a N2kMsg Object, 
     *                    This message is an Group function message
     * \return unsigned long -> PGN for Group Function
     */
    static unsigned long GetPGNForGroupFunction(const tN2kMsg &N2kMsg);

    /**********************************************************************//**
     * \brief Parse group function code and PGN from the message
     *
     * This is a static function for PGN 126208 handling. 
     * 
     * \param N2kMsg      Reference to a N2kMsg Object, 
     *                    This message is an Group function message
     * \param GroupFunctionCode   Group Function Code, see \ref 
     *                            tN2kGroupFunctionCode
     * \param PGNForGroupFunction PGN for the Group function
     * 
     * \return true 
     * \return false -> if (N2kMsg.PGN!=126208L)
     */
    static bool Parse(const tN2kMsg &N2kMsg,
                            tN2kGroupFunctionCode &GroupFunctionCode,
                            unsigned long &PGNForGroupFunction);

    /**********************************************************************//**
     * \brief Parse parameters from group function Request message
     *
     * This is a static function for PGN 126208 handling. 
     * 
     * \param N2kMsg      Reference to a N2kMsg Object, 
     *                    This message is an Group function message
     * \param TransmissionInterval    Transmission interval
     * \param TransmissionIntervalOffset Offset to the transmission interval
     * \param NumberOfParameterPairs   Number of parameter pairs contained
     *                                 inside the group function message
     * 
     * \return true 
     * \return false -> if (N2kMsg.PGN!=126208L)
     */
    static bool ParseRequestParams(const tN2kMsg &N2kMsg,
                               uint32_t &TransmissionInterval,
                               uint16_t &TransmissionIntervalOffset,
                               uint8_t  &NumberOfParameterPairs);

    /**********************************************************************//**
     * \brief Get start Index of pair parameters on the group function 
     * Request message
     *
     * This is a static function for PGN 126208 handling. 
     *
     * \param N2kMsg      Reference to a N2kMsg Object, 
     *                    This message is an Group function message
     * \param Index       Index where the Request Pair Parameters start
     * 
     * \return true 
     * \return false -> if (N2kMsg.PGN!=126208L)
     */
    static bool StartParseRequestPairParameters(const tN2kMsg &N2kMsg, int &Index);

    /**********************************************************************//**
     * \brief Parse parameters from a group function Command message
     *
     * This is a static function for PGN 126208 handling. 
     * 
     * \param N2kMsg      Reference to a N2kMsg Object, 
     *                    This message is an Group function message
     * \param PrioritySetting     Priority setting
     * \param NumberOfParameterPairs   Number of parameter pairs contained
     *                                 inside the group function message
     * 
     * \return true 
     * \return false -> if (N2kMsg.PGN!=126208L)
     */
    static bool ParseCommandParams(const tN2kMsg &N2kMsg,
                               uint8_t &PrioritySetting,
                               uint8_t &NumberOfParameterPairs);

    /**********************************************************************//**
     * \brief Get start Index of pair parameters on the group function 
     * Command message
     *
     * This is a static function for PGN 126208 handling. 
     *
     * \param N2kMsg      Reference to a N2kMsg Object, 
     *                    This message is an Group function message
     * \param Index       Index where the Command Pair Parameters start
     * 
     * \return true 
     * \return false -> if (N2kMsg.PGN!=126208L)
     */
    static bool StartParseCommandPairParameters(const tN2kMsg &N2kMsg, int &Index);

    /**********************************************************************//**
     * \brief Parse parameters from group function acknowledge message
     *
     * This is a static function for PGN 126208 handling. 
     * 
     * \param N2kMsg      Reference to a N2kMsg Object, 
     *                    This message is an Group function message
     * \param PGNErrorCode  PGN error code, see \ref 
     *                      tN2kGroupFunctionPGNErrorCode
     * \param TransmissionOrPriorityErrorCode Transmission or Priority error
     *     code, see \ref tN2kGroupFunctionTransmissionOrPriorityErrorCode
     * \param NumberOfParameterPairs   Number of parameter pairs contained
     *                                 inside the group function message
     * 
     * \return true 
     * \return false -> if (N2kMsg.PGN!=126208L)
     */
    static bool ParseAcknowledgeParams(const tN2kMsg &N2kMsg,
                               tN2kGroupFunctionPGNErrorCode &PGNErrorCode,
                               tN2kGroupFunctionTransmissionOrPriorityErrorCode &TransmissionOrPriorityErrorCode,
                               uint8_t &NumberOfParameterPairs);

    /**********************************************************************//**
     * \brief Get start Index of pair parameters on the group function 
     * ReadOrWrite message
     *
     * This is a static function for PGN 126208 handling. 
     *
     * \param N2kMsg      Reference to a N2kMsg Object, 
     *                    This message is an Group function message
     * \param Proprietary Group function is proprietary
     * \param Index       Index where the Command Pair Parameters start
     * 
     * \return true 
     */
    static bool StartParseReadOrWriteParameters(const tN2kMsg &N2kMsg, bool Proprietary, int &Index);

    /**********************************************************************//**
     * \brief Parse parameters from group function ReadOrWrite message
     *
     * \param N2kMsg      Reference to a N2kMsg Object, 
     *                    This message is an Group function message
     * \param ManufacturerCode    Manufacturer Code, This will be set to 
     *                            0xffff for non-propprietary PNGs
     * \param IndustryGroup       Industry Group Code, This will be set to 
     *                            0xff for non-propprietary PNGs
     * \param UniqueID            Unique ID for the device
     * \param NumberOfSelectionPairs   Number of Selection pairs contained
     *                                 inside the group function message
     * \param NumberOfParameterPairs   Number of parameter pairs contained
     *                                 inside the group function message
     * \param Proprietary Group function is proprietary
     * 
     * \return true 
     * \return false -> if (N2kMsg.PGN!=126208L)
     */
    static bool ParseReadOrWriteParams(const tN2kMsg &N2kMsg,
                               uint16_t &ManufacturerCode,
                               uint8_t &IndustryGroup,
                               uint8_t &UniqueID,
                               uint8_t &NumberOfSelectionPairs,
                               uint8_t &NumberOfParameterPairs,
                               bool Proprietary=false);
    
    /**********************************************************************//**
     * \brief Setting up the group function message for Read Reply
     * 
     *
     * \param N2kMsg      Reference to a N2kMsg Object, 
     *                    Output: NMEA2000 message ready to be send.
     * \param Destination address of Destination 
     * \param PGN         Parameter group Number
     * \param ManufacturerCode    Manufacturer Code, This will be set to 
     *                            0xffff for non-propprietary PNGs
     * \param IndustryGroup       Industry Group Code, This will be set to 
     *                            0xff for non-propprietary PNGs
     * \param UniqueID            Unique ID for the device
     * \param NumberOfSelectionPairs   Number of Selection pairs contained
     *                                 inside the group function message
     * \param NumberOfParameterPairs   Number of parameter pairs contained
     *                                 inside the group function message
     * \param Proprietary Is this a proprietary group function
     */
    static void SetStartReadReply(tN2kMsg &N2kMsg, unsigned char Destination, unsigned long PGN,
                               uint16_t ManufacturerCode,
                               uint8_t IndustryGroup,
                               uint8_t UniqueID,
                               uint8_t NumberOfSelectionPairs,
                               uint8_t NumberOfParameterPairs,
                               bool Proprietary);

    /**********************************************************************//**
     * \brief Setting up the group function message for Write Reply
     * 
     *
     * \param N2kMsg      Reference to a N2kMsg Object, 
     *                    Output: NMEA2000 message ready to be send.
     * \param Destination address of Destination 
     * \param PGN         Parameter group Number
     * \param ManufacturerCode    Manufacturer Code, This will be set to 
     *                            0xffff for non-propprietary PNGs
     * \param IndustryGroup       Industry Group Code, This will be set to 
     *                            0xff for non-propprietary PNGs
     * \param UniqueID            Unique ID for the device
     * \param NumberOfSelectionPairs   Number of Selection pairs contained
     *                                 inside the group function message
     * \param NumberOfParameterPairs   Number of parameter pairs contained
     *                                 inside the group function message
     * \param Proprietary Is this a proprietary group function
     */
    static void SetStartWriteReply(tN2kMsg &N2kMsg, unsigned char Destination, unsigned long PGN,
                               uint16_t ManufacturerCode,
                               uint8_t IndustryGroup,
                               uint8_t UniqueID,
                               uint8_t NumberOfSelectionPairs,
                               uint8_t NumberOfParameterPairs,
                               bool Proprietary);

    /**********************************************************************//**
     * \brief Setting up the group function message for Acknowledge
     *
     * \param N2kMsg      Reference to a N2kMsg Object, 
     *                    Output: NMEA2000 message ready to be send.
     * \param Destination address of Destination 
     * \param PGN         Parameter group Number
     * \param PGNErrorCode  PGN error code, see \ref 
     *                      tN2kGroupFunctionPGNErrorCode
     * \param TransmissionOrPriorityErrorCode Transmission or Priority error
     *     code, see \ref tN2kGroupFunctionTransmissionOrPriorityErrorCode
     * \param NumberOfParameterPairs   Number of parameter pairs contained
     *                                 inside the group function message
     */
    static void SetStartAcknowledge(tN2kMsg &N2kMsg, unsigned char Destination, unsigned long PGN,
                                         tN2kGroupFunctionPGNErrorCode PGNErrorCode,
                                         tN2kGroupFunctionTransmissionOrPriorityErrorCode TransmissionOrPriorityErrorCode,
                                         uint8_t NumberOfParameterPairs=0);

    /**********************************************************************//**
     * \brief Change the PGN error code for a group function message
     *
     * \param N2kMsg      Reference to a N2kMsg Object, 
     *                    This message is an Group function message
     * \param PGNErrorCode  PGN error code, see \ref 
     *                      tN2kGroupFunctionPGNErrorCode
     */
    static void ChangePNGErrorCode(tN2kMsg &N2kMsg, tN2kGroupFunctionPGNErrorCode PGNErrorCode);

    /**********************************************************************//**
     * \brief Change the Transmission or Priority error code code for 
     *        a group function message
     *
     * \param N2kMsg      Reference to a N2kMsg Object, 
     *                    This message is an Group function message
     * \param TransmissionOrPriorityErrorCode Transmission or Priority error
     *     code, see \ref tN2kGroupFunctionTransmissionOrPriorityErrorCode
     */
    static void ChangeTransmissionOrPriorityErrorCode(tN2kMsg &N2kMsg, tN2kGroupFunctionTransmissionOrPriorityErrorCode TransmissionOrPriorityErrorCode);

    /**********************************************************************//**
     * \brief Add parameter to a Acknowledge group function message
     *
     * \param N2kMsg      Reference to a N2kMsg Object, 
     *                    This message is an Group function message
     * \param ParameterPairIndex Index of the parameter pair
     * \param ErrorCode   Error code to be added to the message
     */
    static void AddAcknowledgeParameter(tN2kMsg &N2kMsg,
                                         uint8_t ParameterPairIndex,
                                         tN2kGroupFunctionParameterErrorCode ErrorCode=N2kgfpec_ReadOrWriteIsNotSupported);

    /**********************************************************************//**
     * \brief Send out an Acknowledge message 
     *
     * \param pNMEA2000     NMEA2000 oject
     * \param Destination   address of Destination 
     * \param iDev          Index off the device in \ref tNMEA2000::Devices
     * \param PGN           Parameter group Number
     * \param PGNErrorCode  PGN error code, see \ref 
     *                      tN2kGroupFunctionPGNErrorCode
     * \param TransmissionOrPriorityErrorCode Transmission or Priority error
     *     code, see \ref tN2kGroupFunctionTransmissionOrPriorityErrorCode
     * \param NumberOfParameterPairs   Number of parameter pairs contained
     *                                 inside the group function message
     * \param ParameterErrorCodeForAll Error code for all parameter sets, see 
     *                                 \ref tN2kGroupFunctionParameterErrorCode
     */
    static void SendAcknowledge(tNMEA2000 *pNMEA2000, unsigned char Destination, int iDev, unsigned long PGN,
                                         tN2kGroupFunctionPGNErrorCode PGNErrorCode,
                                         tN2kGroupFunctionTransmissionOrPriorityErrorCode TransmissionOrPriorityErrorCode,
                                         uint8_t NumberOfParameterPairs=0,
                                         tN2kGroupFunctionParameterErrorCode ParameterErrorCodeForAll=N2kgfpec_Acknowledge);

};

#endif

#endif


/*
N2kGroupFunction.cpp

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
*/

#include "N2kGroupFunction.h"
#include "NMEA2000.h"

#if !defined(N2K_NO_GROUP_FUNCTION_SUPPORT)

//*****************************************************************************
tN2kGroupFunctionHandler::tN2kGroupFunctionHandler(tNMEA2000 *_pNMEA2000, unsigned long _PGN)  {
  pNext=0;
  pNMEA2000=_pNMEA2000;
  PGN=_PGN;
  Proprietary=tNMEA2000::IsProprietaryMessage(PGN);
}

//*****************************************************************************
bool tN2kGroupFunctionHandler::Handle(const tN2kMsg &N2kMsg, tN2kGroupFunctionCode GroupFunctionCode, unsigned long PGNForGroupFunction, int iDev) {
  if ( PGN!=PGNForGroupFunction && PGN!=0 ) return false;

  bool handled=false;
  uint16_t ManufacturerCode;
  uint8_t IndustryGroup;
  uint8_t UniqueID;
  uint8_t NumberOfSelectionPairs;
  uint8_t NumberOfParameterPairs;
  bool Propr=(PGN!=0?Proprietary:tNMEA2000::IsProprietaryMessage(PGNForGroupFunction));

  switch (GroupFunctionCode) {
    case N2kgfc_Request:
      uint32_t TransmissionInterval;
      uint16_t TransmissionIntervalOffset;

        if (ParseRequestParams(N2kMsg,TransmissionInterval,TransmissionIntervalOffset,NumberOfParameterPairs)) {
          handled=HandleRequest(N2kMsg,TransmissionInterval,TransmissionIntervalOffset,NumberOfParameterPairs,iDev);
        }
      break;
    case N2kgfc_Command:
      uint8_t PrioritySetting;

        if ( tNMEA2000::IsBroadcast(N2kMsg.Destination) ) {
          handled=true;  // We can mark this handled, since command is not allowed to broadcast.
        } else {
          if (ParseCommandParams(N2kMsg,PrioritySetting,NumberOfParameterPairs)) {
            handled=HandleCommand(N2kMsg,PrioritySetting,NumberOfParameterPairs,iDev);
          }
        }
      break;
    case N2kgfc_Acknowledge:
      tN2kGroupFunctionPGNErrorCode PGNErrorCode;
      tN2kGroupFunctionTransmissionOrPriorityErrorCode TransmissionOrPriorityErrorCode;

        if (ParseAcknowledgeParams(N2kMsg,PGNErrorCode,TransmissionOrPriorityErrorCode,NumberOfParameterPairs)) {
          handled=HandleAcknowledge(N2kMsg,PGNErrorCode,TransmissionOrPriorityErrorCode,NumberOfParameterPairs,iDev);
        }
      break;
    case N2kgfc_Read:
        if ( tNMEA2000::IsBroadcast(N2kMsg.Destination) ) {
          handled=true;  // We can mark this handled, since read is not allowed to broadcast.
        } else {
          if (ParseReadOrWriteParams(N2kMsg,ManufacturerCode,IndustryGroup,UniqueID,NumberOfSelectionPairs,NumberOfParameterPairs,Propr)) {
            handled=HandleReadFields(N2kMsg,ManufacturerCode,IndustryGroup,UniqueID,NumberOfSelectionPairs,NumberOfParameterPairs,iDev);
          }
        }
      break;
    case N2kgfc_ReadReply:
      handled=true;
      break;
    case N2kgfc_Write:
        if ( tNMEA2000::IsBroadcast(N2kMsg.Destination) ) {
          handled=true;  // We can mark this handled, since write is not allowed to broadcast.
        } else {
          if (ParseReadOrWriteParams(N2kMsg,ManufacturerCode,IndustryGroup,UniqueID,NumberOfSelectionPairs,NumberOfParameterPairs,Propr)) {
            handled=HandleWriteFields(N2kMsg,ManufacturerCode,IndustryGroup,UniqueID,NumberOfSelectionPairs,NumberOfParameterPairs,iDev);
          }
        }
      break;
    case N2kgfc_WriteReply:
      handled=true;
      break;

  }

  return handled;
}

//*****************************************************************************
tN2kGroupFunctionTransmissionOrPriorityErrorCode tN2kGroupFunctionHandler::GetRequestGroupFunctionTransmissionOrPriorityErrorCode(
                              uint32_t TransmissionInterval,
                              uint16_t TransmissionIntervalOffset,
                              bool UseIntervalLimits,
                              uint32_t IntervalMax,
                              uint32_t IntervalMin,
                              bool UseOffsetLimits,
                              uint16_t OffsetMax
                              ) {
  // In NMEA tool v2.0 tests "C.3.13.2  Expanded Acknowledgment Message Timing" tool is Old
  // and does not know interval 0xFFFFFFFE=Restore Default Interval. So to pass
  // that test, that has to be commented out
  return ( (TransmissionInterval==0xFFFFFFFF     // No change
            || TransmissionInterval==0xFFFFFFFE  // Restore default
            || TransmissionInterval==0           // Turn off
            || ( UseIntervalLimits && TransmissionInterval>=IntervalMin && TransmissionInterval<=IntervalMax)
           )
           &&
           // Specification for transmission interval is confusing. To keep test tool
           // happy, we accept also 0 offset
           (TransmissionIntervalOffset==0xffff
            || TransmissionIntervalOffset==0
            || ( UseOffsetLimits && TransmissionIntervalOffset<=OffsetMax)
           )
           ?
          N2kgfTPec_Acknowledge:
          N2kgfTPec_TransmitIntervalOrPriorityNotSupported);
}

//*****************************************************************************
bool tN2kGroupFunctionHandler::HandleRequest(const tN2kMsg &N2kMsg,
                               uint32_t TransmissionInterval,
                               uint16_t TransmissionIntervalOffset,
                               uint8_t  NumberOfParameterPairs,
                               int iDev) {

    // As default we respond with not supported.
    bool IsTxPGN=pNMEA2000->IsTxPGN(GetPGNForGroupFunction(N2kMsg),iDev);
    tN2kGroupFunctionTransmissionOrPriorityErrorCode TORec=GetRequestGroupFunctionTransmissionOrPriorityErrorCode(TransmissionInterval,TransmissionIntervalOffset);
    tN2kGroupFunctionPGNErrorCode PGNec=(IsTxPGN?N2kgfPGNec_PGNTemporarilyNotAvailable:N2kgfPGNec_PGNNotSupported);
    tN2kGroupFunctionParameterErrorCode PARec=N2kgfpec_Acknowledge;

    if ( PGNec==N2kgfPGNec_PGNNotSupported ) TORec=N2kgfTPec_Acknowledge; // Always acknoledge for unknown PGN.
    if ( PGNec==N2kgfPGNec_PGNTemporarilyNotAvailable ) {
      if ( TORec==N2kgfTPec_TransmitIntervalOrPriorityNotSupported ) { // Acknowledge PGN for known PGN but for invalid priority
        PGNec=N2kgfPGNec_Acknowledge;
      } else {
        TORec=N2kgfTPec_Acknowledge; //N2kgfTPec_RequestNotSupported;
      }
    }

    if ( !tNMEA2000::IsBroadcast(N2kMsg.Destination) ) {
      SendAcknowledge(pNMEA2000,N2kMsg.Source,iDev,GetPGNForGroupFunction(N2kMsg),
                      PGNec,
                      TORec,
                      NumberOfParameterPairs, PARec);
    }

    return true;
}

//*****************************************************************************
bool tN2kGroupFunctionHandler::HandleCommand(const tN2kMsg &N2kMsg, uint8_t PrioritySetting, uint8_t  NumberOfParameterPairs, int iDev) {

    // As default we respond with not supported.
    bool IsTxPGN=pNMEA2000->IsTxPGN(GetPGNForGroupFunction(N2kMsg),iDev);
    tN2kGroupFunctionPGNErrorCode PGNec=(IsTxPGN?N2kgfPGNec_Acknowledge:N2kgfPGNec_PGNNotSupported);
    tN2kGroupFunctionTransmissionOrPriorityErrorCode TORec=N2kgfTPec_Acknowledge;
    tN2kGroupFunctionParameterErrorCode PARec=N2kgfpec_Acknowledge;

		if (PrioritySetting != 0x08 || PrioritySetting != 0x0f || PrioritySetting != 0x09) TORec = N2kgfTPec_TransmitIntervalOrPriorityNotSupported;

    SendAcknowledge(pNMEA2000,N2kMsg.Source,iDev,GetPGNForGroupFunction(N2kMsg),
                    PGNec,
                    TORec,
                    NumberOfParameterPairs, PARec);

    return true;
}

//*****************************************************************************
bool tN2kGroupFunctionHandler::HandleAcknowledge(const tN2kMsg &/*N2kMsg*/,
                                   tN2kGroupFunctionPGNErrorCode /*PGNErrorCode*/,
                                   tN2kGroupFunctionTransmissionOrPriorityErrorCode /*TransmissionOrPriorityErrorCode*/,
                                   uint8_t /*ParameterCount*/,
                                   int /*iDev*/) {
    // As default, simply return true meaning that received acknowledge has been handled.
    return true;
}

//*****************************************************************************
bool tN2kGroupFunctionHandler::HandleReadFields(const tN2kMsg &N2kMsg,
                                  uint16_t /*ManufacturerCode*/, // This will be set to 0xffff for non-propprietary PNGs
                                  uint8_t /*IndustryGroup*/, // This will be set to 0xff for non-propprietary PNGs
                                  uint8_t /*UniqueID*/,
                                  uint8_t /*NumberOfSelectionPairs*/,
                                  uint8_t NumberOfParameterPairs,
                                  int iDev) {

    // As default we respond with not supported.
    bool IsTxPGN=pNMEA2000->IsTxPGN(GetPGNForGroupFunction(N2kMsg),iDev);
    tN2kGroupFunctionPGNErrorCode PGNec=(IsTxPGN?N2kgfPGNec_ReadOrWriteNotSupported:N2kgfPGNec_PGNNotSupported);
    SendAcknowledge(pNMEA2000,N2kMsg.Source,iDev,GetPGNForGroupFunction(N2kMsg),
                    PGNec,
                    N2kgfTPec_Acknowledge,
                    NumberOfParameterPairs, N2kgfpec_Acknowledge);
    return true;
}

//*****************************************************************************
bool tN2kGroupFunctionHandler::HandleReadFieldsReply(const tN2kMsg &/*N2kMsg*/,int /*iDev*/) {
    return true;
}


//*****************************************************************************
bool tN2kGroupFunctionHandler::HandleWriteFields(const tN2kMsg &N2kMsg,
                                  uint16_t /*ManufacturerCode*/, // This will be set to 0xffff for non-propprietary PNGs
                                  uint8_t /*IndustryGroup*/, // This will be set to 0xff for non-propprietary PNGs
                                  uint8_t /*UniqueID*/,
                                  uint8_t /*NumberOfSelectionPairs*/,
                                  uint8_t NumberOfParameterPairs,
                                  int iDev) {
    // As default we respond with not supported.
    bool IsTxPGN=pNMEA2000->IsTxPGN(GetPGNForGroupFunction(N2kMsg),iDev);
    tN2kGroupFunctionPGNErrorCode PGNec=(IsTxPGN?N2kgfPGNec_ReadOrWriteNotSupported:N2kgfPGNec_PGNNotSupported);
    SendAcknowledge(pNMEA2000,N2kMsg.Source,iDev,GetPGNForGroupFunction(N2kMsg),
                    PGNec,
                    N2kgfTPec_Acknowledge,
                    NumberOfParameterPairs, N2kgfpec_Acknowledge);

    return true;
}

//*****************************************************************************
bool tN2kGroupFunctionHandler::HandleWriteFieldsReply(const tN2kMsg &/*N2kMsg*/,int /*iDev*/) {
    return true;
}

// Static functions for PGN 126208 handling
//*****************************************************************************
unsigned long tN2kGroupFunctionHandler::GetPGNForGroupFunction(const tN2kMsg &N2kMsg) {
  int Index=1;
  return N2kMsg.Get3ByteUInt(Index);
}

//*****************************************************************************
bool tN2kGroupFunctionHandler::Parse(const tN2kMsg &N2kMsg,
                            tN2kGroupFunctionCode &GroupFunctionCode,
                            unsigned long &PGNForGroupFunction) {
  if (N2kMsg.PGN!=126208L) return false;

  GroupFunctionCode=(tN2kGroupFunctionCode)(N2kMsg.Data[0]);
  PGNForGroupFunction=GetPGNForGroupFunction(N2kMsg);

  return true;
}

#define N2kgf_OffsetToParams 4
#define N2kgf_OffsetToRequestPairParameters 11
#define N2kgf_OffsetToCommandPairParameters 6

//*****************************************************************************
bool tN2kGroupFunctionHandler::ParseRequestParams(const tN2kMsg &N2kMsg,
                               uint32_t &TransmissionInterval,
                               uint16_t &TransmissionIntervalOffset,
                               uint8_t  &NumberOfParameterPairs) {
  if (N2kMsg.PGN!=126208L) return false;
  int Index=N2kgf_OffsetToParams;
  TransmissionInterval=N2kMsg.Get4ByteUInt(Index);
  TransmissionIntervalOffset=N2kMsg.Get2ByteUInt(Index);
  NumberOfParameterPairs=N2kMsg.GetByte(Index);

  return true;
}

//*****************************************************************************
bool tN2kGroupFunctionHandler::StartParseRequestPairParameters(const tN2kMsg &N2kMsg, int &Index) {
  if (N2kMsg.PGN!=126208L) return false;
  Index=N2kgf_OffsetToRequestPairParameters;

  return true;
}

//*****************************************************************************
bool tN2kGroupFunctionHandler::ParseCommandParams(const tN2kMsg &N2kMsg,
                               uint8_t &PrioritySetting,
                               uint8_t &NumberOfParameterPairs) {
  if (N2kMsg.PGN!=126208L) return false;
  int Index=N2kgf_OffsetToParams;
  PrioritySetting=N2kMsg.GetByte(Index);
  NumberOfParameterPairs=N2kMsg.GetByte(Index);

  return true;
}

//*****************************************************************************
bool tN2kGroupFunctionHandler::StartParseCommandPairParameters(const tN2kMsg &N2kMsg, int &Index) {
  if (N2kMsg.PGN!=126208L) return false;
  Index=N2kgf_OffsetToCommandPairParameters;

  return true;
}

//*****************************************************************************
bool tN2kGroupFunctionHandler::ParseAcknowledgeParams(const tN2kMsg &N2kMsg,
                               tN2kGroupFunctionPGNErrorCode &PGNErrorCode,
                               tN2kGroupFunctionTransmissionOrPriorityErrorCode &TransmissionOrPriorityErrorCode,
                               uint8_t &NumberOfParameterPairs) {
  PGNErrorCode=N2kgfPGNec_PGNNotSupported;
  TransmissionOrPriorityErrorCode=N2kgfTPec_TransmitIntervalOrPriorityNotSupported;
  NumberOfParameterPairs=0;
  if (N2kMsg.PGN!=126208L) return false;
  int Index=N2kgf_OffsetToParams;
  uint8_t b=N2kMsg.GetByte(Index);
  PGNErrorCode=(tN2kGroupFunctionPGNErrorCode)(b&0x0f);
  TransmissionOrPriorityErrorCode=(tN2kGroupFunctionTransmissionOrPriorityErrorCode)(b>>4);

  return true;
}

//*****************************************************************************
bool tN2kGroupFunctionHandler::StartParseReadOrWriteParameters(const tN2kMsg &N2kMsg, bool Proprietary, int &Index) {
  Index=N2kgf_OffsetToParams;
  if ( Proprietary ) {
    Index+=5;
  } else {
    Index+=3;
  }

  return true;
}

//*****************************************************************************
bool tN2kGroupFunctionHandler::ParseReadOrWriteParams(const tN2kMsg &N2kMsg,
                               uint16_t &ManufacturerCode,
                               uint8_t &IndustryGroup,
                               uint8_t &UniqueID,
                               uint8_t &NumberOfSelectionPairs,
                               uint8_t &NumberOfParameterPairs,
                               bool Proprietary) {
  if (N2kMsg.PGN!=126208L) return false;
  int Index=N2kgf_OffsetToParams;
  ManufacturerCode=0xffff; // We need here information is PGN proprietary or not
  IndustryGroup=0xff;
  if ( Proprietary ) {
    uint16_t ProprietaryInfo=N2kMsg.Get2ByteUInt(Index);
    ManufacturerCode=ProprietaryInfo & 0x07ff;
    IndustryGroup=(ProprietaryInfo>>13) &0x07;
  }
  UniqueID=N2kMsg.GetByte(Index);
  NumberOfSelectionPairs=N2kMsg.GetByte(Index);
  NumberOfParameterPairs=N2kMsg.GetByte(Index);

  return true;
}

//*****************************************************************************
void SetStartReadOrWriteReply(tN2kMsg &N2kMsg, unsigned char Destination, unsigned long PGN, tN2kGroupFunctionCode cmd,
                           uint16_t ManufacturerCode,
                           uint8_t IndustryGroup,
                           uint8_t UniqueID,
                           uint8_t NumberOfSelectionPairs,
                           uint8_t NumberOfParameterPairs,
                           bool Proprietary) {
  N2kMsg.SetPGN(126208L);
	N2kMsg.Priority=3;
  N2kMsg.Destination=Destination;
  N2kMsg.AddByte(cmd);
  N2kMsg.Add3ByteInt(PGN);
  if ( Proprietary ) {
    uint16_t ProprietaryInfo = IndustryGroup<<13 | 0x1800 | (ManufacturerCode & 0x07ff);
    N2kMsg.Add2ByteUInt(ProprietaryInfo);
  }
  N2kMsg.AddByte(UniqueID);
  N2kMsg.AddByte(NumberOfSelectionPairs);
  N2kMsg.AddByte(NumberOfParameterPairs);
}

//*****************************************************************************
void tN2kGroupFunctionHandler::SetStartReadReply(tN2kMsg &N2kMsg, unsigned char Destination, unsigned long PGN,
                           uint16_t ManufacturerCode,
                           uint8_t IndustryGroup,
                           uint8_t UniqueID,
                           uint8_t NumberOfSelectionPairs,
                           uint8_t NumberOfParameterPairs,
                           bool Proprietary) {

  SetStartReadOrWriteReply(N2kMsg,Destination,PGN,N2kgfc_ReadReply,
      ManufacturerCode,IndustryGroup,UniqueID,NumberOfSelectionPairs,NumberOfParameterPairs,Proprietary
    );
}

//*****************************************************************************
void tN2kGroupFunctionHandler::SetStartWriteReply(tN2kMsg &N2kMsg, unsigned char Destination, unsigned long PGN,
                           uint16_t ManufacturerCode,
                           uint8_t IndustryGroup,
                           uint8_t UniqueID,
                           uint8_t NumberOfSelectionPairs,
                           uint8_t NumberOfParameterPairs,
                           bool Proprietary) {

  SetStartReadOrWriteReply(N2kMsg,Destination,PGN,N2kgfc_WriteReply,
      ManufacturerCode,IndustryGroup,UniqueID,NumberOfSelectionPairs,NumberOfParameterPairs,Proprietary
    );
}

//*****************************************************************************
void tN2kGroupFunctionHandler::SetStartAcknowledge(tN2kMsg &N2kMsg, unsigned char Destination, unsigned long PGN,
                                         tN2kGroupFunctionPGNErrorCode PGNErrorCode,
                                         tN2kGroupFunctionTransmissionOrPriorityErrorCode TransmissionOrPriorityErrorCode,
                                         uint8_t NumberOfParameterPairs) {
  N2kMsg.Clear();
	N2kMsg.SetPGN(126208L);
	N2kMsg.Priority=3;
  N2kMsg.Destination=Destination;
	N2kMsg.AddByte(N2kgfc_Acknowledge);
  N2kMsg.Add3ByteInt(PGN);
  N2kMsg.AddByte(PGNErrorCode | TransmissionOrPriorityErrorCode<<4);
  N2kMsg.AddByte(NumberOfParameterPairs);
}

#define ErrorcodeIndex 4

//*****************************************************************************
void tN2kGroupFunctionHandler::ChangePNGErrorCode(tN2kMsg &N2kMsg, tN2kGroupFunctionPGNErrorCode PGNErrorCode) {
  int Index=ErrorcodeIndex;
  uint8_t ec=N2kMsg.GetByte(Index);
  ec = (ec & 0xf0) | PGNErrorCode;
  N2kMsg.Data[ErrorcodeIndex]=ec;
}

//*****************************************************************************
void tN2kGroupFunctionHandler::ChangeTransmissionOrPriorityErrorCode(tN2kMsg &N2kMsg, tN2kGroupFunctionTransmissionOrPriorityErrorCode TransmissionOrPriorityErrorCode) {
  int Index=ErrorcodeIndex;
  uint8_t ec=N2kMsg.GetByte(Index);
  ec = (ec & 0x0f) | (TransmissionOrPriorityErrorCode<<4);
  N2kMsg.Data[ErrorcodeIndex]=ec;
}

//*****************************************************************************
void tN2kGroupFunctionHandler::AddAcknowledgeParameter(tN2kMsg &N2kMsg,
                                         uint8_t ParameterPairIndex,
                                         tN2kGroupFunctionParameterErrorCode ErrorCode) {
  if ( ((ParameterPairIndex % 2) == 0) && (N2kMsg.DataLen>0) ) {
    N2kMsg.AddByte((uint8_t)(ErrorCode) | 0x0f << 4);
  } else {
    // Should actually add AddBits to N2kMsg
    N2kMsg.Data[N2kMsg.DataLen-1]=(N2kMsg.Data[N2kMsg.DataLen-1] & 0x0f) | ((uint8_t)(ErrorCode) << 4);
  }
}

//*****************************************************************************
void tN2kGroupFunctionHandler::SendAcknowledge(tNMEA2000 *pNMEA2000, unsigned char Destination, int iDev, unsigned long PGN,
                                         tN2kGroupFunctionPGNErrorCode PGNErrorCode,
                                         tN2kGroupFunctionTransmissionOrPriorityErrorCode TransmissionOrPriorityErrorCode,
                                         uint8_t NumberOfParameterPairs,
                                         tN2kGroupFunctionParameterErrorCode ParameterErrorCodeForAll) {
  tN2kMsg N2kRMsg;

    // As default we respond with not supported.
    SetStartAcknowledge(N2kRMsg,Destination,PGN,
                        PGNErrorCode,
                        TransmissionOrPriorityErrorCode,
                        NumberOfParameterPairs);
    for (uint8_t ParamIndex=0; ParamIndex<NumberOfParameterPairs;ParamIndex++) {
      AddAcknowledgeParameter(N2kRMsg,ParamIndex,ParameterErrorCodeForAll);
    }
    pNMEA2000->SendMsg(N2kRMsg,iDev);
}

#endif
