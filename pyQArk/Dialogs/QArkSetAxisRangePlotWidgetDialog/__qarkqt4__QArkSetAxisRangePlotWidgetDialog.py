# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#
#
# QArkSetAxisRangePlotWidgetDialog
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

from PyQt4 import QtCore, QtGui

from pyQArk.Core.QArkUiLoader import loadUi
from . import PKGPATH
Ui_QArkSetAxisRangePlotWidgetDialog = loadUi(PKGPATH('./QArkSetAxisRangePlotWidgetDialog.ui'), pkgname=__package__)

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

class QArkSetAxisRangePlotWidgetDialog( QtGui.QDialog, Ui_QArkSetAxisRangePlotWidgetDialog ):

    def __init__( self
                 , parent = None
                 , _o_plotWidget = None
                 ):
        super( QArkSetAxisRangePlotWidgetDialog, self ).__init__( parent = parent )
        self.o_plotWidget = _o_plotWidget
        self.initUi()
        self.initConnection()

    def initUi( self ):
        self.ui = Ui_QArkSetAxisRangePlotWidgetDialog()
        self.ui.setupUi(self)
        self.setObjectName(_fromUtf8("qArkSetAxisRangePlotWidgetDialog"))
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        f_xmin, f_xmax = self.o_plotWidget.getXRange()
        f_ymin, f_ymax = self.o_plotWidget.getYRange()
        self.ui.xminLineEdit.setText( str(f_xmin) )
        self.ui.xmaxLineEdit.setText( str(f_xmax) )
        self.ui.yminLineEdit.setText( str(f_ymin) )
        self.ui.ymaxLineEdit.setText( str(f_ymax) )

    def initConnection( self ):
        """
        """
        pass

    def accept( self ):
        try:
            self.f_xmin = float( self.ui.xminLineEdit.text() )
            self.f_xmax = float( self.ui.xmaxLineEdit.text() )
            self.f_ymin = float( self.ui.yminLineEdit.text() )
            self.f_ymax = float( self.ui.ymaxLineEdit.text() )
            QtGui.QDialog.accept( self )
        except:
            QtGui.QMessageBox.critical( self, ''
                                    , 'Valeur incorrecte'
                                    , QtGui.QMessageBox.Ok
                                    )

    def getRange(self):
        return self.f_xmin, self.f_xmax, self.f_ymin, self.f_ymax
