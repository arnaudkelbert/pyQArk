# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from pyQArk.Core.QArkUiLoader import loadUi
from pyQArk.Widgets.QArkSimpleColorPickerWidget import PKGPATH
Ui_QArkSimpleColorPickerWidget = loadUi(PKGPATH('./QArkSimpleColorPickerWidget.ui'), pkgname=__name__.rpartition('.')[0],
                                  classname='QArkSimpleColorPickerWidget')

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

class QArkSimpleColorPickerWidget( QtWidgets.QWidget, Ui_QArkSimpleColorPickerWidget ):
    """
    """
    def __init__( self
                 , parent=None
                 ):
        super( QArkSimpleColorPickerWidget, self).__init__( parent )
        self.initUi()
        self.initConnection()

    def initUi( self ):
        """
        @brief init user interface
        """
        self.ui = Ui_QArkSimpleColorPickerWidget()
        self.ui.setupUi(self)
        self.setObjectName( _fromUtf8("qArkSimpleColorPickerWidget") )
        self.setAttribute( QtCore.Qt.WA_DeleteOnClose )
        self.ui.colorLabel.setSize( QtCore.QSize(50,23) )
        self.ui.colorLabel.setFillColor( QtGui.QColor(0,0,0))
        self.ui.redSlider.setValue(0)
        self.ui.greenSlider.setValue(0)
        self.ui.blueSlider.setValue(0)
        self.ui.redSlider.setMinimum(0)
        self.ui.redSlider.setMaximum(255)
        self.ui.greenSlider.setMinimum(0)
        self.ui.greenSlider.setMaximum(255)
        self.ui.blueSlider.setMinimum(0)
        self.ui.blueSlider.setMaximum(255)
        self.ui.redSlider.setLabel('R:')
        self.ui.greenSlider.setLabel('G:')
        self.ui.blueSlider.setLabel('B:')

    def initConnection( self ):
        self.ui.redSlider.valueChangedSignal.connect( self.handleSlidersValueChangedSlot )
        self.ui.greenSlider.valueChangedSignal.connect( self.handleSlidersValueChangedSlot )
        self.ui.blueSlider.valueChangedSignal.connect( self.handleSlidersValueChangedSlot )
        self.ui.colorLabel.clicked.connect( self.handleColorLabelClickedSlot )

    @QtCore.pyqtSlot(object)
    def handleSlidersValueChangedSlot( self, _u_value ):
        o_newColor = QtGui.QColor( self.ui.redSlider.getValue()
                                  ,self.ui.greenSlider.getValue()
                                  ,self.ui.blueSlider.getValue()
                                  )
        if o_newColor != self.ui.colorLabel.getFillColor():
            self.ui.colorLabel.setFillColor( o_newColor )

    @QtCore.pyqtSlot()
    def handleColorLabelClickedSlot( self ):
        o_colorDialog = QtWidgets.QColorDialog( self )
        o_colorDialog.setCurrentColor( self.ui.colorLabel.getFillColor() )
        o_newColor = o_colorDialog.getColor()
        if o_newColor != self.ui.colorLabel.getFillColor():
            self.ui.colorLabel.setFillColor( o_newColor )
