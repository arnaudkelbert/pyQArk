# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
# 
#
# Widgets.QArkInputWidget.QArkBooleanInputWidget
# 
#
# @author : Arnaud Kelbert
# @date : Nov 20, 2014
# @version : 0.1
#-----------------------------------------------------------------------
from PyQt4 import QtCore, QtGui

from .QArkInputWidget import QArkInputWidget


class QArkBooleanCheckBoxWidget( QArkInputWidget ):
    
    
    U_COLSIZE = 1
    
    
    def initUi(self,_s_label, _x_initValue):
        self.o_qcheckbox = QtGui.QCheckBox( _s_label, self )
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
    