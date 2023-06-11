# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
# 
#
# Widgets.QArkInputWidget.QArkStringLineEditRangeWidget
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

from pyQArk.Widgets.QArkInputWidget.QArkInputWidget import QArkInputWidget, QArkInputWidgetBadFormat
from pyQArk.Core.QArkRange import QArkRange

class QArkStringLineEditRangeWidget( QArkInputWidget ):
    
    U_COLSIZE = 5

    def initUi(self,_s_label, _x_initValue):
        self.o_label = QtWidgets.QLabel( _s_label, self )
        self.o_label.setSizePolicy( QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred )
        self.o_labelMin = QtWidgets.QLabel( 'Min : ', self )
        self.o_labelMin.setSizePolicy( QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred )
        self.o_labelMax = QtWidgets.QLabel( 'Max : ', self )
        self.o_labelMax.setSizePolicy( QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred )
        self.o_lineEditMin = QtWidgets.QLineEdit( '', self )
        if not _x_initValue is None:
            self.o_lineEditMin.setText( str(_x_initValue[0]) )
        self.o_lineEditMin.setSizePolicy( QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred )
        self.o_lineEditMax = QtWidgets.QLineEdit( '', self )
        if not _x_initValue is None:
            self.o_lineEditMax.setText( str(_x_initValue[1]) )
        self.o_lineEditMax.setSizePolicy( QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred )

    def initConnection(self):
        pass

    def getChildWidget(self, _u_index=0):
        if _u_index == 0:
            return self.o_label
        elif _u_index == 1:
            return self.o_labelMin
        elif _u_index == 2:
            return self.o_lineEditMin
        elif _u_index == 3:
            return self.o_labelMax
        elif _u_index == 4:
            return self.o_lineEditMax
        else:
            return QtCore.QVariant()

    def getValue(self):
        try:
            return QArkRange( str( self.o_lineEditMin.text() ), str( self.o_lineEditMax.text() ) )
        except Exception as e:
            raise QArkInputWidgetBadFormat( self.__class__, '{} {}'.format(self.o_lineEditMin.text(),self.o_lineEditMax.text()), str(e) )

    def setValue( self, *args, **kwargs ):
        """
        Sets the widget value from the value returned by getValue()
        args[0] contains the retur of getValue fonction
        """
        o_qarkRange = args[0]
        self.o_lineEditMin.setText( str(o_qarkRange.min()) )
        self.o_lineEditMax.setText( str(o_qarkRange.max()) )
