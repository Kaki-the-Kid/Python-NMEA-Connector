#!/usr/bin/python
# -*- coding: utf-8 -*-
from multiprocessing import Process
import os

# Import NMEA2000 modules
import NMEA2000_defs

from modulefinder import Module

from Modules.Update import Update
from Modules.UpdateLog import UpdateLog
from Modules.UpdateUnicorn import UniCorn, UpdateIcon
from Modules.init_unicorn import unicorn_init
from Modules.update_matrix import *