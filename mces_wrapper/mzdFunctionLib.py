from structure_class import *

MZDAPILib = CDLL("..\Debug\MZD.dll")

def mzdGetAPIVersion(major_p, minor_p, buildID_p):
    """
    :param major_p: A pointer of c_uint8
    :param minor_p: A pointer of c_uint8
    :param buildID_p: A pointer of c_uint8
    """
    func = MZDAPILib["mzdGetAPIVersion"]
    func.argtypes = [POINTER(c_uint8), POINTER(c_uint8), POINTER(c_uint8)]
    func.restype = c_int
    ret = func(major_p, minor_p, buildID_p)
    return ret


def mzdSetModeSelection(pDev, mdioPort, laneOffset, hostMode, lineMode, modeOptionSel, modeOption, result_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param hostMode: member from enumerate class MZD_OP_MODE
    :param lineMode: member from enumerate class MZD_OP_MODE
    :param modeOptionSel: argument type c_uint32
    :param modeOption: implementation of the structure class MZD_MODE_OPTION_STRUCT
    :param result_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdSetModeSelection"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_int, c_int, c_uint32, MZD_MODE_OPTION_STRUCT, POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, laneOffset, hostMode, lineMode, modeOptionSel, modeOption, result_p)
    return ret


def mzdSetInterfaceUserMode(pDev, mdioPort, host_or_line, laneOffset, opMode, modeOptionSel, modeOption, result_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param opMode: member from enumerate class MZD_OP_MODE
    :param modeOptionSel: argument type c_uint32
    :param modeOption: implementation of the structure class MZD_MODE_OPTION_STRUCT
    :param result_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdSetInterfaceUserMode"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_int, c_uint32, MZD_MODE_OPTION_STRUCT, POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, opMode, modeOptionSel, modeOption, result_p)
    return ret


def mzdGetOpMode(pDev, mdioPort, host_or_line, laneOffset, opMode_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param opMode_p: A pointer of the enumerate class MZD_OP_MODE
    """
    func = MZDAPILib["mzdGetOpMode"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_int)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, opMode_p)
    return ret


def mzdAutoNegControl(pDev, mdioPort, host_or_line, laneOffset, enableAutoNeg, swReset):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param enableAutoNeg: argument type c_uint16
    :param swReset: member from enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdAutoNegControl"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint16, c_int]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, enableAutoNeg, swReset)
    return ret


def mzdAutoNegCheckComplete(pDev, mdioPort, host_or_line, laneOffset, autoNegComplete_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param autoNegComplete_p: A pointer of the enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdAutoNegCheckComplete"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_int)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, autoNegComplete_p)
    return ret


def mzdGetAutoNegResolution(pDev, mdioPort, host_or_line, laneOffset, speed_bits_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param speed_bits_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdGetAutoNegResolution"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, speed_bits_p)
    return ret


def mzdCL37AutoNegControl(pDev, mdioPort, host_or_line, laneOffset, enableAutoNeg):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param enableAutoNeg: argument type c_uint16
    """
    func = MZDAPILib["mzdCL37AutoNegControl"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, enableAutoNeg)
    return ret


def mzdCL37AutoNegCheckComplete(pDev, mdioPort, host_or_line, laneOffset, autoNegComplete_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param autoNegComplete_p: A pointer of the enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdCL37AutoNegCheckComplete"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_int)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, autoNegComplete_p)
    return ret


def mzdSetPauseAdvertisement(pDev, mdioPort, host_or_line, laneOffset, pauseType, swReset):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param pauseType: argument type c_uint16
    :param swReset: member from enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdSetPauseAdvertisement"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint16, c_int]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, pauseType, swReset)
    return ret


def mzdGetPauseAdvertisement(pDev, mdioPort, host_or_line, laneOffset, pauseType_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param pauseType_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdGetPauseAdvertisement"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, pauseType_p)
    return ret


def mzdGetLPAdvertisedPause(pDev, mdioPort, host_or_line, laneOffset, pauseType_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param pauseType_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdGetLPAdvertisedPause"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, pauseType_p)
    return ret


def mzdGetTxRxPauseResolution(pDev, mdioPort, host_or_line, laneOffset, pauseResolved_p, tx_pause_enabled_p, rx_pause_enabled_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param pauseResolved_p: A pointer of the enumerate class MZD_BOOL
    :param tx_pause_enabled_p: A pointer of the enumerate class MZD_BOOL
    :param rx_pause_enabled_p: A pointer of the enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdGetTxRxPauseResolution"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_int), POINTER(c_int), POINTER(c_int)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, pauseResolved_p, tx_pause_enabled_p, rx_pause_enabled_p)
    return ret


def mzdCheckPCSLinkStatus(pDev, mdioPort, laneOffset, currentStatus_p, latchedStatus_p, statusDetail_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param currentStatus_p: A pointer of c_uint16
    :param latchedStatus_p: A pointer of c_uint16
    :param statusDetail_p: A pointer of the structure class MZD_PCS_LINK_STATUS
    """
    func = MZDAPILib["mzdCheckPCSLinkStatus"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, POINTER(c_uint16), POINTER(c_uint16), POINTER(MZD_PCS_LINK_STATUS)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, laneOffset, currentStatus_p, latchedStatus_p, statusDetail_p)
    return ret


def mzdGetDetailedLinkStatus(pDev, mdioPort, laneOffset, host_or_line, currStat_p, latchStat_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param currStat_p: A pointer of c_uint16
    :param latchStat_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdGetDetailedLinkStatus"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_uint16), POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, laneOffset, host_or_line, currStat_p, latchStat_p)
    return ret


def mzdGetPcsFaultStatus(pDev, mdioPort, host_or_line, laneOffset, currentTxFaultStatus_p, currentRxFaultStatus_p, latchedTxFaultStatus_p, latchedRxFaultStatus_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param currentTxFaultStatus_p: A pointer of c_uint16
    :param currentRxFaultStatus_p: A pointer of c_uint16
    :param latchedTxFaultStatus_p: A pointer of c_uint16
    :param latchedRxFaultStatus_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdGetPcsFaultStatus"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_uint16), POINTER(c_uint16), POINTER(c_uint16), POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, currentTxFaultStatus_p, currentRxFaultStatus_p, latchedTxFaultStatus_p, latchedRxFaultStatus_p)
    return ret


def mzdLaneSoftReset(pDev, mdioPort, host_or_line, laneOffset, timeoutMs):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param timeoutMs: argument type c_uint16
    """
    func = MZDAPILib["mzdLaneSoftReset"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, timeoutMs)
    return ret


def mzdSetDPFaultConfig(pDev, mdioPort, host_or_line, laneOffset, datapathMode, txType, rxType):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param datapathMode: argument type c_uint16
    :param txType: argument type c_uint16
    :param rxType: argument type c_uint16
    """
    func = MZDAPILib["mzdSetDPFaultConfig"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint16, c_uint16, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, datapathMode, txType, rxType)
    return ret


def mzdGetDPFaultConfig(pDev, mdioPort, host_or_line, laneOffset, datapathMode_p, txType_p, rxType_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param datapathMode_p: A pointer of c_uint16
    :param txType_p: A pointer of c_uint16
    :param rxType_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdGetDPFaultConfig"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_uint16), POINTER(c_uint16), POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, datapathMode_p, txType_p, rxType_p)
    return ret


def mzdSetSerdesMux(pDev, host_or_line, serdesMux_p):
    """
    :param pDev: argument type c_void_p
    :param host_or_line: argument type c_uint16
    :param serdesMux_p: A pointer of c_uint8
    """
    func = MZDAPILib["mzdSetSerdesMux"]
    func.argtypes = [c_void_p, c_uint16, POINTER(c_uint8)]
    func.restype = c_uint32
    ret = func(pDev, host_or_line, serdesMux_p)
    return ret


def mzdGetSerdesMux(pDev, host_or_line, serdesMux_p):
    """
    :param pDev: argument type c_void_p
    :param host_or_line: argument type c_uint16
    :param serdesMux_p: A pointer of c_uint8
    """
    func = MZDAPILib["mzdGetSerdesMux"]
    func.argtypes = [c_void_p, c_uint16, POINTER(c_uint8)]
    func.restype = c_uint32
    ret = func(pDev, host_or_line, serdesMux_p)
    return ret


def mzdGetLaneRxTrainingState(pDev, mdioPort, host_or_line, laneOffset, rxTraining_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param rxTraining_p: A pointer of the enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdGetLaneRxTrainingState"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_int)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, rxTraining_p)
    return ret


def mzdGetChipRevision(pDev, mdioPort, deviceId_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param deviceId_p: A pointer of the enumerate class MZD_DEVICE_ID
    """
    func = MZDAPILib["mzdGetChipRevision"]
    func.argtypes = [c_void_p, c_uint16, POINTER(c_int)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, deviceId_p)
    return ret


def mzdDevicePortCount(pDev, mdioPort, portCount_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param portCount_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdDevicePortCount"]
    func.argtypes = [c_void_p, c_uint16, POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, portCount_p)
    return ret


def mzdGetChipFWRevision(pDev, major_p, minor_p, patch_p, build_p):
    """
    :param pDev: argument type c_void_p
    :param major_p: A pointer of c_uint16
    :param minor_p: A pointer of c_uint16
    :param patch_p: A pointer of c_uint16
    :param build_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdGetChipFWRevision"]
    func.argtypes = [c_void_p, POINTER(c_uint16), POINTER(c_uint16), POINTER(c_uint16), POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, major_p, minor_p, patch_p, build_p)
    return ret


def mzdGetSerdesFWRevision(pDev, major_p, minor_p, patch_p, build_p):
    """
    :param pDev: argument type c_void_p
    :param major_p: A pointer of c_uint8
    :param minor_p: A pointer of c_uint8
    :param patch_p: A pointer of c_uint8
    :param build_p: A pointer of c_uint8
    """
    func = MZDAPILib["mzdGetSerdesFWRevision"]
    func.argtypes = [c_void_p, POINTER(c_uint8), POINTER(c_uint8), POINTER(c_uint8), POINTER(c_uint8)]
    func.restype = c_uint32
    ret = func(pDev, major_p, minor_p, patch_p, build_p)
    return ret


def mzdGetSerdesFWRevisionAll(pDev, majorMZD_NUM_INTERFACEMZD_MAX_PORTS_p, minorMZD_NUM_INTERFACEMZD_MAX_PORTS_p, patchMZD_NUM_INTERFACEMZD_MAX_PORTS_p, buildMZD_NUM_INTERFACEMZD_MAX_PORTS_p):
    """
    :param pDev: argument type c_void_p
    :param majorMZD_NUM_INTERFACEMZD_MAX_PORTS_p: A pointer of c_uint8
    :param minorMZD_NUM_INTERFACEMZD_MAX_PORTS_p: A pointer of c_uint8
    :param patchMZD_NUM_INTERFACEMZD_MAX_PORTS_p: A pointer of c_uint8
    :param buildMZD_NUM_INTERFACEMZD_MAX_PORTS_p: A pointer of c_uint8
    """
    func = MZDAPILib["mzdGetSerdesFWRevisionAll"]
    func.argtypes = [c_void_p, POINTER(c_uint8), POINTER(c_uint8), POINTER(c_uint8), POINTER(c_uint8)]
    func.restype = c_uint32
    ret = func(pDev, majorMZD_NUM_INTERFACEMZD_MAX_PORTS_p, minorMZD_NUM_INTERFACEMZD_MAX_PORTS_p, patchMZD_NUM_INTERFACEMZD_MAX_PORTS_p, buildMZD_NUM_INTERFACEMZD_MAX_PORTS_p)
    return ret


def mzdGetFirmwareLoadStatus(pDev, loadStatus_p):
    """
    :param pDev: argument type c_void_p
    :param loadStatus_p: A pointer of the enumerate class MZD_FIRMWARE_STATUS
    """
    func = MZDAPILib["mzdGetFirmwareLoadStatus"]
    func.argtypes = [c_void_p, POINTER(c_int)]
    func.restype = c_uint32
    ret = func(pDev, loadStatus_p)
    return ret


def mzdGetSerdesSignalDetectAndDspLock(pDev, mdioPort, host_or_line, laneOffset, signalDetect_p, dspLock_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param signalDetect_p: A pointer of c_uint16
    :param dspLock_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdGetSerdesSignalDetectAndDspLock"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_uint16), POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, signalDetect_p, dspLock_p)
    return ret


def mzdSetPCSLineLoopback(pDev, mdioPort, laneOffset, loopback_type, enable):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param loopback_type: member from enumerate class MZD_PCS_MODE_LOOPBACK
    :param enable: argument type c_uint16
    """
    func = MZDAPILib["mzdSetPCSLineLoopback"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_int, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, laneOffset, loopback_type, enable)
    return ret


def mzdSetPCSHostLoopback(pDev, mdioPort, laneOffset, loopback_type, loopbackState):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param loopback_type: member from enumerate class MZD_PCS_MODE_LOOPBACK
    :param loopbackState: argument type c_uint16
    """
    func = MZDAPILib["mzdSetPCSHostLoopback"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_int, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, laneOffset, loopback_type, loopbackState)
    return ret


def mzdHmuxSetPCSLineDeepLoopback(pDev, hostPort, hostLaneOffset, loopback_type, loopbackState):
    """
    :param pDev: argument type c_void_p
    :param hostPort: argument type c_uint16
    :param hostLaneOffset: argument type c_uint16
    :param loopback_type: member from enumerate class MZD_PCS_MODE_LOOPBACK
    :param loopbackState: argument type c_uint16
    """
    func = MZDAPILib["mzdHmuxSetPCSLineDeepLoopback"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_int, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, hostPort, hostLaneOffset, loopback_type, loopbackState)
    return ret


def mzdHmuxSetPCSHostDeepLoopback(pDev, linePort, lineLaneOffset, loopback_type, loopbackState):
    """
    :param pDev: argument type c_void_p
    :param linePort: argument type c_uint16
    :param lineLaneOffset: argument type c_uint16
    :param loopback_type: member from enumerate class MZD_PCS_MODE_LOOPBACK
    :param loopbackState: argument type c_uint16
    """
    func = MZDAPILib["mzdHmuxSetPCSHostDeepLoopback"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_int, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, linePort, lineLaneOffset, loopback_type, loopbackState)
    return ret


def mzdSetSerdesLaneLoopback(pDev, mdioPort, host_or_line, laneOffset, loopbackState, swReset):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param loopbackState: argument type c_uint16
    :param swReset: member from enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdSetSerdesLaneLoopback"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint16, c_int]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, loopbackState, swReset)
    return ret


def mzdGetSerdesLaneLoopback(pDev, mdioPort, host_or_line, laneOffset, loopbackState_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param loopbackState_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdGetSerdesLaneLoopback"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, loopbackState_p)
    return ret


def mzdConfigurePktGeneratorChecker(pDev, mdioPort, host_or_line, laneOffset, readToClear, dontuseSFDinChecker, pktPatternControl, generateCRCoff, initialPayload, frameLengthControl, numPktsToSend, randomIPG, ipgDuration):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param readToClear: member from enumerate class MZD_BOOL
    :param dontuseSFDinChecker: member from enumerate class MZD_BOOL
    :param pktPatternControl: argument type c_uint16
    :param generateCRCoff: member from enumerate class MZD_BOOL
    :param initialPayload: argument type c_uint32
    :param frameLengthControl: argument type c_uint16
    :param numPktsToSend: argument type c_uint16
    :param randomIPG: member from enumerate class MZD_BOOL
    :param ipgDuration: argument type c_uint16
    """
    func = MZDAPILib["mzdConfigurePktGeneratorChecker"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_int, c_int, c_uint16, c_int, c_uint32, c_uint16, c_uint16, c_int, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, readToClear, dontuseSFDinChecker, pktPatternControl, generateCRCoff, initialPayload, frameLengthControl, numPktsToSend, randomIPG, ipgDuration)
    return ret


def mzdEnablePktGeneratorChecker(pDev, mdioPort, host_or_line, laneOffset, enableGenerator, enableChecker):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param enableGenerator: member from enumerate class MZD_BOOL
    :param enableChecker: member from enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdEnablePktGeneratorChecker"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_int, c_int]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, enableGenerator, enableChecker)
    return ret


def mzdStartStopPktGenTraffic(pDev, mdioPort, host_or_line, laneOffset, numPktsToSend):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param numPktsToSend: member from enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdStartStopPktGenTraffic"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_int]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, numPktsToSend)
    return ret


def mzdPktGeneratorCounterReset(pDev, mdioPort, host_or_line, laneOffset):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    """
    func = MZDAPILib["mzdPktGeneratorCounterReset"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset)
    return ret


def mzdPktGeneratorGetCounter(pDev, mdioPort, host_or_line, laneOffset, pktCntType, packetCount_p, byteCount_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param pktCntType: member from enumerate class MZD_PKT_COUNT_TYPE
    :param packetCount_p: A pointer of c_uint64
    :param byteCount_p: A pointer of c_uint64
    """
    func = MZDAPILib["mzdPktGeneratorGetCounter"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_int, POINTER(c_uint64), POINTER(c_uint64)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, pktCntType, packetCount_p, byteCount_p)
    return ret


def mzdSetPRBSPattern(pDev, mdioPort, host_or_line, laneOffset, pattSel, pattSubSel):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param pattSel: member from enumerate class MZD_PRBS_SELECTOR_TYPE
    :param pattSubSel: member from enumerate class MZD_PATTERN_AB_SELECTOR_TYPE
    """
    func = MZDAPILib["mzdSetPRBSPattern"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_int, c_int]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, pattSel, pattSubSel)
    return ret


def mzdPRBSPatternOption(pDev, mdioPort, host_or_line, laneOffset, patternOption):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param patternOption: argument type c_uint16
    """
    func = MZDAPILib["mzdPRBSPatternOption"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, patternOption)
    return ret


def mzdSetPRBSEnableTxRx(pDev, mdioPort, host_or_line, laneOffset, txEnable, rxEnable, pattSel):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param txEnable: argument type c_uint16
    :param rxEnable: argument type c_uint16
    :param pattSel: member from enumerate class MZD_PRBS_SELECTOR_TYPE
    """
    func = MZDAPILib["mzdSetPRBSEnableTxRx"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint16, c_uint16, c_int]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, txEnable, rxEnable, pattSel)
    return ret


def mzdPRBSCounterReset(pDev, mdioPort, host_or_line, laneOffset):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    """
    func = MZDAPILib["mzdPRBSCounterReset"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset)
    return ret


def mzdSetPRBSWaitForLock(pDev, mdioPort, host_or_line, laneOffset, disableWaitforLock):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param disableWaitforLock: argument type c_uint16
    """
    func = MZDAPILib["mzdSetPRBSWaitForLock"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, disableWaitforLock)
    return ret


def mzdGetPRBSWaitForLock(pDev, mdioPort, host_or_line, laneOffset, disableWaitforLock_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param disableWaitforLock_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdGetPRBSWaitForLock"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, disableWaitforLock_p)
    return ret


def mzdSetPRBSClearOnRead(pDev, mdioPort, host_or_line, laneOffset, enableReadClear):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param enableReadClear: argument type c_uint16
    """
    func = MZDAPILib["mzdSetPRBSClearOnRead"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, enableReadClear)
    return ret


def mzdGetPRBSClearOnRead(pDev, mdioPort, host_or_line, laneOffset, enableReadClear_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param enableReadClear_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdGetPRBSClearOnRead"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, enableReadClear_p)
    return ret


def mzdGetPRBSLocked(pDev, mdioPort, host_or_line, laneOffset, prbsLocked_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param prbsLocked_p: A pointer of the enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdGetPRBSLocked"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_int)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, prbsLocked_p)
    return ret


def mzdGetPRBSCounts(pDev, mdioPort, host_or_line, laneOffset, pattSel, txBitCount_p, rxBitCount_p, rxBitErrorCount_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param pattSel: member from enumerate class MZD_PRBS_SELECTOR_TYPE
    :param txBitCount_p: A pointer of c_uint64
    :param rxBitCount_p: A pointer of c_uint64
    :param rxBitErrorCount_p: A pointer of c_uint64
    """
    func = MZDAPILib["mzdGetPRBSCounts"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_int, POINTER(c_uint64), POINTER(c_uint64), POINTER(c_uint64)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, pattSel, txBitCount_p, rxBitCount_p, rxBitErrorCount_p)
    return ret


def mzdSetTxRxPolarity(pDev, mdioPort, host_or_line, laneOffset, txPolarity, rxPolarity):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param txPolarity: argument type c_uint8
    :param rxPolarity: argument type c_uint8
    """
    func = MZDAPILib["mzdSetTxRxPolarity"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint8, c_uint8]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, txPolarity, rxPolarity)
    return ret


def mzdGetTxRxPolarity(pDev, mdioPort, host_or_line, laneOffset, txPolarity_p, rxPolarity_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param txPolarity_p: A pointer of c_uint8
    :param rxPolarity_p: A pointer of c_uint8
    """
    func = MZDAPILib["mzdGetTxRxPolarity"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_uint8), POINTER(c_uint8)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, txPolarity_p, rxPolarity_p)
    return ret


def mzdSetTxFFE(pDev, mdioPort, host_or_line, laneOffset, txEqParamType, paramValue):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param txEqParamType: member from enumerate class E_N5C112GX4_TXEQ_PARAM
    :param paramValue: argument type c_uint32
    """
    func = MZDAPILib["mzdSetTxFFE"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_int, c_uint32]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, txEqParamType, paramValue)
    return ret


def mzdGetTxFFE(pDev, mdioPort, host_or_line, laneOffset, txEqParamType, paramValue_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param txEqParamType: member from enumerate class E_N5C112GX4_TXEQ_PARAM
    :param paramValue_p: A pointer of c_uint32
    """
    func = MZDAPILib["mzdGetTxFFE"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_int, POINTER(c_uint32)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, txEqParamType, paramValue_p)
    return ret


def mzdDiagStateDump(pDev, mdioPort, host_or_line, laneOffset, stateDumpOptions, pStateDumpInfo_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param stateDumpOptions: argument type c_uint32
    :param pStateDumpInfo_p: A pointer of the structure class MZD_STATE_DUMP
    """
    func = MZDAPILib["mzdDiagStateDump"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint32, POINTER(MZD_STATE_DUMP)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, stateDumpOptions, pStateDumpInfo_p)
    return ret


def mzdSetRsFecControl(pDev, mdioPort, host_or_line, laneOffset, bypassIndicationEnable, bypassCorrectionEnable):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param bypassIndicationEnable: argument type c_uint16
    :param bypassCorrectionEnable: argument type c_uint16
    """
    func = MZDAPILib["mzdSetRsFecControl"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint16, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, bypassIndicationEnable, bypassCorrectionEnable)
    return ret


def mzdGetRsFecControl(pDev, mdioPort, host_or_line, laneOffset, bypassIndicationEnable_p, bypassCorrectionEnable_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param bypassIndicationEnable_p: A pointer of c_uint16
    :param bypassCorrectionEnable_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdGetRsFecControl"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_uint16), POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, bypassIndicationEnable_p, bypassCorrectionEnable_p)
    return ret


def mzdGetRsFecStatus(pDev, mdioPort, host_or_line, laneOffset, pcsLaneAlignment_p, fecLaneAlignment_p, rsFecLaneAMLock_p, latchedRsFecHighErr_p, currRsFecHighErr_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param pcsLaneAlignment_p: A pointer of c_uint16
    :param fecLaneAlignment_p: A pointer of c_uint16
    :param rsFecLaneAMLock_p: A pointer of c_uint16
    :param latchedRsFecHighErr_p: A pointer of c_uint16
    :param currRsFecHighErr_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdGetRsFecStatus"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_uint16), POINTER(c_uint16), POINTER(c_uint16), POINTER(c_uint16), POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, pcsLaneAlignment_p, fecLaneAlignment_p, rsFecLaneAMLock_p, latchedRsFecHighErr_p, currRsFecHighErr_p)
    return ret


def mzdGetRsFecPCSAlignmentStatus(pDev, mdioPort, host_or_line, laneOffset, pcs_lane, blockLocked_p, laneAligned_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param pcs_lane: argument type c_uint16
    :param blockLocked_p: A pointer of c_uint16
    :param laneAligned_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdGetRsFecPCSAlignmentStatus"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint16, POINTER(c_uint16), POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, pcs_lane, blockLocked_p, laneAligned_p)
    return ret


def mzdGetRsFecPMALaneMapping(pDev, mdioPort, host_or_line, laneOffset, mappingMZD_NUM_LANES_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param mappingMZD_NUM_LANES_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdGetRsFecPMALaneMapping"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, mappingMZD_NUM_LANES_p)
    return ret


def mzdGetRxPCSLaneMapping(pDev, mdioPort, host_or_line, lane_offset, interface_lane, pcs_lane_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param lane_offset: argument type c_uint16
    :param interface_lane: argument type c_uint16
    :param pcs_lane_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdGetRxPCSLaneMapping"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint16, POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, lane_offset, interface_lane, pcs_lane_p)
    return ret


def mzdGetRsFecCorrectedCwCntr(pDev, mdioPort, host_or_line, laneOffset, codeWordCounter_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param codeWordCounter_p: A pointer of c_uint32
    """
    func = MZDAPILib["mzdGetRsFecCorrectedCwCntr"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_uint32)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, codeWordCounter_p)
    return ret


def mzdGetRsFecUnCorrectedCwCntr(pDev, mdioPort, host_or_line, laneOffset, codeWordCounter_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param codeWordCounter_p: A pointer of c_uint32
    """
    func = MZDAPILib["mzdGetRsFecUnCorrectedCwCntr"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_uint32)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, codeWordCounter_p)
    return ret


def mzdGetRsFecSymbolErrorCntr(pDev, mdioPort, host_or_line, laneOffset, fecLane, errorCounter_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param fecLane: argument type c_uint16
    :param errorCounter_p: A pointer of c_uint32
    """
    func = MZDAPILib["mzdGetRsFecSymbolErrorCntr"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint16, POINTER(c_uint32)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, fecLane, errorCounter_p)
    return ret


def mzdGetRxPcsBipErrorCntr(pDev, mdioPort, host_or_line, laneOffset, pcs_lane, errorCounter_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param pcs_lane: argument type c_uint16
    :param errorCounter_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdGetRxPcsBipErrorCntr"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint16, POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, pcs_lane, errorCounter_p)
    return ret


def mzdSetRsFecSERControl(pDev, mdioPort, host_or_line, laneOffset, degradedSEREnable, bypassIndicationEnable):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param degradedSEREnable: argument type c_uint16
    :param bypassIndicationEnable: argument type c_uint16
    """
    func = MZDAPILib["mzdSetRsFecSERControl"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint16, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, degradedSEREnable, bypassIndicationEnable)
    return ret


def mzdGetRsFecSERControl(pDev, mdioPort, host_or_line, laneOffset, degradedSEREnable_p, bypassIndicationEnable_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param degradedSEREnable_p: A pointer of c_uint16
    :param bypassIndicationEnable_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdGetRsFecSERControl"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_uint16), POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, degradedSEREnable_p, bypassIndicationEnable_p)
    return ret


def mzdSetRsFecSERThresholds(pDev, mdioPort, host_or_line, laneOffset, serActivateThreshold, serDeactivateThreshold, serInterval):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param serActivateThreshold: argument type c_uint32
    :param serDeactivateThreshold: argument type c_uint32
    :param serInterval: argument type c_uint32
    """
    func = MZDAPILib["mzdSetRsFecSERThresholds"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint32, c_uint32, c_uint32]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, serActivateThreshold, serDeactivateThreshold, serInterval)
    return ret


def mzdGetRsFecSERThresholds(pDev, mdioPort, host_or_line, laneOffset, serActivateThreshold_p, serDeactivateThreshold_p, serInterval_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param serActivateThreshold_p: A pointer of c_uint32
    :param serDeactivateThreshold_p: A pointer of c_uint32
    :param serInterval_p: A pointer of c_uint32
    """
    func = MZDAPILib["mzdGetRsFecSERThresholds"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_uint32), POINTER(c_uint32), POINTER(c_uint32)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, serActivateThreshold_p, serDeactivateThreshold_p, serInterval_p)
    return ret


def mzdGetRsFecDegradedSERStatus(pDev, mdioPort, host_or_line, laneOffset, localDegradedSerRcvd_p, remoteDegradedSerRcvd_p, serDegraded_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param localDegradedSerRcvd_p: A pointer of c_uint16
    :param remoteDegradedSerRcvd_p: A pointer of c_uint16
    :param serDegraded_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdGetRsFecDegradedSERStatus"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_uint16), POINTER(c_uint16), POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, localDegradedSerRcvd_p, remoteDegradedSerRcvd_p, serDegraded_p)
    return ret


def mzdSetKrFecControl(pDev, mdioPort, host_or_line, laneOffset, bypassIndicationEnable):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param bypassIndicationEnable: argument type c_uint16
    """
    func = MZDAPILib["mzdSetKrFecControl"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, bypassIndicationEnable)
    return ret


def mzdGetKrFecControl(pDev, mdioPort, host_or_line, laneOffset, bypassIndicationEnable_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param bypassIndicationEnable_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdGetKrFecControl"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, bypassIndicationEnable_p)
    return ret


def mzdGetKrFecAbility(pDev, mdioPort, host_or_line, laneOffset, krFecAbility_p, errIndicationAbility_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param krFecAbility_p: A pointer of c_uint16
    :param errIndicationAbility_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdGetKrFecAbility"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_uint16), POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, krFecAbility_p, errIndicationAbility_p)
    return ret


def mzdGetKrFecCorrectedBlkCntr(pDev, mdioPort, host_or_line, laneOffset, blockCounter_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param blockCounter_p: A pointer of c_uint32
    """
    func = MZDAPILib["mzdGetKrFecCorrectedBlkCntr"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_uint32)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, blockCounter_p)
    return ret


def mzdGetKrFecUnCorrectedBlkCntr(pDev, mdioPort, host_or_line, laneOffset, blockCounter_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param blockCounter_p: A pointer of c_uint32
    """
    func = MZDAPILib["mzdGetKrFecUnCorrectedBlkCntr"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_uint32)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, blockCounter_p)
    return ret


def mzdFECCounterEnable(pDev, mdioPort, host_or_line, laneOffset, enable, readToClear):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param enable: argument type c_uint16
    :param readToClear: member from enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdFECCounterEnable"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint16, c_int]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, enable, readToClear)
    return ret


def mzdFECCounterSnapshot(pDev, mdioPort, host_or_line):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    """
    func = MZDAPILib["mzdFECCounterSnapshot"]
    func.argtypes = [c_void_p, c_uint16, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line)
    return ret


def mzdFECCounterReset(pDev, mdioPort, host_or_line, laneOffset):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    """
    func = MZDAPILib["mzdFECCounterReset"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset)
    return ret


def mzdFECReadCodewordCounters(pDev, mdioPort, host_or_line, laneOffset, numCodeWords_p, numUncorrectable_p, numCorrected_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param numCodeWords_p: A pointer of c_uint64
    :param numUncorrectable_p: A pointer of c_uint32
    :param numCorrected_p: A pointer of c_uint32
    """
    func = MZDAPILib["mzdFECReadCodewordCounters"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_uint64), POINTER(c_uint32), POINTER(c_uint32)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, numCodeWords_p, numUncorrectable_p, numCorrected_p)
    return ret


def mzdFECReadBurstSymbolErrorCtrs(pDev, mdioPort, host_or_line, laneOffset, burst2Symbols_p, burst3Symbols_p, burst4Symbols_p, burst5Symbols_p, burst6Symbols_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param burst2Symbols_p: A pointer of c_uint32
    :param burst3Symbols_p: A pointer of c_uint16
    :param burst4Symbols_p: A pointer of c_uint16
    :param burst5Symbols_p: A pointer of c_uint16
    :param burst6Symbols_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdFECReadBurstSymbolErrorCtrs"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_uint32), POINTER(c_uint16), POINTER(c_uint16), POINTER(c_uint16), POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, burst2Symbols_p, burst3Symbols_p, burst4Symbols_p, burst5Symbols_p, burst6Symbols_p)
    return ret


def mzdFECReadSymbolErrorCounters(pDev, mdioPort, host_or_line, laneOffset, symbolErrorCounters0to1_p, symbolErrorCounters2to4_p, symbolErrorCounters5to15_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param symbolErrorCounters0to1_p: A pointer of c_uint64
    :param symbolErrorCounters2to4_p: A pointer of c_uint32
    :param symbolErrorCounters5to15_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdFECReadSymbolErrorCounters"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_uint64), POINTER(c_uint32), POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, symbolErrorCounters0to1_p, symbolErrorCounters2to4_p, symbolErrorCounters5to15_p)
    return ret


def mzdFirmwareDownload(pDev, fwImageData_p, fwImageSize, errCode_p):
    """
    :param pDev: argument type c_void_p
    :param fwImageData_p: A pointer of c_uint8
    :param fwImageSize: argument type c_uint32
    :param errCode_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdFirmwareDownload"]
    func.argtypes = [c_void_p, POINTER(c_uint8), c_uint32, POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, fwImageData_p, fwImageSize, errCode_p)
    return ret


def mzdUpdateFlashImage(pDev, fwImageData_p, fwImageSize, slaveData_p, slaveSize, errCode_p):
    """
    :param pDev: argument type c_void_p
    :param fwImageData_p: A pointer of c_uint8
    :param fwImageSize: argument type c_uint32
    :param slaveData_p: A pointer of c_uint8
    :param slaveSize: argument type c_uint32
    :param errCode_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdUpdateFlashImage"]
    func.argtypes = [c_void_p, POINTER(c_uint8), c_uint32, POINTER(c_uint8), c_uint32, POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, fwImageData_p, fwImageSize, slaveData_p, slaveSize, errCode_p)
    return ret


def mzdParallelFirmwareDownload(pDev_p, numPorts, fwImageData_p, fwImageSize, pErrDev_p, errCode_p):
    """
    :param pDev: argument type c_void_p
    :param numPorts: argument type c_uint16
    :param fwImageData_p: A pointer of c_uint8
    :param fwImageSize: argument type c_uint32
    :param pErrDev: argument type c_void_p
    :param errCode_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdParallelFirmwareDownload"]
    func.argtypes = [c_void_p, c_uint16, POINTER(c_uint8), c_uint32, c_void_p, POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev_p, numPorts, fwImageData_p, fwImageSize, pErrDev_p, errCode_p)
    return ret


def mzdParallelUpdateFlashImage(pDev_p, numPorts, fwImageData_p, fwImageSize, slaveData_p, slaveSize, pErrDev_p, errCode_p):
    """
    :param pDev: argument type c_void_p
    :param numPorts: argument type c_uint16
    :param fwImageData_p: A pointer of c_uint8
    :param fwImageSize: argument type c_uint32
    :param slaveData_p: A pointer of c_uint8
    :param slaveSize: argument type c_uint32
    :param pErrDev: argument type c_void_p
    :param errCode_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdParallelUpdateFlashImage"]
    func.argtypes = [c_void_p, c_uint16, POINTER(c_uint8), c_uint32, POINTER(c_uint8), c_uint32, c_void_p, POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev_p, numPorts, fwImageData_p, fwImageSize, slaveData_p, slaveSize, pErrDev_p, errCode_p)
    return ret


def mzdLoadFlashImageToRAM(pDev, errCode_p):
    """
    :param pDev: argument type c_void_p
    :param errCode_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdLoadFlashImageToRAM"]
    func.argtypes = [c_void_p, POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, errCode_p)
    return ret


def mzdHwAPBusRead(pDev, regAPBAddr, data_p):
    """
    :param pDev: argument type c_void_p
    :param regAPBAddr: argument type c_uint32
    :param data_p: A pointer of c_uint32
    """
    func = MZDAPILib["mzdHwAPBusRead"]
    func.argtypes = [c_void_p, c_uint32, POINTER(c_uint32)]
    func.restype = c_uint32
    ret = func(pDev, regAPBAddr, data_p)
    return ret


def mzdHwAPBusWrite(pDev, regAPBAddr, data):
    """
    :param pDev: argument type c_void_p
    :param regAPBAddr: argument type c_uint32
    :param data: argument type c_uint32
    """
    func = MZDAPILib["mzdHwAPBusWrite"]
    func.argtypes = [c_void_p, c_uint32, c_uint32]
    func.restype = c_uint32
    ret = func(pDev, regAPBAddr, data)
    return ret


def mzdHwAPBusWriteBlock(pDev, regAPBAddr, data_p, size):
    """
    :param pDev: argument type c_void_p
    :param regAPBAddr: argument type c_uint32
    :param data_p: A pointer of c_uint32
    :param size: argument type c_uint32
    """
    func = MZDAPILib["mzdHwAPBusWriteBlock"]
    func.argtypes = [c_void_p, c_uint32, POINTER(c_uint32), c_uint32]
    func.restype = c_uint32
    ret = func(pDev, regAPBAddr, data_p, size)
    return ret


def mzdHwAPBusReadBlock(pDev, regAPBAddr, size, data_p):
    """
    :param pDev: argument type c_void_p
    :param regAPBAddr: argument type c_uint32
    :param size: argument type c_uint32
    :param data_p: A pointer of c_uint32
    """
    func = MZDAPILib["mzdHwAPBusReadBlock"]
    func.argtypes = [c_void_p, c_uint32, c_uint32, POINTER(c_uint32)]
    func.restype = c_uint32
    ret = func(pDev, regAPBAddr, size, data_p)
    return ret


def mzdHwAPBusSetRegField(pDev, regAPBAddr, fieldOffset, fieldLength, data):
    """
    :param pDev: argument type c_void_p
    :param regAPBAddr: argument type c_uint32
    :param fieldOffset: argument type c_uint8
    :param fieldLength: argument type c_uint8
    :param data: argument type c_uint32
    """
    func = MZDAPILib["mzdHwAPBusSetRegField"]
    func.argtypes = [c_void_p, c_uint32, c_uint8, c_uint8, c_uint32]
    func.restype = c_uint32
    ret = func(pDev, regAPBAddr, fieldOffset, fieldLength, data)
    return ret


def mzdHwAPBusGetRegField(pDev, regAPBAddr, fieldOffset, fieldLength, data_p):
    """
    :param pDev: argument type c_void_p
    :param regAPBAddr: argument type c_uint32
    :param fieldOffset: argument type c_uint8
    :param fieldLength: argument type c_uint8
    :param data_p: A pointer of c_uint32
    """
    func = MZDAPILib["mzdHwAPBusGetRegField"]
    func.argtypes = [c_void_p, c_uint32, c_uint8, c_uint8, POINTER(c_uint32)]
    func.restype = c_uint32
    ret = func(pDev, regAPBAddr, fieldOffset, fieldLength, data_p)
    return ret


def mzdHwLockAPBSemaphore(pDev, semOption):
    """
    :param pDev: argument type c_void_p
    :param semOption: argument type c_uint16
    """
    func = MZDAPILib["mzdHwLockAPBSemaphore"]
    func.argtypes = [c_void_p, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, semOption)
    return ret


def mzdHwReleaseAPBSemaphore(pDev, semOption):
    """
    :param pDev: argument type c_void_p
    :param semOption: argument type c_uint16
    """
    func = MZDAPILib["mzdHwReleaseAPBSemaphore"]
    func.argtypes = [c_void_p, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, semOption)
    return ret


def mzdHwAPBSemaphoreConfig(pDev, semConfigOption):
    """
    :param pDev: argument type c_void_p
    :param semConfigOption: argument type c_uint16
    """
    func = MZDAPILib["mzdHwAPBSemaphoreConfig"]
    func.argtypes = [c_void_p, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, semConfigOption)
    return ret


def mzdHwXmdioWrite(pDev, mdioPort, dev, reg, value):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param dev: argument type c_uint16
    :param reg: argument type c_uint16
    :param value: argument type c_uint16
    """
    func = MZDAPILib["mzdHwXmdioWrite"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, dev, reg, value)
    return ret


def mzdHwXmdioRead(pDev, mdioPort, dev, reg, data_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param dev: argument type c_uint16
    :param reg: argument type c_uint16
    :param data_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdHwXmdioRead"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, dev, reg, data_p)
    return ret


def mzdHwGetPhyRegField(pDev, mdioPort, dev, regAddr, fieldOffset, fieldLength, data_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param dev: argument type c_uint16
    :param regAddr: argument type c_uint16
    :param fieldOffset: argument type c_uint8
    :param fieldLength: argument type c_uint8
    :param data_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdHwGetPhyRegField"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint8, c_uint8, POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, dev, regAddr, fieldOffset, fieldLength, data_p)
    return ret


def mzdHwSetPhyRegField(pDev, mdioPort, dev, regAddr, fieldOffset, fieldLength, data):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param dev: argument type c_uint16
    :param regAddr: argument type c_uint16
    :param fieldOffset: argument type c_uint8
    :param fieldLength: argument type c_uint8
    :param data: argument type c_uint16
    """
    func = MZDAPILib["mzdHwSetPhyRegField"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint8, c_uint8, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, dev, regAddr, fieldOffset, fieldLength, data)
    return ret


def mzdHwGetRegFieldFromWord(regData, fieldOffset, fieldLength, data_p):
    """
    :param regData: argument type c_uint16
    :param fieldOffset: argument type c_uint8
    :param fieldLength: argument type c_uint8
    :param data_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdHwGetRegFieldFromWord"]
    func.argtypes = [c_uint16, c_uint8, c_uint8, POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(regData, fieldOffset, fieldLength, data_p)
    return ret


def mzdHwSetRegFieldToWord(regData, bitFieldData, fieldOffset, fieldLength, data_p):
    """
    :param regData: argument type c_uint16
    :param bitFieldData: argument type c_uint16
    :param fieldOffset: argument type c_uint8
    :param fieldLength: argument type c_uint8
    :param data_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdHwSetRegFieldToWord"]
    func.argtypes = [c_uint16, c_uint16, c_uint8, c_uint8, POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(regData, bitFieldData, fieldOffset, fieldLength, data_p)
    return ret


def mzdHwWaitForRegFieldValue(pDev, mdioPort, dev, regAddr, fieldOffset, fieldLength, expectedValue, timeoutMs):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param dev: argument type c_uint16
    :param regAddr: argument type c_uint16
    :param fieldOffset: argument type c_uint8
    :param fieldLength: argument type c_uint8
    :param expectedValue: argument type c_uint16
    :param timeoutMs: argument type c_uint16
    """
    func = MZDAPILib["mzdHwWaitForRegFieldValue"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint8, c_uint8, c_uint16, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, dev, regAddr, fieldOffset, fieldLength, expectedValue, timeoutMs)
    return ret


def mzdHwWaitForRegFieldValueList(pDev, mdioPort, dev, regAddr, fieldOffset, fieldLength, expectedValueList_p, numOfExpValue, timeoutMs, fieldValue_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param dev: argument type c_uint16
    :param regAddr: argument type c_uint16
    :param fieldOffset: argument type c_uint8
    :param fieldLength: argument type c_uint8
    :param expectedValueList_p: A pointer of c_uint16
    :param numOfExpValue: argument type c_uint16
    :param timeoutMs: argument type c_uint16
    :param fieldValue_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdHwWaitForRegFieldValueList"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint8, c_uint8, POINTER(c_uint16), c_uint16, c_uint16, POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, dev, regAddr, fieldOffset, fieldLength, expectedValueList_p, numOfExpValue, timeoutMs, fieldValue_p)
    return ret


def mzdHwXmdioBlockWrite(pDev, mdioPort, dev, reg, data_p, dataSize):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param dev: argument type c_uint16
    :param reg: argument type c_uint16
    :param data_p: A pointer of c_uint8
    :param dataSize: argument type c_uint32
    """
    func = MZDAPILib["mzdHwXmdioBlockWrite"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_uint8), c_uint32]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, dev, reg, data_p, dataSize)
    return ret


def mzdWait(pDev, waitTime):
    """
    :param pDev: argument type c_void_p
    :param waitTime: argument type c_uint
    """
    func = MZDAPILib["mzdWait"]
    func.argtypes = [c_void_p, c_uint]
    func.restype = c_uint32
    ret = func(pDev, waitTime)
    return ret


def mzdMacSecMappedDevAddr(deviceId, deviceNum, firstOffset, lastOffset, HostContext_p, platfromFirstOffset_p, platfromLastOffset_p):
    """
    :param deviceId: argument type c_uint32
    :param deviceNum: argument type c_uint32
    :param firstOffset: argument type c_uint32
    :param lastOffset: argument type c_uint32
    :param HostContext: argument type c_void_p
    :param platfromFirstOffset_p: A pointer of c_uint32
    :param platfromLastOffset_p: A pointer of c_uint32
    """
    func = MZDAPILib["mzdMacSecMappedDevAddr"]
    func.argtypes = [c_uint32, c_uint32, c_uint32, c_uint32, c_void_p, POINTER(c_uint32), POINTER(c_uint32)]
    func.restype = c_uint32
    ret = func(deviceId, deviceNum, firstOffset, lastOffset, HostContext_p, platfromFirstOffset_p, platfromLastOffset_p)
    return ret


def mzdSetMacSecDevInfo(pDev, macsecMapPort, macsecLane):
    """
    :param pDev: argument type c_void_p
    :param macsecMapPort: argument type c_uint16
    :param macsecLane: argument type c_uint16
    """
    func = MZDAPILib["mzdSetMacSecDevInfo"]
    func.argtypes = [c_void_p, c_uint16, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, macsecMapPort, macsecLane)
    return ret


def mzdHwMacSecRegWrite(pDev, macsecMapPort, macsecAddr, data):
    """
    :param pDev: argument type c_void_p
    :param macsecMapPort: argument type c_uint16
    :param macsecAddr: argument type c_uint32
    :param data: argument type c_uint32
    """
    func = MZDAPILib["mzdHwMacSecRegWrite"]
    func.argtypes = [c_void_p, c_uint16, c_uint32, c_uint32]
    func.restype = c_uint32
    ret = func(pDev, macsecMapPort, macsecAddr, data)
    return ret


def mzdHwMacSecRegRead(pDev, macsecMapPort, macsecAddr, data_p):
    """
    :param pDev: argument type c_void_p
    :param macsecMapPort: argument type c_uint16
    :param macsecAddr: argument type c_uint32
    :param data_p: A pointer of c_uint32
    """
    func = MZDAPILib["mzdHwMacSecRegRead"]
    func.argtypes = [c_void_p, c_uint16, c_uint32, POINTER(c_uint32)]
    func.restype = c_uint32
    ret = func(pDev, macsecMapPort, macsecAddr, data_p)
    return ret


def mzdHwSetMacSecRegField(pDev, macsecMapPort, macsecAddr, fieldOffset, fieldLength, data):
    """
    :param pDev: argument type c_void_p
    :param macsecMapPort: argument type c_uint16
    :param macsecAddr: argument type c_uint32
    :param fieldOffset: argument type c_uint8
    :param fieldLength: argument type c_uint8
    :param data: argument type c_uint32
    """
    func = MZDAPILib["mzdHwSetMacSecRegField"]
    func.argtypes = [c_void_p, c_uint16, c_uint32, c_uint8, c_uint8, c_uint32]
    func.restype = c_uint32
    ret = func(pDev, macsecMapPort, macsecAddr, fieldOffset, fieldLength, data)
    return ret


def mzdHwGetMacSecRegField(pDev, macsecMapPort, macsecAddr, fieldOffset, fieldLength, data_p):
    """
    :param pDev: argument type c_void_p
    :param macsecMapPort: argument type c_uint16
    :param macsecAddr: argument type c_uint32
    :param fieldOffset: argument type c_uint8
    :param fieldLength: argument type c_uint8
    :param data_p: A pointer of c_uint32
    """
    func = MZDAPILib["mzdHwGetMacSecRegField"]
    func.argtypes = [c_void_p, c_uint16, c_uint32, c_uint8, c_uint8, POINTER(c_uint32)]
    func.restype = c_uint32
    ret = func(pDev, macsecMapPort, macsecAddr, fieldOffset, fieldLength, data_p)
    return ret


def mzdHwMacSecSBUFRegWrite(pDev, macsecMapPort, macsecAddr, data):
    """
    :param pDev: argument type c_void_p
    :param macsecMapPort: argument type c_uint16
    :param macsecAddr: argument type c_uint32
    :param data: argument type c_uint32
    """
    func = MZDAPILib["mzdHwMacSecSBUFRegWrite"]
    func.argtypes = [c_void_p, c_uint16, c_uint32, c_uint32]
    func.restype = c_uint32
    ret = func(pDev, macsecMapPort, macsecAddr, data)
    return ret


def mzdHwMacSecSBUFRegRead(pDev, macsecMapPort, macsecAddr, data_p):
    """
    :param pDev: argument type c_void_p
    :param macsecMapPort: argument type c_uint16
    :param macsecAddr: argument type c_uint32
    :param data_p: A pointer of c_uint32
    """
    func = MZDAPILib["mzdHwMacSecSBUFRegRead"]
    func.argtypes = [c_void_p, c_uint16, c_uint32, POINTER(c_uint32)]
    func.restype = c_uint32
    ret = func(pDev, macsecMapPort, macsecAddr, data_p)
    return ret


def mzdHwSetMacSecSBUFRegField(pDev, macsecMapPort, macsecAddr, fieldOffset, fieldLength, data):
    """
    :param pDev: argument type c_void_p
    :param macsecMapPort: argument type c_uint16
    :param macsecAddr: argument type c_uint32
    :param fieldOffset: argument type c_uint8
    :param fieldLength: argument type c_uint8
    :param data: argument type c_uint32
    """
    func = MZDAPILib["mzdHwSetMacSecSBUFRegField"]
    func.argtypes = [c_void_p, c_uint16, c_uint32, c_uint8, c_uint8, c_uint32]
    func.restype = c_uint32
    ret = func(pDev, macsecMapPort, macsecAddr, fieldOffset, fieldLength, data)
    return ret


def mzdHwGetMacSecSBUFRegField(pDev, macsecMapPort, macsecAddr, fieldOffset, fieldLength, data_p):
    """
    :param pDev: argument type c_void_p
    :param macsecMapPort: argument type c_uint16
    :param macsecAddr: argument type c_uint32
    :param fieldOffset: argument type c_uint8
    :param fieldLength: argument type c_uint8
    :param data_p: A pointer of c_uint32
    """
    func = MZDAPILib["mzdHwGetMacSecSBUFRegField"]
    func.argtypes = [c_void_p, c_uint16, c_uint32, c_uint8, c_uint8, POINTER(c_uint32)]
    func.restype = c_uint32
    ret = func(pDev, macsecMapPort, macsecAddr, fieldOffset, fieldLength, data_p)
    return ret


def mzdHwMacRegWrite(pDev, macMapPort, host_or_line, macAddr, data):
    """
    :param pDev: argument type c_void_p
    :param macMapPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param macAddr: argument type c_uint32
    :param data: argument type c_uint32
    """
    func = MZDAPILib["mzdHwMacRegWrite"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint32, c_uint32]
    func.restype = c_uint32
    ret = func(pDev, macMapPort, host_or_line, macAddr, data)
    return ret


def mzdHwMacRegRead(pDev, macMapPort, host_or_line, macAddr, data_p):
    """
    :param pDev: argument type c_void_p
    :param macMapPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param macAddr: argument type c_uint32
    :param data_p: A pointer of c_uint32
    """
    func = MZDAPILib["mzdHwMacRegRead"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint32, POINTER(c_uint32)]
    func.restype = c_uint32
    ret = func(pDev, macMapPort, host_or_line, macAddr, data_p)
    return ret


def mzdHwSetMacRegField(pDev, macMapPort, host_or_line, macAddr, fieldOffset, fieldLength, data):
    """
    :param pDev: argument type c_void_p
    :param macMapPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param macAddr: argument type c_uint32
    :param fieldOffset: argument type c_uint8
    :param fieldLength: argument type c_uint8
    :param data: argument type c_uint32
    """
    func = MZDAPILib["mzdHwSetMacRegField"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint32, c_uint8, c_uint8, c_uint32]
    func.restype = c_uint32
    ret = func(pDev, macMapPort, host_or_line, macAddr, fieldOffset, fieldLength, data)
    return ret


def mzdHwGetMacRegField(pDev, macMapPort, host_or_line, macAddr, fieldOffset, fieldLength, data_p):
    """
    :param pDev: argument type c_void_p
    :param macMapPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param macAddr: argument type c_uint32
    :param fieldOffset: argument type c_uint8
    :param fieldLength: argument type c_uint8
    :param data_p: A pointer of c_uint32
    """
    func = MZDAPILib["mzdHwGetMacRegField"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint32, c_uint8, c_uint8, POINTER(c_uint32)]
    func.restype = c_uint32
    ret = func(pDev, macMapPort, host_or_line, macAddr, fieldOffset, fieldLength, data_p)
    return ret


def mzdInitSerdesDev(pDev, serdesRead_p, serdesWrite_p):
    """
    :param pDev: argument type c_void_p
    :param serdesRead: a function pointer
    :param serdesWrite: a function pointer
    """
    func = MZDAPILib["mzdInitSerdesDev"]
    func.argtypes = [c_void_p, CFUNCTYPE(c_void_p, c_uint32, POINTER(c_uint32)), CFUNCTYPE(c_void_p, c_uint32, c_uint32)]
    func.restype = c_uint32
    ret = func(pDev, serdesRead_p, serdesWrite_p)
    return ret


def mzdSetSerdesDevInfo(pDev, serdesMapPort, serdesMapHostLine):
    """
    :param pDev: argument type c_void_p
    :param serdesMapPort: argument type c_uint16
    :param serdesMapHostLine: argument type c_uint16
    """
    func = MZDAPILib["mzdSetSerdesDevInfo"]
    func.argtypes = [c_void_p, c_uint16, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, serdesMapPort, serdesMapHostLine)
    return ret


def mzdHwSerdesPhyRegWrite(pDev, mdioPort, host_or_line, serdesLane, regAddr, data):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param serdesLane: argument type c_uint16
    :param regAddr: argument type c_uint32
    :param data: argument type c_uint32
    """
    func = MZDAPILib["mzdHwSerdesPhyRegWrite"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint32, c_uint32]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, serdesLane, regAddr, data)
    return ret


def mzdHwSerdesPhyRegRead(pDev, mdioPort, host_or_line, serdesLane, regAddr, data_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param serdesLane: argument type c_uint16
    :param regAddr: argument type c_uint32
    :param data_p: A pointer of c_uint32
    """
    func = MZDAPILib["mzdHwSerdesPhyRegRead"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint32, POINTER(c_uint32)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, serdesLane, regAddr, data_p)
    return ret


def mzdHwSetSerdesPhyRegField(pDev, mdioPort, host_or_line, serdesLane, regAddr, fieldOffset, fieldLength, data):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param serdesLane: argument type c_uint16
    :param regAddr: argument type c_uint32
    :param fieldOffset: argument type c_uint8
    :param fieldLength: argument type c_uint8
    :param data: argument type c_uint32
    """
    func = MZDAPILib["mzdHwSetSerdesPhyRegField"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint32, c_uint8, c_uint8, c_uint32]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, serdesLane, regAddr, fieldOffset, fieldLength, data)
    return ret


def mzdHwGetSerdesPhyRegField(pDev, mdioPort, host_or_line, serdesLane, regAddr, fieldOffset, fieldLength, data_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param serdesLane: argument type c_uint16
    :param regAddr: argument type c_uint32
    :param fieldOffset: argument type c_uint8
    :param fieldLength: argument type c_uint8
    :param data_p: A pointer of c_uint32
    """
    func = MZDAPILib["mzdHwGetSerdesPhyRegField"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint32, c_uint8, c_uint8, POINTER(c_uint32)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, serdesLane, regAddr, fieldOffset, fieldLength, data_p)
    return ret


def mzdHwSerdesPhyLaneRegBroadcast(pDev, mdioPort, host_or_line, enable):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param enable: argument type c_uint32
    """
    func = MZDAPILib["mzdHwSerdesPhyLaneRegBroadcast"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint32]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, enable)
    return ret


def mzdInitDriver(mzdFuncReadMdio_p, mzdFuncWriteMdio_p, mzdFuncWait_p, serdesRead_p, serdesWrite_p, mdioPort, pFirmwareImage_p, firmwareSize, pHostContext, pDev):
    """
    :param mzdFuncReadMdio: a function pointer
    :param mzdFuncWriteMdio: a function pointer
    :param mzdFuncWait: a function pointer
    :param serdesRead: a function pointer
    :param serdesWrite: a function pointer
    :param mdioPort: argument type c_uint16
    :param pFirmwareImage_p: A pointer of c_uint8
    :param firmwareSize: argument type c_uint32
    :param pHostContext: argument type c_void_p
    :param pDev: argument type c_void_p
    """
    func = MZDAPILib["mzdInitDriver"]
    func.argtypes = [CFUNCTYPE(c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_uint16)), CFUNCTYPE(c_void_p, c_uint16, c_uint16, c_uint16, c_uint16), CFUNCTYPE(c_void_p, c_uint), CFUNCTYPE(c_void_p, c_uint32, POINTER(c_uint32)), CFUNCTYPE(c_void_p, c_uint32, c_uint32), c_uint16, POINTER(c_uint8), c_uint32, c_void_p, c_void_p]
    func.restype = c_uint32
    ret = func(mzdFuncReadMdio_p, mzdFuncWriteMdio_p, mzdFuncWait_p, serdesRead_p, serdesWrite_p, mdioPort, pFirmwareImage_p, firmwareSize, pHostContext, pDev)
    return ret


def mzdReloadDriver(mzdFuncReadMdio_p, mzdFuncWriteMdio_p, mzdFuncWait_p, serdesRead_p, serdesWrite_p, mdioPort, pHostContext, optionFlag, pDev):
    """
    :param mzdFuncReadMdio: a function pointer
    :param mzdFuncWriteMdio: a function pointer
    :param mzdFuncWait: a function pointer
    :param serdesRead: a function pointer
    :param serdesWrite: a function pointer
    :param mdioPort: argument type c_uint16
    :param pHostContext: argument type c_void_p
    :param optionFlag: argument type c_uint16
    :param pDev: argument type c_void_p
    """
    func = MZDAPILib["mzdReloadDriver"]
    func.argtypes = [CFUNCTYPE(c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_uint16)), CFUNCTYPE(c_void_p, c_uint16, c_uint16, c_uint16, c_uint16), CFUNCTYPE(c_void_p, c_uint), CFUNCTYPE(c_void_p, c_uint32, POINTER(c_uint32)), CFUNCTYPE(c_void_p, c_uint32, c_uint32), c_uint16, c_void_p, c_uint16, c_void_p]
    func.restype = c_uint32
    ret = func(mzdFuncReadMdio_p, mzdFuncWriteMdio_p, mzdFuncWait_p, serdesRead_p, serdesWrite_p, mdioPort, pHostContext, optionFlag, pDev)
    return ret


def mzdUnloadDriver(pDev):
    """
    :param pDev: argument type c_void_p
    """
    func = MZDAPILib["mzdUnloadDriver"]
    func.argtypes = [c_void_p]
    func.restype = c_uint32
    ret = func(pDev)
    return ret


def mzdLanePowerdown(pDev, mdioPort, host_or_line, laneOffset):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    """
    func = MZDAPILib["mzdLanePowerdown"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset)
    return ret


def mzdLanePowerup(pDev, mdioPort, host_or_line, laneOffset):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    """
    func = MZDAPILib["mzdLanePowerup"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset)
    return ret


def mzdPortReset(pDev, mdioPort, host_or_line, resetType, timeoutMs):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param resetType: member from enumerate class MZD_RESET_TYPE
    :param timeoutMs: argument type c_uint16
    """
    func = MZDAPILib["mzdPortReset"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_int, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, resetType, timeoutMs)
    return ret


def mzdChipResetControl(pDev, resetType, bRestore):
    """
    :param pDev: argument type c_void_p
    :param resetType: argument type c_uint16
    :param bRestore: member from enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdChipResetControl"]
    func.argtypes = [c_void_p, c_uint16, c_int]
    func.restype = c_uint32
    ret = func(pDev, resetType, bRestore)
    return ret


def mzdGetIntrSrcStatus(pDev, intrSelector, forceInterrupt_p, intrSrc_p):
    """
    :param pDev: argument type c_void_p
    :param intrSelector: implementation of the structure class MZD_GLOBAL_CHIP_INTR
    :param forceInterrupt_p: A pointer of the enumerate class MZD_BOOL
    :param intrSrc_p: A pointer of the structure class MZD_GLOBAL_CHIP_INTR
    """
    func = MZDAPILib["mzdGetIntrSrcStatus"]
    func.argtypes = [c_void_p, MZD_GLOBAL_CHIP_INTR, POINTER(c_int), POINTER(MZD_GLOBAL_CHIP_INTR)]
    func.restype = c_uint32
    ret = func(pDev, intrSelector, forceInterrupt_p, intrSrc_p)
    return ret


def mzdSetGlobalInterruptCntl(pDev, openDrain, intrPolarity, forceInterrupt):
    """
    :param pDev: argument type c_void_p
    :param openDrain: member from enumerate class MZD_BOOL
    :param intrPolarity: argument type c_uint16
    :param forceInterrupt: member from enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdSetGlobalInterruptCntl"]
    func.argtypes = [c_void_p, c_int, c_uint16, c_int]
    func.restype = c_uint32
    ret = func(pDev, openDrain, intrPolarity, forceInterrupt)
    return ret


def mzdGetGlobalInterruptCntl(pDev, openDrain_p, intrPolarity_p, forceInterrupt_p):
    """
    :param pDev: argument type c_void_p
    :param openDrain_p: A pointer of the enumerate class MZD_BOOL
    :param intrPolarity_p: A pointer of c_uint16
    :param forceInterrupt_p: A pointer of the enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdGetGlobalInterruptCntl"]
    func.argtypes = [c_void_p, POINTER(c_int), POINTER(c_uint16), POINTER(c_int)]
    func.restype = c_uint32
    ret = func(pDev, openDrain_p, intrPolarity_p, forceInterrupt_p)
    return ret


def mzdSetGlobalInterruptEnable(pDev, globalAggregatedIntrEnable1, globalAggregatedIntrEnable2):
    """
    :param pDev: argument type c_void_p
    :param globalAggregatedIntrEnable1: argument type c_uint16
    :param globalAggregatedIntrEnable2: argument type c_uint16
    """
    func = MZDAPILib["mzdSetGlobalInterruptEnable"]
    func.argtypes = [c_void_p, c_uint16, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, globalAggregatedIntrEnable1, globalAggregatedIntrEnable2)
    return ret


def mzdGetGlobalInterruptEnable(pDev, globalAggregatedIntrEnable1_p, globalAggregatedIntrEnable2_p):
    """
    :param pDev: argument type c_void_p
    :param globalAggregatedIntrEnable1_p: A pointer of c_uint16
    :param globalAggregatedIntrEnable2_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdGetGlobalInterruptEnable"]
    func.argtypes = [c_void_p, POINTER(c_uint16), POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, globalAggregatedIntrEnable1_p, globalAggregatedIntrEnable2_p)
    return ret


def mzdGetUnmaskedInterrupts(pDev, intrSelector_p):
    """
    :param pDev: argument type c_void_p
    :param intrSelector_p: A pointer of the structure class MZD_GLOBAL_CHIP_INTR
    """
    func = MZDAPILib["mzdGetUnmaskedInterrupts"]
    func.argtypes = [c_void_p, POINTER(MZD_GLOBAL_CHIP_INTR)]
    func.restype = c_uint32
    ret = func(pDev, intrSelector_p)
    return ret


def mzdSetGPIOInterruptEnable(pDev, gpioPinId, gpioIntrEnable):
    """
    :param pDev: argument type c_void_p
    :param gpioPinId: member from enumerate class MZD_PIN_ID
    :param gpioIntrEnable: argument type c_uint16
    """
    func = MZDAPILib["mzdSetGPIOInterruptEnable"]
    func.argtypes = [c_void_p, c_int, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, gpioPinId, gpioIntrEnable)
    return ret


def mzdGetGPIOInterruptEnable(pDev, gpioPinId, gpioIntrEnable_p):
    """
    :param pDev: argument type c_void_p
    :param gpioPinId: member from enumerate class MZD_PIN_ID
    :param gpioIntrEnable_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdGetGPIOInterruptEnable"]
    func.argtypes = [c_void_p, c_int, POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, gpioPinId, gpioIntrEnable_p)
    return ret


def mzdSetGPIOInterruptType(pDev, gpioPinId, gpioIntrType):
    """
    :param pDev: argument type c_void_p
    :param gpioPinId: member from enumerate class MZD_PIN_ID
    :param gpioIntrType: argument type c_uint16
    """
    func = MZDAPILib["mzdSetGPIOInterruptType"]
    func.argtypes = [c_void_p, c_int, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, gpioPinId, gpioIntrType)
    return ret


def mzdGetGPIOInterruptType(pDev, gpioPinId, gpioIntrType_p):
    """
    :param pDev: argument type c_void_p
    :param gpioPinId: member from enumerate class MZD_PIN_ID
    :param gpioIntrType_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdGetGPIOInterruptType"]
    func.argtypes = [c_void_p, c_int, POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, gpioPinId, gpioIntrType_p)
    return ret


def mzdGetGPIOInterruptStatus(pDev, gpioPinId, gpioIntrLatchedStatus_p, gpioIntrCurrentStatus_p):
    """
    :param pDev: argument type c_void_p
    :param gpioPinId: member from enumerate class MZD_PIN_ID
    :param gpioIntrLatchedStatus_p: A pointer of c_uint16
    :param gpioIntrCurrentStatus_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdGetGPIOInterruptStatus"]
    func.argtypes = [c_void_p, c_int, POINTER(c_uint16), POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, gpioPinId, gpioIntrLatchedStatus_p, gpioIntrCurrentStatus_p)
    return ret


def mzdSetPCSInterruptEnable(pDev, mdioPort, host_or_line, laneOffset, intrEnable):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param intrEnable: implementation of the structure class MZD_PCS_UNIT_INTR
    """
    func = MZDAPILib["mzdSetPCSInterruptEnable"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, MZD_PCS_UNIT_INTR]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, intrEnable)
    return ret


def mzdGetPCSInterruptEnable(pDev, mdioPort, host_or_line, laneOffset, intrEnable_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param intrEnable_p: A pointer of the structure class MZD_PCS_UNIT_INTR
    """
    func = MZDAPILib["mzdGetPCSInterruptEnable"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(MZD_PCS_UNIT_INTR)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, intrEnable_p)
    return ret


def mzdGetPCSInterruptStatus(pDev, mdioPort, host_or_line, laneOffset, latchedIntrStatus_p, currentIntrStatus_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param latchedIntrStatus_p: A pointer of the structure class MZD_PCS_UNIT_INTR
    :param currentIntrStatus_p: A pointer of the structure class MZD_PCS_UNIT_INTR
    """
    func = MZDAPILib["mzdGetPCSInterruptStatus"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(MZD_PCS_UNIT_INTR), POINTER(MZD_PCS_UNIT_INTR)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, latchedIntrStatus_p, currentIntrStatus_p)
    return ret


def mzdGetPCSRealtimeStatus(pDev, mdioPort, host_or_line, laneOffset, rtIntrStatus_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param rtIntrStatus_p: A pointer of the structure class MZD_PCS_UNIT_INTR
    """
    func = MZDAPILib["mzdGetPCSRealtimeStatus"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(MZD_PCS_UNIT_INTR)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, rtIntrStatus_p)
    return ret


def mzdSetPinMode(pDev, pinId, pinMode, openDrain):
    """
    :param pDev: argument type c_void_p
    :param pinId: member from enumerate class MZD_PIN_ID
    :param pinMode: member from enumerate class MZD_PIN_MODE
    :param openDrain: member from enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdSetPinMode"]
    func.argtypes = [c_void_p, c_int, c_int, c_int]
    func.restype = c_uint32
    ret = func(pDev, pinId, pinMode, openDrain)
    return ret


def mzdGetPinMode(pDev, pinId, pinMode_p, openDrain_p):
    """
    :param pDev: argument type c_void_p
    :param pinId: member from enumerate class MZD_PIN_ID
    :param pinMode_p: A pointer of the enumerate class MZD_PIN_MODE
    :param openDrain_p: A pointer of the enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdGetPinMode"]
    func.argtypes = [c_void_p, c_int, POINTER(c_int), POINTER(c_int)]
    func.restype = c_uint32
    ret = func(pDev, pinId, pinMode_p, openDrain_p)
    return ret


def mzdSetGPIOPinDirection(pDev, gpioPinId, gpioPinDirection):
    """
    :param pDev: argument type c_void_p
    :param gpioPinId: member from enumerate class MZD_PIN_ID
    :param gpioPinDirection: argument type c_uint16
    """
    func = MZDAPILib["mzdSetGPIOPinDirection"]
    func.argtypes = [c_void_p, c_int, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, gpioPinId, gpioPinDirection)
    return ret


def mzdGetGPIOPinDirection(pDev, gpioPinId, gpioPinDirection_p):
    """
    :param pDev: argument type c_void_p
    :param gpioPinId: member from enumerate class MZD_PIN_ID
    :param gpioPinDirection_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdGetGPIOPinDirection"]
    func.argtypes = [c_void_p, c_int, POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, gpioPinId, gpioPinDirection_p)
    return ret


def mzdSetGPIOPinData(pDev, gpioPinId, gpioData):
    """
    :param pDev: argument type c_void_p
    :param gpioPinId: member from enumerate class MZD_PIN_ID
    :param gpioData: argument type c_uint16
    """
    func = MZDAPILib["mzdSetGPIOPinData"]
    func.argtypes = [c_void_p, c_int, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, gpioPinId, gpioData)
    return ret


def mzdGetGPIOPinData(pDev, gpioPinId, gpioData_p):
    """
    :param pDev: argument type c_void_p
    :param gpioPinId: member from enumerate class MZD_PIN_ID
    :param gpioData_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdGetGPIOPinData"]
    func.argtypes = [c_void_p, c_int, POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, gpioPinId, gpioData_p)
    return ret


def mzdSetLEDControl(pDev, ledPinId, ledCtrl):
    """
    :param pDev: argument type c_void_p
    :param ledPinId: member from enumerate class MZD_PIN_ID
    :param ledCtrl: implementation of the structure class MZD_LED_CTRL
    """
    func = MZDAPILib["mzdSetLEDControl"]
    func.argtypes = [c_void_p, c_int, MZD_LED_CTRL]
    func.restype = c_uint32
    ret = func(pDev, ledPinId, ledCtrl)
    return ret


def mzdSetLEDTimer(pDev, ledTimerConfig):
    """
    :param pDev: argument type c_void_p
    :param ledTimerConfig: implementation of the structure class MZD_LED_TIMER_CONFIG
    """
    func = MZDAPILib["mzdSetLEDTimer"]
    func.argtypes = [c_void_p, MZD_LED_TIMER_CONFIG]
    func.restype = c_uint32
    ret = func(pDev, ledTimerConfig)
    return ret


def mzdConfigRClkPin(pDev, rClkPinId, portSelect, interfaceSelect, laneSelect):
    """
    :param pDev: argument type c_void_p
    :param rClkPinId: member from enumerate class MZD_PIN_ID
    :param portSelect: argument type c_uint16
    :param interfaceSelect: argument type c_uint16
    :param laneSelect: argument type c_uint16
    """
    func = MZDAPILib["mzdConfigRClkPin"]
    func.argtypes = [c_void_p, c_int, c_uint16, c_uint16, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, rClkPinId, portSelect, interfaceSelect, laneSelect)
    return ret


def mzdConfigRClkSource(pDev, portSelect, interfaceSelect, laneSelect, clockOption):
    """
    :param pDev: argument type c_void_p
    :param portSelect: argument type c_uint16
    :param interfaceSelect: argument type c_uint16
    :param laneSelect: argument type c_uint16
    :param clockOption: implementation of the structure class MZD_RCLK_SRC_OPTION
    """
    func = MZDAPILib["mzdConfigRClkSource"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, MZD_RCLK_SRC_OPTION]
    func.restype = c_uint32
    ret = func(pDev, portSelect, interfaceSelect, laneSelect, clockOption)
    return ret


def mzdMacSecMacInit(pDev, mdioPort, host_or_line, laneOffset, opMode, initOption):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param opMode: member from enumerate class MZD_OP_MODE
    :param initOption: argument type c_uint16
    """
    func = MZDAPILib["mzdMacSecMacInit"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_int, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, opMode, initOption)
    return ret


def mzdMacEnable(pDev, mdioPort, host_or_line, laneOffset, macEnable):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param macEnable: member from enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdMacEnable"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_int]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, macEnable)
    return ret


def mzdMacSecEnable(pDev, mdioPort, host_or_line, macsecEnable):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param macsecEnable: member from enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdMacSecEnable"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_int]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, macsecEnable)
    return ret


def mzdMacSetLowSpeed(pDev, mdioPort, laneOffset):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param laneOffset: argument type c_uint16
    """
    func = MZDAPILib["mzdMacSetLowSpeed"]
    func.argtypes = [c_void_p, c_uint16, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, laneOffset)
    return ret


def mzdMacSetHighSpeed(pDev, mdioPort):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    """
    func = MZDAPILib["mzdMacSetHighSpeed"]
    func.argtypes = [c_void_p, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort)
    return ret


def mzdMacSecPtpBypass(pDev, mdioPort, bypassPtp):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param bypassPtp: member from enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdMacSecPtpBypass"]
    func.argtypes = [c_void_p, c_uint16, c_int]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, bypassPtp)
    return ret


def mzdMacSecEgressBypass(pDev, mdioPort, laneOffset, egressBypass):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param egressBypass: member from enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdMacSecEgressBypass"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_int]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, laneOffset, egressBypass)
    return ret


def mzdMacSecIngressBypass(pDev, mdioPort, laneOffset, ingressBypass):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param ingressBypass: member from enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdMacSecIngressBypass"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_int]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, laneOffset, ingressBypass)
    return ret


def mzdMacBypassPPMFifo(pDev, mdioPort, bypassPPMFifo):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param bypassPPMFifo: member from enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdMacBypassPPMFifo"]
    func.argtypes = [c_void_p, c_uint16, c_int]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, bypassPPMFifo)
    return ret


def mzdMacBypassPPMFifoPushBackLatencyMatch(pDev, mdioPort, host_or_line, laneOffset, pushBackLatencyMatch):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param pushBackLatencyMatch: argument type c_uint16
    """
    func = MZDAPILib["mzdMacBypassPPMFifoPushBackLatencyMatch"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, pushBackLatencyMatch)
    return ret


def mzdMacBypassPPMFifoDelayAlignMarkerPushBack(pDev, mdioPort, host_or_line, laneOffset, pushBackDelay):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param pushBackDelay: argument type c_uint16
    """
    func = MZDAPILib["mzdMacBypassPPMFifoDelayAlignMarkerPushBack"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, pushBackDelay)
    return ret


def mzdMacMIBStatDump(pDev, mdioPort, host_or_line, laneOffset, stateDumpOptions):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param stateDumpOptions: argument type c_uint32
    """
    func = MZDAPILib["mzdMacMIBStatDump"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint32]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, stateDumpOptions)
    return ret


def mzdMacPauseFrameInjectionToHost(pDev, mdioPort, laneOffset, enable):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param enable: argument type c_uint16
    """
    func = MZDAPILib["mzdMacPauseFrameInjectionToHost"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, laneOffset, enable)
    return ret


def mzdMacSetPauseFrameToHostThreshold(pDev, mdioPort, laneOffset, lowThreshold, highThreshold):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param lowThreshold: argument type c_uint16
    :param highThreshold: argument type c_uint16
    """
    func = MZDAPILib["mzdMacSetPauseFrameToHostThreshold"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, laneOffset, lowThreshold, highThreshold)
    return ret


def mzdMacGetPauseFrameToHostThreshold(pDev, mdioPort, laneOffset, lowThreshold_p, highThreshold_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param lowThreshold_p: A pointer of c_uint16
    :param highThreshold_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdMacGetPauseFrameToHostThreshold"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, POINTER(c_uint16), POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, laneOffset, lowThreshold_p, highThreshold_p)
    return ret


def mzdMacSecHmux4ArbiterEnable(pDev, macsecMapPort, hostSideMode, lowerPortPrimary, hmux4Options):
    """
    :param pDev: argument type c_void_p
    :param macsecMapPort: argument type c_uint16
    :param hostSideMode: member from enumerate class MZD_OP_MODE
    :param lowerPortPrimary: member from enumerate class MZD_BOOL
    :param hmux4Options: argument type c_uint32
    """
    func = MZDAPILib["mzdMacSecHmux4ArbiterEnable"]
    func.argtypes = [c_void_p, c_uint16, c_int, c_int, c_uint32]
    func.restype = c_uint32
    ret = func(pDev, macsecMapPort, hostSideMode, lowerPortPrimary, hmux4Options)
    return ret


def mzdMacSecHmux8ArbiterEnable(pDev, hostSideMode, lowerPortsPrimary, hmux8Options):
    """
    :param pDev: argument type c_void_p
    :param hostSideMode: member from enumerate class MZD_OP_MODE
    :param lowerPortsPrimary: member from enumerate class MZD_BOOL
    :param hmux8Options: argument type c_uint32
    """
    func = MZDAPILib["mzdMacSecHmux8ArbiterEnable"]
    func.argtypes = [c_void_p, c_int, c_int, c_uint32]
    func.restype = c_uint32
    ret = func(pDev, hostSideMode, lowerPortsPrimary, hmux8Options)
    return ret


def mzdMacSecHmuxArbiterEnablePerLane(pDev, mdioPort, laneOffset, hostSideMode, hmuxType):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param hostSideMode: member from enumerate class MZD_OP_MODE
    :param hmuxType: argument type c_uint16
    """
    func = MZDAPILib["mzdMacSecHmuxArbiterEnablePerLane"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_int, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, laneOffset, hostSideMode, hmuxType)
    return ret


def mzdHmuxArbiterReset(pDev, mdioPort, laneOffset, arbiterSelect):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param arbiterSelect: argument type c_uint16
    """
    func = MZDAPILib["mzdHmuxArbiterReset"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, laneOffset, arbiterSelect)
    return ret


def mzdMacSecSelectHmuxType(pDev, macsecMapPort, hmuxType, lowerPortPrimary, hmuxOptions):
    """
    :param pDev: argument type c_void_p
    :param macsecMapPort: argument type c_uint16
    :param hmuxType: argument type c_uint16
    :param lowerPortPrimary: member from enumerate class MZD_BOOL
    :param hmuxOptions: argument type c_uint16
    """
    func = MZDAPILib["mzdMacSecSelectHmuxType"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_int, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, macsecMapPort, hmuxType, lowerPortPrimary, hmuxOptions)
    return ret


def mzdMacSecHmuxArbiterState(pDev, macsecMapPort, arbiterEgrState_p, arbiterIngrState_p):
    """
    :param pDev: argument type c_void_p
    :param macsecMapPort: argument type c_uint16
    :param arbiterEgrState_p: A pointer of c_uint16
    :param arbiterIngrState_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdMacSecHmuxArbiterState"]
    func.argtypes = [c_void_p, c_uint16, POINTER(c_uint16), POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, macsecMapPort, arbiterEgrState_p, arbiterIngrState_p)
    return ret


def mzdMacSecHmuxBlockBackUpIngress(pDev, macsecMapPort, blockBackUpPorts):
    """
    :param pDev: argument type c_void_p
    :param macsecMapPort: argument type c_uint16
    :param blockBackUpPorts: member from enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdMacSecHmuxBlockBackUpIngress"]
    func.argtypes = [c_void_p, c_uint16, c_int]
    func.restype = c_uint32
    ret = func(pDev, macsecMapPort, blockBackUpPorts)
    return ret


def mzdMacSecHmuxTimeOut(pDev, mdioPort, hmuxTimeOutSel, hmuxTimeOutSelOptions):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param hmuxTimeOutSel: argument type c_uint32
    :param hmuxTimeOutSelOptions: argument type c_uint32
    """
    func = MZDAPILib["mzdMacSecHmuxTimeOut"]
    func.argtypes = [c_void_p, c_uint16, c_uint32, c_uint32]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, hmuxTimeOutSel, hmuxTimeOutSelOptions)
    return ret


def mzdMacSecManualHmuxStopTraffic(pDev, macsecMapPort):
    """
    :param pDev: argument type c_void_p
    :param macsecMapPort: argument type c_uint16
    """
    func = MZDAPILib["mzdMacSecManualHmuxStopTraffic"]
    func.argtypes = [c_void_p, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, macsecMapPort)
    return ret


def mzdMacSecManualHmuxStartTraffic(pDev, macsecMapPort):
    """
    :param pDev: argument type c_void_p
    :param macsecMapPort: argument type c_uint16
    """
    func = MZDAPILib["mzdMacSecManualHmuxStartTraffic"]
    func.argtypes = [c_void_p, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, macsecMapPort)
    return ret


def mzdMacSecHmuxAutoSwitch(pDev, macsecMapPort):
    """
    :param pDev: argument type c_void_p
    :param macsecMapPort: argument type c_uint16
    """
    func = MZDAPILib["mzdMacSecHmuxAutoSwitch"]
    func.argtypes = [c_void_p, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, macsecMapPort)
    return ret


def mzdMacSecHmuxGPIOSwitchCntl(pDev, macsecMapPort, enable, edgeDetect):
    """
    :param pDev: argument type c_void_p
    :param macsecMapPort: argument type c_uint16
    :param enable: argument type c_uint16
    :param edgeDetect: argument type c_uint16
    """
    func = MZDAPILib["mzdMacSecHmuxGPIOSwitchCntl"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, macsecMapPort, enable, edgeDetect)
    return ret


def mzdMacSecHmuxLevelGPIOSwitchCntl(pDev, enable):
    """
    :param pDev: argument type c_void_p
    :param enable: argument type c_uint16
    """
    func = MZDAPILib["mzdMacSecHmuxLevelGPIOSwitchCntl"]
    func.argtypes = [c_void_p, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, enable)
    return ret


def mzdMacSecHmuxStatusOutputCntl(pDev, macsecMapPort, enable, polarity):
    """
    :param pDev: argument type c_void_p
    :param macsecMapPort: argument type c_uint16
    :param enable: argument type c_uint16
    :param polarity: argument type c_uint16
    """
    func = MZDAPILib["mzdMacSecHmuxStatusOutputCntl"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, macsecMapPort, enable, polarity)
    return ret


def mzdMacTxFifoReset(pDev, mdioPort, host_or_line, laneOffset):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    """
    func = MZDAPILib["mzdMacTxFifoReset"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset)
    return ret


def mzdMacInsertTxCRC(pDev, mdioPort, laneOffset, insertTxCRC):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param insertTxCRC: member from enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdMacInsertTxCRC"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_int]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, laneOffset, insertTxCRC)
    return ret


def mzdMacForwardRxCRC(pDev, mdioPort, laneOffset, forwardRxCRC):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param forwardRxCRC: member from enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdMacForwardRxCRC"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_int]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, laneOffset, forwardRxCRC)
    return ret


def mzdMacFlowControl(pDev, mdioPort, laneOffset, flowCntlOption, enableFlag):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param flowCntlOption: argument type c_uint16
    :param enableFlag: argument type c_uint16
    """
    func = MZDAPILib["mzdMacFlowControl"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, laneOffset, flowCntlOption, enableFlag)
    return ret


def mzdSetMacLaneInterruptEnable(pDev, mdioPort, host_or_line, laneOffset, intrEnable):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param intrEnable: argument type c_uint32
    """
    func = MZDAPILib["mzdSetMacLaneInterruptEnable"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint32]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, intrEnable)
    return ret


def mzdGetMacLaneInterruptEnable(pDev, mdioPort, host_or_line, laneOffset, intrEnable_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param intrEnable_p: A pointer of c_uint32
    """
    func = MZDAPILib["mzdGetMacLaneInterruptEnable"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_uint32)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, intrEnable_p)
    return ret


def mzdGetMacLaneInterruptStatus(pDev, mdioPort, host_or_line, laneOffset, intrStatus_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param intrStatus_p: A pointer of c_uint32
    """
    func = MZDAPILib["mzdGetMacLaneInterruptStatus"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_uint32)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, intrStatus_p)
    return ret


def mzdSetMacTodInterruptEnable(pDev, mdioPort, host_or_line, overrunIntrEnable, underrunIntrEnable):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param overrunIntrEnable: argument type c_uint32
    :param underrunIntrEnable: argument type c_uint32
    """
    func = MZDAPILib["mzdSetMacTodInterruptEnable"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint32, c_uint32]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, overrunIntrEnable, underrunIntrEnable)
    return ret


def mzdGetMacTodInterruptEnable(pDev, mdioPort, host_or_line, overrunIntrEnable_p, underrunIntrEnable_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param overrunIntrEnable_p: A pointer of c_uint32
    :param underrunIntrEnable_p: A pointer of c_uint32
    """
    func = MZDAPILib["mzdGetMacTodInterruptEnable"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, POINTER(c_uint32), POINTER(c_uint32)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, overrunIntrEnable_p, underrunIntrEnable_p)
    return ret


def mzdGetMacTodInterruptStatus(pDev, mdioPort, host_or_line, intrType, overrunIntrStatus_p, underrunIntrStatus_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param intrType: member from enumerate class MZD_MAC_TOD_INTR_TYPE
    :param overrunIntrStatus_p: A pointer of c_uint32
    :param underrunIntrStatus_p: A pointer of c_uint32
    """
    func = MZDAPILib["mzdGetMacTodInterruptStatus"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_int, POINTER(c_uint32), POINTER(c_uint32)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, intrType, overrunIntrStatus_p, underrunIntrStatus_p)
    return ret


def mzdSetMacGlobalInterruptEnable(pDev, mdioPort, host_or_line, intrEnable):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param intrEnable: argument type c_uint32
    """
    func = MZDAPILib["mzdSetMacGlobalInterruptEnable"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint32]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, intrEnable)
    return ret


def mzdGetMacGlobalInterruptEnable(pDev, mdioPort, host_or_line, intrEnable_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param intrEnable_p: A pointer of c_uint32
    """
    func = MZDAPILib["mzdGetMacGlobalInterruptEnable"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, POINTER(c_uint32)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, intrEnable_p)
    return ret


def mzdGetMacGlobalInterruptStatus(pDev, mdioPort, host_or_line, intrStatus_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param intrStatus_p: A pointer of c_uint32
    """
    func = MZDAPILib["mzdGetMacGlobalInterruptStatus"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, POINTER(c_uint32)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, intrStatus_p)
    return ret


def mzdMacSecHmuxConfigDump(pDev, mdioPort, dumpOptions):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param dumpOptions: argument type c_uint32
    """
    func = MZDAPILib["mzdMacSecHmuxConfigDump"]
    func.argtypes = [c_void_p, c_uint16, c_uint32]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, dumpOptions)
    return ret


def mzdPtpInit(pDev, mdioPort):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    """
    func = MZDAPILib["mzdPtpInit"]
    func.argtypes = [c_void_p, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort)
    return ret


def mzdPtpDisable(pDev, mdioPort, laneOffset, isEgress):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param isEgress: member from enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdPtpDisable"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_int]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, laneOffset, isEgress)
    return ret


def mzdPtpDisableAllPacketType(pDev, mdioPort, laneOffset, isEgress):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param isEgress: member from enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdPtpDisableAllPacketType"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_int]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, laneOffset, isEgress)
    return ret


def mzdPtpTCInit(pDev, mdioPort, laneOffset, isEgress):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param isEgress: member from enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdPtpTCInit"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_int]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, laneOffset, isEgress)
    return ret


def mzdPtpDistributedTCInit(pDev, mdioPort, laneOffset, isEgress):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param isEgress: member from enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdPtpDistributedTCInit"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_int]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, laneOffset, isEgress)
    return ret


def mzdPtpFromReservedInit(pDev, mdioPort, laneOffset, isEgress):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param isEgress: member from enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdPtpFromReservedInit"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_int]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, laneOffset, isEgress)
    return ret


def mzdPtpSetIgnoreMacSec(pDev, mdioPort, laneOffset, isEgress, isIgnore):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param isEgress: member from enumerate class MZD_BOOL
    :param isIgnore: member from enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdPtpSetIgnoreMacSec"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_int, c_int]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, laneOffset, isEgress, isIgnore)
    return ret


def mzdPtpGetEgressTSQ(pDev, mdioPort, laneOffset, queueId, egressTSQ_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param queueId: argument type c_uint16
    :param egressTSQ_p: A pointer of the structure class MZD_PTP_EGRESS_TSQ
    """
    func = MZDAPILib["mzdPtpGetEgressTSQ"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(MZD_PTP_EGRESS_TSQ)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, laneOffset, queueId, egressTSQ_p)
    return ret


def mzdPtpGetIngressTSQ(pDev, mdioPort, laneOffset, ingressTSQ_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param ingressTSQ_p: A pointer of the structure class MZD_PTP_INGRESS_TSQ
    """
    func = MZDAPILib["mzdPtpGetIngressTSQ"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, POINTER(MZD_PTP_INGRESS_TSQ)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, laneOffset, ingressTSQ_p)
    return ret


def mzdPtpSetMACOneStep(pDev, mdioPort, laneOffset, host_or_line, isHighSpeed, isEnable):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param isHighSpeed: member from enumerate class MZD_BOOL
    :param isEnable: member from enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdPtpSetMACOneStep"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_int, c_int]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, laneOffset, host_or_line, isHighSpeed, isEnable)
    return ret


def mzdPtpTODSelect(pDev, mdioPort, laneOffset, host_or_line, isHighSpeed, taiSel):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param isHighSpeed: member from enumerate class MZD_BOOL
    :param taiSel: member from enumerate class MZD_TAI_SELECT
    """
    func = MZDAPILib["mzdPtpTODSelect"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_int, c_int]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, laneOffset, host_or_line, isHighSpeed, taiSel)
    return ret


def mzdPtpVxlanEnable(pDev, mdioPort, laneOffset, isEgress, isEnable):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param isEgress: member from enumerate class MZD_BOOL
    :param isEnable: member from enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdPtpVxlanEnable"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_int, c_int]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, laneOffset, isEgress, isEnable)
    return ret


def mzdPtpEnableSelectPacketType(pDev, mdioPort, laneOffset, isEgress, packetType):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param isEgress: member from enumerate class MZD_BOOL
    :param packetType: member from enumerate class MZD_PACKET_TYPE
    """
    func = MZDAPILib["mzdPtpEnableSelectPacketType"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_int, c_int]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, laneOffset, isEgress, packetType)
    return ret


def mzdPtpUserDefinedTPID(pDev, mdioPort, isEgress, entryId, tpid):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param isEgress: member from enumerate class MZD_BOOL
    :param entryId: argument type c_uint16
    :param tpid: argument type c_uint16
    """
    func = MZDAPILib["mzdPtpUserDefinedTPID"]
    func.argtypes = [c_void_p, c_uint16, c_int, c_uint16, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, isEgress, entryId, tpid)
    return ret


def mzdPtpTSDFSEnable(pDev, mdioPort, laneOffset, host_or_line, opMode, isEnable):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param opMode: member from enumerate class MZD_OP_MODE
    :param isEnable: member from enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdPtpTSDFSEnable"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_int, c_int]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, laneOffset, host_or_line, opMode, isEnable)
    return ret


def mzdPtpTSDAMREnable(pDev, mdioPort, laneOffset, host_or_line, opMode, isEnable):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param opMode: member from enumerate class MZD_OP_MODE
    :param isEnable: member from enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdPtpTSDAMREnable"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_int, c_int]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, laneOffset, host_or_line, opMode, isEnable)
    return ret


def mzdPtpTSXEnable(pDev, mdioPort, laneOffset, host_or_line, isEgress, isHighSpeed, isEnable):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param isEgress: member from enumerate class MZD_BOOL
    :param isHighSpeed: member from enumerate class MZD_BOOL
    :param isEnable: member from enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdPtpTSXEnable"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_int, c_int, c_int]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, laneOffset, host_or_line, isEgress, isHighSpeed, isEnable)
    return ret


def mzdPtpSetShareBufferPTPIgnore(pDev, mdioPort, isIgnore):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param isIgnore: member from enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdPtpSetShareBufferPTPIgnore"]
    func.argtypes = [c_void_p, c_uint16, c_int]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, isIgnore)
    return ret


def mzdPtpSetBypassEip218(pDev, mdioPort, isBypass):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param isBypass: member from enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdPtpSetBypassEip218"]
    func.argtypes = [c_void_p, c_uint16, c_int]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, isBypass)
    return ret


def mzdTaiInit(pDev, mdioPort):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    """
    func = MZDAPILib["mzdTaiInit"]
    func.argtypes = [c_void_p, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort)
    return ret


def mzdTaiReadRegister(pDev, mdioPort, taiNum, regAddr, data_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param taiNum: member from enumerate class MZD_TAI_SELECT
    :param regAddr: argument type c_uint32
    :param data_p: A pointer of c_uint32
    """
    func = MZDAPILib["mzdTaiReadRegister"]
    func.argtypes = [c_void_p, c_uint16, c_int, c_uint32, POINTER(c_uint32)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, taiNum, regAddr, data_p)
    return ret


def mzdTaiWriteRegister(pDev, mdioPort, taiNum, regAddr, data):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param taiNum: member from enumerate class MZD_TAI_SELECT
    :param regAddr: argument type c_uint32
    :param data: argument type c_uint32
    """
    func = MZDAPILib["mzdTaiWriteRegister"]
    func.argtypes = [c_void_p, c_uint16, c_int, c_uint32, c_uint32]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, taiNum, regAddr, data)
    return ret


def mzdTaiReadRegisterField(pDev, mdioPort, taiNum, regAddr, fieldOffset, fieldLength, data_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param taiNum: member from enumerate class MZD_TAI_SELECT
    :param regAddr: argument type c_uint32
    :param fieldOffset: argument type c_uint16
    :param fieldLength: argument type c_uint16
    :param data_p: A pointer of c_uint32
    """
    func = MZDAPILib["mzdTaiReadRegisterField"]
    func.argtypes = [c_void_p, c_uint16, c_int, c_uint32, c_uint16, c_uint16, POINTER(c_uint32)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, taiNum, regAddr, fieldOffset, fieldLength, data_p)
    return ret


def mzdTaiWriteRegisterField(pDev, mdioPort, taiNum, regAddr, fieldOffset, fieldLength, data):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param taiNum: member from enumerate class MZD_TAI_SELECT
    :param regAddr: argument type c_uint32
    :param fieldOffset: argument type c_uint16
    :param fieldLength: argument type c_uint16
    :param data: argument type c_uint32
    """
    func = MZDAPILib["mzdTaiWriteRegisterField"]
    func.argtypes = [c_void_p, c_uint16, c_int, c_uint32, c_uint16, c_uint16, c_uint32]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, taiNum, regAddr, fieldOffset, fieldLength, data)
    return ret


def mzdTaiTodUpdate(pDev, mdioPort, taiNum, timeArray_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param taiNum: member from enumerate class MZD_TAI_SELECT
    :param timeArray_p: A pointer of the structure class MZD_TAI_TIME_ARRAY
    """
    func = MZDAPILib["mzdTaiTodUpdate"]
    func.argtypes = [c_void_p, c_uint16, c_int, POINTER(MZD_TAI_TIME_ARRAY)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, taiNum, timeArray_p)
    return ret


def mzdTaiTodFreqUpdate(pDev, mdioPort, taiNum, fracNano):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param taiNum: member from enumerate class MZD_TAI_SELECT
    :param fracNano: argument type c_int32
    """
    func = MZDAPILib["mzdTaiTodFreqUpdate"]
    func.argtypes = [c_void_p, c_uint16, c_int, c_int32]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, taiNum, fracNano)
    return ret


def mzdTaiTodCapture(pDev, mdioPort, taiNum):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param taiNum: member from enumerate class MZD_TAI_SELECT
    """
    func = MZDAPILib["mzdTaiTodCapture"]
    func.argtypes = [c_void_p, c_uint16, c_int]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, taiNum)
    return ret


def mzdTaiTodIncrement(pDev, mdioPort, taiNum, todOffset_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param taiNum: member from enumerate class MZD_TAI_SELECT
    :param todOffset_p: A pointer of the structure class MZD_TAI_TIME_ARRAY
    """
    func = MZDAPILib["mzdTaiTodIncrement"]
    func.argtypes = [c_void_p, c_uint16, c_int, POINTER(MZD_TAI_TIME_ARRAY)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, taiNum, todOffset_p)
    return ret


def mzdTaiTodDecrement(pDev, mdioPort, taiNum, todOffset_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param taiNum: member from enumerate class MZD_TAI_SELECT
    :param todOffset_p: A pointer of the structure class MZD_TAI_TIME_ARRAY
    """
    func = MZDAPILib["mzdTaiTodDecrement"]
    func.argtypes = [c_void_p, c_uint16, c_int, POINTER(MZD_TAI_TIME_ARRAY)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, taiNum, todOffset_p)
    return ret


def mzdTaiTodGracefulInc(pDev, mdioPort, taiNum, graceStep, todOffset_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param taiNum: member from enumerate class MZD_TAI_SELECT
    :param graceStep: argument type c_uint8
    :param todOffset_p: A pointer of the structure class MZD_TAI_TIME_ARRAY
    """
    func = MZDAPILib["mzdTaiTodGracefulInc"]
    func.argtypes = [c_void_p, c_uint16, c_int, c_uint8, POINTER(MZD_TAI_TIME_ARRAY)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, taiNum, graceStep, todOffset_p)
    return ret


def mzdTaiTodGracefulDec(pDev, mdioPort, taiNum, graceStep, todOffset_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param taiNum: member from enumerate class MZD_TAI_SELECT
    :param graceStep: argument type c_uint8
    :param todOffset_p: A pointer of the structure class MZD_TAI_TIME_ARRAY
    """
    func = MZDAPILib["mzdTaiTodGracefulDec"]
    func.argtypes = [c_void_p, c_uint16, c_int, c_uint8, POINTER(MZD_TAI_TIME_ARRAY)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, taiNum, graceStep, todOffset_p)
    return ret


def mzdTaiTodTimeCounterFunctionSet(pDev, mdioPort, taiNum, todOp):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param taiNum: member from enumerate class MZD_TAI_SELECT
    :param todOp: member from enumerate class MZD_TOD_OP
    """
    func = MZDAPILib["mzdTaiTodTimeCounterFunctionSet"]
    func.argtypes = [c_void_p, c_uint16, c_int, c_int]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, taiNum, todOp)
    return ret


def mzdTaiTodTimeLoadValueSet(pDev, mdioPort, taiNum, todValue_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param taiNum: member from enumerate class MZD_TAI_SELECT
    :param todValue_p: A pointer of the structure class MZD_TAI_TIME_ARRAY
    """
    func = MZDAPILib["mzdTaiTodTimeLoadValueSet"]
    func.argtypes = [c_void_p, c_uint16, c_int, POINTER(MZD_TAI_TIME_ARRAY)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, taiNum, todValue_p)
    return ret


def mzdTaiTodTimeCaptureValue0Get(pDev, mdioPort, taiNum, todValue_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param taiNum: member from enumerate class MZD_TAI_SELECT
    :param todValue_p: A pointer of the structure class MZD_TAI_TIME_ARRAY
    """
    func = MZDAPILib["mzdTaiTodTimeCaptureValue0Get"]
    func.argtypes = [c_void_p, c_uint16, c_int, POINTER(MZD_TAI_TIME_ARRAY)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, taiNum, todValue_p)
    return ret


def mzdTaiTodTimeCaptureValue1Get(pDev, mdioPort, taiNum, todValue_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param taiNum: member from enumerate class MZD_TAI_SELECT
    :param todValue_p: A pointer of the structure class MZD_TAI_TIME_ARRAY
    """
    func = MZDAPILib["mzdTaiTodTimeCaptureValue1Get"]
    func.argtypes = [c_void_p, c_uint16, c_int, POINTER(MZD_TAI_TIME_ARRAY)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, taiNum, todValue_p)
    return ret


def mzdTaiTodTimeCaptureStatusGet(pDev, mdioPort, taiNum, valid_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param taiNum: member from enumerate class MZD_TAI_SELECT
    :param valid_p: A pointer of c_uint32
    """
    func = MZDAPILib["mzdTaiTodTimeCaptureStatusGet"]
    func.argtypes = [c_void_p, c_uint16, c_int, POINTER(c_uint32)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, taiNum, valid_p)
    return ret


def mzdTaiTodStepSet(pDev, mdioPort, taiNum, stepNano, stepFracNano):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param taiNum: member from enumerate class MZD_TAI_SELECT
    :param stepNano: argument type c_uint16
    :param stepFracNano: argument type c_int32
    """
    func = MZDAPILib["mzdTaiTodStepSet"]
    func.argtypes = [c_void_p, c_uint16, c_int, c_uint16, c_int32]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, taiNum, stepNano, stepFracNano)
    return ret


def mzdTaiTodStepGet(pDev, mdioPort, taiNum, stepNano_p, stepFracNano_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param taiNum: member from enumerate class MZD_TAI_SELECT
    :param stepNano_p: A pointer of c_uint16
    :param stepFracNano_p: A pointer of c_int32
    """
    func = MZDAPILib["mzdTaiTodStepGet"]
    func.argtypes = [c_void_p, c_uint16, c_int, POINTER(c_uint16), POINTER(c_int32)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, taiNum, stepNano_p, stepFracNano_p)
    return ret


def mzdTaiPpsGenerationSet(pDev, mdioPort, taiNum, pulseData_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param taiNum: member from enumerate class MZD_TAI_SELECT
    :param pulseData_p: A pointer of the structure class MZD_TAI_PPS_PULSE
    """
    func = MZDAPILib["mzdTaiPpsGenerationSet"]
    func.argtypes = [c_void_p, c_uint16, c_int, POINTER(MZD_TAI_PPS_PULSE)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, taiNum, pulseData_p)
    return ret


def mzdTaiPpsReceptionSet(pDev, mdioPort, taiNum, pulseData_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param taiNum: member from enumerate class MZD_TAI_SELECT
    :param pulseData_p: A pointer of the structure class MZD_TAI_PPS_PULSE
    """
    func = MZDAPILib["mzdTaiPpsReceptionSet"]
    func.argtypes = [c_void_p, c_uint16, c_int, POINTER(MZD_TAI_PPS_PULSE)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, taiNum, pulseData_p)
    return ret


def mzdTaiPpsAdvReceptionSet(pDev, mdioPort, taiNum, pulseData_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param taiNum: member from enumerate class MZD_TAI_SELECT
    :param pulseData_p: A pointer of the structure class MZD_TAI_PPS_PULSE
    """
    func = MZDAPILib["mzdTaiPpsAdvReceptionSet"]
    func.argtypes = [c_void_p, c_uint16, c_int, POINTER(MZD_TAI_PPS_PULSE)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, taiNum, pulseData_p)
    return ret


def mzdTaiTriggerGenerationPulseSet(pDev, mdioPort, taiNum, triggerTod_p, triggerTodMask_p, pulseWidth):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param taiNum: member from enumerate class MZD_TAI_SELECT
    :param triggerTod_p: A pointer of the structure class MZD_TAI_TIME_ARRAY
    :param triggerTodMask_p: A pointer of the structure class MZD_TAI_TIME_ARRAY
    :param pulseWidth: argument type c_uint32
    """
    func = MZDAPILib["mzdTaiTriggerGenerationPulseSet"]
    func.argtypes = [c_void_p, c_uint16, c_int, POINTER(MZD_TAI_TIME_ARRAY), POINTER(MZD_TAI_TIME_ARRAY), c_uint32]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, taiNum, triggerTod_p, triggerTodMask_p, pulseWidth)
    return ret


def mzdTaiPulseInMuxingEnableSet(pDev, mdioPort, taiNum, en):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param taiNum: member from enumerate class MZD_TAI_SELECT
    :param en: member from enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdTaiPulseInMuxingEnableSet"]
    func.argtypes = [c_void_p, c_uint16, c_int, c_int]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, taiNum, en)
    return ret


def mzdTaiInterruptCauseGet(pDev, mdioPort, taiNum, intCause_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param taiNum: member from enumerate class MZD_TAI_SELECT
    :param intCause_p: A pointer of c_uint32
    """
    func = MZDAPILib["mzdTaiInterruptCauseGet"]
    func.argtypes = [c_void_p, c_uint16, c_int, POINTER(c_uint32)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, taiNum, intCause_p)
    return ret


def mzdTaiInterruptMaskSet(pDev, mdioPort, taiNum, intMask):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param taiNum: member from enumerate class MZD_TAI_SELECT
    :param intMask: argument type c_uint32
    """
    func = MZDAPILib["mzdTaiInterruptMaskSet"]
    func.argtypes = [c_void_p, c_uint16, c_int, c_uint32]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, taiNum, intMask)
    return ret


def mzdTaiTodFractionalNanosecondDriftGet(pDev, mdioPort, taiNum, driftValue_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param taiNum: member from enumerate class MZD_TAI_SELECT
    :param driftValue_p: A pointer of c_uint32
    """
    func = MZDAPILib["mzdTaiTodFractionalNanosecondDriftGet"]
    func.argtypes = [c_void_p, c_uint16, c_int, POINTER(c_uint32)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, taiNum, driftValue_p)
    return ret


def mzdTaiClockGenClockRatioSet(pDev, mdioPort, taiNum, ratio):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param taiNum: member from enumerate class MZD_TAI_SELECT
    :param ratio: argument type c_uint16
    """
    func = MZDAPILib["mzdTaiClockGenClockRatioSet"]
    func.argtypes = [c_void_p, c_uint16, c_int, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, taiNum, ratio)
    return ret


def mzdTaiTodUpdateEnableFirmware(pDev, mdioPort, taiNum, enableTodUpdate):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param taiNum: member from enumerate class MZD_TAI_SELECT
    :param enableTodUpdate: member from enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdTaiTodUpdateEnableFirmware"]
    func.argtypes = [c_void_p, c_uint16, c_int, c_int]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, taiNum, enableTodUpdate)
    return ret


def mzdTaiTodUpdateEnableFirmwareGet(pDev, enableTodUpdate_p):
    """
    :param pDev: argument type c_void_p
    :param enableTodUpdate_p: A pointer of the enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdTaiTodUpdateEnableFirmwareGet"]
    func.argtypes = [c_void_p, POINTER(c_int)]
    func.restype = c_uint32
    ret = func(pDev, enableTodUpdate_p)
    return ret


def mzdTaiClockConfig(pDev, mdioPort, refClock, taiClock):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param refClock: member from enumerate class MZD_TAI_REF_CLK
    :param taiClock: member from enumerate class MZD_TAI_CLK
    """
    func = MZDAPILib["mzdTaiClockConfig"]
    func.argtypes = [c_void_p, c_uint16, c_int, c_int]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, refClock, taiClock)
    return ret


def mzdMacSecSupportedMacSecDeviceCount(pDev, supportedMacSecDeviceCount_p):
    """
    :param pDev: argument type c_void_p
    :param supportedMacSecDeviceCount_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdMacSecSupportedMacSecDeviceCount"]
    func.argtypes = [c_void_p, POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, supportedMacSecDeviceCount_p)
    return ret


def mzdMacSecAssignDeviceID(pDev):
    """
    :param pDev: argument type c_void_p
    """
    func = MZDAPILib["mzdMacSecAssignDeviceID"]
    func.argtypes = [c_void_p]
    func.restype = c_uint32
    ret = func(pDev)
    return ret


def mzdMacSecGetAssignedDeviceID(pDev, mdioPort, macsecIngressDevId_p, macsecEgressDevId_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param macsecIngressDevId_p: A pointer of c_uint8
    :param macsecEgressDevId_p: A pointer of c_uint8
    """
    func = MZDAPILib["mzdMacSecGetAssignedDeviceID"]
    func.argtypes = [c_void_p, c_uint16, POINTER(c_uint8), POINTER(c_uint8)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, macsecIngressDevId_p, macsecEgressDevId_p)
    return ret


def mzdMacSecUnAssignDeviceID(pDev):
    """
    :param pDev: argument type c_void_p
    """
    func = MZDAPILib["mzdMacSecUnAssignDeviceID"]
    func.argtypes = [c_void_p]
    func.restype = c_uint32
    ret = func(pDev)
    return ret


def mzdMacSecDeviceInit(pDev, mdioPort, laneOffset):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param laneOffset: argument type c_uint16
    """
    func = MZDAPILib["mzdMacSecDeviceInit"]
    func.argtypes = [c_void_p, c_uint16, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, laneOffset)
    return ret


def mzdMacSecDropAction(pDev, mdioPort, fIngress, dropAction):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param fIngress: member from enumerate class MZD_BOOL
    :param dropAction: member from enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdMacSecDropAction"]
    func.argtypes = [c_void_p, c_uint16, c_int, c_int]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, fIngress, dropAction)
    return ret


def mzdMACsecInterruptEnable(pDev, mdioPort, laneOffset, deviceMACSecId, cfyE_or_secY, interruptMask, bGlobalInterrupt):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param deviceMACSecId: argument type c_uint16
    :param cfyE_or_secY: member from enumerate class MZD_MACSEC_BLOCK
    :param interruptMask: argument type c_uint32
    :param bGlobalInterrupt: member from enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdMACsecInterruptEnable"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_int, c_uint32, c_int]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, laneOffset, deviceMACSecId, cfyE_or_secY, interruptMask, bGlobalInterrupt)
    return ret


def mzdMACsecInterruptClear(pDev, mdioPort, laneOffset, deviceMACSecId, cfyE_or_secY, interruptMask, bGlobalInterrupt):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param deviceMACSecId: argument type c_uint16
    :param cfyE_or_secY: member from enumerate class MZD_MACSEC_BLOCK
    :param interruptMask: argument type c_uint32
    :param bGlobalInterrupt: member from enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdMACsecInterruptClear"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_int, c_uint32, c_int]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, laneOffset, deviceMACSecId, cfyE_or_secY, interruptMask, bGlobalInterrupt)
    return ret


def mzdMACsecInterruptDisable(pDev, mdioPort, laneOffset, deviceMACSecId, cfyE_or_secY, interruptMask, bGlobalInterrupt):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param deviceMACSecId: argument type c_uint16
    :param cfyE_or_secY: member from enumerate class MZD_MACSEC_BLOCK
    :param interruptMask: argument type c_uint32
    :param bGlobalInterrupt: member from enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdMACsecInterruptDisable"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_int, c_uint32, c_int]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, laneOffset, deviceMACSecId, cfyE_or_secY, interruptMask, bGlobalInterrupt)
    return ret


def mzdMACsecGetInterruptStatus(pDev, mdioPort, laneOffset, deviceMACSecId, cfyE_or_secY, interruptSourceStatus_p, bGlobalInterrupt):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param deviceMACSecId: argument type c_uint16
    :param cfyE_or_secY: member from enumerate class MZD_MACSEC_BLOCK
    :param interruptSourceStatus_p: A pointer of c_uint32
    :param bGlobalInterrupt: member from enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdMACsecGetInterruptStatus"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_int, POINTER(c_uint32), c_int]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, laneOffset, deviceMACSecId, cfyE_or_secY, interruptSourceStatus_p, bGlobalInterrupt)
    return ret


def mzdMACsecGetEnabledInterruptStatus(pDev, mdioPort, laneOffset, deviceMACSecId, cfyE_or_secY, interruptSourceStatus_p, bGlobalInterrupt):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param deviceMACSecId: argument type c_uint16
    :param cfyE_or_secY: member from enumerate class MZD_MACSEC_BLOCK
    :param interruptSourceStatus_p: A pointer of c_uint32
    :param bGlobalInterrupt: member from enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdMACsecGetEnabledInterruptStatus"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_int, POINTER(c_uint32), c_int]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, laneOffset, deviceMACSecId, cfyE_or_secY, interruptSourceStatus_p, bGlobalInterrupt)
    return ret


def mzdMACsecMappedAICDevices(pDev, mdioPort, laneOffset, deviceMACSecId, cfyE_or_secY, globalICDev_p, channelICDev_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param deviceMACSecId: argument type c_uint16
    :param cfyE_or_secY: member from enumerate class MZD_MACSEC_BLOCK
    :param globalICDev: argument type c_void_p
    :param channelICDev: argument type c_void_p
    """
    func = MZDAPILib["mzdMACsecMappedAICDevices"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_int, c_void_p, c_void_p]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, laneOffset, deviceMACSecId, cfyE_or_secY, globalICDev_p, channelICDev_p)
    return ret


def mzdGetAPIVersion(major_p, minor_p, buildID_p):
    """
    :param major_p: A pointer of c_uint8
    :param minor_p: A pointer of c_uint8
    :param buildID_p: A pointer of c_uint8
    """
    func = MZDAPILib["mzdGetAPIVersion"]
    func.argtypes = [POINTER(c_uint8), POINTER(c_uint8), POINTER(c_uint8)]
    func.restype = c_int
    ret = func(major_p, minor_p, buildID_p)
    return ret


def mzdSetModeSelection(pDev, mdioPort, laneOffset, hostMode, lineMode, modeOptionSel, modeOption, result_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param hostMode: member from enumerate class MZD_OP_MODE
    :param lineMode: member from enumerate class MZD_OP_MODE
    :param modeOptionSel: argument type c_uint32
    :param modeOption: implementation of the structure class MZD_MODE_OPTION_STRUCT
    :param result_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdSetModeSelection"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_int, c_int, c_uint32, MZD_MODE_OPTION_STRUCT, POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, laneOffset, hostMode, lineMode, modeOptionSel, modeOption, result_p)
    return ret


def mzdSetInterfaceUserMode(pDev, mdioPort, host_or_line, laneOffset, opMode, modeOptionSel, modeOption, result_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param opMode: member from enumerate class MZD_OP_MODE
    :param modeOptionSel: argument type c_uint32
    :param modeOption: implementation of the structure class MZD_MODE_OPTION_STRUCT
    :param result_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdSetInterfaceUserMode"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_int, c_uint32, MZD_MODE_OPTION_STRUCT, POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, opMode, modeOptionSel, modeOption, result_p)
    return ret


def mzdGetOpMode(pDev, mdioPort, host_or_line, laneOffset, opMode_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param opMode_p: A pointer of the enumerate class MZD_OP_MODE
    """
    func = MZDAPILib["mzdGetOpMode"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_int)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, opMode_p)
    return ret


def mzdAutoNegControl(pDev, mdioPort, host_or_line, laneOffset, enableAutoNeg, swReset):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param enableAutoNeg: argument type c_uint16
    :param swReset: member from enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdAutoNegControl"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint16, c_int]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, enableAutoNeg, swReset)
    return ret


def mzdAutoNegCheckComplete(pDev, mdioPort, host_or_line, laneOffset, autoNegComplete_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param autoNegComplete_p: A pointer of the enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdAutoNegCheckComplete"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_int)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, autoNegComplete_p)
    return ret


def mzdGetAutoNegResolution(pDev, mdioPort, host_or_line, laneOffset, speed_bits_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param speed_bits_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdGetAutoNegResolution"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, speed_bits_p)
    return ret


def mzdCL37AutoNegControl(pDev, mdioPort, host_or_line, laneOffset, enableAutoNeg):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param enableAutoNeg: argument type c_uint16
    """
    func = MZDAPILib["mzdCL37AutoNegControl"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, enableAutoNeg)
    return ret


def mzdCL37AutoNegCheckComplete(pDev, mdioPort, host_or_line, laneOffset, autoNegComplete_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param autoNegComplete_p: A pointer of the enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdCL37AutoNegCheckComplete"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_int)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, autoNegComplete_p)
    return ret


def mzdSetPauseAdvertisement(pDev, mdioPort, host_or_line, laneOffset, pauseType, swReset):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param pauseType: argument type c_uint16
    :param swReset: member from enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdSetPauseAdvertisement"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint16, c_int]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, pauseType, swReset)
    return ret


def mzdGetPauseAdvertisement(pDev, mdioPort, host_or_line, laneOffset, pauseType_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param pauseType_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdGetPauseAdvertisement"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, pauseType_p)
    return ret


def mzdGetLPAdvertisedPause(pDev, mdioPort, host_or_line, laneOffset, pauseType_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param pauseType_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdGetLPAdvertisedPause"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, pauseType_p)
    return ret


def mzdGetTxRxPauseResolution(pDev, mdioPort, host_or_line, laneOffset, pauseResolved_p, tx_pause_enabled_p, rx_pause_enabled_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param pauseResolved_p: A pointer of the enumerate class MZD_BOOL
    :param tx_pause_enabled_p: A pointer of the enumerate class MZD_BOOL
    :param rx_pause_enabled_p: A pointer of the enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdGetTxRxPauseResolution"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_int), POINTER(c_int), POINTER(c_int)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, pauseResolved_p, tx_pause_enabled_p, rx_pause_enabled_p)
    return ret


def mzdCheckPCSLinkStatus(pDev, mdioPort, laneOffset, currentStatus_p, latchedStatus_p, statusDetail_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param currentStatus_p: A pointer of c_uint16
    :param latchedStatus_p: A pointer of c_uint16
    :param statusDetail_p: A pointer of the structure class MZD_PCS_LINK_STATUS
    """
    func = MZDAPILib["mzdCheckPCSLinkStatus"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, POINTER(c_uint16), POINTER(c_uint16), POINTER(MZD_PCS_LINK_STATUS)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, laneOffset, currentStatus_p, latchedStatus_p, statusDetail_p)
    return ret


def mzdGetDetailedLinkStatus(pDev, mdioPort, laneOffset, host_or_line, currStat_p, latchStat_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param currStat_p: A pointer of c_uint16
    :param latchStat_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdGetDetailedLinkStatus"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_uint16), POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, laneOffset, host_or_line, currStat_p, latchStat_p)
    return ret


def mzdGetPcsFaultStatus(pDev, mdioPort, host_or_line, laneOffset, currentTxFaultStatus_p, currentRxFaultStatus_p, latchedTxFaultStatus_p, latchedRxFaultStatus_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param currentTxFaultStatus_p: A pointer of c_uint16
    :param currentRxFaultStatus_p: A pointer of c_uint16
    :param latchedTxFaultStatus_p: A pointer of c_uint16
    :param latchedRxFaultStatus_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdGetPcsFaultStatus"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_uint16), POINTER(c_uint16), POINTER(c_uint16), POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, currentTxFaultStatus_p, currentRxFaultStatus_p, latchedTxFaultStatus_p, latchedRxFaultStatus_p)
    return ret


def mzdLaneSoftReset(pDev, mdioPort, host_or_line, laneOffset, timeoutMs):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param timeoutMs: argument type c_uint16
    """
    func = MZDAPILib["mzdLaneSoftReset"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, timeoutMs)
    return ret


def mzdSetDPFaultConfig(pDev, mdioPort, host_or_line, laneOffset, datapathMode, txType, rxType):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param datapathMode: argument type c_uint16
    :param txType: argument type c_uint16
    :param rxType: argument type c_uint16
    """
    func = MZDAPILib["mzdSetDPFaultConfig"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint16, c_uint16, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, datapathMode, txType, rxType)
    return ret


def mzdGetDPFaultConfig(pDev, mdioPort, host_or_line, laneOffset, datapathMode_p, txType_p, rxType_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param datapathMode_p: A pointer of c_uint16
    :param txType_p: A pointer of c_uint16
    :param rxType_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdGetDPFaultConfig"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_uint16), POINTER(c_uint16), POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, datapathMode_p, txType_p, rxType_p)
    return ret


def mzdSetSerdesMux(pDev, host_or_line, serdesMux_p):
    """
    :param pDev: argument type c_void_p
    :param host_or_line: argument type c_uint16
    :param serdesMux_p: A pointer of c_uint8
    """
    func = MZDAPILib["mzdSetSerdesMux"]
    func.argtypes = [c_void_p, c_uint16, POINTER(c_uint8)]
    func.restype = c_uint32
    ret = func(pDev, host_or_line, serdesMux_p)
    return ret


def mzdGetSerdesMux(pDev, host_or_line, serdesMux_p):
    """
    :param pDev: argument type c_void_p
    :param host_or_line: argument type c_uint16
    :param serdesMux_p: A pointer of c_uint8
    """
    func = MZDAPILib["mzdGetSerdesMux"]
    func.argtypes = [c_void_p, c_uint16, POINTER(c_uint8)]
    func.restype = c_uint32
    ret = func(pDev, host_or_line, serdesMux_p)
    return ret


def mzdGetLaneRxTrainingState(pDev, mdioPort, host_or_line, laneOffset, rxTraining_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param rxTraining_p: A pointer of the enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdGetLaneRxTrainingState"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_int)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, rxTraining_p)
    return ret


def mzdGetChipRevision(pDev, mdioPort, deviceId_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param deviceId_p: A pointer of the enumerate class MZD_DEVICE_ID
    """
    func = MZDAPILib["mzdGetChipRevision"]
    func.argtypes = [c_void_p, c_uint16, POINTER(c_int)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, deviceId_p)
    return ret


def mzdDevicePortCount(pDev, mdioPort, portCount_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param portCount_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdDevicePortCount"]
    func.argtypes = [c_void_p, c_uint16, POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, portCount_p)
    return ret


def mzdGetChipFWRevision(pDev, major_p, minor_p, patch_p, build_p):
    """
    :param pDev: argument type c_void_p
    :param major_p: A pointer of c_uint16
    :param minor_p: A pointer of c_uint16
    :param patch_p: A pointer of c_uint16
    :param build_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdGetChipFWRevision"]
    func.argtypes = [c_void_p, POINTER(c_uint16), POINTER(c_uint16), POINTER(c_uint16), POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, major_p, minor_p, patch_p, build_p)
    return ret


def mzdGetSerdesFWRevision(pDev, major_p, minor_p, patch_p, build_p):
    """
    :param pDev: argument type c_void_p
    :param major_p: A pointer of c_uint8
    :param minor_p: A pointer of c_uint8
    :param patch_p: A pointer of c_uint8
    :param build_p: A pointer of c_uint8
    """
    func = MZDAPILib["mzdGetSerdesFWRevision"]
    func.argtypes = [c_void_p, POINTER(c_uint8), POINTER(c_uint8), POINTER(c_uint8), POINTER(c_uint8)]
    func.restype = c_uint32
    ret = func(pDev, major_p, minor_p, patch_p, build_p)
    return ret


def mzdGetSerdesFWRevisionAll(pDev, majorMZD_NUM_INTERFACEMZD_MAX_PORTS_p, minorMZD_NUM_INTERFACEMZD_MAX_PORTS_p, patchMZD_NUM_INTERFACEMZD_MAX_PORTS_p, buildMZD_NUM_INTERFACEMZD_MAX_PORTS_p):
    """
    :param pDev: argument type c_void_p
    :param majorMZD_NUM_INTERFACEMZD_MAX_PORTS_p: A pointer of c_uint8
    :param minorMZD_NUM_INTERFACEMZD_MAX_PORTS_p: A pointer of c_uint8
    :param patchMZD_NUM_INTERFACEMZD_MAX_PORTS_p: A pointer of c_uint8
    :param buildMZD_NUM_INTERFACEMZD_MAX_PORTS_p: A pointer of c_uint8
    """
    func = MZDAPILib["mzdGetSerdesFWRevisionAll"]
    func.argtypes = [c_void_p, POINTER(c_uint8), POINTER(c_uint8), POINTER(c_uint8), POINTER(c_uint8)]
    func.restype = c_uint32
    ret = func(pDev, majorMZD_NUM_INTERFACEMZD_MAX_PORTS_p, minorMZD_NUM_INTERFACEMZD_MAX_PORTS_p, patchMZD_NUM_INTERFACEMZD_MAX_PORTS_p, buildMZD_NUM_INTERFACEMZD_MAX_PORTS_p)
    return ret


def mzdGetFirmwareLoadStatus(pDev, loadStatus_p):
    """
    :param pDev: argument type c_void_p
    :param loadStatus_p: A pointer of the enumerate class MZD_FIRMWARE_STATUS
    """
    func = MZDAPILib["mzdGetFirmwareLoadStatus"]
    func.argtypes = [c_void_p, POINTER(c_int)]
    func.restype = c_uint32
    ret = func(pDev, loadStatus_p)
    return ret


def mzdGetSerdesSignalDetectAndDspLock(pDev, mdioPort, host_or_line, laneOffset, signalDetect_p, dspLock_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param signalDetect_p: A pointer of c_uint16
    :param dspLock_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdGetSerdesSignalDetectAndDspLock"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_uint16), POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, signalDetect_p, dspLock_p)
    return ret


def mzdSetPCSLineLoopback(pDev, mdioPort, laneOffset, loopback_type, enable):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param loopback_type: member from enumerate class MZD_PCS_MODE_LOOPBACK
    :param enable: argument type c_uint16
    """
    func = MZDAPILib["mzdSetPCSLineLoopback"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_int, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, laneOffset, loopback_type, enable)
    return ret


def mzdSetPCSHostLoopback(pDev, mdioPort, laneOffset, loopback_type, loopbackState):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param loopback_type: member from enumerate class MZD_PCS_MODE_LOOPBACK
    :param loopbackState: argument type c_uint16
    """
    func = MZDAPILib["mzdSetPCSHostLoopback"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_int, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, laneOffset, loopback_type, loopbackState)
    return ret


def mzdHmuxSetPCSLineDeepLoopback(pDev, hostPort, hostLaneOffset, loopback_type, loopbackState):
    """
    :param pDev: argument type c_void_p
    :param hostPort: argument type c_uint16
    :param hostLaneOffset: argument type c_uint16
    :param loopback_type: member from enumerate class MZD_PCS_MODE_LOOPBACK
    :param loopbackState: argument type c_uint16
    """
    func = MZDAPILib["mzdHmuxSetPCSLineDeepLoopback"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_int, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, hostPort, hostLaneOffset, loopback_type, loopbackState)
    return ret


def mzdHmuxSetPCSHostDeepLoopback(pDev, linePort, lineLaneOffset, loopback_type, loopbackState):
    """
    :param pDev: argument type c_void_p
    :param linePort: argument type c_uint16
    :param lineLaneOffset: argument type c_uint16
    :param loopback_type: member from enumerate class MZD_PCS_MODE_LOOPBACK
    :param loopbackState: argument type c_uint16
    """
    func = MZDAPILib["mzdHmuxSetPCSHostDeepLoopback"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_int, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, linePort, lineLaneOffset, loopback_type, loopbackState)
    return ret


def mzdSetSerdesLaneLoopback(pDev, mdioPort, host_or_line, laneOffset, loopbackState, swReset):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param loopbackState: argument type c_uint16
    :param swReset: member from enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdSetSerdesLaneLoopback"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint16, c_int]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, loopbackState, swReset)
    return ret


def mzdGetSerdesLaneLoopback(pDev, mdioPort, host_or_line, laneOffset, loopbackState_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param loopbackState_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdGetSerdesLaneLoopback"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, loopbackState_p)
    return ret


def mzdConfigurePktGeneratorChecker(pDev, mdioPort, host_or_line, laneOffset, readToClear, dontuseSFDinChecker, pktPatternControl, generateCRCoff, initialPayload, frameLengthControl, numPktsToSend, randomIPG, ipgDuration):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param readToClear: member from enumerate class MZD_BOOL
    :param dontuseSFDinChecker: member from enumerate class MZD_BOOL
    :param pktPatternControl: argument type c_uint16
    :param generateCRCoff: member from enumerate class MZD_BOOL
    :param initialPayload: argument type c_uint32
    :param frameLengthControl: argument type c_uint16
    :param numPktsToSend: argument type c_uint16
    :param randomIPG: member from enumerate class MZD_BOOL
    :param ipgDuration: argument type c_uint16
    """
    func = MZDAPILib["mzdConfigurePktGeneratorChecker"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_int, c_int, c_uint16, c_int, c_uint32, c_uint16, c_uint16, c_int, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, readToClear, dontuseSFDinChecker, pktPatternControl, generateCRCoff, initialPayload, frameLengthControl, numPktsToSend, randomIPG, ipgDuration)
    return ret


def mzdEnablePktGeneratorChecker(pDev, mdioPort, host_or_line, laneOffset, enableGenerator, enableChecker):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param enableGenerator: member from enumerate class MZD_BOOL
    :param enableChecker: member from enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdEnablePktGeneratorChecker"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_int, c_int]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, enableGenerator, enableChecker)
    return ret


def mzdStartStopPktGenTraffic(pDev, mdioPort, host_or_line, laneOffset, numPktsToSend):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param numPktsToSend: member from enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdStartStopPktGenTraffic"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_int]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, numPktsToSend)
    return ret


def mzdPktGeneratorCounterReset(pDev, mdioPort, host_or_line, laneOffset):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    """
    func = MZDAPILib["mzdPktGeneratorCounterReset"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset)
    return ret


def mzdPktGeneratorGetCounter(pDev, mdioPort, host_or_line, laneOffset, pktCntType, packetCount_p, byteCount_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param pktCntType: member from enumerate class MZD_PKT_COUNT_TYPE
    :param packetCount_p: A pointer of c_uint64
    :param byteCount_p: A pointer of c_uint64
    """
    func = MZDAPILib["mzdPktGeneratorGetCounter"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_int, POINTER(c_uint64), POINTER(c_uint64)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, pktCntType, packetCount_p, byteCount_p)
    return ret


def mzdSetPRBSPattern(pDev, mdioPort, host_or_line, laneOffset, pattSel, pattSubSel):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param pattSel: member from enumerate class MZD_PRBS_SELECTOR_TYPE
    :param pattSubSel: member from enumerate class MZD_PATTERN_AB_SELECTOR_TYPE
    """
    func = MZDAPILib["mzdSetPRBSPattern"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_int, c_int]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, pattSel, pattSubSel)
    return ret


def mzdPRBSPatternOption(pDev, mdioPort, host_or_line, laneOffset, patternOption):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param patternOption: argument type c_uint16
    """
    func = MZDAPILib["mzdPRBSPatternOption"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, patternOption)
    return ret


def mzdSetPRBSEnableTxRx(pDev, mdioPort, host_or_line, laneOffset, txEnable, rxEnable, pattSel):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param txEnable: argument type c_uint16
    :param rxEnable: argument type c_uint16
    :param pattSel: member from enumerate class MZD_PRBS_SELECTOR_TYPE
    """
    func = MZDAPILib["mzdSetPRBSEnableTxRx"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint16, c_uint16, c_int]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, txEnable, rxEnable, pattSel)
    return ret


def mzdPRBSCounterReset(pDev, mdioPort, host_or_line, laneOffset):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    """
    func = MZDAPILib["mzdPRBSCounterReset"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset)
    return ret


def mzdSetPRBSWaitForLock(pDev, mdioPort, host_or_line, laneOffset, disableWaitforLock):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param disableWaitforLock: argument type c_uint16
    """
    func = MZDAPILib["mzdSetPRBSWaitForLock"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, disableWaitforLock)
    return ret


def mzdGetPRBSWaitForLock(pDev, mdioPort, host_or_line, laneOffset, disableWaitforLock_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param disableWaitforLock_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdGetPRBSWaitForLock"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, disableWaitforLock_p)
    return ret


def mzdSetPRBSClearOnRead(pDev, mdioPort, host_or_line, laneOffset, enableReadClear):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param enableReadClear: argument type c_uint16
    """
    func = MZDAPILib["mzdSetPRBSClearOnRead"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, enableReadClear)
    return ret


def mzdGetPRBSClearOnRead(pDev, mdioPort, host_or_line, laneOffset, enableReadClear_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param enableReadClear_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdGetPRBSClearOnRead"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, enableReadClear_p)
    return ret


def mzdGetPRBSLocked(pDev, mdioPort, host_or_line, laneOffset, prbsLocked_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param prbsLocked_p: A pointer of the enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdGetPRBSLocked"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_int)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, prbsLocked_p)
    return ret


def mzdGetPRBSCounts(pDev, mdioPort, host_or_line, laneOffset, pattSel, txBitCount_p, rxBitCount_p, rxBitErrorCount_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param pattSel: member from enumerate class MZD_PRBS_SELECTOR_TYPE
    :param txBitCount_p: A pointer of c_uint64
    :param rxBitCount_p: A pointer of c_uint64
    :param rxBitErrorCount_p: A pointer of c_uint64
    """
    func = MZDAPILib["mzdGetPRBSCounts"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_int, POINTER(c_uint64), POINTER(c_uint64), POINTER(c_uint64)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, pattSel, txBitCount_p, rxBitCount_p, rxBitErrorCount_p)
    return ret


def mzdSetTxRxPolarity(pDev, mdioPort, host_or_line, laneOffset, txPolarity, rxPolarity):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param txPolarity: argument type c_uint8
    :param rxPolarity: argument type c_uint8
    """
    func = MZDAPILib["mzdSetTxRxPolarity"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint8, c_uint8]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, txPolarity, rxPolarity)
    return ret


def mzdGetTxRxPolarity(pDev, mdioPort, host_or_line, laneOffset, txPolarity_p, rxPolarity_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param txPolarity_p: A pointer of c_uint8
    :param rxPolarity_p: A pointer of c_uint8
    """
    func = MZDAPILib["mzdGetTxRxPolarity"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_uint8), POINTER(c_uint8)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, txPolarity_p, rxPolarity_p)
    return ret


def mzdSetTxFFE(pDev, mdioPort, host_or_line, laneOffset, txEqParamType, paramValue):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param txEqParamType: member from enumerate class E_N5C112GX4_TXEQ_PARAM
    :param paramValue: argument type c_uint32
    """
    func = MZDAPILib["mzdSetTxFFE"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_int, c_uint32]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, txEqParamType, paramValue)
    return ret


def mzdGetTxFFE(pDev, mdioPort, host_or_line, laneOffset, txEqParamType, paramValue_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param txEqParamType: member from enumerate class E_N5C112GX4_TXEQ_PARAM
    :param paramValue_p: A pointer of c_uint32
    """
    func = MZDAPILib["mzdGetTxFFE"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_int, POINTER(c_uint32)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, txEqParamType, paramValue_p)
    return ret


def mzdDiagStateDump(pDev, mdioPort, host_or_line, laneOffset, stateDumpOptions, pStateDumpInfo_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param stateDumpOptions: argument type c_uint32
    :param pStateDumpInfo_p: A pointer of the structure class MZD_STATE_DUMP
    """
    func = MZDAPILib["mzdDiagStateDump"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint32, POINTER(MZD_STATE_DUMP)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, stateDumpOptions, pStateDumpInfo_p)
    return ret


def mzdSetRsFecControl(pDev, mdioPort, host_or_line, laneOffset, bypassIndicationEnable, bypassCorrectionEnable):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param bypassIndicationEnable: argument type c_uint16
    :param bypassCorrectionEnable: argument type c_uint16
    """
    func = MZDAPILib["mzdSetRsFecControl"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint16, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, bypassIndicationEnable, bypassCorrectionEnable)
    return ret


def mzdGetRsFecControl(pDev, mdioPort, host_or_line, laneOffset, bypassIndicationEnable_p, bypassCorrectionEnable_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param bypassIndicationEnable_p: A pointer of c_uint16
    :param bypassCorrectionEnable_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdGetRsFecControl"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_uint16), POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, bypassIndicationEnable_p, bypassCorrectionEnable_p)
    return ret


def mzdGetRsFecStatus(pDev, mdioPort, host_or_line, laneOffset, pcsLaneAlignment_p, fecLaneAlignment_p, rsFecLaneAMLock_p, latchedRsFecHighErr_p, currRsFecHighErr_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param pcsLaneAlignment_p: A pointer of c_uint16
    :param fecLaneAlignment_p: A pointer of c_uint16
    :param rsFecLaneAMLock_p: A pointer of c_uint16
    :param latchedRsFecHighErr_p: A pointer of c_uint16
    :param currRsFecHighErr_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdGetRsFecStatus"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_uint16), POINTER(c_uint16), POINTER(c_uint16), POINTER(c_uint16), POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, pcsLaneAlignment_p, fecLaneAlignment_p, rsFecLaneAMLock_p, latchedRsFecHighErr_p, currRsFecHighErr_p)
    return ret


def mzdGetRsFecPCSAlignmentStatus(pDev, mdioPort, host_or_line, laneOffset, pcs_lane, blockLocked_p, laneAligned_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param pcs_lane: argument type c_uint16
    :param blockLocked_p: A pointer of c_uint16
    :param laneAligned_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdGetRsFecPCSAlignmentStatus"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint16, POINTER(c_uint16), POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, pcs_lane, blockLocked_p, laneAligned_p)
    return ret


def mzdGetRsFecPMALaneMapping(pDev, mdioPort, host_or_line, laneOffset, mappingMZD_NUM_LANES_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param mappingMZD_NUM_LANES_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdGetRsFecPMALaneMapping"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, mappingMZD_NUM_LANES_p)
    return ret


def mzdGetRxPCSLaneMapping(pDev, mdioPort, host_or_line, lane_offset, interface_lane, pcs_lane_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param lane_offset: argument type c_uint16
    :param interface_lane: argument type c_uint16
    :param pcs_lane_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdGetRxPCSLaneMapping"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint16, POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, lane_offset, interface_lane, pcs_lane_p)
    return ret


def mzdGetRsFecCorrectedCwCntr(pDev, mdioPort, host_or_line, laneOffset, codeWordCounter_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param codeWordCounter_p: A pointer of c_uint32
    """
    func = MZDAPILib["mzdGetRsFecCorrectedCwCntr"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_uint32)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, codeWordCounter_p)
    return ret


def mzdGetRsFecUnCorrectedCwCntr(pDev, mdioPort, host_or_line, laneOffset, codeWordCounter_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param codeWordCounter_p: A pointer of c_uint32
    """
    func = MZDAPILib["mzdGetRsFecUnCorrectedCwCntr"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_uint32)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, codeWordCounter_p)
    return ret


def mzdGetRsFecSymbolErrorCntr(pDev, mdioPort, host_or_line, laneOffset, fecLane, errorCounter_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param fecLane: argument type c_uint16
    :param errorCounter_p: A pointer of c_uint32
    """
    func = MZDAPILib["mzdGetRsFecSymbolErrorCntr"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint16, POINTER(c_uint32)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, fecLane, errorCounter_p)
    return ret


def mzdGetRxPcsBipErrorCntr(pDev, mdioPort, host_or_line, laneOffset, pcs_lane, errorCounter_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param pcs_lane: argument type c_uint16
    :param errorCounter_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdGetRxPcsBipErrorCntr"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint16, POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, pcs_lane, errorCounter_p)
    return ret


def mzdSetRsFecSERControl(pDev, mdioPort, host_or_line, laneOffset, degradedSEREnable, bypassIndicationEnable):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param degradedSEREnable: argument type c_uint16
    :param bypassIndicationEnable: argument type c_uint16
    """
    func = MZDAPILib["mzdSetRsFecSERControl"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint16, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, degradedSEREnable, bypassIndicationEnable)
    return ret


def mzdGetRsFecSERControl(pDev, mdioPort, host_or_line, laneOffset, degradedSEREnable_p, bypassIndicationEnable_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param degradedSEREnable_p: A pointer of c_uint16
    :param bypassIndicationEnable_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdGetRsFecSERControl"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_uint16), POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, degradedSEREnable_p, bypassIndicationEnable_p)
    return ret


def mzdSetRsFecSERThresholds(pDev, mdioPort, host_or_line, laneOffset, serActivateThreshold, serDeactivateThreshold, serInterval):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param serActivateThreshold: argument type c_uint32
    :param serDeactivateThreshold: argument type c_uint32
    :param serInterval: argument type c_uint32
    """
    func = MZDAPILib["mzdSetRsFecSERThresholds"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint32, c_uint32, c_uint32]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, serActivateThreshold, serDeactivateThreshold, serInterval)
    return ret


def mzdGetRsFecSERThresholds(pDev, mdioPort, host_or_line, laneOffset, serActivateThreshold_p, serDeactivateThreshold_p, serInterval_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param serActivateThreshold_p: A pointer of c_uint32
    :param serDeactivateThreshold_p: A pointer of c_uint32
    :param serInterval_p: A pointer of c_uint32
    """
    func = MZDAPILib["mzdGetRsFecSERThresholds"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_uint32), POINTER(c_uint32), POINTER(c_uint32)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, serActivateThreshold_p, serDeactivateThreshold_p, serInterval_p)
    return ret


def mzdGetRsFecDegradedSERStatus(pDev, mdioPort, host_or_line, laneOffset, localDegradedSerRcvd_p, remoteDegradedSerRcvd_p, serDegraded_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param localDegradedSerRcvd_p: A pointer of c_uint16
    :param remoteDegradedSerRcvd_p: A pointer of c_uint16
    :param serDegraded_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdGetRsFecDegradedSERStatus"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_uint16), POINTER(c_uint16), POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, localDegradedSerRcvd_p, remoteDegradedSerRcvd_p, serDegraded_p)
    return ret


def mzdSetKrFecControl(pDev, mdioPort, host_or_line, laneOffset, bypassIndicationEnable):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param bypassIndicationEnable: argument type c_uint16
    """
    func = MZDAPILib["mzdSetKrFecControl"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, bypassIndicationEnable)
    return ret


def mzdGetKrFecControl(pDev, mdioPort, host_or_line, laneOffset, bypassIndicationEnable_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param bypassIndicationEnable_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdGetKrFecControl"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, bypassIndicationEnable_p)
    return ret


def mzdGetKrFecAbility(pDev, mdioPort, host_or_line, laneOffset, krFecAbility_p, errIndicationAbility_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param krFecAbility_p: A pointer of c_uint16
    :param errIndicationAbility_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdGetKrFecAbility"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_uint16), POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, krFecAbility_p, errIndicationAbility_p)
    return ret


def mzdGetKrFecCorrectedBlkCntr(pDev, mdioPort, host_or_line, laneOffset, blockCounter_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param blockCounter_p: A pointer of c_uint32
    """
    func = MZDAPILib["mzdGetKrFecCorrectedBlkCntr"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_uint32)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, blockCounter_p)
    return ret


def mzdGetKrFecUnCorrectedBlkCntr(pDev, mdioPort, host_or_line, laneOffset, blockCounter_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param blockCounter_p: A pointer of c_uint32
    """
    func = MZDAPILib["mzdGetKrFecUnCorrectedBlkCntr"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_uint32)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, blockCounter_p)
    return ret


def mzdFECCounterEnable(pDev, mdioPort, host_or_line, laneOffset, enable, readToClear):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param enable: argument type c_uint16
    :param readToClear: member from enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdFECCounterEnable"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint16, c_int]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, enable, readToClear)
    return ret


def mzdFECCounterSnapshot(pDev, mdioPort, host_or_line):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    """
    func = MZDAPILib["mzdFECCounterSnapshot"]
    func.argtypes = [c_void_p, c_uint16, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line)
    return ret


def mzdFECCounterReset(pDev, mdioPort, host_or_line, laneOffset):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    """
    func = MZDAPILib["mzdFECCounterReset"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset)
    return ret


def mzdFECReadCodewordCounters(pDev, mdioPort, host_or_line, laneOffset, numCodeWords_p, numUncorrectable_p, numCorrected_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param numCodeWords_p: A pointer of c_uint64
    :param numUncorrectable_p: A pointer of c_uint32
    :param numCorrected_p: A pointer of c_uint32
    """
    func = MZDAPILib["mzdFECReadCodewordCounters"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_uint64), POINTER(c_uint32), POINTER(c_uint32)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, numCodeWords_p, numUncorrectable_p, numCorrected_p)
    return ret


def mzdFECReadBurstSymbolErrorCtrs(pDev, mdioPort, host_or_line, laneOffset, burst2Symbols_p, burst3Symbols_p, burst4Symbols_p, burst5Symbols_p, burst6Symbols_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param burst2Symbols_p: A pointer of c_uint32
    :param burst3Symbols_p: A pointer of c_uint16
    :param burst4Symbols_p: A pointer of c_uint16
    :param burst5Symbols_p: A pointer of c_uint16
    :param burst6Symbols_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdFECReadBurstSymbolErrorCtrs"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_uint32), POINTER(c_uint16), POINTER(c_uint16), POINTER(c_uint16), POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, burst2Symbols_p, burst3Symbols_p, burst4Symbols_p, burst5Symbols_p, burst6Symbols_p)
    return ret


def mzdFECReadSymbolErrorCounters(pDev, mdioPort, host_or_line, laneOffset, symbolErrorCounters0to1_p, symbolErrorCounters2to4_p, symbolErrorCounters5to15_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param symbolErrorCounters0to1_p: A pointer of c_uint64
    :param symbolErrorCounters2to4_p: A pointer of c_uint32
    :param symbolErrorCounters5to15_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdFECReadSymbolErrorCounters"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_uint64), POINTER(c_uint32), POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, symbolErrorCounters0to1_p, symbolErrorCounters2to4_p, symbolErrorCounters5to15_p)
    return ret


def mzdFirmwareDownload(pDev, fwImageData_p, fwImageSize, errCode_p):
    """
    :param pDev: argument type c_void_p
    :param fwImageData_p: A pointer of c_uint8
    :param fwImageSize: argument type c_uint32
    :param errCode_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdFirmwareDownload"]
    func.argtypes = [c_void_p, POINTER(c_uint8), c_uint32, POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, fwImageData_p, fwImageSize, errCode_p)
    return ret


def mzdUpdateFlashImage(pDev, fwImageData_p, fwImageSize, slaveData_p, slaveSize, errCode_p):
    """
    :param pDev: argument type c_void_p
    :param fwImageData_p: A pointer of c_uint8
    :param fwImageSize: argument type c_uint32
    :param slaveData_p: A pointer of c_uint8
    :param slaveSize: argument type c_uint32
    :param errCode_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdUpdateFlashImage"]
    func.argtypes = [c_void_p, POINTER(c_uint8), c_uint32, POINTER(c_uint8), c_uint32, POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, fwImageData_p, fwImageSize, slaveData_p, slaveSize, errCode_p)
    return ret


def mzdParallelFirmwareDownload(pDev_p, numPorts, fwImageData_p, fwImageSize, pErrDev_p, errCode_p):
    """
    :param pDev: argument type c_void_p
    :param numPorts: argument type c_uint16
    :param fwImageData_p: A pointer of c_uint8
    :param fwImageSize: argument type c_uint32
    :param pErrDev: argument type c_void_p
    :param errCode_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdParallelFirmwareDownload"]
    func.argtypes = [c_void_p, c_uint16, POINTER(c_uint8), c_uint32, c_void_p, POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev_p, numPorts, fwImageData_p, fwImageSize, pErrDev_p, errCode_p)
    return ret


def mzdParallelUpdateFlashImage(pDev_p, numPorts, fwImageData_p, fwImageSize, slaveData_p, slaveSize, pErrDev_p, errCode_p):
    """
    :param pDev: argument type c_void_p
    :param numPorts: argument type c_uint16
    :param fwImageData_p: A pointer of c_uint8
    :param fwImageSize: argument type c_uint32
    :param slaveData_p: A pointer of c_uint8
    :param slaveSize: argument type c_uint32
    :param pErrDev: argument type c_void_p
    :param errCode_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdParallelUpdateFlashImage"]
    func.argtypes = [c_void_p, c_uint16, POINTER(c_uint8), c_uint32, POINTER(c_uint8), c_uint32, c_void_p, POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev_p, numPorts, fwImageData_p, fwImageSize, slaveData_p, slaveSize, pErrDev_p, errCode_p)
    return ret


def mzdLoadFlashImageToRAM(pDev, errCode_p):
    """
    :param pDev: argument type c_void_p
    :param errCode_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdLoadFlashImageToRAM"]
    func.argtypes = [c_void_p, POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, errCode_p)
    return ret


def mzdHwAPBusRead(pDev, regAPBAddr, data_p):
    """
    :param pDev: argument type c_void_p
    :param regAPBAddr: argument type c_uint32
    :param data_p: A pointer of c_uint32
    """
    func = MZDAPILib["mzdHwAPBusRead"]
    func.argtypes = [c_void_p, c_uint32, POINTER(c_uint32)]
    func.restype = c_uint32
    ret = func(pDev, regAPBAddr, data_p)
    return ret


def mzdHwAPBusWrite(pDev, regAPBAddr, data):
    """
    :param pDev: argument type c_void_p
    :param regAPBAddr: argument type c_uint32
    :param data: argument type c_uint32
    """
    func = MZDAPILib["mzdHwAPBusWrite"]
    func.argtypes = [c_void_p, c_uint32, c_uint32]
    func.restype = c_uint32
    ret = func(pDev, regAPBAddr, data)
    return ret


def mzdHwAPBusWriteBlock(pDev, regAPBAddr, data_p, size):
    """
    :param pDev: argument type c_void_p
    :param regAPBAddr: argument type c_uint32
    :param data_p: A pointer of c_uint32
    :param size: argument type c_uint32
    """
    func = MZDAPILib["mzdHwAPBusWriteBlock"]
    func.argtypes = [c_void_p, c_uint32, POINTER(c_uint32), c_uint32]
    func.restype = c_uint32
    ret = func(pDev, regAPBAddr, data_p, size)
    return ret


def mzdHwAPBusReadBlock(pDev, regAPBAddr, size, data_p):
    """
    :param pDev: argument type c_void_p
    :param regAPBAddr: argument type c_uint32
    :param size: argument type c_uint32
    :param data_p: A pointer of c_uint32
    """
    func = MZDAPILib["mzdHwAPBusReadBlock"]
    func.argtypes = [c_void_p, c_uint32, c_uint32, POINTER(c_uint32)]
    func.restype = c_uint32
    ret = func(pDev, regAPBAddr, size, data_p)
    return ret


def mzdHwAPBusSetRegField(pDev, regAPBAddr, fieldOffset, fieldLength, data):
    """
    :param pDev: argument type c_void_p
    :param regAPBAddr: argument type c_uint32
    :param fieldOffset: argument type c_uint8
    :param fieldLength: argument type c_uint8
    :param data: argument type c_uint32
    """
    func = MZDAPILib["mzdHwAPBusSetRegField"]
    func.argtypes = [c_void_p, c_uint32, c_uint8, c_uint8, c_uint32]
    func.restype = c_uint32
    ret = func(pDev, regAPBAddr, fieldOffset, fieldLength, data)
    return ret


def mzdHwAPBusGetRegField(pDev, regAPBAddr, fieldOffset, fieldLength, data_p):
    """
    :param pDev: argument type c_void_p
    :param regAPBAddr: argument type c_uint32
    :param fieldOffset: argument type c_uint8
    :param fieldLength: argument type c_uint8
    :param data_p: A pointer of c_uint32
    """
    func = MZDAPILib["mzdHwAPBusGetRegField"]
    func.argtypes = [c_void_p, c_uint32, c_uint8, c_uint8, POINTER(c_uint32)]
    func.restype = c_uint32
    ret = func(pDev, regAPBAddr, fieldOffset, fieldLength, data_p)
    return ret


def mzdHwLockAPBSemaphore(pDev, semOption):
    """
    :param pDev: argument type c_void_p
    :param semOption: argument type c_uint16
    """
    func = MZDAPILib["mzdHwLockAPBSemaphore"]
    func.argtypes = [c_void_p, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, semOption)
    return ret


def mzdHwReleaseAPBSemaphore(pDev, semOption):
    """
    :param pDev: argument type c_void_p
    :param semOption: argument type c_uint16
    """
    func = MZDAPILib["mzdHwReleaseAPBSemaphore"]
    func.argtypes = [c_void_p, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, semOption)
    return ret


def mzdHwAPBSemaphoreConfig(pDev, semConfigOption):
    """
    :param pDev: argument type c_void_p
    :param semConfigOption: argument type c_uint16
    """
    func = MZDAPILib["mzdHwAPBSemaphoreConfig"]
    func.argtypes = [c_void_p, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, semConfigOption)
    return ret


def mzdHwXmdioWrite(pDev, mdioPort, dev, reg, value):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param dev: argument type c_uint16
    :param reg: argument type c_uint16
    :param value: argument type c_uint16
    """
    func = MZDAPILib["mzdHwXmdioWrite"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, dev, reg, value)
    return ret


def mzdHwXmdioRead(pDev, mdioPort, dev, reg, data_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param dev: argument type c_uint16
    :param reg: argument type c_uint16
    :param data_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdHwXmdioRead"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, dev, reg, data_p)
    return ret


def mzdHwGetPhyRegField(pDev, mdioPort, dev, regAddr, fieldOffset, fieldLength, data_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param dev: argument type c_uint16
    :param regAddr: argument type c_uint16
    :param fieldOffset: argument type c_uint8
    :param fieldLength: argument type c_uint8
    :param data_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdHwGetPhyRegField"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint8, c_uint8, POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, dev, regAddr, fieldOffset, fieldLength, data_p)
    return ret


def mzdHwSetPhyRegField(pDev, mdioPort, dev, regAddr, fieldOffset, fieldLength, data):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param dev: argument type c_uint16
    :param regAddr: argument type c_uint16
    :param fieldOffset: argument type c_uint8
    :param fieldLength: argument type c_uint8
    :param data: argument type c_uint16
    """
    func = MZDAPILib["mzdHwSetPhyRegField"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint8, c_uint8, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, dev, regAddr, fieldOffset, fieldLength, data)
    return ret


def mzdHwGetRegFieldFromWord(regData, fieldOffset, fieldLength, data_p):
    """
    :param regData: argument type c_uint16
    :param fieldOffset: argument type c_uint8
    :param fieldLength: argument type c_uint8
    :param data_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdHwGetRegFieldFromWord"]
    func.argtypes = [c_uint16, c_uint8, c_uint8, POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(regData, fieldOffset, fieldLength, data_p)
    return ret


def mzdHwSetRegFieldToWord(regData, bitFieldData, fieldOffset, fieldLength, data_p):
    """
    :param regData: argument type c_uint16
    :param bitFieldData: argument type c_uint16
    :param fieldOffset: argument type c_uint8
    :param fieldLength: argument type c_uint8
    :param data_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdHwSetRegFieldToWord"]
    func.argtypes = [c_uint16, c_uint16, c_uint8, c_uint8, POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(regData, bitFieldData, fieldOffset, fieldLength, data_p)
    return ret


def mzdHwWaitForRegFieldValue(pDev, mdioPort, dev, regAddr, fieldOffset, fieldLength, expectedValue, timeoutMs):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param dev: argument type c_uint16
    :param regAddr: argument type c_uint16
    :param fieldOffset: argument type c_uint8
    :param fieldLength: argument type c_uint8
    :param expectedValue: argument type c_uint16
    :param timeoutMs: argument type c_uint16
    """
    func = MZDAPILib["mzdHwWaitForRegFieldValue"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint8, c_uint8, c_uint16, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, dev, regAddr, fieldOffset, fieldLength, expectedValue, timeoutMs)
    return ret


def mzdHwWaitForRegFieldValueList(pDev, mdioPort, dev, regAddr, fieldOffset, fieldLength, expectedValueList_p, numOfExpValue, timeoutMs, fieldValue_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param dev: argument type c_uint16
    :param regAddr: argument type c_uint16
    :param fieldOffset: argument type c_uint8
    :param fieldLength: argument type c_uint8
    :param expectedValueList_p: A pointer of c_uint16
    :param numOfExpValue: argument type c_uint16
    :param timeoutMs: argument type c_uint16
    :param fieldValue_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdHwWaitForRegFieldValueList"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint8, c_uint8, POINTER(c_uint16), c_uint16, c_uint16, POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, dev, regAddr, fieldOffset, fieldLength, expectedValueList_p, numOfExpValue, timeoutMs, fieldValue_p)
    return ret


def mzdHwXmdioBlockWrite(pDev, mdioPort, dev, reg, data_p, dataSize):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param dev: argument type c_uint16
    :param reg: argument type c_uint16
    :param data_p: A pointer of c_uint8
    :param dataSize: argument type c_uint32
    """
    func = MZDAPILib["mzdHwXmdioBlockWrite"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_uint8), c_uint32]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, dev, reg, data_p, dataSize)
    return ret


def mzdWait(pDev, waitTime):
    """
    :param pDev: argument type c_void_p
    :param waitTime: argument type c_uint
    """
    func = MZDAPILib["mzdWait"]
    func.argtypes = [c_void_p, c_uint]
    func.restype = c_uint32
    ret = func(pDev, waitTime)
    return ret


def mzdMacSecMappedDevAddr(deviceId, deviceNum, firstOffset, lastOffset, HostContext_p, platfromFirstOffset_p, platfromLastOffset_p):
    """
    :param deviceId: argument type c_uint32
    :param deviceNum: argument type c_uint32
    :param firstOffset: argument type c_uint32
    :param lastOffset: argument type c_uint32
    :param HostContext: argument type c_void_p
    :param platfromFirstOffset_p: A pointer of c_uint32
    :param platfromLastOffset_p: A pointer of c_uint32
    """
    func = MZDAPILib["mzdMacSecMappedDevAddr"]
    func.argtypes = [c_uint32, c_uint32, c_uint32, c_uint32, c_void_p, POINTER(c_uint32), POINTER(c_uint32)]
    func.restype = c_uint32
    ret = func(deviceId, deviceNum, firstOffset, lastOffset, HostContext_p, platfromFirstOffset_p, platfromLastOffset_p)
    return ret


def mzdSetMacSecDevInfo(pDev, macsecMapPort, macsecLane):
    """
    :param pDev: argument type c_void_p
    :param macsecMapPort: argument type c_uint16
    :param macsecLane: argument type c_uint16
    """
    func = MZDAPILib["mzdSetMacSecDevInfo"]
    func.argtypes = [c_void_p, c_uint16, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, macsecMapPort, macsecLane)
    return ret


def mzdHwMacSecRegWrite(pDev, macsecMapPort, macsecAddr, data):
    """
    :param pDev: argument type c_void_p
    :param macsecMapPort: argument type c_uint16
    :param macsecAddr: argument type c_uint32
    :param data: argument type c_uint32
    """
    func = MZDAPILib["mzdHwMacSecRegWrite"]
    func.argtypes = [c_void_p, c_uint16, c_uint32, c_uint32]
    func.restype = c_uint32
    ret = func(pDev, macsecMapPort, macsecAddr, data)
    return ret


def mzdHwMacSecRegRead(pDev, macsecMapPort, macsecAddr, data_p):
    """
    :param pDev: argument type c_void_p
    :param macsecMapPort: argument type c_uint16
    :param macsecAddr: argument type c_uint32
    :param data_p: A pointer of c_uint32
    """
    func = MZDAPILib["mzdHwMacSecRegRead"]
    func.argtypes = [c_void_p, c_uint16, c_uint32, POINTER(c_uint32)]
    func.restype = c_uint32
    ret = func(pDev, macsecMapPort, macsecAddr, data_p)
    return ret


def mzdHwSetMacSecRegField(pDev, macsecMapPort, macsecAddr, fieldOffset, fieldLength, data):
    """
    :param pDev: argument type c_void_p
    :param macsecMapPort: argument type c_uint16
    :param macsecAddr: argument type c_uint32
    :param fieldOffset: argument type c_uint8
    :param fieldLength: argument type c_uint8
    :param data: argument type c_uint32
    """
    func = MZDAPILib["mzdHwSetMacSecRegField"]
    func.argtypes = [c_void_p, c_uint16, c_uint32, c_uint8, c_uint8, c_uint32]
    func.restype = c_uint32
    ret = func(pDev, macsecMapPort, macsecAddr, fieldOffset, fieldLength, data)
    return ret


def mzdHwGetMacSecRegField(pDev, macsecMapPort, macsecAddr, fieldOffset, fieldLength, data_p):
    """
    :param pDev: argument type c_void_p
    :param macsecMapPort: argument type c_uint16
    :param macsecAddr: argument type c_uint32
    :param fieldOffset: argument type c_uint8
    :param fieldLength: argument type c_uint8
    :param data_p: A pointer of c_uint32
    """
    func = MZDAPILib["mzdHwGetMacSecRegField"]
    func.argtypes = [c_void_p, c_uint16, c_uint32, c_uint8, c_uint8, POINTER(c_uint32)]
    func.restype = c_uint32
    ret = func(pDev, macsecMapPort, macsecAddr, fieldOffset, fieldLength, data_p)
    return ret


def mzdHwMacSecSBUFRegWrite(pDev, macsecMapPort, macsecAddr, data):
    """
    :param pDev: argument type c_void_p
    :param macsecMapPort: argument type c_uint16
    :param macsecAddr: argument type c_uint32
    :param data: argument type c_uint32
    """
    func = MZDAPILib["mzdHwMacSecSBUFRegWrite"]
    func.argtypes = [c_void_p, c_uint16, c_uint32, c_uint32]
    func.restype = c_uint32
    ret = func(pDev, macsecMapPort, macsecAddr, data)
    return ret


def mzdHwMacSecSBUFRegRead(pDev, macsecMapPort, macsecAddr, data_p):
    """
    :param pDev: argument type c_void_p
    :param macsecMapPort: argument type c_uint16
    :param macsecAddr: argument type c_uint32
    :param data_p: A pointer of c_uint32
    """
    func = MZDAPILib["mzdHwMacSecSBUFRegRead"]
    func.argtypes = [c_void_p, c_uint16, c_uint32, POINTER(c_uint32)]
    func.restype = c_uint32
    ret = func(pDev, macsecMapPort, macsecAddr, data_p)
    return ret


def mzdHwSetMacSecSBUFRegField(pDev, macsecMapPort, macsecAddr, fieldOffset, fieldLength, data):
    """
    :param pDev: argument type c_void_p
    :param macsecMapPort: argument type c_uint16
    :param macsecAddr: argument type c_uint32
    :param fieldOffset: argument type c_uint8
    :param fieldLength: argument type c_uint8
    :param data: argument type c_uint32
    """
    func = MZDAPILib["mzdHwSetMacSecSBUFRegField"]
    func.argtypes = [c_void_p, c_uint16, c_uint32, c_uint8, c_uint8, c_uint32]
    func.restype = c_uint32
    ret = func(pDev, macsecMapPort, macsecAddr, fieldOffset, fieldLength, data)
    return ret


def mzdHwGetMacSecSBUFRegField(pDev, macsecMapPort, macsecAddr, fieldOffset, fieldLength, data_p):
    """
    :param pDev: argument type c_void_p
    :param macsecMapPort: argument type c_uint16
    :param macsecAddr: argument type c_uint32
    :param fieldOffset: argument type c_uint8
    :param fieldLength: argument type c_uint8
    :param data_p: A pointer of c_uint32
    """
    func = MZDAPILib["mzdHwGetMacSecSBUFRegField"]
    func.argtypes = [c_void_p, c_uint16, c_uint32, c_uint8, c_uint8, POINTER(c_uint32)]
    func.restype = c_uint32
    ret = func(pDev, macsecMapPort, macsecAddr, fieldOffset, fieldLength, data_p)
    return ret


def mzdHwMacRegWrite(pDev, macMapPort, host_or_line, macAddr, data):
    """
    :param pDev: argument type c_void_p
    :param macMapPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param macAddr: argument type c_uint32
    :param data: argument type c_uint32
    """
    func = MZDAPILib["mzdHwMacRegWrite"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint32, c_uint32]
    func.restype = c_uint32
    ret = func(pDev, macMapPort, host_or_line, macAddr, data)
    return ret


def mzdHwMacRegRead(pDev, macMapPort, host_or_line, macAddr, data_p):
    """
    :param pDev: argument type c_void_p
    :param macMapPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param macAddr: argument type c_uint32
    :param data_p: A pointer of c_uint32
    """
    func = MZDAPILib["mzdHwMacRegRead"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint32, POINTER(c_uint32)]
    func.restype = c_uint32
    ret = func(pDev, macMapPort, host_or_line, macAddr, data_p)
    return ret


def mzdHwSetMacRegField(pDev, macMapPort, host_or_line, macAddr, fieldOffset, fieldLength, data):
    """
    :param pDev: argument type c_void_p
    :param macMapPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param macAddr: argument type c_uint32
    :param fieldOffset: argument type c_uint8
    :param fieldLength: argument type c_uint8
    :param data: argument type c_uint32
    """
    func = MZDAPILib["mzdHwSetMacRegField"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint32, c_uint8, c_uint8, c_uint32]
    func.restype = c_uint32
    ret = func(pDev, macMapPort, host_or_line, macAddr, fieldOffset, fieldLength, data)
    return ret


def mzdHwGetMacRegField(pDev, macMapPort, host_or_line, macAddr, fieldOffset, fieldLength, data_p):
    """
    :param pDev: argument type c_void_p
    :param macMapPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param macAddr: argument type c_uint32
    :param fieldOffset: argument type c_uint8
    :param fieldLength: argument type c_uint8
    :param data_p: A pointer of c_uint32
    """
    func = MZDAPILib["mzdHwGetMacRegField"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint32, c_uint8, c_uint8, POINTER(c_uint32)]
    func.restype = c_uint32
    ret = func(pDev, macMapPort, host_or_line, macAddr, fieldOffset, fieldLength, data_p)
    return ret


def mzdInitSerdesDev(pDev, serdesRead_p, serdesWrite_p):
    """
    :param pDev: argument type c_void_p
    :param serdesRead: a function pointer
    :param serdesWrite: a function pointer
    """
    func = MZDAPILib["mzdInitSerdesDev"]
    func.argtypes = [c_void_p, CFUNCTYPE(c_void_p, c_uint32, POINTER(c_uint32)), CFUNCTYPE(c_void_p, c_uint32, c_uint32)]
    func.restype = c_uint32
    ret = func(pDev, serdesRead_p, serdesWrite_p)
    return ret


def mzdSetSerdesDevInfo(pDev, serdesMapPort, serdesMapHostLine):
    """
    :param pDev: argument type c_void_p
    :param serdesMapPort: argument type c_uint16
    :param serdesMapHostLine: argument type c_uint16
    """
    func = MZDAPILib["mzdSetSerdesDevInfo"]
    func.argtypes = [c_void_p, c_uint16, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, serdesMapPort, serdesMapHostLine)
    return ret


def mzdHwSerdesPhyRegWrite(pDev, mdioPort, host_or_line, serdesLane, regAddr, data):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param serdesLane: argument type c_uint16
    :param regAddr: argument type c_uint32
    :param data: argument type c_uint32
    """
    func = MZDAPILib["mzdHwSerdesPhyRegWrite"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint32, c_uint32]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, serdesLane, regAddr, data)
    return ret


def mzdHwSerdesPhyRegRead(pDev, mdioPort, host_or_line, serdesLane, regAddr, data_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param serdesLane: argument type c_uint16
    :param regAddr: argument type c_uint32
    :param data_p: A pointer of c_uint32
    """
    func = MZDAPILib["mzdHwSerdesPhyRegRead"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint32, POINTER(c_uint32)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, serdesLane, regAddr, data_p)
    return ret


def mzdHwSetSerdesPhyRegField(pDev, mdioPort, host_or_line, serdesLane, regAddr, fieldOffset, fieldLength, data):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param serdesLane: argument type c_uint16
    :param regAddr: argument type c_uint32
    :param fieldOffset: argument type c_uint8
    :param fieldLength: argument type c_uint8
    :param data: argument type c_uint32
    """
    func = MZDAPILib["mzdHwSetSerdesPhyRegField"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint32, c_uint8, c_uint8, c_uint32]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, serdesLane, regAddr, fieldOffset, fieldLength, data)
    return ret


def mzdHwGetSerdesPhyRegField(pDev, mdioPort, host_or_line, serdesLane, regAddr, fieldOffset, fieldLength, data_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param serdesLane: argument type c_uint16
    :param regAddr: argument type c_uint32
    :param fieldOffset: argument type c_uint8
    :param fieldLength: argument type c_uint8
    :param data_p: A pointer of c_uint32
    """
    func = MZDAPILib["mzdHwGetSerdesPhyRegField"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint32, c_uint8, c_uint8, POINTER(c_uint32)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, serdesLane, regAddr, fieldOffset, fieldLength, data_p)
    return ret


def mzdHwSerdesPhyLaneRegBroadcast(pDev, mdioPort, host_or_line, enable):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param enable: argument type c_uint32
    """
    func = MZDAPILib["mzdHwSerdesPhyLaneRegBroadcast"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint32]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, enable)
    return ret


def mzdInitDriver(mzdFuncReadMdio_p, mzdFuncWriteMdio_p, mzdFuncWait_p, serdesRead_p, serdesWrite_p, mdioPort, pFirmwareImage_p, firmwareSize, pHostContext, pDev):
    """
    :param mzdFuncReadMdio: a function pointer
    :param mzdFuncWriteMdio: a function pointer
    :param mzdFuncWait: a function pointer
    :param serdesRead: a function pointer
    :param serdesWrite: a function pointer
    :param mdioPort: argument type c_uint16
    :param pFirmwareImage_p: A pointer of c_uint8
    :param firmwareSize: argument type c_uint32
    :param pHostContext: argument type c_void_p
    :param pDev: argument type c_void_p
    """
    func = MZDAPILib["mzdInitDriver"]
    func.argtypes = [CFUNCTYPE(c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_uint16)), CFUNCTYPE(c_void_p, c_uint16, c_uint16, c_uint16, c_uint16), CFUNCTYPE(c_void_p, c_uint), CFUNCTYPE(c_void_p, c_uint32, POINTER(c_uint32)), CFUNCTYPE(c_void_p, c_uint32, c_uint32), c_uint16, POINTER(c_uint8), c_uint32, c_void_p, c_void_p]
    func.restype = c_uint32
    ret = func(mzdFuncReadMdio_p, mzdFuncWriteMdio_p, mzdFuncWait_p, serdesRead_p, serdesWrite_p, mdioPort, pFirmwareImage_p, firmwareSize, pHostContext, pDev)
    return ret


def mzdReloadDriver(mzdFuncReadMdio_p, mzdFuncWriteMdio_p, mzdFuncWait_p, serdesRead_p, serdesWrite_p, mdioPort, pHostContext, optionFlag, pDev):
    """
    :param mzdFuncReadMdio: a function pointer
    :param mzdFuncWriteMdio: a function pointer
    :param mzdFuncWait: a function pointer
    :param serdesRead: a function pointer
    :param serdesWrite: a function pointer
    :param mdioPort: argument type c_uint16
    :param pHostContext: argument type c_void_p
    :param optionFlag: argument type c_uint16
    :param pDev: argument type c_void_p
    """
    func = MZDAPILib["mzdReloadDriver"]
    func.argtypes = [CFUNCTYPE(c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_uint16)), CFUNCTYPE(c_void_p, c_uint16, c_uint16, c_uint16, c_uint16), CFUNCTYPE(c_void_p, c_uint), CFUNCTYPE(c_void_p, c_uint32, POINTER(c_uint32)), CFUNCTYPE(c_void_p, c_uint32, c_uint32), c_uint16, c_void_p, c_uint16, c_void_p]
    func.restype = c_uint32
    ret = func(mzdFuncReadMdio_p, mzdFuncWriteMdio_p, mzdFuncWait_p, serdesRead_p, serdesWrite_p, mdioPort, pHostContext, optionFlag, pDev)
    return ret


def mzdUnloadDriver(pDev):
    """
    :param pDev: argument type c_void_p
    """
    func = MZDAPILib["mzdUnloadDriver"]
    func.argtypes = [c_void_p]
    func.restype = c_uint32
    ret = func(pDev)
    return ret


def mzdLanePowerdown(pDev, mdioPort, host_or_line, laneOffset):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    """
    func = MZDAPILib["mzdLanePowerdown"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset)
    return ret


def mzdLanePowerup(pDev, mdioPort, host_or_line, laneOffset):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    """
    func = MZDAPILib["mzdLanePowerup"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset)
    return ret


def mzdPortReset(pDev, mdioPort, host_or_line, resetType, timeoutMs):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param resetType: member from enumerate class MZD_RESET_TYPE
    :param timeoutMs: argument type c_uint16
    """
    func = MZDAPILib["mzdPortReset"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_int, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, resetType, timeoutMs)
    return ret


def mzdChipResetControl(pDev, resetType, bRestore):
    """
    :param pDev: argument type c_void_p
    :param resetType: argument type c_uint16
    :param bRestore: member from enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdChipResetControl"]
    func.argtypes = [c_void_p, c_uint16, c_int]
    func.restype = c_uint32
    ret = func(pDev, resetType, bRestore)
    return ret


def mzdGetIntrSrcStatus(pDev, intrSelector, forceInterrupt_p, intrSrc_p):
    """
    :param pDev: argument type c_void_p
    :param intrSelector: implementation of the structure class MZD_GLOBAL_CHIP_INTR
    :param forceInterrupt_p: A pointer of the enumerate class MZD_BOOL
    :param intrSrc_p: A pointer of the structure class MZD_GLOBAL_CHIP_INTR
    """
    func = MZDAPILib["mzdGetIntrSrcStatus"]
    func.argtypes = [c_void_p, MZD_GLOBAL_CHIP_INTR, POINTER(c_int), POINTER(MZD_GLOBAL_CHIP_INTR)]
    func.restype = c_uint32
    ret = func(pDev, intrSelector, forceInterrupt_p, intrSrc_p)
    return ret


def mzdSetGlobalInterruptCntl(pDev, openDrain, intrPolarity, forceInterrupt):
    """
    :param pDev: argument type c_void_p
    :param openDrain: member from enumerate class MZD_BOOL
    :param intrPolarity: argument type c_uint16
    :param forceInterrupt: member from enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdSetGlobalInterruptCntl"]
    func.argtypes = [c_void_p, c_int, c_uint16, c_int]
    func.restype = c_uint32
    ret = func(pDev, openDrain, intrPolarity, forceInterrupt)
    return ret


def mzdGetGlobalInterruptCntl(pDev, openDrain_p, intrPolarity_p, forceInterrupt_p):
    """
    :param pDev: argument type c_void_p
    :param openDrain_p: A pointer of the enumerate class MZD_BOOL
    :param intrPolarity_p: A pointer of c_uint16
    :param forceInterrupt_p: A pointer of the enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdGetGlobalInterruptCntl"]
    func.argtypes = [c_void_p, POINTER(c_int), POINTER(c_uint16), POINTER(c_int)]
    func.restype = c_uint32
    ret = func(pDev, openDrain_p, intrPolarity_p, forceInterrupt_p)
    return ret


def mzdSetGlobalInterruptEnable(pDev, globalAggregatedIntrEnable1, globalAggregatedIntrEnable2):
    """
    :param pDev: argument type c_void_p
    :param globalAggregatedIntrEnable1: argument type c_uint16
    :param globalAggregatedIntrEnable2: argument type c_uint16
    """
    func = MZDAPILib["mzdSetGlobalInterruptEnable"]
    func.argtypes = [c_void_p, c_uint16, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, globalAggregatedIntrEnable1, globalAggregatedIntrEnable2)
    return ret


def mzdGetGlobalInterruptEnable(pDev, globalAggregatedIntrEnable1_p, globalAggregatedIntrEnable2_p):
    """
    :param pDev: argument type c_void_p
    :param globalAggregatedIntrEnable1_p: A pointer of c_uint16
    :param globalAggregatedIntrEnable2_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdGetGlobalInterruptEnable"]
    func.argtypes = [c_void_p, POINTER(c_uint16), POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, globalAggregatedIntrEnable1_p, globalAggregatedIntrEnable2_p)
    return ret


def mzdGetUnmaskedInterrupts(pDev, intrSelector_p):
    """
    :param pDev: argument type c_void_p
    :param intrSelector_p: A pointer of the structure class MZD_GLOBAL_CHIP_INTR
    """
    func = MZDAPILib["mzdGetUnmaskedInterrupts"]
    func.argtypes = [c_void_p, POINTER(MZD_GLOBAL_CHIP_INTR)]
    func.restype = c_uint32
    ret = func(pDev, intrSelector_p)
    return ret


def mzdSetGPIOInterruptEnable(pDev, gpioPinId, gpioIntrEnable):
    """
    :param pDev: argument type c_void_p
    :param gpioPinId: member from enumerate class MZD_PIN_ID
    :param gpioIntrEnable: argument type c_uint16
    """
    func = MZDAPILib["mzdSetGPIOInterruptEnable"]
    func.argtypes = [c_void_p, c_int, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, gpioPinId, gpioIntrEnable)
    return ret


def mzdGetGPIOInterruptEnable(pDev, gpioPinId, gpioIntrEnable_p):
    """
    :param pDev: argument type c_void_p
    :param gpioPinId: member from enumerate class MZD_PIN_ID
    :param gpioIntrEnable_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdGetGPIOInterruptEnable"]
    func.argtypes = [c_void_p, c_int, POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, gpioPinId, gpioIntrEnable_p)
    return ret


def mzdSetGPIOInterruptType(pDev, gpioPinId, gpioIntrType):
    """
    :param pDev: argument type c_void_p
    :param gpioPinId: member from enumerate class MZD_PIN_ID
    :param gpioIntrType: argument type c_uint16
    """
    func = MZDAPILib["mzdSetGPIOInterruptType"]
    func.argtypes = [c_void_p, c_int, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, gpioPinId, gpioIntrType)
    return ret


def mzdGetGPIOInterruptType(pDev, gpioPinId, gpioIntrType_p):
    """
    :param pDev: argument type c_void_p
    :param gpioPinId: member from enumerate class MZD_PIN_ID
    :param gpioIntrType_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdGetGPIOInterruptType"]
    func.argtypes = [c_void_p, c_int, POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, gpioPinId, gpioIntrType_p)
    return ret


def mzdGetGPIOInterruptStatus(pDev, gpioPinId, gpioIntrLatchedStatus_p, gpioIntrCurrentStatus_p):
    """
    :param pDev: argument type c_void_p
    :param gpioPinId: member from enumerate class MZD_PIN_ID
    :param gpioIntrLatchedStatus_p: A pointer of c_uint16
    :param gpioIntrCurrentStatus_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdGetGPIOInterruptStatus"]
    func.argtypes = [c_void_p, c_int, POINTER(c_uint16), POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, gpioPinId, gpioIntrLatchedStatus_p, gpioIntrCurrentStatus_p)
    return ret


def mzdSetPCSInterruptEnable(pDev, mdioPort, host_or_line, laneOffset, intrEnable):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param intrEnable: implementation of the structure class MZD_PCS_UNIT_INTR
    """
    func = MZDAPILib["mzdSetPCSInterruptEnable"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, MZD_PCS_UNIT_INTR]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, intrEnable)
    return ret


def mzdGetPCSInterruptEnable(pDev, mdioPort, host_or_line, laneOffset, intrEnable_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param intrEnable_p: A pointer of the structure class MZD_PCS_UNIT_INTR
    """
    func = MZDAPILib["mzdGetPCSInterruptEnable"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(MZD_PCS_UNIT_INTR)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, intrEnable_p)
    return ret


def mzdGetPCSInterruptStatus(pDev, mdioPort, host_or_line, laneOffset, latchedIntrStatus_p, currentIntrStatus_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param latchedIntrStatus_p: A pointer of the structure class MZD_PCS_UNIT_INTR
    :param currentIntrStatus_p: A pointer of the structure class MZD_PCS_UNIT_INTR
    """
    func = MZDAPILib["mzdGetPCSInterruptStatus"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(MZD_PCS_UNIT_INTR), POINTER(MZD_PCS_UNIT_INTR)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, latchedIntrStatus_p, currentIntrStatus_p)
    return ret


def mzdGetPCSRealtimeStatus(pDev, mdioPort, host_or_line, laneOffset, rtIntrStatus_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param rtIntrStatus_p: A pointer of the structure class MZD_PCS_UNIT_INTR
    """
    func = MZDAPILib["mzdGetPCSRealtimeStatus"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(MZD_PCS_UNIT_INTR)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, rtIntrStatus_p)
    return ret


def mzdSetPinMode(pDev, pinId, pinMode, openDrain):
    """
    :param pDev: argument type c_void_p
    :param pinId: member from enumerate class MZD_PIN_ID
    :param pinMode: member from enumerate class MZD_PIN_MODE
    :param openDrain: member from enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdSetPinMode"]
    func.argtypes = [c_void_p, c_int, c_int, c_int]
    func.restype = c_uint32
    ret = func(pDev, pinId, pinMode, openDrain)
    return ret


def mzdGetPinMode(pDev, pinId, pinMode_p, openDrain_p):
    """
    :param pDev: argument type c_void_p
    :param pinId: member from enumerate class MZD_PIN_ID
    :param pinMode_p: A pointer of the enumerate class MZD_PIN_MODE
    :param openDrain_p: A pointer of the enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdGetPinMode"]
    func.argtypes = [c_void_p, c_int, POINTER(c_int), POINTER(c_int)]
    func.restype = c_uint32
    ret = func(pDev, pinId, pinMode_p, openDrain_p)
    return ret


def mzdSetGPIOPinDirection(pDev, gpioPinId, gpioPinDirection):
    """
    :param pDev: argument type c_void_p
    :param gpioPinId: member from enumerate class MZD_PIN_ID
    :param gpioPinDirection: argument type c_uint16
    """
    func = MZDAPILib["mzdSetGPIOPinDirection"]
    func.argtypes = [c_void_p, c_int, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, gpioPinId, gpioPinDirection)
    return ret


def mzdGetGPIOPinDirection(pDev, gpioPinId, gpioPinDirection_p):
    """
    :param pDev: argument type c_void_p
    :param gpioPinId: member from enumerate class MZD_PIN_ID
    :param gpioPinDirection_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdGetGPIOPinDirection"]
    func.argtypes = [c_void_p, c_int, POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, gpioPinId, gpioPinDirection_p)
    return ret


def mzdSetGPIOPinData(pDev, gpioPinId, gpioData):
    """
    :param pDev: argument type c_void_p
    :param gpioPinId: member from enumerate class MZD_PIN_ID
    :param gpioData: argument type c_uint16
    """
    func = MZDAPILib["mzdSetGPIOPinData"]
    func.argtypes = [c_void_p, c_int, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, gpioPinId, gpioData)
    return ret


def mzdGetGPIOPinData(pDev, gpioPinId, gpioData_p):
    """
    :param pDev: argument type c_void_p
    :param gpioPinId: member from enumerate class MZD_PIN_ID
    :param gpioData_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdGetGPIOPinData"]
    func.argtypes = [c_void_p, c_int, POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, gpioPinId, gpioData_p)
    return ret


def mzdSetLEDControl(pDev, ledPinId, ledCtrl):
    """
    :param pDev: argument type c_void_p
    :param ledPinId: member from enumerate class MZD_PIN_ID
    :param ledCtrl: implementation of the structure class MZD_LED_CTRL
    """
    func = MZDAPILib["mzdSetLEDControl"]
    func.argtypes = [c_void_p, c_int, MZD_LED_CTRL]
    func.restype = c_uint32
    ret = func(pDev, ledPinId, ledCtrl)
    return ret


def mzdSetLEDTimer(pDev, ledTimerConfig):
    """
    :param pDev: argument type c_void_p
    :param ledTimerConfig: implementation of the structure class MZD_LED_TIMER_CONFIG
    """
    func = MZDAPILib["mzdSetLEDTimer"]
    func.argtypes = [c_void_p, MZD_LED_TIMER_CONFIG]
    func.restype = c_uint32
    ret = func(pDev, ledTimerConfig)
    return ret


def mzdConfigRClkPin(pDev, rClkPinId, portSelect, interfaceSelect, laneSelect):
    """
    :param pDev: argument type c_void_p
    :param rClkPinId: member from enumerate class MZD_PIN_ID
    :param portSelect: argument type c_uint16
    :param interfaceSelect: argument type c_uint16
    :param laneSelect: argument type c_uint16
    """
    func = MZDAPILib["mzdConfigRClkPin"]
    func.argtypes = [c_void_p, c_int, c_uint16, c_uint16, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, rClkPinId, portSelect, interfaceSelect, laneSelect)
    return ret


def mzdConfigRClkSource(pDev, portSelect, interfaceSelect, laneSelect, clockOption):
    """
    :param pDev: argument type c_void_p
    :param portSelect: argument type c_uint16
    :param interfaceSelect: argument type c_uint16
    :param laneSelect: argument type c_uint16
    :param clockOption: implementation of the structure class MZD_RCLK_SRC_OPTION
    """
    func = MZDAPILib["mzdConfigRClkSource"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, MZD_RCLK_SRC_OPTION]
    func.restype = c_uint32
    ret = func(pDev, portSelect, interfaceSelect, laneSelect, clockOption)
    return ret


def mzdMacSecMacInit(pDev, mdioPort, host_or_line, laneOffset, opMode, initOption):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param opMode: member from enumerate class MZD_OP_MODE
    :param initOption: argument type c_uint16
    """
    func = MZDAPILib["mzdMacSecMacInit"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_int, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, opMode, initOption)
    return ret


def mzdMacEnable(pDev, mdioPort, host_or_line, laneOffset, macEnable):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param macEnable: member from enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdMacEnable"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_int]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, macEnable)
    return ret


def mzdMacSecEnable(pDev, mdioPort, host_or_line, macsecEnable):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param macsecEnable: member from enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdMacSecEnable"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_int]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, macsecEnable)
    return ret


def mzdMacSetLowSpeed(pDev, mdioPort, laneOffset):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param laneOffset: argument type c_uint16
    """
    func = MZDAPILib["mzdMacSetLowSpeed"]
    func.argtypes = [c_void_p, c_uint16, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, laneOffset)
    return ret


def mzdMacSetHighSpeed(pDev, mdioPort):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    """
    func = MZDAPILib["mzdMacSetHighSpeed"]
    func.argtypes = [c_void_p, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort)
    return ret


def mzdMacSecPtpBypass(pDev, mdioPort, bypassPtp):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param bypassPtp: member from enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdMacSecPtpBypass"]
    func.argtypes = [c_void_p, c_uint16, c_int]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, bypassPtp)
    return ret


def mzdMacSecEgressBypass(pDev, mdioPort, laneOffset, egressBypass):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param egressBypass: member from enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdMacSecEgressBypass"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_int]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, laneOffset, egressBypass)
    return ret


def mzdMacSecIngressBypass(pDev, mdioPort, laneOffset, ingressBypass):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param ingressBypass: member from enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdMacSecIngressBypass"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_int]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, laneOffset, ingressBypass)
    return ret


def mzdMacBypassPPMFifo(pDev, mdioPort, bypassPPMFifo):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param bypassPPMFifo: member from enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdMacBypassPPMFifo"]
    func.argtypes = [c_void_p, c_uint16, c_int]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, bypassPPMFifo)
    return ret


def mzdMacBypassPPMFifoPushBackLatencyMatch(pDev, mdioPort, host_or_line, laneOffset, pushBackLatencyMatch):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param pushBackLatencyMatch: argument type c_uint16
    """
    func = MZDAPILib["mzdMacBypassPPMFifoPushBackLatencyMatch"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, pushBackLatencyMatch)
    return ret


def mzdMacBypassPPMFifoDelayAlignMarkerPushBack(pDev, mdioPort, host_or_line, laneOffset, pushBackDelay):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param pushBackDelay: argument type c_uint16
    """
    func = MZDAPILib["mzdMacBypassPPMFifoDelayAlignMarkerPushBack"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, pushBackDelay)
    return ret


def mzdMacMIBStatDump(pDev, mdioPort, host_or_line, laneOffset, stateDumpOptions):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param stateDumpOptions: argument type c_uint32
    """
    func = MZDAPILib["mzdMacMIBStatDump"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint32]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, stateDumpOptions)
    return ret


def mzdMacPauseFrameInjectionToHost(pDev, mdioPort, laneOffset, enable):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param enable: argument type c_uint16
    """
    func = MZDAPILib["mzdMacPauseFrameInjectionToHost"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, laneOffset, enable)
    return ret


def mzdMacSetPauseFrameToHostThreshold(pDev, mdioPort, laneOffset, lowThreshold, highThreshold):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param lowThreshold: argument type c_uint16
    :param highThreshold: argument type c_uint16
    """
    func = MZDAPILib["mzdMacSetPauseFrameToHostThreshold"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, laneOffset, lowThreshold, highThreshold)
    return ret


def mzdMacGetPauseFrameToHostThreshold(pDev, mdioPort, laneOffset, lowThreshold_p, highThreshold_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param lowThreshold_p: A pointer of c_uint16
    :param highThreshold_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdMacGetPauseFrameToHostThreshold"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, POINTER(c_uint16), POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, laneOffset, lowThreshold_p, highThreshold_p)
    return ret


def mzdMacSecHmux4ArbiterEnable(pDev, macsecMapPort, hostSideMode, lowerPortPrimary, hmux4Options):
    """
    :param pDev: argument type c_void_p
    :param macsecMapPort: argument type c_uint16
    :param hostSideMode: member from enumerate class MZD_OP_MODE
    :param lowerPortPrimary: member from enumerate class MZD_BOOL
    :param hmux4Options: argument type c_uint32
    """
    func = MZDAPILib["mzdMacSecHmux4ArbiterEnable"]
    func.argtypes = [c_void_p, c_uint16, c_int, c_int, c_uint32]
    func.restype = c_uint32
    ret = func(pDev, macsecMapPort, hostSideMode, lowerPortPrimary, hmux4Options)
    return ret


def mzdMacSecHmux8ArbiterEnable(pDev, hostSideMode, lowerPortsPrimary, hmux8Options):
    """
    :param pDev: argument type c_void_p
    :param hostSideMode: member from enumerate class MZD_OP_MODE
    :param lowerPortsPrimary: member from enumerate class MZD_BOOL
    :param hmux8Options: argument type c_uint32
    """
    func = MZDAPILib["mzdMacSecHmux8ArbiterEnable"]
    func.argtypes = [c_void_p, c_int, c_int, c_uint32]
    func.restype = c_uint32
    ret = func(pDev, hostSideMode, lowerPortsPrimary, hmux8Options)
    return ret


def mzdMacSecHmuxArbiterEnablePerLane(pDev, mdioPort, laneOffset, hostSideMode, hmuxType):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param hostSideMode: member from enumerate class MZD_OP_MODE
    :param hmuxType: argument type c_uint16
    """
    func = MZDAPILib["mzdMacSecHmuxArbiterEnablePerLane"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_int, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, laneOffset, hostSideMode, hmuxType)
    return ret


def mzdHmuxArbiterReset(pDev, mdioPort, laneOffset, arbiterSelect):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param arbiterSelect: argument type c_uint16
    """
    func = MZDAPILib["mzdHmuxArbiterReset"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, laneOffset, arbiterSelect)
    return ret


def mzdMacSecSelectHmuxType(pDev, macsecMapPort, hmuxType, lowerPortPrimary, hmuxOptions):
    """
    :param pDev: argument type c_void_p
    :param macsecMapPort: argument type c_uint16
    :param hmuxType: argument type c_uint16
    :param lowerPortPrimary: member from enumerate class MZD_BOOL
    :param hmuxOptions: argument type c_uint16
    """
    func = MZDAPILib["mzdMacSecSelectHmuxType"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_int, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, macsecMapPort, hmuxType, lowerPortPrimary, hmuxOptions)
    return ret


def mzdMacSecHmuxArbiterState(pDev, macsecMapPort, arbiterEgrState_p, arbiterIngrState_p):
    """
    :param pDev: argument type c_void_p
    :param macsecMapPort: argument type c_uint16
    :param arbiterEgrState_p: A pointer of c_uint16
    :param arbiterIngrState_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdMacSecHmuxArbiterState"]
    func.argtypes = [c_void_p, c_uint16, POINTER(c_uint16), POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, macsecMapPort, arbiterEgrState_p, arbiterIngrState_p)
    return ret


def mzdMacSecHmuxBlockBackUpIngress(pDev, macsecMapPort, blockBackUpPorts):
    """
    :param pDev: argument type c_void_p
    :param macsecMapPort: argument type c_uint16
    :param blockBackUpPorts: member from enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdMacSecHmuxBlockBackUpIngress"]
    func.argtypes = [c_void_p, c_uint16, c_int]
    func.restype = c_uint32
    ret = func(pDev, macsecMapPort, blockBackUpPorts)
    return ret


def mzdMacSecHmuxTimeOut(pDev, mdioPort, hmuxTimeOutSel, hmuxTimeOutSelOptions):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param hmuxTimeOutSel: argument type c_uint32
    :param hmuxTimeOutSelOptions: argument type c_uint32
    """
    func = MZDAPILib["mzdMacSecHmuxTimeOut"]
    func.argtypes = [c_void_p, c_uint16, c_uint32, c_uint32]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, hmuxTimeOutSel, hmuxTimeOutSelOptions)
    return ret


def mzdMacSecManualHmuxStopTraffic(pDev, macsecMapPort):
    """
    :param pDev: argument type c_void_p
    :param macsecMapPort: argument type c_uint16
    """
    func = MZDAPILib["mzdMacSecManualHmuxStopTraffic"]
    func.argtypes = [c_void_p, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, macsecMapPort)
    return ret


def mzdMacSecManualHmuxStartTraffic(pDev, macsecMapPort):
    """
    :param pDev: argument type c_void_p
    :param macsecMapPort: argument type c_uint16
    """
    func = MZDAPILib["mzdMacSecManualHmuxStartTraffic"]
    func.argtypes = [c_void_p, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, macsecMapPort)
    return ret


def mzdMacSecHmuxAutoSwitch(pDev, macsecMapPort):
    """
    :param pDev: argument type c_void_p
    :param macsecMapPort: argument type c_uint16
    """
    func = MZDAPILib["mzdMacSecHmuxAutoSwitch"]
    func.argtypes = [c_void_p, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, macsecMapPort)
    return ret


def mzdMacSecHmuxGPIOSwitchCntl(pDev, macsecMapPort, enable, edgeDetect):
    """
    :param pDev: argument type c_void_p
    :param macsecMapPort: argument type c_uint16
    :param enable: argument type c_uint16
    :param edgeDetect: argument type c_uint16
    """
    func = MZDAPILib["mzdMacSecHmuxGPIOSwitchCntl"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, macsecMapPort, enable, edgeDetect)
    return ret


def mzdMacSecHmuxLevelGPIOSwitchCntl(pDev, enable):
    """
    :param pDev: argument type c_void_p
    :param enable: argument type c_uint16
    """
    func = MZDAPILib["mzdMacSecHmuxLevelGPIOSwitchCntl"]
    func.argtypes = [c_void_p, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, enable)
    return ret


def mzdMacSecHmuxStatusOutputCntl(pDev, macsecMapPort, enable, polarity):
    """
    :param pDev: argument type c_void_p
    :param macsecMapPort: argument type c_uint16
    :param enable: argument type c_uint16
    :param polarity: argument type c_uint16
    """
    func = MZDAPILib["mzdMacSecHmuxStatusOutputCntl"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, macsecMapPort, enable, polarity)
    return ret


def mzdMacTxFifoReset(pDev, mdioPort, host_or_line, laneOffset):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    """
    func = MZDAPILib["mzdMacTxFifoReset"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset)
    return ret


def mzdMacInsertTxCRC(pDev, mdioPort, laneOffset, insertTxCRC):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param insertTxCRC: member from enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdMacInsertTxCRC"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_int]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, laneOffset, insertTxCRC)
    return ret


def mzdMacForwardRxCRC(pDev, mdioPort, laneOffset, forwardRxCRC):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param forwardRxCRC: member from enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdMacForwardRxCRC"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_int]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, laneOffset, forwardRxCRC)
    return ret


def mzdMacFlowControl(pDev, mdioPort, laneOffset, flowCntlOption, enableFlag):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param flowCntlOption: argument type c_uint16
    :param enableFlag: argument type c_uint16
    """
    func = MZDAPILib["mzdMacFlowControl"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, laneOffset, flowCntlOption, enableFlag)
    return ret


def mzdSetMacLaneInterruptEnable(pDev, mdioPort, host_or_line, laneOffset, intrEnable):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param intrEnable: argument type c_uint32
    """
    func = MZDAPILib["mzdSetMacLaneInterruptEnable"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint32]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, intrEnable)
    return ret


def mzdGetMacLaneInterruptEnable(pDev, mdioPort, host_or_line, laneOffset, intrEnable_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param intrEnable_p: A pointer of c_uint32
    """
    func = MZDAPILib["mzdGetMacLaneInterruptEnable"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_uint32)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, intrEnable_p)
    return ret


def mzdGetMacLaneInterruptStatus(pDev, mdioPort, host_or_line, laneOffset, intrStatus_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param intrStatus_p: A pointer of c_uint32
    """
    func = MZDAPILib["mzdGetMacLaneInterruptStatus"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_uint32)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, intrStatus_p)
    return ret


def mzdSetMacTodInterruptEnable(pDev, mdioPort, host_or_line, overrunIntrEnable, underrunIntrEnable):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param overrunIntrEnable: argument type c_uint32
    :param underrunIntrEnable: argument type c_uint32
    """
    func = MZDAPILib["mzdSetMacTodInterruptEnable"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint32, c_uint32]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, overrunIntrEnable, underrunIntrEnable)
    return ret


def mzdGetMacTodInterruptEnable(pDev, mdioPort, host_or_line, overrunIntrEnable_p, underrunIntrEnable_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param overrunIntrEnable_p: A pointer of c_uint32
    :param underrunIntrEnable_p: A pointer of c_uint32
    """
    func = MZDAPILib["mzdGetMacTodInterruptEnable"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, POINTER(c_uint32), POINTER(c_uint32)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, overrunIntrEnable_p, underrunIntrEnable_p)
    return ret


def mzdGetMacTodInterruptStatus(pDev, mdioPort, host_or_line, intrType, overrunIntrStatus_p, underrunIntrStatus_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param intrType: member from enumerate class MZD_MAC_TOD_INTR_TYPE
    :param overrunIntrStatus_p: A pointer of c_uint32
    :param underrunIntrStatus_p: A pointer of c_uint32
    """
    func = MZDAPILib["mzdGetMacTodInterruptStatus"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_int, POINTER(c_uint32), POINTER(c_uint32)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, intrType, overrunIntrStatus_p, underrunIntrStatus_p)
    return ret


def mzdSetMacGlobalInterruptEnable(pDev, mdioPort, host_or_line, intrEnable):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param intrEnable: argument type c_uint32
    """
    func = MZDAPILib["mzdSetMacGlobalInterruptEnable"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint32]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, intrEnable)
    return ret


def mzdGetMacGlobalInterruptEnable(pDev, mdioPort, host_or_line, intrEnable_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param intrEnable_p: A pointer of c_uint32
    """
    func = MZDAPILib["mzdGetMacGlobalInterruptEnable"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, POINTER(c_uint32)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, intrEnable_p)
    return ret


def mzdGetMacGlobalInterruptStatus(pDev, mdioPort, host_or_line, intrStatus_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param intrStatus_p: A pointer of c_uint32
    """
    func = MZDAPILib["mzdGetMacGlobalInterruptStatus"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, POINTER(c_uint32)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, intrStatus_p)
    return ret


def mzdMacSecHmuxConfigDump(pDev, mdioPort, dumpOptions):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param dumpOptions: argument type c_uint32
    """
    func = MZDAPILib["mzdMacSecHmuxConfigDump"]
    func.argtypes = [c_void_p, c_uint16, c_uint32]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, dumpOptions)
    return ret


def mzdSampleHMux4MacSecBypass(pDev, mdioPort, hostSideMode):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param hostSideMode: member from enumerate class MZD_OP_MODE
    """
    func = MZDAPILib["mzdSampleHMux4MacSecBypass"]
    func.argtypes = [c_void_p, c_uint16, c_int]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, hostSideMode)
    return ret


def mzdSampleHMux8MacSecBypassPerLane(pDev, hostSideMode, lowerPortsPrimary):
    """
    :param pDev: argument type c_void_p
    :param hostSideMode: member from enumerate class MZD_OP_MODE
    :param lowerPortsPrimary: member from enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdSampleHMux8MacSecBypassPerLane"]
    func.argtypes = [c_void_p, c_int, c_int]
    func.restype = c_uint32
    ret = func(pDev, hostSideMode, lowerPortsPrimary)
    return ret


def mzdSampleHMux8MacSecEnable(pDev, hostSideMode, lowerPortsPrimary):
    """
    :param pDev: argument type c_void_p
    :param hostSideMode: member from enumerate class MZD_OP_MODE
    :param lowerPortsPrimary: member from enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdSampleHMux8MacSecEnable"]
    func.argtypes = [c_void_p, c_int, c_int]
    func.restype = c_uint32
    ret = func(pDev, hostSideMode, lowerPortsPrimary)
    return ret


def mzdSampleHMux8DeMuxInitMacSecBypass(pDev, hostSideMode, lineSideMode, lowerPortsPrimary):
    """
    :param pDev: argument type c_void_p
    :param hostSideMode: member from enumerate class MZD_OP_MODE
    :param lineSideMode: member from enumerate class MZD_OP_MODE
    :param lowerPortsPrimary: member from enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdSampleHMux8DeMuxInitMacSecBypass"]
    func.argtypes = [c_void_p, c_int, c_int, c_int]
    func.restype = c_uint32
    ret = func(pDev, hostSideMode, lineSideMode, lowerPortsPrimary)
    return ret


def mzdSampleHMux8DeMux2MacSecBypass(pDev):
    """
    :param pDev: argument type c_void_p
    """
    func = MZDAPILib["mzdSampleHMux8DeMux2MacSecBypass"]
    func.argtypes = [c_void_p]
    func.restype = c_uint32
    ret = func(pDev)
    return ret


def mzdSampleHMux8DeMux2MixSpeed(pDev):
    """
    :param pDev: argument type c_void_p
    """
    func = MZDAPILib["mzdSampleHMux8DeMux2MixSpeed"]
    func.argtypes = [c_void_p]
    func.restype = c_uint32
    ret = func(pDev)
    return ret


def mzdSampleLoadImageFile(filename_p, imageSize_p, pFirmwareImage_p):
    """
    :param filename_p: A pointer of c_char
    :param imageSize_p: A pointer of c_uint32
    :param pFirmwareImage_p: A pointer of c_uint8
    """
    func = MZDAPILib["mzdSampleLoadImageFile"]
    func.argtypes = [POINTER(c_char), POINTER(c_uint32), POINTER(c_uint8)]
    func.restype = c_uint32
    ret = func(filename_p, imageSize_p, pFirmwareImage_p)
    return ret


def mzdSampleUnloadDrv(pDev):
    """
    :param pDev: argument type c_void_p
    """
    func = MZDAPILib["mzdSampleUnloadDrv"]
    func.argtypes = [c_void_p]
    func.restype = c_uint32
    ret = func(pDev)
    return ret


def mzdSampleInitDrv(pHostContext, mdioFirstPort, mzdFuncReadMdio_p, mzdFuncWriteMdio_p, mzdFuncWait_p, serdesRead_p, serdesWrite_p, mzdUseFlash, pDev):
    """
    :param pHostContext: argument type c_void_p
    :param mdioFirstPort: argument type c_uint16
    :param mzdFuncReadMdio: a function pointer
    :param mzdFuncWriteMdio: a function pointer
    :param mzdFuncWait: a function pointer
    :param serdesRead: a function pointer
    :param serdesWrite: a function pointer
    :param mzdUseFlash: member from enumerate class MZD_BOOL
    :param pDev: argument type c_void_p
    """
    func = MZDAPILib["mzdSampleInitDrv"]
    func.argtypes = [c_void_p, c_uint16, CFUNCTYPE(c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_uint16)), CFUNCTYPE(c_void_p, c_uint16, c_uint16, c_uint16, c_uint16), CFUNCTYPE(c_void_p, c_uint), CFUNCTYPE(c_void_p, c_uint32, POINTER(c_uint32)), CFUNCTYPE(c_void_p, c_uint32, c_uint32), c_int, c_void_p]
    func.restype = c_uint32
    ret = func(pHostContext, mdioFirstPort, mzdFuncReadMdio_p, mzdFuncWriteMdio_p, mzdFuncWait_p, serdesRead_p, serdesWrite_p, mzdUseFlash, pDev)
    return ret


def mzdSampleUpdateFlash(pDev):
    """
    :param pDev: argument type c_void_p
    """
    func = MZDAPILib["mzdSampleUpdateFlash"]
    func.argtypes = [c_void_p]
    func.restype = c_uint32
    ret = func(pDev)
    return ret


def mzdSampleEraseFlash(pDev):
    """
    :param pDev: argument type c_void_p
    """
    func = MZDAPILib["mzdSampleEraseFlash"]
    func.argtypes = [c_void_p]
    func.restype = c_uint32
    ret = func(pDev)
    return ret


def mzdSampleInitDrvParallelLoad(pHostContext, mdioFirstPort, mzdFuncReadMdio_p, mzdFuncWriteMdio_p, mzdFuncWait_p, serdesRead_p, serdesWrite_p, pDev0, pDev1):
    """
    :param pHostContext: argument type c_void_p
    :param mdioFirstPort: argument type c_uint16
    :param mzdFuncReadMdio: a function pointer
    :param mzdFuncWriteMdio: a function pointer
    :param mzdFuncWait: a function pointer
    :param serdesRead: a function pointer
    :param serdesWrite: a function pointer
    :param pDev0: argument type c_void_p
    :param pDev1: argument type c_void_p
    """
    func = MZDAPILib["mzdSampleInitDrvParallelLoad"]
    func.argtypes = [c_void_p, c_uint16, CFUNCTYPE(c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_uint16)), CFUNCTYPE(c_void_p, c_uint16, c_uint16, c_uint16, c_uint16), CFUNCTYPE(c_void_p, c_uint), CFUNCTYPE(c_void_p, c_uint32, POINTER(c_uint32)), CFUNCTYPE(c_void_p, c_uint32, c_uint32), c_void_p, c_void_p]
    func.restype = c_uint32
    ret = func(pHostContext, mdioFirstPort, mzdFuncReadMdio_p, mzdFuncWriteMdio_p, mzdFuncWait_p, serdesRead_p, serdesWrite_p, pDev0, pDev1)
    return ret


def mzdSampleParallelUpdateFlash(pDev0, pDev1):
    """
    :param pDev0: argument type c_void_p
    :param pDev1: argument type c_void_p
    """
    func = MZDAPILib["mzdSampleParallelUpdateFlash"]
    func.argtypes = [c_void_p, c_void_p]
    func.restype = c_uint32
    ret = func(pDev0, pDev1)
    return ret


def mzdSampleParallelEraseFlash(pDev0, pDev1):
    """
    :param pDev0: argument type c_void_p
    :param pDev1: argument type c_void_p
    """
    func = MZDAPILib["mzdSampleParallelEraseFlash"]
    func.argtypes = [c_void_p, c_void_p]
    func.restype = c_uint32
    ret = func(pDev0, pDev1)
    return ret


def mzdSampleReloadDriver(mdioPort, pHostContext, pDev):
    """
    :param mdioPort: argument type c_uint16
    :param pHostContext: argument type c_void_p
    :param pDev: argument type c_void_p
    """
    func = MZDAPILib["mzdSampleReloadDriver"]
    func.argtypes = [c_uint16, c_void_p, c_void_p]
    func.restype = c_uint32
    ret = func(mdioPort, pHostContext, pDev)
    return ret


def mzdSampleSetPCSMode(pDev, mdioPort, laneOffset, modeOptionSel, modeOption, hostMode, lineMode, pollLinkStatus):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param modeOptionSel: argument type c_uint32
    :param modeOption: implementation of the structure class MZD_MODE_OPTION_STRUCT
    :param hostMode: member from enumerate class MZD_OP_MODE
    :param lineMode: member from enumerate class MZD_OP_MODE
    :param pollLinkStatus: member from enumerate class MZD_BOOL
    """
    func = MZDAPILib["mzdSampleSetPCSMode"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint32, MZD_MODE_OPTION_STRUCT, c_int, c_int, c_int]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, laneOffset, modeOptionSel, modeOption, hostMode, lineMode, pollLinkStatus)
    return ret


def mzdSamplePRBSTest(pDev0, pDev1, mdioPort, laneOffset):
    """
    :param pDev0: argument type c_void_p
    :param pDev1: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param laneOffset: argument type c_uint16
    """
    func = MZDAPILib["mzdSamplePRBSTest"]
    func.argtypes = [c_void_p, c_void_p, c_uint16, c_uint16]
    func.restype = c_uint32
    ret = func(pDev0, pDev1, mdioPort, laneOffset)
    return ret


def mzdSampleLoopbackPacketGen(pDev0, pDev1, mdioPort0, mdioPort1, laneOffset):
    """
    :param pDev0: argument type c_void_p
    :param pDev1: argument type c_void_p
    :param mdioPort0: argument type c_uint16
    :param mdioPort1: argument type c_uint16
    :param laneOffset: argument type c_uint16
    """
    func = MZDAPILib["mzdSampleLoopbackPacketGen"]
    func.argtypes = [c_void_p, c_void_p, c_uint16, c_uint16, c_uint16]
    func.restype = c_uint32
    ret = func(pDev0, pDev1, mdioPort0, mdioPort1, laneOffset)
    return ret


def mzdSampleGetEyeWidthHeight(pDev, mdioPort, host_or_line, laneOffset, eyeTMB, eyeWidth_p, eyeHeight_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param eyeTMB: member from enumerate class E_N5C112GX4_EYE_TMB
    :param eyeWidth_p: A pointer of c_uint16
    :param eyeHeight_p: A pointer of c_uint16
    """
    func = MZDAPILib["mzdSampleGetEyeWidthHeight"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_int, POINTER(c_uint16), POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, eyeTMB, eyeWidth_p, eyeHeight_p)
    return ret


def mzdSampleGetEye(pDev, mdioPort, host_or_line, laneOffset, voltageSteps, phaseLevels):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param voltageSteps: argument type c_uint16
    :param phaseLevels: argument type c_uint16
    """
    func = MZDAPILib["mzdSampleGetEye"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_uint16, c_uint16]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, voltageSteps, phaseLevels)
    return ret


def mzdSampleGetTemperature(pDev, mdioPort, temperature_p):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param temperature_p: A pointer of c_int32
    """
    func = MZDAPILib["mzdSampleGetTemperature"]
    func.argtypes = [c_void_p, c_uint16, POINTER(c_int32)]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, temperature_p)
    return ret


def mzdSampleSetCTLE(pDev, mdioPort, host_or_line, laneOffset, ctleParamType, paramValue):
    """
    :param pDev: argument type c_void_p
    :param mdioPort: argument type c_uint16
    :param host_or_line: argument type c_uint16
    :param laneOffset: argument type c_uint16
    :param ctleParamType: member from enumerate class E_N5C112GX4_CTLE_PARAM
    :param paramValue: argument type c_uint32
    """
    func = MZDAPILib["mzdSampleSetCTLE"]
    func.argtypes = [c_void_p, c_uint16, c_uint16, c_uint16, c_int, c_uint32]
    func.restype = c_uint32
    ret = func(pDev, mdioPort, host_or_line, laneOffset, ctleParamType, paramValue)
    return ret


def mzdSampleSerdesMux(pDev0, pDev1, host_or_line):
    """
    :param pDev0: argument type c_void_p
    :param pDev1: argument type c_void_p
    :param host_or_line: argument type c_uint16
    """
    func = MZDAPILib["mzdSampleSerdesMux"]
    func.argtypes = [c_void_p, c_void_p, c_uint16]
    func.restype = c_uint32
    ret = func(pDev0, pDev1, host_or_line)
    return ret


