from ctypes import *


MZDAPILib = CDLL("..\Debug\MZD.dll")

class MZD_PCS_LINK_STATUS(Structure):
    _fields_ = [("hostCurrent", c_uint16),
                ("hostLatched", c_uint16),
                ("lineCurrent", c_uint16),
                ("lineLatched", c_uint16)]


class MZD_REPEATER_LINK_STATUS(Structure):
    _fields_ = [("hostCurrent", c_uint16 * 8),
                ("lineCurrent", c_uint16 * 8)]


class MZD_MODE_CONFIG(Structure):
    _fields_ = [("opMode", c_int),
                ("speed", c_int),
                ("opModeType", c_uint16),
                ("signalType", c_uint16),
                ("typeFEC", c_uint16),
                ("autoNeg", c_uint16),
                ("laneCount", c_uint16),
                ("reserved0", c_uint16),
                ("reserved1", c_uint16),
                ("reserved2", c_uint16)]


class MZD_MODE_OPTION_STRUCT(Structure):
    _fields_ = [("buffer", c_uint8 * 128)]


class MZD_SERDES_EYE_RAW(Structure):
    _fields_ = [("eyeRawData", c_int32 * 33153)]


class MZD_DIAG_FFE(Structure):
    _fields_ = [("taps", c_int32 * 33)]


class MZD_DIAG_TX_FFE(Structure):
    _fields_ = [("preCursor", c_uint32),
                ("pre2Cursor", c_uint32),
                ("pre3Cursor", c_uint32),
                ("mainCursor", c_uint32),
                ("postCursor", c_uint32)]


class MZD_FILE_HEADER_TYPE(Structure):
    _fields_ = [("dataLength", c_uint32),
                ("dataDestination", c_uint32),
                ("secChecksum", c_uint16),
                ("data_only", c_uint16),
                ("port_skip", c_uint16),
                ("nextHeaderOffset", c_uint32)]


class MZD_PCS_UNIT_INTR(Structure):
    _fields_ = [("srcFlag1", c_uint16),
                ("srcFlag2", c_uint16),
                ("apAutoNeg", c_int),
                ("excessiveLinkErr", c_int)]


class MZD_SERDES_UNIT_INTR(Structure):
    _fields_ = [("powerCntl", c_uint32),
                ("speedCntl", c_uint32),
                ("rxLane", c_uint32),
                ("autoNeg", c_uint32)]


class MZD_MAC_UNIT_INTR(Structure):
    _fields_ = [("todOverrun", c_uint32),
                ("todUnderrun", c_uint32),
                ("global", c_uint32),
                ("lane", c_uint32 * 8)]


class MZD_LED_CTRL(Structure):
    _fields_ = [("interfaceSelect", c_uint16),
                ("portSelect", c_uint16),
                ("laneSelect", c_uint16),
                ("blinkActivity", c_uint16),
                ("solidActivity", c_uint16),
                ("polarity", c_uint16),
                ("mixRateLevel", c_uint16),
                ("blinkRateSelect", c_uint16)]


class MZD_LED_TIMER_CONFIG(Structure):
    _fields_ = [("blinkRate1", c_uint16),
                ("blinkRate2", c_uint16),
                ("pulseStretchDuration", c_uint16)]


class MZD_RCLK_SRC_OPTION(Structure):
    _fields_ = [("overWriteSrcClock", c_int),
                ("srcClockSelect", c_uint16),
                ("dividerConfig", c_uint16),
                ("divideRatio", c_uint16)]


class MCESD_FIELD(Structure):
    _fields_ = [("reg", c_uint32),
                ("hiBit", c_int16),
                ("loBit", c_int16),
                ("totalBits", c_int16),
                ("mask", c_uint32),
                ("retainMask", c_uint32)]


class MZD_PTP_EGRESS_TSQ(Structure):
    _fields_ = [("timestamp", c_uint32),
                ("todUpdate", c_uint8),
                ("taiSelect", c_uint8),
                ("queueEntryID", c_uint16),
                ("valid", c_int)]


class MZD_PTP_EGRESS_MAC_TSQ(Structure):
    _fields_ = [("timestamp", c_uint32),
                ("seqId", c_uint16),
                ("domain", c_uint8),
                ("mssageType", c_uint8),
                ("taiSelect", c_uint8),
                ("todUpdate", c_uint8),
                ("valid", c_int)]


