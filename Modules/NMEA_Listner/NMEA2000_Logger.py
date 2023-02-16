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


class NMEA2000(object):
    def __init__(self, config):
        self.config = config
        self.logger = self._get_logger()
        self.logger.info("Starting NMEA2000")
        self.logger.info("NMEA2000 version: %s"   % NMEA2000_VERSION)
        self.logger.info("NMEA2000 config: %s"    % self.config)
        self.logger.info("NMEA2000 device: %s"    % self.config.get("NMEA2000", "NMEA2000_DEVICE"))
        self.logger.info("NMEA2000 baudrate: %s"  % self.config.get("NMEA2000", "NMEA2000_BAUDRATE"))
        self.logger.info("NMEA2000 data bits: %s" % self.config.get("NMEA2000", "NMEA2000_DATA_BITS"))
        self.logger.info("NMEA2000 parity: %s"    % self.config.get("NMEA2000", "NMEA2000_PARITY"))
        self.logger.info("NMEA2000 stop bits: %s" % self.config.get("NMEA2000", "NMEA2000_STOP_BITS"))
        self.logger.info("NMEA2000 handshake: %s" % self.config.get("NMEA2000", "NMEA2000_HANDSHAKE"))
        self.logger.info("NMEA2000 log level: %s" % self.config.get("NMEA2000", "NMEA2000_LOG_LEVEL"))
        self.logger.info("NMEA2000 log file: %s"  % self.config.get("NMEA2000", "NMEA2000_LOG_FILE"))
