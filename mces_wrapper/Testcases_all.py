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

    logging.info("Function name : API_N5C112GX4_GetFirmwareRev")
    devPtr = apiWrapper.pSerdesDev
    major = 1
    major_p = c_uint8(major)
    minor = 1
    minor_p = c_uint8(minor)
    patch = 1
    patch_p = c_uint8(patch)
    build = 1
    build_p = c_uint8(build)
    try:
        API_N5C112GX4_GetFirmwareRev(devPtr, major_p, minor_p, patch_p, build_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"major = {major}")
    logging.debug(f"minor = {minor}")
    logging.debug(f"patch = {patch}")
    logging.debug(f"build = {build}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_GetPLLLock")
    devPtr = apiWrapper.pSerdesDev
    lane = 1
    tsLocked = MCESD_BOOL.MCESD_FALSE.value
    tsLocked_p = c_long(tsLocked)
    rsLocked = MCESD_BOOL.MCESD_FALSE.value
    rsLocked_p = c_long(rsLocked)
    try:
        API_N5C112GX4_GetPLLLock(devPtr, lane, tsLocked_p, rsLocked_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"lane = {lane}")
    logging.debug(f"tsLocked = {tsLocked}")
    logging.debug(f"rsLocked = {rsLocked}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_GetTxRxReady")
    devPtr = apiWrapper.pSerdesDev
    lane = 1
    txReady = MCESD_BOOL.MCESD_FALSE.value
    txReady_p = c_long(txReady)
    rxReady = MCESD_BOOL.MCESD_FALSE.value
    rxReady_p = c_long(rxReady)
    try:
        API_N5C112GX4_GetTxRxReady(devPtr, lane, txReady_p, rxReady_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"lane = {lane}")
    logging.debug(f"txReady = {txReady}")
    logging.debug(f"rxReady = {rxReady}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_GetCDRLock")
    devPtr = apiWrapper.pSerdesDev
    lane = 1
    cdrLocked = MCESD_BOOL.MCESD_FALSE.value
    cdrLocked_p = c_long(cdrLocked)
    try:
        API_N5C112GX4_GetCDRLock(devPtr, lane, cdrLocked_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"lane = {lane}")
    logging.debug(f"cdrLocked = {cdrLocked}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_RxInit")
    devPtr = apiWrapper.pSerdesDev
    lane = 1
    try:
        API_N5C112GX4_RxInit(devPtr, lane)
    except Exception:
        traceback.print_exc()
    logging.debug(f"lane = {lane}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_SetTxEqParam")
    devPtr = apiWrapper.pSerdesDev
    lane = 1
    param = E_N5C112GX4_TXEQ_PARAM.N5C112GX4_TXEQ_EM_PRE3_CTRL.value
    paramValue = 1
    try:
        API_N5C112GX4_SetTxEqParam(devPtr, lane, param, paramValue)
    except Exception:
        traceback.print_exc()
    logging.debug(f"lane = {lane}")
    logging.debug(f"param = {param}")
    logging.debug(f"paramValue = {paramValue}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_GetTxEqParam")
    devPtr = apiWrapper.pSerdesDev
    lane = 1
    param = E_N5C112GX4_TXEQ_PARAM.N5C112GX4_TXEQ_EM_PRE3_CTRL.value
    paramValue = 1
    paramValue_p = c_uint32(paramValue)
    try:
        API_N5C112GX4_GetTxEqParam(devPtr, lane, param, paramValue_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"lane = {lane}")
    logging.debug(f"param = {param}")
    logging.debug(f"paramValue = {paramValue}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_SetCTLEParam")
    devPtr = apiWrapper.pSerdesDev
    lane = 1
    param = E_N5C112GX4_CTLE_PARAM.N5C112GX4_RX_DC_TERM_EN.value
    paramValue = 1
    try:
        API_N5C112GX4_SetCTLEParam(devPtr, lane, param, paramValue)
    except Exception:
        traceback.print_exc()
    logging.debug(f"lane = {lane}")
    logging.debug(f"param = {param}")
    logging.debug(f"paramValue = {paramValue}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_GetCTLEParam")
    devPtr = apiWrapper.pSerdesDev
    lane = 1
    param = E_N5C112GX4_CTLE_PARAM.N5C112GX4_RX_DC_TERM_EN.value
    paramValue = 1
    paramValue_p = c_uint32(paramValue)
    try:
        API_N5C112GX4_GetCTLEParam(devPtr, lane, param, paramValue_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"lane = {lane}")
    logging.debug(f"param = {param}")
    logging.debug(f"paramValue = {paramValue}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_GetFfeTap")
    devPtr = apiWrapper.pSerdesDev
    lane = 1
    path = E_N5C112GX4_FFE_PATH.N5C112GX4_DATA_PATH.value
    tap = E_N5C112GX4_FFE_TAP.N5C112GX4_FFE_PRE_6.value
    tapValue = 1
    tapValue_p = c_int32(tapValue)
    try:
        API_N5C112GX4_GetFfeTap(devPtr, lane, path, tap, tapValue_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"lane = {lane}")
    logging.debug(f"path = {path}")
    logging.debug(f"tap = {tap}")
    logging.debug(f"tapValue = {tapValue}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_SetMcuBroadcast")
    devPtr = apiWrapper.pSerdesDev
    state = MCESD_BOOL.MCESD_FALSE.value
    try:
        API_N5C112GX4_SetMcuBroadcast(devPtr, state)
    except Exception:
        traceback.print_exc()
    logging.debug(f"state = {state}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_GetMcuBroadcast")
    devPtr = apiWrapper.pSerdesDev
    state = MCESD_BOOL.MCESD_FALSE.value
    state_p = c_long(state)
    try:
        API_N5C112GX4_GetMcuBroadcast(devPtr, state_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"state = {state}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_SetPowerPLL")
    devPtr = apiWrapper.pSerdesDev
    lane = 1
    state = MCESD_BOOL.MCESD_FALSE.value
    try:
        API_N5C112GX4_SetPowerPLL(devPtr, lane, state)
    except Exception:
        traceback.print_exc()
    logging.debug(f"lane = {lane}")
    logging.debug(f"state = {state}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_GetPowerPLL")
    devPtr = apiWrapper.pSerdesDev
    lane = 1
    state = MCESD_BOOL.MCESD_FALSE.value
    state_p = c_long(state)
    try:
        API_N5C112GX4_GetPowerPLL(devPtr, lane, state_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"lane = {lane}")
    logging.debug(f"state = {state}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_SetPowerTx")
    devPtr = apiWrapper.pSerdesDev
    lane = 1
    state = MCESD_BOOL.MCESD_FALSE.value
    try:
        API_N5C112GX4_SetPowerTx(devPtr, lane, state)
    except Exception:
        traceback.print_exc()
    logging.debug(f"lane = {lane}")
    logging.debug(f"state = {state}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_GetPowerTx")
    devPtr = apiWrapper.pSerdesDev
    lane = 1
    state = MCESD_BOOL.MCESD_FALSE.value
    state_p = c_long(state)
    try:
        API_N5C112GX4_GetPowerTx(devPtr, lane, state_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"lane = {lane}")
    logging.debug(f"state = {state}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_SetPowerRx")
    devPtr = apiWrapper.pSerdesDev
    lane = 1
    state = MCESD_BOOL.MCESD_FALSE.value
    try:
        API_N5C112GX4_SetPowerRx(devPtr, lane, state)
    except Exception:
        traceback.print_exc()
    logging.debug(f"lane = {lane}")
    logging.debug(f"state = {state}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_GetPowerRx")
    devPtr = apiWrapper.pSerdesDev
    lane = 1
    state = MCESD_BOOL.MCESD_FALSE.value
    state_p = c_long(state)
    try:
        API_N5C112GX4_GetPowerRx(devPtr, lane, state_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"lane = {lane}")
    logging.debug(f"state = {state}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_SetPhyMode")
    devPtr = apiWrapper.pSerdesDev
    mode = E_N5C112GX4_PHYMODE.N5C112GX4_PHYMODE_SERDES.value
    try:
        API_N5C112GX4_SetPhyMode(devPtr, mode)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mode = {mode}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_GetPhyMode")
    devPtr = apiWrapper.pSerdesDev
    mode = E_N5C112GX4_PHYMODE.N5C112GX4_PHYMODE_SERDES.value
    mode_p = c_long(mode)
    try:
        API_N5C112GX4_GetPhyMode(devPtr, mode_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mode = {mode}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_SetRefFreq")
    devPtr = apiWrapper.pSerdesDev
    lane = 1
    freq = E_N5C112GX4_REFFREQ.N5C112GX4_REFFREQ_25MHZ.value
    clkSel = E_N5C112GX4_REFCLK_SEL.N5C112GX4_REFCLK_SEL_GROUP1.value
    try:
        API_N5C112GX4_SetRefFreq(devPtr, lane, freq, clkSel)
    except Exception:
        traceback.print_exc()
    logging.debug(f"lane = {lane}")
    logging.debug(f"freq = {freq}")
    logging.debug(f"clkSel = {clkSel}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_GetRefFreq")
    devPtr = apiWrapper.pSerdesDev
    lane = 1
    refFreq = E_N5C112GX4_REFFREQ.N5C112GX4_REFFREQ_25MHZ.value
    refFreq_p = c_long(refFreq)
    refClkSel = E_N5C112GX4_REFCLK_SEL.N5C112GX4_REFCLK_SEL_GROUP1.value
    refClkSel_p = c_long(refClkSel)
    try:
        API_N5C112GX4_GetRefFreq(devPtr, lane, refFreq_p, refClkSel_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"lane = {lane}")
    logging.debug(f"refFreq = {refFreq}")
    logging.debug(f"refClkSel = {refClkSel}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_SetTxRxBitRate")
    devPtr = apiWrapper.pSerdesDev
    lane = 1
    speed = E_N5C112GX4_SERDES_SPEED.N5C112GX4_SERDES_1P0625G.value
    try:
        API_N5C112GX4_SetTxRxBitRate(devPtr, lane, speed)
    except Exception:
        traceback.print_exc()
    logging.debug(f"lane = {lane}")
    logging.debug(f"speed = {speed}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_GetTxRxBitRate")
    devPtr = apiWrapper.pSerdesDev
    lane = 1
    speed = E_N5C112GX4_SERDES_SPEED.N5C112GX4_SERDES_1P0625G.value
    speed_p = c_long(speed)
    try:
        API_N5C112GX4_GetTxRxBitRate(devPtr, lane, speed_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"lane = {lane}")
    logging.debug(f"speed = {speed}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_SetDataBusWidth")
    devPtr = apiWrapper.pSerdesDev
    lane = 1
    txWidth = E_N5C112GX4_DATABUS_WIDTH.N5C112GX4_DATABUS_32BIT.value
    rxWidth = E_N5C112GX4_DATABUS_WIDTH.N5C112GX4_DATABUS_32BIT.value
    try:
        API_N5C112GX4_SetDataBusWidth(devPtr, lane, txWidth, rxWidth)
    except Exception:
        traceback.print_exc()
    logging.debug(f"lane = {lane}")
    logging.debug(f"txWidth = {txWidth}")
    logging.debug(f"rxWidth = {rxWidth}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_GetDataBusWidth")
    devPtr = apiWrapper.pSerdesDev
    lane = 1
    txWidth = E_N5C112GX4_DATABUS_WIDTH.N5C112GX4_DATABUS_32BIT.value
    txWidth_p = c_long(txWidth)
    rxWidth = E_N5C112GX4_DATABUS_WIDTH.N5C112GX4_DATABUS_32BIT.value
    rxWidth_p = c_long(rxWidth)
    try:
        API_N5C112GX4_GetDataBusWidth(devPtr, lane, txWidth_p, rxWidth_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"lane = {lane}")
    logging.debug(f"txWidth = {txWidth}")
    logging.debug(f"rxWidth = {rxWidth}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_SetMcuClockFreq")
    devPtr = apiWrapper.pSerdesDev
    clockMHz = 1
    try:
        API_N5C112GX4_SetMcuClockFreq(devPtr, clockMHz)
    except Exception:
        traceback.print_exc()
    logging.debug(f"clockMHz = {clockMHz}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_GetMcuClockFreq")
    devPtr = apiWrapper.pSerdesDev
    clockMHz = 1
    clockMHz_p = c_uint16(clockMHz)
    try:
        API_N5C112GX4_GetMcuClockFreq(devPtr, clockMHz_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"clockMHz = {clockMHz}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_SetTxOutputEnable")
    devPtr = apiWrapper.pSerdesDev
    lane = 1
    state = MCESD_BOOL.MCESD_FALSE.value
    try:
        API_N5C112GX4_SetTxOutputEnable(devPtr, lane, state)
    except Exception:
        traceback.print_exc()
    logging.debug(f"lane = {lane}")
    logging.debug(f"state = {state}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_GetTxOutputEnable")
    devPtr = apiWrapper.pSerdesDev
    lane = 1
    state = MCESD_BOOL.MCESD_FALSE.value
    state_p = c_long(state)
    try:
        API_N5C112GX4_GetTxOutputEnable(devPtr, lane, state_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"lane = {lane}")
    logging.debug(f"state = {state}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_SetPowerIvRef")
    devPtr = apiWrapper.pSerdesDev
    state = MCESD_BOOL.MCESD_FALSE.value
    try:
        API_N5C112GX4_SetPowerIvRef(devPtr, state)
    except Exception:
        traceback.print_exc()
    logging.debug(f"state = {state}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_GetPowerIvRef")
    devPtr = apiWrapper.pSerdesDev
    state = MCESD_BOOL.MCESD_FALSE.value
    state_p = c_long(state)
    try:
        API_N5C112GX4_GetPowerIvRef(devPtr, state_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"state = {state}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_SetCDRParam")
    devPtr = apiWrapper.pSerdesDev
    lane = 1
    param = E_N5C112GX4_CDR_PARAM.N5C112GX4_CDR_KP_FRAC.value
    paramValue = 1
    try:
        API_N5C112GX4_SetCDRParam(devPtr, lane, param, paramValue)
    except Exception:
        traceback.print_exc()
    logging.debug(f"lane = {lane}")
    logging.debug(f"param = {param}")
    logging.debug(f"paramValue = {paramValue}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_GetCDRParam")
    devPtr = apiWrapper.pSerdesDev
    lane = 1
    param = E_N5C112GX4_CDR_PARAM.N5C112GX4_CDR_KP_FRAC.value
    paramValue = 1
    paramValue_p = c_uint32(paramValue)
    try:
        API_N5C112GX4_GetCDRParam(devPtr, lane, param, paramValue_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"lane = {lane}")
    logging.debug(f"param = {param}")
    logging.debug(f"paramValue = {paramValue}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_SetTrainingTimeout")
    devPtr = apiWrapper.pSerdesDev
    lane = 1
    type = E_N5C112GX4_TRAINING.N5C112GX4_TRAINING_TRX.value
    training = S_N5C112GX4_TRAINING_TIMEOUT(0, 0)
    training_p = byref(training)
    try:
        API_N5C112GX4_SetTrainingTimeout(devPtr, lane, type, training_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"lane = {lane}")
    logging.debug(f"type = {type}")
    logging.debug(f"training = {S_N5C112GX4_TRAINING_TIMEOUT.timeout}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_GetTrainingTimeout")
    devPtr = apiWrapper.pSerdesDev
    lane = 1
    type = E_N5C112GX4_TRAINING.N5C112GX4_TRAINING_TRX.value
    training = S_N5C112GX4_TRAINING_TIMEOUT(0, 0)
    training_p = byref(training)
    try:
        API_N5C112GX4_GetTrainingTimeout(devPtr, lane, type, training_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"lane = {lane}")
    logging.debug(f"type = {type}")
    logging.debug(f"training = {S_N5C112GX4_TRAINING_TIMEOUT.timeout}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_GetSquelchDetect")
    devPtr = apiWrapper.pSerdesDev
    lane = 1
    squelched = MCESD_BOOL.MCESD_FALSE.value
    squelched_p = c_long(squelched)
    try:
        API_N5C112GX4_GetSquelchDetect(devPtr, lane, squelched_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"lane = {lane}")
    logging.debug(f"squelched = {squelched}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_SetSquelchThreshold")
    devPtr = apiWrapper.pSerdesDev
    lane = 1
    threshold = 1
    try:
        API_N5C112GX4_SetSquelchThreshold(devPtr, lane, threshold)
    except Exception:
        traceback.print_exc()
    logging.debug(f"lane = {lane}")
    logging.debug(f"threshold = {threshold}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_GetSquelchThreshold")
    devPtr = apiWrapper.pSerdesDev
    lane = 1
    threshold = 1
    threshold_p = c_uint8(threshold)
    try:
        API_N5C112GX4_GetSquelchThreshold(devPtr, lane, threshold_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"lane = {lane}")
    logging.debug(f"threshold = {threshold}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_SetDataPath")
    devPtr = apiWrapper.pSerdesDev
    lane = 1
    path = E_N5C112GX4_DATAPATH.N5C112GX4_PATH_EXTERNAL.value
    try:
        API_N5C112GX4_SetDataPath(devPtr, lane, path)
    except Exception:
        traceback.print_exc()
    logging.debug(f"lane = {lane}")
    logging.debug(f"path = {path}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_GetDataPath")
    devPtr = apiWrapper.pSerdesDev
    lane = 1
    path = E_N5C112GX4_DATAPATH.N5C112GX4_PATH_EXTERNAL.value
    path_p = c_long(path)
    try:
        API_N5C112GX4_GetDataPath(devPtr, lane, path_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"lane = {lane}")
    logging.debug(f"path = {path}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_GetTemperature")
    devPtr = apiWrapper.pSerdesDev
    temperature = 1
    temperature_p = c_int32(temperature)
    try:
        API_N5C112GX4_GetTemperature(devPtr, temperature_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"temperature = {temperature}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_SetTxRxPolarity")
    devPtr = apiWrapper.pSerdesDev
    lane = 1
    txPolarity = E_N5C112GX4_POLARITY.N5C112GX4_POLARITY_NORMAL.value
    rxPolarity = E_N5C112GX4_POLARITY.N5C112GX4_POLARITY_NORMAL.value
    try:
        API_N5C112GX4_SetTxRxPolarity(devPtr, lane, txPolarity, rxPolarity)
    except Exception:
        traceback.print_exc()
    logging.debug(f"lane = {lane}")
    logging.debug(f"txPolarity = {txPolarity}")
    logging.debug(f"rxPolarity = {rxPolarity}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_GetTxRxPolarity")
    devPtr = apiWrapper.pSerdesDev
    lane = 1
    txPolarity = E_N5C112GX4_POLARITY.N5C112GX4_POLARITY_NORMAL.value
    txPolarity_p = c_long(txPolarity)
    rxPolarity = E_N5C112GX4_POLARITY.N5C112GX4_POLARITY_NORMAL.value
    rxPolarity_p = c_long(rxPolarity)
    try:
        API_N5C112GX4_GetTxRxPolarity(devPtr, lane, txPolarity_p, rxPolarity_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"lane = {lane}")
    logging.debug(f"txPolarity = {txPolarity}")
    logging.debug(f"rxPolarity = {rxPolarity}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_TxInjectError")
    devPtr = apiWrapper.pSerdesDev
    lane = 1
    errors = 1
    try:
        API_N5C112GX4_TxInjectError(devPtr, lane, errors)
    except Exception:
        traceback.print_exc()
    logging.debug(f"lane = {lane}")
    logging.debug(f"errors = {errors}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_SetTxRxPattern")
    devPtr = apiWrapper.pSerdesDev
    lane = 1
    txPattern = E_N5C112GX4_PATTERN.N5C112GX4_PAT_USER.value
    rxPattern = E_N5C112GX4_PATTERN.N5C112GX4_PAT_USER.value
    txUserPattern = 1
    txUserPattern_p = c_char(txUserPattern)
    rxUserPattern = 1
    rxUserPattern_p = c_char(rxUserPattern)
    try:
        API_N5C112GX4_SetTxRxPattern(devPtr, lane, txPattern, rxPattern, txUserPattern_p, rxUserPattern_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"lane = {lane}")
    logging.debug(f"txPattern = {txPattern}")
    logging.debug(f"rxPattern = {rxPattern}")
    logging.debug(f"txUserPattern = {txUserPattern}")
    logging.debug(f"rxUserPattern = {rxUserPattern}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_GetTxRxPattern")
    devPtr = apiWrapper.pSerdesDev
    lane = 1
    txPattern = E_N5C112GX4_PATTERN.N5C112GX4_PAT_USER.value
    txPattern_p = c_long(txPattern)
    rxPattern = E_N5C112GX4_PATTERN.N5C112GX4_PAT_USER.value
    rxPattern_p = c_long(rxPattern)
    txUserPattern = 1
    txUserPattern_p = c_char(txUserPattern)
    rxUserPattern = 1
    rxUserPattern_p = c_char(rxUserPattern)
    try:
        API_N5C112GX4_GetTxRxPattern(devPtr, lane, txPattern_p, rxPattern_p, txUserPattern_p, rxUserPattern_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"lane = {lane}")
    logging.debug(f"txPattern = {txPattern}")
    logging.debug(f"rxPattern = {rxPattern}")
    logging.debug(f"txUserPattern = {txUserPattern}")
    logging.debug(f"rxUserPattern = {rxUserPattern}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_SetMSBLSBSwap")
    devPtr = apiWrapper.pSerdesDev
    lane = 1
    txSwapMsbLsb = E_N5C112GX4_SWAP_MSB_LSB.N5C112GX4_SWAP_DISABLE.value
    rxSwapMsbLsb = E_N5C112GX4_SWAP_MSB_LSB.N5C112GX4_SWAP_DISABLE.value
    try:
        API_N5C112GX4_SetMSBLSBSwap(devPtr, lane, txSwapMsbLsb, rxSwapMsbLsb)
    except Exception:
        traceback.print_exc()
    logging.debug(f"lane = {lane}")
    logging.debug(f"txSwapMsbLsb = {txSwapMsbLsb}")
    logging.debug(f"rxSwapMsbLsb = {rxSwapMsbLsb}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_GetMSBLSBSwap")
    devPtr = apiWrapper.pSerdesDev
    lane = 1
    txSwapMsbLsb = E_N5C112GX4_SWAP_MSB_LSB.N5C112GX4_SWAP_DISABLE.value
    txSwapMsbLsb_p = c_long(txSwapMsbLsb)
    rxSwapMsbLsb = E_N5C112GX4_SWAP_MSB_LSB.N5C112GX4_SWAP_DISABLE.value
    rxSwapMsbLsb_p = c_long(rxSwapMsbLsb)
    try:
        API_N5C112GX4_GetMSBLSBSwap(devPtr, lane, txSwapMsbLsb_p, rxSwapMsbLsb_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"lane = {lane}")
    logging.debug(f"txSwapMsbLsb = {txSwapMsbLsb}")
    logging.debug(f"rxSwapMsbLsb = {rxSwapMsbLsb}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_SetGrayCode")
    devPtr = apiWrapper.pSerdesDev
    lane = 1
    txGrayCode = E_N5C112GX4_GRAY_CODE.N5C112GX4_GRAY_CODE_DISABLE.value
    rxGrayCode = E_N5C112GX4_GRAY_CODE.N5C112GX4_GRAY_CODE_DISABLE.value
    try:
        API_N5C112GX4_SetGrayCode(devPtr, lane, txGrayCode, rxGrayCode)
    except Exception:
        traceback.print_exc()
    logging.debug(f"lane = {lane}")
    logging.debug(f"txGrayCode = {txGrayCode}")
    logging.debug(f"rxGrayCode = {rxGrayCode}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_GetGrayCode")
    devPtr = apiWrapper.pSerdesDev
    lane = 1
    txGrayCode = E_N5C112GX4_GRAY_CODE.N5C112GX4_GRAY_CODE_DISABLE.value
    txGrayCode_p = c_long(txGrayCode)
    rxGrayCode = E_N5C112GX4_GRAY_CODE.N5C112GX4_GRAY_CODE_DISABLE.value
    rxGrayCode_p = c_long(rxGrayCode)
    try:
        API_N5C112GX4_GetGrayCode(devPtr, lane, txGrayCode_p, rxGrayCode_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"lane = {lane}")
    logging.debug(f"txGrayCode = {txGrayCode}")
    logging.debug(f"rxGrayCode = {rxGrayCode}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_GetDataAcquisitionRate")
    devPtr = apiWrapper.pSerdesDev
    lane = 1
    acqRate = E_N5C112GX4_DATA_ACQ_RATE.N5C112GX4_RATE_QUARTER.value
    acqRate_p = c_long(acqRate)
    try:
        API_N5C112GX4_GetDataAcquisitionRate(devPtr, lane, acqRate_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"lane = {lane}")
    logging.debug(f"acqRate = {acqRate}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_ExecuteTraining")
    devPtr = apiWrapper.pSerdesDev
    lane = 1
    type = E_N5C112GX4_TRAINING.N5C112GX4_TRAINING_TRX.value
    try:
        API_N5C112GX4_ExecuteTraining(devPtr, lane, type)
    except Exception:
        traceback.print_exc()
    logging.debug(f"lane = {lane}")
    logging.debug(f"type = {type}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_StartTraining")
    devPtr = apiWrapper.pSerdesDev
    lane = 1
    type = E_N5C112GX4_TRAINING.N5C112GX4_TRAINING_TRX.value
    try:
        API_N5C112GX4_StartTraining(devPtr, lane, type)
    except Exception:
        traceback.print_exc()
    logging.debug(f"lane = {lane}")
    logging.debug(f"type = {type}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_CheckTraining")
    devPtr = apiWrapper.pSerdesDev
    lane = 1
    type = E_N5C112GX4_TRAINING.N5C112GX4_TRAINING_TRX.value
    completed = MCESD_BOOL.MCESD_FALSE.value
    completed_p = c_long(completed)
    failed = MCESD_BOOL.MCESD_FALSE.value
    failed_p = c_long(failed)
    try:
        API_N5C112GX4_CheckTraining(devPtr, lane, type, completed_p, failed_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"lane = {lane}")
    logging.debug(f"type = {type}")
    logging.debug(f"completed = {completed}")
    logging.debug(f"failed = {failed}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_StopTraining")
    devPtr = apiWrapper.pSerdesDev
    lane = 1
    type = E_N5C112GX4_TRAINING.N5C112GX4_TRAINING_TRX.value
    try:
        API_N5C112GX4_StopTraining(devPtr, lane, type)
    except Exception:
        traceback.print_exc()
    logging.debug(f"lane = {lane}")
    logging.debug(f"type = {type}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_GetComparatorStats")
    devPtr = apiWrapper.pSerdesDev
    lane = 1
    statistics = S_N5C112GX4_PATTERN_STATISTICS(0, 0, 0, 0)
    statistics_p = byref(statistics)
    try:
        API_N5C112GX4_GetComparatorStats(devPtr, lane, statistics_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"lane = {lane}")
    logging.debug(f"statistics = {S_N5C112GX4_PATTERN_STATISTICS.totalErrorBits}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_ResetComparatorStats")
    devPtr = apiWrapper.pSerdesDev
    lane = 1
    try:
        API_N5C112GX4_ResetComparatorStats(devPtr, lane)
    except Exception:
        traceback.print_exc()
    logging.debug(f"lane = {lane}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_StartPhyTest")
    devPtr = apiWrapper.pSerdesDev
    lane = 1
    try:
        API_N5C112GX4_StartPhyTest(devPtr, lane)
    except Exception:
        traceback.print_exc()
    logging.debug(f"lane = {lane}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_StopPhyTest")
    devPtr = apiWrapper.pSerdesDev
    lane = 1
    try:
        API_N5C112GX4_StopPhyTest(devPtr, lane)
    except Exception:
        traceback.print_exc()
    logging.debug(f"lane = {lane}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_EOMInit")
    devPtr = apiWrapper.pSerdesDev
    lane = 1
    try:
        API_N5C112GX4_EOMInit(devPtr, lane)
    except Exception:
        traceback.print_exc()
    logging.debug(f"lane = {lane}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_EOMFinalize")
    devPtr = apiWrapper.pSerdesDev
    lane = 1
    try:
        API_N5C112GX4_EOMFinalize(devPtr, lane)
    except Exception:
        traceback.print_exc()
    logging.debug(f"lane = {lane}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_EOMMeasPoint")
    devPtr = apiWrapper.pSerdesDev
    lane = 1
    eyeTMB = E_N5C112GX4_EYE_TMB.N5C112GX4_EYE_MID.value
    phase = 1
    voltage = 1
    measurement = S_N5C112GX4_EOM_DATA(0, 0, 0, 0, 0, 0)
    measurement_p = byref(measurement)
    try:
        API_N5C112GX4_EOMMeasPoint(devPtr, lane, eyeTMB, phase, voltage, measurement_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"lane = {lane}")
    logging.debug(f"eyeTMB = {eyeTMB}")
    logging.debug(f"phase = {phase}")
    logging.debug(f"voltage = {voltage}")
    logging.debug(f"measurement = {S_N5C112GX4_EOM_DATA.lowerBitErrorCount}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_EOM1UIStepCount")
    devPtr = apiWrapper.pSerdesDev
    lane = 1
    phaseStepCount = 1
    phaseStepCount_p = c_uint16(phaseStepCount)
    voltageStepCount = 1
    voltageStepCount_p = c_uint16(voltageStepCount)
    try:
        API_N5C112GX4_EOM1UIStepCount(devPtr, lane, phaseStepCount_p, voltageStepCount_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"lane = {lane}")
    logging.debug(f"phaseStepCount = {phaseStepCount}")
    logging.debug(f"voltageStepCount = {voltageStepCount}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_EOMGetWidthHeight")
    devPtr = apiWrapper.pSerdesDev
    lane = 1
    eyeTMB = E_N5C112GX4_EYE_TMB.N5C112GX4_EYE_MID.value
    width = 1
    width_p = c_uint16(width)
    height = 1
    height_p = c_uint16(height)
    try:
        API_N5C112GX4_EOMGetWidthHeight(devPtr, lane, eyeTMB, width_p, height_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"lane = {lane}")
    logging.debug(f"eyeTMB = {eyeTMB}")
    logging.debug(f"width = {width}")
    logging.debug(f"height = {height}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_ExecuteCDS")
    devPtr = apiWrapper.pSerdesDev
    lane = 1
    try:
        API_N5C112GX4_ExecuteCDS(devPtr, lane)
    except Exception:
        traceback.print_exc()
    logging.debug(f"lane = {lane}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_GetSNR")
    devPtr = apiWrapper.pSerdesDev
    lane = 1
    snr = 1
    snr_p = c_uint32(snr)
    try:
        API_N5C112GX4_GetSNR(devPtr, lane, snr_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"lane = {lane}")
    logging.debug(f"snr = {snr}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_PowerOnSeq")
    devPtr = apiWrapper.pSerdesDev
    powerOn = S_N5C112GX4_PowerOn(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    try:
        API_N5C112GX4_PowerOnSeq(devPtr, powerOn)
    except Exception:
        traceback.print_exc()
    logging.debug(f"powerOn = {S_N5C112GX4_PowerOn.fwDownload}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_PowerOffLane")
    devPtr = apiWrapper.pSerdesDev
    lane = 1
    try:
        API_N5C112GX4_PowerOffLane(devPtr, lane)
    except Exception:
        traceback.print_exc()
    logging.debug(f"lane = {lane}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_DownloadFirmware")
    devPtr = apiWrapper.pSerdesDev
    fwCodePtr = 1
    fwCodePtr_p = c_uint32(fwCodePtr)
    fwCodeSizeDW = 1
    errCode = 1
    errCode_p = c_uint16(errCode)
    try:
        API_N5C112GX4_DownloadFirmware(devPtr, fwCodePtr_p, fwCodeSizeDW, errCode_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"fwCodePtr = {fwCodePtr}")
    logging.debug(f"fwCodeSizeDW = {fwCodeSizeDW}")
    logging.debug(f"errCode = {errCode}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_UpdateRamCode")
    devPtr = apiWrapper.pSerdesDev
    lane = 1
    code = 1
    code_p = c_uint32(code)
    codeSize = 1
    memSize = 1
    address = 1
    errCode = 1
    errCode_p = c_uint16(errCode)
    try:
        API_N5C112GX4_UpdateRamCode(devPtr, lane, code_p, codeSize, memSize, address, errCode_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"lane = {lane}")
    logging.debug(f"code = {code}")
    logging.debug(f"codeSize = {codeSize}")
    logging.debug(f"memSize = {memSize}")
    logging.debug(f"address = {address}")
    logging.debug(f"errCode = {errCode}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_HwWriteReg")
    devPtr = apiWrapper.pSerdesDev
    reg = 1
    value = 1
    try:
        API_N5C112GX4_HwWriteReg(devPtr, reg, value)
    except Exception:
        traceback.print_exc()
    logging.debug(f"reg = {reg}")
    logging.debug(f"value = {value}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_HwReadReg")
    devPtr = apiWrapper.pSerdesDev
    reg = 1
    data = 1
    data_p = c_uint32(data)
    try:
        API_N5C112GX4_HwReadReg(devPtr, reg, data_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"reg = {reg}")
    logging.debug(f"data = {data}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_HwSetPinCfg")
    devPtr = apiWrapper.pSerdesDev
    pin = E_N5C112GX4_PIN.N5C112GX4_PIN_RESET.value
    pinValue = 1
    try:
        API_N5C112GX4_HwSetPinCfg(devPtr, pin, pinValue)
    except Exception:
        traceback.print_exc()
    logging.debug(f"pin = {pin}")
    logging.debug(f"pinValue = {pinValue}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_HwGetPinCfg")
    devPtr = apiWrapper.pSerdesDev
    pin = E_N5C112GX4_PIN.N5C112GX4_PIN_RESET.value
    pinValue = 1
    pinValue_p = c_uint16(pinValue)
    try:
        API_N5C112GX4_HwGetPinCfg(devPtr, pin, pinValue_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"pin = {pin}")
    logging.debug(f"pinValue = {pinValue}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_Wait")
    devPtr = apiWrapper.pSerdesDev
    ms = 1
    try:
        API_N5C112GX4_Wait(devPtr, ms)
    except Exception:
        traceback.print_exc()
    logging.debug(f"ms = {ms}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_WriteReg")
    devPtr = apiWrapper.pSerdesDev
    lane = 1
    reg = 1
    value = 1
    try:
        API_N5C112GX4_WriteReg(devPtr, lane, reg, value)
    except Exception:
        traceback.print_exc()
    logging.debug(f"lane = {lane}")
    logging.debug(f"reg = {reg}")
    logging.debug(f"value = {value}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_ReadReg")
    devPtr = apiWrapper.pSerdesDev
    lane = 1
    reg = 1
    data = 1
    data_p = c_uint32(data)
    try:
        API_N5C112GX4_ReadReg(devPtr, lane, reg, data_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"lane = {lane}")
    logging.debug(f"reg = {reg}")
    logging.debug(f"data = {data}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_WriteField")
    devPtr = apiWrapper.pSerdesDev
    lane = 1
    fieldPtr = MCESD_FIELD(0, 0, 0, 0, 0, 0)
    value = 1
    value_p = c_uint32(value)
    try:
        API_N5C112GX4_WriteField(devPtr, lane, fieldPtr, value_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"lane = {lane}")
    logging.debug(f"fieldPtr = {MCESD_FIELD.retainMask}")
    logging.debug(f"value = {value}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_ReadField")
    devPtr = apiWrapper.pSerdesDev
    lane = 1
    fieldPtr = MCESD_FIELD(0, 0, 0, 0, 0, 0)
    data = 1
    data_p = c_uint32(data)
    try:
        API_N5C112GX4_ReadField(devPtr, lane, fieldPtr, data_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"lane = {lane}")
    logging.debug(f"fieldPtr = {MCESD_FIELD.retainMask}")
    logging.debug(f"data = {data}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_PollField")
    devPtr = apiWrapper.pSerdesDev
    lane = 1
    fieldPtr = MCESD_FIELD(0, 0, 0, 0, 0, 0)
    value = 1
    value_p = c_uint32(value)
    timeout_ms = 1
    try:
        API_N5C112GX4_PollField(devPtr, lane, fieldPtr, value_p, timeout_ms)
    except Exception:
        traceback.print_exc()
    logging.debug(f"lane = {lane}")
    logging.debug(f"fieldPtr = {MCESD_FIELD.retainMask}")
    logging.debug(f"value = {value}")
    logging.debug(f"timeout_ms = {timeout_ms}")
    logging.info("\n")

    logging.info("Function name : API_N5C112GX4_PollPin")
    devPtr = apiWrapper.pSerdesDev
    pin = E_N5C112GX4_PIN.N5C112GX4_PIN_RESET.value
    value = 1
    timeout_ms = 1
    try:
        API_N5C112GX4_PollPin(devPtr, pin, value, timeout_ms)
    except Exception:
        traceback.print_exc()
    logging.debug(f"pin = {pin}")
    logging.debug(f"value = {value}")
    logging.debug(f"timeout_ms = {timeout_ms}")
    logging.info("\n")

