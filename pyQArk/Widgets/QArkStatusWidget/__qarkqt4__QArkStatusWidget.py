# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#
#
# QArkStatusWidget
#
#
# @author : Arnaud Kelbert
# @date : 2014/08/01
# @version : 0.1
#-----------------------------------------------------------------------
# {-- Pyhton 2/3 compatibility ------------------------------------------
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
# }-- Pyhton 2/3 compatibility ------------------------------------------
from PyQt4 import QtCore, QtGui

from pyQArk.Core.QArkUiLoader import loadUi
from pyQArk.Widgets.QArkStatusWidget import PKGPATH
Ui_QArkStatusWidget = loadUi(PKGPATH('./QArkStatusWidget.ui'), pkgname=__name__.rpartition('.')[0])

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

class QArkStatusWidget( QtGui.QWidget ):
    """
    """
    def __init__( self
                 , parent=None
                 ):
        super( QArkStatusWidget, self).__init__( parent )
        self.initUi()

    def initUi( self ):
        """
        @brief init user interface
        """
        self.ui = Ui_QArkStatusWidget()
        self.ui.setupUi(self)
        self.setObjectName( _fromUtf8("qArkStatusWidget") )
        self.setAttribute( QtCore.Qt.WA_DeleteOnClose )
        self.setProgressBarValue(0)
        self.setProgressLabel('')
        self.setMessageLabel('')

    def enableMessageStatus( self, _b_enable = True ):
        self.ui.statusLabel.setVisible( _b_enable )
        self.ui.statusLabel.setEnabled( _b_enable )

    def enableProgressStatus( self, _b_enable = True ):
        self.ui.progressLabel.setVisible( _b_enable )
        self.ui.progressLabel.setEnabled( _b_enable )
        self.ui.progressBar.setVisible( _b_enable )
        self.ui.progressBar.setEnabled( _b_enable )

    def setProgressLabel( self, _s_text ):
        self.ui.progressLabel.setText( _s_text )

    def setProgressBarValue( self, _u_progress ):
        self.ui.progressBar.setValue( _u_progress )

    def setMessageLabel( self, _s_text ):
        self.ui.statusLabel.setText( _s_text )

    def switchToProgress( self, _b_reset = True, _s_label = 'Progress...' ):
        self.enableProgressStatus(True)
        self.enableMessageStatus(False)
        if _b_reset:
            self.setProgressLabel( _s_label )
            self.setProgressBarValue( 0 )

    def switchToMessage( self ):
        self.enableProgressStatus(False)
        self.enableMessageStatus(True)

    def isMessageEnabled(self):
        return self.ui.statusLabel.isEnabled()

    def isProgressEnabled(self):
        return self.ui.progressBar.isEnabled()

    @QtCore.pyqtSlot(object)
    def setMessageSlot( self, _s_message ):
        if not self.isMessageEnabled():
            self.switchToMessage()
        self.setMessageLabel( _s_message )

    @QtCore.pyqtSlot(int)
    def setProgressValueSlot( self, _u_progress ):
        if not self.isProgressEnabled():
            self.switchToProgress()
        self.setProgressBarValue( _u_progress )


    @QtCore.pyqtSlot(object)
    def setProgressLabelSlot( self, _s_message ):
        if not self.isProgressEnabled():
            self.switchToProgress()
        self.setProgressLabel( _s_message )

    @QtCore.pyqtSlot()
    def handleSwitchToMessageRequest( self ):
        self.switchToMessage()

    @QtCore.pyqtSlot(object)
    def handleSwitchToProgressRequest( self, _s_label ):
        self.switchToProgress(_b_reset = True, _s_label = _s_label)







