# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#
#
# QArkWorkerThreadController
#
# This implementation uses QThread subclassing.
# => Should reimplement it with so that the usage is transparent
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
from PyQt5 import QtWidgets, QtCore

from pyQArk.Core.QArkWorkerInterruptor import QArkWorkerInterruptor
#from pyQArk.Core.QArkWorkerThread import QArkWorkerThread

class QArkWorkerThreadController_EventDriven(QtCore.QObject):

    workerFinished = QtCore.pyqtSignal()
    #workerTerminated = QtCore.pyqtSignal() # => does not exists in Qt5
    workerError = QtCore.pyqtSignal(object)
    writeStdOutRequest = QtCore.pyqtSignal(object)
    interruptRequest = QtCore.pyqtSignal()
    interruptWorker = QtCore.pyqtSignal()

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
        self.interruptRequest.connect(self.handleInterruptRequest)
        self.b_doInterrupt = False

    def hasWorkerFinished(self):
        return self.b_hasWorkerFinished

    def setWorkerParameters(self, _t_param):
        self.t_workerParameters = _t_param

    def interrupt(self):
        self.interruptRequest.emit()

    def startThread( self ):
        self.b_doInterrupt = False
        self.t_returnedData = None
        #self.o_interruptor = QArkWorkerInterruptor()

        self.o_thread = QtCore.QThread()
        self.o_worker = self.cls_worker(_t_workerParameters=self.t_workerParameters
                                        #,_o_workerInterruptor=QArkWorkerInterruptor()
                                        ,_o_exceptionHandler=self.o_exceptionHandler
                                        ,_b_selfIO=self.b_selfIO
                                        )

        if not self.o_exceptionHandler is None:
            self.o_exceptionHandler.restoreSystemExceptHook()


        self.o_worker.moveToThread(self.o_thread)
        self.o_thread.started.connect(self.o_worker.start)
        self.interruptWorker.connect(self.o_worker.handleInterruptRequest)

        #self.o_thread.finished.connect(self.handleWorkerThreadFinished)

        #self.o_thread.finished.connect(self.o_worker.deleteLater)
        self.o_thread.finished.connect(self.o_worker.handleInterruptRequest)
        self.o_thread.finished.connect(self.o_thread.deleteLater)

        QtWidgets.qApp.aboutToQuit.connect(self.o_thread.quit)

        self.o_worker.o_workerInterruptor.isDoInterrupt.connect(self.handleIsDoInterrupt)
        self.o_worker.stdoutWriteRequest.connect(self.handleWorkerStdOutWriteRequest)
        self.o_worker.returnedDataReady.connect(self.handleWorkerReturnedDataReady)
        self.o_worker.errorOccured.connect(self.handleWorkerErrorOccured)
        self.o_worker.finished.connect(self.handleWorkerFinished)
        self.o_worker.finished.connect(self.o_thread.quit)


        #self.o_interruptor.moveToThread(self.o_thread)

        self.o_thread.start()

#        #self.o_thread.finished.connect(self.handleWorkerThreadFinished)
#        self.o_thread.finished.connect(self.o_worker.deleteLater)
#        self.o_thread.finished.connect(self.o_thread.deleteLater)
#
#
#        self.o_worker.finished.connect(self.o_thread.quit)
#        self.o_worker.errorOccured.connect(self.o_thread.quit)
#        self.o_worker.finished.connect(self.handleWorkerFinished)
#        self.o_worker.errorOccured.connect(self.handleWorkerErrorOccured)
#        self.o_worker.stdoutWriteRequest.connect(self.handleWorkerStdOutWriteRequest)
#        self.o_worker.returnedDataReady.connect(self.handleWorkerReturnedDataReady)
#
#
#        self.o_thread.started.connect(self.o_worker.start)
#        self.o_worker.moveToThread(self.o_thread)
#        self.interruptRequest.connect(self.o_worker.handleInterruptRequest)
#        #self.o_interruptor.moveToThread(self.o_thread)
#        QtWidgets.qApp.aboutToQuit.connect(self.o_thread.quit)
#        self.o_thread.start()

    def print_lock(self,_s_str):
        try:
            o_mutex = self.t_workerParameters['print_lock']
            o_locker = QtCore.QMutexLocker(o_mutex)
            print(_s_str)
        except KeyError:
            print(_s_str)

    def getReturnedData(self):
        return self.t_returnedData

    @QtCore.pyqtSlot(str)
    def handleWorkerStdOutWriteRequest(self, _s_str):
        self.writeStdOutRequest.emit(_s_str)

    @QtCore.pyqtSlot()
    def handleWorkerFinished(self):
        self.b_hasWorkerFinished = True
        self.workerFinished.emit()
        if not self.o_exceptionHandler is None:
            self.o_exceptionHandler.restoreLocalExceptHook()

    @QtCore.pyqtSlot(str)
    def handleWorkerErrorOccured(self, _s_str):
        self.workerError.emit(_s_str)

    @QtCore.pyqtSlot(list)
    def handleWorkerReturnedDataReady(self, _t_return):
        self.t_returnedData = _t_return

    @QtCore.pyqtSlot()
    def handleInterruptRequest(self):
        self.b_doInterrupt = True

    @QtCore.pyqtSlot()
    def handleIsDoInterrupt(self):
        #self.print_lock('thread asked for is do interrupt')
        if self.b_doInterrupt:
            self.print_lock('self.interruptWorker.emit()')
            #self.interruptWorker.emit()
            self.o_worker.o_workerInterruptor.doInterrupt()
            self.o_thread.quit()