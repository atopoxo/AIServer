import AIBuffer
import AISocketStream

MAX_PACKAGE_SIZE = 8192

class AINetworkBase(object):
    def __new__(CurrentClass):
        CurrentObject = super().__new__(CurrentClass)
        CurrentObject.Init()
        return CurrentObject

    def Init(Self):
        Self.m_ReceiveDataMap           = {}
        Self.m_bSocketError             = False
        Self.m_uLogOutputInternalTime   = 60000
        Self.m_uNextLogOutputTime       = 0

    def UnInit(Self):
        Self.m_bSocketError     = False
        for Buffer in Self.m_ReceiveDataMap.values():
            Buffer.Release()
        Self.m_ReceiveDataMap.clear()

    def Dispatch(Self, AIBuffer, AISocketStream, nMaxPackageSize = MAX_PACKAGE_SIZE):
        nOriginSize = AIBuffer.GetSize()
        if nOriginSize <= nMaxPackageSize:
            Self._RealSend(AIBuffer, AISocketStream)
        else:
            print()

    def Collect(Self, AISocketStream, nConnIndex, nMaxPackageSize = MAX_PACKAGE_SIZE):
        print()

    def _RealSend(Self, AIBuffer, AISocketStream):
        print()
        