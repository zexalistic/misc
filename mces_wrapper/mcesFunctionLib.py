from ctypes import *

class S_N5C112GX4_PATTERN_STATISTICS(Structure):
    _fields_ = [("lock", c_int),
                ("pass", c_int),
                ("totalBits", c_uint64),
                ("totalErrorBits", c_uint64),
               ]

class S_N5C112GX4_EOM_DATA(Structure):
    _fields_ = [("phase", c_int32),
                ("voltage", c_uint8),
                ("upperBitCount", c_uint64),
                ("upperBitErrorCount", c_uint32),
                ("lowerBitCount", c_uint64),
                ("lowerBitErrorCount", c_uint32),
               ]

class S_N5C112GX4_TRAINING_TIMEOUT(Structure):
    _fields_ = [("enable", c_int),
                ("timeout", c_uint16),
               ]

class MCESD_FIELD(Structure):
    _fields_ = [("reg", c_uint32),
                ("hiBit", c_int16),
                ("loBit", c_int16),
                ("totalBits", c_int16),
                ("mask", c_uint32),
                ("retainMask", c_uint32),
               ]

class _MCESD_DEV(Structure):
    _fields_ = [("ipMajorRev", c_uint8),
                ("ipMinorRev", c_uint8),
                ("devEnabled", c_int),
                ("fmcesdReadReg", CFUNCTYPE(c_void_p, c_uint32, POINTER(c_uint32))),
                ("fmcesdWriteReg", CFUNCTYPE(c_void_p, c_uint32, c_uint32)),
                ("fmcesdSetPinCfg", CFUNCTYPE(c_void_p, c_uint16, c_uint16)),
                ("fmcesdGetPinCfg", CFUNCTYPE(c_void_p, c_uint16, POINTER(c_uint16))),
                ("fmcesdWaitFunc", CFUNCTYPE(c_void_p, c_uint32)),
                ("appData", c_void_p),
               ]

class S_N5C112GX4_PowerOn(Structure):
    _fields_ = [
        ('unions', c_void_p),
        ('initTx', c_int),
        ('initRx', c_int),
        ('txOutputEn', c_int),
        ('downloadFw', c_int),
        ('dataPath', c_int),
        ('refClkSel', c_int),
        ('dataBusWidth', c_int),
        ('speed', c_int),
        ('refFreq', c_int),
        ('avdd', c_int),
        ('spdCfg', c_int),
        ('fwDownload', c_void_p)
    ]


MZDAPILib = CDLL("..\Debug\MZD.dll")

def API_N5C112GX4_GetFirmwareRev(devPtr, major_p, minor_p, patch_p, build_p):
    """
    :param devPtr: argument type c_void_p
    :param major: A pointer of c_uint8
    :param minor: A pointer of c_uint8
    :param patch: A pointer of c_uint8
    :param build: A pointer of c_uint8
    """
    func = MZDAPILib["API_N5C112GX4_GetFirmwareRev"]
    func.argtypes = [c_void_p, POINTER(c_uint8), POINTER(c_uint8), POINTER(c_uint8), POINTER(c_uint8)]
    func.restype = c_uint32
    ret = func(devPtr, major_p, minor_p, patch_p, build_p)
    return ret


def API_N5C112GX4_GetPLLLock(devPtr, lane, tsLocked_p, rsLocked_p):
    """
    :param devPtr: argument type c_void_p
    :param lane: argument type c_uint8
    :param tsLocked: A pointer of the enumerate class MCESD_BOOL
    :param rsLocked: A pointer of the enumerate class MCESD_BOOL
    """
    func = MZDAPILib["API_N5C112GX4_GetPLLLock"]
    func.argtypes = [c_void_p, c_uint8, POINTER(c_int), POINTER(c_int)]
    func.restype = c_uint32
    ret = func(devPtr, lane, tsLocked_p, rsLocked_p)
    return ret


def API_N5C112GX4_GetTxRxReady(devPtr, lane, txReady_p, rxReady_p):
    """
    :param devPtr: argument type c_void_p
    :param lane: argument type c_uint8
    :param txReady: A pointer of the enumerate class MCESD_BOOL
    :param rxReady: A pointer of the enumerate class MCESD_BOOL
    """
    func = MZDAPILib["API_N5C112GX4_GetTxRxReady"]
    func.argtypes = [c_void_p, c_uint8, POINTER(c_int), POINTER(c_int)]
    func.restype = c_uint32
    ret = func(devPtr, lane, txReady_p, rxReady_p)
    return ret


def API_N5C112GX4_GetCDRLock(devPtr, lane, cdrLocked_p):
    """
    :param devPtr: argument type c_void_p
    :param lane: argument type c_uint8
    :param cdrLocked: A pointer of the enumerate class MCESD_BOOL
    """
    func = MZDAPILib["API_N5C112GX4_GetCDRLock"]
    func.argtypes = [c_void_p, c_uint8, POINTER(c_int)]
    func.restype = c_uint32
    ret = func(devPtr, lane, cdrLocked_p)
    return ret


def API_N5C112GX4_RxInit(devPtr, lane):
    """
    :param devPtr: argument type c_void_p
    :param lane: argument type c_uint8
    """
    func = MZDAPILib["API_N5C112GX4_RxInit"]
    func.argtypes = [c_void_p, c_uint8]
    func.restype = c_uint32
    ret = func(devPtr, lane)
    return ret


def API_N5C112GX4_SetTxEqParam(devPtr, lane, param, paramValue):
    """
    :param devPtr: argument type c_void_p
    :param lane: argument type c_uint8
    :param param: member from enumerate class E_N5C112GX4_TXEQ_PARAM
    :param paramValue: argument type c_uint32
    """
    func = MZDAPILib["API_N5C112GX4_SetTxEqParam"]
    func.argtypes = [c_void_p, c_uint8, c_int, c_uint32]
    func.restype = c_uint32
    ret = func(devPtr, lane, param, paramValue)
    return ret