class MZD_PTP_INGRESS_TSQ(Structure):
    _fields_ = [("timestamp", c_uint32),
                ("seqId", c_uint16),
                ("domain", c_uint8),
                ("mssageType", c_uint8),
                ("taiSelect", c_uint8),
                ("todUpdate", c_uint8),
                ("valid", c_int)]


class MZD_TAI_TIME_ARRAY(Structure):
    _fields_ = [("todSecondsHigh", c_uint16),
                ("todSecondsLow", c_uint32),
                ("todNanoseconds", c_uint32),
                ("todFracNano", c_int32)]


class MZD_TAI_PPS_PULSE(Structure):
    _fields_ = [("ppsPulseCycSec", c_uint8),
                ("ppsPulseCycNanoSec", c_uint32),
                ("ppsPulseHiLvLen", c_uint32)]


class MCESD_DEV(Structure):
    _fields_ = [("ipMajorRev", c_uint8),
                ("ipMinorRev", c_uint8),
                ("devEnabled", c_int),
                ("fmcesdReadReg", CFUNCTYPE(c_void_p, c_uint32, POINTER(c_uint32))),
                ("fmcesdWriteReg", CFUNCTYPE(c_void_p, c_uint32, c_uint32)),
                ("fmcesdSetPinCfg", CFUNCTYPE(c_void_p, c_uint16, c_uint16)),
                ("fmcesdGetPinCfg", CFUNCTYPE(c_void_p, c_uint16, POINTER(c_uint16))),
                ("fmcesdWaitFunc", CFUNCTYPE(c_void_p, c_uint32)),
                ("appData", c_void_p)]


class MZD_SERDES_CTRL(Structure):
    _fields_ = [("serdesDev", MCESD_DEV),
                ("serdesMapPort", c_uint16),
                ("serdesMapHostLine", c_uint16)]


class MZD_PCS_CHIP_INTR(Structure):
    _fields_ = [("line", MZD_PCS_UNIT_INTR),
                ("host", MZD_PCS_UNIT_INTR)]


class MZD_SERDES_CHIP_INTR(Structure):
    _fields_ = [("line", MZD_SERDES_UNIT_INTR),
                ("host", MZD_SERDES_UNIT_INTR)]


class MZD_MAC_CHIP_INTR(Structure):
    _fields_ = [("lineMac", MZD_MAC_UNIT_INTR),
                ("hostMac", MZD_MAC_UNIT_INTR)]


class MZD_DEV(Structure):
    _fields_ = [("deviceId", c_int),
                ("chipRevision", c_int),
                ("mdioPort", c_uint16),
                ("portCount", c_uint16),
                ("hostConfig", MZD_MODE_CONFIG * 16),
                ("lineConfig", MZD_MODE_CONFIG * 16),
                ("devEnabled", c_int),
                ("devFlash", c_int),
                ("devInfo", c_int * 4),
                ("mzdFuncReadMdio", CFUNCTYPE(c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_uint16))),
                ("mzdFuncWriteMdio", CFUNCTYPE(c_void_p, c_uint16, c_uint16, c_uint16, c_uint16)),
                ("mzdFuncWait", CFUNCTYPE(c_void_p, c_uint)),
                ("serdesCntl", MZD_SERDES_CTRL),
                ("hostContext", c_void_p)]


class MZD_STATE_DUMP(Structure):
    _fields_ = [("devStuct", MZD_DEV),
                ("apiVersion", c_uint8 * 3),
                ("fwVersion", c_uint8 * 4),
                ("serdesRevision", c_uint8 * 4),
                ("coreTemperature", c_int32),
                ("cntlPCSReg", c_uint16),
                ("statusPCSReg", c_uint16 * 2),
                ("modeSelectReg", c_uint16),
                ("ffe", MZD_DIAG_FFE),
                ("txFFE", MZD_DIAG_TX_FFE),
                ("ctrlVal", c_uint32 * 64)]


class MZD_GLOBAL_CHIP_INTR(Structure):
    _fields_ = [("globalAggregatedIntr1", c_uint16),
                ("globalAggregatedIntr2", c_uint16),
                ("onChipProcIntr", c_int),
                ("gpioIntr", c_int * 9),
                ("macIntr", MZD_MAC_CHIP_INTR * 2),
                ("serdesIntr", MZD_SERDES_CHIP_INTR * 4),
                ("pcsIntr", MZD_PCS_CHIP_INTR * 16)]


