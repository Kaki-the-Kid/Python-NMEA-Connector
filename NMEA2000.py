#!/usr/bin/python
# -*- coding: utf-8 -*-
from multiprocessing import Process
import os

#import NMEA2000_defs
#import NMEA2000_Receive
#import NMEA2000_Send

import Modules.Config.Config as Config
       
# Import NMEA2000 modules
from Modules.Update.Update import Update
from Modules.Update.UpdateLog import UpdateLog
#from modules.update.UpdateUnicorn import UniCorn, UpdateIcon
#from modules.update.init_unicorn import unicorn_init
from Modules.RasPiShield_Matrix.update_matrix import update_bargraph, update_matrix

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
