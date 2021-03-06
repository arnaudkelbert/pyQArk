# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#
#
# QArkWarning
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
from pyQArk import QArkConfig
if QArkConfig.QARK_QT_GENERATION == 4:
    from PyQt4 import QtCore
elif QArkConfig.QARK_QT_GENERATION == 5:
    from PyQt5 import QtCore
import time

class QArkWarning( QtCore.QObject ):
    """
    A class that represents warnings. A QArkWarning can be emitted by a
    QArkWarningSender object.
    The time is stored at object creation.
    """
    def __init__( self
                  , _s_message
                  ):
        QtCore.QObject.__init__(self)
        self.s_message = _s_message
        self.s_time = time.strftime("%H:%M:%S")

    def __repr__( self ):
        return '[WARNING][{0}] {1}'.format( self.s_time, self.s_message )

    def getMessage(self):
        return self.s_message

    def getTime(self):
        return self.s_time
