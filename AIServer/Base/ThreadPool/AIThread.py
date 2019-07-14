import threading
from threading import Thread

class AIThread(Thread):
    m_bRun = False
    m_CurrentThreadName = None
    def __new__(CurrentClass, WorkQueue):
        CurrentObject = super(AIThread, CurrentClass).__new__(CurrentClass)
        CurrentObject.Init(WorkQueue)
        return CurrentObject

    def Init(Self, WorkQueue):
        Self.m_bRun = True
        Thread.__init__(Self, target = Active)
        Self.m_WorkQueue = WorkQueue
        Self.daemon = True
        Self.start()

    def Active(Self):
        Self.m_CurrentThreadName = threading.current_thread().name
        print("Thread[%s] Begin" %Self.m_CurrentThreadName)
        while GetRunState():
            if m_WorkQueue.empty():
                break
            Target, Args = Self.m_WorkQueue.get()
            Target(*Args)
            Self.m_WorkQueue.task_done()
            Self.m_WorkQueue.put((Target, Args))
        print("Thread[%s] End" %Self.m_CurrentThreadName)

    def SetRunState(Self, bState):
        m_bRun = bState

    def GetRunState(Self):
        return m_bRun