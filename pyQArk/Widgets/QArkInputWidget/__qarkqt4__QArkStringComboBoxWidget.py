# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
# 
#
# Widgets.QArkInputWidget.QArkStringComboBoxWidget
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
from PyQt4 import QtCore, QtGui

from .QArkInputWidget import QArkInputWidget, QArkInputWidgetBadFormat


class QArkStringComboBoxWidget( QArkInputWidget ):
    
    
    U_COLSIZE = 2
    
    
    def initUi(self,_s_label, _x_initValue):
        self.o_label = QtGui.QLabel( _s_label, self )
        self.o_label.setSizePolicy( QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred )
        
        self.o_comboBox = QtGui.QComboBox( self )
        self.o_comboBox.addItems( _x_initValue )
        self.o_comboBox.setSizePolicy( QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred )
    
    
    
    def initConnection(self):
        pass
    
    
    
    def getChildWidget(self, _u_index=0):
        if _u_index == 0:
            return self.o_label
        elif _u_index == 1:
            return self.o_comboBox
        else:
            return QtCore.QVariant()
    
    
    
    def getValue(self):
        try:
            return str( self.o_comboBox.currentText() )
        except Exception as e:
            raise QArkInputWidgetBadFormat( self.__class__, self.o_lineEdit.text(), str(e) )



    def setValue( self, *args, **kwargs ):
        """
        Sets the widget value from the value returned by getValue()
        args[0] contains the retur of getValue fonction
        """
        t_itemTexts = [ self.o_comboBox.itemText( u_index ) for u_index in xrange(self.o_comboBox.count()) ]

        try:
            self.o_comboBox.setCurrentIndex( t_itemTexts.index( args[0] ) )
        except:
            self.o_comboBox.setCurrentIndex( 0 )
