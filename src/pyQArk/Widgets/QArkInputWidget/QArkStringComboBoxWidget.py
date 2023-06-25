# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets

from pyQArk.Widgets.QArkInputWidget.QArkInputWidget import QArkInputWidget, QArkInputWidgetBadFormat

class QArkStringComboBoxWidget( QArkInputWidget ):

    U_COLSIZE = 2

    def initUi(self,_s_label, _x_initValue):
        self.o_label = QtWidgets.QLabel( _s_label, self )
        self.o_label.setSizePolicy( QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred )
        self.o_comboBox = QtWidgets.QComboBox( self )
        self.o_comboBox.addItems( _x_initValue )
        self.o_comboBox.setSizePolicy( QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred )

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
        t_itemTexts = [ self.o_comboBox.itemText( u_index ) for u_index in range(self.o_comboBox.count()) ]

        try:
            self.o_comboBox.setCurrentIndex( t_itemTexts.index( args[0] ) )
        except:
            self.o_comboBox.setCurrentIndex( 0 )
