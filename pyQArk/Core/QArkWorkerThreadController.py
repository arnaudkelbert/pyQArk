# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#
#
# QArkWorkerThreadController
#
#
# @author : Arnaud Kelbert
# @date : 2019/03/05
# @version : 0.2
#
# Historic:
# 0.1 : init version
# 0.2 : add python 2/3 compatibility
#-----------------------------------------------------------------------
#{-- Pyhton 2/3 compatibility ------------------------------------------
from __future__ import (absolute_import, division, print_function, unicode_literals)
import sys
try:
    from future import standard_library
    standard_library.install_aliases()

    from builtins import (ascii, bytes, chr, dict, filter, hex, input,
                          int, map, next, oct, open, pow, range, round,
                          str, super, zip)
except ImportError:
    if sys.version_info.major == 2:
        print('Warning : future package is missing - compatibility issues between python 2 and 3 may occur')
try:
    # Python 2 : basestring exists (for isinstance test)
    basestring
except:
    # Python 3 : basestring does not exist
    basestring = str
#}-- Pyhton 2/3 compatibility ------------------------------------------
from PyQt4 import QtCore

from .QArkWorker import QArkWorker
from .QArkWorkerThread import QArkWorkerThread

class QArkWorkerThreadController(QtCore.QObject):

    workerFinished = QtCore.pyqtSignal()
    workerTerminated = QtCore.pyqtSignal()
    workerError = QtCore.pyqtSignal(str)
    writeStdOutRequest = QtCore.pyqtSignal(str)
    interruptRequest = QtCore.pyqtSignal()

    def __init__( self
                 , _cls_worker
                 , _t_workerParameters
                 , _o_exceptionHandler
                 ):
        """
        """
        QtCore.QObject.__init__(self)
        self.b_hasWorkerFinished = False
        self.cls_worker = _cls_worker
        self.t_workerParameters = _t_workerParameters
        self.o_exceptionHandler = _o_exceptionHandler
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
                                          )
        self.o_workerThread.finished.connect( self.handleWorkerThreadFinished )
        self.o_workerThread.terminated.connect( self.handleWorkerThreadTerminated )
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

    @QtCore.pyqtSlot()
    def handleWorkerThreadTerminated(self):
        self.b_hasWorkerFinished = True
        self.workerTerminated.emit()
        if not self.o_exceptionHandler is None:
            self.o_exceptionHandler.restoreLocalExceptHook()

    @QtCore.pyqtSlot(str)
    def handleWorkerThreadErrorOccured(self, _s_str):
        self.workerError.emit(_s_str)

    @QtCore.pyqtSlot(list)
    def handleWorkerThreadReturnedDataReady(self, _t_return):
        self.t_returnedData = _t_return