def API_N5C112GX4_GetTxEqParam(devPtr, lane, param, paramValue_p):
    """
    :param devPtr: argument type c_void_p
    :param lane: argument type c_uint8
    :param param: member from enumerate class E_N5C112GX4_TXEQ_PARAM
    :param paramValue: A pointer of c_uint32
    """
    func = MZDAPILib["API_N5C112GX4_GetTxEqParam"]
    func.argtypes = [c_void_p, c_uint8, c_int, POINTER(c_uint32)]
    func.restype = c_uint32
    ret = func(devPtr, lane, param, paramValue_p)
    return ret


def API_N5C112GX4_SetCTLEParam(devPtr, lane, param, paramValue):
    """
    :param devPtr: argument type c_void_p
    :param lane: argument type c_uint8
    :param param: member from enumerate class E_N5C112GX4_CTLE_PARAM
    :param paramValue: argument type c_uint32
    """
    func = MZDAPILib["API_N5C112GX4_SetCTLEParam"]
    func.argtypes = [c_void_p, c_uint8, c_int, c_uint32]
    func.restype = c_uint32
    ret = func(devPtr, lane, param, paramValue)
    return ret


def API_N5C112GX4_GetCTLEParam(devPtr, lane, param, paramValue_p):
    """
    :param devPtr: argument type c_void_p
    :param lane: argument type c_uint8
    :param param: member from enumerate class E_N5C112GX4_CTLE_PARAM
    :param paramValue: A pointer of c_uint32
    """
    func = MZDAPILib["API_N5C112GX4_GetCTLEParam"]
    func.argtypes = [c_void_p, c_uint8, c_int, POINTER(c_uint32)]
    func.restype = c_uint32
    ret = func(devPtr, lane, param, paramValue_p)
    return ret


def API_N5C112GX4_GetFfeTap(devPtr, lane, path, tap, tapValue_p):
    """
    :param devPtr: argument type c_void_p
    :param lane: argument type c_uint8
    :param path: member from enumerate class E_N5C112GX4_FFE_PATH
    :param tap: member from enumerate class E_N5C112GX4_FFE_TAP
    :param tapValue: A pointer of c_int32
    """
    func = MZDAPILib["API_N5C112GX4_GetFfeTap"]
    func.argtypes = [c_void_p, c_uint8, c_int, c_int, POINTER(c_int32)]
    func.restype = c_uint32
    ret = func(devPtr, lane, path, tap, tapValue_p)
    return ret


def API_N5C112GX4_SetMcuBroadcast(devPtr, state):
    """
    :param devPtr: argument type c_void_p
    :param state: member from enumerate class MCESD_BOOL
    """
    func = MZDAPILib["API_N5C112GX4_SetMcuBroadcast"]
    func.argtypes = [c_void_p, c_int]
    func.restype = c_uint32
    ret = func(devPtr, state)
    return ret


def API_N5C112GX4_GetMcuBroadcast(devPtr, state_p):
    """
    :param devPtr: argument type c_void_p
    :param state: A pointer of the enumerate class MCESD_BOOL
    """
    func = MZDAPILib["API_N5C112GX4_GetMcuBroadcast"]
    func.argtypes = [c_void_p, POINTER(c_int)]
    func.restype = c_uint32
    ret = func(devPtr, state_p)
    return ret


def API_N5C112GX4_SetPowerPLL(devPtr, lane, state):
    """
    :param devPtr: argument type c_void_p
    :param lane: argument type c_uint8
    :param state: member from enumerate class MCESD_BOOL
    """
    func = MZDAPILib["API_N5C112GX4_SetPowerPLL"]
    func.argtypes = [c_void_p, c_uint8, c_int]
    func.restype = c_uint32
    ret = func(devPtr, lane, state)
    return ret


def API_N5C112GX4_GetPowerPLL(devPtr, lane, state_p):
    """
    :param devPtr: argument type c_void_p
    :param lane: argument type c_uint8
    :param state: A pointer of the enumerate class MCESD_BOOL
    """
    func = MZDAPILib["API_N5C112GX4_GetPowerPLL"]
    func.argtypes = [c_void_p, c_uint8, POINTER(c_int)]
    func.restype = c_uint32
    ret = func(devPtr, lane, state_p)
    return ret


def API_N5C112GX4_SetPowerTx(devPtr, lane, state):
    """
    :param devPtr: argument type c_void_p
    :param lane: argument type c_uint8
    :param state: member from enumerate class MCESD_BOOL
    """
    func = MZDAPILib["API_N5C112GX4_SetPowerTx"]
    func.argtypes = [c_void_p, c_uint8, c_int]
    func.restype = c_uint32
    ret = func(devPtr, lane, state)
    return ret


def API_N5C112GX4_GetPowerTx(devPtr, lane, state_p):
    """
    :param devPtr: argument type c_void_p
    :param lane: argument type c_uint8
    :param state: A pointer of the enumerate class MCESD_BOOL
    """
    func = MZDAPILib["API_N5C112GX4_GetPowerTx"]
    func.argtypes = [c_void_p, c_uint8, POINTER(c_int)]
    func.restype = c_uint32
    ret = func(devPtr, lane, state_p)
    return ret


def API_N5C112GX4_SetPowerRx(devPtr, lane, state):
    """
    :param devPtr: argument type c_void_p
    :param lane: argument type c_uint8
    :param state: member from enumerate class MCESD_BOOL
    """
    func = MZDAPILib["API_N5C112GX4_SetPowerRx"]
    func.argtypes = [c_void_p, c_uint8, c_int]
    func.restype = c_uint32
    ret = func(devPtr, lane, state)
    return ret


