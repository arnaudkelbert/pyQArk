# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#
#
# QArkPlotPenSettingsWidget
#
#
# @author : Arnaud Kelbert
# @date : 2014/08/01
# @version : 0.1
#-----------------------------------------------------------------------
from PyQt4 import QtCore, QtGui

from .Ui_QArkPlotPenSettingsWidget import Ui_QArkPlotPenSettingsWidget

from ...Core.QArkPlotableObject import QArkPlotableObject


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




class QArkPlotPenSettingsWidget( QtGui.QWidget, Ui_QArkPlotPenSettingsWidget ):
    """
    """
    applyClicked = QtCore.pyqtSignal()

    def __init__( self
                 , parent=None
                 ):
        super( QArkPlotPenSettingsWidget, self).__init__( parent )

        self.initUi()
        self.initConnection()



    def initUi( self ):
        """
        @brief init user interface
        """
        self.ui = Ui_QArkPlotPenSettingsWidget()
        self.ui.setupUi(self)

        self.setObjectName( _fromUtf8("qArkPlotPenSettingsWidget") )
        self.setAttribute( QtCore.Qt.WA_DeleteOnClose )

        self.ui.colorLabel.setSize( QtCore.QSize(37,17) )
        self.ui.colorLabel.setFillColor( QtGui.QColor(0,0,0))

        self.ui.styleComboBox.addItems( QArkPlotableObject.T_LIST_STYLES.values() )




    def initConnection( self ):
        self.ui.redSpinBox.valueChanged.connect( self.handleSpinBoxValueChangedSlot )
        self.ui.greenSpinBox.valueChanged.connect( self.handleSpinBoxValueChangedSlot )
        self.ui.blueSpinBox.valueChanged.connect( self.handleSpinBoxValueChangedSlot )

        self.ui.colorLabel.clicked.connect( self.handleColorLabelClickedSlot )
        self.ui.applyPushButton.clicked.connect( self.handleApplyPushButtonClickedSlot )



    def setColorSpinBoxes( self, _o_color ):
        if _o_color.red() != self.ui.redSpinBox.value():
            self.ui.redSpinBox.setValue( _o_color.red() )

        if _o_color.green() != self.ui.greenSpinBox.value():
            self.ui.greenSpinBox.setValue( _o_color.green() )

        if _o_color.blue() != self.ui.blueSpinBox.value():
            self.ui.blueSpinBox.setValue( _o_color.blue() )





    def setColor( self, _o_color ):
        self.ui.colorLabel.setFillColor( _o_color )
        self.setColorSpinBoxes( _o_color )


    def getColor( self ):
        return QtGui.QColor( self.ui.redSpinBox.value()
                            ,self.ui.greenSpinBox.value()
                            ,self.ui.blueSpinBox.value()
                            )


    def setLineWidth( self, _u_value ):
        self.ui.widthSpinBox.setValue( _u_value )


    def getLineWidth( self ):
        return self.ui.widthSpinBox.value()



    def setLineStyle( self, _u_style ):
        s_style = QArkPlotableObject.T_LIST_STYLES[_u_style]

        self.ui.styleComboBox.setCurrentIndex(
            self.ui.styleComboBox.findText( s_style )
            )


    def getLineStyle( self ):
        for key, value in QArkPlotableObject.T_LIST_STYLES.iteritems():
            if value == self.ui.styleComboBox.currentText():
                return key
        return None



    def setSettingsFromObject( self, _o_plotableObject ):
        self.setColor( _o_plotableObject.getColor() )
        self.setLineWidth( _o_plotableObject.getPenWidth() )
        self.setLineStyle( _o_plotableObject.getLineStyle() )



    @QtCore.pyqtSlot(object)
    def handleSpinBoxValueChangedSlot( self, _u_value ):
        o_newColor = QtGui.QColor( self.ui.redSpinBox.value()
                                  ,self.ui.greenSpinBox.value()
                                  ,self.ui.blueSpinBox.value()
                                  )

        if o_newColor != self.ui.colorLabel.getFillColor():
            self.ui.colorLabel.setFillColor( o_newColor )



    @QtCore.pyqtSlot()
    def handleColorLabelClickedSlot( self ):
        o_colorDialog = QtGui.QColorDialog( self )
        o_colorDialog.setCurrentColor( self.ui.colorLabel.getFillColor() )

        o_newColor = o_colorDialog.getColor()

        if o_newColor != self.ui.colorLabel.getFillColor():
            self.ui.colorLabel.setFillColor( o_newColor )
            self.setColorSpinBoxes( o_newColor )


    @QtCore.pyqtSlot()
    def handleApplyPushButtonClickedSlot(self):
        self.applyClicked.emit()






