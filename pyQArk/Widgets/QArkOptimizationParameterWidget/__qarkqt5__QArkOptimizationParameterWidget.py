# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#
#
# QArkOptimizationParameterWidget
#
#
# @author : Arnaud Kelbert
# @date : 2021/11/25
#
# Historic:
# 0.1 : init version
# 2021/11/25 : add python 2/3 compatibility
# -----------------------------------------------------------------------
# {-- Python 2/3 compatibility ------------------------------------------
from __future__ import (absolute_import, division, print_function, unicode_literals)
import sys
try:
    from future import standard_library
    standard_library.install_aliases()

    from builtins import (ascii, bytes, chr, dict, filter, hex, input,
                          int, map, next, oct, open, pow, range, round,
                          str, super, zip)
except ImportError:
    if sys.version_info.major == 2:
        print('Warning : future package is missing - compatibility issues between python 2 and 3 may occur')
try:
    # Python 2 : basestring exists (for isinstance test)
    basestring
except:
    # Python 3 : basestring does not exist
    basestring = str
# }-- Python 2/3 compatibility ------------------------------------------
from PyQt5 import QtCore, QtWidgets
from pyQArk.Dialogs.QArkCriticalMessageBox.QArkCriticalMessageBox import QArkCriticalMessageBox
from pyQArk.Core import QArkQt
from pyQArk.Core.QArkUiLoader import loadUi
from pyQArk.Widgets.QArkOptimizationParameterWidget import PKGPATH
Ui_QArkOptimizationParameterWidget = loadUi(PKGPATH('./QArkOptimizationParameterWidget.ui'), pkgname=__name__.rpartition('.')[0])

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