def API_N5C112GX4_GetPowerRx(devPtr, lane, state_p):
    """
    :param devPtr: argument type c_void_p
    :param lane: argument type c_uint8
    :param state: A pointer of the enumerate class MCESD_BOOL
    """
    func = MZDAPILib["API_N5C112GX4_GetPowerRx"]
    func.argtypes = [c_void_p, c_uint8, POINTER(c_int)]
    func.restype = c_uint32
    ret = func(devPtr, lane, state_p)
    return ret


def API_N5C112GX4_SetPhyMode(devPtr, mode):
    """
    :param devPtr: argument type c_void_p
    :param mode: member from enumerate class E_N5C112GX4_PHYMODE
    """
    func = MZDAPILib["API_N5C112GX4_SetPhyMode"]
    func.argtypes = [c_void_p, c_int]
    func.restype = c_uint32
    ret = func(devPtr, mode)
    return ret


def API_N5C112GX4_GetPhyMode(devPtr, mode_p):
    """
    :param devPtr: argument type c_void_p
    :param mode: A pointer of the enumerate class E_N5C112GX4_PHYMODE
    """
    func = MZDAPILib["API_N5C112GX4_GetPhyMode"]
    func.argtypes = [c_void_p, POINTER(c_int)]
    func.restype = c_uint32
    ret = func(devPtr, mode_p)
    return ret


def API_N5C112GX4_SetRefFreq(devPtr, lane, freq, clkSel):
    """
    :param devPtr: argument type c_void_p
    :param lane: argument type c_uint8
    :param freq: member from enumerate class E_N5C112GX4_REFFREQ
    :param clkSel: member from enumerate class E_N5C112GX4_REFCLK_SEL
    """
    func = MZDAPILib["API_N5C112GX4_SetRefFreq"]
    func.argtypes = [c_void_p, c_uint8, c_int, c_int]
    func.restype = c_uint32
    ret = func(devPtr, lane, freq, clkSel)
    return ret


def API_N5C112GX4_GetRefFreq(devPtr, lane, refFreq_p, refClkSel_p):
    """
    :param devPtr: argument type c_void_p
    :param lane: argument type c_uint8
    :param refFreq: A pointer of the enumerate class E_N5C112GX4_REFFREQ
    :param refClkSel: A pointer of the enumerate class E_N5C112GX4_REFCLK_SEL
    """
    func = MZDAPILib["API_N5C112GX4_GetRefFreq"]
    func.argtypes = [c_void_p, c_uint8, POINTER(c_int), POINTER(c_int)]
    func.restype = c_uint32
    ret = func(devPtr, lane, refFreq_p, refClkSel_p)
    return ret


def API_N5C112GX4_SetTxRxBitRate(devPtr, lane, speed):
    """
    :param devPtr: argument type c_void_p
    :param lane: argument type c_uint8
    :param speed: member from enumerate class E_N5C112GX4_SERDES_SPEED
    """
    func = MZDAPILib["API_N5C112GX4_SetTxRxBitRate"]
    func.argtypes = [c_void_p, c_uint8, c_int]
    func.restype = c_uint32
    ret = func(devPtr, lane, speed)
    return ret


def API_N5C112GX4_GetTxRxBitRate(devPtr, lane, speed_p):
    """
    :param devPtr: argument type c_void_p
    :param lane: argument type c_uint8
    :param speed: A pointer of the enumerate class E_N5C112GX4_SERDES_SPEED
    """
    func = MZDAPILib["API_N5C112GX4_GetTxRxBitRate"]
    func.argtypes = [c_void_p, c_uint8, POINTER(c_int)]
    func.restype = c_uint32
    ret = func(devPtr, lane, speed_p)
    return ret


def API_N5C112GX4_SetDataBusWidth(devPtr, lane, txWidth, rxWidth):
    """
    :param devPtr: argument type c_void_p
    :param lane: argument type c_uint8
    :param txWidth: member from enumerate class E_N5C112GX4_DATABUS_WIDTH
    :param rxWidth: member from enumerate class E_N5C112GX4_DATABUS_WIDTH
    """
    func = MZDAPILib["API_N5C112GX4_SetDataBusWidth"]
    func.argtypes = [c_void_p, c_uint8, c_int, c_int]
    func.restype = c_uint32
    ret = func(devPtr, lane, txWidth, rxWidth)
    return ret


def API_N5C112GX4_GetDataBusWidth(devPtr, lane, txWidth_p, rxWidth_p):
    """
    :param devPtr: argument type c_void_p
    :param lane: argument type c_uint8
    :param txWidth: A pointer of the enumerate class E_N5C112GX4_DATABUS_WIDTH
    :param rxWidth: A pointer of the enumerate class E_N5C112GX4_DATABUS_WIDTH
    """
    func = MZDAPILib["API_N5C112GX4_GetDataBusWidth"]
    func.argtypes = [c_void_p, c_uint8, POINTER(c_int), POINTER(c_int)]
    func.restype = c_uint32
    ret = func(devPtr, lane, txWidth_p, rxWidth_p)
    return ret


def API_N5C112GX4_SetMcuClockFreq(devPtr, clockMHz):
    """
    :param devPtr: argument type c_void_p
    :param clockMHz: argument type c_uint16
    """
    func = MZDAPILib["API_N5C112GX4_SetMcuClockFreq"]
    func.argtypes = [c_void_p, c_uint16]
    func.restype = c_uint32
    ret = func(devPtr, clockMHz)
    return ret


