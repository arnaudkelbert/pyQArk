# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#
#
# QArkWorker
#
#
# @author : Arnaud Kelbert
# @date : 2019/03/05
# @version : 0.2
#
# TODO : User interrupt is not working (signal from Main Tread to Worker Thread is executed once the worker job is done)
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
from PyQt5 import QtCore

from pyQArk.Core.QArkWorkerInterruptor import QArkWorkerInterruptor

def print_lock(str, _o_mutex):
    # Obliger de stocker le QMutexLocker dans une variable pour pas qu'il soit detruit : la portee du Mutex couvre ici l'ensemble de la methode
    # On peut aussi utiliser acquire() et release() sur _o_mutex => mais il ne faut pas oublier de release !
    o_locker = QtCore.QMutexLocker(_o_mutex)
    print(str)

class QArkWorker_EventDriven(QtCore.QObject):

    stdoutWriteRequest = QtCore.pyqtSignal(str)
    errorOccured = QtCore.pyqtSignal(str)
    returnedDataReady = QtCore.pyqtSignal(list)
    finished = QtCore.pyqtSignal()

    def __init__(self
                 ,_t_workerParameters
                 #,_o_workerInterruptor
                 ,_o_exceptionHandler
                 ,_b_selfIO
                 ):
        QtCore.QObject.__init__(self)
        self.t_workerParameters = _t_workerParameters
        self.o_exceptionHandler = _o_exceptionHandler
        self.b_hasBeenTerminated = False
        self.o_saveStdOut = None
        self.o_saveStdErr = None
        self.x_return = None
        self.b_interruptThread = False
        #self.o_workerInterruptor = _o_workerInterruptor
        self.o_workerInterruptor = QArkWorkerInterruptor()
        self.o_mutexInterruptThread = QtCore.QMutex()
        self.b_selfIO = _b_selfIO

        try:
            self.o_printMutex = self.t_workerParameters['print_lock']
        except KeyError:
            self.o_printMutex = None

    def saveIO(self):
        self.o_saveStdOut = sys.stdout
        self.o_saveStdErr = sys.stderr

    def restoreIO(self):
        sys.stdout = self.o_saveStdOut
        sys.stderr = self.o_saveStdErr

    def write(self, _s_str):
        # called if self IO
        self.stdoutWriteRequest.emit(_s_str)

    def flush(self):
        # called if self IO
        pass

    def _start(self):
        if self.b_selfIO:
            self.saveIO()
            # should not be done like this => not working for concurrent threads
            sys.stdout = self
            sys.stderr = self

        self.b_hasBeenTerminated = False
        try:
            self.x_return = self.__class__.run( _t_param=self.t_workerParameters
                                                ,_o_interruptor=self.o_workerInterruptor
                                                )
            if not isinstance(self.x_return, list):
                self.x_return = [self.x_return]
            self.returnedDataReady.emit(self.x_return)
        except BaseException as e:
            self.errorOccured.emit(str(e))
        except:
            self.errorOccured.emit('\n'.join(map(str, sys.exc_info())))
        finally:
            self.finished.emit()

    @classmethod
    def run( cls, _t_param, _o_interruptor ):
        """
        Run method : should be called in a QThread subclass mechanism where a QArkWorker instantiation is not needed
        """
        print_lock('QArkWorker.run():start', _t_param['print_lock'])
        # define here what to do
        print( _t_param, _t_param['print_lock'])
        _o_interruptor.checkInterrupt()
        print( 'QArkWorker.run():end', _t_param['print_lock'])

    @QtCore.pyqtSlot()
    def start(self):
        self._start()

    @QtCore.pyqtSlot()
    def handleInterruptRequest(self):
        print_lock('handleInterruptRequest', self.o_printMutex)
        self.o_workerInterruptor.doInterrupt()
        #self.doInterrupt()
        #self.o_interruptor.doInterrupt()