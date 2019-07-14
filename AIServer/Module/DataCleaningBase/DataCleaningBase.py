class DataCleaningBase(object):
    def __new__(CurrentClass):
        CurrentObject = super().__new__(CurrentClass)
        CurrentObject.Init()
        return CurrentObject

    def Init(Self):
        print("Call %s Init" %Self.__class__)


