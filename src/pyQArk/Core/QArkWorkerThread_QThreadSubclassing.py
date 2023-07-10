# -*- coding: utf-8 -*-
from PyQt5 import QtCore

from pyQArk.Core.QArkWorkerInterruptor import QArkWorkerInterruptor

class QArkWorkerThread_QThreadSubclassing(QtCore.QThread):
    
    stdoutWriteRequest = QtCore.pyqtSignal(str)
    errorOccured = QtCore.pyqtSignal(str)
    returnedDataReady = QtCore.pyqtSignal(list)
    
    def __init__(self
                 , parent
                 , _cls_worker
                 , _t_workerParam
                 , _o_exceptionHandler
                 , _b_selfIO = True
                 ):
        QtCore.QThread.__init__(self, parent)
        self.t_workerParam = _t_workerParam
        self.cls_worker = _cls_worker
        self.o_exceptionHandler = _o_exceptionHandler    
        self.b_hasBeenTerminated = False
        self.o_saveStdOut = None
        self.o_saveStdErr = None
        self.x_return = None
        self.b_interruptThread = False
        self.o_mutexInterruptThread = QtCore.QMutex()
        self.b_selfIO = _b_selfIO

    def saveIO( self ):
        self.o_saveStdOut = sys.stdout
        self.o_saveStdErr = sys.stderr

    def restoreIO( self ):
        sys.stdout = self.o_saveStdOut
        sys.stderr = self.o_saveStdErr
                
    def write(self, _s_str):
        # called if self IO
        self.stdoutWriteRequest.emit( _s_str )

    def flush(self):
        # called if self IO
        pass

    def quit(self):
        if self.b_selfIO:
            self.restoreIO()
        QtCore.QThread.quit(self)

    def start(self):
        if self.b_selfIO:
            self.saveIO()
            # should not be done like this => not working for concurrent threads
            sys.stdout = self
            sys.stderr = self
        QtCore.QThread.start(self)
        
    def run(self):
        self.b_hasBeenTerminated = False    
        try:
            self.o_interruptor = QArkWorkerInterruptor()
            self.x_return = self.cls_worker.run( self.t_workerParam, self.o_interruptor )
            
            if not isinstance( self.x_return, list ):
                self.x_return = [ self.x_return ]        
            self.returnedDataReady.emit( self.x_return )
        except BaseException as e:
            self.errorOccured.emit( str(e) )
            #self.interruptThread()
            self.quit()    
        except:
            self.errorOccured.emit( '\n'.join(map(str,sys.exc_info())) )
            #self.interruptThread()
            self.quit()
        finally:
            self.quit()
            #self.restoreIO()

    #def isInterrupted( self ):
        #self.o_mutexInterruptThread.lock()
        #b_ret = self.b_interruptThread
        #self.o_mutexInterruptThread.unlock()
        #return b_ret

    #@QtCore.pyqtSlot()
    #def interruptThread( self ):
        #self.o_mutexInterruptThread.lock()
        #self.b_interruptThread = True
        #self.o_mutexInterruptThread.unlock()

    @QtCore.pyqtSlot()
    def handleInterruptRequest(self):
        self.o_interruptor.doInterrupt()
