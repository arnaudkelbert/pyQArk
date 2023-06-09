# -*- coding: utf-8 -*-
from PyQt5 import QtCore

from pyQArk.Core.QArkWarning import QArkWarning

class QArkWarningSender( QtCore.QObject ):
    """
    A class that can send QArkWarningSender.
    A Qt signal is emitted.
    One object must be created in order to send warning.
    The global QARK_WARNING_SENDER object can be used to send warning
    and to connect signal with other QObject
    """
    warningSentSignal = QtCore.pyqtSignal( object )

    def __init__( self ):
        QtCore.QObject.__init__(self)

    def send( self
             , _o_warning ):
        """
        Emit a signal with the warning as argument
        @param _o_warning : the warning to emit
        @type _o_warning : L{QArkWarning}
        """
        assert( isinstance(_o_warning, QArkWarning) )
        self.warningSentSignal.emit( _o_warning )

"""A global variable that can be used to send warnings"""
QARK_WARNING_SENDER = QArkWarningSender()

def sendWarning( _o_warning ):
    """
    A convenient function to send warning.
    The QArkWarningSender sender is the global QARK_WARNING_SENDER
    @param _o_warning : the warning to emit
    @type _o_warning : L{QArkWarning}
    """
    QARK_WARNING_SENDER.send( _o_warning )
