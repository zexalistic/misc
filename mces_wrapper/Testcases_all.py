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
from mzdFunctionLib import *
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
    pDev = apiWrapper.devHandle

    cur_time = time.strftime("%m-%d-%Y_%H-%M-%S", time.localtime())
    logging.basicConfig(level=logging.DEBUG,
                        filename=f'X93160_API_test_{cur_time}.log',
                        format='%(message)s',
                        datefmt='%d-%M-%Y %H:%M:%S')

    # Data path's choice has problem

    logging.info("Function name : mzdGetAPIVersion")
    major = 1
    major_p = c_uint8(major)
    minor = 1
    minor_p = c_uint8(minor)
    buildID = 1
    buildID_p = c_uint8(buildID)
    try:
        mzdGetAPIVersion(major_p, minor_p, buildID_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"major = {major_p.value}")
    logging.debug(f"minor = {minor_p.value}")
    logging.debug(f"buildID = {buildID_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdSetModeSelection")
    mdioPort = 1
    laneOffset = 1
    hostMode = MZD_OP_MODE.MZD_OP_MODE_UNKNOWN.value
    lineMode = MZD_OP_MODE.MZD_OP_MODE_UNKNOWN.value
    modeOptionSel = 1
    buffer = (c_uint8 * 128)()
    buffer_init = [0] * 128
    for idx, value in enumerate(buffer_init):
        buffer[idx] = value
    modeOption = MZD_MODE_OPTION_STRUCT(buffer)
    result = 1
    result_p = c_uint16(result)
    try:
        mzdSetModeSelection(pDev, mdioPort, laneOffset, hostMode, lineMode, modeOptionSel, modeOption, result_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"hostMode = {hostMode}")
    logging.debug(f"lineMode = {lineMode}")
    logging.debug(f"modeOptionSel = {modeOptionSel}")
    logging.debug(f"result = {result_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdSetInterfaceUserMode")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    opMode = MZD_OP_MODE.MZD_OP_MODE_UNKNOWN.value
    modeOptionSel = 1
    buffer = (c_uint8 * 128)()
    buffer_init = [0] * 128
    for idx, value in enumerate(buffer_init):
        buffer[idx] = value
    modeOption = MZD_MODE_OPTION_STRUCT(buffer)
    result = 1
    result_p = c_uint16(result)
    try:
        mzdSetInterfaceUserMode(pDev, mdioPort, host_or_line, laneOffset, opMode, modeOptionSel, modeOption, result_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"opMode = {opMode}")
    logging.debug(f"modeOptionSel = {modeOptionSel}")
    logging.debug(f"result = {result_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdGetOpMode")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    opMode = MZD_OP_MODE.MZD_OP_MODE_UNKNOWN.value
    opMode_p = MZD_OP_MODE(opMode)
    try:
        mzdGetOpMode(pDev, mdioPort, host_or_line, laneOffset, opMode_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"opMode = {opMode_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdAutoNegControl")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    enableAutoNeg = 1
    swReset = MZD_BOOL.MZD_FALSE.value
    try:
        mzdAutoNegControl(pDev, mdioPort, host_or_line, laneOffset, enableAutoNeg, swReset)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"enableAutoNeg = {enableAutoNeg}")
    logging.debug(f"swReset = {swReset}")
    logging.info("\n")

    logging.info("Function name : mzdAutoNegCheckComplete")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    autoNegComplete = MZD_BOOL.MZD_FALSE.value
    autoNegComplete_p = MZD_BOOL(autoNegComplete)
    try:
        mzdAutoNegCheckComplete(pDev, mdioPort, host_or_line, laneOffset, autoNegComplete_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"autoNegComplete = {autoNegComplete_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdGetAutoNegResolution")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    speed_bits = 1
    speed_bits_p = c_uint16(speed_bits)
    try:
        mzdGetAutoNegResolution(pDev, mdioPort, host_or_line, laneOffset, speed_bits_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"speed_bits = {speed_bits_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdCL37AutoNegControl")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    enableAutoNeg = 1
    try:
        mzdCL37AutoNegControl(pDev, mdioPort, host_or_line, laneOffset, enableAutoNeg)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"enableAutoNeg = {enableAutoNeg}")
    logging.info("\n")

    logging.info("Function name : mzdCL37AutoNegCheckComplete")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    autoNegComplete = MZD_BOOL.MZD_FALSE.value
    autoNegComplete_p = MZD_BOOL(autoNegComplete)
    try:
        mzdCL37AutoNegCheckComplete(pDev, mdioPort, host_or_line, laneOffset, autoNegComplete_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"autoNegComplete = {autoNegComplete_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdSetPauseAdvertisement")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    pauseType = 1
    swReset = MZD_BOOL.MZD_FALSE.value
    try:
        mzdSetPauseAdvertisement(pDev, mdioPort, host_or_line, laneOffset, pauseType, swReset)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"pauseType = {pauseType}")
    logging.debug(f"swReset = {swReset}")
    logging.info("\n")

    logging.info("Function name : mzdGetPauseAdvertisement")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    pauseType = 1
    pauseType_p = c_uint16(pauseType)
    try:
        mzdGetPauseAdvertisement(pDev, mdioPort, host_or_line, laneOffset, pauseType_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"pauseType = {pauseType_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdGetLPAdvertisedPause")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    pauseType = 1
    pauseType_p = c_uint16(pauseType)
    try:
        mzdGetLPAdvertisedPause(pDev, mdioPort, host_or_line, laneOffset, pauseType_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"pauseType = {pauseType_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdGetTxRxPauseResolution")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    pauseResolved = MZD_BOOL.MZD_FALSE.value
    pauseResolved_p = MZD_BOOL(pauseResolved)
    tx_pause_enabled = MZD_BOOL.MZD_FALSE.value
    tx_pause_enabled_p = MZD_BOOL(tx_pause_enabled)
    rx_pause_enabled = MZD_BOOL.MZD_FALSE.value
    rx_pause_enabled_p = MZD_BOOL(rx_pause_enabled)
    try:
        mzdGetTxRxPauseResolution(pDev, mdioPort, host_or_line, laneOffset, pauseResolved_p, tx_pause_enabled_p, rx_pause_enabled_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"pauseResolved = {pauseResolved_p.value}")
    logging.debug(f"tx_pause_enabled = {tx_pause_enabled_p.value}")
    logging.debug(f"rx_pause_enabled = {rx_pause_enabled_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdCheckPCSLinkStatus")
    mdioPort = 1
    laneOffset = 1
    currentStatus = 1
    currentStatus_p = c_uint16(currentStatus)
    latchedStatus = 1
    latchedStatus_p = c_uint16(latchedStatus)
    statusDetail = MZD_PCS_LINK_STATUS(0, 0, 0, 0)
    statusDetail_p = byref(statusDetail)
    try:
        mzdCheckPCSLinkStatus(pDev, mdioPort, laneOffset, currentStatus_p, latchedStatus_p, statusDetail_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"currentStatus = {currentStatus_p.value}")
    logging.debug(f"latchedStatus = {latchedStatus_p.value}")
    logging.debug(f"statusDetail = {MZD_PCS_LINK_STATUS.hostCurrent}")
    logging.debug(f"statusDetail = {MZD_PCS_LINK_STATUS.hostLatched}")
    logging.debug(f"statusDetail = {MZD_PCS_LINK_STATUS.lineCurrent}")
    logging.debug(f"statusDetail = {MZD_PCS_LINK_STATUS.lineLatched}")
    logging.info("\n")

    logging.info("Function name : mzdGetDetailedLinkStatus")
    mdioPort = 1
    laneOffset = 1
    host_or_line = 1
    currStat = 1
    currStat_p = c_uint16(currStat)
    latchStat = 1
    latchStat_p = c_uint16(latchStat)
    try:
        mzdGetDetailedLinkStatus(pDev, mdioPort, laneOffset, host_or_line, currStat_p, latchStat_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"currStat = {currStat_p.value}")
    logging.debug(f"latchStat = {latchStat_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdGetPcsFaultStatus")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    currentTxFaultStatus = 1
    currentTxFaultStatus_p = c_uint16(currentTxFaultStatus)
    currentRxFaultStatus = 1
    currentRxFaultStatus_p = c_uint16(currentRxFaultStatus)
    latchedTxFaultStatus = 1
    latchedTxFaultStatus_p = c_uint16(latchedTxFaultStatus)
    latchedRxFaultStatus = 1
    latchedRxFaultStatus_p = c_uint16(latchedRxFaultStatus)
    try:
        mzdGetPcsFaultStatus(pDev, mdioPort, host_or_line, laneOffset, currentTxFaultStatus_p, currentRxFaultStatus_p, latchedTxFaultStatus_p, latchedRxFaultStatus_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"currentTxFaultStatus = {currentTxFaultStatus_p.value}")
    logging.debug(f"currentRxFaultStatus = {currentRxFaultStatus_p.value}")
    logging.debug(f"latchedTxFaultStatus = {latchedTxFaultStatus_p.value}")
    logging.debug(f"latchedRxFaultStatus = {latchedRxFaultStatus_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdLaneSoftReset")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    timeoutMs = 1
    try:
        mzdLaneSoftReset(pDev, mdioPort, host_or_line, laneOffset, timeoutMs)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"timeoutMs = {timeoutMs}")
    logging.info("\n")

    logging.info("Function name : mzdSetDPFaultConfig")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    datapathMode = 1
    txType = 1
    rxType = 1
    try:
        mzdSetDPFaultConfig(pDev, mdioPort, host_or_line, laneOffset, datapathMode, txType, rxType)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"datapathMode = {datapathMode}")
    logging.debug(f"txType = {txType}")
    logging.debug(f"rxType = {rxType}")
    logging.info("\n")

    logging.info("Function name : mzdGetDPFaultConfig")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    datapathMode = 1
    datapathMode_p = c_uint16(datapathMode)
    txType = 1
    txType_p = c_uint16(txType)
    rxType = 1
    rxType_p = c_uint16(rxType)
    try:
        mzdGetDPFaultConfig(pDev, mdioPort, host_or_line, laneOffset, datapathMode_p, txType_p, rxType_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"datapathMode = {datapathMode_p.value}")
    logging.debug(f"txType = {txType_p.value}")
    logging.debug(f"rxType = {rxType_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdSetSerdesMux")
    host_or_line = 1
    serdesMux = 1
    serdesMux_p = c_uint8(serdesMux)
    try:
        mzdSetSerdesMux(pDev, host_or_line, serdesMux_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"serdesMux = {serdesMux_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdGetSerdesMux")
    host_or_line = 1
    serdesMux = 1
    serdesMux_p = c_uint8(serdesMux)
    try:
        mzdGetSerdesMux(pDev, host_or_line, serdesMux_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"serdesMux = {serdesMux_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdGetLaneRxTrainingState")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    rxTraining = MZD_BOOL.MZD_FALSE.value
    rxTraining_p = MZD_BOOL(rxTraining)
    try:
        mzdGetLaneRxTrainingState(pDev, mdioPort, host_or_line, laneOffset, rxTraining_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"rxTraining = {rxTraining_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdGetChipRevision")
    mdioPort = 1
    deviceId = MZD_DEVICE_ID.MZD_DEV_X7121M.value
    deviceId_p = MZD_DEVICE_ID(deviceId)
    try:
        mzdGetChipRevision(pDev, mdioPort, deviceId_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"deviceId = {deviceId_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdDevicePortCount")
    mdioPort = 1
    portCount = 1
    portCount_p = c_uint16(portCount)
    try:
        mzdDevicePortCount(pDev, mdioPort, portCount_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"portCount = {portCount_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdGetChipFWRevision")
    major = 1
    major_p = c_uint16(major)
    minor = 1
    minor_p = c_uint16(minor)
    patch = 1
    patch_p = c_uint16(patch)
    build = 1
    build_p = c_uint16(build)
    try:
        mzdGetChipFWRevision(pDev, major_p, minor_p, patch_p, build_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"major = {major_p.value}")
    logging.debug(f"minor = {minor_p.value}")
    logging.debug(f"patch = {patch_p.value}")
    logging.debug(f"build = {build_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdGetSerdesFWRevision")
    major = 1
    major_p = c_uint8(major)
    minor = 1
    minor_p = c_uint8(minor)
    patch = 1
    patch_p = c_uint8(patch)
    build = 1
    build_p = c_uint8(build)
    try:
        mzdGetSerdesFWRevision(pDev, major_p, minor_p, patch_p, build_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"major = {major_p.value}")
    logging.debug(f"minor = {minor_p.value}")
    logging.debug(f"patch = {patch_p.value}")
    logging.debug(f"build = {build_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdGetSerdesFWRevisionAll")
    majorMZD_NUM_INTERFACEMZD_MAX_PORTS = 1
    majorMZD_NUM_INTERFACEMZD_MAX_PORTS_p = c_uint8(majorMZD_NUM_INTERFACEMZD_MAX_PORTS)
    minorMZD_NUM_INTERFACEMZD_MAX_PORTS = 1
    minorMZD_NUM_INTERFACEMZD_MAX_PORTS_p = c_uint8(minorMZD_NUM_INTERFACEMZD_MAX_PORTS)
    patchMZD_NUM_INTERFACEMZD_MAX_PORTS = 1
    patchMZD_NUM_INTERFACEMZD_MAX_PORTS_p = c_uint8(patchMZD_NUM_INTERFACEMZD_MAX_PORTS)
    buildMZD_NUM_INTERFACEMZD_MAX_PORTS = 1
    buildMZD_NUM_INTERFACEMZD_MAX_PORTS_p = c_uint8(buildMZD_NUM_INTERFACEMZD_MAX_PORTS)
    try:
        mzdGetSerdesFWRevisionAll(pDev, majorMZD_NUM_INTERFACEMZD_MAX_PORTS_p, minorMZD_NUM_INTERFACEMZD_MAX_PORTS_p, patchMZD_NUM_INTERFACEMZD_MAX_PORTS_p, buildMZD_NUM_INTERFACEMZD_MAX_PORTS_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"majorMZD_NUM_INTERFACEMZD_MAX_PORTS = {majorMZD_NUM_INTERFACEMZD_MAX_PORTS_p.value}")
    logging.debug(f"minorMZD_NUM_INTERFACEMZD_MAX_PORTS = {minorMZD_NUM_INTERFACEMZD_MAX_PORTS_p.value}")
    logging.debug(f"patchMZD_NUM_INTERFACEMZD_MAX_PORTS = {patchMZD_NUM_INTERFACEMZD_MAX_PORTS_p.value}")
    logging.debug(f"buildMZD_NUM_INTERFACEMZD_MAX_PORTS = {buildMZD_NUM_INTERFACEMZD_MAX_PORTS_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdGetFirmwareLoadStatus")
    loadStatus = MZD_FIRMWARE_STATUS.MZD_FIRMWARE_STATUS_UNKNOWN.value
    loadStatus_p = MZD_FIRMWARE_STATUS(loadStatus)
    try:
        mzdGetFirmwareLoadStatus(pDev, loadStatus_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"loadStatus = {loadStatus_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdGetSerdesSignalDetectAndDspLock")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    signalDetect = 1
    signalDetect_p = c_uint16(signalDetect)
    dspLock = 1
    dspLock_p = c_uint16(dspLock)
    try:
        mzdGetSerdesSignalDetectAndDspLock(pDev, mdioPort, host_or_line, laneOffset, signalDetect_p, dspLock_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"signalDetect = {signalDetect_p.value}")
    logging.debug(f"dspLock = {dspLock_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdSetPCSLineLoopback")
    mdioPort = 1
    laneOffset = 1
    loopback_type = MZD_PCS_MODE_LOOPBACK.MZD_PCS_SHALLOW_LOOPBACK.value
    enable = 1
    try:
        mzdSetPCSLineLoopback(pDev, mdioPort, laneOffset, loopback_type, enable)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"loopback_type = {loopback_type}")
    logging.debug(f"enable = {enable}")
    logging.info("\n")

    logging.info("Function name : mzdSetPCSHostLoopback")
    mdioPort = 1
    laneOffset = 1
    loopback_type = MZD_PCS_MODE_LOOPBACK.MZD_PCS_SHALLOW_LOOPBACK.value
    loopbackState = 1
    try:
        mzdSetPCSHostLoopback(pDev, mdioPort, laneOffset, loopback_type, loopbackState)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"loopback_type = {loopback_type}")
    logging.debug(f"loopbackState = {loopbackState}")
    logging.info("\n")

    logging.info("Function name : mzdHmuxSetPCSLineDeepLoopback")
    hostPort = 1
    hostLaneOffset = 1
    loopback_type = MZD_PCS_MODE_LOOPBACK.MZD_PCS_SHALLOW_LOOPBACK.value
    loopbackState = 1
    try:
        mzdHmuxSetPCSLineDeepLoopback(pDev, hostPort, hostLaneOffset, loopback_type, loopbackState)
    except Exception:
        traceback.print_exc()
    logging.debug(f"hostPort = {hostPort}")
    logging.debug(f"hostLaneOffset = {hostLaneOffset}")
    logging.debug(f"loopback_type = {loopback_type}")
    logging.debug(f"loopbackState = {loopbackState}")
    logging.info("\n")

    logging.info("Function name : mzdHmuxSetPCSHostDeepLoopback")
    linePort = 1
    lineLaneOffset = 1
    loopback_type = MZD_PCS_MODE_LOOPBACK.MZD_PCS_SHALLOW_LOOPBACK.value
    loopbackState = 1
    try:
        mzdHmuxSetPCSHostDeepLoopback(pDev, linePort, lineLaneOffset, loopback_type, loopbackState)
    except Exception:
        traceback.print_exc()
    logging.debug(f"linePort = {linePort}")
    logging.debug(f"lineLaneOffset = {lineLaneOffset}")
    logging.debug(f"loopback_type = {loopback_type}")
    logging.debug(f"loopbackState = {loopbackState}")
    logging.info("\n")

    logging.info("Function name : mzdSetSerdesLaneLoopback")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    loopbackState = 1
    swReset = MZD_BOOL.MZD_FALSE.value
    try:
        mzdSetSerdesLaneLoopback(pDev, mdioPort, host_or_line, laneOffset, loopbackState, swReset)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"loopbackState = {loopbackState}")
    logging.debug(f"swReset = {swReset}")
    logging.info("\n")

    logging.info("Function name : mzdGetSerdesLaneLoopback")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    loopbackState = 1
    loopbackState_p = c_uint16(loopbackState)
    try:
        mzdGetSerdesLaneLoopback(pDev, mdioPort, host_or_line, laneOffset, loopbackState_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"loopbackState = {loopbackState_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdConfigurePktGeneratorChecker")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    readToClear = MZD_BOOL.MZD_FALSE.value
    dontuseSFDinChecker = MZD_BOOL.MZD_FALSE.value
    pktPatternControl = 1
    generateCRCoff = MZD_BOOL.MZD_FALSE.value
    initialPayload = 1
    frameLengthControl = 1
    numPktsToSend = 1
    randomIPG = MZD_BOOL.MZD_FALSE.value
    ipgDuration = 1
    try:
        mzdConfigurePktGeneratorChecker(pDev, mdioPort, host_or_line, laneOffset, readToClear, dontuseSFDinChecker, pktPatternControl, generateCRCoff, initialPayload, frameLengthControl, numPktsToSend, randomIPG, ipgDuration)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"readToClear = {readToClear}")
    logging.debug(f"dontuseSFDinChecker = {dontuseSFDinChecker}")
    logging.debug(f"pktPatternControl = {pktPatternControl}")
    logging.debug(f"generateCRCoff = {generateCRCoff}")
    logging.debug(f"initialPayload = {initialPayload}")
    logging.debug(f"frameLengthControl = {frameLengthControl}")
    logging.debug(f"numPktsToSend = {numPktsToSend}")
    logging.debug(f"randomIPG = {randomIPG}")
    logging.debug(f"ipgDuration = {ipgDuration}")
    logging.info("\n")

    logging.info("Function name : mzdEnablePktGeneratorChecker")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    enableGenerator = MZD_BOOL.MZD_FALSE.value
    enableChecker = MZD_BOOL.MZD_FALSE.value
    try:
        mzdEnablePktGeneratorChecker(pDev, mdioPort, host_or_line, laneOffset, enableGenerator, enableChecker)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"enableGenerator = {enableGenerator}")
    logging.debug(f"enableChecker = {enableChecker}")
    logging.info("\n")

    logging.info("Function name : mzdStartStopPktGenTraffic")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    numPktsToSend = MZD_BOOL.MZD_FALSE.value
    try:
        mzdStartStopPktGenTraffic(pDev, mdioPort, host_or_line, laneOffset, numPktsToSend)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"numPktsToSend = {numPktsToSend}")
    logging.info("\n")

    logging.info("Function name : mzdPktGeneratorCounterReset")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    try:
        mzdPktGeneratorCounterReset(pDev, mdioPort, host_or_line, laneOffset)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.info("\n")

    logging.info("Function name : mzdPktGeneratorGetCounter")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    pktCntType = MZD_PKT_COUNT_TYPE.MZD_PKT_GET_TX.value
    packetCount = 1
    packetCount_p = c_uint64(packetCount)
    byteCount = 1
    byteCount_p = c_uint64(byteCount)
    try:
        mzdPktGeneratorGetCounter(pDev, mdioPort, host_or_line, laneOffset, pktCntType, packetCount_p, byteCount_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"pktCntType = {pktCntType}")
    logging.debug(f"packetCount = {packetCount_p.value}")
    logging.debug(f"byteCount = {byteCount_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdSetPRBSPattern")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    pattSel = MZD_PRBS_SELECTOR_TYPE.MZD_PRBS31.value
    pattSubSel = MZD_PATTERN_AB_SELECTOR_TYPE.MZD_PRBS_NONE.value
    try:
        mzdSetPRBSPattern(pDev, mdioPort, host_or_line, laneOffset, pattSel, pattSubSel)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"pattSel = {pattSel}")
    logging.debug(f"pattSubSel = {pattSubSel}")
    logging.info("\n")

    logging.info("Function name : mzdPRBSPatternOption")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    patternOption = 1
    try:
        mzdPRBSPatternOption(pDev, mdioPort, host_or_line, laneOffset, patternOption)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"patternOption = {patternOption}")
    logging.info("\n")

    logging.info("Function name : mzdSetPRBSEnableTxRx")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    txEnable = 1
    rxEnable = 1
    pattSel = MZD_PRBS_SELECTOR_TYPE.MZD_PRBS31.value
    try:
        mzdSetPRBSEnableTxRx(pDev, mdioPort, host_or_line, laneOffset, txEnable, rxEnable, pattSel)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"txEnable = {txEnable}")
    logging.debug(f"rxEnable = {rxEnable}")
    logging.debug(f"pattSel = {pattSel}")
    logging.info("\n")

    logging.info("Function name : mzdPRBSCounterReset")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    try:
        mzdPRBSCounterReset(pDev, mdioPort, host_or_line, laneOffset)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.info("\n")

    logging.info("Function name : mzdSetPRBSWaitForLock")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    disableWaitforLock = 1
    try:
        mzdSetPRBSWaitForLock(pDev, mdioPort, host_or_line, laneOffset, disableWaitforLock)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"disableWaitforLock = {disableWaitforLock}")
    logging.info("\n")

    logging.info("Function name : mzdGetPRBSWaitForLock")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    disableWaitforLock = 1
    disableWaitforLock_p = c_uint16(disableWaitforLock)
    try:
        mzdGetPRBSWaitForLock(pDev, mdioPort, host_or_line, laneOffset, disableWaitforLock_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"disableWaitforLock = {disableWaitforLock_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdSetPRBSClearOnRead")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    enableReadClear = 1
    try:
        mzdSetPRBSClearOnRead(pDev, mdioPort, host_or_line, laneOffset, enableReadClear)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"enableReadClear = {enableReadClear}")
    logging.info("\n")

    logging.info("Function name : mzdGetPRBSClearOnRead")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    enableReadClear = 1
    enableReadClear_p = c_uint16(enableReadClear)
    try:
        mzdGetPRBSClearOnRead(pDev, mdioPort, host_or_line, laneOffset, enableReadClear_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"enableReadClear = {enableReadClear_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdGetPRBSLocked")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    prbsLocked = MZD_BOOL.MZD_FALSE.value
    prbsLocked_p = MZD_BOOL(prbsLocked)
    try:
        mzdGetPRBSLocked(pDev, mdioPort, host_or_line, laneOffset, prbsLocked_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"prbsLocked = {prbsLocked_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdGetPRBSCounts")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    pattSel = MZD_PRBS_SELECTOR_TYPE.MZD_PRBS31.value
    txBitCount = 1
    txBitCount_p = c_uint64(txBitCount)
    rxBitCount = 1
    rxBitCount_p = c_uint64(rxBitCount)
    rxBitErrorCount = 1
    rxBitErrorCount_p = c_uint64(rxBitErrorCount)
    try:
        mzdGetPRBSCounts(pDev, mdioPort, host_or_line, laneOffset, pattSel, txBitCount_p, rxBitCount_p, rxBitErrorCount_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"pattSel = {pattSel}")
    logging.debug(f"txBitCount = {txBitCount_p.value}")
    logging.debug(f"rxBitCount = {rxBitCount_p.value}")
    logging.debug(f"rxBitErrorCount = {rxBitErrorCount_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdSetTxRxPolarity")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    txPolarity = 1
    rxPolarity = 1
    try:
        mzdSetTxRxPolarity(pDev, mdioPort, host_or_line, laneOffset, txPolarity, rxPolarity)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"txPolarity = {txPolarity}")
    logging.debug(f"rxPolarity = {rxPolarity}")
    logging.info("\n")

    logging.info("Function name : mzdGetTxRxPolarity")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    txPolarity = 1
    txPolarity_p = c_uint8(txPolarity)
    rxPolarity = 1
    rxPolarity_p = c_uint8(rxPolarity)
    try:
        mzdGetTxRxPolarity(pDev, mdioPort, host_or_line, laneOffset, txPolarity_p, rxPolarity_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"txPolarity = {txPolarity_p.value}")
    logging.debug(f"rxPolarity = {rxPolarity_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdSetTxFFE")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    txEqParamType = E_N5C112GX4_TXEQ_PARAM.N5C112GX4_TXEQ_EM_PRE3_CTRL.value
    paramValue = 1
    try:
        mzdSetTxFFE(pDev, mdioPort, host_or_line, laneOffset, txEqParamType, paramValue)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"txEqParamType = {txEqParamType}")
    logging.debug(f"paramValue = {paramValue}")
    logging.info("\n")

    logging.info("Function name : mzdGetTxFFE")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    txEqParamType = E_N5C112GX4_TXEQ_PARAM.N5C112GX4_TXEQ_EM_PRE3_CTRL.value
    paramValue = 1
    paramValue_p = c_uint32(paramValue)
    try:
        mzdGetTxFFE(pDev, mdioPort, host_or_line, laneOffset, txEqParamType, paramValue_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"txEqParamType = {txEqParamType}")
    logging.debug(f"paramValue = {paramValue_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdDiagStateDump")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    stateDumpOptions = 1
    apiVersion = (c_uint8 * 3)()
    apiVersion_init = [0] * 3
    for idx, value in enumerate(apiVersion_init):
        apiVersion[idx] = value
    fwVersion = (c_uint8 * 4)()
    fwVersion_init = [0] * 4
    for idx, value in enumerate(fwVersion_init):
        fwVersion[idx] = value
    serdesRevision = (c_uint8 * 4)()
    serdesRevision_init = [0] * 4
    for idx, value in enumerate(serdesRevision_init):
        serdesRevision[idx] = value
    statusPCSReg = (c_uint16 * 2)()
    statusPCSReg_init = [0] * 2
    for idx, value in enumerate(statusPCSReg_init):
        statusPCSReg[idx] = value
    ctrlVal = (c_uint32 * 64)()
    ctrlVal_init = [0] * 64
    for idx, value in enumerate(ctrlVal_init):
        ctrlVal[idx] = value
    pStateDumpInfo = MZD_STATE_DUMP(0, apiVersion, fwVersion, serdesRevision, 0, 0, statusPCSReg, 0, 0, 0, ctrlVal)
    pStateDumpInfo_p = byref(pStateDumpInfo)
    try:
        mzdDiagStateDump(pDev, mdioPort, host_or_line, laneOffset, stateDumpOptions, pStateDumpInfo_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"stateDumpOptions = {stateDumpOptions}")
    logging.debug(f"pStateDumpInfo = {MZD_STATE_DUMP.devStuct}")
    logging.debug(f"pStateDumpInfo = {MZD_STATE_DUMP.coreTemperature}")
    logging.debug(f"pStateDumpInfo = {MZD_STATE_DUMP.cntlPCSReg}")
    logging.debug(f"pStateDumpInfo = {MZD_STATE_DUMP.modeSelectReg}")
    logging.debug(f"pStateDumpInfo = {MZD_STATE_DUMP.ffe}")
    logging.debug(f"pStateDumpInfo = {MZD_STATE_DUMP.txFFE}")
    logging.info("\n")

    logging.info("Function name : mzdSetRsFecControl")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    bypassIndicationEnable = 1
    bypassCorrectionEnable = 1
    try:
        mzdSetRsFecControl(pDev, mdioPort, host_or_line, laneOffset, bypassIndicationEnable, bypassCorrectionEnable)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"bypassIndicationEnable = {bypassIndicationEnable}")
    logging.debug(f"bypassCorrectionEnable = {bypassCorrectionEnable}")
    logging.info("\n")

    logging.info("Function name : mzdGetRsFecControl")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    bypassIndicationEnable = 1
    bypassIndicationEnable_p = c_uint16(bypassIndicationEnable)
    bypassCorrectionEnable = 1
    bypassCorrectionEnable_p = c_uint16(bypassCorrectionEnable)
    try:
        mzdGetRsFecControl(pDev, mdioPort, host_or_line, laneOffset, bypassIndicationEnable_p, bypassCorrectionEnable_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"bypassIndicationEnable = {bypassIndicationEnable_p.value}")
    logging.debug(f"bypassCorrectionEnable = {bypassCorrectionEnable_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdGetRsFecStatus")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    pcsLaneAlignment = 1
    pcsLaneAlignment_p = c_uint16(pcsLaneAlignment)
    fecLaneAlignment = 1
    fecLaneAlignment_p = c_uint16(fecLaneAlignment)
    rsFecLaneAMLock = 1
    rsFecLaneAMLock_p = c_uint16(rsFecLaneAMLock)
    latchedRsFecHighErr = 1
    latchedRsFecHighErr_p = c_uint16(latchedRsFecHighErr)
    currRsFecHighErr = 1
    currRsFecHighErr_p = c_uint16(currRsFecHighErr)
    try:
        mzdGetRsFecStatus(pDev, mdioPort, host_or_line, laneOffset, pcsLaneAlignment_p, fecLaneAlignment_p, rsFecLaneAMLock_p, latchedRsFecHighErr_p, currRsFecHighErr_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"pcsLaneAlignment = {pcsLaneAlignment_p.value}")
    logging.debug(f"fecLaneAlignment = {fecLaneAlignment_p.value}")
    logging.debug(f"rsFecLaneAMLock = {rsFecLaneAMLock_p.value}")
    logging.debug(f"latchedRsFecHighErr = {latchedRsFecHighErr_p.value}")
    logging.debug(f"currRsFecHighErr = {currRsFecHighErr_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdGetRsFecPCSAlignmentStatus")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    pcs_lane = 1
    blockLocked = 1
    blockLocked_p = c_uint16(blockLocked)
    laneAligned = 1
    laneAligned_p = c_uint16(laneAligned)
    try:
        mzdGetRsFecPCSAlignmentStatus(pDev, mdioPort, host_or_line, laneOffset, pcs_lane, blockLocked_p, laneAligned_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"pcs_lane = {pcs_lane}")
    logging.debug(f"blockLocked = {blockLocked_p.value}")
    logging.debug(f"laneAligned = {laneAligned_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdGetRsFecPMALaneMapping")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    mappingMZD_NUM_LANES = 1
    mappingMZD_NUM_LANES_p = c_uint16(mappingMZD_NUM_LANES)
    try:
        mzdGetRsFecPMALaneMapping(pDev, mdioPort, host_or_line, laneOffset, mappingMZD_NUM_LANES_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"mappingMZD_NUM_LANES = {mappingMZD_NUM_LANES_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdGetRxPCSLaneMapping")
    mdioPort = 1
    host_or_line = 1
    lane_offset = 1
    interface_lane = 1
    pcs_lane = 1
    pcs_lane_p = c_uint16(pcs_lane)
    try:
        mzdGetRxPCSLaneMapping(pDev, mdioPort, host_or_line, lane_offset, interface_lane, pcs_lane_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"lane_offset = {lane_offset}")
    logging.debug(f"interface_lane = {interface_lane}")
    logging.debug(f"pcs_lane = {pcs_lane_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdGetRsFecCorrectedCwCntr")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    codeWordCounter = 1
    codeWordCounter_p = c_uint32(codeWordCounter)
    try:
        mzdGetRsFecCorrectedCwCntr(pDev, mdioPort, host_or_line, laneOffset, codeWordCounter_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"codeWordCounter = {codeWordCounter_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdGetRsFecUnCorrectedCwCntr")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    codeWordCounter = 1
    codeWordCounter_p = c_uint32(codeWordCounter)
    try:
        mzdGetRsFecUnCorrectedCwCntr(pDev, mdioPort, host_or_line, laneOffset, codeWordCounter_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"codeWordCounter = {codeWordCounter_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdGetRsFecSymbolErrorCntr")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    fecLane = 1
    errorCounter = 1
    errorCounter_p = c_uint32(errorCounter)
    try:
        mzdGetRsFecSymbolErrorCntr(pDev, mdioPort, host_or_line, laneOffset, fecLane, errorCounter_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"fecLane = {fecLane}")
    logging.debug(f"errorCounter = {errorCounter_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdGetRxPcsBipErrorCntr")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    pcs_lane = 1
    errorCounter = 1
    errorCounter_p = c_uint16(errorCounter)
    try:
        mzdGetRxPcsBipErrorCntr(pDev, mdioPort, host_or_line, laneOffset, pcs_lane, errorCounter_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"pcs_lane = {pcs_lane}")
    logging.debug(f"errorCounter = {errorCounter_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdSetRsFecSERControl")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    degradedSEREnable = 1
    bypassIndicationEnable = 1
    try:
        mzdSetRsFecSERControl(pDev, mdioPort, host_or_line, laneOffset, degradedSEREnable, bypassIndicationEnable)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"degradedSEREnable = {degradedSEREnable}")
    logging.debug(f"bypassIndicationEnable = {bypassIndicationEnable}")
    logging.info("\n")

    logging.info("Function name : mzdGetRsFecSERControl")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    degradedSEREnable = 1
    degradedSEREnable_p = c_uint16(degradedSEREnable)
    bypassIndicationEnable = 1
    bypassIndicationEnable_p = c_uint16(bypassIndicationEnable)
    try:
        mzdGetRsFecSERControl(pDev, mdioPort, host_or_line, laneOffset, degradedSEREnable_p, bypassIndicationEnable_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"degradedSEREnable = {degradedSEREnable_p.value}")
    logging.debug(f"bypassIndicationEnable = {bypassIndicationEnable_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdSetRsFecSERThresholds")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    serActivateThreshold = 1
    serDeactivateThreshold = 1
    serInterval = 1
    try:
        mzdSetRsFecSERThresholds(pDev, mdioPort, host_or_line, laneOffset, serActivateThreshold, serDeactivateThreshold, serInterval)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"serActivateThreshold = {serActivateThreshold}")
    logging.debug(f"serDeactivateThreshold = {serDeactivateThreshold}")
    logging.debug(f"serInterval = {serInterval}")
    logging.info("\n")

    logging.info("Function name : mzdGetRsFecSERThresholds")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    serActivateThreshold = 1
    serActivateThreshold_p = c_uint32(serActivateThreshold)
    serDeactivateThreshold = 1
    serDeactivateThreshold_p = c_uint32(serDeactivateThreshold)
    serInterval = 1
    serInterval_p = c_uint32(serInterval)
    try:
        mzdGetRsFecSERThresholds(pDev, mdioPort, host_or_line, laneOffset, serActivateThreshold_p, serDeactivateThreshold_p, serInterval_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"serActivateThreshold = {serActivateThreshold_p.value}")
    logging.debug(f"serDeactivateThreshold = {serDeactivateThreshold_p.value}")
    logging.debug(f"serInterval = {serInterval_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdGetRsFecDegradedSERStatus")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    localDegradedSerRcvd = 1
    localDegradedSerRcvd_p = c_uint16(localDegradedSerRcvd)
    remoteDegradedSerRcvd = 1
    remoteDegradedSerRcvd_p = c_uint16(remoteDegradedSerRcvd)
    serDegraded = 1
    serDegraded_p = c_uint16(serDegraded)
    try:
        mzdGetRsFecDegradedSERStatus(pDev, mdioPort, host_or_line, laneOffset, localDegradedSerRcvd_p, remoteDegradedSerRcvd_p, serDegraded_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"localDegradedSerRcvd = {localDegradedSerRcvd_p.value}")
    logging.debug(f"remoteDegradedSerRcvd = {remoteDegradedSerRcvd_p.value}")
    logging.debug(f"serDegraded = {serDegraded_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdSetKrFecControl")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    bypassIndicationEnable = 1
    try:
        mzdSetKrFecControl(pDev, mdioPort, host_or_line, laneOffset, bypassIndicationEnable)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"bypassIndicationEnable = {bypassIndicationEnable}")
    logging.info("\n")

    logging.info("Function name : mzdGetKrFecControl")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    bypassIndicationEnable = 1
    bypassIndicationEnable_p = c_uint16(bypassIndicationEnable)
    try:
        mzdGetKrFecControl(pDev, mdioPort, host_or_line, laneOffset, bypassIndicationEnable_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"bypassIndicationEnable = {bypassIndicationEnable_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdGetKrFecAbility")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    krFecAbility = 1
    krFecAbility_p = c_uint16(krFecAbility)
    errIndicationAbility = 1
    errIndicationAbility_p = c_uint16(errIndicationAbility)
    try:
        mzdGetKrFecAbility(pDev, mdioPort, host_or_line, laneOffset, krFecAbility_p, errIndicationAbility_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"krFecAbility = {krFecAbility_p.value}")
    logging.debug(f"errIndicationAbility = {errIndicationAbility_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdGetKrFecCorrectedBlkCntr")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    blockCounter = 1
    blockCounter_p = c_uint32(blockCounter)
    try:
        mzdGetKrFecCorrectedBlkCntr(pDev, mdioPort, host_or_line, laneOffset, blockCounter_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"blockCounter = {blockCounter_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdGetKrFecUnCorrectedBlkCntr")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    blockCounter = 1
    blockCounter_p = c_uint32(blockCounter)
    try:
        mzdGetKrFecUnCorrectedBlkCntr(pDev, mdioPort, host_or_line, laneOffset, blockCounter_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"blockCounter = {blockCounter_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdFECCounterEnable")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    enable = 1
    readToClear = MZD_BOOL.MZD_FALSE.value
    try:
        mzdFECCounterEnable(pDev, mdioPort, host_or_line, laneOffset, enable, readToClear)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"enable = {enable}")
    logging.debug(f"readToClear = {readToClear}")
    logging.info("\n")

    logging.info("Function name : mzdFECCounterSnapshot")
    mdioPort = 1
    host_or_line = 1
    try:
        mzdFECCounterSnapshot(pDev, mdioPort, host_or_line)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.info("\n")

    logging.info("Function name : mzdFECCounterReset")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    try:
        mzdFECCounterReset(pDev, mdioPort, host_or_line, laneOffset)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.info("\n")

    logging.info("Function name : mzdFECReadCodewordCounters")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    numCodeWords = 1
    numCodeWords_p = c_uint64(numCodeWords)
    numUncorrectable = 1
    numUncorrectable_p = c_uint32(numUncorrectable)
    numCorrected = 1
    numCorrected_p = c_uint32(numCorrected)
    try:
        mzdFECReadCodewordCounters(pDev, mdioPort, host_or_line, laneOffset, numCodeWords_p, numUncorrectable_p, numCorrected_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"numCodeWords = {numCodeWords_p.value}")
    logging.debug(f"numUncorrectable = {numUncorrectable_p.value}")
    logging.debug(f"numCorrected = {numCorrected_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdFECReadBurstSymbolErrorCtrs")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    burst2Symbols = 1
    burst2Symbols_p = c_uint32(burst2Symbols)
    burst3Symbols = 1
    burst3Symbols_p = c_uint16(burst3Symbols)
    burst4Symbols = 1
    burst4Symbols_p = c_uint16(burst4Symbols)
    burst5Symbols = 1
    burst5Symbols_p = c_uint16(burst5Symbols)
    burst6Symbols = 1
    burst6Symbols_p = c_uint16(burst6Symbols)
    try:
        mzdFECReadBurstSymbolErrorCtrs(pDev, mdioPort, host_or_line, laneOffset, burst2Symbols_p, burst3Symbols_p, burst4Symbols_p, burst5Symbols_p, burst6Symbols_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"burst2Symbols = {burst2Symbols_p.value}")
    logging.debug(f"burst3Symbols = {burst3Symbols_p.value}")
    logging.debug(f"burst4Symbols = {burst4Symbols_p.value}")
    logging.debug(f"burst5Symbols = {burst5Symbols_p.value}")
    logging.debug(f"burst6Symbols = {burst6Symbols_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdFECReadSymbolErrorCounters")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    symbolErrorCounters0to1 = 1
    symbolErrorCounters0to1_p = c_uint64(symbolErrorCounters0to1)
    symbolErrorCounters2to4 = 1
    symbolErrorCounters2to4_p = c_uint32(symbolErrorCounters2to4)
    symbolErrorCounters5to15 = 1
    symbolErrorCounters5to15_p = c_uint16(symbolErrorCounters5to15)
    try:
        mzdFECReadSymbolErrorCounters(pDev, mdioPort, host_or_line, laneOffset, symbolErrorCounters0to1_p, symbolErrorCounters2to4_p, symbolErrorCounters5to15_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"symbolErrorCounters0to1 = {symbolErrorCounters0to1_p.value}")
    logging.debug(f"symbolErrorCounters2to4 = {symbolErrorCounters2to4_p.value}")
    logging.debug(f"symbolErrorCounters5to15 = {symbolErrorCounters5to15_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdFirmwareDownload")
    fwImageData = 1
    fwImageData_p = c_uint8(fwImageData)
    fwImageSize = 1
    errCode = 1
    errCode_p = c_uint16(errCode)
    try:
        mzdFirmwareDownload(pDev, fwImageData_p, fwImageSize, errCode_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"fwImageData = {fwImageData_p.value}")
    logging.debug(f"fwImageSize = {fwImageSize}")
    logging.debug(f"errCode = {errCode_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdUpdateFlashImage")
    fwImageData = 1
    fwImageData_p = c_uint8(fwImageData)
    fwImageSize = 1
    slaveData = 1
    slaveData_p = c_uint8(slaveData)
    slaveSize = 1
    errCode = 1
    errCode_p = c_uint16(errCode)
    try:
        mzdUpdateFlashImage(pDev, fwImageData_p, fwImageSize, slaveData_p, slaveSize, errCode_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"fwImageData = {fwImageData_p.value}")
    logging.debug(f"fwImageSize = {fwImageSize}")
    logging.debug(f"slaveData = {slaveData_p.value}")
    logging.debug(f"slaveSize = {slaveSize}")
    logging.debug(f"errCode = {errCode_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdParallelFirmwareDownload")
    numPorts = 1
    fwImageData = 1
    fwImageData_p = c_uint8(fwImageData)
    fwImageSize = 1
    errCode = 1
    errCode_p = c_uint16(errCode)
    try:
        mzdParallelFirmwareDownload(pDev, numPorts, fwImageData_p, fwImageSize, pErrDev, errCode_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"numPorts = {numPorts}")
    logging.debug(f"fwImageData = {fwImageData_p.value}")
    logging.debug(f"fwImageSize = {fwImageSize}")
    logging.debug(f"errCode = {errCode_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdParallelUpdateFlashImage")
    numPorts = 1
    fwImageData = 1
    fwImageData_p = c_uint8(fwImageData)
    fwImageSize = 1
    slaveData = 1
    slaveData_p = c_uint8(slaveData)
    slaveSize = 1
    errCode = 1
    errCode_p = c_uint16(errCode)
    try:
        mzdParallelUpdateFlashImage(pDev, numPorts, fwImageData_p, fwImageSize, slaveData_p, slaveSize, pErrDev, errCode_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"numPorts = {numPorts}")
    logging.debug(f"fwImageData = {fwImageData_p.value}")
    logging.debug(f"fwImageSize = {fwImageSize}")
    logging.debug(f"slaveData = {slaveData_p.value}")
    logging.debug(f"slaveSize = {slaveSize}")
    logging.debug(f"errCode = {errCode_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdLoadFlashImageToRAM")
    errCode = 1
    errCode_p = c_uint16(errCode)
    try:
        mzdLoadFlashImageToRAM(pDev, errCode_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"errCode = {errCode_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdHwAPBusRead")
    regAPBAddr = 1
    data = 1
    data_p = c_uint32(data)
    try:
        mzdHwAPBusRead(pDev, regAPBAddr, data_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"regAPBAddr = {regAPBAddr}")
    logging.debug(f"data = {data_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdHwAPBusWrite")
    regAPBAddr = 1
    data = 1
    try:
        mzdHwAPBusWrite(pDev, regAPBAddr, data)
    except Exception:
        traceback.print_exc()
    logging.debug(f"regAPBAddr = {regAPBAddr}")
    logging.debug(f"data = {data}")
    logging.info("\n")

    logging.info("Function name : mzdHwAPBusWriteBlock")
    regAPBAddr = 1
    data = 1
    data_p = c_uint32(data)
    size = 1
    try:
        mzdHwAPBusWriteBlock(pDev, regAPBAddr, data_p, size)
    except Exception:
        traceback.print_exc()
    logging.debug(f"regAPBAddr = {regAPBAddr}")
    logging.debug(f"data = {data_p.value}")
    logging.debug(f"size = {size}")
    logging.info("\n")

    logging.info("Function name : mzdHwAPBusReadBlock")
    regAPBAddr = 1
    size = 1
    data = 1
    data_p = c_uint32(data)
    try:
        mzdHwAPBusReadBlock(pDev, regAPBAddr, size, data_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"regAPBAddr = {regAPBAddr}")
    logging.debug(f"size = {size}")
    logging.debug(f"data = {data_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdHwAPBusSetRegField")
    regAPBAddr = 1
    fieldOffset = 1
    fieldLength = 1
    data = 1
    try:
        mzdHwAPBusSetRegField(pDev, regAPBAddr, fieldOffset, fieldLength, data)
    except Exception:
        traceback.print_exc()
    logging.debug(f"regAPBAddr = {regAPBAddr}")
    logging.debug(f"fieldOffset = {fieldOffset}")
    logging.debug(f"fieldLength = {fieldLength}")
    logging.debug(f"data = {data}")
    logging.info("\n")

    logging.info("Function name : mzdHwAPBusGetRegField")
    regAPBAddr = 1
    fieldOffset = 1
    fieldLength = 1
    data = 1
    data_p = c_uint32(data)
    try:
        mzdHwAPBusGetRegField(pDev, regAPBAddr, fieldOffset, fieldLength, data_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"regAPBAddr = {regAPBAddr}")
    logging.debug(f"fieldOffset = {fieldOffset}")
    logging.debug(f"fieldLength = {fieldLength}")
    logging.debug(f"data = {data_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdHwLockAPBSemaphore")
    semOption = 1
    try:
        mzdHwLockAPBSemaphore(pDev, semOption)
    except Exception:
        traceback.print_exc()
    logging.debug(f"semOption = {semOption}")
    logging.info("\n")

    logging.info("Function name : mzdHwReleaseAPBSemaphore")
    semOption = 1
    try:
        mzdHwReleaseAPBSemaphore(pDev, semOption)
    except Exception:
        traceback.print_exc()
    logging.debug(f"semOption = {semOption}")
    logging.info("\n")

    logging.info("Function name : mzdHwAPBSemaphoreConfig")
    semConfigOption = 1
    try:
        mzdHwAPBSemaphoreConfig(pDev, semConfigOption)
    except Exception:
        traceback.print_exc()
    logging.debug(f"semConfigOption = {semConfigOption}")
    logging.info("\n")

    logging.info("Function name : mzdHwXmdioWrite")
    mdioPort = 1
    dev = 1
    reg = 1
    value = 1
    try:
        mzdHwXmdioWrite(pDev, mdioPort, dev, reg, value)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"dev = {dev}")
    logging.debug(f"reg = {reg}")
    logging.debug(f"value = {value}")
    logging.info("\n")

    logging.info("Function name : mzdHwXmdioRead")
    mdioPort = 1
    dev = 1
    reg = 1
    data = 1
    data_p = c_uint16(data)
    try:
        mzdHwXmdioRead(pDev, mdioPort, dev, reg, data_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"dev = {dev}")
    logging.debug(f"reg = {reg}")
    logging.debug(f"data = {data_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdHwGetPhyRegField")
    mdioPort = 1
    dev = 1
    regAddr = 1
    fieldOffset = 1
    fieldLength = 1
    data = 1
    data_p = c_uint16(data)
    try:
        mzdHwGetPhyRegField(pDev, mdioPort, dev, regAddr, fieldOffset, fieldLength, data_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"dev = {dev}")
    logging.debug(f"regAddr = {regAddr}")
    logging.debug(f"fieldOffset = {fieldOffset}")
    logging.debug(f"fieldLength = {fieldLength}")
    logging.debug(f"data = {data_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdHwSetPhyRegField")
    mdioPort = 1
    dev = 1
    regAddr = 1
    fieldOffset = 1
    fieldLength = 1
    data = 1
    try:
        mzdHwSetPhyRegField(pDev, mdioPort, dev, regAddr, fieldOffset, fieldLength, data)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"dev = {dev}")
    logging.debug(f"regAddr = {regAddr}")
    logging.debug(f"fieldOffset = {fieldOffset}")
    logging.debug(f"fieldLength = {fieldLength}")
    logging.debug(f"data = {data}")
    logging.info("\n")

    logging.info("Function name : mzdHwGetRegFieldFromWord")
    regData = 1
    fieldOffset = 1
    fieldLength = 1
    data = 1
    data_p = c_uint16(data)
    try:
        mzdHwGetRegFieldFromWord(regData, fieldOffset, fieldLength, data_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"regData = {regData}")
    logging.debug(f"fieldOffset = {fieldOffset}")
    logging.debug(f"fieldLength = {fieldLength}")
    logging.debug(f"data = {data_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdHwSetRegFieldToWord")
    regData = 1
    bitFieldData = 1
    fieldOffset = 1
    fieldLength = 1
    data = 1
    data_p = c_uint16(data)
    try:
        mzdHwSetRegFieldToWord(regData, bitFieldData, fieldOffset, fieldLength, data_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"regData = {regData}")
    logging.debug(f"bitFieldData = {bitFieldData}")
    logging.debug(f"fieldOffset = {fieldOffset}")
    logging.debug(f"fieldLength = {fieldLength}")
    logging.debug(f"data = {data_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdHwWaitForRegFieldValue")
    mdioPort = 1
    dev = 1
    regAddr = 1
    fieldOffset = 1
    fieldLength = 1
    expectedValue = 1
    timeoutMs = 1
    try:
        mzdHwWaitForRegFieldValue(pDev, mdioPort, dev, regAddr, fieldOffset, fieldLength, expectedValue, timeoutMs)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"dev = {dev}")
    logging.debug(f"regAddr = {regAddr}")
    logging.debug(f"fieldOffset = {fieldOffset}")
    logging.debug(f"fieldLength = {fieldLength}")
    logging.debug(f"expectedValue = {expectedValue}")
    logging.debug(f"timeoutMs = {timeoutMs}")
    logging.info("\n")

    logging.info("Function name : mzdHwWaitForRegFieldValueList")
    mdioPort = 1
    dev = 1
    regAddr = 1
    fieldOffset = 1
    fieldLength = 1
    expectedValueList = 1
    expectedValueList_p = c_uint16(expectedValueList)
    numOfExpValue = 1
    timeoutMs = 1
    fieldValue = 1
    fieldValue_p = c_uint16(fieldValue)
    try:
        mzdHwWaitForRegFieldValueList(pDev, mdioPort, dev, regAddr, fieldOffset, fieldLength, expectedValueList_p, numOfExpValue, timeoutMs, fieldValue_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"dev = {dev}")
    logging.debug(f"regAddr = {regAddr}")
    logging.debug(f"fieldOffset = {fieldOffset}")
    logging.debug(f"fieldLength = {fieldLength}")
    logging.debug(f"expectedValueList = {expectedValueList_p.value}")
    logging.debug(f"numOfExpValue = {numOfExpValue}")
    logging.debug(f"timeoutMs = {timeoutMs}")
    logging.debug(f"fieldValue = {fieldValue_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdHwXmdioBlockWrite")
    mdioPort = 1
    dev = 1
    reg = 1
    data = 1
    data_p = c_uint8(data)
    dataSize = 1
    try:
        mzdHwXmdioBlockWrite(pDev, mdioPort, dev, reg, data_p, dataSize)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"dev = {dev}")
    logging.debug(f"reg = {reg}")
    logging.debug(f"data = {data_p.value}")
    logging.debug(f"dataSize = {dataSize}")
    logging.info("\n")

    logging.info("Function name : mzdWait")
    waitTime = 1
    try:
        mzdWait(pDev, waitTime)
    except Exception:
        traceback.print_exc()
    logging.debug(f"waitTime = {waitTime}")
    logging.info("\n")

    logging.info("Function name : mzdMacSecMappedDevAddr")
    deviceId = 1
    deviceNum = 1
    firstOffset = 1
    lastOffset = 1
    platfromFirstOffset = 1
    platfromFirstOffset_p = c_uint32(platfromFirstOffset)
    platfromLastOffset = 1
    platfromLastOffset_p = c_uint32(platfromLastOffset)
    try:
        mzdMacSecMappedDevAddr(deviceId, deviceNum, firstOffset, lastOffset, HostContext, platfromFirstOffset_p, platfromLastOffset_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"deviceId = {deviceId}")
    logging.debug(f"deviceNum = {deviceNum}")
    logging.debug(f"firstOffset = {firstOffset}")
    logging.debug(f"lastOffset = {lastOffset}")
    logging.debug(f"platfromFirstOffset = {platfromFirstOffset_p.value}")
    logging.debug(f"platfromLastOffset = {platfromLastOffset_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdSetMacSecDevInfo")
    macsecMapPort = 1
    macsecLane = 1
    try:
        mzdSetMacSecDevInfo(pDev, macsecMapPort, macsecLane)
    except Exception:
        traceback.print_exc()
    logging.debug(f"macsecMapPort = {macsecMapPort}")
    logging.debug(f"macsecLane = {macsecLane}")
    logging.info("\n")

    logging.info("Function name : mzdHwMacSecRegWrite")
    macsecMapPort = 1
    macsecAddr = 1
    data = 1
    try:
        mzdHwMacSecRegWrite(pDev, macsecMapPort, macsecAddr, data)
    except Exception:
        traceback.print_exc()
    logging.debug(f"macsecMapPort = {macsecMapPort}")
    logging.debug(f"macsecAddr = {macsecAddr}")
    logging.debug(f"data = {data}")
    logging.info("\n")

    logging.info("Function name : mzdHwMacSecRegRead")
    macsecMapPort = 1
    macsecAddr = 1
    data = 1
    data_p = c_uint32(data)
    try:
        mzdHwMacSecRegRead(pDev, macsecMapPort, macsecAddr, data_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"macsecMapPort = {macsecMapPort}")
    logging.debug(f"macsecAddr = {macsecAddr}")
    logging.debug(f"data = {data_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdHwSetMacSecRegField")
    macsecMapPort = 1
    macsecAddr = 1
    fieldOffset = 1
    fieldLength = 1
    data = 1
    try:
        mzdHwSetMacSecRegField(pDev, macsecMapPort, macsecAddr, fieldOffset, fieldLength, data)
    except Exception:
        traceback.print_exc()
    logging.debug(f"macsecMapPort = {macsecMapPort}")
    logging.debug(f"macsecAddr = {macsecAddr}")
    logging.debug(f"fieldOffset = {fieldOffset}")
    logging.debug(f"fieldLength = {fieldLength}")
    logging.debug(f"data = {data}")
    logging.info("\n")

    logging.info("Function name : mzdHwGetMacSecRegField")
    macsecMapPort = 1
    macsecAddr = 1
    fieldOffset = 1
    fieldLength = 1
    data = 1
    data_p = c_uint32(data)
    try:
        mzdHwGetMacSecRegField(pDev, macsecMapPort, macsecAddr, fieldOffset, fieldLength, data_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"macsecMapPort = {macsecMapPort}")
    logging.debug(f"macsecAddr = {macsecAddr}")
    logging.debug(f"fieldOffset = {fieldOffset}")
    logging.debug(f"fieldLength = {fieldLength}")
    logging.debug(f"data = {data_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdHwMacSecSBUFRegWrite")
    macsecMapPort = 1
    macsecAddr = 1
    data = 1
    try:
        mzdHwMacSecSBUFRegWrite(pDev, macsecMapPort, macsecAddr, data)
    except Exception:
        traceback.print_exc()
    logging.debug(f"macsecMapPort = {macsecMapPort}")
    logging.debug(f"macsecAddr = {macsecAddr}")
    logging.debug(f"data = {data}")
    logging.info("\n")

    logging.info("Function name : mzdHwMacSecSBUFRegRead")
    macsecMapPort = 1
    macsecAddr = 1
    data = 1
    data_p = c_uint32(data)
    try:
        mzdHwMacSecSBUFRegRead(pDev, macsecMapPort, macsecAddr, data_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"macsecMapPort = {macsecMapPort}")
    logging.debug(f"macsecAddr = {macsecAddr}")
    logging.debug(f"data = {data_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdHwSetMacSecSBUFRegField")
    macsecMapPort = 1
    macsecAddr = 1
    fieldOffset = 1
    fieldLength = 1
    data = 1
    try:
        mzdHwSetMacSecSBUFRegField(pDev, macsecMapPort, macsecAddr, fieldOffset, fieldLength, data)
    except Exception:
        traceback.print_exc()
    logging.debug(f"macsecMapPort = {macsecMapPort}")
    logging.debug(f"macsecAddr = {macsecAddr}")
    logging.debug(f"fieldOffset = {fieldOffset}")
    logging.debug(f"fieldLength = {fieldLength}")
    logging.debug(f"data = {data}")
    logging.info("\n")

    logging.info("Function name : mzdHwGetMacSecSBUFRegField")
    macsecMapPort = 1
    macsecAddr = 1
    fieldOffset = 1
    fieldLength = 1
    data = 1
    data_p = c_uint32(data)
    try:
        mzdHwGetMacSecSBUFRegField(pDev, macsecMapPort, macsecAddr, fieldOffset, fieldLength, data_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"macsecMapPort = {macsecMapPort}")
    logging.debug(f"macsecAddr = {macsecAddr}")
    logging.debug(f"fieldOffset = {fieldOffset}")
    logging.debug(f"fieldLength = {fieldLength}")
    logging.debug(f"data = {data_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdHwMacRegWrite")
    macMapPort = 1
    host_or_line = 1
    macAddr = 1
    data = 1
    try:
        mzdHwMacRegWrite(pDev, macMapPort, host_or_line, macAddr, data)
    except Exception:
        traceback.print_exc()
    logging.debug(f"macMapPort = {macMapPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"macAddr = {macAddr}")
    logging.debug(f"data = {data}")
    logging.info("\n")

    logging.info("Function name : mzdHwMacRegRead")
    macMapPort = 1
    host_or_line = 1
    macAddr = 1
    data = 1
    data_p = c_uint32(data)
    try:
        mzdHwMacRegRead(pDev, macMapPort, host_or_line, macAddr, data_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"macMapPort = {macMapPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"macAddr = {macAddr}")
    logging.debug(f"data = {data_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdHwSetMacRegField")
    macMapPort = 1
    host_or_line = 1
    macAddr = 1
    fieldOffset = 1
    fieldLength = 1
    data = 1
    try:
        mzdHwSetMacRegField(pDev, macMapPort, host_or_line, macAddr, fieldOffset, fieldLength, data)
    except Exception:
        traceback.print_exc()
    logging.debug(f"macMapPort = {macMapPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"macAddr = {macAddr}")
    logging.debug(f"fieldOffset = {fieldOffset}")
    logging.debug(f"fieldLength = {fieldLength}")
    logging.debug(f"data = {data}")
    logging.info("\n")

    logging.info("Function name : mzdHwGetMacRegField")
    macMapPort = 1
    host_or_line = 1
    macAddr = 1
    fieldOffset = 1
    fieldLength = 1
    data = 1
    data_p = c_uint32(data)
    try:
        mzdHwGetMacRegField(pDev, macMapPort, host_or_line, macAddr, fieldOffset, fieldLength, data_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"macMapPort = {macMapPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"macAddr = {macAddr}")
    logging.debug(f"fieldOffset = {fieldOffset}")
    logging.debug(f"fieldLength = {fieldLength}")
    logging.debug(f"data = {data_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdSetSerdesDevInfo")
    serdesMapPort = 1
    serdesMapHostLine = 1
    try:
        mzdSetSerdesDevInfo(pDev, serdesMapPort, serdesMapHostLine)
    except Exception:
        traceback.print_exc()
    logging.debug(f"serdesMapPort = {serdesMapPort}")
    logging.debug(f"serdesMapHostLine = {serdesMapHostLine}")
    logging.info("\n")

    logging.info("Function name : mzdHwSerdesPhyRegWrite")
    mdioPort = 1
    host_or_line = 1
    serdesLane = 1
    regAddr = 1
    data = 1
    try:
        mzdHwSerdesPhyRegWrite(pDev, mdioPort, host_or_line, serdesLane, regAddr, data)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"serdesLane = {serdesLane}")
    logging.debug(f"regAddr = {regAddr}")
    logging.debug(f"data = {data}")
    logging.info("\n")

    logging.info("Function name : mzdHwSerdesPhyRegRead")
    mdioPort = 1
    host_or_line = 1
    serdesLane = 1
    regAddr = 1
    data = 1
    data_p = c_uint32(data)
    try:
        mzdHwSerdesPhyRegRead(pDev, mdioPort, host_or_line, serdesLane, regAddr, data_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"serdesLane = {serdesLane}")
    logging.debug(f"regAddr = {regAddr}")
    logging.debug(f"data = {data_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdHwSetSerdesPhyRegField")
    mdioPort = 1
    host_or_line = 1
    serdesLane = 1
    regAddr = 1
    fieldOffset = 1
    fieldLength = 1
    data = 1
    try:
        mzdHwSetSerdesPhyRegField(pDev, mdioPort, host_or_line, serdesLane, regAddr, fieldOffset, fieldLength, data)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"serdesLane = {serdesLane}")
    logging.debug(f"regAddr = {regAddr}")
    logging.debug(f"fieldOffset = {fieldOffset}")
    logging.debug(f"fieldLength = {fieldLength}")
    logging.debug(f"data = {data}")
    logging.info("\n")

    logging.info("Function name : mzdHwGetSerdesPhyRegField")
    mdioPort = 1
    host_or_line = 1
    serdesLane = 1
    regAddr = 1
    fieldOffset = 1
    fieldLength = 1
    data = 1
    data_p = c_uint32(data)
    try:
        mzdHwGetSerdesPhyRegField(pDev, mdioPort, host_or_line, serdesLane, regAddr, fieldOffset, fieldLength, data_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"serdesLane = {serdesLane}")
    logging.debug(f"regAddr = {regAddr}")
    logging.debug(f"fieldOffset = {fieldOffset}")
    logging.debug(f"fieldLength = {fieldLength}")
    logging.debug(f"data = {data_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdHwSerdesPhyLaneRegBroadcast")
    mdioPort = 1
    host_or_line = 1
    enable = 1
    try:
        mzdHwSerdesPhyLaneRegBroadcast(pDev, mdioPort, host_or_line, enable)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"enable = {enable}")
    logging.info("\n")

    logging.info("Function name : mzdLanePowerdown")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    try:
        mzdLanePowerdown(pDev, mdioPort, host_or_line, laneOffset)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.info("\n")

    logging.info("Function name : mzdLanePowerup")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    try:
        mzdLanePowerup(pDev, mdioPort, host_or_line, laneOffset)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.info("\n")

    logging.info("Function name : mzdPortReset")
    mdioPort = 1
    host_or_line = 1
    resetType = MZD_RESET_TYPE.MZD_SOFT_RESET.value
    timeoutMs = 1
    try:
        mzdPortReset(pDev, mdioPort, host_or_line, resetType, timeoutMs)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"resetType = {resetType}")
    logging.debug(f"timeoutMs = {timeoutMs}")
    logging.info("\n")

    logging.info("Function name : mzdChipResetControl")
    resetType = 1
    bRestore = MZD_BOOL.MZD_FALSE.value
    try:
        mzdChipResetControl(pDev, resetType, bRestore)
    except Exception:
        traceback.print_exc()
    logging.debug(f"resetType = {resetType}")
    logging.debug(f"bRestore = {bRestore}")
    logging.info("\n")

    logging.info("Function name : mzdGetIntrSrcStatus")
    gpioIntr = (c_int * 9)()
    gpioIntr_init = [0] * 9
    for idx, value in enumerate(gpioIntr_init):
        gpioIntr[idx] = value
    macIntr = (MZD_MAC_CHIP_INTR * 2)()
    macIntr_init = [0] * 2
    for idx, value in enumerate(macIntr_init):
        macIntr[idx] = value
    serdesIntr = (MZD_SERDES_CHIP_INTR * 4)()
    serdesIntr_init = [0] * 4
    for idx, value in enumerate(serdesIntr_init):
        serdesIntr[idx] = value
    pcsIntr = (MZD_PCS_CHIP_INTR * 16)()
    pcsIntr_init = [0] * 16
    for idx, value in enumerate(pcsIntr_init):
        pcsIntr[idx] = value
    intrSelector = MZD_GLOBAL_CHIP_INTR(0, 0, 0, gpioIntr, macIntr, serdesIntr, pcsIntr)
    forceInterrupt = MZD_BOOL.MZD_FALSE.value
    forceInterrupt_p = MZD_BOOL(forceInterrupt)
    gpioIntr = (c_int * 9)()
    gpioIntr_init = [0] * 9
    for idx, value in enumerate(gpioIntr_init):
        gpioIntr[idx] = value
    macIntr = (MZD_MAC_CHIP_INTR * 2)()
    macIntr_init = [0] * 2
    for idx, value in enumerate(macIntr_init):
        macIntr[idx] = value
    serdesIntr = (MZD_SERDES_CHIP_INTR * 4)()
    serdesIntr_init = [0] * 4
    for idx, value in enumerate(serdesIntr_init):
        serdesIntr[idx] = value
    pcsIntr = (MZD_PCS_CHIP_INTR * 16)()
    pcsIntr_init = [0] * 16
    for idx, value in enumerate(pcsIntr_init):
        pcsIntr[idx] = value
    intrSrc = MZD_GLOBAL_CHIP_INTR(0, 0, 0, gpioIntr, macIntr, serdesIntr, pcsIntr)
    intrSrc_p = byref(intrSrc)
    try:
        mzdGetIntrSrcStatus(pDev, intrSelector, forceInterrupt_p, intrSrc_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"intrSelector = {MZD_GLOBAL_CHIP_INTR.globalAggregatedIntr1}")
    logging.debug(f"intrSelector = {MZD_GLOBAL_CHIP_INTR.globalAggregatedIntr2}")
    logging.debug(f"intrSelector = {MZD_GLOBAL_CHIP_INTR.onChipProcIntr}")
    logging.debug(f"forceInterrupt = {forceInterrupt_p.value}")
    logging.debug(f"intrSrc = {MZD_GLOBAL_CHIP_INTR.globalAggregatedIntr1}")
    logging.debug(f"intrSrc = {MZD_GLOBAL_CHIP_INTR.globalAggregatedIntr2}")
    logging.debug(f"intrSrc = {MZD_GLOBAL_CHIP_INTR.onChipProcIntr}")
    logging.info("\n")

    logging.info("Function name : mzdSetGlobalInterruptCntl")
    openDrain = MZD_BOOL.MZD_FALSE.value
    intrPolarity = 1
    forceInterrupt = MZD_BOOL.MZD_FALSE.value
    try:
        mzdSetGlobalInterruptCntl(pDev, openDrain, intrPolarity, forceInterrupt)
    except Exception:
        traceback.print_exc()
    logging.debug(f"openDrain = {openDrain}")
    logging.debug(f"intrPolarity = {intrPolarity}")
    logging.debug(f"forceInterrupt = {forceInterrupt}")
    logging.info("\n")

    logging.info("Function name : mzdGetGlobalInterruptCntl")
    openDrain = MZD_BOOL.MZD_FALSE.value
    openDrain_p = MZD_BOOL(openDrain)
    intrPolarity = 1
    intrPolarity_p = c_uint16(intrPolarity)
    forceInterrupt = MZD_BOOL.MZD_FALSE.value
    forceInterrupt_p = MZD_BOOL(forceInterrupt)
    try:
        mzdGetGlobalInterruptCntl(pDev, openDrain_p, intrPolarity_p, forceInterrupt_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"openDrain = {openDrain_p.value}")
    logging.debug(f"intrPolarity = {intrPolarity_p.value}")
    logging.debug(f"forceInterrupt = {forceInterrupt_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdSetGlobalInterruptEnable")
    globalAggregatedIntrEnable1 = 1
    globalAggregatedIntrEnable2 = 1
    try:
        mzdSetGlobalInterruptEnable(pDev, globalAggregatedIntrEnable1, globalAggregatedIntrEnable2)
    except Exception:
        traceback.print_exc()
    logging.debug(f"globalAggregatedIntrEnable1 = {globalAggregatedIntrEnable1}")
    logging.debug(f"globalAggregatedIntrEnable2 = {globalAggregatedIntrEnable2}")
    logging.info("\n")

    logging.info("Function name : mzdGetGlobalInterruptEnable")
    globalAggregatedIntrEnable1 = 1
    globalAggregatedIntrEnable1_p = c_uint16(globalAggregatedIntrEnable1)
    globalAggregatedIntrEnable2 = 1
    globalAggregatedIntrEnable2_p = c_uint16(globalAggregatedIntrEnable2)
    try:
        mzdGetGlobalInterruptEnable(pDev, globalAggregatedIntrEnable1_p, globalAggregatedIntrEnable2_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"globalAggregatedIntrEnable1 = {globalAggregatedIntrEnable1_p.value}")
    logging.debug(f"globalAggregatedIntrEnable2 = {globalAggregatedIntrEnable2_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdGetUnmaskedInterrupts")
    gpioIntr = (c_int * 9)()
    gpioIntr_init = [0] * 9
    for idx, value in enumerate(gpioIntr_init):
        gpioIntr[idx] = value
    macIntr = (MZD_MAC_CHIP_INTR * 2)()
    macIntr_init = [0] * 2
    for idx, value in enumerate(macIntr_init):
        macIntr[idx] = value
    serdesIntr = (MZD_SERDES_CHIP_INTR * 4)()
    serdesIntr_init = [0] * 4
    for idx, value in enumerate(serdesIntr_init):
        serdesIntr[idx] = value
    pcsIntr = (MZD_PCS_CHIP_INTR * 16)()
    pcsIntr_init = [0] * 16
    for idx, value in enumerate(pcsIntr_init):
        pcsIntr[idx] = value
    intrSelector = MZD_GLOBAL_CHIP_INTR(0, 0, 0, gpioIntr, macIntr, serdesIntr, pcsIntr)
    intrSelector_p = byref(intrSelector)
    try:
        mzdGetUnmaskedInterrupts(pDev, intrSelector_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"intrSelector = {MZD_GLOBAL_CHIP_INTR.globalAggregatedIntr1}")
    logging.debug(f"intrSelector = {MZD_GLOBAL_CHIP_INTR.globalAggregatedIntr2}")
    logging.debug(f"intrSelector = {MZD_GLOBAL_CHIP_INTR.onChipProcIntr}")
    logging.info("\n")

    logging.info("Function name : mzdSetGPIOInterruptEnable")
    gpioPinId = MZD_PIN_ID.MZD_PIN_GPIO1.value
    gpioIntrEnable = 1
    try:
        mzdSetGPIOInterruptEnable(pDev, gpioPinId, gpioIntrEnable)
    except Exception:
        traceback.print_exc()
    logging.debug(f"gpioPinId = {gpioPinId}")
    logging.debug(f"gpioIntrEnable = {gpioIntrEnable}")
    logging.info("\n")

    logging.info("Function name : mzdGetGPIOInterruptEnable")
    gpioPinId = MZD_PIN_ID.MZD_PIN_GPIO1.value
    gpioIntrEnable = 1
    gpioIntrEnable_p = c_uint16(gpioIntrEnable)
    try:
        mzdGetGPIOInterruptEnable(pDev, gpioPinId, gpioIntrEnable_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"gpioPinId = {gpioPinId}")
    logging.debug(f"gpioIntrEnable = {gpioIntrEnable_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdSetGPIOInterruptType")
    gpioPinId = MZD_PIN_ID.MZD_PIN_GPIO1.value
    gpioIntrType = 1
    try:
        mzdSetGPIOInterruptType(pDev, gpioPinId, gpioIntrType)
    except Exception:
        traceback.print_exc()
    logging.debug(f"gpioPinId = {gpioPinId}")
    logging.debug(f"gpioIntrType = {gpioIntrType}")
    logging.info("\n")

    logging.info("Function name : mzdGetGPIOInterruptType")
    gpioPinId = MZD_PIN_ID.MZD_PIN_GPIO1.value
    gpioIntrType = 1
    gpioIntrType_p = c_uint16(gpioIntrType)
    try:
        mzdGetGPIOInterruptType(pDev, gpioPinId, gpioIntrType_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"gpioPinId = {gpioPinId}")
    logging.debug(f"gpioIntrType = {gpioIntrType_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdGetGPIOInterruptStatus")
    gpioPinId = MZD_PIN_ID.MZD_PIN_GPIO1.value
    gpioIntrLatchedStatus = 1
    gpioIntrLatchedStatus_p = c_uint16(gpioIntrLatchedStatus)
    gpioIntrCurrentStatus = 1
    gpioIntrCurrentStatus_p = c_uint16(gpioIntrCurrentStatus)
    try:
        mzdGetGPIOInterruptStatus(pDev, gpioPinId, gpioIntrLatchedStatus_p, gpioIntrCurrentStatus_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"gpioPinId = {gpioPinId}")
    logging.debug(f"gpioIntrLatchedStatus = {gpioIntrLatchedStatus_p.value}")
    logging.debug(f"gpioIntrCurrentStatus = {gpioIntrCurrentStatus_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdSetPCSInterruptEnable")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    intrEnable = MZD_PCS_UNIT_INTR(0, 0, 0, 0)
    try:
        mzdSetPCSInterruptEnable(pDev, mdioPort, host_or_line, laneOffset, intrEnable)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"intrEnable = {MZD_PCS_UNIT_INTR.srcFlag1}")
    logging.debug(f"intrEnable = {MZD_PCS_UNIT_INTR.srcFlag2}")
    logging.debug(f"intrEnable = {MZD_PCS_UNIT_INTR.apAutoNeg}")
    logging.debug(f"intrEnable = {MZD_PCS_UNIT_INTR.excessiveLinkErr}")
    logging.info("\n")

    logging.info("Function name : mzdGetPCSInterruptEnable")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    intrEnable = MZD_PCS_UNIT_INTR(0, 0, 0, 0)
    intrEnable_p = byref(intrEnable)
    try:
        mzdGetPCSInterruptEnable(pDev, mdioPort, host_or_line, laneOffset, intrEnable_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"intrEnable = {MZD_PCS_UNIT_INTR.srcFlag1}")
    logging.debug(f"intrEnable = {MZD_PCS_UNIT_INTR.srcFlag2}")
    logging.debug(f"intrEnable = {MZD_PCS_UNIT_INTR.apAutoNeg}")
    logging.debug(f"intrEnable = {MZD_PCS_UNIT_INTR.excessiveLinkErr}")
    logging.info("\n")

    logging.info("Function name : mzdGetPCSInterruptStatus")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    latchedIntrStatus = MZD_PCS_UNIT_INTR(0, 0, 0, 0)
    latchedIntrStatus_p = byref(latchedIntrStatus)
    currentIntrStatus = MZD_PCS_UNIT_INTR(0, 0, 0, 0)
    currentIntrStatus_p = byref(currentIntrStatus)
    try:
        mzdGetPCSInterruptStatus(pDev, mdioPort, host_or_line, laneOffset, latchedIntrStatus_p, currentIntrStatus_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"latchedIntrStatus = {MZD_PCS_UNIT_INTR.srcFlag1}")
    logging.debug(f"latchedIntrStatus = {MZD_PCS_UNIT_INTR.srcFlag2}")
    logging.debug(f"latchedIntrStatus = {MZD_PCS_UNIT_INTR.apAutoNeg}")
    logging.debug(f"latchedIntrStatus = {MZD_PCS_UNIT_INTR.excessiveLinkErr}")
    logging.debug(f"currentIntrStatus = {MZD_PCS_UNIT_INTR.srcFlag1}")
    logging.debug(f"currentIntrStatus = {MZD_PCS_UNIT_INTR.srcFlag2}")
    logging.debug(f"currentIntrStatus = {MZD_PCS_UNIT_INTR.apAutoNeg}")
    logging.debug(f"currentIntrStatus = {MZD_PCS_UNIT_INTR.excessiveLinkErr}")
    logging.info("\n")

    logging.info("Function name : mzdGetPCSRealtimeStatus")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    rtIntrStatus = MZD_PCS_UNIT_INTR(0, 0, 0, 0)
    rtIntrStatus_p = byref(rtIntrStatus)
    try:
        mzdGetPCSRealtimeStatus(pDev, mdioPort, host_or_line, laneOffset, rtIntrStatus_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"rtIntrStatus = {MZD_PCS_UNIT_INTR.srcFlag1}")
    logging.debug(f"rtIntrStatus = {MZD_PCS_UNIT_INTR.srcFlag2}")
    logging.debug(f"rtIntrStatus = {MZD_PCS_UNIT_INTR.apAutoNeg}")
    logging.debug(f"rtIntrStatus = {MZD_PCS_UNIT_INTR.excessiveLinkErr}")
    logging.info("\n")

    logging.info("Function name : mzdSetPinMode")
    pinId = MZD_PIN_ID.MZD_PIN_GPIO1.value
    pinMode = MZD_PIN_MODE.MZD_PIN_MODE_GPIO.value
    openDrain = MZD_BOOL.MZD_FALSE.value
    try:
        mzdSetPinMode(pDev, pinId, pinMode, openDrain)
    except Exception:
        traceback.print_exc()
    logging.debug(f"pinId = {pinId}")
    logging.debug(f"pinMode = {pinMode}")
    logging.debug(f"openDrain = {openDrain}")
    logging.info("\n")

    logging.info("Function name : mzdGetPinMode")
    pinId = MZD_PIN_ID.MZD_PIN_GPIO1.value
    pinMode = MZD_PIN_MODE.MZD_PIN_MODE_GPIO.value
    pinMode_p = MZD_PIN_MODE(pinMode)
    openDrain = MZD_BOOL.MZD_FALSE.value
    openDrain_p = MZD_BOOL(openDrain)
    try:
        mzdGetPinMode(pDev, pinId, pinMode_p, openDrain_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"pinId = {pinId}")
    logging.debug(f"pinMode = {pinMode_p.value}")
    logging.debug(f"openDrain = {openDrain_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdSetGPIOPinDirection")
    gpioPinId = MZD_PIN_ID.MZD_PIN_GPIO1.value
    gpioPinDirection = 1
    try:
        mzdSetGPIOPinDirection(pDev, gpioPinId, gpioPinDirection)
    except Exception:
        traceback.print_exc()
    logging.debug(f"gpioPinId = {gpioPinId}")
    logging.debug(f"gpioPinDirection = {gpioPinDirection}")
    logging.info("\n")

    logging.info("Function name : mzdGetGPIOPinDirection")
    gpioPinId = MZD_PIN_ID.MZD_PIN_GPIO1.value
    gpioPinDirection = 1
    gpioPinDirection_p = c_uint16(gpioPinDirection)
    try:
        mzdGetGPIOPinDirection(pDev, gpioPinId, gpioPinDirection_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"gpioPinId = {gpioPinId}")
    logging.debug(f"gpioPinDirection = {gpioPinDirection_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdSetGPIOPinData")
    gpioPinId = MZD_PIN_ID.MZD_PIN_GPIO1.value
    gpioData = 1
    try:
        mzdSetGPIOPinData(pDev, gpioPinId, gpioData)
    except Exception:
        traceback.print_exc()
    logging.debug(f"gpioPinId = {gpioPinId}")
    logging.debug(f"gpioData = {gpioData}")
    logging.info("\n")

    logging.info("Function name : mzdGetGPIOPinData")
    gpioPinId = MZD_PIN_ID.MZD_PIN_GPIO1.value
    gpioData = 1
    gpioData_p = c_uint16(gpioData)
    try:
        mzdGetGPIOPinData(pDev, gpioPinId, gpioData_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"gpioPinId = {gpioPinId}")
    logging.debug(f"gpioData = {gpioData_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdSetLEDControl")
    ledPinId = MZD_PIN_ID.MZD_PIN_GPIO1.value
    ledCtrl = MZD_LED_CTRL(0, 0, 0, 0, 0, 0, 0, 0)
    try:
        mzdSetLEDControl(pDev, ledPinId, ledCtrl)
    except Exception:
        traceback.print_exc()
    logging.debug(f"ledPinId = {ledPinId}")
    logging.debug(f"ledCtrl = {MZD_LED_CTRL.interfaceSelect}")
    logging.debug(f"ledCtrl = {MZD_LED_CTRL.portSelect}")
    logging.debug(f"ledCtrl = {MZD_LED_CTRL.laneSelect}")
    logging.debug(f"ledCtrl = {MZD_LED_CTRL.blinkActivity}")
    logging.debug(f"ledCtrl = {MZD_LED_CTRL.solidActivity}")
    logging.debug(f"ledCtrl = {MZD_LED_CTRL.polarity}")
    logging.debug(f"ledCtrl = {MZD_LED_CTRL.mixRateLevel}")
    logging.debug(f"ledCtrl = {MZD_LED_CTRL.blinkRateSelect}")
    logging.info("\n")

    logging.info("Function name : mzdSetLEDTimer")
    ledTimerConfig = MZD_LED_TIMER_CONFIG(0, 0, 0)
    try:
        mzdSetLEDTimer(pDev, ledTimerConfig)
    except Exception:
        traceback.print_exc()
    logging.debug(f"ledTimerConfig = {MZD_LED_TIMER_CONFIG.blinkRate1}")
    logging.debug(f"ledTimerConfig = {MZD_LED_TIMER_CONFIG.blinkRate2}")
    logging.debug(f"ledTimerConfig = {MZD_LED_TIMER_CONFIG.pulseStretchDuration}")
    logging.info("\n")

    logging.info("Function name : mzdConfigRClkPin")
    rClkPinId = MZD_PIN_ID.MZD_PIN_GPIO1.value
    portSelect = 1
    interfaceSelect = 1
    laneSelect = 1
    try:
        mzdConfigRClkPin(pDev, rClkPinId, portSelect, interfaceSelect, laneSelect)
    except Exception:
        traceback.print_exc()
    logging.debug(f"rClkPinId = {rClkPinId}")
    logging.debug(f"portSelect = {portSelect}")
    logging.debug(f"interfaceSelect = {interfaceSelect}")
    logging.debug(f"laneSelect = {laneSelect}")
    logging.info("\n")

    logging.info("Function name : mzdConfigRClkSource")
    portSelect = 1
    interfaceSelect = 1
    laneSelect = 1
    clockOption = MZD_RCLK_SRC_OPTION(0, 0, 0, 0)
    try:
        mzdConfigRClkSource(pDev, portSelect, interfaceSelect, laneSelect, clockOption)
    except Exception:
        traceback.print_exc()
    logging.debug(f"portSelect = {portSelect}")
    logging.debug(f"interfaceSelect = {interfaceSelect}")
    logging.debug(f"laneSelect = {laneSelect}")
    logging.debug(f"clockOption = {MZD_RCLK_SRC_OPTION.overWriteSrcClock}")
    logging.debug(f"clockOption = {MZD_RCLK_SRC_OPTION.srcClockSelect}")
    logging.debug(f"clockOption = {MZD_RCLK_SRC_OPTION.dividerConfig}")
    logging.debug(f"clockOption = {MZD_RCLK_SRC_OPTION.divideRatio}")
    logging.info("\n")

    logging.info("Function name : mzdMacSecMacInit")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    opMode = MZD_OP_MODE.MZD_OP_MODE_UNKNOWN.value
    initOption = 1
    try:
        mzdMacSecMacInit(pDev, mdioPort, host_or_line, laneOffset, opMode, initOption)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"opMode = {opMode}")
    logging.debug(f"initOption = {initOption}")
    logging.info("\n")

    logging.info("Function name : mzdMacEnable")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    macEnable = MZD_BOOL.MZD_FALSE.value
    try:
        mzdMacEnable(pDev, mdioPort, host_or_line, laneOffset, macEnable)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"macEnable = {macEnable}")
    logging.info("\n")

    logging.info("Function name : mzdMacSecEnable")
    mdioPort = 1
    host_or_line = 1
    macsecEnable = MZD_BOOL.MZD_FALSE.value
    try:
        mzdMacSecEnable(pDev, mdioPort, host_or_line, macsecEnable)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"macsecEnable = {macsecEnable}")
    logging.info("\n")

    logging.info("Function name : mzdMacSetLowSpeed")
    mdioPort = 1
    laneOffset = 1
    try:
        mzdMacSetLowSpeed(pDev, mdioPort, laneOffset)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.info("\n")

    logging.info("Function name : mzdMacSetHighSpeed")
    mdioPort = 1
    try:
        mzdMacSetHighSpeed(pDev, mdioPort)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.info("\n")

    logging.info("Function name : mzdMacSecPtpBypass")
    mdioPort = 1
    bypassPtp = MZD_BOOL.MZD_FALSE.value
    try:
        mzdMacSecPtpBypass(pDev, mdioPort, bypassPtp)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"bypassPtp = {bypassPtp}")
    logging.info("\n")

    logging.info("Function name : mzdMacSecEgressBypass")
    mdioPort = 1
    laneOffset = 1
    egressBypass = MZD_BOOL.MZD_FALSE.value
    try:
        mzdMacSecEgressBypass(pDev, mdioPort, laneOffset, egressBypass)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"egressBypass = {egressBypass}")
    logging.info("\n")

    logging.info("Function name : mzdMacSecIngressBypass")
    mdioPort = 1
    laneOffset = 1
    ingressBypass = MZD_BOOL.MZD_FALSE.value
    try:
        mzdMacSecIngressBypass(pDev, mdioPort, laneOffset, ingressBypass)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"ingressBypass = {ingressBypass}")
    logging.info("\n")

    logging.info("Function name : mzdMacBypassPPMFifo")
    mdioPort = 1
    bypassPPMFifo = MZD_BOOL.MZD_FALSE.value
    try:
        mzdMacBypassPPMFifo(pDev, mdioPort, bypassPPMFifo)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"bypassPPMFifo = {bypassPPMFifo}")
    logging.info("\n")

    logging.info("Function name : mzdMacBypassPPMFifoPushBackLatencyMatch")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    pushBackLatencyMatch = 1
    try:
        mzdMacBypassPPMFifoPushBackLatencyMatch(pDev, mdioPort, host_or_line, laneOffset, pushBackLatencyMatch)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"pushBackLatencyMatch = {pushBackLatencyMatch}")
    logging.info("\n")

    logging.info("Function name : mzdMacBypassPPMFifoDelayAlignMarkerPushBack")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    pushBackDelay = 1
    try:
        mzdMacBypassPPMFifoDelayAlignMarkerPushBack(pDev, mdioPort, host_or_line, laneOffset, pushBackDelay)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"pushBackDelay = {pushBackDelay}")
    logging.info("\n")

    logging.info("Function name : mzdMacMIBStatDump")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    stateDumpOptions = 1
    try:
        mzdMacMIBStatDump(pDev, mdioPort, host_or_line, laneOffset, stateDumpOptions)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"stateDumpOptions = {stateDumpOptions}")
    logging.info("\n")

    logging.info("Function name : mzdMacPauseFrameInjectionToHost")
    mdioPort = 1
    laneOffset = 1
    enable = 1
    try:
        mzdMacPauseFrameInjectionToHost(pDev, mdioPort, laneOffset, enable)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"enable = {enable}")
    logging.info("\n")

    logging.info("Function name : mzdMacSetPauseFrameToHostThreshold")
    mdioPort = 1
    laneOffset = 1
    lowThreshold = 1
    highThreshold = 1
    try:
        mzdMacSetPauseFrameToHostThreshold(pDev, mdioPort, laneOffset, lowThreshold, highThreshold)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"lowThreshold = {lowThreshold}")
    logging.debug(f"highThreshold = {highThreshold}")
    logging.info("\n")

    logging.info("Function name : mzdMacGetPauseFrameToHostThreshold")
    mdioPort = 1
    laneOffset = 1
    lowThreshold = 1
    lowThreshold_p = c_uint16(lowThreshold)
    highThreshold = 1
    highThreshold_p = c_uint16(highThreshold)
    try:
        mzdMacGetPauseFrameToHostThreshold(pDev, mdioPort, laneOffset, lowThreshold_p, highThreshold_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"lowThreshold = {lowThreshold_p.value}")
    logging.debug(f"highThreshold = {highThreshold_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdMacSecHmux4ArbiterEnable")
    macsecMapPort = 1
    hostSideMode = MZD_OP_MODE.MZD_OP_MODE_UNKNOWN.value
    lowerPortPrimary = MZD_BOOL.MZD_FALSE.value
    hmux4Options = 1
    try:
        mzdMacSecHmux4ArbiterEnable(pDev, macsecMapPort, hostSideMode, lowerPortPrimary, hmux4Options)
    except Exception:
        traceback.print_exc()
    logging.debug(f"macsecMapPort = {macsecMapPort}")
    logging.debug(f"hostSideMode = {hostSideMode}")
    logging.debug(f"lowerPortPrimary = {lowerPortPrimary}")
    logging.debug(f"hmux4Options = {hmux4Options}")
    logging.info("\n")

    logging.info("Function name : mzdMacSecHmux8ArbiterEnable")
    hostSideMode = MZD_OP_MODE.MZD_OP_MODE_UNKNOWN.value
    lowerPortsPrimary = MZD_BOOL.MZD_FALSE.value
    hmux8Options = 1
    try:
        mzdMacSecHmux8ArbiterEnable(pDev, hostSideMode, lowerPortsPrimary, hmux8Options)
    except Exception:
        traceback.print_exc()
    logging.debug(f"hostSideMode = {hostSideMode}")
    logging.debug(f"lowerPortsPrimary = {lowerPortsPrimary}")
    logging.debug(f"hmux8Options = {hmux8Options}")
    logging.info("\n")

    logging.info("Function name : mzdMacSecHmuxArbiterEnablePerLane")
    mdioPort = 1
    laneOffset = 1
    hostSideMode = MZD_OP_MODE.MZD_OP_MODE_UNKNOWN.value
    hmuxType = 1
    try:
        mzdMacSecHmuxArbiterEnablePerLane(pDev, mdioPort, laneOffset, hostSideMode, hmuxType)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"hostSideMode = {hostSideMode}")
    logging.debug(f"hmuxType = {hmuxType}")
    logging.info("\n")

    logging.info("Function name : mzdHmuxArbiterReset")
    mdioPort = 1
    laneOffset = 1
    arbiterSelect = 1
    try:
        mzdHmuxArbiterReset(pDev, mdioPort, laneOffset, arbiterSelect)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"arbiterSelect = {arbiterSelect}")
    logging.info("\n")

    logging.info("Function name : mzdMacSecSelectHmuxType")
    macsecMapPort = 1
    hmuxType = 1
    lowerPortPrimary = MZD_BOOL.MZD_FALSE.value
    hmuxOptions = 1
    try:
        mzdMacSecSelectHmuxType(pDev, macsecMapPort, hmuxType, lowerPortPrimary, hmuxOptions)
    except Exception:
        traceback.print_exc()
    logging.debug(f"macsecMapPort = {macsecMapPort}")
    logging.debug(f"hmuxType = {hmuxType}")
    logging.debug(f"lowerPortPrimary = {lowerPortPrimary}")
    logging.debug(f"hmuxOptions = {hmuxOptions}")
    logging.info("\n")

    logging.info("Function name : mzdMacSecHmuxArbiterState")
    macsecMapPort = 1
    arbiterEgrState = 1
    arbiterEgrState_p = c_uint16(arbiterEgrState)
    arbiterIngrState = 1
    arbiterIngrState_p = c_uint16(arbiterIngrState)
    try:
        mzdMacSecHmuxArbiterState(pDev, macsecMapPort, arbiterEgrState_p, arbiterIngrState_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"macsecMapPort = {macsecMapPort}")
    logging.debug(f"arbiterEgrState = {arbiterEgrState_p.value}")
    logging.debug(f"arbiterIngrState = {arbiterIngrState_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdMacSecHmuxBlockBackUpIngress")
    macsecMapPort = 1
    blockBackUpPorts = MZD_BOOL.MZD_FALSE.value
    try:
        mzdMacSecHmuxBlockBackUpIngress(pDev, macsecMapPort, blockBackUpPorts)
    except Exception:
        traceback.print_exc()
    logging.debug(f"macsecMapPort = {macsecMapPort}")
    logging.debug(f"blockBackUpPorts = {blockBackUpPorts}")
    logging.info("\n")

    logging.info("Function name : mzdMacSecHmuxTimeOut")
    mdioPort = 1
    hmuxTimeOutSel = 1
    hmuxTimeOutSelOptions = 1
    try:
        mzdMacSecHmuxTimeOut(pDev, mdioPort, hmuxTimeOutSel, hmuxTimeOutSelOptions)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"hmuxTimeOutSel = {hmuxTimeOutSel}")
    logging.debug(f"hmuxTimeOutSelOptions = {hmuxTimeOutSelOptions}")
    logging.info("\n")

    logging.info("Function name : mzdMacSecManualHmuxStopTraffic")
    macsecMapPort = 1
    try:
        mzdMacSecManualHmuxStopTraffic(pDev, macsecMapPort)
    except Exception:
        traceback.print_exc()
    logging.debug(f"macsecMapPort = {macsecMapPort}")
    logging.info("\n")

    logging.info("Function name : mzdMacSecManualHmuxStartTraffic")
    macsecMapPort = 1
    try:
        mzdMacSecManualHmuxStartTraffic(pDev, macsecMapPort)
    except Exception:
        traceback.print_exc()
    logging.debug(f"macsecMapPort = {macsecMapPort}")
    logging.info("\n")

    logging.info("Function name : mzdMacSecHmuxAutoSwitch")
    macsecMapPort = 1
    try:
        mzdMacSecHmuxAutoSwitch(pDev, macsecMapPort)
    except Exception:
        traceback.print_exc()
    logging.debug(f"macsecMapPort = {macsecMapPort}")
    logging.info("\n")

    logging.info("Function name : mzdMacSecHmuxGPIOSwitchCntl")
    macsecMapPort = 1
    enable = 1
    edgeDetect = 1
    try:
        mzdMacSecHmuxGPIOSwitchCntl(pDev, macsecMapPort, enable, edgeDetect)
    except Exception:
        traceback.print_exc()
    logging.debug(f"macsecMapPort = {macsecMapPort}")
    logging.debug(f"enable = {enable}")
    logging.debug(f"edgeDetect = {edgeDetect}")
    logging.info("\n")

    logging.info("Function name : mzdMacSecHmuxLevelGPIOSwitchCntl")
    enable = 1
    try:
        mzdMacSecHmuxLevelGPIOSwitchCntl(pDev, enable)
    except Exception:
        traceback.print_exc()
    logging.debug(f"enable = {enable}")
    logging.info("\n")

    logging.info("Function name : mzdMacSecHmuxStatusOutputCntl")
    macsecMapPort = 1
    enable = 1
    polarity = 1
    try:
        mzdMacSecHmuxStatusOutputCntl(pDev, macsecMapPort, enable, polarity)
    except Exception:
        traceback.print_exc()
    logging.debug(f"macsecMapPort = {macsecMapPort}")
    logging.debug(f"enable = {enable}")
    logging.debug(f"polarity = {polarity}")
    logging.info("\n")

    logging.info("Function name : mzdMacTxFifoReset")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    try:
        mzdMacTxFifoReset(pDev, mdioPort, host_or_line, laneOffset)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.info("\n")

    logging.info("Function name : mzdMacInsertTxCRC")
    mdioPort = 1
    laneOffset = 1
    insertTxCRC = MZD_BOOL.MZD_FALSE.value
    try:
        mzdMacInsertTxCRC(pDev, mdioPort, laneOffset, insertTxCRC)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"insertTxCRC = {insertTxCRC}")
    logging.info("\n")

    logging.info("Function name : mzdMacForwardRxCRC")
    mdioPort = 1
    laneOffset = 1
    forwardRxCRC = MZD_BOOL.MZD_FALSE.value
    try:
        mzdMacForwardRxCRC(pDev, mdioPort, laneOffset, forwardRxCRC)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"forwardRxCRC = {forwardRxCRC}")
    logging.info("\n")

    logging.info("Function name : mzdMacFlowControl")
    mdioPort = 1
    laneOffset = 1
    flowCntlOption = 1
    enableFlag = 1
    try:
        mzdMacFlowControl(pDev, mdioPort, laneOffset, flowCntlOption, enableFlag)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"flowCntlOption = {flowCntlOption}")
    logging.debug(f"enableFlag = {enableFlag}")
    logging.info("\n")

    logging.info("Function name : mzdSetMacLaneInterruptEnable")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    intrEnable = 1
    try:
        mzdSetMacLaneInterruptEnable(pDev, mdioPort, host_or_line, laneOffset, intrEnable)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"intrEnable = {intrEnable}")
    logging.info("\n")

    logging.info("Function name : mzdGetMacLaneInterruptEnable")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    intrEnable = 1
    intrEnable_p = c_uint32(intrEnable)
    try:
        mzdGetMacLaneInterruptEnable(pDev, mdioPort, host_or_line, laneOffset, intrEnable_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"intrEnable = {intrEnable_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdGetMacLaneInterruptStatus")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    intrStatus = 1
    intrStatus_p = c_uint32(intrStatus)
    try:
        mzdGetMacLaneInterruptStatus(pDev, mdioPort, host_or_line, laneOffset, intrStatus_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"intrStatus = {intrStatus_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdSetMacTodInterruptEnable")
    mdioPort = 1
    host_or_line = 1
    overrunIntrEnable = 1
    underrunIntrEnable = 1
    try:
        mzdSetMacTodInterruptEnable(pDev, mdioPort, host_or_line, overrunIntrEnable, underrunIntrEnable)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"overrunIntrEnable = {overrunIntrEnable}")
    logging.debug(f"underrunIntrEnable = {underrunIntrEnable}")
    logging.info("\n")

    logging.info("Function name : mzdGetMacTodInterruptEnable")
    mdioPort = 1
    host_or_line = 1
    overrunIntrEnable = 1
    overrunIntrEnable_p = c_uint32(overrunIntrEnable)
    underrunIntrEnable = 1
    underrunIntrEnable_p = c_uint32(underrunIntrEnable)
    try:
        mzdGetMacTodInterruptEnable(pDev, mdioPort, host_or_line, overrunIntrEnable_p, underrunIntrEnable_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"overrunIntrEnable = {overrunIntrEnable_p.value}")
    logging.debug(f"underrunIntrEnable = {underrunIntrEnable_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdGetMacTodInterruptStatus")
    mdioPort = 1
    host_or_line = 1
    intrType = MZD_MAC_TOD_INTR_TYPE.MZD_MAC_TOD_INTR_TYPE_OVERRUN.value
    overrunIntrStatus = 1
    overrunIntrStatus_p = c_uint32(overrunIntrStatus)
    underrunIntrStatus = 1
    underrunIntrStatus_p = c_uint32(underrunIntrStatus)
    try:
        mzdGetMacTodInterruptStatus(pDev, mdioPort, host_or_line, intrType, overrunIntrStatus_p, underrunIntrStatus_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"intrType = {intrType}")
    logging.debug(f"overrunIntrStatus = {overrunIntrStatus_p.value}")
    logging.debug(f"underrunIntrStatus = {underrunIntrStatus_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdSetMacGlobalInterruptEnable")
    mdioPort = 1
    host_or_line = 1
    intrEnable = 1
    try:
        mzdSetMacGlobalInterruptEnable(pDev, mdioPort, host_or_line, intrEnable)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"intrEnable = {intrEnable}")
    logging.info("\n")

    logging.info("Function name : mzdGetMacGlobalInterruptEnable")
    mdioPort = 1
    host_or_line = 1
    intrEnable = 1
    intrEnable_p = c_uint32(intrEnable)
    try:
        mzdGetMacGlobalInterruptEnable(pDev, mdioPort, host_or_line, intrEnable_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"intrEnable = {intrEnable_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdGetMacGlobalInterruptStatus")
    mdioPort = 1
    host_or_line = 1
    intrStatus = 1
    intrStatus_p = c_uint32(intrStatus)
    try:
        mzdGetMacGlobalInterruptStatus(pDev, mdioPort, host_or_line, intrStatus_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"intrStatus = {intrStatus_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdMacSecHmuxConfigDump")
    mdioPort = 1
    dumpOptions = 1
    try:
        mzdMacSecHmuxConfigDump(pDev, mdioPort, dumpOptions)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"dumpOptions = {dumpOptions}")
    logging.info("\n")

    logging.info("Function name : mzdPtpInit")
    mdioPort = 1
    try:
        mzdPtpInit(pDev, mdioPort)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.info("\n")

    logging.info("Function name : mzdPtpDisable")
    mdioPort = 1
    laneOffset = 1
    isEgress = MZD_BOOL.MZD_FALSE.value
    try:
        mzdPtpDisable(pDev, mdioPort, laneOffset, isEgress)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"isEgress = {isEgress}")
    logging.info("\n")

    logging.info("Function name : mzdPtpDisableAllPacketType")
    mdioPort = 1
    laneOffset = 1
    isEgress = MZD_BOOL.MZD_FALSE.value
    try:
        mzdPtpDisableAllPacketType(pDev, mdioPort, laneOffset, isEgress)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"isEgress = {isEgress}")
    logging.info("\n")

    logging.info("Function name : mzdPtpTCInit")
    mdioPort = 1
    laneOffset = 1
    isEgress = MZD_BOOL.MZD_FALSE.value
    try:
        mzdPtpTCInit(pDev, mdioPort, laneOffset, isEgress)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"isEgress = {isEgress}")
    logging.info("\n")

    logging.info("Function name : mzdPtpDistributedTCInit")
    mdioPort = 1
    laneOffset = 1
    isEgress = MZD_BOOL.MZD_FALSE.value
    try:
        mzdPtpDistributedTCInit(pDev, mdioPort, laneOffset, isEgress)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"isEgress = {isEgress}")
    logging.info("\n")

    logging.info("Function name : mzdPtpFromReservedInit")
    mdioPort = 1
    laneOffset = 1
    isEgress = MZD_BOOL.MZD_FALSE.value
    try:
        mzdPtpFromReservedInit(pDev, mdioPort, laneOffset, isEgress)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"isEgress = {isEgress}")
    logging.info("\n")

    logging.info("Function name : mzdPtpSetIgnoreMacSec")
    mdioPort = 1
    laneOffset = 1
    isEgress = MZD_BOOL.MZD_FALSE.value
    isIgnore = MZD_BOOL.MZD_FALSE.value
    try:
        mzdPtpSetIgnoreMacSec(pDev, mdioPort, laneOffset, isEgress, isIgnore)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"isEgress = {isEgress}")
    logging.debug(f"isIgnore = {isIgnore}")
    logging.info("\n")

    logging.info("Function name : mzdPtpGetEgressTSQ")
    mdioPort = 1
    laneOffset = 1
    queueId = 1
    egressTSQ = MZD_PTP_EGRESS_TSQ(0, 0, 0, 0, 0)
    egressTSQ_p = byref(egressTSQ)
    try:
        mzdPtpGetEgressTSQ(pDev, mdioPort, laneOffset, queueId, egressTSQ_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"queueId = {queueId}")
    logging.debug(f"egressTSQ = {MZD_PTP_EGRESS_TSQ.timestamp}")
    logging.debug(f"egressTSQ = {MZD_PTP_EGRESS_TSQ.todUpdate}")
    logging.debug(f"egressTSQ = {MZD_PTP_EGRESS_TSQ.taiSelect}")
    logging.debug(f"egressTSQ = {MZD_PTP_EGRESS_TSQ.queueEntryID}")
    logging.debug(f"egressTSQ = {MZD_PTP_EGRESS_TSQ.valid}")
    logging.info("\n")

    logging.info("Function name : mzdPtpGetIngressTSQ")
    mdioPort = 1
    laneOffset = 1
    ingressTSQ = MZD_PTP_INGRESS_TSQ(0, 0, 0, 0, 0, 0, 0)
    ingressTSQ_p = byref(ingressTSQ)
    try:
        mzdPtpGetIngressTSQ(pDev, mdioPort, laneOffset, ingressTSQ_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"ingressTSQ = {MZD_PTP_INGRESS_TSQ.timestamp}")
    logging.debug(f"ingressTSQ = {MZD_PTP_INGRESS_TSQ.seqId}")
    logging.debug(f"ingressTSQ = {MZD_PTP_INGRESS_TSQ.domain}")
    logging.debug(f"ingressTSQ = {MZD_PTP_INGRESS_TSQ.mssageType}")
    logging.debug(f"ingressTSQ = {MZD_PTP_INGRESS_TSQ.taiSelect}")
    logging.debug(f"ingressTSQ = {MZD_PTP_INGRESS_TSQ.todUpdate}")
    logging.debug(f"ingressTSQ = {MZD_PTP_INGRESS_TSQ.valid}")
    logging.info("\n")

    logging.info("Function name : mzdPtpSetMACOneStep")
    mdioPort = 1
    laneOffset = 1
    host_or_line = 1
    isHighSpeed = MZD_BOOL.MZD_FALSE.value
    isEnable = MZD_BOOL.MZD_FALSE.value
    try:
        mzdPtpSetMACOneStep(pDev, mdioPort, laneOffset, host_or_line, isHighSpeed, isEnable)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"isHighSpeed = {isHighSpeed}")
    logging.debug(f"isEnable = {isEnable}")
    logging.info("\n")

    logging.info("Function name : mzdPtpTODSelect")
    mdioPort = 1
    laneOffset = 1
    host_or_line = 1
    isHighSpeed = MZD_BOOL.MZD_FALSE.value
    taiSel = MZD_TAI_SELECT.MZD_TAI0.value
    try:
        mzdPtpTODSelect(pDev, mdioPort, laneOffset, host_or_line, isHighSpeed, taiSel)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"isHighSpeed = {isHighSpeed}")
    logging.debug(f"taiSel = {taiSel}")
    logging.info("\n")

    logging.info("Function name : mzdPtpVxlanEnable")
    mdioPort = 1
    laneOffset = 1
    isEgress = MZD_BOOL.MZD_FALSE.value
    isEnable = MZD_BOOL.MZD_FALSE.value
    try:
        mzdPtpVxlanEnable(pDev, mdioPort, laneOffset, isEgress, isEnable)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"isEgress = {isEgress}")
    logging.debug(f"isEnable = {isEnable}")
    logging.info("\n")

    logging.info("Function name : mzdPtpEnableSelectPacketType")
    mdioPort = 1
    laneOffset = 1
    isEgress = MZD_BOOL.MZD_FALSE.value
    packetType = MZD_PACKET_TYPE.MZD_PTP_ETHERTYPE.value
    try:
        mzdPtpEnableSelectPacketType(pDev, mdioPort, laneOffset, isEgress, packetType)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"isEgress = {isEgress}")
    logging.debug(f"packetType = {packetType}")
    logging.info("\n")

    logging.info("Function name : mzdPtpUserDefinedTPID")
    mdioPort = 1
    isEgress = MZD_BOOL.MZD_FALSE.value
    entryId = 1
    tpid = 1
    try:
        mzdPtpUserDefinedTPID(pDev, mdioPort, isEgress, entryId, tpid)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"isEgress = {isEgress}")
    logging.debug(f"entryId = {entryId}")
    logging.debug(f"tpid = {tpid}")
    logging.info("\n")

    logging.info("Function name : mzdPtpTSDFSEnable")
    mdioPort = 1
    laneOffset = 1
    host_or_line = 1
    opMode = MZD_OP_MODE.MZD_OP_MODE_UNKNOWN.value
    isEnable = MZD_BOOL.MZD_FALSE.value
    try:
        mzdPtpTSDFSEnable(pDev, mdioPort, laneOffset, host_or_line, opMode, isEnable)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"opMode = {opMode}")
    logging.debug(f"isEnable = {isEnable}")
    logging.info("\n")

    logging.info("Function name : mzdPtpTSDAMREnable")
    mdioPort = 1
    laneOffset = 1
    host_or_line = 1
    opMode = MZD_OP_MODE.MZD_OP_MODE_UNKNOWN.value
    isEnable = MZD_BOOL.MZD_FALSE.value
    try:
        mzdPtpTSDAMREnable(pDev, mdioPort, laneOffset, host_or_line, opMode, isEnable)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"opMode = {opMode}")
    logging.debug(f"isEnable = {isEnable}")
    logging.info("\n")

    logging.info("Function name : mzdPtpTSXEnable")
    mdioPort = 1
    laneOffset = 1
    host_or_line = 1
    isEgress = MZD_BOOL.MZD_FALSE.value
    isHighSpeed = MZD_BOOL.MZD_FALSE.value
    isEnable = MZD_BOOL.MZD_FALSE.value
    try:
        mzdPtpTSXEnable(pDev, mdioPort, laneOffset, host_or_line, isEgress, isHighSpeed, isEnable)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"isEgress = {isEgress}")
    logging.debug(f"isHighSpeed = {isHighSpeed}")
    logging.debug(f"isEnable = {isEnable}")
    logging.info("\n")

    logging.info("Function name : mzdPtpSetShareBufferPTPIgnore")
    mdioPort = 1
    isIgnore = MZD_BOOL.MZD_FALSE.value
    try:
        mzdPtpSetShareBufferPTPIgnore(pDev, mdioPort, isIgnore)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"isIgnore = {isIgnore}")
    logging.info("\n")

    logging.info("Function name : mzdPtpSetBypassEip218")
    mdioPort = 1
    isBypass = MZD_BOOL.MZD_FALSE.value
    try:
        mzdPtpSetBypassEip218(pDev, mdioPort, isBypass)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"isBypass = {isBypass}")
    logging.info("\n")

    logging.info("Function name : mzdTaiInit")
    mdioPort = 1
    try:
        mzdTaiInit(pDev, mdioPort)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.info("\n")

    logging.info("Function name : mzdTaiReadRegister")
    mdioPort = 1
    taiNum = MZD_TAI_SELECT.MZD_TAI0.value
    regAddr = 1
    data = 1
    data_p = c_uint32(data)
    try:
        mzdTaiReadRegister(pDev, mdioPort, taiNum, regAddr, data_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"taiNum = {taiNum}")
    logging.debug(f"regAddr = {regAddr}")
    logging.debug(f"data = {data_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdTaiWriteRegister")
    mdioPort = 1
    taiNum = MZD_TAI_SELECT.MZD_TAI0.value
    regAddr = 1
    data = 1
    try:
        mzdTaiWriteRegister(pDev, mdioPort, taiNum, regAddr, data)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"taiNum = {taiNum}")
    logging.debug(f"regAddr = {regAddr}")
    logging.debug(f"data = {data}")
    logging.info("\n")

    logging.info("Function name : mzdTaiReadRegisterField")
    mdioPort = 1
    taiNum = MZD_TAI_SELECT.MZD_TAI0.value
    regAddr = 1
    fieldOffset = 1
    fieldLength = 1
    data = 1
    data_p = c_uint32(data)
    try:
        mzdTaiReadRegisterField(pDev, mdioPort, taiNum, regAddr, fieldOffset, fieldLength, data_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"taiNum = {taiNum}")
    logging.debug(f"regAddr = {regAddr}")
    logging.debug(f"fieldOffset = {fieldOffset}")
    logging.debug(f"fieldLength = {fieldLength}")
    logging.debug(f"data = {data_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdTaiWriteRegisterField")
    mdioPort = 1
    taiNum = MZD_TAI_SELECT.MZD_TAI0.value
    regAddr = 1
    fieldOffset = 1
    fieldLength = 1
    data = 1
    try:
        mzdTaiWriteRegisterField(pDev, mdioPort, taiNum, regAddr, fieldOffset, fieldLength, data)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"taiNum = {taiNum}")
    logging.debug(f"regAddr = {regAddr}")
    logging.debug(f"fieldOffset = {fieldOffset}")
    logging.debug(f"fieldLength = {fieldLength}")
    logging.debug(f"data = {data}")
    logging.info("\n")

    logging.info("Function name : mzdTaiTodUpdate")
    mdioPort = 1
    taiNum = MZD_TAI_SELECT.MZD_TAI0.value
    timeArray = MZD_TAI_TIME_ARRAY(0, 0, 0, 0)
    timeArray_p = byref(timeArray)
    try:
        mzdTaiTodUpdate(pDev, mdioPort, taiNum, timeArray_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"taiNum = {taiNum}")
    logging.debug(f"timeArray = {MZD_TAI_TIME_ARRAY.todSecondsHigh}")
    logging.debug(f"timeArray = {MZD_TAI_TIME_ARRAY.todSecondsLow}")
    logging.debug(f"timeArray = {MZD_TAI_TIME_ARRAY.todNanoseconds}")
    logging.debug(f"timeArray = {MZD_TAI_TIME_ARRAY.todFracNano}")
    logging.info("\n")

    logging.info("Function name : mzdTaiTodFreqUpdate")
    mdioPort = 1
    taiNum = MZD_TAI_SELECT.MZD_TAI0.value
    fracNano = 1
    try:
        mzdTaiTodFreqUpdate(pDev, mdioPort, taiNum, fracNano)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"taiNum = {taiNum}")
    logging.debug(f"fracNano = {fracNano}")
    logging.info("\n")

    logging.info("Function name : mzdTaiTodCapture")
    mdioPort = 1
    taiNum = MZD_TAI_SELECT.MZD_TAI0.value
    try:
        mzdTaiTodCapture(pDev, mdioPort, taiNum)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"taiNum = {taiNum}")
    logging.info("\n")

    logging.info("Function name : mzdTaiTodIncrement")
    mdioPort = 1
    taiNum = MZD_TAI_SELECT.MZD_TAI0.value
    todOffset = MZD_TAI_TIME_ARRAY(0, 0, 0, 0)
    todOffset_p = byref(todOffset)
    try:
        mzdTaiTodIncrement(pDev, mdioPort, taiNum, todOffset_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"taiNum = {taiNum}")
    logging.debug(f"todOffset = {MZD_TAI_TIME_ARRAY.todSecondsHigh}")
    logging.debug(f"todOffset = {MZD_TAI_TIME_ARRAY.todSecondsLow}")
    logging.debug(f"todOffset = {MZD_TAI_TIME_ARRAY.todNanoseconds}")
    logging.debug(f"todOffset = {MZD_TAI_TIME_ARRAY.todFracNano}")
    logging.info("\n")

    logging.info("Function name : mzdTaiTodDecrement")
    mdioPort = 1
    taiNum = MZD_TAI_SELECT.MZD_TAI0.value
    todOffset = MZD_TAI_TIME_ARRAY(0, 0, 0, 0)
    todOffset_p = byref(todOffset)
    try:
        mzdTaiTodDecrement(pDev, mdioPort, taiNum, todOffset_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"taiNum = {taiNum}")
    logging.debug(f"todOffset = {MZD_TAI_TIME_ARRAY.todSecondsHigh}")
    logging.debug(f"todOffset = {MZD_TAI_TIME_ARRAY.todSecondsLow}")
    logging.debug(f"todOffset = {MZD_TAI_TIME_ARRAY.todNanoseconds}")
    logging.debug(f"todOffset = {MZD_TAI_TIME_ARRAY.todFracNano}")
    logging.info("\n")

    logging.info("Function name : mzdTaiTodGracefulInc")
    mdioPort = 1
    taiNum = MZD_TAI_SELECT.MZD_TAI0.value
    graceStep = 1
    todOffset = MZD_TAI_TIME_ARRAY(0, 0, 0, 0)
    todOffset_p = byref(todOffset)
    try:
        mzdTaiTodGracefulInc(pDev, mdioPort, taiNum, graceStep, todOffset_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"taiNum = {taiNum}")
    logging.debug(f"graceStep = {graceStep}")
    logging.debug(f"todOffset = {MZD_TAI_TIME_ARRAY.todSecondsHigh}")
    logging.debug(f"todOffset = {MZD_TAI_TIME_ARRAY.todSecondsLow}")
    logging.debug(f"todOffset = {MZD_TAI_TIME_ARRAY.todNanoseconds}")
    logging.debug(f"todOffset = {MZD_TAI_TIME_ARRAY.todFracNano}")
    logging.info("\n")

    logging.info("Function name : mzdTaiTodGracefulDec")
    mdioPort = 1
    taiNum = MZD_TAI_SELECT.MZD_TAI0.value
    graceStep = 1
    todOffset = MZD_TAI_TIME_ARRAY(0, 0, 0, 0)
    todOffset_p = byref(todOffset)
    try:
        mzdTaiTodGracefulDec(pDev, mdioPort, taiNum, graceStep, todOffset_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"taiNum = {taiNum}")
    logging.debug(f"graceStep = {graceStep}")
    logging.debug(f"todOffset = {MZD_TAI_TIME_ARRAY.todSecondsHigh}")
    logging.debug(f"todOffset = {MZD_TAI_TIME_ARRAY.todSecondsLow}")
    logging.debug(f"todOffset = {MZD_TAI_TIME_ARRAY.todNanoseconds}")
    logging.debug(f"todOffset = {MZD_TAI_TIME_ARRAY.todFracNano}")
    logging.info("\n")

    logging.info("Function name : mzdTaiTodTimeCounterFunctionSet")
    mdioPort = 1
    taiNum = MZD_TAI_SELECT.MZD_TAI0.value
    todOp = MZD_TOD_OP.TOD_UPDATE.value
    try:
        mzdTaiTodTimeCounterFunctionSet(pDev, mdioPort, taiNum, todOp)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"taiNum = {taiNum}")
    logging.debug(f"todOp = {todOp}")
    logging.info("\n")

    logging.info("Function name : mzdTaiTodTimeLoadValueSet")
    mdioPort = 1
    taiNum = MZD_TAI_SELECT.MZD_TAI0.value
    todValue = MZD_TAI_TIME_ARRAY(0, 0, 0, 0)
    todValue_p = byref(todValue)
    try:
        mzdTaiTodTimeLoadValueSet(pDev, mdioPort, taiNum, todValue_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"taiNum = {taiNum}")
    logging.debug(f"todValue = {MZD_TAI_TIME_ARRAY.todSecondsHigh}")
    logging.debug(f"todValue = {MZD_TAI_TIME_ARRAY.todSecondsLow}")
    logging.debug(f"todValue = {MZD_TAI_TIME_ARRAY.todNanoseconds}")
    logging.debug(f"todValue = {MZD_TAI_TIME_ARRAY.todFracNano}")
    logging.info("\n")

    logging.info("Function name : mzdTaiTodTimeCaptureValue0Get")
    mdioPort = 1
    taiNum = MZD_TAI_SELECT.MZD_TAI0.value
    todValue = MZD_TAI_TIME_ARRAY(0, 0, 0, 0)
    todValue_p = byref(todValue)
    try:
        mzdTaiTodTimeCaptureValue0Get(pDev, mdioPort, taiNum, todValue_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"taiNum = {taiNum}")
    logging.debug(f"todValue = {MZD_TAI_TIME_ARRAY.todSecondsHigh}")
    logging.debug(f"todValue = {MZD_TAI_TIME_ARRAY.todSecondsLow}")
    logging.debug(f"todValue = {MZD_TAI_TIME_ARRAY.todNanoseconds}")
    logging.debug(f"todValue = {MZD_TAI_TIME_ARRAY.todFracNano}")
    logging.info("\n")

    logging.info("Function name : mzdTaiTodTimeCaptureValue1Get")
    mdioPort = 1
    taiNum = MZD_TAI_SELECT.MZD_TAI0.value
    todValue = MZD_TAI_TIME_ARRAY(0, 0, 0, 0)
    todValue_p = byref(todValue)
    try:
        mzdTaiTodTimeCaptureValue1Get(pDev, mdioPort, taiNum, todValue_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"taiNum = {taiNum}")
    logging.debug(f"todValue = {MZD_TAI_TIME_ARRAY.todSecondsHigh}")
    logging.debug(f"todValue = {MZD_TAI_TIME_ARRAY.todSecondsLow}")
    logging.debug(f"todValue = {MZD_TAI_TIME_ARRAY.todNanoseconds}")
    logging.debug(f"todValue = {MZD_TAI_TIME_ARRAY.todFracNano}")
    logging.info("\n")

    logging.info("Function name : mzdTaiTodTimeCaptureStatusGet")
    mdioPort = 1
    taiNum = MZD_TAI_SELECT.MZD_TAI0.value
    valid = 1
    valid_p = c_uint32(valid)
    try:
        mzdTaiTodTimeCaptureStatusGet(pDev, mdioPort, taiNum, valid_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"taiNum = {taiNum}")
    logging.debug(f"valid = {valid_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdTaiTodStepSet")
    mdioPort = 1
    taiNum = MZD_TAI_SELECT.MZD_TAI0.value
    stepNano = 1
    stepFracNano = 1
    try:
        mzdTaiTodStepSet(pDev, mdioPort, taiNum, stepNano, stepFracNano)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"taiNum = {taiNum}")
    logging.debug(f"stepNano = {stepNano}")
    logging.debug(f"stepFracNano = {stepFracNano}")
    logging.info("\n")

    logging.info("Function name : mzdTaiTodStepGet")
    mdioPort = 1
    taiNum = MZD_TAI_SELECT.MZD_TAI0.value
    stepNano = 1
    stepNano_p = c_uint16(stepNano)
    stepFracNano = 1
    stepFracNano_p = c_int32(stepFracNano)
    try:
        mzdTaiTodStepGet(pDev, mdioPort, taiNum, stepNano_p, stepFracNano_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"taiNum = {taiNum}")
    logging.debug(f"stepNano = {stepNano_p.value}")
    logging.debug(f"stepFracNano = {stepFracNano_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdTaiPpsGenerationSet")
    mdioPort = 1
    taiNum = MZD_TAI_SELECT.MZD_TAI0.value
    pulseData = MZD_TAI_PPS_PULSE(0, 0, 0)
    pulseData_p = byref(pulseData)
    try:
        mzdTaiPpsGenerationSet(pDev, mdioPort, taiNum, pulseData_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"taiNum = {taiNum}")
    logging.debug(f"pulseData = {MZD_TAI_PPS_PULSE.ppsPulseCycSec}")
    logging.debug(f"pulseData = {MZD_TAI_PPS_PULSE.ppsPulseCycNanoSec}")
    logging.debug(f"pulseData = {MZD_TAI_PPS_PULSE.ppsPulseHiLvLen}")
    logging.info("\n")

    logging.info("Function name : mzdTaiPpsReceptionSet")
    mdioPort = 1
    taiNum = MZD_TAI_SELECT.MZD_TAI0.value
    pulseData = MZD_TAI_PPS_PULSE(0, 0, 0)
    pulseData_p = byref(pulseData)
    try:
        mzdTaiPpsReceptionSet(pDev, mdioPort, taiNum, pulseData_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"taiNum = {taiNum}")
    logging.debug(f"pulseData = {MZD_TAI_PPS_PULSE.ppsPulseCycSec}")
    logging.debug(f"pulseData = {MZD_TAI_PPS_PULSE.ppsPulseCycNanoSec}")
    logging.debug(f"pulseData = {MZD_TAI_PPS_PULSE.ppsPulseHiLvLen}")
    logging.info("\n")

    logging.info("Function name : mzdTaiPpsAdvReceptionSet")
    mdioPort = 1
    taiNum = MZD_TAI_SELECT.MZD_TAI0.value
    pulseData = MZD_TAI_PPS_PULSE(0, 0, 0)
    pulseData_p = byref(pulseData)
    try:
        mzdTaiPpsAdvReceptionSet(pDev, mdioPort, taiNum, pulseData_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"taiNum = {taiNum}")
    logging.debug(f"pulseData = {MZD_TAI_PPS_PULSE.ppsPulseCycSec}")
    logging.debug(f"pulseData = {MZD_TAI_PPS_PULSE.ppsPulseCycNanoSec}")
    logging.debug(f"pulseData = {MZD_TAI_PPS_PULSE.ppsPulseHiLvLen}")
    logging.info("\n")

    logging.info("Function name : mzdTaiTriggerGenerationPulseSet")
    mdioPort = 1
    taiNum = MZD_TAI_SELECT.MZD_TAI0.value
    triggerTod = MZD_TAI_TIME_ARRAY(0, 0, 0, 0)
    triggerTod_p = byref(triggerTod)
    triggerTodMask = MZD_TAI_TIME_ARRAY(0, 0, 0, 0)
    triggerTodMask_p = byref(triggerTodMask)
    pulseWidth = 1
    try:
        mzdTaiTriggerGenerationPulseSet(pDev, mdioPort, taiNum, triggerTod_p, triggerTodMask_p, pulseWidth)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"taiNum = {taiNum}")
    logging.debug(f"triggerTod = {MZD_TAI_TIME_ARRAY.todSecondsHigh}")
    logging.debug(f"triggerTod = {MZD_TAI_TIME_ARRAY.todSecondsLow}")
    logging.debug(f"triggerTod = {MZD_TAI_TIME_ARRAY.todNanoseconds}")
    logging.debug(f"triggerTod = {MZD_TAI_TIME_ARRAY.todFracNano}")
    logging.debug(f"triggerTodMask = {MZD_TAI_TIME_ARRAY.todSecondsHigh}")
    logging.debug(f"triggerTodMask = {MZD_TAI_TIME_ARRAY.todSecondsLow}")
    logging.debug(f"triggerTodMask = {MZD_TAI_TIME_ARRAY.todNanoseconds}")
    logging.debug(f"triggerTodMask = {MZD_TAI_TIME_ARRAY.todFracNano}")
    logging.debug(f"pulseWidth = {pulseWidth}")
    logging.info("\n")

    logging.info("Function name : mzdTaiPulseInMuxingEnableSet")
    mdioPort = 1
    taiNum = MZD_TAI_SELECT.MZD_TAI0.value
    en = MZD_BOOL.MZD_FALSE.value
    try:
        mzdTaiPulseInMuxingEnableSet(pDev, mdioPort, taiNum, en)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"taiNum = {taiNum}")
    logging.debug(f"en = {en}")
    logging.info("\n")

    logging.info("Function name : mzdTaiInterruptCauseGet")
    mdioPort = 1
    taiNum = MZD_TAI_SELECT.MZD_TAI0.value
    intCause = 1
    intCause_p = c_uint32(intCause)
    try:
        mzdTaiInterruptCauseGet(pDev, mdioPort, taiNum, intCause_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"taiNum = {taiNum}")
    logging.debug(f"intCause = {intCause_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdTaiInterruptMaskSet")
    mdioPort = 1
    taiNum = MZD_TAI_SELECT.MZD_TAI0.value
    intMask = 1
    try:
        mzdTaiInterruptMaskSet(pDev, mdioPort, taiNum, intMask)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"taiNum = {taiNum}")
    logging.debug(f"intMask = {intMask}")
    logging.info("\n")

    logging.info("Function name : mzdTaiTodFractionalNanosecondDriftGet")
    mdioPort = 1
    taiNum = MZD_TAI_SELECT.MZD_TAI0.value
    driftValue = 1
    driftValue_p = c_uint32(driftValue)
    try:
        mzdTaiTodFractionalNanosecondDriftGet(pDev, mdioPort, taiNum, driftValue_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"taiNum = {taiNum}")
    logging.debug(f"driftValue = {driftValue_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdTaiClockGenClockRatioSet")
    mdioPort = 1
    taiNum = MZD_TAI_SELECT.MZD_TAI0.value
    ratio = 1
    try:
        mzdTaiClockGenClockRatioSet(pDev, mdioPort, taiNum, ratio)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"taiNum = {taiNum}")
    logging.debug(f"ratio = {ratio}")
    logging.info("\n")

    logging.info("Function name : mzdTaiTodUpdateEnableFirmware")
    mdioPort = 1
    taiNum = MZD_TAI_SELECT.MZD_TAI0.value
    enableTodUpdate = MZD_BOOL.MZD_FALSE.value
    try:
        mzdTaiTodUpdateEnableFirmware(pDev, mdioPort, taiNum, enableTodUpdate)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"taiNum = {taiNum}")
    logging.debug(f"enableTodUpdate = {enableTodUpdate}")
    logging.info("\n")

    logging.info("Function name : mzdTaiTodUpdateEnableFirmwareGet")
    enableTodUpdate = MZD_BOOL.MZD_FALSE.value
    enableTodUpdate_p = MZD_BOOL(enableTodUpdate)
    try:
        mzdTaiTodUpdateEnableFirmwareGet(pDev, enableTodUpdate_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"enableTodUpdate = {enableTodUpdate_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdTaiClockConfig")
    mdioPort = 1
    refClock = MZD_TAI_REF_CLK.MZD_TAI_REF_CLK_0.value
    taiClock = MZD_TAI_CLK.MZD_TAI_CLK_0.value
    try:
        mzdTaiClockConfig(pDev, mdioPort, refClock, taiClock)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"refClock = {refClock}")
    logging.debug(f"taiClock = {taiClock}")
    logging.info("\n")

    logging.info("Function name : mzdMacSecSupportedMacSecDeviceCount")
    supportedMacSecDeviceCount = 1
    supportedMacSecDeviceCount_p = c_uint16(supportedMacSecDeviceCount)
    try:
        mzdMacSecSupportedMacSecDeviceCount(pDev, supportedMacSecDeviceCount_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"supportedMacSecDeviceCount = {supportedMacSecDeviceCount_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdMacSecGetAssignedDeviceID")
    mdioPort = 1
    macsecIngressDevId = 1
    macsecIngressDevId_p = c_uint8(macsecIngressDevId)
    macsecEgressDevId = 1
    macsecEgressDevId_p = c_uint8(macsecEgressDevId)
    try:
        mzdMacSecGetAssignedDeviceID(pDev, mdioPort, macsecIngressDevId_p, macsecEgressDevId_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"macsecIngressDevId = {macsecIngressDevId_p.value}")
    logging.debug(f"macsecEgressDevId = {macsecEgressDevId_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdMacSecDeviceInit")
    mdioPort = 1
    laneOffset = 1
    try:
        mzdMacSecDeviceInit(pDev, mdioPort, laneOffset)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.info("\n")

    logging.info("Function name : mzdMacSecDropAction")
    mdioPort = 1
    fIngress = MZD_BOOL.MZD_FALSE.value
    dropAction = MZD_BOOL.MZD_FALSE.value
    try:
        mzdMacSecDropAction(pDev, mdioPort, fIngress, dropAction)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"fIngress = {fIngress}")
    logging.debug(f"dropAction = {dropAction}")
    logging.info("\n")

    logging.info("Function name : mzdMACsecInterruptEnable")
    mdioPort = 1
    laneOffset = 1
    deviceMACSecId = 1
    cfyE_or_secY = MZD_MACSEC_BLOCK.MZD_MACSEC_CFYE.value
    interruptMask = 1
    bGlobalInterrupt = MZD_BOOL.MZD_FALSE.value
    try:
        mzdMACsecInterruptEnable(pDev, mdioPort, laneOffset, deviceMACSecId, cfyE_or_secY, interruptMask, bGlobalInterrupt)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"deviceMACSecId = {deviceMACSecId}")
    logging.debug(f"cfyE_or_secY = {cfyE_or_secY}")
    logging.debug(f"interruptMask = {interruptMask}")
    logging.debug(f"bGlobalInterrupt = {bGlobalInterrupt}")
    logging.info("\n")

    logging.info("Function name : mzdMACsecInterruptClear")
    mdioPort = 1
    laneOffset = 1
    deviceMACSecId = 1
    cfyE_or_secY = MZD_MACSEC_BLOCK.MZD_MACSEC_CFYE.value
    interruptMask = 1
    bGlobalInterrupt = MZD_BOOL.MZD_FALSE.value
    try:
        mzdMACsecInterruptClear(pDev, mdioPort, laneOffset, deviceMACSecId, cfyE_or_secY, interruptMask, bGlobalInterrupt)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"deviceMACSecId = {deviceMACSecId}")
    logging.debug(f"cfyE_or_secY = {cfyE_or_secY}")
    logging.debug(f"interruptMask = {interruptMask}")
    logging.debug(f"bGlobalInterrupt = {bGlobalInterrupt}")
    logging.info("\n")

    logging.info("Function name : mzdMACsecInterruptDisable")
    mdioPort = 1
    laneOffset = 1
    deviceMACSecId = 1
    cfyE_or_secY = MZD_MACSEC_BLOCK.MZD_MACSEC_CFYE.value
    interruptMask = 1
    bGlobalInterrupt = MZD_BOOL.MZD_FALSE.value
    try:
        mzdMACsecInterruptDisable(pDev, mdioPort, laneOffset, deviceMACSecId, cfyE_or_secY, interruptMask, bGlobalInterrupt)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"deviceMACSecId = {deviceMACSecId}")
    logging.debug(f"cfyE_or_secY = {cfyE_or_secY}")
    logging.debug(f"interruptMask = {interruptMask}")
    logging.debug(f"bGlobalInterrupt = {bGlobalInterrupt}")
    logging.info("\n")

    logging.info("Function name : mzdMACsecGetInterruptStatus")
    mdioPort = 1
    laneOffset = 1
    deviceMACSecId = 1
    cfyE_or_secY = MZD_MACSEC_BLOCK.MZD_MACSEC_CFYE.value
    interruptSourceStatus = 1
    interruptSourceStatus_p = c_uint32(interruptSourceStatus)
    bGlobalInterrupt = MZD_BOOL.MZD_FALSE.value
    try:
        mzdMACsecGetInterruptStatus(pDev, mdioPort, laneOffset, deviceMACSecId, cfyE_or_secY, interruptSourceStatus_p, bGlobalInterrupt)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"deviceMACSecId = {deviceMACSecId}")
    logging.debug(f"cfyE_or_secY = {cfyE_or_secY}")
    logging.debug(f"interruptSourceStatus = {interruptSourceStatus_p.value}")
    logging.debug(f"bGlobalInterrupt = {bGlobalInterrupt}")
    logging.info("\n")

    logging.info("Function name : mzdMACsecGetEnabledInterruptStatus")
    mdioPort = 1
    laneOffset = 1
    deviceMACSecId = 1
    cfyE_or_secY = MZD_MACSEC_BLOCK.MZD_MACSEC_CFYE.value
    interruptSourceStatus = 1
    interruptSourceStatus_p = c_uint32(interruptSourceStatus)
    bGlobalInterrupt = MZD_BOOL.MZD_FALSE.value
    try:
        mzdMACsecGetEnabledInterruptStatus(pDev, mdioPort, laneOffset, deviceMACSecId, cfyE_or_secY, interruptSourceStatus_p, bGlobalInterrupt)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"deviceMACSecId = {deviceMACSecId}")
    logging.debug(f"cfyE_or_secY = {cfyE_or_secY}")
    logging.debug(f"interruptSourceStatus = {interruptSourceStatus_p.value}")
    logging.debug(f"bGlobalInterrupt = {bGlobalInterrupt}")
    logging.info("\n")

    logging.info("Function name : mzdMACsecMappedAICDevices")
    mdioPort = 1
    laneOffset = 1
    deviceMACSecId = 1
    cfyE_or_secY = MZD_MACSEC_BLOCK.MZD_MACSEC_CFYE.value
    try:
        mzdMACsecMappedAICDevices(pDev, mdioPort, laneOffset, deviceMACSecId, cfyE_or_secY, globalICDev, channelICDev)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"deviceMACSecId = {deviceMACSecId}")
    logging.debug(f"cfyE_or_secY = {cfyE_or_secY}")
    logging.info("\n")

    logging.info("Function name : mzdGetAPIVersion")
    major = 1
    major_p = c_uint8(major)
    minor = 1
    minor_p = c_uint8(minor)
    buildID = 1
    buildID_p = c_uint8(buildID)
    try:
        mzdGetAPIVersion(major_p, minor_p, buildID_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"major = {major_p.value}")
    logging.debug(f"minor = {minor_p.value}")
    logging.debug(f"buildID = {buildID_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdSetModeSelection")
    mdioPort = 1
    laneOffset = 1
    hostMode = MZD_OP_MODE.MZD_OP_MODE_UNKNOWN.value
    lineMode = MZD_OP_MODE.MZD_OP_MODE_UNKNOWN.value
    modeOptionSel = 1
    buffer = (c_uint8 * 128)()
    buffer_init = [0] * 128
    for idx, value in enumerate(buffer_init):
        buffer[idx] = value
    modeOption = MZD_MODE_OPTION_STRUCT(buffer)
    result = 1
    result_p = c_uint16(result)
    try:
        mzdSetModeSelection(pDev, mdioPort, laneOffset, hostMode, lineMode, modeOptionSel, modeOption, result_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"hostMode = {hostMode}")
    logging.debug(f"lineMode = {lineMode}")
    logging.debug(f"modeOptionSel = {modeOptionSel}")
    logging.debug(f"result = {result_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdSetInterfaceUserMode")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    opMode = MZD_OP_MODE.MZD_OP_MODE_UNKNOWN.value
    modeOptionSel = 1
    buffer = (c_uint8 * 128)()
    buffer_init = [0] * 128
    for idx, value in enumerate(buffer_init):
        buffer[idx] = value
    modeOption = MZD_MODE_OPTION_STRUCT(buffer)
    result = 1
    result_p = c_uint16(result)
    try:
        mzdSetInterfaceUserMode(pDev, mdioPort, host_or_line, laneOffset, opMode, modeOptionSel, modeOption, result_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"opMode = {opMode}")
    logging.debug(f"modeOptionSel = {modeOptionSel}")
    logging.debug(f"result = {result_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdGetOpMode")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    opMode = MZD_OP_MODE.MZD_OP_MODE_UNKNOWN.value
    opMode_p = MZD_OP_MODE(opMode)
    try:
        mzdGetOpMode(pDev, mdioPort, host_or_line, laneOffset, opMode_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"opMode = {opMode_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdAutoNegControl")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    enableAutoNeg = 1
    swReset = MZD_BOOL.MZD_FALSE.value
    try:
        mzdAutoNegControl(pDev, mdioPort, host_or_line, laneOffset, enableAutoNeg, swReset)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"enableAutoNeg = {enableAutoNeg}")
    logging.debug(f"swReset = {swReset}")
    logging.info("\n")

    logging.info("Function name : mzdAutoNegCheckComplete")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    autoNegComplete = MZD_BOOL.MZD_FALSE.value
    autoNegComplete_p = MZD_BOOL(autoNegComplete)
    try:
        mzdAutoNegCheckComplete(pDev, mdioPort, host_or_line, laneOffset, autoNegComplete_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"autoNegComplete = {autoNegComplete_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdGetAutoNegResolution")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    speed_bits = 1
    speed_bits_p = c_uint16(speed_bits)
    try:
        mzdGetAutoNegResolution(pDev, mdioPort, host_or_line, laneOffset, speed_bits_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"speed_bits = {speed_bits_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdCL37AutoNegControl")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    enableAutoNeg = 1
    try:
        mzdCL37AutoNegControl(pDev, mdioPort, host_or_line, laneOffset, enableAutoNeg)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"enableAutoNeg = {enableAutoNeg}")
    logging.info("\n")

    logging.info("Function name : mzdCL37AutoNegCheckComplete")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    autoNegComplete = MZD_BOOL.MZD_FALSE.value
    autoNegComplete_p = MZD_BOOL(autoNegComplete)
    try:
        mzdCL37AutoNegCheckComplete(pDev, mdioPort, host_or_line, laneOffset, autoNegComplete_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"autoNegComplete = {autoNegComplete_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdSetPauseAdvertisement")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    pauseType = 1
    swReset = MZD_BOOL.MZD_FALSE.value
    try:
        mzdSetPauseAdvertisement(pDev, mdioPort, host_or_line, laneOffset, pauseType, swReset)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"pauseType = {pauseType}")
    logging.debug(f"swReset = {swReset}")
    logging.info("\n")

    logging.info("Function name : mzdGetPauseAdvertisement")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    pauseType = 1
    pauseType_p = c_uint16(pauseType)
    try:
        mzdGetPauseAdvertisement(pDev, mdioPort, host_or_line, laneOffset, pauseType_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"pauseType = {pauseType_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdGetLPAdvertisedPause")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    pauseType = 1
    pauseType_p = c_uint16(pauseType)
    try:
        mzdGetLPAdvertisedPause(pDev, mdioPort, host_or_line, laneOffset, pauseType_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"pauseType = {pauseType_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdGetTxRxPauseResolution")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    pauseResolved = MZD_BOOL.MZD_FALSE.value
    pauseResolved_p = MZD_BOOL(pauseResolved)
    tx_pause_enabled = MZD_BOOL.MZD_FALSE.value
    tx_pause_enabled_p = MZD_BOOL(tx_pause_enabled)
    rx_pause_enabled = MZD_BOOL.MZD_FALSE.value
    rx_pause_enabled_p = MZD_BOOL(rx_pause_enabled)
    try:
        mzdGetTxRxPauseResolution(pDev, mdioPort, host_or_line, laneOffset, pauseResolved_p, tx_pause_enabled_p, rx_pause_enabled_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"pauseResolved = {pauseResolved_p.value}")
    logging.debug(f"tx_pause_enabled = {tx_pause_enabled_p.value}")
    logging.debug(f"rx_pause_enabled = {rx_pause_enabled_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdCheckPCSLinkStatus")
    mdioPort = 1
    laneOffset = 1
    currentStatus = 1
    currentStatus_p = c_uint16(currentStatus)
    latchedStatus = 1
    latchedStatus_p = c_uint16(latchedStatus)
    statusDetail = MZD_PCS_LINK_STATUS(0, 0, 0, 0)
    statusDetail_p = byref(statusDetail)
    try:
        mzdCheckPCSLinkStatus(pDev, mdioPort, laneOffset, currentStatus_p, latchedStatus_p, statusDetail_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"currentStatus = {currentStatus_p.value}")
    logging.debug(f"latchedStatus = {latchedStatus_p.value}")
    logging.debug(f"statusDetail = {MZD_PCS_LINK_STATUS.hostCurrent}")
    logging.debug(f"statusDetail = {MZD_PCS_LINK_STATUS.hostLatched}")
    logging.debug(f"statusDetail = {MZD_PCS_LINK_STATUS.lineCurrent}")
    logging.debug(f"statusDetail = {MZD_PCS_LINK_STATUS.lineLatched}")
    logging.info("\n")

    logging.info("Function name : mzdGetDetailedLinkStatus")
    mdioPort = 1
    laneOffset = 1
    host_or_line = 1
    currStat = 1
    currStat_p = c_uint16(currStat)
    latchStat = 1
    latchStat_p = c_uint16(latchStat)
    try:
        mzdGetDetailedLinkStatus(pDev, mdioPort, laneOffset, host_or_line, currStat_p, latchStat_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"currStat = {currStat_p.value}")
    logging.debug(f"latchStat = {latchStat_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdGetPcsFaultStatus")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    currentTxFaultStatus = 1
    currentTxFaultStatus_p = c_uint16(currentTxFaultStatus)
    currentRxFaultStatus = 1
    currentRxFaultStatus_p = c_uint16(currentRxFaultStatus)
    latchedTxFaultStatus = 1
    latchedTxFaultStatus_p = c_uint16(latchedTxFaultStatus)
    latchedRxFaultStatus = 1
    latchedRxFaultStatus_p = c_uint16(latchedRxFaultStatus)
    try:
        mzdGetPcsFaultStatus(pDev, mdioPort, host_or_line, laneOffset, currentTxFaultStatus_p, currentRxFaultStatus_p, latchedTxFaultStatus_p, latchedRxFaultStatus_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"currentTxFaultStatus = {currentTxFaultStatus_p.value}")
    logging.debug(f"currentRxFaultStatus = {currentRxFaultStatus_p.value}")
    logging.debug(f"latchedTxFaultStatus = {latchedTxFaultStatus_p.value}")
    logging.debug(f"latchedRxFaultStatus = {latchedRxFaultStatus_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdLaneSoftReset")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    timeoutMs = 1
    try:
        mzdLaneSoftReset(pDev, mdioPort, host_or_line, laneOffset, timeoutMs)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"timeoutMs = {timeoutMs}")
    logging.info("\n")

    logging.info("Function name : mzdSetDPFaultConfig")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    datapathMode = 1
    txType = 1
    rxType = 1
    try:
        mzdSetDPFaultConfig(pDev, mdioPort, host_or_line, laneOffset, datapathMode, txType, rxType)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"datapathMode = {datapathMode}")
    logging.debug(f"txType = {txType}")
    logging.debug(f"rxType = {rxType}")
    logging.info("\n")

    logging.info("Function name : mzdGetDPFaultConfig")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    datapathMode = 1
    datapathMode_p = c_uint16(datapathMode)
    txType = 1
    txType_p = c_uint16(txType)
    rxType = 1
    rxType_p = c_uint16(rxType)
    try:
        mzdGetDPFaultConfig(pDev, mdioPort, host_or_line, laneOffset, datapathMode_p, txType_p, rxType_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"datapathMode = {datapathMode_p.value}")
    logging.debug(f"txType = {txType_p.value}")
    logging.debug(f"rxType = {rxType_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdSetSerdesMux")
    host_or_line = 1
    serdesMux = 1
    serdesMux_p = c_uint8(serdesMux)
    try:
        mzdSetSerdesMux(pDev, host_or_line, serdesMux_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"serdesMux = {serdesMux_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdGetSerdesMux")
    host_or_line = 1
    serdesMux = 1
    serdesMux_p = c_uint8(serdesMux)
    try:
        mzdGetSerdesMux(pDev, host_or_line, serdesMux_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"serdesMux = {serdesMux_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdGetLaneRxTrainingState")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    rxTraining = MZD_BOOL.MZD_FALSE.value
    rxTraining_p = MZD_BOOL(rxTraining)
    try:
        mzdGetLaneRxTrainingState(pDev, mdioPort, host_or_line, laneOffset, rxTraining_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"rxTraining = {rxTraining_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdGetChipRevision")
    mdioPort = 1
    deviceId = MZD_DEVICE_ID.MZD_DEV_X7121M.value
    deviceId_p = MZD_DEVICE_ID(deviceId)
    try:
        mzdGetChipRevision(pDev, mdioPort, deviceId_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"deviceId = {deviceId_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdDevicePortCount")
    mdioPort = 1
    portCount = 1
    portCount_p = c_uint16(portCount)
    try:
        mzdDevicePortCount(pDev, mdioPort, portCount_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"portCount = {portCount_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdGetChipFWRevision")
    major = 1
    major_p = c_uint16(major)
    minor = 1
    minor_p = c_uint16(minor)
    patch = 1
    patch_p = c_uint16(patch)
    build = 1
    build_p = c_uint16(build)
    try:
        mzdGetChipFWRevision(pDev, major_p, minor_p, patch_p, build_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"major = {major_p.value}")
    logging.debug(f"minor = {minor_p.value}")
    logging.debug(f"patch = {patch_p.value}")
    logging.debug(f"build = {build_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdGetSerdesFWRevision")
    major = 1
    major_p = c_uint8(major)
    minor = 1
    minor_p = c_uint8(minor)
    patch = 1
    patch_p = c_uint8(patch)
    build = 1
    build_p = c_uint8(build)
    try:
        mzdGetSerdesFWRevision(pDev, major_p, minor_p, patch_p, build_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"major = {major_p.value}")
    logging.debug(f"minor = {minor_p.value}")
    logging.debug(f"patch = {patch_p.value}")
    logging.debug(f"build = {build_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdGetSerdesFWRevisionAll")
    majorMZD_NUM_INTERFACEMZD_MAX_PORTS = 1
    majorMZD_NUM_INTERFACEMZD_MAX_PORTS_p = c_uint8(majorMZD_NUM_INTERFACEMZD_MAX_PORTS)
    minorMZD_NUM_INTERFACEMZD_MAX_PORTS = 1
    minorMZD_NUM_INTERFACEMZD_MAX_PORTS_p = c_uint8(minorMZD_NUM_INTERFACEMZD_MAX_PORTS)
    patchMZD_NUM_INTERFACEMZD_MAX_PORTS = 1
    patchMZD_NUM_INTERFACEMZD_MAX_PORTS_p = c_uint8(patchMZD_NUM_INTERFACEMZD_MAX_PORTS)
    buildMZD_NUM_INTERFACEMZD_MAX_PORTS = 1
    buildMZD_NUM_INTERFACEMZD_MAX_PORTS_p = c_uint8(buildMZD_NUM_INTERFACEMZD_MAX_PORTS)
    try:
        mzdGetSerdesFWRevisionAll(pDev, majorMZD_NUM_INTERFACEMZD_MAX_PORTS_p, minorMZD_NUM_INTERFACEMZD_MAX_PORTS_p, patchMZD_NUM_INTERFACEMZD_MAX_PORTS_p, buildMZD_NUM_INTERFACEMZD_MAX_PORTS_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"majorMZD_NUM_INTERFACEMZD_MAX_PORTS = {majorMZD_NUM_INTERFACEMZD_MAX_PORTS_p.value}")
    logging.debug(f"minorMZD_NUM_INTERFACEMZD_MAX_PORTS = {minorMZD_NUM_INTERFACEMZD_MAX_PORTS_p.value}")
    logging.debug(f"patchMZD_NUM_INTERFACEMZD_MAX_PORTS = {patchMZD_NUM_INTERFACEMZD_MAX_PORTS_p.value}")
    logging.debug(f"buildMZD_NUM_INTERFACEMZD_MAX_PORTS = {buildMZD_NUM_INTERFACEMZD_MAX_PORTS_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdGetFirmwareLoadStatus")
    loadStatus = MZD_FIRMWARE_STATUS.MZD_FIRMWARE_STATUS_UNKNOWN.value
    loadStatus_p = MZD_FIRMWARE_STATUS(loadStatus)
    try:
        mzdGetFirmwareLoadStatus(pDev, loadStatus_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"loadStatus = {loadStatus_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdGetSerdesSignalDetectAndDspLock")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    signalDetect = 1
    signalDetect_p = c_uint16(signalDetect)
    dspLock = 1
    dspLock_p = c_uint16(dspLock)
    try:
        mzdGetSerdesSignalDetectAndDspLock(pDev, mdioPort, host_or_line, laneOffset, signalDetect_p, dspLock_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"signalDetect = {signalDetect_p.value}")
    logging.debug(f"dspLock = {dspLock_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdSetPCSLineLoopback")
    mdioPort = 1
    laneOffset = 1
    loopback_type = MZD_PCS_MODE_LOOPBACK.MZD_PCS_SHALLOW_LOOPBACK.value
    enable = 1
    try:
        mzdSetPCSLineLoopback(pDev, mdioPort, laneOffset, loopback_type, enable)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"loopback_type = {loopback_type}")
    logging.debug(f"enable = {enable}")
    logging.info("\n")

    logging.info("Function name : mzdSetPCSHostLoopback")
    mdioPort = 1
    laneOffset = 1
    loopback_type = MZD_PCS_MODE_LOOPBACK.MZD_PCS_SHALLOW_LOOPBACK.value
    loopbackState = 1
    try:
        mzdSetPCSHostLoopback(pDev, mdioPort, laneOffset, loopback_type, loopbackState)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"loopback_type = {loopback_type}")
    logging.debug(f"loopbackState = {loopbackState}")
    logging.info("\n")

    logging.info("Function name : mzdHmuxSetPCSLineDeepLoopback")
    hostPort = 1
    hostLaneOffset = 1
    loopback_type = MZD_PCS_MODE_LOOPBACK.MZD_PCS_SHALLOW_LOOPBACK.value
    loopbackState = 1
    try:
        mzdHmuxSetPCSLineDeepLoopback(pDev, hostPort, hostLaneOffset, loopback_type, loopbackState)
    except Exception:
        traceback.print_exc()
    logging.debug(f"hostPort = {hostPort}")
    logging.debug(f"hostLaneOffset = {hostLaneOffset}")
    logging.debug(f"loopback_type = {loopback_type}")
    logging.debug(f"loopbackState = {loopbackState}")
    logging.info("\n")

    logging.info("Function name : mzdHmuxSetPCSHostDeepLoopback")
    linePort = 1
    lineLaneOffset = 1
    loopback_type = MZD_PCS_MODE_LOOPBACK.MZD_PCS_SHALLOW_LOOPBACK.value
    loopbackState = 1
    try:
        mzdHmuxSetPCSHostDeepLoopback(pDev, linePort, lineLaneOffset, loopback_type, loopbackState)
    except Exception:
        traceback.print_exc()
    logging.debug(f"linePort = {linePort}")
    logging.debug(f"lineLaneOffset = {lineLaneOffset}")
    logging.debug(f"loopback_type = {loopback_type}")
    logging.debug(f"loopbackState = {loopbackState}")
    logging.info("\n")

    logging.info("Function name : mzdSetSerdesLaneLoopback")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    loopbackState = 1
    swReset = MZD_BOOL.MZD_FALSE.value
    try:
        mzdSetSerdesLaneLoopback(pDev, mdioPort, host_or_line, laneOffset, loopbackState, swReset)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"loopbackState = {loopbackState}")
    logging.debug(f"swReset = {swReset}")
    logging.info("\n")

    logging.info("Function name : mzdGetSerdesLaneLoopback")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    loopbackState = 1
    loopbackState_p = c_uint16(loopbackState)
    try:
        mzdGetSerdesLaneLoopback(pDev, mdioPort, host_or_line, laneOffset, loopbackState_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"loopbackState = {loopbackState_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdConfigurePktGeneratorChecker")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    readToClear = MZD_BOOL.MZD_FALSE.value
    dontuseSFDinChecker = MZD_BOOL.MZD_FALSE.value
    pktPatternControl = 1
    generateCRCoff = MZD_BOOL.MZD_FALSE.value
    initialPayload = 1
    frameLengthControl = 1
    numPktsToSend = 1
    randomIPG = MZD_BOOL.MZD_FALSE.value
    ipgDuration = 1
    try:
        mzdConfigurePktGeneratorChecker(pDev, mdioPort, host_or_line, laneOffset, readToClear, dontuseSFDinChecker, pktPatternControl, generateCRCoff, initialPayload, frameLengthControl, numPktsToSend, randomIPG, ipgDuration)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"readToClear = {readToClear}")
    logging.debug(f"dontuseSFDinChecker = {dontuseSFDinChecker}")
    logging.debug(f"pktPatternControl = {pktPatternControl}")
    logging.debug(f"generateCRCoff = {generateCRCoff}")
    logging.debug(f"initialPayload = {initialPayload}")
    logging.debug(f"frameLengthControl = {frameLengthControl}")
    logging.debug(f"numPktsToSend = {numPktsToSend}")
    logging.debug(f"randomIPG = {randomIPG}")
    logging.debug(f"ipgDuration = {ipgDuration}")
    logging.info("\n")

    logging.info("Function name : mzdEnablePktGeneratorChecker")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    enableGenerator = MZD_BOOL.MZD_FALSE.value
    enableChecker = MZD_BOOL.MZD_FALSE.value
    try:
        mzdEnablePktGeneratorChecker(pDev, mdioPort, host_or_line, laneOffset, enableGenerator, enableChecker)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"enableGenerator = {enableGenerator}")
    logging.debug(f"enableChecker = {enableChecker}")
    logging.info("\n")

    logging.info("Function name : mzdStartStopPktGenTraffic")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    numPktsToSend = MZD_BOOL.MZD_FALSE.value
    try:
        mzdStartStopPktGenTraffic(pDev, mdioPort, host_or_line, laneOffset, numPktsToSend)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"numPktsToSend = {numPktsToSend}")
    logging.info("\n")

    logging.info("Function name : mzdPktGeneratorCounterReset")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    try:
        mzdPktGeneratorCounterReset(pDev, mdioPort, host_or_line, laneOffset)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.info("\n")

    logging.info("Function name : mzdPktGeneratorGetCounter")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    pktCntType = MZD_PKT_COUNT_TYPE.MZD_PKT_GET_TX.value
    packetCount = 1
    packetCount_p = c_uint64(packetCount)
    byteCount = 1
    byteCount_p = c_uint64(byteCount)
    try:
        mzdPktGeneratorGetCounter(pDev, mdioPort, host_or_line, laneOffset, pktCntType, packetCount_p, byteCount_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"pktCntType = {pktCntType}")
    logging.debug(f"packetCount = {packetCount_p.value}")
    logging.debug(f"byteCount = {byteCount_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdSetPRBSPattern")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    pattSel = MZD_PRBS_SELECTOR_TYPE.MZD_PRBS31.value
    pattSubSel = MZD_PATTERN_AB_SELECTOR_TYPE.MZD_PRBS_NONE.value
    try:
        mzdSetPRBSPattern(pDev, mdioPort, host_or_line, laneOffset, pattSel, pattSubSel)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"pattSel = {pattSel}")
    logging.debug(f"pattSubSel = {pattSubSel}")
    logging.info("\n")

    logging.info("Function name : mzdPRBSPatternOption")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    patternOption = 1
    try:
        mzdPRBSPatternOption(pDev, mdioPort, host_or_line, laneOffset, patternOption)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"patternOption = {patternOption}")
    logging.info("\n")

    logging.info("Function name : mzdSetPRBSEnableTxRx")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    txEnable = 1
    rxEnable = 1
    pattSel = MZD_PRBS_SELECTOR_TYPE.MZD_PRBS31.value
    try:
        mzdSetPRBSEnableTxRx(pDev, mdioPort, host_or_line, laneOffset, txEnable, rxEnable, pattSel)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"txEnable = {txEnable}")
    logging.debug(f"rxEnable = {rxEnable}")
    logging.debug(f"pattSel = {pattSel}")
    logging.info("\n")

    logging.info("Function name : mzdPRBSCounterReset")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    try:
        mzdPRBSCounterReset(pDev, mdioPort, host_or_line, laneOffset)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.info("\n")

    logging.info("Function name : mzdSetPRBSWaitForLock")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    disableWaitforLock = 1
    try:
        mzdSetPRBSWaitForLock(pDev, mdioPort, host_or_line, laneOffset, disableWaitforLock)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"disableWaitforLock = {disableWaitforLock}")
    logging.info("\n")

    logging.info("Function name : mzdGetPRBSWaitForLock")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    disableWaitforLock = 1
    disableWaitforLock_p = c_uint16(disableWaitforLock)
    try:
        mzdGetPRBSWaitForLock(pDev, mdioPort, host_or_line, laneOffset, disableWaitforLock_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"disableWaitforLock = {disableWaitforLock_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdSetPRBSClearOnRead")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    enableReadClear = 1
    try:
        mzdSetPRBSClearOnRead(pDev, mdioPort, host_or_line, laneOffset, enableReadClear)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"enableReadClear = {enableReadClear}")
    logging.info("\n")

    logging.info("Function name : mzdGetPRBSClearOnRead")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    enableReadClear = 1
    enableReadClear_p = c_uint16(enableReadClear)
    try:
        mzdGetPRBSClearOnRead(pDev, mdioPort, host_or_line, laneOffset, enableReadClear_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"enableReadClear = {enableReadClear_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdGetPRBSLocked")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    prbsLocked = MZD_BOOL.MZD_FALSE.value
    prbsLocked_p = MZD_BOOL(prbsLocked)
    try:
        mzdGetPRBSLocked(pDev, mdioPort, host_or_line, laneOffset, prbsLocked_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"prbsLocked = {prbsLocked_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdGetPRBSCounts")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    pattSel = MZD_PRBS_SELECTOR_TYPE.MZD_PRBS31.value
    txBitCount = 1
    txBitCount_p = c_uint64(txBitCount)
    rxBitCount = 1
    rxBitCount_p = c_uint64(rxBitCount)
    rxBitErrorCount = 1
    rxBitErrorCount_p = c_uint64(rxBitErrorCount)
    try:
        mzdGetPRBSCounts(pDev, mdioPort, host_or_line, laneOffset, pattSel, txBitCount_p, rxBitCount_p, rxBitErrorCount_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"pattSel = {pattSel}")
    logging.debug(f"txBitCount = {txBitCount_p.value}")
    logging.debug(f"rxBitCount = {rxBitCount_p.value}")
    logging.debug(f"rxBitErrorCount = {rxBitErrorCount_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdSetTxRxPolarity")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    txPolarity = 1
    rxPolarity = 1
    try:
        mzdSetTxRxPolarity(pDev, mdioPort, host_or_line, laneOffset, txPolarity, rxPolarity)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"txPolarity = {txPolarity}")
    logging.debug(f"rxPolarity = {rxPolarity}")
    logging.info("\n")

    logging.info("Function name : mzdGetTxRxPolarity")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    txPolarity = 1
    txPolarity_p = c_uint8(txPolarity)
    rxPolarity = 1
    rxPolarity_p = c_uint8(rxPolarity)
    try:
        mzdGetTxRxPolarity(pDev, mdioPort, host_or_line, laneOffset, txPolarity_p, rxPolarity_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"txPolarity = {txPolarity_p.value}")
    logging.debug(f"rxPolarity = {rxPolarity_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdSetTxFFE")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    txEqParamType = E_N5C112GX4_TXEQ_PARAM.N5C112GX4_TXEQ_EM_PRE3_CTRL.value
    paramValue = 1
    try:
        mzdSetTxFFE(pDev, mdioPort, host_or_line, laneOffset, txEqParamType, paramValue)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"txEqParamType = {txEqParamType}")
    logging.debug(f"paramValue = {paramValue}")
    logging.info("\n")

    logging.info("Function name : mzdGetTxFFE")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    txEqParamType = E_N5C112GX4_TXEQ_PARAM.N5C112GX4_TXEQ_EM_PRE3_CTRL.value
    paramValue = 1
    paramValue_p = c_uint32(paramValue)
    try:
        mzdGetTxFFE(pDev, mdioPort, host_or_line, laneOffset, txEqParamType, paramValue_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"txEqParamType = {txEqParamType}")
    logging.debug(f"paramValue = {paramValue_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdDiagStateDump")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    stateDumpOptions = 1
    apiVersion = (c_uint8 * 3)()
    apiVersion_init = [0] * 3
    for idx, value in enumerate(apiVersion_init):
        apiVersion[idx] = value
    fwVersion = (c_uint8 * 4)()
    fwVersion_init = [0] * 4
    for idx, value in enumerate(fwVersion_init):
        fwVersion[idx] = value
    serdesRevision = (c_uint8 * 4)()
    serdesRevision_init = [0] * 4
    for idx, value in enumerate(serdesRevision_init):
        serdesRevision[idx] = value
    statusPCSReg = (c_uint16 * 2)()
    statusPCSReg_init = [0] * 2
    for idx, value in enumerate(statusPCSReg_init):
        statusPCSReg[idx] = value
    ctrlVal = (c_uint32 * 64)()
    ctrlVal_init = [0] * 64
    for idx, value in enumerate(ctrlVal_init):
        ctrlVal[idx] = value
    pStateDumpInfo = MZD_STATE_DUMP(0, apiVersion, fwVersion, serdesRevision, 0, 0, statusPCSReg, 0, 0, 0, ctrlVal)
    pStateDumpInfo_p = byref(pStateDumpInfo)
    try:
        mzdDiagStateDump(pDev, mdioPort, host_or_line, laneOffset, stateDumpOptions, pStateDumpInfo_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"stateDumpOptions = {stateDumpOptions}")
    logging.debug(f"pStateDumpInfo = {MZD_STATE_DUMP.devStuct}")
    logging.debug(f"pStateDumpInfo = {MZD_STATE_DUMP.coreTemperature}")
    logging.debug(f"pStateDumpInfo = {MZD_STATE_DUMP.cntlPCSReg}")
    logging.debug(f"pStateDumpInfo = {MZD_STATE_DUMP.modeSelectReg}")
    logging.debug(f"pStateDumpInfo = {MZD_STATE_DUMP.ffe}")
    logging.debug(f"pStateDumpInfo = {MZD_STATE_DUMP.txFFE}")
    logging.info("\n")

    logging.info("Function name : mzdSetRsFecControl")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    bypassIndicationEnable = 1
    bypassCorrectionEnable = 1
    try:
        mzdSetRsFecControl(pDev, mdioPort, host_or_line, laneOffset, bypassIndicationEnable, bypassCorrectionEnable)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"bypassIndicationEnable = {bypassIndicationEnable}")
    logging.debug(f"bypassCorrectionEnable = {bypassCorrectionEnable}")
    logging.info("\n")

    logging.info("Function name : mzdGetRsFecControl")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    bypassIndicationEnable = 1
    bypassIndicationEnable_p = c_uint16(bypassIndicationEnable)
    bypassCorrectionEnable = 1
    bypassCorrectionEnable_p = c_uint16(bypassCorrectionEnable)
    try:
        mzdGetRsFecControl(pDev, mdioPort, host_or_line, laneOffset, bypassIndicationEnable_p, bypassCorrectionEnable_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"bypassIndicationEnable = {bypassIndicationEnable_p.value}")
    logging.debug(f"bypassCorrectionEnable = {bypassCorrectionEnable_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdGetRsFecStatus")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    pcsLaneAlignment = 1
    pcsLaneAlignment_p = c_uint16(pcsLaneAlignment)
    fecLaneAlignment = 1
    fecLaneAlignment_p = c_uint16(fecLaneAlignment)
    rsFecLaneAMLock = 1
    rsFecLaneAMLock_p = c_uint16(rsFecLaneAMLock)
    latchedRsFecHighErr = 1
    latchedRsFecHighErr_p = c_uint16(latchedRsFecHighErr)
    currRsFecHighErr = 1
    currRsFecHighErr_p = c_uint16(currRsFecHighErr)
    try:
        mzdGetRsFecStatus(pDev, mdioPort, host_or_line, laneOffset, pcsLaneAlignment_p, fecLaneAlignment_p, rsFecLaneAMLock_p, latchedRsFecHighErr_p, currRsFecHighErr_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"pcsLaneAlignment = {pcsLaneAlignment_p.value}")
    logging.debug(f"fecLaneAlignment = {fecLaneAlignment_p.value}")
    logging.debug(f"rsFecLaneAMLock = {rsFecLaneAMLock_p.value}")
    logging.debug(f"latchedRsFecHighErr = {latchedRsFecHighErr_p.value}")
    logging.debug(f"currRsFecHighErr = {currRsFecHighErr_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdGetRsFecPCSAlignmentStatus")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    pcs_lane = 1
    blockLocked = 1
    blockLocked_p = c_uint16(blockLocked)
    laneAligned = 1
    laneAligned_p = c_uint16(laneAligned)
    try:
        mzdGetRsFecPCSAlignmentStatus(pDev, mdioPort, host_or_line, laneOffset, pcs_lane, blockLocked_p, laneAligned_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"pcs_lane = {pcs_lane}")
    logging.debug(f"blockLocked = {blockLocked_p.value}")
    logging.debug(f"laneAligned = {laneAligned_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdGetRsFecPMALaneMapping")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    mappingMZD_NUM_LANES = 1
    mappingMZD_NUM_LANES_p = c_uint16(mappingMZD_NUM_LANES)
    try:
        mzdGetRsFecPMALaneMapping(pDev, mdioPort, host_or_line, laneOffset, mappingMZD_NUM_LANES_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"mappingMZD_NUM_LANES = {mappingMZD_NUM_LANES_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdGetRxPCSLaneMapping")
    mdioPort = 1
    host_or_line = 1
    lane_offset = 1
    interface_lane = 1
    pcs_lane = 1
    pcs_lane_p = c_uint16(pcs_lane)
    try:
        mzdGetRxPCSLaneMapping(pDev, mdioPort, host_or_line, lane_offset, interface_lane, pcs_lane_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"lane_offset = {lane_offset}")
    logging.debug(f"interface_lane = {interface_lane}")
    logging.debug(f"pcs_lane = {pcs_lane_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdGetRsFecCorrectedCwCntr")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    codeWordCounter = 1
    codeWordCounter_p = c_uint32(codeWordCounter)
    try:
        mzdGetRsFecCorrectedCwCntr(pDev, mdioPort, host_or_line, laneOffset, codeWordCounter_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"codeWordCounter = {codeWordCounter_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdGetRsFecUnCorrectedCwCntr")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    codeWordCounter = 1
    codeWordCounter_p = c_uint32(codeWordCounter)
    try:
        mzdGetRsFecUnCorrectedCwCntr(pDev, mdioPort, host_or_line, laneOffset, codeWordCounter_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"codeWordCounter = {codeWordCounter_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdGetRsFecSymbolErrorCntr")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    fecLane = 1
    errorCounter = 1
    errorCounter_p = c_uint32(errorCounter)
    try:
        mzdGetRsFecSymbolErrorCntr(pDev, mdioPort, host_or_line, laneOffset, fecLane, errorCounter_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"fecLane = {fecLane}")
    logging.debug(f"errorCounter = {errorCounter_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdGetRxPcsBipErrorCntr")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    pcs_lane = 1
    errorCounter = 1
    errorCounter_p = c_uint16(errorCounter)
    try:
        mzdGetRxPcsBipErrorCntr(pDev, mdioPort, host_or_line, laneOffset, pcs_lane, errorCounter_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"pcs_lane = {pcs_lane}")
    logging.debug(f"errorCounter = {errorCounter_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdSetRsFecSERControl")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    degradedSEREnable = 1
    bypassIndicationEnable = 1
    try:
        mzdSetRsFecSERControl(pDev, mdioPort, host_or_line, laneOffset, degradedSEREnable, bypassIndicationEnable)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"degradedSEREnable = {degradedSEREnable}")
    logging.debug(f"bypassIndicationEnable = {bypassIndicationEnable}")
    logging.info("\n")

    logging.info("Function name : mzdGetRsFecSERControl")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    degradedSEREnable = 1
    degradedSEREnable_p = c_uint16(degradedSEREnable)
    bypassIndicationEnable = 1
    bypassIndicationEnable_p = c_uint16(bypassIndicationEnable)
    try:
        mzdGetRsFecSERControl(pDev, mdioPort, host_or_line, laneOffset, degradedSEREnable_p, bypassIndicationEnable_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"degradedSEREnable = {degradedSEREnable_p.value}")
    logging.debug(f"bypassIndicationEnable = {bypassIndicationEnable_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdSetRsFecSERThresholds")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    serActivateThreshold = 1
    serDeactivateThreshold = 1
    serInterval = 1
    try:
        mzdSetRsFecSERThresholds(pDev, mdioPort, host_or_line, laneOffset, serActivateThreshold, serDeactivateThreshold, serInterval)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"serActivateThreshold = {serActivateThreshold}")
    logging.debug(f"serDeactivateThreshold = {serDeactivateThreshold}")
    logging.debug(f"serInterval = {serInterval}")
    logging.info("\n")

    logging.info("Function name : mzdGetRsFecSERThresholds")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    serActivateThreshold = 1
    serActivateThreshold_p = c_uint32(serActivateThreshold)
    serDeactivateThreshold = 1
    serDeactivateThreshold_p = c_uint32(serDeactivateThreshold)
    serInterval = 1
    serInterval_p = c_uint32(serInterval)
    try:
        mzdGetRsFecSERThresholds(pDev, mdioPort, host_or_line, laneOffset, serActivateThreshold_p, serDeactivateThreshold_p, serInterval_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"serActivateThreshold = {serActivateThreshold_p.value}")
    logging.debug(f"serDeactivateThreshold = {serDeactivateThreshold_p.value}")
    logging.debug(f"serInterval = {serInterval_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdGetRsFecDegradedSERStatus")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    localDegradedSerRcvd = 1
    localDegradedSerRcvd_p = c_uint16(localDegradedSerRcvd)
    remoteDegradedSerRcvd = 1
    remoteDegradedSerRcvd_p = c_uint16(remoteDegradedSerRcvd)
    serDegraded = 1
    serDegraded_p = c_uint16(serDegraded)
    try:
        mzdGetRsFecDegradedSERStatus(pDev, mdioPort, host_or_line, laneOffset, localDegradedSerRcvd_p, remoteDegradedSerRcvd_p, serDegraded_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"localDegradedSerRcvd = {localDegradedSerRcvd_p.value}")
    logging.debug(f"remoteDegradedSerRcvd = {remoteDegradedSerRcvd_p.value}")
    logging.debug(f"serDegraded = {serDegraded_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdSetKrFecControl")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    bypassIndicationEnable = 1
    try:
        mzdSetKrFecControl(pDev, mdioPort, host_or_line, laneOffset, bypassIndicationEnable)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"bypassIndicationEnable = {bypassIndicationEnable}")
    logging.info("\n")

    logging.info("Function name : mzdGetKrFecControl")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    bypassIndicationEnable = 1
    bypassIndicationEnable_p = c_uint16(bypassIndicationEnable)
    try:
        mzdGetKrFecControl(pDev, mdioPort, host_or_line, laneOffset, bypassIndicationEnable_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"bypassIndicationEnable = {bypassIndicationEnable_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdGetKrFecAbility")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    krFecAbility = 1
    krFecAbility_p = c_uint16(krFecAbility)
    errIndicationAbility = 1
    errIndicationAbility_p = c_uint16(errIndicationAbility)
    try:
        mzdGetKrFecAbility(pDev, mdioPort, host_or_line, laneOffset, krFecAbility_p, errIndicationAbility_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"krFecAbility = {krFecAbility_p.value}")
    logging.debug(f"errIndicationAbility = {errIndicationAbility_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdGetKrFecCorrectedBlkCntr")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    blockCounter = 1
    blockCounter_p = c_uint32(blockCounter)
    try:
        mzdGetKrFecCorrectedBlkCntr(pDev, mdioPort, host_or_line, laneOffset, blockCounter_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"blockCounter = {blockCounter_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdGetKrFecUnCorrectedBlkCntr")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    blockCounter = 1
    blockCounter_p = c_uint32(blockCounter)
    try:
        mzdGetKrFecUnCorrectedBlkCntr(pDev, mdioPort, host_or_line, laneOffset, blockCounter_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"blockCounter = {blockCounter_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdFECCounterEnable")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    enable = 1
    readToClear = MZD_BOOL.MZD_FALSE.value
    try:
        mzdFECCounterEnable(pDev, mdioPort, host_or_line, laneOffset, enable, readToClear)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"enable = {enable}")
    logging.debug(f"readToClear = {readToClear}")
    logging.info("\n")

    logging.info("Function name : mzdFECCounterSnapshot")
    mdioPort = 1
    host_or_line = 1
    try:
        mzdFECCounterSnapshot(pDev, mdioPort, host_or_line)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.info("\n")

    logging.info("Function name : mzdFECCounterReset")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    try:
        mzdFECCounterReset(pDev, mdioPort, host_or_line, laneOffset)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.info("\n")

    logging.info("Function name : mzdFECReadCodewordCounters")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    numCodeWords = 1
    numCodeWords_p = c_uint64(numCodeWords)
    numUncorrectable = 1
    numUncorrectable_p = c_uint32(numUncorrectable)
    numCorrected = 1
    numCorrected_p = c_uint32(numCorrected)
    try:
        mzdFECReadCodewordCounters(pDev, mdioPort, host_or_line, laneOffset, numCodeWords_p, numUncorrectable_p, numCorrected_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"numCodeWords = {numCodeWords_p.value}")
    logging.debug(f"numUncorrectable = {numUncorrectable_p.value}")
    logging.debug(f"numCorrected = {numCorrected_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdFECReadBurstSymbolErrorCtrs")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    burst2Symbols = 1
    burst2Symbols_p = c_uint32(burst2Symbols)
    burst3Symbols = 1
    burst3Symbols_p = c_uint16(burst3Symbols)
    burst4Symbols = 1
    burst4Symbols_p = c_uint16(burst4Symbols)
    burst5Symbols = 1
    burst5Symbols_p = c_uint16(burst5Symbols)
    burst6Symbols = 1
    burst6Symbols_p = c_uint16(burst6Symbols)
    try:
        mzdFECReadBurstSymbolErrorCtrs(pDev, mdioPort, host_or_line, laneOffset, burst2Symbols_p, burst3Symbols_p, burst4Symbols_p, burst5Symbols_p, burst6Symbols_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"burst2Symbols = {burst2Symbols_p.value}")
    logging.debug(f"burst3Symbols = {burst3Symbols_p.value}")
    logging.debug(f"burst4Symbols = {burst4Symbols_p.value}")
    logging.debug(f"burst5Symbols = {burst5Symbols_p.value}")
    logging.debug(f"burst6Symbols = {burst6Symbols_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdFECReadSymbolErrorCounters")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    symbolErrorCounters0to1 = 1
    symbolErrorCounters0to1_p = c_uint64(symbolErrorCounters0to1)
    symbolErrorCounters2to4 = 1
    symbolErrorCounters2to4_p = c_uint32(symbolErrorCounters2to4)
    symbolErrorCounters5to15 = 1
    symbolErrorCounters5to15_p = c_uint16(symbolErrorCounters5to15)
    try:
        mzdFECReadSymbolErrorCounters(pDev, mdioPort, host_or_line, laneOffset, symbolErrorCounters0to1_p, symbolErrorCounters2to4_p, symbolErrorCounters5to15_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"symbolErrorCounters0to1 = {symbolErrorCounters0to1_p.value}")
    logging.debug(f"symbolErrorCounters2to4 = {symbolErrorCounters2to4_p.value}")
    logging.debug(f"symbolErrorCounters5to15 = {symbolErrorCounters5to15_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdFirmwareDownload")
    fwImageData = 1
    fwImageData_p = c_uint8(fwImageData)
    fwImageSize = 1
    errCode = 1
    errCode_p = c_uint16(errCode)
    try:
        mzdFirmwareDownload(pDev, fwImageData_p, fwImageSize, errCode_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"fwImageData = {fwImageData_p.value}")
    logging.debug(f"fwImageSize = {fwImageSize}")
    logging.debug(f"errCode = {errCode_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdUpdateFlashImage")
    fwImageData = 1
    fwImageData_p = c_uint8(fwImageData)
    fwImageSize = 1
    slaveData = 1
    slaveData_p = c_uint8(slaveData)
    slaveSize = 1
    errCode = 1
    errCode_p = c_uint16(errCode)
    try:
        mzdUpdateFlashImage(pDev, fwImageData_p, fwImageSize, slaveData_p, slaveSize, errCode_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"fwImageData = {fwImageData_p.value}")
    logging.debug(f"fwImageSize = {fwImageSize}")
    logging.debug(f"slaveData = {slaveData_p.value}")
    logging.debug(f"slaveSize = {slaveSize}")
    logging.debug(f"errCode = {errCode_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdParallelFirmwareDownload")
    numPorts = 1
    fwImageData = 1
    fwImageData_p = c_uint8(fwImageData)
    fwImageSize = 1
    errCode = 1
    errCode_p = c_uint16(errCode)
    try:
        mzdParallelFirmwareDownload(pDev, numPorts, fwImageData_p, fwImageSize, pErrDev, errCode_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"numPorts = {numPorts}")
    logging.debug(f"fwImageData = {fwImageData_p.value}")
    logging.debug(f"fwImageSize = {fwImageSize}")
    logging.debug(f"errCode = {errCode_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdParallelUpdateFlashImage")
    numPorts = 1
    fwImageData = 1
    fwImageData_p = c_uint8(fwImageData)
    fwImageSize = 1
    slaveData = 1
    slaveData_p = c_uint8(slaveData)
    slaveSize = 1
    errCode = 1
    errCode_p = c_uint16(errCode)
    try:
        mzdParallelUpdateFlashImage(pDev, numPorts, fwImageData_p, fwImageSize, slaveData_p, slaveSize, pErrDev, errCode_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"numPorts = {numPorts}")
    logging.debug(f"fwImageData = {fwImageData_p.value}")
    logging.debug(f"fwImageSize = {fwImageSize}")
    logging.debug(f"slaveData = {slaveData_p.value}")
    logging.debug(f"slaveSize = {slaveSize}")
    logging.debug(f"errCode = {errCode_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdLoadFlashImageToRAM")
    errCode = 1
    errCode_p = c_uint16(errCode)
    try:
        mzdLoadFlashImageToRAM(pDev, errCode_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"errCode = {errCode_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdHwAPBusRead")
    regAPBAddr = 1
    data = 1
    data_p = c_uint32(data)
    try:
        mzdHwAPBusRead(pDev, regAPBAddr, data_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"regAPBAddr = {regAPBAddr}")
    logging.debug(f"data = {data_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdHwAPBusWrite")
    regAPBAddr = 1
    data = 1
    try:
        mzdHwAPBusWrite(pDev, regAPBAddr, data)
    except Exception:
        traceback.print_exc()
    logging.debug(f"regAPBAddr = {regAPBAddr}")
    logging.debug(f"data = {data}")
    logging.info("\n")

    logging.info("Function name : mzdHwAPBusWriteBlock")
    regAPBAddr = 1
    data = 1
    data_p = c_uint32(data)
    size = 1
    try:
        mzdHwAPBusWriteBlock(pDev, regAPBAddr, data_p, size)
    except Exception:
        traceback.print_exc()
    logging.debug(f"regAPBAddr = {regAPBAddr}")
    logging.debug(f"data = {data_p.value}")
    logging.debug(f"size = {size}")
    logging.info("\n")

    logging.info("Function name : mzdHwAPBusReadBlock")
    regAPBAddr = 1
    size = 1
    data = 1
    data_p = c_uint32(data)
    try:
        mzdHwAPBusReadBlock(pDev, regAPBAddr, size, data_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"regAPBAddr = {regAPBAddr}")
    logging.debug(f"size = {size}")
    logging.debug(f"data = {data_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdHwAPBusSetRegField")
    regAPBAddr = 1
    fieldOffset = 1
    fieldLength = 1
    data = 1
    try:
        mzdHwAPBusSetRegField(pDev, regAPBAddr, fieldOffset, fieldLength, data)
    except Exception:
        traceback.print_exc()
    logging.debug(f"regAPBAddr = {regAPBAddr}")
    logging.debug(f"fieldOffset = {fieldOffset}")
    logging.debug(f"fieldLength = {fieldLength}")
    logging.debug(f"data = {data}")
    logging.info("\n")

    logging.info("Function name : mzdHwAPBusGetRegField")
    regAPBAddr = 1
    fieldOffset = 1
    fieldLength = 1
    data = 1
    data_p = c_uint32(data)
    try:
        mzdHwAPBusGetRegField(pDev, regAPBAddr, fieldOffset, fieldLength, data_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"regAPBAddr = {regAPBAddr}")
    logging.debug(f"fieldOffset = {fieldOffset}")
    logging.debug(f"fieldLength = {fieldLength}")
    logging.debug(f"data = {data_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdHwLockAPBSemaphore")
    semOption = 1
    try:
        mzdHwLockAPBSemaphore(pDev, semOption)
    except Exception:
        traceback.print_exc()
    logging.debug(f"semOption = {semOption}")
    logging.info("\n")

    logging.info("Function name : mzdHwReleaseAPBSemaphore")
    semOption = 1
    try:
        mzdHwReleaseAPBSemaphore(pDev, semOption)
    except Exception:
        traceback.print_exc()
    logging.debug(f"semOption = {semOption}")
    logging.info("\n")

    logging.info("Function name : mzdHwAPBSemaphoreConfig")
    semConfigOption = 1
    try:
        mzdHwAPBSemaphoreConfig(pDev, semConfigOption)
    except Exception:
        traceback.print_exc()
    logging.debug(f"semConfigOption = {semConfigOption}")
    logging.info("\n")

    logging.info("Function name : mzdHwXmdioWrite")
    mdioPort = 1
    dev = 1
    reg = 1
    value = 1
    try:
        mzdHwXmdioWrite(pDev, mdioPort, dev, reg, value)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"dev = {dev}")
    logging.debug(f"reg = {reg}")
    logging.debug(f"value = {value}")
    logging.info("\n")

    logging.info("Function name : mzdHwXmdioRead")
    mdioPort = 1
    dev = 1
    reg = 1
    data = 1
    data_p = c_uint16(data)
    try:
        mzdHwXmdioRead(pDev, mdioPort, dev, reg, data_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"dev = {dev}")
    logging.debug(f"reg = {reg}")
    logging.debug(f"data = {data_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdHwGetPhyRegField")
    mdioPort = 1
    dev = 1
    regAddr = 1
    fieldOffset = 1
    fieldLength = 1
    data = 1
    data_p = c_uint16(data)
    try:
        mzdHwGetPhyRegField(pDev, mdioPort, dev, regAddr, fieldOffset, fieldLength, data_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"dev = {dev}")
    logging.debug(f"regAddr = {regAddr}")
    logging.debug(f"fieldOffset = {fieldOffset}")
    logging.debug(f"fieldLength = {fieldLength}")
    logging.debug(f"data = {data_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdHwSetPhyRegField")
    mdioPort = 1
    dev = 1
    regAddr = 1
    fieldOffset = 1
    fieldLength = 1
    data = 1
    try:
        mzdHwSetPhyRegField(pDev, mdioPort, dev, regAddr, fieldOffset, fieldLength, data)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"dev = {dev}")
    logging.debug(f"regAddr = {regAddr}")
    logging.debug(f"fieldOffset = {fieldOffset}")
    logging.debug(f"fieldLength = {fieldLength}")
    logging.debug(f"data = {data}")
    logging.info("\n")

    logging.info("Function name : mzdHwGetRegFieldFromWord")
    regData = 1
    fieldOffset = 1
    fieldLength = 1
    data = 1
    data_p = c_uint16(data)
    try:
        mzdHwGetRegFieldFromWord(regData, fieldOffset, fieldLength, data_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"regData = {regData}")
    logging.debug(f"fieldOffset = {fieldOffset}")
    logging.debug(f"fieldLength = {fieldLength}")
    logging.debug(f"data = {data_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdHwSetRegFieldToWord")
    regData = 1
    bitFieldData = 1
    fieldOffset = 1
    fieldLength = 1
    data = 1
    data_p = c_uint16(data)
    try:
        mzdHwSetRegFieldToWord(regData, bitFieldData, fieldOffset, fieldLength, data_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"regData = {regData}")
    logging.debug(f"bitFieldData = {bitFieldData}")
    logging.debug(f"fieldOffset = {fieldOffset}")
    logging.debug(f"fieldLength = {fieldLength}")
    logging.debug(f"data = {data_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdHwWaitForRegFieldValue")
    mdioPort = 1
    dev = 1
    regAddr = 1
    fieldOffset = 1
    fieldLength = 1
    expectedValue = 1
    timeoutMs = 1
    try:
        mzdHwWaitForRegFieldValue(pDev, mdioPort, dev, regAddr, fieldOffset, fieldLength, expectedValue, timeoutMs)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"dev = {dev}")
    logging.debug(f"regAddr = {regAddr}")
    logging.debug(f"fieldOffset = {fieldOffset}")
    logging.debug(f"fieldLength = {fieldLength}")
    logging.debug(f"expectedValue = {expectedValue}")
    logging.debug(f"timeoutMs = {timeoutMs}")
    logging.info("\n")

    logging.info("Function name : mzdHwWaitForRegFieldValueList")
    mdioPort = 1
    dev = 1
    regAddr = 1
    fieldOffset = 1
    fieldLength = 1
    expectedValueList = 1
    expectedValueList_p = c_uint16(expectedValueList)
    numOfExpValue = 1
    timeoutMs = 1
    fieldValue = 1
    fieldValue_p = c_uint16(fieldValue)
    try:
        mzdHwWaitForRegFieldValueList(pDev, mdioPort, dev, regAddr, fieldOffset, fieldLength, expectedValueList_p, numOfExpValue, timeoutMs, fieldValue_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"dev = {dev}")
    logging.debug(f"regAddr = {regAddr}")
    logging.debug(f"fieldOffset = {fieldOffset}")
    logging.debug(f"fieldLength = {fieldLength}")
    logging.debug(f"expectedValueList = {expectedValueList_p.value}")
    logging.debug(f"numOfExpValue = {numOfExpValue}")
    logging.debug(f"timeoutMs = {timeoutMs}")
    logging.debug(f"fieldValue = {fieldValue_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdHwXmdioBlockWrite")
    mdioPort = 1
    dev = 1
    reg = 1
    data = 1
    data_p = c_uint8(data)
    dataSize = 1
    try:
        mzdHwXmdioBlockWrite(pDev, mdioPort, dev, reg, data_p, dataSize)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"dev = {dev}")
    logging.debug(f"reg = {reg}")
    logging.debug(f"data = {data_p.value}")
    logging.debug(f"dataSize = {dataSize}")
    logging.info("\n")

    logging.info("Function name : mzdWait")
    waitTime = 1
    try:
        mzdWait(pDev, waitTime)
    except Exception:
        traceback.print_exc()
    logging.debug(f"waitTime = {waitTime}")
    logging.info("\n")

    logging.info("Function name : mzdMacSecMappedDevAddr")
    deviceId = 1
    deviceNum = 1
    firstOffset = 1
    lastOffset = 1
    platfromFirstOffset = 1
    platfromFirstOffset_p = c_uint32(platfromFirstOffset)
    platfromLastOffset = 1
    platfromLastOffset_p = c_uint32(platfromLastOffset)
    try:
        mzdMacSecMappedDevAddr(deviceId, deviceNum, firstOffset, lastOffset, HostContext, platfromFirstOffset_p, platfromLastOffset_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"deviceId = {deviceId}")
    logging.debug(f"deviceNum = {deviceNum}")
    logging.debug(f"firstOffset = {firstOffset}")
    logging.debug(f"lastOffset = {lastOffset}")
    logging.debug(f"platfromFirstOffset = {platfromFirstOffset_p.value}")
    logging.debug(f"platfromLastOffset = {platfromLastOffset_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdSetMacSecDevInfo")
    macsecMapPort = 1
    macsecLane = 1
    try:
        mzdSetMacSecDevInfo(pDev, macsecMapPort, macsecLane)
    except Exception:
        traceback.print_exc()
    logging.debug(f"macsecMapPort = {macsecMapPort}")
    logging.debug(f"macsecLane = {macsecLane}")
    logging.info("\n")

    logging.info("Function name : mzdHwMacSecRegWrite")
    macsecMapPort = 1
    macsecAddr = 1
    data = 1
    try:
        mzdHwMacSecRegWrite(pDev, macsecMapPort, macsecAddr, data)
    except Exception:
        traceback.print_exc()
    logging.debug(f"macsecMapPort = {macsecMapPort}")
    logging.debug(f"macsecAddr = {macsecAddr}")
    logging.debug(f"data = {data}")
    logging.info("\n")

    logging.info("Function name : mzdHwMacSecRegRead")
    macsecMapPort = 1
    macsecAddr = 1
    data = 1
    data_p = c_uint32(data)
    try:
        mzdHwMacSecRegRead(pDev, macsecMapPort, macsecAddr, data_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"macsecMapPort = {macsecMapPort}")
    logging.debug(f"macsecAddr = {macsecAddr}")
    logging.debug(f"data = {data_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdHwSetMacSecRegField")
    macsecMapPort = 1
    macsecAddr = 1
    fieldOffset = 1
    fieldLength = 1
    data = 1
    try:
        mzdHwSetMacSecRegField(pDev, macsecMapPort, macsecAddr, fieldOffset, fieldLength, data)
    except Exception:
        traceback.print_exc()
    logging.debug(f"macsecMapPort = {macsecMapPort}")
    logging.debug(f"macsecAddr = {macsecAddr}")
    logging.debug(f"fieldOffset = {fieldOffset}")
    logging.debug(f"fieldLength = {fieldLength}")
    logging.debug(f"data = {data}")
    logging.info("\n")

    logging.info("Function name : mzdHwGetMacSecRegField")
    macsecMapPort = 1
    macsecAddr = 1
    fieldOffset = 1
    fieldLength = 1
    data = 1
    data_p = c_uint32(data)
    try:
        mzdHwGetMacSecRegField(pDev, macsecMapPort, macsecAddr, fieldOffset, fieldLength, data_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"macsecMapPort = {macsecMapPort}")
    logging.debug(f"macsecAddr = {macsecAddr}")
    logging.debug(f"fieldOffset = {fieldOffset}")
    logging.debug(f"fieldLength = {fieldLength}")
    logging.debug(f"data = {data_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdHwMacSecSBUFRegWrite")
    macsecMapPort = 1
    macsecAddr = 1
    data = 1
    try:
        mzdHwMacSecSBUFRegWrite(pDev, macsecMapPort, macsecAddr, data)
    except Exception:
        traceback.print_exc()
    logging.debug(f"macsecMapPort = {macsecMapPort}")
    logging.debug(f"macsecAddr = {macsecAddr}")
    logging.debug(f"data = {data}")
    logging.info("\n")

    logging.info("Function name : mzdHwMacSecSBUFRegRead")
    macsecMapPort = 1
    macsecAddr = 1
    data = 1
    data_p = c_uint32(data)
    try:
        mzdHwMacSecSBUFRegRead(pDev, macsecMapPort, macsecAddr, data_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"macsecMapPort = {macsecMapPort}")
    logging.debug(f"macsecAddr = {macsecAddr}")
    logging.debug(f"data = {data_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdHwSetMacSecSBUFRegField")
    macsecMapPort = 1
    macsecAddr = 1
    fieldOffset = 1
    fieldLength = 1
    data = 1
    try:
        mzdHwSetMacSecSBUFRegField(pDev, macsecMapPort, macsecAddr, fieldOffset, fieldLength, data)
    except Exception:
        traceback.print_exc()
    logging.debug(f"macsecMapPort = {macsecMapPort}")
    logging.debug(f"macsecAddr = {macsecAddr}")
    logging.debug(f"fieldOffset = {fieldOffset}")
    logging.debug(f"fieldLength = {fieldLength}")
    logging.debug(f"data = {data}")
    logging.info("\n")

    logging.info("Function name : mzdHwGetMacSecSBUFRegField")
    macsecMapPort = 1
    macsecAddr = 1
    fieldOffset = 1
    fieldLength = 1
    data = 1
    data_p = c_uint32(data)
    try:
        mzdHwGetMacSecSBUFRegField(pDev, macsecMapPort, macsecAddr, fieldOffset, fieldLength, data_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"macsecMapPort = {macsecMapPort}")
    logging.debug(f"macsecAddr = {macsecAddr}")
    logging.debug(f"fieldOffset = {fieldOffset}")
    logging.debug(f"fieldLength = {fieldLength}")
    logging.debug(f"data = {data_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdHwMacRegWrite")
    macMapPort = 1
    host_or_line = 1
    macAddr = 1
    data = 1
    try:
        mzdHwMacRegWrite(pDev, macMapPort, host_or_line, macAddr, data)
    except Exception:
        traceback.print_exc()
    logging.debug(f"macMapPort = {macMapPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"macAddr = {macAddr}")
    logging.debug(f"data = {data}")
    logging.info("\n")

    logging.info("Function name : mzdHwMacRegRead")
    macMapPort = 1
    host_or_line = 1
    macAddr = 1
    data = 1
    data_p = c_uint32(data)
    try:
        mzdHwMacRegRead(pDev, macMapPort, host_or_line, macAddr, data_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"macMapPort = {macMapPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"macAddr = {macAddr}")
    logging.debug(f"data = {data_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdHwSetMacRegField")
    macMapPort = 1
    host_or_line = 1
    macAddr = 1
    fieldOffset = 1
    fieldLength = 1
    data = 1
    try:
        mzdHwSetMacRegField(pDev, macMapPort, host_or_line, macAddr, fieldOffset, fieldLength, data)
    except Exception:
        traceback.print_exc()
    logging.debug(f"macMapPort = {macMapPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"macAddr = {macAddr}")
    logging.debug(f"fieldOffset = {fieldOffset}")
    logging.debug(f"fieldLength = {fieldLength}")
    logging.debug(f"data = {data}")
    logging.info("\n")

    logging.info("Function name : mzdHwGetMacRegField")
    macMapPort = 1
    host_or_line = 1
    macAddr = 1
    fieldOffset = 1
    fieldLength = 1
    data = 1
    data_p = c_uint32(data)
    try:
        mzdHwGetMacRegField(pDev, macMapPort, host_or_line, macAddr, fieldOffset, fieldLength, data_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"macMapPort = {macMapPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"macAddr = {macAddr}")
    logging.debug(f"fieldOffset = {fieldOffset}")
    logging.debug(f"fieldLength = {fieldLength}")
    logging.debug(f"data = {data_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdSetSerdesDevInfo")
    serdesMapPort = 1
    serdesMapHostLine = 1
    try:
        mzdSetSerdesDevInfo(pDev, serdesMapPort, serdesMapHostLine)
    except Exception:
        traceback.print_exc()
    logging.debug(f"serdesMapPort = {serdesMapPort}")
    logging.debug(f"serdesMapHostLine = {serdesMapHostLine}")
    logging.info("\n")

    logging.info("Function name : mzdHwSerdesPhyRegWrite")
    mdioPort = 1
    host_or_line = 1
    serdesLane = 1
    regAddr = 1
    data = 1
    try:
        mzdHwSerdesPhyRegWrite(pDev, mdioPort, host_or_line, serdesLane, regAddr, data)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"serdesLane = {serdesLane}")
    logging.debug(f"regAddr = {regAddr}")
    logging.debug(f"data = {data}")
    logging.info("\n")

    logging.info("Function name : mzdHwSerdesPhyRegRead")
    mdioPort = 1
    host_or_line = 1
    serdesLane = 1
    regAddr = 1
    data = 1
    data_p = c_uint32(data)
    try:
        mzdHwSerdesPhyRegRead(pDev, mdioPort, host_or_line, serdesLane, regAddr, data_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"serdesLane = {serdesLane}")
    logging.debug(f"regAddr = {regAddr}")
    logging.debug(f"data = {data_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdHwSetSerdesPhyRegField")
    mdioPort = 1
    host_or_line = 1
    serdesLane = 1
    regAddr = 1
    fieldOffset = 1
    fieldLength = 1
    data = 1
    try:
        mzdHwSetSerdesPhyRegField(pDev, mdioPort, host_or_line, serdesLane, regAddr, fieldOffset, fieldLength, data)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"serdesLane = {serdesLane}")
    logging.debug(f"regAddr = {regAddr}")
    logging.debug(f"fieldOffset = {fieldOffset}")
    logging.debug(f"fieldLength = {fieldLength}")
    logging.debug(f"data = {data}")
    logging.info("\n")

    logging.info("Function name : mzdHwGetSerdesPhyRegField")
    mdioPort = 1
    host_or_line = 1
    serdesLane = 1
    regAddr = 1
    fieldOffset = 1
    fieldLength = 1
    data = 1
    data_p = c_uint32(data)
    try:
        mzdHwGetSerdesPhyRegField(pDev, mdioPort, host_or_line, serdesLane, regAddr, fieldOffset, fieldLength, data_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"serdesLane = {serdesLane}")
    logging.debug(f"regAddr = {regAddr}")
    logging.debug(f"fieldOffset = {fieldOffset}")
    logging.debug(f"fieldLength = {fieldLength}")
    logging.debug(f"data = {data_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdHwSerdesPhyLaneRegBroadcast")
    mdioPort = 1
    host_or_line = 1
    enable = 1
    try:
        mzdHwSerdesPhyLaneRegBroadcast(pDev, mdioPort, host_or_line, enable)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"enable = {enable}")
    logging.info("\n")

    logging.info("Function name : mzdLanePowerdown")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    try:
        mzdLanePowerdown(pDev, mdioPort, host_or_line, laneOffset)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.info("\n")

    logging.info("Function name : mzdLanePowerup")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    try:
        mzdLanePowerup(pDev, mdioPort, host_or_line, laneOffset)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.info("\n")

    logging.info("Function name : mzdPortReset")
    mdioPort = 1
    host_or_line = 1
    resetType = MZD_RESET_TYPE.MZD_SOFT_RESET.value
    timeoutMs = 1
    try:
        mzdPortReset(pDev, mdioPort, host_or_line, resetType, timeoutMs)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"resetType = {resetType}")
    logging.debug(f"timeoutMs = {timeoutMs}")
    logging.info("\n")

    logging.info("Function name : mzdChipResetControl")
    resetType = 1
    bRestore = MZD_BOOL.MZD_FALSE.value
    try:
        mzdChipResetControl(pDev, resetType, bRestore)
    except Exception:
        traceback.print_exc()
    logging.debug(f"resetType = {resetType}")
    logging.debug(f"bRestore = {bRestore}")
    logging.info("\n")

    logging.info("Function name : mzdGetIntrSrcStatus")
    gpioIntr = (c_int * 9)()
    gpioIntr_init = [0] * 9
    for idx, value in enumerate(gpioIntr_init):
        gpioIntr[idx] = value
    macIntr = (MZD_MAC_CHIP_INTR * 2)()
    macIntr_init = [0] * 2
    for idx, value in enumerate(macIntr_init):
        macIntr[idx] = value
    serdesIntr = (MZD_SERDES_CHIP_INTR * 4)()
    serdesIntr_init = [0] * 4
    for idx, value in enumerate(serdesIntr_init):
        serdesIntr[idx] = value
    pcsIntr = (MZD_PCS_CHIP_INTR * 16)()
    pcsIntr_init = [0] * 16
    for idx, value in enumerate(pcsIntr_init):
        pcsIntr[idx] = value
    intrSelector = MZD_GLOBAL_CHIP_INTR(0, 0, 0, gpioIntr, macIntr, serdesIntr, pcsIntr)
    forceInterrupt = MZD_BOOL.MZD_FALSE.value
    forceInterrupt_p = MZD_BOOL(forceInterrupt)
    gpioIntr = (c_int * 9)()
    gpioIntr_init = [0] * 9
    for idx, value in enumerate(gpioIntr_init):
        gpioIntr[idx] = value
    macIntr = (MZD_MAC_CHIP_INTR * 2)()
    macIntr_init = [0] * 2
    for idx, value in enumerate(macIntr_init):
        macIntr[idx] = value
    serdesIntr = (MZD_SERDES_CHIP_INTR * 4)()
    serdesIntr_init = [0] * 4
    for idx, value in enumerate(serdesIntr_init):
        serdesIntr[idx] = value
    pcsIntr = (MZD_PCS_CHIP_INTR * 16)()
    pcsIntr_init = [0] * 16
    for idx, value in enumerate(pcsIntr_init):
        pcsIntr[idx] = value
    intrSrc = MZD_GLOBAL_CHIP_INTR(0, 0, 0, gpioIntr, macIntr, serdesIntr, pcsIntr)
    intrSrc_p = byref(intrSrc)
    try:
        mzdGetIntrSrcStatus(pDev, intrSelector, forceInterrupt_p, intrSrc_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"intrSelector = {MZD_GLOBAL_CHIP_INTR.globalAggregatedIntr1}")
    logging.debug(f"intrSelector = {MZD_GLOBAL_CHIP_INTR.globalAggregatedIntr2}")
    logging.debug(f"intrSelector = {MZD_GLOBAL_CHIP_INTR.onChipProcIntr}")
    logging.debug(f"forceInterrupt = {forceInterrupt_p.value}")
    logging.debug(f"intrSrc = {MZD_GLOBAL_CHIP_INTR.globalAggregatedIntr1}")
    logging.debug(f"intrSrc = {MZD_GLOBAL_CHIP_INTR.globalAggregatedIntr2}")
    logging.debug(f"intrSrc = {MZD_GLOBAL_CHIP_INTR.onChipProcIntr}")
    logging.info("\n")

    logging.info("Function name : mzdSetGlobalInterruptCntl")
    openDrain = MZD_BOOL.MZD_FALSE.value
    intrPolarity = 1
    forceInterrupt = MZD_BOOL.MZD_FALSE.value
    try:
        mzdSetGlobalInterruptCntl(pDev, openDrain, intrPolarity, forceInterrupt)
    except Exception:
        traceback.print_exc()
    logging.debug(f"openDrain = {openDrain}")
    logging.debug(f"intrPolarity = {intrPolarity}")
    logging.debug(f"forceInterrupt = {forceInterrupt}")
    logging.info("\n")

    logging.info("Function name : mzdGetGlobalInterruptCntl")
    openDrain = MZD_BOOL.MZD_FALSE.value
    openDrain_p = MZD_BOOL(openDrain)
    intrPolarity = 1
    intrPolarity_p = c_uint16(intrPolarity)
    forceInterrupt = MZD_BOOL.MZD_FALSE.value
    forceInterrupt_p = MZD_BOOL(forceInterrupt)
    try:
        mzdGetGlobalInterruptCntl(pDev, openDrain_p, intrPolarity_p, forceInterrupt_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"openDrain = {openDrain_p.value}")
    logging.debug(f"intrPolarity = {intrPolarity_p.value}")
    logging.debug(f"forceInterrupt = {forceInterrupt_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdSetGlobalInterruptEnable")
    globalAggregatedIntrEnable1 = 1
    globalAggregatedIntrEnable2 = 1
    try:
        mzdSetGlobalInterruptEnable(pDev, globalAggregatedIntrEnable1, globalAggregatedIntrEnable2)
    except Exception:
        traceback.print_exc()
    logging.debug(f"globalAggregatedIntrEnable1 = {globalAggregatedIntrEnable1}")
    logging.debug(f"globalAggregatedIntrEnable2 = {globalAggregatedIntrEnable2}")
    logging.info("\n")

    logging.info("Function name : mzdGetGlobalInterruptEnable")
    globalAggregatedIntrEnable1 = 1
    globalAggregatedIntrEnable1_p = c_uint16(globalAggregatedIntrEnable1)
    globalAggregatedIntrEnable2 = 1
    globalAggregatedIntrEnable2_p = c_uint16(globalAggregatedIntrEnable2)
    try:
        mzdGetGlobalInterruptEnable(pDev, globalAggregatedIntrEnable1_p, globalAggregatedIntrEnable2_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"globalAggregatedIntrEnable1 = {globalAggregatedIntrEnable1_p.value}")
    logging.debug(f"globalAggregatedIntrEnable2 = {globalAggregatedIntrEnable2_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdGetUnmaskedInterrupts")
    gpioIntr = (c_int * 9)()
    gpioIntr_init = [0] * 9
    for idx, value in enumerate(gpioIntr_init):
        gpioIntr[idx] = value
    macIntr = (MZD_MAC_CHIP_INTR * 2)()
    macIntr_init = [0] * 2
    for idx, value in enumerate(macIntr_init):
        macIntr[idx] = value
    serdesIntr = (MZD_SERDES_CHIP_INTR * 4)()
    serdesIntr_init = [0] * 4
    for idx, value in enumerate(serdesIntr_init):
        serdesIntr[idx] = value
    pcsIntr = (MZD_PCS_CHIP_INTR * 16)()
    pcsIntr_init = [0] * 16
    for idx, value in enumerate(pcsIntr_init):
        pcsIntr[idx] = value
    intrSelector = MZD_GLOBAL_CHIP_INTR(0, 0, 0, gpioIntr, macIntr, serdesIntr, pcsIntr)
    intrSelector_p = byref(intrSelector)
    try:
        mzdGetUnmaskedInterrupts(pDev, intrSelector_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"intrSelector = {MZD_GLOBAL_CHIP_INTR.globalAggregatedIntr1}")
    logging.debug(f"intrSelector = {MZD_GLOBAL_CHIP_INTR.globalAggregatedIntr2}")
    logging.debug(f"intrSelector = {MZD_GLOBAL_CHIP_INTR.onChipProcIntr}")
    logging.info("\n")

    logging.info("Function name : mzdSetGPIOInterruptEnable")
    gpioPinId = MZD_PIN_ID.MZD_PIN_GPIO1.value
    gpioIntrEnable = 1
    try:
        mzdSetGPIOInterruptEnable(pDev, gpioPinId, gpioIntrEnable)
    except Exception:
        traceback.print_exc()
    logging.debug(f"gpioPinId = {gpioPinId}")
    logging.debug(f"gpioIntrEnable = {gpioIntrEnable}")
    logging.info("\n")

    logging.info("Function name : mzdGetGPIOInterruptEnable")
    gpioPinId = MZD_PIN_ID.MZD_PIN_GPIO1.value
    gpioIntrEnable = 1
    gpioIntrEnable_p = c_uint16(gpioIntrEnable)
    try:
        mzdGetGPIOInterruptEnable(pDev, gpioPinId, gpioIntrEnable_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"gpioPinId = {gpioPinId}")
    logging.debug(f"gpioIntrEnable = {gpioIntrEnable_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdSetGPIOInterruptType")
    gpioPinId = MZD_PIN_ID.MZD_PIN_GPIO1.value
    gpioIntrType = 1
    try:
        mzdSetGPIOInterruptType(pDev, gpioPinId, gpioIntrType)
    except Exception:
        traceback.print_exc()
    logging.debug(f"gpioPinId = {gpioPinId}")
    logging.debug(f"gpioIntrType = {gpioIntrType}")
    logging.info("\n")

    logging.info("Function name : mzdGetGPIOInterruptType")
    gpioPinId = MZD_PIN_ID.MZD_PIN_GPIO1.value
    gpioIntrType = 1
    gpioIntrType_p = c_uint16(gpioIntrType)
    try:
        mzdGetGPIOInterruptType(pDev, gpioPinId, gpioIntrType_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"gpioPinId = {gpioPinId}")
    logging.debug(f"gpioIntrType = {gpioIntrType_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdGetGPIOInterruptStatus")
    gpioPinId = MZD_PIN_ID.MZD_PIN_GPIO1.value
    gpioIntrLatchedStatus = 1
    gpioIntrLatchedStatus_p = c_uint16(gpioIntrLatchedStatus)
    gpioIntrCurrentStatus = 1
    gpioIntrCurrentStatus_p = c_uint16(gpioIntrCurrentStatus)
    try:
        mzdGetGPIOInterruptStatus(pDev, gpioPinId, gpioIntrLatchedStatus_p, gpioIntrCurrentStatus_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"gpioPinId = {gpioPinId}")
    logging.debug(f"gpioIntrLatchedStatus = {gpioIntrLatchedStatus_p.value}")
    logging.debug(f"gpioIntrCurrentStatus = {gpioIntrCurrentStatus_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdSetPCSInterruptEnable")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    intrEnable = MZD_PCS_UNIT_INTR(0, 0, 0, 0)
    try:
        mzdSetPCSInterruptEnable(pDev, mdioPort, host_or_line, laneOffset, intrEnable)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"intrEnable = {MZD_PCS_UNIT_INTR.srcFlag1}")
    logging.debug(f"intrEnable = {MZD_PCS_UNIT_INTR.srcFlag2}")
    logging.debug(f"intrEnable = {MZD_PCS_UNIT_INTR.apAutoNeg}")
    logging.debug(f"intrEnable = {MZD_PCS_UNIT_INTR.excessiveLinkErr}")
    logging.info("\n")

    logging.info("Function name : mzdGetPCSInterruptEnable")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    intrEnable = MZD_PCS_UNIT_INTR(0, 0, 0, 0)
    intrEnable_p = byref(intrEnable)
    try:
        mzdGetPCSInterruptEnable(pDev, mdioPort, host_or_line, laneOffset, intrEnable_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"intrEnable = {MZD_PCS_UNIT_INTR.srcFlag1}")
    logging.debug(f"intrEnable = {MZD_PCS_UNIT_INTR.srcFlag2}")
    logging.debug(f"intrEnable = {MZD_PCS_UNIT_INTR.apAutoNeg}")
    logging.debug(f"intrEnable = {MZD_PCS_UNIT_INTR.excessiveLinkErr}")
    logging.info("\n")

    logging.info("Function name : mzdGetPCSInterruptStatus")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    latchedIntrStatus = MZD_PCS_UNIT_INTR(0, 0, 0, 0)
    latchedIntrStatus_p = byref(latchedIntrStatus)
    currentIntrStatus = MZD_PCS_UNIT_INTR(0, 0, 0, 0)
    currentIntrStatus_p = byref(currentIntrStatus)
    try:
        mzdGetPCSInterruptStatus(pDev, mdioPort, host_or_line, laneOffset, latchedIntrStatus_p, currentIntrStatus_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"latchedIntrStatus = {MZD_PCS_UNIT_INTR.srcFlag1}")
    logging.debug(f"latchedIntrStatus = {MZD_PCS_UNIT_INTR.srcFlag2}")
    logging.debug(f"latchedIntrStatus = {MZD_PCS_UNIT_INTR.apAutoNeg}")
    logging.debug(f"latchedIntrStatus = {MZD_PCS_UNIT_INTR.excessiveLinkErr}")
    logging.debug(f"currentIntrStatus = {MZD_PCS_UNIT_INTR.srcFlag1}")
    logging.debug(f"currentIntrStatus = {MZD_PCS_UNIT_INTR.srcFlag2}")
    logging.debug(f"currentIntrStatus = {MZD_PCS_UNIT_INTR.apAutoNeg}")
    logging.debug(f"currentIntrStatus = {MZD_PCS_UNIT_INTR.excessiveLinkErr}")
    logging.info("\n")

    logging.info("Function name : mzdGetPCSRealtimeStatus")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    rtIntrStatus = MZD_PCS_UNIT_INTR(0, 0, 0, 0)
    rtIntrStatus_p = byref(rtIntrStatus)
    try:
        mzdGetPCSRealtimeStatus(pDev, mdioPort, host_or_line, laneOffset, rtIntrStatus_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"rtIntrStatus = {MZD_PCS_UNIT_INTR.srcFlag1}")
    logging.debug(f"rtIntrStatus = {MZD_PCS_UNIT_INTR.srcFlag2}")
    logging.debug(f"rtIntrStatus = {MZD_PCS_UNIT_INTR.apAutoNeg}")
    logging.debug(f"rtIntrStatus = {MZD_PCS_UNIT_INTR.excessiveLinkErr}")
    logging.info("\n")

    logging.info("Function name : mzdSetPinMode")
    pinId = MZD_PIN_ID.MZD_PIN_GPIO1.value
    pinMode = MZD_PIN_MODE.MZD_PIN_MODE_GPIO.value
    openDrain = MZD_BOOL.MZD_FALSE.value
    try:
        mzdSetPinMode(pDev, pinId, pinMode, openDrain)
    except Exception:
        traceback.print_exc()
    logging.debug(f"pinId = {pinId}")
    logging.debug(f"pinMode = {pinMode}")
    logging.debug(f"openDrain = {openDrain}")
    logging.info("\n")

    logging.info("Function name : mzdGetPinMode")
    pinId = MZD_PIN_ID.MZD_PIN_GPIO1.value
    pinMode = MZD_PIN_MODE.MZD_PIN_MODE_GPIO.value
    pinMode_p = MZD_PIN_MODE(pinMode)
    openDrain = MZD_BOOL.MZD_FALSE.value
    openDrain_p = MZD_BOOL(openDrain)
    try:
        mzdGetPinMode(pDev, pinId, pinMode_p, openDrain_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"pinId = {pinId}")
    logging.debug(f"pinMode = {pinMode_p.value}")
    logging.debug(f"openDrain = {openDrain_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdSetGPIOPinDirection")
    gpioPinId = MZD_PIN_ID.MZD_PIN_GPIO1.value
    gpioPinDirection = 1
    try:
        mzdSetGPIOPinDirection(pDev, gpioPinId, gpioPinDirection)
    except Exception:
        traceback.print_exc()
    logging.debug(f"gpioPinId = {gpioPinId}")
    logging.debug(f"gpioPinDirection = {gpioPinDirection}")
    logging.info("\n")

    logging.info("Function name : mzdGetGPIOPinDirection")
    gpioPinId = MZD_PIN_ID.MZD_PIN_GPIO1.value
    gpioPinDirection = 1
    gpioPinDirection_p = c_uint16(gpioPinDirection)
    try:
        mzdGetGPIOPinDirection(pDev, gpioPinId, gpioPinDirection_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"gpioPinId = {gpioPinId}")
    logging.debug(f"gpioPinDirection = {gpioPinDirection_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdSetGPIOPinData")
    gpioPinId = MZD_PIN_ID.MZD_PIN_GPIO1.value
    gpioData = 1
    try:
        mzdSetGPIOPinData(pDev, gpioPinId, gpioData)
    except Exception:
        traceback.print_exc()
    logging.debug(f"gpioPinId = {gpioPinId}")
    logging.debug(f"gpioData = {gpioData}")
    logging.info("\n")

    logging.info("Function name : mzdGetGPIOPinData")
    gpioPinId = MZD_PIN_ID.MZD_PIN_GPIO1.value
    gpioData = 1
    gpioData_p = c_uint16(gpioData)
    try:
        mzdGetGPIOPinData(pDev, gpioPinId, gpioData_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"gpioPinId = {gpioPinId}")
    logging.debug(f"gpioData = {gpioData_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdSetLEDControl")
    ledPinId = MZD_PIN_ID.MZD_PIN_GPIO1.value
    ledCtrl = MZD_LED_CTRL(0, 0, 0, 0, 0, 0, 0, 0)
    try:
        mzdSetLEDControl(pDev, ledPinId, ledCtrl)
    except Exception:
        traceback.print_exc()
    logging.debug(f"ledPinId = {ledPinId}")
    logging.debug(f"ledCtrl = {MZD_LED_CTRL.interfaceSelect}")
    logging.debug(f"ledCtrl = {MZD_LED_CTRL.portSelect}")
    logging.debug(f"ledCtrl = {MZD_LED_CTRL.laneSelect}")
    logging.debug(f"ledCtrl = {MZD_LED_CTRL.blinkActivity}")
    logging.debug(f"ledCtrl = {MZD_LED_CTRL.solidActivity}")
    logging.debug(f"ledCtrl = {MZD_LED_CTRL.polarity}")
    logging.debug(f"ledCtrl = {MZD_LED_CTRL.mixRateLevel}")
    logging.debug(f"ledCtrl = {MZD_LED_CTRL.blinkRateSelect}")
    logging.info("\n")

    logging.info("Function name : mzdSetLEDTimer")
    ledTimerConfig = MZD_LED_TIMER_CONFIG(0, 0, 0)
    try:
        mzdSetLEDTimer(pDev, ledTimerConfig)
    except Exception:
        traceback.print_exc()
    logging.debug(f"ledTimerConfig = {MZD_LED_TIMER_CONFIG.blinkRate1}")
    logging.debug(f"ledTimerConfig = {MZD_LED_TIMER_CONFIG.blinkRate2}")
    logging.debug(f"ledTimerConfig = {MZD_LED_TIMER_CONFIG.pulseStretchDuration}")
    logging.info("\n")

    logging.info("Function name : mzdConfigRClkPin")
    rClkPinId = MZD_PIN_ID.MZD_PIN_GPIO1.value
    portSelect = 1
    interfaceSelect = 1
    laneSelect = 1
    try:
        mzdConfigRClkPin(pDev, rClkPinId, portSelect, interfaceSelect, laneSelect)
    except Exception:
        traceback.print_exc()
    logging.debug(f"rClkPinId = {rClkPinId}")
    logging.debug(f"portSelect = {portSelect}")
    logging.debug(f"interfaceSelect = {interfaceSelect}")
    logging.debug(f"laneSelect = {laneSelect}")
    logging.info("\n")

    logging.info("Function name : mzdConfigRClkSource")
    portSelect = 1
    interfaceSelect = 1
    laneSelect = 1
    clockOption = MZD_RCLK_SRC_OPTION(0, 0, 0, 0)
    try:
        mzdConfigRClkSource(pDev, portSelect, interfaceSelect, laneSelect, clockOption)
    except Exception:
        traceback.print_exc()
    logging.debug(f"portSelect = {portSelect}")
    logging.debug(f"interfaceSelect = {interfaceSelect}")
    logging.debug(f"laneSelect = {laneSelect}")
    logging.debug(f"clockOption = {MZD_RCLK_SRC_OPTION.overWriteSrcClock}")
    logging.debug(f"clockOption = {MZD_RCLK_SRC_OPTION.srcClockSelect}")
    logging.debug(f"clockOption = {MZD_RCLK_SRC_OPTION.dividerConfig}")
    logging.debug(f"clockOption = {MZD_RCLK_SRC_OPTION.divideRatio}")
    logging.info("\n")

    logging.info("Function name : mzdMacSecMacInit")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    opMode = MZD_OP_MODE.MZD_OP_MODE_UNKNOWN.value
    initOption = 1
    try:
        mzdMacSecMacInit(pDev, mdioPort, host_or_line, laneOffset, opMode, initOption)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"opMode = {opMode}")
    logging.debug(f"initOption = {initOption}")
    logging.info("\n")

    logging.info("Function name : mzdMacEnable")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    macEnable = MZD_BOOL.MZD_FALSE.value
    try:
        mzdMacEnable(pDev, mdioPort, host_or_line, laneOffset, macEnable)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"macEnable = {macEnable}")
    logging.info("\n")

    logging.info("Function name : mzdMacSecEnable")
    mdioPort = 1
    host_or_line = 1
    macsecEnable = MZD_BOOL.MZD_FALSE.value
    try:
        mzdMacSecEnable(pDev, mdioPort, host_or_line, macsecEnable)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"macsecEnable = {macsecEnable}")
    logging.info("\n")

    logging.info("Function name : mzdMacSetLowSpeed")
    mdioPort = 1
    laneOffset = 1
    try:
        mzdMacSetLowSpeed(pDev, mdioPort, laneOffset)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.info("\n")

    logging.info("Function name : mzdMacSetHighSpeed")
    mdioPort = 1
    try:
        mzdMacSetHighSpeed(pDev, mdioPort)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.info("\n")

    logging.info("Function name : mzdMacSecPtpBypass")
    mdioPort = 1
    bypassPtp = MZD_BOOL.MZD_FALSE.value
    try:
        mzdMacSecPtpBypass(pDev, mdioPort, bypassPtp)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"bypassPtp = {bypassPtp}")
    logging.info("\n")

    logging.info("Function name : mzdMacSecEgressBypass")
    mdioPort = 1
    laneOffset = 1
    egressBypass = MZD_BOOL.MZD_FALSE.value
    try:
        mzdMacSecEgressBypass(pDev, mdioPort, laneOffset, egressBypass)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"egressBypass = {egressBypass}")
    logging.info("\n")

    logging.info("Function name : mzdMacSecIngressBypass")
    mdioPort = 1
    laneOffset = 1
    ingressBypass = MZD_BOOL.MZD_FALSE.value
    try:
        mzdMacSecIngressBypass(pDev, mdioPort, laneOffset, ingressBypass)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"ingressBypass = {ingressBypass}")
    logging.info("\n")

    logging.info("Function name : mzdMacBypassPPMFifo")
    mdioPort = 1
    bypassPPMFifo = MZD_BOOL.MZD_FALSE.value
    try:
        mzdMacBypassPPMFifo(pDev, mdioPort, bypassPPMFifo)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"bypassPPMFifo = {bypassPPMFifo}")
    logging.info("\n")

    logging.info("Function name : mzdMacBypassPPMFifoPushBackLatencyMatch")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    pushBackLatencyMatch = 1
    try:
        mzdMacBypassPPMFifoPushBackLatencyMatch(pDev, mdioPort, host_or_line, laneOffset, pushBackLatencyMatch)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"pushBackLatencyMatch = {pushBackLatencyMatch}")
    logging.info("\n")

    logging.info("Function name : mzdMacBypassPPMFifoDelayAlignMarkerPushBack")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    pushBackDelay = 1
    try:
        mzdMacBypassPPMFifoDelayAlignMarkerPushBack(pDev, mdioPort, host_or_line, laneOffset, pushBackDelay)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"pushBackDelay = {pushBackDelay}")
    logging.info("\n")

    logging.info("Function name : mzdMacMIBStatDump")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    stateDumpOptions = 1
    try:
        mzdMacMIBStatDump(pDev, mdioPort, host_or_line, laneOffset, stateDumpOptions)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"stateDumpOptions = {stateDumpOptions}")
    logging.info("\n")

    logging.info("Function name : mzdMacPauseFrameInjectionToHost")
    mdioPort = 1
    laneOffset = 1
    enable = 1
    try:
        mzdMacPauseFrameInjectionToHost(pDev, mdioPort, laneOffset, enable)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"enable = {enable}")
    logging.info("\n")

    logging.info("Function name : mzdMacSetPauseFrameToHostThreshold")
    mdioPort = 1
    laneOffset = 1
    lowThreshold = 1
    highThreshold = 1
    try:
        mzdMacSetPauseFrameToHostThreshold(pDev, mdioPort, laneOffset, lowThreshold, highThreshold)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"lowThreshold = {lowThreshold}")
    logging.debug(f"highThreshold = {highThreshold}")
    logging.info("\n")

    logging.info("Function name : mzdMacGetPauseFrameToHostThreshold")
    mdioPort = 1
    laneOffset = 1
    lowThreshold = 1
    lowThreshold_p = c_uint16(lowThreshold)
    highThreshold = 1
    highThreshold_p = c_uint16(highThreshold)
    try:
        mzdMacGetPauseFrameToHostThreshold(pDev, mdioPort, laneOffset, lowThreshold_p, highThreshold_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"lowThreshold = {lowThreshold_p.value}")
    logging.debug(f"highThreshold = {highThreshold_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdMacSecHmux4ArbiterEnable")
    macsecMapPort = 1
    hostSideMode = MZD_OP_MODE.MZD_OP_MODE_UNKNOWN.value
    lowerPortPrimary = MZD_BOOL.MZD_FALSE.value
    hmux4Options = 1
    try:
        mzdMacSecHmux4ArbiterEnable(pDev, macsecMapPort, hostSideMode, lowerPortPrimary, hmux4Options)
    except Exception:
        traceback.print_exc()
    logging.debug(f"macsecMapPort = {macsecMapPort}")
    logging.debug(f"hostSideMode = {hostSideMode}")
    logging.debug(f"lowerPortPrimary = {lowerPortPrimary}")
    logging.debug(f"hmux4Options = {hmux4Options}")
    logging.info("\n")

    logging.info("Function name : mzdMacSecHmux8ArbiterEnable")
    hostSideMode = MZD_OP_MODE.MZD_OP_MODE_UNKNOWN.value
    lowerPortsPrimary = MZD_BOOL.MZD_FALSE.value
    hmux8Options = 1
    try:
        mzdMacSecHmux8ArbiterEnable(pDev, hostSideMode, lowerPortsPrimary, hmux8Options)
    except Exception:
        traceback.print_exc()
    logging.debug(f"hostSideMode = {hostSideMode}")
    logging.debug(f"lowerPortsPrimary = {lowerPortsPrimary}")
    logging.debug(f"hmux8Options = {hmux8Options}")
    logging.info("\n")

    logging.info("Function name : mzdMacSecHmuxArbiterEnablePerLane")
    mdioPort = 1
    laneOffset = 1
    hostSideMode = MZD_OP_MODE.MZD_OP_MODE_UNKNOWN.value
    hmuxType = 1
    try:
        mzdMacSecHmuxArbiterEnablePerLane(pDev, mdioPort, laneOffset, hostSideMode, hmuxType)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"hostSideMode = {hostSideMode}")
    logging.debug(f"hmuxType = {hmuxType}")
    logging.info("\n")

    logging.info("Function name : mzdHmuxArbiterReset")
    mdioPort = 1
    laneOffset = 1
    arbiterSelect = 1
    try:
        mzdHmuxArbiterReset(pDev, mdioPort, laneOffset, arbiterSelect)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"arbiterSelect = {arbiterSelect}")
    logging.info("\n")

    logging.info("Function name : mzdMacSecSelectHmuxType")
    macsecMapPort = 1
    hmuxType = 1
    lowerPortPrimary = MZD_BOOL.MZD_FALSE.value
    hmuxOptions = 1
    try:
        mzdMacSecSelectHmuxType(pDev, macsecMapPort, hmuxType, lowerPortPrimary, hmuxOptions)
    except Exception:
        traceback.print_exc()
    logging.debug(f"macsecMapPort = {macsecMapPort}")
    logging.debug(f"hmuxType = {hmuxType}")
    logging.debug(f"lowerPortPrimary = {lowerPortPrimary}")
    logging.debug(f"hmuxOptions = {hmuxOptions}")
    logging.info("\n")

    logging.info("Function name : mzdMacSecHmuxArbiterState")
    macsecMapPort = 1
    arbiterEgrState = 1
    arbiterEgrState_p = c_uint16(arbiterEgrState)
    arbiterIngrState = 1
    arbiterIngrState_p = c_uint16(arbiterIngrState)
    try:
        mzdMacSecHmuxArbiterState(pDev, macsecMapPort, arbiterEgrState_p, arbiterIngrState_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"macsecMapPort = {macsecMapPort}")
    logging.debug(f"arbiterEgrState = {arbiterEgrState_p.value}")
    logging.debug(f"arbiterIngrState = {arbiterIngrState_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdMacSecHmuxBlockBackUpIngress")
    macsecMapPort = 1
    blockBackUpPorts = MZD_BOOL.MZD_FALSE.value
    try:
        mzdMacSecHmuxBlockBackUpIngress(pDev, macsecMapPort, blockBackUpPorts)
    except Exception:
        traceback.print_exc()
    logging.debug(f"macsecMapPort = {macsecMapPort}")
    logging.debug(f"blockBackUpPorts = {blockBackUpPorts}")
    logging.info("\n")

    logging.info("Function name : mzdMacSecHmuxTimeOut")
    mdioPort = 1
    hmuxTimeOutSel = 1
    hmuxTimeOutSelOptions = 1
    try:
        mzdMacSecHmuxTimeOut(pDev, mdioPort, hmuxTimeOutSel, hmuxTimeOutSelOptions)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"hmuxTimeOutSel = {hmuxTimeOutSel}")
    logging.debug(f"hmuxTimeOutSelOptions = {hmuxTimeOutSelOptions}")
    logging.info("\n")

    logging.info("Function name : mzdMacSecManualHmuxStopTraffic")
    macsecMapPort = 1
    try:
        mzdMacSecManualHmuxStopTraffic(pDev, macsecMapPort)
    except Exception:
        traceback.print_exc()
    logging.debug(f"macsecMapPort = {macsecMapPort}")
    logging.info("\n")

    logging.info("Function name : mzdMacSecManualHmuxStartTraffic")
    macsecMapPort = 1
    try:
        mzdMacSecManualHmuxStartTraffic(pDev, macsecMapPort)
    except Exception:
        traceback.print_exc()
    logging.debug(f"macsecMapPort = {macsecMapPort}")
    logging.info("\n")

    logging.info("Function name : mzdMacSecHmuxAutoSwitch")
    macsecMapPort = 1
    try:
        mzdMacSecHmuxAutoSwitch(pDev, macsecMapPort)
    except Exception:
        traceback.print_exc()
    logging.debug(f"macsecMapPort = {macsecMapPort}")
    logging.info("\n")

    logging.info("Function name : mzdMacSecHmuxGPIOSwitchCntl")
    macsecMapPort = 1
    enable = 1
    edgeDetect = 1
    try:
        mzdMacSecHmuxGPIOSwitchCntl(pDev, macsecMapPort, enable, edgeDetect)
    except Exception:
        traceback.print_exc()
    logging.debug(f"macsecMapPort = {macsecMapPort}")
    logging.debug(f"enable = {enable}")
    logging.debug(f"edgeDetect = {edgeDetect}")
    logging.info("\n")

    logging.info("Function name : mzdMacSecHmuxLevelGPIOSwitchCntl")
    enable = 1
    try:
        mzdMacSecHmuxLevelGPIOSwitchCntl(pDev, enable)
    except Exception:
        traceback.print_exc()
    logging.debug(f"enable = {enable}")
    logging.info("\n")

    logging.info("Function name : mzdMacSecHmuxStatusOutputCntl")
    macsecMapPort = 1
    enable = 1
    polarity = 1
    try:
        mzdMacSecHmuxStatusOutputCntl(pDev, macsecMapPort, enable, polarity)
    except Exception:
        traceback.print_exc()
    logging.debug(f"macsecMapPort = {macsecMapPort}")
    logging.debug(f"enable = {enable}")
    logging.debug(f"polarity = {polarity}")
    logging.info("\n")

    logging.info("Function name : mzdMacTxFifoReset")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    try:
        mzdMacTxFifoReset(pDev, mdioPort, host_or_line, laneOffset)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.info("\n")

    logging.info("Function name : mzdMacInsertTxCRC")
    mdioPort = 1
    laneOffset = 1
    insertTxCRC = MZD_BOOL.MZD_FALSE.value
    try:
        mzdMacInsertTxCRC(pDev, mdioPort, laneOffset, insertTxCRC)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"insertTxCRC = {insertTxCRC}")
    logging.info("\n")

    logging.info("Function name : mzdMacForwardRxCRC")
    mdioPort = 1
    laneOffset = 1
    forwardRxCRC = MZD_BOOL.MZD_FALSE.value
    try:
        mzdMacForwardRxCRC(pDev, mdioPort, laneOffset, forwardRxCRC)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"forwardRxCRC = {forwardRxCRC}")
    logging.info("\n")

    logging.info("Function name : mzdMacFlowControl")
    mdioPort = 1
    laneOffset = 1
    flowCntlOption = 1
    enableFlag = 1
    try:
        mzdMacFlowControl(pDev, mdioPort, laneOffset, flowCntlOption, enableFlag)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"flowCntlOption = {flowCntlOption}")
    logging.debug(f"enableFlag = {enableFlag}")
    logging.info("\n")

    logging.info("Function name : mzdSetMacLaneInterruptEnable")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    intrEnable = 1
    try:
        mzdSetMacLaneInterruptEnable(pDev, mdioPort, host_or_line, laneOffset, intrEnable)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"intrEnable = {intrEnable}")
    logging.info("\n")

    logging.info("Function name : mzdGetMacLaneInterruptEnable")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    intrEnable = 1
    intrEnable_p = c_uint32(intrEnable)
    try:
        mzdGetMacLaneInterruptEnable(pDev, mdioPort, host_or_line, laneOffset, intrEnable_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"intrEnable = {intrEnable_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdGetMacLaneInterruptStatus")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    intrStatus = 1
    intrStatus_p = c_uint32(intrStatus)
    try:
        mzdGetMacLaneInterruptStatus(pDev, mdioPort, host_or_line, laneOffset, intrStatus_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"intrStatus = {intrStatus_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdSetMacTodInterruptEnable")
    mdioPort = 1
    host_or_line = 1
    overrunIntrEnable = 1
    underrunIntrEnable = 1
    try:
        mzdSetMacTodInterruptEnable(pDev, mdioPort, host_or_line, overrunIntrEnable, underrunIntrEnable)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"overrunIntrEnable = {overrunIntrEnable}")
    logging.debug(f"underrunIntrEnable = {underrunIntrEnable}")
    logging.info("\n")

    logging.info("Function name : mzdGetMacTodInterruptEnable")
    mdioPort = 1
    host_or_line = 1
    overrunIntrEnable = 1
    overrunIntrEnable_p = c_uint32(overrunIntrEnable)
    underrunIntrEnable = 1
    underrunIntrEnable_p = c_uint32(underrunIntrEnable)
    try:
        mzdGetMacTodInterruptEnable(pDev, mdioPort, host_or_line, overrunIntrEnable_p, underrunIntrEnable_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"overrunIntrEnable = {overrunIntrEnable_p.value}")
    logging.debug(f"underrunIntrEnable = {underrunIntrEnable_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdGetMacTodInterruptStatus")
    mdioPort = 1
    host_or_line = 1
    intrType = MZD_MAC_TOD_INTR_TYPE.MZD_MAC_TOD_INTR_TYPE_OVERRUN.value
    overrunIntrStatus = 1
    overrunIntrStatus_p = c_uint32(overrunIntrStatus)
    underrunIntrStatus = 1
    underrunIntrStatus_p = c_uint32(underrunIntrStatus)
    try:
        mzdGetMacTodInterruptStatus(pDev, mdioPort, host_or_line, intrType, overrunIntrStatus_p, underrunIntrStatus_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"intrType = {intrType}")
    logging.debug(f"overrunIntrStatus = {overrunIntrStatus_p.value}")
    logging.debug(f"underrunIntrStatus = {underrunIntrStatus_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdSetMacGlobalInterruptEnable")
    mdioPort = 1
    host_or_line = 1
    intrEnable = 1
    try:
        mzdSetMacGlobalInterruptEnable(pDev, mdioPort, host_or_line, intrEnable)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"intrEnable = {intrEnable}")
    logging.info("\n")

    logging.info("Function name : mzdGetMacGlobalInterruptEnable")
    mdioPort = 1
    host_or_line = 1
    intrEnable = 1
    intrEnable_p = c_uint32(intrEnable)
    try:
        mzdGetMacGlobalInterruptEnable(pDev, mdioPort, host_or_line, intrEnable_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"intrEnable = {intrEnable_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdGetMacGlobalInterruptStatus")
    mdioPort = 1
    host_or_line = 1
    intrStatus = 1
    intrStatus_p = c_uint32(intrStatus)
    try:
        mzdGetMacGlobalInterruptStatus(pDev, mdioPort, host_or_line, intrStatus_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"intrStatus = {intrStatus_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdMacSecHmuxConfigDump")
    mdioPort = 1
    dumpOptions = 1
    try:
        mzdMacSecHmuxConfigDump(pDev, mdioPort, dumpOptions)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"dumpOptions = {dumpOptions}")
    logging.info("\n")

    logging.info("Function name : mzdSampleHMux4MacSecBypass")
    mdioPort = 1
    hostSideMode = MZD_OP_MODE.MZD_OP_MODE_UNKNOWN.value
    try:
        mzdSampleHMux4MacSecBypass(pDev, mdioPort, hostSideMode)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"hostSideMode = {hostSideMode}")
    logging.info("\n")

    logging.info("Function name : mzdSampleHMux8MacSecBypassPerLane")
    hostSideMode = MZD_OP_MODE.MZD_OP_MODE_UNKNOWN.value
    lowerPortsPrimary = MZD_BOOL.MZD_FALSE.value
    try:
        mzdSampleHMux8MacSecBypassPerLane(pDev, hostSideMode, lowerPortsPrimary)
    except Exception:
        traceback.print_exc()
    logging.debug(f"hostSideMode = {hostSideMode}")
    logging.debug(f"lowerPortsPrimary = {lowerPortsPrimary}")
    logging.info("\n")

    logging.info("Function name : mzdSampleHMux8MacSecEnable")
    hostSideMode = MZD_OP_MODE.MZD_OP_MODE_UNKNOWN.value
    lowerPortsPrimary = MZD_BOOL.MZD_FALSE.value
    try:
        mzdSampleHMux8MacSecEnable(pDev, hostSideMode, lowerPortsPrimary)
    except Exception:
        traceback.print_exc()
    logging.debug(f"hostSideMode = {hostSideMode}")
    logging.debug(f"lowerPortsPrimary = {lowerPortsPrimary}")
    logging.info("\n")

    logging.info("Function name : mzdSampleHMux8DeMuxInitMacSecBypass")
    hostSideMode = MZD_OP_MODE.MZD_OP_MODE_UNKNOWN.value
    lineSideMode = MZD_OP_MODE.MZD_OP_MODE_UNKNOWN.value
    lowerPortsPrimary = MZD_BOOL.MZD_FALSE.value
    try:
        mzdSampleHMux8DeMuxInitMacSecBypass(pDev, hostSideMode, lineSideMode, lowerPortsPrimary)
    except Exception:
        traceback.print_exc()
    logging.debug(f"hostSideMode = {hostSideMode}")
    logging.debug(f"lineSideMode = {lineSideMode}")
    logging.debug(f"lowerPortsPrimary = {lowerPortsPrimary}")
    logging.info("\n")

    logging.info("Function name : mzdSampleLoadImageFile")
    filename = 1
    filename_p = c_char(filename)
    imageSize = 1
    imageSize_p = c_uint32(imageSize)
    pFirmwareImage = 1
    pFirmwareImage_p = c_uint8(pFirmwareImage)
    try:
        mzdSampleLoadImageFile(filename_p, imageSize_p, pFirmwareImage_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"filename = {filename_p.value}")
    logging.debug(f"imageSize = {imageSize_p.value}")
    logging.debug(f"pFirmwareImage = {pFirmwareImage_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdSampleReloadDriver")
    mdioPort = 1
    try:
        mzdSampleReloadDriver(mdioPort, pHostContext, pDev)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.info("\n")

    logging.info("Function name : mzdSampleSetPCSMode")
    mdioPort = 1
    laneOffset = 1
    modeOptionSel = 1
    buffer = (c_uint8 * 128)()
    buffer_init = [0] * 128
    for idx, value in enumerate(buffer_init):
        buffer[idx] = value
    modeOption = MZD_MODE_OPTION_STRUCT(buffer)
    hostMode = MZD_OP_MODE.MZD_OP_MODE_UNKNOWN.value
    lineMode = MZD_OP_MODE.MZD_OP_MODE_UNKNOWN.value
    pollLinkStatus = MZD_BOOL.MZD_FALSE.value
    try:
        mzdSampleSetPCSMode(pDev, mdioPort, laneOffset, modeOptionSel, modeOption, hostMode, lineMode, pollLinkStatus)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"modeOptionSel = {modeOptionSel}")
    logging.debug(f"hostMode = {hostMode}")
    logging.debug(f"lineMode = {lineMode}")
    logging.debug(f"pollLinkStatus = {pollLinkStatus}")
    logging.info("\n")

    logging.info("Function name : mzdSamplePRBSTest")
    mdioPort = 1
    laneOffset = 1
    try:
        mzdSamplePRBSTest(pDev0, pDev1, mdioPort, laneOffset)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.info("\n")

    logging.info("Function name : mzdSampleLoopbackPacketGen")
    mdioPort0 = 1
    mdioPort1 = 1
    laneOffset = 1
    try:
        mzdSampleLoopbackPacketGen(pDev0, pDev1, mdioPort0, mdioPort1, laneOffset)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort0 = {mdioPort0}")
    logging.debug(f"mdioPort1 = {mdioPort1}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.info("\n")

    logging.info("Function name : mzdSampleGetEyeWidthHeight")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    eyeTMB = E_N5C112GX4_EYE_TMB.N5C112GX4_EYE_MID.value
    eyeWidth = 1
    eyeWidth_p = c_uint16(eyeWidth)
    eyeHeight = 1
    eyeHeight_p = c_uint16(eyeHeight)
    try:
        mzdSampleGetEyeWidthHeight(pDev, mdioPort, host_or_line, laneOffset, eyeTMB, eyeWidth_p, eyeHeight_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"eyeTMB = {eyeTMB}")
    logging.debug(f"eyeWidth = {eyeWidth_p.value}")
    logging.debug(f"eyeHeight = {eyeHeight_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdSampleGetEye")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    voltageSteps = 1
    phaseLevels = 1
    try:
        mzdSampleGetEye(pDev, mdioPort, host_or_line, laneOffset, voltageSteps, phaseLevels)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"voltageSteps = {voltageSteps}")
    logging.debug(f"phaseLevels = {phaseLevels}")
    logging.info("\n")

    logging.info("Function name : mzdSampleGetTemperature")
    mdioPort = 1
    temperature = 1
    temperature_p = c_int32(temperature)
    try:
        mzdSampleGetTemperature(pDev, mdioPort, temperature_p)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"temperature = {temperature_p.value}")
    logging.info("\n")

    logging.info("Function name : mzdSampleSetCTLE")
    mdioPort = 1
    host_or_line = 1
    laneOffset = 1
    ctleParamType = E_N5C112GX4_CTLE_PARAM.N5C112GX4_RX_DC_TERM_EN.value
    paramValue = 1
    try:
        mzdSampleSetCTLE(pDev, mdioPort, host_or_line, laneOffset, ctleParamType, paramValue)
    except Exception:
        traceback.print_exc()
    logging.debug(f"mdioPort = {mdioPort}")
    logging.debug(f"host_or_line = {host_or_line}")
    logging.debug(f"laneOffset = {laneOffset}")
    logging.debug(f"ctleParamType = {ctleParamType}")
    logging.debug(f"paramValue = {paramValue}")
    logging.info("\n")

    logging.info("Function name : mzdSampleSerdesMux")
    host_or_line = 1
    try:
        mzdSampleSerdesMux(pDev0, pDev1, host_or_line)
    except Exception:
        traceback.print_exc()
    logging.debug(f"host_or_line = {host_or_line}")
    logging.info("\n")

