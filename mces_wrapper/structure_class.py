from ctypes import *

# MZDAPILib = CDLL('..\Debug\MZD.dll')

class S_N5C112GX4_PATTERN_STATISTICS(Structure):
    _fields_ = [("lock", c_bool),
                ("pass", c_bool),
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
    _fields_ = [("enable", c_bool),
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
                ("devEnabled", c_bool),
                ("fmcesdReadReg", CFUNCTYPE(c_void_p, c_uint32, POINTER(c_uint32))),
                ("fmcesdWriteReg", CFUNCTYPE(c_void_p, c_uint32, c_uint32)),
                ("fmcesdSetPinCfg", CFUNCTYPE(c_void_p, c_uint16, c_uint16)),
                ("fmcesdGetPinCfg", CFUNCTYPE(c_void_p, c_uint16, POINTER(c_uint16))),
                ("fmcesdWaitFunc", CFUNCTYPE(c_void_p, c_uint32)),
                ("appData", c_void_p),
               ]

# We may have errors here
class S_N5C112GX4_PowerOn(Structure):
    _fields_ = [
        ('unions', c_void_p),
        ('initTx', c_bool),
        ('initRx', c_bool),
        ('txOutputEn', c_bool),
        ('downloadFw', c_bool),
        ('dataPath', c_int),
        ('refClkSel', c_int),
        ('dataBusWidth', c_int),
        ('speed', c_int),
        ('refFreq', c_int),
        ('avdd', c_int),
        ('spdCfg', c_int),
        ('fwDownload', c_void_p)
    ]





