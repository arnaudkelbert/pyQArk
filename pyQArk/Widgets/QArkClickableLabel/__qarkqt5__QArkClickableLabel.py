# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#
#
# QArkClickableLabel
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
import unittest

from pyQArk import QArkConfig

from PyQt5 import QtCore, QtGui, QtWidgets

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)

class QArkClickableLabel( QtWidgets.QLabel ):
    """
    A clickable label widget
    """
    clicked = QtCore.pyqtSignal()

    def __init__( self
                 , parent=None
                 ):
        super( QArkClickableLabel, self).__init__( parent )

    def mouseReleaseEvent(self, ev):
        print( 'clicked' )
        self.clicked.emit()

class QArkClickableLabelTest( unittest.TestCase ):
    """
    Test
    """
    def test_widget(self):
        o_app = QtWidgets.QApplication( sys.argv )
        o_w = QArkClickableLabel()
        o_w.setText('click me!')
        o_w.show()
        o_app.exec_()

if __name__ == '__main__':
    unittest.main()
    #suite = unittest.TestLoader().loadTestsFromModule (QArkClickableLabelTest)
    #unittest.TextTestRunner().run(suite)
