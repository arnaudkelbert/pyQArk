# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
# 
#
# Widgets.QArkInputWidget.QArkInputWidget
# 
#
# @author : Arnaud Kelbert
# @date : 2019/03/19
# @version : 0.2
#
# Historic:
# 0.1 : init version
# 0.2 : add python 2/3 compatibility
# -----------------------------------------------------------------------
# {-- Pyhton 2/3 compatibility ------------------------------------------
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
import unittest
from PyQt5 import QtWidgets

from pyQArk.Core.QArkException import QArkException

class QArkInputWidgetBadFormat(QArkException):
    def __init__( self, *message ):
        super( self.__class__, self ).__init__( T_ERROR_MESSAGES[self.__class__].format(*message) )

T_ERROR_MESSAGES = {
  QArkInputWidgetBadFormat: '{} : bad input value {} - {}'
}    

class QArkInputWidget(QtWidgets.QWidget):
    
    U_COLSIZE = 1
    
    def __init__(self, parent, _s_label, _x_initValue, **kwargs ):
        QtWidgets.QWidget.__init__(self, parent)
        self.initUi( _s_label, _x_initValue )
        self.initConnection()
    
    def initUi(self,_s_label, _x_initValue):
        raise NotImplemented

    def initConnection(self):
        pass

    def getChildWidget(self, _u_index):
        raise NotImplemented

    def getValue(self):
        raise NotImplemented

    def setValue( self, *args, **kwargs):
        """
        Sets the widget value from the value returned by getValue()
        args[0] contains the retur of getValue fonction
        """
        raise NotImplemented
