# -*- coding: utf-8 -*-
from PyQt5 import QtCore
import time

class QArkMessage( QtCore.QObject ):
    """
    A class that represents message. A QArkMessage can be emitted by a
    QArkMessageSender object.
    The time is stored at object creation.
    """

    def __init__( self
                  , _s_message
                  ):
        QtCore.QObject.__init__(self)
        self.s_message = _s_message
        self.s_time = time.strftime("%H:%M:%S")

    def __repr__( self ):
        return '[MESSAGE][{0}] {1}'.format( self.s_time, self.s_message )

    def getMessage(self):
        return self.s_message

    def getTime(self):
        return self.s_time
