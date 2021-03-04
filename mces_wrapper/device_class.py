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

