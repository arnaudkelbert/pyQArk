# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#
#
# QArkHorizontalSlider
#
#
# @author : Arnaud Kelbert
# @date : 2014/008/01
# @version : 0.1
#-----------------------------------------------------------------------
import sys
import os

from PyQt4 import QtCore, QtGui

from .Ui_QArkHorizontalSlider import Ui_QArkHorizontalSlider


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)




class QArkHorizontalSlider( QtGui.QTabWidget, Ui_QArkHorizontalSlider ):
    """
    """
    valueChangedSignal = QtCore.pyqtSignal(object)

    def __init__( self
                 , parent = None
                 ):
        super( QArkHorizontalSlider, self).__init__( parent = parent )

        self.initUi()
        self.initConnection()



    def initUi( self ):
        """
        @brief init user interface
        """
        self.ui = Ui_QArkHorizontalSlider()
        self.ui.setupUi(self)

        self.setObjectName( _fromUtf8("qArkHorizontalSlider") )
        self.setAttribute( QtCore.Qt.WA_DeleteOnClose )



    def setLabel( self, _s_label ):
        self.ui.label.setText(_s_label)



    def setMinimum( self, _u_value ):
        self.ui.horizontalSlider.setMinimum(_u_value)
        self.ui.spinBox.setMinimum(_u_value)



    def setMaximum( self, _u_value ):
        self.ui.horizontalSlider.setMaximum(_u_value)
        self.ui.spinBox.setMaximum(_u_value)



    def initConnection( self ):
        """
        @brief init connection
        """
        self.ui.horizontalSlider.valueChanged.connect( self.updateSpinBoxSlot )
        self.ui.spinBox.valueChanged.connect( self.updateSliderSlot )




    def getValue(self):
        return self.ui.horizontalSlider.value()



    def setValue(self, _u_value):
        self.ui.spinBox.setValue(_u_value)



    @QtCore.pyqtSlot(int)
    def updateSpinBoxSlot( self, _u_value ):
        if _u_value != self.ui.spinBox.value():
            self.ui.spinBox.setValue(_u_value)
            self.valueChangedSignal.emit( _u_value )



    @QtCore.pyqtSlot()
    def updateSliderSlot( self ):
        if self.ui.spinBox.value() != self.ui.horizontalSlider.value:
            self.ui.horizontalSlider.setValue( self.ui.spinBox.value() )
            self.valueChangedSignal.emit( self.ui.spinBox.value() )





if __name__ == '__main__':
    o_app = QtGui.QApplication( sys.argv )
    o_w = QArkHorizontalSlider()
    o_w.show()

    sys.exit( o_app.exec_() )



