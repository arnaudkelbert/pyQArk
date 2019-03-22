# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
# 
#
# Widgets.QArkInputWidget.QArkBooleanInputWidget
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
from PyQt5 import QtCore, QtWidgets

from .QArkInputWidget import QArkInputWidget

class QArkBooleanCheckBoxWidget(QArkInputWidget):

    U_COLSIZE = 1

    def initUi(self,_s_label, _x_initValue):
        self.o_qcheckbox = QtWidgets.QCheckBox( _s_label, self )
        self.o_qcheckbox.setChecked( _x_initValue )

    def initConnection(self):
        pass

    def getChildWidget(self, _u_index=0):
        if _u_index == 0:
            return self.o_qcheckbox
        else:
            return QtCore.QVariant()

    def getValue(self):
        return self.o_qcheckbox.isChecked()

    def setValue( self, *args, **kwargs ):
        """
        Sets the widget value from the value returned by getValue()
        args[0] contains the retur of getValue fonction
        """
        self.o_qcheckbox.setChecked( args[0] )
