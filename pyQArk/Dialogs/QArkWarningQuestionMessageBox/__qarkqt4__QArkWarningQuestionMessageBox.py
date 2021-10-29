# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#
#
# QArkWarningMessageBox
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
from PyQt4 import QtGui, QtCore

from pyQArk.Dialogs.QArkDialog import QArkDialog

class QArkWarningQuestionMessageBox(QtGui.QMessageBox):

    def __init__(self, message, detailedMessage=None, *args, **kwargs):
        QtGui.QMessageBox.__init__(self, *args, **kwargs)
        self.setText( message )
        self.setStandardButtons(QtGui.QMessageBox.Ignore | QtGui.QMessageBox.Abort)
        self.setIcon( QtGui.QMessageBox.Warning )
        if not detailedMessage is None:
            self.setDetailedText( detailedMessage )
        self.initConnection()

    def initConnection(self):
        self.finished.connect(self.handleFinished)

    def exec_(self, _b_centered=True, **kwargs):
        # Reimplemented to get it centered
        if _b_centered:
            QArkDialog.centerDialog( self, **kwargs )
        QtGui.QMessageBox.exec_(self, **kwargs)

    def isReplyIgnore(self):
        return self.u_reply == QtGui.QMessageBox.Ignore

    def isReplyAbort(self):
        return self.u_reply == QtGui.QMessageBox.Abort

    @QtCore.pyqtSlot(int)
    def handleFinished(self, v):
        self.u_reply = v
