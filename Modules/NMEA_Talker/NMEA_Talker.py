@staticclass
class TalkerHelper:

	def __del__(self):
  		# body of destructor
		pass

	@staticmethod
	def GetTalker( messageType: str):
		if (messageType[0] == 'P'):
			return Talker.ProprietaryCode

		if (TalkerLookupTable.ContainsKey(messageType.Substring(0, 2))):
			return TalkerLookupTable[messageType.Substring(0, 2)]

		return Talker.Unknown

	#@public
	TalkerLookupTable = dict(
		{"AB", Talker.IndependentAISBaseStation                 },
		{"AD", Talker.DependentAISBaseStation                   },
		{"AG", Talker.HeadingTrackControllerGeneral             },
		{"AP", Talker.HeadingTrackControllerMagnetic            },
		{"AI", Talker.MobileClassAorBAISStation                 },
		{"AN", Talker.AISAidstoNavigationStation                },
		{"AR", Talker.AISReceivingStation                       },
		{"AS", Talker.AISStation                                },
		{"AT", Talker.AISTransmittingStation                    },
		{"AX", Talker.AISSimplexRepeaterStation                 },
		{"BI", Talker.BilgeSystems                              },
		{"CD", Talker.DigitalSelectiveCalling                   },
		{"CR", Talker.DataReceiver                              },
		{"CS", Talker.Satellite                                 },
		{"CT", Talker.RadioTelephoneMFHF                        },
		{"CV", Talker.RadioTelephoneVHF                         },
		{"CX", Talker.ScanningReceiver                          },
		{"DE", Talker.DECCANavigator                            },
		{"DF", Talker.DirectionFinder                           },
		{"DU", Talker.DuplexRepeaterStation                     },
		{"EC", Talker.ElectronicChartSystem                     },
		{"EI", Talker.ElectronicChartDisplayInformationSystem   },
		{"EP", Talker.EmergencyPositionIndicatingBeacon         },
		{"ER", Talker.EngineRoomMonitoringSystems               },
		{"FD", Talker.FireDoorControllerMonitoringPoint         },
		{"FE", Talker.FireExtinguisherSystem                    },
		{"FR", Talker.FireDetectionPoint                        },
		{"FS", Talker.FireSprinklerSystem                       },
		{"GA", Talker.GalileoPositioningSystem                  },
		{"GB", Talker.BeiDouNavigationSatelliteSystem           },
		{"GL", Talker.GlonassReceiver                           },
		{"GN", Talker.GlobalNavigationSatelliteSystem           },
		{"GP", Talker.GlobalPositioningSystem                   },
		{"GI", Talker.IndianRegionalNavigationSatelliteSystem   },
		{"GQ", Talker.QuasiZenithSatelliteSystem                },
		{"HC", Talker.CompassMagnetic                           },
		{"HE", Talker.GyroNorthSeeking                          },
		{"HF", Talker.Fluxgate                                  },
		{"HN", Talker.GyroNonNorthSeeking                       },
		{"HD", Talker.HullDoorControllerMonitoringPanel         },
		{"HS", Talker.HullStressMonitoring                      },
		{"II", Talker.IntegratedInstrumentation                 },
		{"IN", Talker.IntegratedNavigation                      },
		{"LC", Talker.LoranC                                    },
		{"P ", Talker.ProprietaryCode                           },
		{"RA", Talker.RadarAndOrRadarPlotting                   },
		{"RC", Talker.PropulsionMachineryIncludingRemoteControl },
		{"SA", Talker.PhysicalShoreAISStation                   },
		{"SD", Talker.SounderDepth                              },
		{"SG", Talker.SteeringGearSteeringEngine                },
		{"SN", Talker.ElectronicPositioningSystem               },
		{"SS", Talker.SounderScanning                           },
		{"TI", Talker.TurnRateIndicator                         },
		{"UP", Talker.MicroprocessorController                  },
		{"U0", Talker.UserID0                                   },
		{"U1", Talker.UserID1                                   },
		{"U2", Talker.UserID2                                   },
		{"U3", Talker.UserID3                                   },
		{"U4", Talker.UserID4                                   },
		{"U5", Talker.UserID5                                   },
		{"U6", Talker.UserID6                                   },
		{"U7", Talker.UserID7                                   },
		{"U8", Talker.UserID8                                   },
		{"U9", Talker.UserID9                                   },
		{"VD", Talker.Doppler                                   },
		{"VM", Talker.SpeedLogWaterMagnetic                     },
		{"VW", Talker.SpeedLogWaterMechanical                   },
		{"VR", Talker.VoyageDataRecorder                        },
		{"WD", Talker.WatertightDoorControllerMonitoringPanel   },
		{"WI", Talker.WeatherInstruments                        },
		{"WL", Talker.WaterLevelDetectionSystems                },
		{"YX", Talker.Transducer                                },
		{"ZA", Talker.AtomicsClock                              },
		{"ZC", Talker.Chronometer                               },
		{"ZQ", Talker.Quartz                                    },
		{"ZV", Talker.RadioUpdate                               },
		{"ZX", Talker.Xtal                                      },
		{"ZZ", Talker.Other                                     },
		{"!A", Talker.AISAutomaticIdentificationSystem          },
		{"!B", Talker.AISBaseStation                            },
		{"!C", Talker.AISClassBCS                               },
		{"!D", Talker.AISDSC                                    },
		{"!E", Talker.AISDSCStation                             },
		{"!F", Talker.AISFleetBroadcaster                       },
		{"!G", Talker.AISGroupAssignmentCommand                 },
		{"!H", Talker.AISAidstoNavigationStation                },
		{"!I", Talker.AISInformationStation                     },
		{"!J", Talker.AISLoranStation                           },
		{"!K", Talker.AISRadioStation                           },
		{"!L", Talker.AISLoranStation                           },
		{"!M", Talker.AISMobileStation                          },
		{"!N", Talker.AISMobileStation                          },
		{"!O", Talker.AISOffshoreBaseStation                    },
		{"!P", Talker.AISRegionalBaseStation                    },
		{"!Q", Talker.AISRegionalBaseStation                    },
		{"!R", Talker.AISReceivingStation                       },
		{"!S", Talker.AISSafetyRelatedBroadcastStation          },
		{"!T", Talker.AISTargetStation                          },
		{"!U", Talker.AISUserTerminal                           },
		{"!V", Talker.AISVTSRegional                            },
		{"!W", Talker.AISVTSLocal                               },
		{"!X", Talker.AISMobileStation                          },
		{"!Y", Talker.AISMobileStation                          },
		{"!Z", Talker.AISMobileStation                          },
	)


	# Talker Identifier
	enum Talker: int
	# Multiple talker IDs sometimes seen in <see cref="IMultiSentenceMessage"/>
	Multiple = -2,
	# Unrecognized Talker ID
	Unknown = -1,
	# Independent AIS Base Station
	IndependentAISBaseStation = "AB",
	# Dependent AIS Base Station
	DependentAISBaseStation = "AD", 
	# Heading Track Controller (Autopilot) - General
	HeadingTrackControllerGeneral = "AG",
	# Heading Track Controller (Autopilot) - Magnetic
	HeadingTrackControllerMagnetic = "AP", #
	# Mobile Class A or B AIS Station
	MobileClassAorBAISStation, # = AI
	# AIS Aids to Navigation Station 
	AISAidstoNavigationStation, # = AN
	# AIS Receiving Station
	AISReceivingStation, # = AR
	# AIS Station (ITU_R M1371,  (“Limited Base Station’)
	AISStation, # = AS
	# AIS Transmitting Station
	AISTransmittingStation, # = AT
	# AIS Simplex Repeater Station
	AISSimplexRepeaterStation, # = AX
	# BeiDou Navigation Satellite System
	BeiDouNavigationSatelliteSystem, # == GB
	# Bilge Systems
	BilgeSystems, # = BI
	# 
	DigitalSelectiveCalling, # = CD
	# 
	DataReceiver, # = CR
	# 
	Satellite, # = CS
	# 
	RadioTelephoneMFHF, # = CT
	# 
	RadioTelephoneVHF, # = CV
	# 
	ScanningReceiver, # = CX
	# 
	DECCANavigator, # = DE
	# 
	DirectionFinder, # = DF
	# 
	DuplexRepeaterStation, # = DU
	# 
	ElectronicChartSystem, # = EC
	# 
	ElectronicChartDisplayInformationSystem, # = EI
	# 
	EmergencyPositionIndicatingBeacon, # = EP
	# 
	EngineRoomMonitoringSystems, # = ER
	# 
	FireDoorControllerMonitoringPoint, # = FD
	# 
	FireExtinguisherSystem, # = FE
	# 
	FireDetectionPoint, # = FR
	# 
	FireSprinklerSystem, # = FS
	# Galileo Positioning System
	GalileoPositioningSystem, # = GA
	# GLONASS Receiver
	GlonassReceiver, # = GL
	# Global Navigation Satellite System (GNSS)
	GlobalNavigationSatelliteSystem, # = GN
	# Global Positioning System (GPS)
	GlobalPositioningSystem, # = GPS
	# Heading Sensor - Compass, Magnetic
	CompassMagnetic, # = HC
	# Heading Sensor - Gyro, North Seeking
	GyroNorthSeeking, # = HE
	# Heading Sensor - Fluxgate
	Fluxgate, # = HF
	# Heading Sensor - Gyro, Non-North Seeking
	GyroNonNorthSeeking, # = HN
	# Hull Door Controller/Monitoring Panel
	HullDoorControllerMonitoringPanel, # = HD
	# Hull Stress Monitoring
	HullStressMonitoring, # = HS
	# Indian Regional Navigation Satellite System (IRNSS)
	IndianRegionalNavigationSatelliteSystem, # = GI
	# Integrated Instrumentation
	IntegratedInstrumentation, # = II
	# Integrated Navigation
	IntegratedNavigation, # = IN
	# Loran C
	LoranC, # = LC
	# 
	ProprietaryCode, # = P
	# 
	RadarAndOrRadarPlotting, # = RA
	# 
	PropulsionMachineryIncludingRemoteControl, # = RC
	# 
	PhysicalShoreAISStation, # = SA
	# 
	SounderDepth, # = SD
	# 
	SteeringGearSteeringEngine, # = SG
	# 
	ElectronicPositioningSystem, # = SN
	# 
	SounderScanning, # = SS
	# 
	TurnRateIndicator, # = TI
	# 
	MicroprocessorController, # = UP
	# User configured talker identifier
	UserID0, # = U0
	# User configured talker identifier
	UserID1, # = U1
	# User configured talker identifier
	UserID2, # = U2
	# User configured talker identifier
	UserID3, # = U3
	# User configured talker identifier
	UserID4, # = U4
	# User configured talker identifier
	UserID5, # = U5
	# User configured talker identifier
	UserID6, # = U6
	# User configured talker identifier
	UserID7, # = U7
	# User configured talker identifier
	UserID8, # = U8
	# User configured talker identifier
	UserID9, # = U9
	# Velocity sensor - Doppler
	Doppler, # = VD
	# Velocity sensor - Speed Log, Water, Magnetic
	SpeedLogWaterMagnetic, # = VM
	# Velocity sensor - Speed Log, Water Mechanical
	SpeedLogWaterMechanical, # = VW
	# Voyage Data Recorder
	VoyageDataRecorder, # = VR
	# Watertight Door Controller/Monitoring Panel
	WatertightDoorControllerMonitoringPanel, # = WD
	# Weather Instruments
	WeatherInstruments, # = WI
	# Water Level Detection Systems 
	WaterLevelDetectionSystems, # = WL
	# Transducer
	Transducer, # = YX
	# Time keeper - Atomics Clock
	AtomicsClock, # = ZA
	# Time keeper - Chronometer
	Chronometer, # = ZC
	# Time keeper - Quartz
	Quartz, # = ZQ
	# Quasi-Zenith Satellite System (QZSS)
	QuasiZenithSatelliteSystem, 
	# Time keeper - Radio Update
	RadioUpdate, # = ZV

}