def API_N5C112GX4_GetMcuClockFreq(devPtr, clockMHz_p):
    """
    :param devPtr: argument type c_void_p
    :param clockMHz: A pointer of c_uint16
    """
    func = MZDAPILib["API_N5C112GX4_GetMcuClockFreq"]
    func.argtypes = [c_void_p, POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(devPtr, clockMHz_p)
    return ret


def API_N5C112GX4_SetTxOutputEnable(devPtr, lane, state):
    """
    :param devPtr: argument type c_void_p
    :param lane: argument type c_uint8
    :param state: member from enumerate class MCESD_BOOL
    """
    func = MZDAPILib["API_N5C112GX4_SetTxOutputEnable"]
    func.argtypes = [c_void_p, c_uint8, c_int]
    func.restype = c_uint32
    ret = func(devPtr, lane, state)
    return ret


def API_N5C112GX4_GetTxOutputEnable(devPtr, lane, state_p):
    """
    :param devPtr: argument type c_void_p
    :param lane: argument type c_uint8
    :param state: A pointer of the enumerate class MCESD_BOOL
    """
    func = MZDAPILib["API_N5C112GX4_GetTxOutputEnable"]
    func.argtypes = [c_void_p, c_uint8, POINTER(c_int)]
    func.restype = c_uint32
    ret = func(devPtr, lane, state_p)
    return ret


def API_N5C112GX4_SetPowerIvRef(devPtr, state):
    """
    :param devPtr: argument type c_void_p
    :param state: member from enumerate class MCESD_BOOL
    """
    func = MZDAPILib["API_N5C112GX4_SetPowerIvRef"]
    func.argtypes = [c_void_p, c_int]
    func.restype = c_uint32
    ret = func(devPtr, state)
    return ret


def API_N5C112GX4_GetPowerIvRef(devPtr, state_p):
    """
    :param devPtr: argument type c_void_p
    :param state: A pointer of the enumerate class MCESD_BOOL
    """
    func = MZDAPILib["API_N5C112GX4_GetPowerIvRef"]
    func.argtypes = [c_void_p, POINTER(c_int)]
    func.restype = c_uint32
    ret = func(devPtr, state_p)
    return ret


def API_N5C112GX4_SetCDRParam(devPtr, lane, param, paramValue):
    """
    :param devPtr: argument type c_void_p
    :param lane: argument type c_uint8
    :param param: member from enumerate class E_N5C112GX4_CDR_PARAM
    :param paramValue: argument type c_uint32
    """
    func = MZDAPILib["API_N5C112GX4_SetCDRParam"]
    func.argtypes = [c_void_p, c_uint8, c_int, c_uint32]
    func.restype = c_uint32
    ret = func(devPtr, lane, param, paramValue)
    return ret


def API_N5C112GX4_GetCDRParam(devPtr, lane, param, paramValue_p):
    """
    :param devPtr: argument type c_void_p
    :param lane: argument type c_uint8
    :param param: member from enumerate class E_N5C112GX4_CDR_PARAM
    :param paramValue: A pointer of c_uint32
    """
    func = MZDAPILib["API_N5C112GX4_GetCDRParam"]
    func.argtypes = [c_void_p, c_uint8, c_int, POINTER(c_uint32)]
    func.restype = c_uint32
    ret = func(devPtr, lane, param, paramValue_p)
    return ret


def API_N5C112GX4_SetTrainingTimeout(devPtr, lane, type, training_p):
    """
    :param devPtr: argument type c_void_p
    :param lane: argument type c_uint8
    :param type: member from enumerate class E_N5C112GX4_TRAINING
    :param training: A pointer of the structure class S_N5C112GX4_TRAINING_TIMEOUT
    """
    func = MZDAPILib["API_N5C112GX4_SetTrainingTimeout"]
    func.argtypes = [c_void_p, c_uint8, c_int, POINTER(S_N5C112GX4_TRAINING_TIMEOUT)]
    func.restype = c_uint32
    ret = func(devPtr, lane, type, training_p)
    return ret


def API_N5C112GX4_GetTrainingTimeout(devPtr, lane, type, training_p):
    """
    :param devPtr: argument type c_void_p
    :param lane: argument type c_uint8
    :param type: member from enumerate class E_N5C112GX4_TRAINING
    :param training: A pointer of the structure class S_N5C112GX4_TRAINING_TIMEOUT
    """
    func = MZDAPILib["API_N5C112GX4_GetTrainingTimeout"]
    func.argtypes = [c_void_p, c_uint8, c_int, POINTER(S_N5C112GX4_TRAINING_TIMEOUT)]
    func.restype = c_uint32
    ret = func(devPtr, lane, type, training_p)
    return ret


def API_N5C112GX4_GetSquelchDetect(devPtr, lane, squelched_p):
    """
    :param devPtr: argument type c_void_p
    :param lane: argument type c_uint8
    :param squelched: A pointer of the enumerate class MCESD_BOOL
    """
    func = MZDAPILib["API_N5C112GX4_GetSquelchDetect"]
    func.argtypes = [c_void_p, c_uint8, POINTER(c_int)]
    func.restype = c_uint32
    ret = func(devPtr, lane, squelched_p)
    return ret


def API_N5C112GX4_SetSquelchThreshold(devPtr, lane, threshold):
    """
    :param devPtr: argument type c_void_p
    :param lane: argument type c_uint8
    :param threshold: argument type c_uint8
    """
    func = MZDAPILib["API_N5C112GX4_SetSquelchThreshold"]
    func.argtypes = [c_void_p, c_uint8, c_uint8]
    func.restype = c_uint32
    ret = func(devPtr, lane, threshold)
    return ret


def API_N5C112GX4_GetSquelchThreshold(devPtr, lane, threshold_p):
    """
    :param devPtr: argument type c_void_p
    :param lane: argument type c_uint8
    :param threshold: A pointer of c_uint8
    """
    func = MZDAPILib["API_N5C112GX4_GetSquelchThreshold"]
    func.argtypes = [c_void_p, c_uint8, POINTER(c_uint8)]
    func.restype = c_uint32
    ret = func(devPtr, lane, threshold_p)
    return ret


def API_N5C112GX4_SetDataPath(devPtr, lane, path):
    """
    :param devPtr: argument type c_void_p
    :param lane: argument type c_uint8
    :param path: member from enumerate class E_N5C112GX4_DATAPATH
    """
    func = MZDAPILib["API_N5C112GX4_SetDataPath"]
    func.argtypes = [c_void_p, c_uint8, c_int]
    func.restype = c_uint32
    ret = func(devPtr, lane, path)
    return ret


def API_N5C112GX4_GetDataPath(devPtr, lane, path_p):
    """
    :param devPtr: argument type c_void_p
    :param lane: argument type c_uint8
    :param path: A pointer of the enumerate class E_N5C112GX4_DATAPATH
    """
    func = MZDAPILib["API_N5C112GX4_GetDataPath"]
    func.argtypes = [c_void_p, c_uint8, POINTER(c_int)]
    func.restype = c_uint32
    ret = func(devPtr, lane, path_p)
    return ret


def API_N5C112GX4_GetTemperature(devPtr, temperature_p):
    """
    :param devPtr: argument type c_void_p
    :param temperature: A pointer of c_int32
    """
    func = MZDAPILib["API_N5C112GX4_GetTemperature"]
    func.argtypes = [c_void_p, POINTER(c_int32)]
    func.restype = c_uint32
    ret = func(devPtr, temperature_p)
    return ret


def API_N5C112GX4_SetTxRxPolarity(devPtr, lane, txPolarity, rxPolarity):
    """
    :param devPtr: argument type c_void_p
    :param lane: argument type c_uint8
    :param txPolarity: member from enumerate class E_N5C112GX4_POLARITY
    :param rxPolarity: member from enumerate class E_N5C112GX4_POLARITY
    """
    func = MZDAPILib["API_N5C112GX4_SetTxRxPolarity"]
    func.argtypes = [c_void_p, c_uint8, c_int, c_int]
    func.restype = c_uint32
    ret = func(devPtr, lane, txPolarity, rxPolarity)
    return ret


def API_N5C112GX4_GetTxRxPolarity(devPtr, lane, txPolarity_p, rxPolarity_p):
    """
    :param devPtr: argument type c_void_p
    :param lane: argument type c_uint8
    :param txPolarity: A pointer of the enumerate class E_N5C112GX4_POLARITY
    :param rxPolarity: A pointer of the enumerate class E_N5C112GX4_POLARITY
    """
    func = MZDAPILib["API_N5C112GX4_GetTxRxPolarity"]
    func.argtypes = [c_void_p, c_uint8, POINTER(c_int), POINTER(c_int)]
    func.restype = c_uint32
    ret = func(devPtr, lane, txPolarity_p, rxPolarity_p)
    return ret


def API_N5C112GX4_TxInjectError(devPtr, lane, errors):
    """
    :param devPtr: argument type c_void_p
    :param lane: argument type c_uint8
    :param errors: argument type c_uint8
    """
    func = MZDAPILib["API_N5C112GX4_TxInjectError"]
    func.argtypes = [c_void_p, c_uint8, c_uint8]
    func.restype = c_uint32
    ret = func(devPtr, lane, errors)
    return ret


def API_N5C112GX4_SetTxRxPattern(devPtr, lane, txPattern, rxPattern, txUserPattern_p, rxUserPattern_p):
    """
    :param devPtr: argument type c_void_p
    :param lane: argument type c_uint8
    :param txPattern: member from enumerate class E_N5C112GX4_PATTERN
    :param rxPattern: member from enumerate class E_N5C112GX4_PATTERN
    :param txUserPattern: A pointer of c_char
    :param rxUserPattern: A pointer of c_char
    """
    func = MZDAPILib["API_N5C112GX4_SetTxRxPattern"]
    func.argtypes = [c_void_p, c_uint8, c_int, c_int, POINTER(c_char), POINTER(c_char)]
    func.restype = c_uint32
    ret = func(devPtr, lane, txPattern, rxPattern, txUserPattern_p, rxUserPattern_p)
    return ret


def API_N5C112GX4_GetTxRxPattern(devPtr, lane, txPattern_p, rxPattern_p, txUserPattern_p, rxUserPattern_p):
    """
    :param devPtr: argument type c_void_p
    :param lane: argument type c_uint8
    :param txPattern: A pointer of the enumerate class E_N5C112GX4_PATTERN
    :param rxPattern: A pointer of the enumerate class E_N5C112GX4_PATTERN
    :param txUserPattern: A pointer of c_char
    :param rxUserPattern: A pointer of c_char
    """
    func = MZDAPILib["API_N5C112GX4_GetTxRxPattern"]
    func.argtypes = [c_void_p, c_uint8, POINTER(c_int), POINTER(c_int), POINTER(c_char), POINTER(c_char)]
    func.restype = c_uint32
    ret = func(devPtr, lane, txPattern_p, rxPattern_p, txUserPattern_p, rxUserPattern_p)
    return ret


def API_N5C112GX4_SetMSBLSBSwap(devPtr, lane, txSwapMsbLsb, rxSwapMsbLsb):
    """
    :param devPtr: argument type c_void_p
    :param lane: argument type c_uint8
    :param txSwapMsbLsb: member from enumerate class E_N5C112GX4_SWAP_MSB_LSB
    :param rxSwapMsbLsb: member from enumerate class E_N5C112GX4_SWAP_MSB_LSB
    """
    func = MZDAPILib["API_N5C112GX4_SetMSBLSBSwap"]
    func.argtypes = [c_void_p, c_uint8, c_int, c_int]
    func.restype = c_uint32
    ret = func(devPtr, lane, txSwapMsbLsb, rxSwapMsbLsb)
    return ret


def API_N5C112GX4_GetMSBLSBSwap(devPtr, lane, txSwapMsbLsb_p, rxSwapMsbLsb_p):
    """
    :param devPtr: argument type c_void_p
    :param lane: argument type c_uint8
    :param txSwapMsbLsb: A pointer of the enumerate class E_N5C112GX4_SWAP_MSB_LSB
    :param rxSwapMsbLsb: A pointer of the enumerate class E_N5C112GX4_SWAP_MSB_LSB
    """
    func = MZDAPILib["API_N5C112GX4_GetMSBLSBSwap"]
    func.argtypes = [c_void_p, c_uint8, POINTER(c_int), POINTER(c_int)]
    func.restype = c_uint32
    ret = func(devPtr, lane, txSwapMsbLsb_p, rxSwapMsbLsb_p)
    return ret


def API_N5C112GX4_SetGrayCode(devPtr, lane, txGrayCode, rxGrayCode):
    """
    :param devPtr: argument type c_void_p
    :param lane: argument type c_uint8
    :param txGrayCode: member from enumerate class E_N5C112GX4_GRAY_CODE
    :param rxGrayCode: member from enumerate class E_N5C112GX4_GRAY_CODE
    """
    func = MZDAPILib["API_N5C112GX4_SetGrayCode"]
    func.argtypes = [c_void_p, c_uint8, c_int, c_int]
    func.restype = c_uint32
    ret = func(devPtr, lane, txGrayCode, rxGrayCode)
    return ret


def API_N5C112GX4_GetGrayCode(devPtr, lane, txGrayCode_p, rxGrayCode_p):
    """
    :param devPtr: argument type c_void_p
    :param lane: argument type c_uint8
    :param txGrayCode: A pointer of the enumerate class E_N5C112GX4_GRAY_CODE
    :param rxGrayCode: A pointer of the enumerate class E_N5C112GX4_GRAY_CODE
    """
    func = MZDAPILib["API_N5C112GX4_GetGrayCode"]
    func.argtypes = [c_void_p, c_uint8, POINTER(c_int), POINTER(c_int)]
    func.restype = c_uint32
    ret = func(devPtr, lane, txGrayCode_p, rxGrayCode_p)
    return ret


def API_N5C112GX4_GetDataAcquisitionRate(devPtr, lane, acqRate_p):
    """
    :param devPtr: argument type c_void_p
    :param lane: argument type c_uint8
    :param acqRate: A pointer of the enumerate class E_N5C112GX4_DATA_ACQ_RATE
    """
    func = MZDAPILib["API_N5C112GX4_GetDataAcquisitionRate"]
    func.argtypes = [c_void_p, c_uint8, POINTER(c_int)]
    func.restype = c_uint32
    ret = func(devPtr, lane, acqRate_p)
    return ret


def API_N5C112GX4_ExecuteTraining(devPtr, lane, type):
    """
    :param devPtr: argument type c_void_p
    :param lane: argument type c_uint8
    :param type: member from enumerate class E_N5C112GX4_TRAINING
    """
    func = MZDAPILib["API_N5C112GX4_ExecuteTraining"]
    func.argtypes = [c_void_p, c_uint8, c_int]
    func.restype = c_uint32
    ret = func(devPtr, lane, type)
    return ret


def API_N5C112GX4_StartTraining(devPtr, lane, type):
    """
    :param devPtr: argument type c_void_p
    :param lane: argument type c_uint8
    :param type: member from enumerate class E_N5C112GX4_TRAINING
    """
    func = MZDAPILib["API_N5C112GX4_StartTraining"]
    func.argtypes = [c_void_p, c_uint8, c_int]
    func.restype = c_uint32
    ret = func(devPtr, lane, type)
    return ret


def API_N5C112GX4_CheckTraining(devPtr, lane, type, completed_p, failed_p):
    """
    :param devPtr: argument type c_void_p
    :param lane: argument type c_uint8
    :param type: member from enumerate class E_N5C112GX4_TRAINING
    :param completed: A pointer of the enumerate class MCESD_BOOL
    :param failed: A pointer of the enumerate class MCESD_BOOL
    """
    func = MZDAPILib["API_N5C112GX4_CheckTraining"]
    func.argtypes = [c_void_p, c_uint8, c_int, POINTER(c_int), POINTER(c_int)]
    func.restype = c_uint32
    ret = func(devPtr, lane, type, completed_p, failed_p)
    return ret


def API_N5C112GX4_StopTraining(devPtr, lane, type):
    """
    :param devPtr: argument type c_void_p
    :param lane: argument type c_uint8
    :param type: member from enumerate class E_N5C112GX4_TRAINING
    """
    func = MZDAPILib["API_N5C112GX4_StopTraining"]
    func.argtypes = [c_void_p, c_uint8, c_int]
    func.restype = c_uint32
    ret = func(devPtr, lane, type)
    return ret


def API_N5C112GX4_GetComparatorStats(devPtr, lane, statistics_p):
    """
    :param devPtr: argument type c_void_p
    :param lane: argument type c_uint8
    :param statistics: A pointer of the structure class S_N5C112GX4_PATTERN_STATISTICS
    """
    func = MZDAPILib["API_N5C112GX4_GetComparatorStats"]
    func.argtypes = [c_void_p, c_uint8, POINTER(S_N5C112GX4_PATTERN_STATISTICS)]
    func.restype = c_uint32
    ret = func(devPtr, lane, statistics_p)
    return ret


def API_N5C112GX4_ResetComparatorStats(devPtr, lane):
    """
    :param devPtr: argument type c_void_p
    :param lane: argument type c_uint8
    """
    func = MZDAPILib["API_N5C112GX4_ResetComparatorStats"]
    func.argtypes = [c_void_p, c_uint8]
    func.restype = c_uint32
    ret = func(devPtr, lane)
    return ret


def API_N5C112GX4_StartPhyTest(devPtr, lane):
    """
    :param devPtr: argument type c_void_p
    :param lane: argument type c_uint8
    """
    func = MZDAPILib["API_N5C112GX4_StartPhyTest"]
    func.argtypes = [c_void_p, c_uint8]
    func.restype = c_uint32
    ret = func(devPtr, lane)
    return ret


def API_N5C112GX4_StopPhyTest(devPtr, lane):
    """
    :param devPtr: argument type c_void_p
    :param lane: argument type c_uint8
    """
    func = MZDAPILib["API_N5C112GX4_StopPhyTest"]
    func.argtypes = [c_void_p, c_uint8]
    func.restype = c_uint32
    ret = func(devPtr, lane)
    return ret


def API_N5C112GX4_EOMInit(devPtr, lane):
    """
    :param devPtr: argument type c_void_p
    :param lane: argument type c_uint8
    """
    func = MZDAPILib["API_N5C112GX4_EOMInit"]
    func.argtypes = [c_void_p, c_uint8]
    func.restype = c_uint32
    ret = func(devPtr, lane)
    return ret


def API_N5C112GX4_EOMFinalize(devPtr, lane):
    """
    :param devPtr: argument type c_void_p
    :param lane: argument type c_uint8
    """
    func = MZDAPILib["API_N5C112GX4_EOMFinalize"]
    func.argtypes = [c_void_p, c_uint8]
    func.restype = c_uint32
    ret = func(devPtr, lane)
    return ret


def API_N5C112GX4_EOMMeasPoint(devPtr, lane, eyeTMB, phase, voltage, measurement_p):
    """
    :param devPtr: argument type c_void_p
    :param lane: argument type c_uint8
    :param eyeTMB: member from enumerate class E_N5C112GX4_EYE_TMB
    :param phase: argument type c_int32
    :param voltage: argument type c_uint8
    :param measurement: A pointer of the structure class S_N5C112GX4_EOM_DATA
    """
    func = MZDAPILib["API_N5C112GX4_EOMMeasPoint"]
    func.argtypes = [c_void_p, c_uint8, c_int, c_int32, c_uint8, POINTER(S_N5C112GX4_EOM_DATA)]
    func.restype = c_uint32
    ret = func(devPtr, lane, eyeTMB, phase, voltage, measurement_p)
    return ret


def API_N5C112GX4_EOM1UIStepCount(devPtr, lane, phaseStepCount_p, voltageStepCount_p):
    """
    :param devPtr: argument type c_void_p
    :param lane: argument type c_uint8
    :param phaseStepCount: A pointer of c_uint16
    :param voltageStepCount: A pointer of c_uint16
    """
    func = MZDAPILib["API_N5C112GX4_EOM1UIStepCount"]
    func.argtypes = [c_void_p, c_uint8, POINTER(c_uint16), POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(devPtr, lane, phaseStepCount_p, voltageStepCount_p)
    return ret


def API_N5C112GX4_EOMGetWidthHeight(devPtr, lane, eyeTMB, width_p, height_p):
    """
    :param devPtr: argument type c_void_p
    :param lane: argument type c_uint8
    :param eyeTMB: member from enumerate class E_N5C112GX4_EYE_TMB
    :param width: A pointer of c_uint16
    :param height: A pointer of c_uint16
    """
    func = MZDAPILib["API_N5C112GX4_EOMGetWidthHeight"]
    func.argtypes = [c_void_p, c_uint8, c_int, POINTER(c_uint16), POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(devPtr, lane, eyeTMB, width_p, height_p)
    return ret


def API_N5C112GX4_ExecuteCDS(devPtr, lane):
    """
    :param devPtr: argument type c_void_p
    :param lane: argument type c_uint8
    """
    func = MZDAPILib["API_N5C112GX4_ExecuteCDS"]
    func.argtypes = [c_void_p, c_uint8]
    func.restype = c_uint32
    ret = func(devPtr, lane)
    return ret


def API_N5C112GX4_GetSNR(devPtr, lane, snr_p):
    """
    :param devPtr: argument type c_void_p
    :param lane: argument type c_uint8
    :param snr: A pointer of c_uint32
    """
    func = MZDAPILib["API_N5C112GX4_GetSNR"]
    func.argtypes = [c_void_p, c_uint8, POINTER(c_uint32)]
    func.restype = c_uint32
    ret = func(devPtr, lane, snr_p)
    return ret


def API_N5C112GX4_PowerOnSeq(devPtr, powerOn):
    """
    :param devPtr: argument type c_void_p
    :param powerOn: implementation of the structure class S_N5C112GX4_PowerOn
    """
    func = MZDAPILib["API_N5C112GX4_PowerOnSeq"]
    func.argtypes = [c_void_p, S_N5C112GX4_PowerOn]
    func.restype = c_uint32
    ret = func(devPtr, powerOn)
    return ret


def API_N5C112GX4_PowerOffLane(devPtr, lane):
    """
    :param devPtr: argument type c_void_p
    :param lane: argument type c_uint8
    """
    func = MZDAPILib["API_N5C112GX4_PowerOffLane"]
    func.argtypes = [c_void_p, c_uint8]
    func.restype = c_uint32
    ret = func(devPtr, lane)
    return ret


def API_N5C112GX4_DownloadFirmware(devPtr, fwCodePtr_p, fwCodeSizeDW, errCode_p):
    """
    :param devPtr: argument type c_void_p
    :param fwCodePtr: A pointer of c_uint32
    :param fwCodeSizeDW: argument type c_uint32
    :param errCode: A pointer of c_uint16
    """
    func = MZDAPILib["API_N5C112GX4_DownloadFirmware"]
    func.argtypes = [c_void_p, POINTER(c_uint32), c_uint32, POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(devPtr, fwCodePtr_p, fwCodeSizeDW, errCode_p)
    return ret


def API_N5C112GX4_UpdateRamCode(devPtr, lane, code_p, codeSize, memSize, address, errCode_p):
    """
    :param devPtr: argument type c_void_p
    :param lane: argument type c_uint8
    :param code: A pointer of c_uint32
    :param codeSize: argument type c_uint32
    :param memSize: argument type c_uint32
    :param address: argument type c_uint32
    :param errCode: A pointer of c_uint16
    """
    func = MZDAPILib["API_N5C112GX4_UpdateRamCode"]
    func.argtypes = [c_void_p, c_uint8, POINTER(c_uint32), c_uint32, c_uint32, c_uint32, POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(devPtr, lane, code_p, codeSize, memSize, address, errCode_p)
    return ret


def API_N5C112GX4_HwWriteReg(devPtr, reg, value):
    """
    :param devPtr: argument type c_void_p
    :param reg: argument type c_uint32
    :param value: argument type c_uint32
    """
    func = MZDAPILib["API_N5C112GX4_HwWriteReg"]
    func.argtypes = [c_void_p, c_uint32, c_uint32]
    func.restype = c_uint32
    ret = func(devPtr, reg, value)
    return ret


def API_N5C112GX4_HwReadReg(devPtr, reg, data_p):
    """
    :param devPtr: argument type c_void_p
    :param reg: argument type c_uint32
    :param data: A pointer of c_uint32
    """
    func = MZDAPILib["API_N5C112GX4_HwReadReg"]
    func.argtypes = [c_void_p, c_uint32, POINTER(c_uint32)]
    func.restype = c_uint32
    ret = func(devPtr, reg, data_p)
    return ret


def API_N5C112GX4_HwSetPinCfg(devPtr, pin, pinValue):
    """
    :param devPtr: argument type c_void_p
    :param pin: member from enumerate class E_N5C112GX4_PIN
    :param pinValue: argument type c_uint16
    """
    func = MZDAPILib["API_N5C112GX4_HwSetPinCfg"]
    func.argtypes = [c_void_p, c_int, c_uint16]
    func.restype = c_uint32
    ret = func(devPtr, pin, pinValue)
    return ret


def API_N5C112GX4_HwGetPinCfg(devPtr, pin, pinValue_p):
    """
    :param devPtr: argument type c_void_p
    :param pin: member from enumerate class E_N5C112GX4_PIN
    :param pinValue: A pointer of c_uint16
    """
    func = MZDAPILib["API_N5C112GX4_HwGetPinCfg"]
    func.argtypes = [c_void_p, c_int, POINTER(c_uint16)]
    func.restype = c_uint32
    ret = func(devPtr, pin, pinValue_p)
    return ret


def API_N5C112GX4_Wait(devPtr, ms):
    """
    :param devPtr: argument type c_void_p
    :param ms: argument type c_uint32
    """
    func = MZDAPILib["API_N5C112GX4_Wait"]
    func.argtypes = [c_void_p, c_uint32]
    func.restype = c_uint32
    ret = func(devPtr, ms)
    return ret


def API_N5C112GX4_WriteReg(devPtr, lane, reg, value):
    """
    :param devPtr: argument type c_void_p
    :param lane: argument type c_uint8
    :param reg: argument type c_uint32
    :param value: argument type c_uint32
    """
    func = MZDAPILib["API_N5C112GX4_WriteReg"]
    func.argtypes = [c_void_p, c_uint8, c_uint32, c_uint32]
    func.restype = c_uint32
    ret = func(devPtr, lane, reg, value)
    return ret


def API_N5C112GX4_ReadReg(devPtr, lane, reg, data_p):
    """
    :param devPtr: argument type c_void_p
    :param lane: argument type c_uint8
    :param reg: argument type c_uint32
    :param data: A pointer of c_uint32
    """
    func = MZDAPILib["API_N5C112GX4_ReadReg"]
    func.argtypes = [c_void_p, c_uint8, c_uint32, POINTER(c_uint32)]
    func.restype = c_uint32
    ret = func(devPtr, lane, reg, data_p)
    return ret


def API_N5C112GX4_WriteField(devPtr, lane, fieldPtr_p, value):
    """
    :param devPtr: argument type c_void_p
    :param lane: argument type c_uint8
    :param fieldPtr: A pointer of the structure class MCESD_FIELD
    :param value: argument type c_uint32
    """
    func = MZDAPILib["API_N5C112GX4_WriteField"]
    func.argtypes = [c_void_p, c_uint8, POINTER(MCESD_FIELD), c_uint32]
    func.restype = c_uint32
    ret = func(devPtr, lane, fieldPtr_p, value)
    return ret


def API_N5C112GX4_ReadField(devPtr, lane, fieldPtr_p, data_p):
    """
    :param devPtr: argument type c_void_p
    :param lane: argument type c_uint8
    :param fieldPtr: A pointer of the structure class MCESD_FIELD
    :param data: A pointer of c_uint32
    """
    func = MZDAPILib["API_N5C112GX4_ReadField"]
    func.argtypes = [c_void_p, c_uint8, POINTER(MCESD_FIELD), POINTER(c_uint32)]
    func.restype = c_uint32
    ret = func(devPtr, lane, fieldPtr_p, data_p)
    return ret


def API_N5C112GX4_PollField(devPtr, lane, fieldPtr_p, value, timeout_ms):
    """
    :param devPtr: argument type c_void_p
    :param lane: argument type c_uint8
    :param fieldPtr: A pointer of the structure class MCESD_FIELD
    :param value: argument type c_uint32
    :param timeout_ms: argument type c_uint32
    """
    func = MZDAPILib["API_N5C112GX4_PollField"]
    func.argtypes = [c_void_p, c_uint8, POINTER(MCESD_FIELD), c_uint32, c_uint32]
    func.restype = c_uint32
    ret = func(devPtr, lane, fieldPtr_p, value, timeout_ms)
    return ret


def API_N5C112GX4_PollPin(devPtr, pin, value, timeout_ms):
    """
    :param devPtr: argument type c_void_p
    :param pin: member from enumerate class E_N5C112GX4_PIN
    :param value: argument type c_uint16
    :param timeout_ms: argument type c_uint32
    """
    func = MZDAPILib["API_N5C112GX4_PollPin"]
    func.argtypes = [c_void_p, c_int, c_uint16, c_uint32]
    func.restype = c_uint32
    ret = func(devPtr, pin, value, timeout_ms)
    return ret


