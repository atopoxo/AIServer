import os
import queue as Queue
import AIThread

class AIThreadPool:
    m_Instance = None
    m_MaxThreadCount = 0
    m_ThreaList = []

    def __new__(CurrentClass):
        if not CurrentClass.m_Instance:
            CurrentClass.m_Instance = super(AIThreadPool, CurrentClass).__new__(CurrentClass)
            print("Class %s Created" %CurrentClass.m_Instance.__class__)
            CurrentClass.Init(CurrentClass.m_Instance)
        return CurrentClass.m_Instance

    def __del__(Self):
        Self.DeallocateThreads()

    def Release(Self):
        Self.DeallocateThreads()

    def Init(Self):
        print("Class %s Init Begin" %Self.__class__)
        m_ThreaList = Queue()
        Self.WorkQueue = Queue()
        m_MaxThreadCount = os.environ['NUMBER_OF_PROCESSORS']
        print("Class %s Init End" %Self.__class__)

    def AddTask(Self, Func, *Args):
        AIThreadInstance = AllocateThread();
        Self.WorkQueue.put((Func, Args))

    def AllocateThread(Self):
        AIThreadInstance = None
        if len(Self.m_ThreaList) <= m_MaxThreadCount:
            AIThreadInstance = AIThread(Self.WorkQueue)
            Self.m_ThreaList.append(AIThreadInstance)
        return AIThreadInstance

    def DeallocateThreads(Self):
        while len(Self.m_ThreadList) > 0:
            Self.m_ThreadList.SetRunState(False)
            Self.m_ThreadList.join()