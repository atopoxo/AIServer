import DataCleaningBase
import DataCleaningTypes

class FunctionProfile(DataCleaningBase):
    m_Instance = None
    def __new__(CurrentClass):
        if not CurrentClass.m_Instance:
            CurrentClass.m_Instance = super(FunctionProfile, CurrentClass).__new__(CurrentClass)
            print("Class %s Created" %CurrentClass.m_Instance.__class__)
            CurrentClass.Init(CurrentClass.m_Instance)
        return CurrentClass.m_Instance

    def Init(Self):
        print("Class %s Init Begin" %Self.__class__)
        print("Class %s Init End" %Self.__class__)

    def Update(Self, ):
        print("AIPerfAnalyzer Update")


