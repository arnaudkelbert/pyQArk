# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
# 
#
# Widgets.QArkInputWidget.QArkStringLineEditRangeWidget
# 
#
# @author : Arnaud Kelbert
# @date : Nov 20, 2014
# @version : 0.1
#-----------------------------------------------------------------------
from PyQt4 import QtCore, QtGui

from .QArkInputWidget import QArkInputWidget, QArkInputWidgetBadFormat

from ...Core.QArkRange import QArkRange


class QArkStringLineEditRangeWidget( QArkInputWidget ):
    
    U_COLSIZE = 5
    
    
    def initUi(self,_s_label, _x_initValue):
        self.o_label = QtGui.QLabel( _s_label, self )
        self.o_label.setSizePolicy( QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred )
        
        self.o_labelMin = QtGui.QLabel( 'Min : ', self )
        self.o_labelMin.setSizePolicy( QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred )
        
        self.o_labelMax = QtGui.QLabel( 'Max : ', self )
        self.o_labelMax.setSizePolicy( QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred )
        
        self.o_lineEditMin = QtGui.QLineEdit( '', self )
        if not _x_initValue is None:
            self.o_lineEditMin.setText( str(_x_initValue[0]) )
        self.o_lineEditMin.setSizePolicy( QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred )
        
        self.o_lineEditMax = QtGui.QLineEdit( '', self )
        if not _x_initValue is None:
            self.o_lineEditMax.setText( str(_x_initValue[1]) )
        self.o_lineEditMax.setSizePolicy( QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred )
    
    
    
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
