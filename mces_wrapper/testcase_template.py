# using -*-utf-8-*-
#
# This class creates MZD driver.
# This class can use MZDWrapper.dll and CPalladiumAccess.dll
# Created by Wei Lai, 2021-01-22
# Modified by Yihao Liu, 2021-2-20
#

from tkinter import Tcl
import os
import socket
import logging
import sys
import shutil
from enum_class import *
from ctypes import *
from mcesFunctionLib import *
import importlib
import time
import traceback
import random
from ctypes import *

currentPath = os.getcwd()
path = os.path.dirname(__file__)
os.chdir(path)
parrentPath = os.path.abspath(os.path.join(os.getcwd(), ".."))


class mcesAPIPythonWrapper(object):
    """description of class"""

    def __init__(self, host='10.68.32.132', port=45256):  # ce1:10.65.140.73  z1-01:10.68.32.132
        # load DLL
        try:
            self.CPalladiumAccess = CDLL('..\Debug\CPalladiumAccess.dll')
            self.wrapper = CDLL('..\Debug\MZDWrapper.dll')
        except:
            raise Exception('Load DLL error!')
        # connect TCL server
        eval_f = "Client.tcl".encode()
        host_p = c_char_p(host.encode())
        port_p = c_int(port)
        eval_p = c_char_p(eval_f)
        ret = self.MZDHwLoadTclScript(host_p, port_p, eval_p)
        self.MZDInit()

    def MZDHwLoadTclScript(self, host, port, str):
        func = self.CPalladiumAccess['LoasTclScript']
        func.argtypes = [c_char_p, c_int32, c_char_p]
        func.restype = c_int64
        return func(host, port, str)

    def MZDGetSerdesDev(self):
        # get serdes dev handler
        func = self.wrapper['getSerdesDev']
        func.argtypes = [c_void_p]
        func.restype = c_void_p
        self.pSerdesDev = func(self.devHandle)

    def MZDInit(self, basePhyAddr=0):
        # init MZD API
        self.basePhyAddr = basePhyAddr
        self.PhyAddrOffsetMax = 32
        func = self.wrapper['initDev']
        func.argtypes = [c_uint16]
        func.restype = c_void_p
        # get MZD dev handler
        self.devHandle = func(basePhyAddr)
        self.MZDGetSerdesDev()


if __name__ == '__main__':
    host = '10.68.32.132'
    port = 45256

    apiWrapper = mcesAPIPythonWrapper(host, port)
    apiWrapper.MZDInit()

    cur_time = time.strftime("%m-%d-%Y_%H-%M-%S", time.localtime())
    logging.basicConfig(level=logging.DEBUG,
                        filename=f'X93160_API_test_{cur_time}.log',
                        format='%(message)s',
                        datefmt='%d-%M-%Y %H:%M:%S')

    # Data path's choice has problem

