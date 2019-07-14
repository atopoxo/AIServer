class AINetworkBase(object):
    def __new__(CurrentClass):
        CurrentObject = super().__new__(CurrentClass)
        CurrentObject.Init()
        return CurrentObject

    def Init(Self):
        print("Call %s Init" %Self.__class__)

    def Active(Self):
        print("Active")

    def Send(Self):
        print("Send")

    def RealSend(Self):
        print("RealSend")

        