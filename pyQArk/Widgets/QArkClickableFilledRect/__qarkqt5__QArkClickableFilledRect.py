# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#
#
# QArkClickableFilledRect
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

from pyQArk.Widgets.QArkClickableLabel.QArkClickableLabel import QArkClickableLabel

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

class QArkClickableFilledRect( QArkClickableLabel ):
    """
    """
    colorChangedSignal = QtCore.pyqtSignal(object)

    def __init__( self
                 , parent=None
                 , size = QtCore.QSize(100,100)
                 , borderWidth = 0
                 , fillColor = QtGui.QColor( 255, 255, 255 )
                 , borderColor = QtGui.QColor( 0, 0, 0 )
                 ):
        super( QArkClickableFilledRect, self).__init__( parent )
        self.o_size = size
        self.u_borderWidth = borderWidth
        self.o_fillColor = fillColor
        self.o_borderColor = borderColor
        self.initUi()

    def initUi(self):
        self.setFillColor( self.o_fillColor )

    def setSize( self, size ):
        self.o_size = size

    def getFillColor(self):
        return self.o_fillColor

    def setFillColor( self, _o_color ):
        o_pixmap = QtGui.QPixmap( self.o_size )
        o_pixmap.fill( _o_color )

        if self.u_borderWidth > 0:
            o_pen = QtGui.QPen(QtCore.Qt.SolidLine)
            o_pen.setWidth(self.u_borderWidth)
            o_pen.setColor(self.o_borderColor)

            o_painter = QtGui.QPainter( o_pixmap )
            o_painter.setPen(o_pen)
            o_painter.drawRect(0,0,self.o_size.width()-1,self.o_size.height()-1)
            o_painter.end()

        self.setPixmap(o_pixmap)
        self.setScaledContents(True)

        if _o_color != self.o_fillColor:
            self.colorChangedSignal.emit(_o_color)

        self.o_fillColor = _o_color

    def mouseReleaseEvent(self, ev):
        print( 'clicked' )
        self.clicked.emit()

class QArkClickableFilledRectTest( unittest.TestCase ):
    """
    Test
    """
    def test_widget(self):
        o_app = QtWidgets.QApplication( sys.argv )
        o_w = QArkClickableFilledRect( borderWidth=1, fillColor=QtGui.QColor(255,0,0) )
        #o_w.setText('click me!')
        o_w.show()
        o_app.exec_()

if __name__ == '__main__':
    unittest.main()
