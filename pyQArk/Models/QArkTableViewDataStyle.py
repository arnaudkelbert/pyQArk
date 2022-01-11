# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#
#
# QArkTableViewDataStyle
#
#
# @author : Arnaud Kelbert
# @date : 2022/01/10
#
#-----------------------------------------------------------------------
#{-- Python 2/3 compatibility ------------------------------------------
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
# }-- Pyhton 2/3 compatibility ------------------------------------------
import datetime
from pyQArk.QArkConfig import QARK_QT_GENERATION

if QARK_QT_GENERATION == 4:
    from PyQt4 import QtGui, QtCore
    QtWidgets=QtGui
elif QARK_QT_GENERATION == 5:
    from PyQt5 import QtWidgets, QtCore, QtGui

def createGradientBrush(_o_color1, _o_color2):
    verGradient = QtGui.QLinearGradient(0, 0, 0, 20)
    gradient = verGradient
    gradient.setColorAt(0.0, _o_color1)
    gradient.setColorAt(1.0, _o_color2)
    brush = QtGui.QBrush(gradient)
    return brush

class QArkTableViewDataStyle(object):
    def __init__(self, _o_background, _o_foreground, _o_font):
        self.o_background = _o_background
        self.o_foreground = _o_foreground
        self.o_font = _o_font
    def getBackgroundRole(self):
        return self.o_background
    def getForegroundRole(self):
        return self.o_foreground
    def getFontRole(self):
        return self.o_font

