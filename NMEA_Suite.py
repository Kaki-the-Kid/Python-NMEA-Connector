#!/usr/bin/python
# -*- coding: utf-8 -*-
from multiprocessing import Process
import os
import sys
import argparse

# Config for the project
import config.config as config
       
# Import NMEA2000 modules
#from Modules.Update.Update import Update
#from Modules.Update.UpdateLog import UpdateLog
#from modules.update.UpdateUnicorn import UniCorn, UpdateIcon
#from modules.update.init_unicorn import unicorn_init
#from Modules.RasPiShield_Matrix.update_matrix import update_bargraph, update_matrix

import Modules.NMEA_GUI.NMEA_GUI as NMEA_GUI
import Modules.NMEA_Interpreter.NMEA_Interpreter as Interpreter

import Modules.NMEA_Interpreter.NMEA_Interpreter as Interpreter
#import NMEA2000_Receive
#import NMEA2000_Send


# Global variables
processes_bar = []

def quit_all_threads():
    for thread in threads:
        thread.cancel()
        thread.join()
        

def quit_all_processes():
    for process in processes:
        process.terminate()
        process.join()

    
def main():
    # Check f or command line arguments
    argParser = argparse.ArgumentParser()
    argParser.add_argument("-n", "--name", help="your name")

    args = argParser.parse_args()
    print("args=%s" % args)

    print("args.name=%s" % args.name)
    
    main_thread = threading.Timer(THREADING_TIMER, main)
    main_thread.start()
    threads.append(main_thread)

    try:
        Update().update_json()
        UpdateLog().create_log()
        update_matrix()

        p = Process(target=update_bargraph)

        for process in processes_bar:
            process.terminate()

        p.start()
        #processes_bar.append(p)

        UpdateIcon().set_icon_path()

    except KeyboardInterrupt:
        quit_all_threads()
        #clear_all()
        quit_all_processes()
        
    NMEA_GUI.main()

