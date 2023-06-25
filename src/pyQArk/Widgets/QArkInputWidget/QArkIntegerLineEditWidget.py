# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets

from pyQArk.Widgets.QArkInputWidget.QArkInputWidget import QArkInputWidget, QArkInputWidgetBadFormat

class QArkIntegerLineEditWidget( QArkInputWidget ):

    U_COLSIZE = 2

    def initUi(self,_s_label, _x_initValue):
        self.o_label = QtWidgets.QLabel( _s_label, self )
        self.o_label.setSizePolicy( QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred )
        self.o_lineEdit = QtWidgets.QLineEdit( _s_label, self )
        self.o_lineEdit.setText( str(_x_initValue) )
        self.o_lineEdit.setSizePolicy( QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred )

    def initConnection(self):
        pass
    
    def getChildWidget(self, _u_index=0):
        if _u_index == 0:
            return self.o_label
        elif _u_index == 1:
            return self.o_lineEdit
        else:
            return QtCore.QVariant()
    
    def getValue(self):
        try:
            return int( self.o_lineEdit.text() )
        except Exception as e:
            raise QArkInputWidgetBadFormat( self.__class__, self.o_lineEdit.text(), str(e) )

    def setValue( self, *args, **kwargs ):
        """
        Sets the widget value from the value returned by getValue()
        args[0] contains the retur of getValue fonction
        """
        self.o_lineEdit.setText( str(args[0]) )
