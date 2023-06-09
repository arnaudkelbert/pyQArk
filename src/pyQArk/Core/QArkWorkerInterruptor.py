# -*- coding: utf-8 -*-
from pyQArk import QArkConfig
from PyQt5 import QtCore

from pyQArk.Core.QArkException import QArkException

class QArkWorkerInterruptException( QArkException ):
    def __init__( self ):
        super( self.__class__, self ).__init__( T_ERROR_MESSAGES[self.__class__] )

T_ERROR_MESSAGES = {
  QArkWorkerInterruptException : 'User interrupt'
}

#class QArkWorkerInterruptor(QtCore.QObject):
class QArkWorkerInterruptor(QtCore.QObject):

    isDoInterrupt = QtCore.pyqtSignal()

    def __init__(self):
        """
        """
        QtCore.QObject.__init__(self)
        self.b_interrupt = False

    def reset(self):
        self.b_interrupt = False

    def doInterrupt(self):
        self.b_interrupt = True
        
    def checkInterrupt(self):
        """
        Check interrupt
        This method should be called in the worker run function
        """
        if QArkConfig.QARK_QT_THREADING_EVENT_DRIVEN:
            # send a signal : used for asking connected thread (usually main/gui thread)
            # if user wants to interrupt
            self.isDoInterrupt.emit()
        if self.b_interrupt:
            raise QArkWorkerInterruptException()

    @classmethod
    def forceInterrupt(cls):
        raise QArkWorkerInterruptException()