# -*- coding: utf-8 -*-
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

    def internalLayout(self):
        o_layout = QtWidgets.QHBoxLayout(self)
        for i in range(self.__class__.U_COLSIZE):
            o_layout.addWidget(self.getChildWidget(i))
        return o_layout

    def setInternalLayout(self):
        self.setLayout(self.internalLayout())

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
