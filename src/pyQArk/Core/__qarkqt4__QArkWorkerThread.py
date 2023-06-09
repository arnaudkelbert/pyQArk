# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#
#
# QArkWorkerThread
#
# This implementation uses QThread subclassing.
# => Should reimplement it to use an Event Driven mechanism
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

from pyQArk.Core.QArkWorkerInterruptor import QArkWorkerInterruptor

class QArkWorkerThread(QtCore.QThread):
    
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
        if self.b_selfIO:
            self.stdoutWriteRequest.emit( _s_str )
        else:
            QtCore.QThread.write(self, _s_str)

    def flush(self):
        if self.b_selfIO:
            pass
        else:
            try:
                QtCore.QThread.flush()
            except:
                pass

    def quit(self):
        if self.b_selfIO:
            self.restoreIO()
        QtCore.QThread.quit(self)

    def start(self):
        if self.b_selfIO:
            self.saveIO()
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
            self.errorOccured.emit('\n'.join([str(v) for v in sys.exc_info()]))
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