class QArkOptimizationParameterWidget( QtWidgets.QWidget, Ui_QArkOptimizationParameterWidget ):
    """
    """

    def __init__( self
                 , parent = None
                 ):
        super( QArkOptimizationParameterWidget, self).__init__( parent = parent )
        self.s_parameterName = ''
        self.initUi()
        self.initConnection()

    def initUi( self ):
        """
        @brief init user interface
        """
        self.ui = Ui_QArkOptimizationParameterWidget()
        self.ui.setupUi(self)

        self.setObjectName( _fromUtf8("QArkOptimizationParameterWidget") )
        self.setAttribute( QtCore.Qt.WA_DeleteOnClose )

    def initConnection( self ):
        """
        @brief init connection
        """
        self.ui.minCheckBox.toggled.connect( self.handleMinCheckBoxToggled )
        self.ui.maxCheckBox.toggled.connect( self.handleMaxCheckBoxToggled )
        self.ui.optimizeCheckBox.toggled.connect( self.handleOptimizeCheckBoxToggled )

    def setParameterName(self, _s_name):
        self.s_parameterName = _s_name

    def setAll( self, _f_value, _b_optimize, _f_min=None, _f_max=None ):
        self.setValue(_f_value)
        self.ui.optimizeCheckBox.setChecked(_b_optimize)
        self.setMinValue(_f_min)
        self.setMaxValue(_f_max)

        if _f_min is None:
            self.ui.minCheckBox.setChecked(False)
        else:
            self.ui.minCheckBox.setChecked(True)

        if _f_max is None:
            self.ui.maxCheckBox.setChecked(False)
        else:
            self.ui.maxCheckBox.setChecked(True)

        self.checkOptimize()
        self.checkEnabledMin()
        self.checkEnabledMax()

    def isOptimized(self):
        return self.ui.optimizeCheckBox.isChecked()

    def setEnabledOptimize(self, _b_enabled):
        self.ui.optimizeCheckBox.setChecked(_b_enabled)
        self.ui.optimizeCheckBox.setEnabled(_b_enabled)
        self.ui.minCheckBox.setEnabled(_b_enabled)
        self.ui.maxCheckBox.setEnabled(_b_enabled)
        self.ui.minLineEdit.setEnabled(_b_enabled)
        self.ui.maxLineEdit.setEnabled(_b_enabled)

    def setVisibleOptimizeOptions(self, _b_visible):
        self.ui.optimizeCheckBox.setVisible(_b_visible)
        self.ui.minCheckBox.setVisible(_b_visible)
        self.ui.maxCheckBox.setVisible(_b_visible)
        self.ui.minLineEdit.setVisible(_b_visible)
        self.ui.maxLineEdit.setVisible(_b_visible)

    def checkOptimize(self):
        if self.ui.optimizeCheckBox.isChecked():
            self.ui.minCheckBox.setEnabled(True)
            self.ui.maxCheckBox.setEnabled(True)
            self.ui.minLineEdit.setEnabled(self.ui.minCheckBox.isChecked())
            self.ui.maxLineEdit.setEnabled(self.ui.maxCheckBox.isChecked())

        else:
            self.ui.minLineEdit.setEnabled(False)
            self.ui.maxLineEdit.setEnabled(False)
            self.ui.minCheckBox.setEnabled(False)
            self.ui.maxCheckBox.setEnabled(False)

    def checkEnabledMin( self ):
        if self.ui.minCheckBox.isChecked():
            self.ui.minLineEdit.setEnabled(self.ui.optimizeCheckBox.isChecked())
        else:
            self.ui.minLineEdit.setEnabled(False)
            self.setMinValue(None)

    def checkEnabledMax( self ):
        if self.ui.maxCheckBox.isChecked():
            self.ui.maxLineEdit.setEnabled(self.ui.optimizeCheckBox.isChecked())
        else:
            self.ui.maxLineEdit.setEnabled(False)
            self.setMaxValue(None)

    def checkValues(self):
        try:
            self.getValue()
        except Exception as e:
            QArkQt._exec(QArkCriticalMessageBox('Parameter {} : invalid value'.format(self.s_parameterName), str(e)))
            return False

        try:
            self.getMinValue()
        except Exception as e:
            QArkQt._exec(QArkCriticalMessageBox('Parameter {} : invalid minimum boundary'.format(self.s_parameterName), str(e)))
            return False

        try:
            self.getMaxValue()
        except Exception as e:
            QArkQt._exec(QArkCriticalMessageBox('Parameter {} : invalid maximum boundary'.format(self.s_parameterName), str(e)))
            return False

        return True

    def setValue(self, _f_value):
        self.ui.valueLineEdit.setText( '%s' % _f_value )

    def setMinValue(self, _f_value):
        if not _f_value is None:
            self.ui.minLineEdit.setText( '%s' % _f_value )
        else:
            self.ui.minLineEdit.setText( '' )

    def setMaxValue(self, _f_value):
        if not _f_value is None:
            self.ui.maxLineEdit.setText( '%s' % _f_value )
        else:
            self.ui.maxLineEdit.setText( '' )

    def getValue(self, _f_factor=1.0):
        return float(str(self.ui.valueLineEdit.text()) ) * _f_factor

    def getMinValue( self, _f_factor=1.0 ):
        if self.ui.minCheckBox.isChecked():
            f_value = float( str(self.ui.minLineEdit.text()) ) * _f_factor
            return f_value
        else:
            return None

    def getMaxValue( self, _f_factor=1.0 ):
        if self.ui.maxCheckBox.isChecked():
            f_value = float( str(self.ui.maxLineEdit.text()) ) * _f_factor
            return f_value
        else:
            return None

    def getValuesAsDict( self, _f_factor=1.0 ):
        return { 'value' : self.getValue(_f_factor=_f_factor)
                ,'min' : self.getMinValue(_f_factor=_f_factor)
                ,'max' : self.getMaxValue(_f_factor=_f_factor)
                ,'optimize': self.ui.optimizeCheckBox.isChecked()
                }

    @QtCore.pyqtSlot()
    def handleOptimizeCheckBoxToggled(self):
        self.checkOptimize()

    @QtCore.pyqtSlot()
    def handleMinCheckBoxToggled( self ):
        self.checkEnabledMin()

    @QtCore.pyqtSlot()
    def handleMaxCheckBoxToggled( self ):
        self.checkEnabledMax()

