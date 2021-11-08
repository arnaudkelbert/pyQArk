# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#
#
# QArkSetNotationPlotWidgetDialog
#
#
# @author : Arnaud Kelbert
# @date : 2019/03/05
# @version : 0.2
#
# Historic:
# 0.1 : init version
# 0.2 : add python 2/3 compatibility
#-----------------------------------------------------------------------
#{-- Pyhton 2/3 compatibility ------------------------------------------
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
#}-- Pyhton 2/3 compatibility ------------------------------------------
from PyQt5 import QtCore, QtGui, QtWidgets

from pyQArk.Core.QArkUiLoader import loadUi
from pyQArk.Dialogs.QArkSetNotationPlotWidgetDialog import PKGPATH
Ui_QArkSetNotationPlotWidgetDialog = loadUi(PKGPATH('./QArkSetNotationPlotWidgetDialog.ui'), pkgname=__name__.rpartition('.')[0])

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



class QArkSetNotationPlotWidgetDialog( QtWidgets.QDialog, Ui_QArkSetNotationPlotWidgetDialog ):

    def __init__( self
                 , parent = None
                 , _o_plotWidget = None
                 ):
        super( QArkSetNotationPlotWidgetDialog, self ).__init__( parent = parent )
        self.o_plotWidget = _o_plotWidget
        self.initUi()
        self.initConnection()

    def initUi( self ):
        self.ui = Ui_QArkSetNotationPlotWidgetDialog()
        self.ui.setupUi(self)
        self.setObjectName(_fromUtf8("qArkSetNotationPlotWidgetDialog"))
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.ui.titleLineEdit.setText( self.o_plotWidget.getTitle() )
        self.ui.xLabelLineEdit.setText( self.o_plotWidget.getXLabel() )
        self.ui.yLabelLineEdit.setText( self.o_plotWidget.getYLabel() )

    def initConnection( self ):
        """
        """
        pass

    def accept( self ):
        try:
            self.s_title = str( self.ui.titleLineEdit.text() )
            self.s_xLabel = str( self.ui.xLabelLineEdit.text() )
            self.s_yLabel = str( self.ui.yLabelLineEdit.text() )
            QtWidgets.QDialog.accept( self )
        except:
            QtWidgets.QMessageBox.critical( self, ''
                                    , 'Valeur incorrecte'
                                    , QtGui.QMessageBox.Ok
                                    )

    def getTitle(self):
        return self.s_title

    def getXLabel(self):
        return self.s_xLabel

    def getYLabel(self):
        return self.s_yLabel