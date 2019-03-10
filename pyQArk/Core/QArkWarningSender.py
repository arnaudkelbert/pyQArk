# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
# 
#
# QArkWarningSender
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

from .QArkWarning import QArkWarning

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
