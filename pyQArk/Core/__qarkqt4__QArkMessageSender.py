# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
# 
#
# QArkMessageSender
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

from .QArkMessage import QArkMessage

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
