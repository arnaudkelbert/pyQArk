# -*- coding: utf-8 -*-
from PyQt5 import QtCore

from pyQArk.Core.QArkMessage import QArkMessage

class QArkMessageSender( QtCore.QObject ):
    """
    A class that can send QArkMessageSender.
    A Qt signal is emitted.
    One object must be created in order to send message.
    The global QARK_MESSAGE_SENDER object can be used to send message
    and to connect signal with other QObject
    """

    messageSentSignal = QtCore.pyqtSignal( object )

    def __init__( self ):
        QtCore.QObject.__init__(self)

    def send( self
             , _o_message ):
        """
        Emit a signal with the message as argument
        @param _o_message : the message to emit
        @type _o_message : L{QArkMessage}
        """
        assert( isinstance(_o_message, QArkMessage) )
        self.messageSentSignal.emit( _o_message )

"""A global variable that can be used to send messages"""
QARK_MESSAGE_SENDER = QArkMessageSender()

def sendMessage( _o_message ):
    """
    A convenient function to send message.
    The QArkMessageSender sender is the global QARK_MESSAGE_SENDER
    @param _o_message : the message to emit
    @type _o_message : L{QArkMessage}
    """
    QARK_MESSAGE_SENDER.send( _o_message )
