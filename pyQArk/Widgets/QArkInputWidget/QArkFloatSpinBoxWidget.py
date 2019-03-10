# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
# 
#
# Widgets.QArkInputWidget.QArkFloatSpinBoxWidget
# 
#
# @author : Arnaud Kelbert
# @date : Nov 20, 2014
# @version : 0.1
#-----------------------------------------------------------------------
from PyQt4 import QtCore, QtGui

from .QArkInputWidget import QArkInputWidget, QArkInputWidgetBadFormat


class QArkFloatSpinBoxWidget( QArkInputWidget ):
    
    
    U_COLSIZE = 2
    
    
    def initUi(self,_s_label, _x_initValue):
        self.o_label = QtGui.QLabel( _s_label, self )
        self.o_label.setSizePolicy( QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred )
        
        self.o_spinbox = QtGui.QDoubleSpinBox( self )
        self.o_spinbox.setValue( float(_x_initValue) )
        self.o_spinbox.setSizePolicy( QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred )
    
    
    
    def initConnection(self):
        pass
    
    
    
    def getChildWidget(self, _u_index=0):
        if _u_index == 0:
            return self.o_label
        elif _u_index == 1:
            return self.o_spinbox
        else:
            return QtCore.QVariant()
    
    
    
    def getValue(self):
        return float( self.o_spinbox.value() )


    def setValue( self, *args, **kwargs ):
        """
        Sets the widget value from the value returned by getValue()
        args[0] contains the retur of getValue fonction
        """
        self.o_spinbox.setValue( args[0] )
