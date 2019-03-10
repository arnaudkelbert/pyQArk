# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
# 
#
# Widgets.QArkInputWidget.QArkInputWidget
# 
#
# @author : Arnaud Kelbert
# @date : Nov 20, 2014
# @version : 0.1
#-----------------------------------------------------------------------
from PyQt4 import QtGui

from ...Core.QArkException import QArkException

class QArkInputWidgetBadFormat(QArkException):
    def __init__( self, *message ):
        super( self.__class__, self ).__init__( T_ERROR_MESSAGES[self.__class__].format(*message) )

T_ERROR_MESSAGES = {
 QArkInputWidgetBadFormat : '{} : bad input value {} - {}'
}    


class QArkInputWidget( QtGui.QWidget ):
    
    U_COLSIZE = 1
    
    def __init__(self, parent, _s_label, _x_initValue, **kwargs ):
        QtGui.QWidget.__init__(self, parent)
        
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


