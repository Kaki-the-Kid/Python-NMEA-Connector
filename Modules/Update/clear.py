#!/usr/bin/python
# -*- coding: utf-8 -*-
from Modules.RasPiShield_Blinkt.init_blinkt import *
from Modules.RasPiShield_Matrix.init_matrix import *
from Modules.RasPiShield_Unicorn.init_unicorn import *


def clear_all():

    for matrix in matrix_list:

        matrix.clear()
        matrix.write_display()

    bargraph.clear()
    bargraph.write_display()

    unicorn.clear()
    unicorn.show()

    blinkt.clear()
    blinkt.show()

    log_string('Clear Display')


if __name__ == '__main__':

    clear_all()
