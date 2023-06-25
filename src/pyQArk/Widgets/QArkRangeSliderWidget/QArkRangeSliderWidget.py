# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from pyQArk.Core.QArkUiLoader import loadUi
from pyQArk.Widgets.QArkRangeSliderWidget import PKGPATH
Ui_QArkRangeSliderWidget = loadUi(PKGPATH('./QArkRangeSliderWidget.ui'), pkgname=__name__.rpartition('.')[0],
                                  classname='QArkRangeSliderWidget')

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

class QArkRangeSliderWidget( QtWidgets.QWidget, Ui_QArkRangeSliderWidget ):
    """
    """
    def __init__( self
                 , parent = None
                 , parentMDI = None
                 ):
        super( QArkRangeSliderWidget, self).__init__( parent = parent )
        self.o_data = None
        # decimal precision (only used for text)
        self.u_decimalPrec = None
        self.initUi()
        self.initConnection()

    def setDecimalPrecision(self, _u_prec):
        self.u_decimalPrec = _u_prec
        if not _u_prec is None:
            self.ui.minValueLabel.setText( '{0:.{1}f}'.format( self.getLowerValue(), self.u_decimalPrec ) )
            self.ui.maxValueLabel.setText( '{0:.{1}f}'.format( self.getUpperValue(), self.u_decimalPrec ) )

    def initUi( self ):
        """
        @brief init user interface
        """
        self.ui = Ui_QArkRangeSliderWidget()
        self.ui.setupUi(self)
        self.setObjectName( _fromUtf8("qArkRangeSliderWidget") )
        self.setAttribute( QtCore.Qt.WA_DeleteOnClose )
        self.ui.slider.setMinimum(0)
        self.ui.slider.setMaximum(100)

    def initConnection( self ):
        """
        @brief init connection
        """
        self.ui.slider.lowerPositionChanged.connect( self.handleLowerPositionChanged )
        self.ui.slider.upperPositionChanged.connect( self.handleUpperPositionChanged )

    def setUpperValue(self, _f_value):
        self.f_upperValue = _f_value
        try:
            u_position = self.valueToPos( _f_value )
        except ZeroDivisionError:
            self.ui.slider.setUpperValue( 100 )
        else:
            self.ui.slider.setUpperValue( u_position )

    def setLowerValue(self, _f_value):
        self.f_lowerValue = _f_value
        try:
            u_position = self.valueToPos( _f_value )
        except:
            self.ui.slider.setUpperValue( 0 )
        else:
            self.ui.slider.setUpperValue( u_position )

    def setLimit( self, _f_min, _f_max ):
        self.f_min = _f_min
        self.f_max = _f_max
        #self.valueToPos = lambda x : int( 100 * (x-self.f_min)/(self.f_max-self.f_min) )
        #self.posToValue = lambda p : 0.01 * p * (self.f_max-self.f_min) + self.f_min
        self.setLowerValue( _f_min )
        self.setUpperValue( _f_max )
        self.ui.minValueLabel.setText( str(_f_min) )
        self.ui.maxValueLabel.setText( str(_f_max) )

    def posToValue(self, p):
        return 0.01 * p * (self.f_max-self.f_min) + self.f_min

    def valueToPos(self, x):
        return int( 100 * (x-self.f_min)/(self.f_max-self.f_min) )

    def getLowerValue(self):
        f_value = self.posToValue( self.ui.slider.lowerPos )
        return f_value

    def getUpperValue(self):
        f_value = self.posToValue( self.ui.slider.upperPos )
        return f_value

    @QtCore.pyqtSlot()
    def handleLowerPositionChanged(self):
        if not self.u_decimalPrec is None:
            self.ui.minValueLabel.setText( '{0:.{1}f}'.format( self.getLowerValue(), self.u_decimalPrec ) )
        else:
            self.ui.minValueLabel.setText( str( self.getLowerValue() ) )

    @QtCore.pyqtSlot()
    def handleUpperPositionChanged(self):
        if not self.u_decimalPrec is None:
            self.ui.maxValueLabel.setText( '{0:.{1}f}'.format( self.getUpperValue(), self.u_decimalPrec ) )
        else:
            self.ui.maxValueLabel.setText( str( self.getUpperValue() ) )