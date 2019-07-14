import AICSNetwork

class AIServer:
    m_Instance = None
    def __new__(CurrentClass):
        if not CurrentClass.m_Instance:
            CurrentClass.m_Instance = super(AIServer, CurrentClass).__new__(CurrentClass)
            print("Class %s Created" %CurrentClass.m_Instance.__class__)
            CurrentClass.Init(CurrentClass.m_Instance)
        return CurrentClass.m_Instance

    def InitNetwork(Self):
        print("Class %s Init Network Begin" %Self.__class__)
        #ToDo
        print("Class %s Init Network End" %Self.__class__)

    def Init(Self):
        print("Class %s Init Begin" %Self.__class__)
        Self.InitNetwork()
        print("Class %s Init End" %Self.__class__)