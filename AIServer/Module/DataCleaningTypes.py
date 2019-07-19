class FUNCTION_PROFILE_NODE:
    def __new__(CurrentClass):
        CurrentObject = super().__new__(CurrentClass)
        CurrentObject.Init()
        return CurrentObject

    def Init(Self):
        print("%s Init Begin" %Self.__class__)
        Self.uUID = 0
        print("%s Init End" %Self.__class__)
