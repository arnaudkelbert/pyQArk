# -*- coding: utf-8 -*-
from PyQt5 import QtCore

from pyQArk.Core.QArkWorkerThread import QArkWorkerThread

class QArkWorkerThreadController_QThreadSubclassing(QtCore.QObject):

    workerFinished = QtCore.pyqtSignal()
    #workerTerminated = QtCore.pyqtSignal() # => does not exists in Qt5
    workerError = QtCore.pyqtSignal(object)
    writeStdOutRequest = QtCore.pyqtSignal(object)
    interruptRequest = QtCore.pyqtSignal()

    def __init__( self
                 , _cls_worker
                 , _t_workerParameters
                 , _o_exceptionHandler
                 , _b_selfIO = True
                 ):
        """
        """
        QtCore.QObject.__init__(self)
        self.b_hasWorkerFinished = False
        self.cls_worker = _cls_worker
        self.t_workerParameters = _t_workerParameters
        self.o_exceptionHandler = _o_exceptionHandler
        self.b_selfIO = _b_selfIO
        if self.o_exceptionHandler is None:
            print('Warning ! QArkWorkerThreadController:self.o_exceptionHandler not set - strange behaviour could occure')

    def hasWorkerFinished(self):
        return self.b_hasWorkerFinished

    def setWorkerParameters(self, _t_param):
        self.t_workerParameters = _t_param

    def interrupt(self):
        self.interruptRequest.emit()

    def startThread( self ):
        self.t_returnedData = None
        self.o_workerThread = QArkWorkerThread( None
                                          , self.cls_worker
                                          , self.t_workerParameters
                                          , self.o_exceptionHandler
                                          , _b_selfIO = self.b_selfIO
                                          )
        self.o_workerThread.finished.connect( self.handleWorkerThreadFinished )
        #self.o_workerThread.terminated.connect( self.handleWorkerThreadTerminated )
        self.o_workerThread.errorOccured.connect( self.handleWorkerThreadErrorOccured )
        self.o_workerThread.stdoutWriteRequest.connect( self.handleWorkerThreadStdOutWriteRequest )
        self.o_workerThread.returnedDataReady.connect( self.handleWorkerThreadReturnedDataReady )
        self.interruptRequest.connect( self.o_workerThread.handleInterruptRequest )

        if not self.o_exceptionHandler is None:
            self.o_exceptionHandler.restoreSystemExceptHook()

        self.o_workerThread.start()

    def getReturnedData(self):
        return self.t_returnedData

    @QtCore.pyqtSlot(str)
    def handleWorkerThreadStdOutWriteRequest(self, _s_str):
        self.writeStdOutRequest.emit( _s_str )

    @QtCore.pyqtSlot()
    def handleWorkerThreadFinished(self):
        self.b_hasWorkerFinished = True
        self.workerFinished.emit()
        if not self.o_exceptionHandler is None:
            self.o_exceptionHandler.restoreLocalExceptHook()

#    @QtCore.pyqtSlot()
#    def handleWorkerThreadTerminated(self):
#        self.b_hasWorkerFinished = True
#        self.workerTerminated.emit()
#        if not self.o_exceptionHandler is None:
#            self.o_exceptionHandler.restoreLocalExceptHook()

    @QtCore.pyqtSlot(str)
    def handleWorkerThreadErrorOccured(self, _s_str):
        self.workerError.emit(_s_str)

    @QtCore.pyqtSlot(list)
    def handleWorkerThreadReturnedDataReady(self, _t_return):
        self.t_returnedData = _t_return
