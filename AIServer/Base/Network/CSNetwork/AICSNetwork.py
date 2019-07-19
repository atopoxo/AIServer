import AINetworkBase

class AICSNetwork(AINetworkBase):
    m_Instance = None
    def __new__(CurrentClass):
        if not CurrentClass.m_Instance:
            CurrentClass.m_Instance = super(AICSNetwork, CurrentClass).__new__(CurrentClass)
            print("Class %s Created" %CurrentClass.m_Instance.__class__)
            CurrentClass.Init(CurrentClass.m_Instance)
        return CurrentClass.m_Instance

    def Init(Self):
        AINetworkBase.__init__(Self)
        print("Class %s Init" %Self.__class__)

