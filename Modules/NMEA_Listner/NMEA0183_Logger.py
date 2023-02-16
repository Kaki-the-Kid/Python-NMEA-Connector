#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
import logging.handlers
import serial
import time
import sys
import os
import re
import datetime
import ConfigParser


class NMEA0183(object):
    def __init__(self, config):
        self.config = config
        self.logger = self._get_logger()
        self.logger.info("Starting NMEA0183")
        self.logger.info("NMEA0183 version: %s"   % NMEA0183_VERSION)
        self.logger.info("NMEA0183 config: %s"    % self.config)
        self.logger.info("NMEA0183 device: %s"    % self.config.get("NMEA0183", "NMEA0183_DEVICE"))
        self.logger.info("NMEA0183 baudrate: %s"  % self.config.get("NMEA0183", "NMEA0183_BAUDRATE"))
        self.logger.info("NMEA0183 data bits: %s" % self.config.get("NMEA0183", "NMEA0183_DATA_BITS"))
        self.logger.info("NMEA0183 parity: %s"    % self.config.get("NMEA0183", "NMEA0183_PARITY"))
        self.logger.info("NMEA0183 stop bits: %s" % self.config.get("NMEA0183", "NMEA0183_STOP_BITS"))
        self.logger.info("NMEA0183 handshake: %s" % self.config.get("NMEA0183", "NMEA0183_HANDSHAKE"))
        self.logger.info("NMEA0183 log level: %s" % self.config.get("NMEA0183", "NMEA0183_LOG_LEVEL"))
        self.logger.info("NMEA0183 log file: %s"  % self.config.get("NMEA0183", "NMEA0183_LOG_FILE"))
