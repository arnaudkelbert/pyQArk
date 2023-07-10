# -*- coding: utf-8 -*-
import unittest
from PyQt5 import QtCore, QtWidgets
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
                 , fillColor = QtWidgets.QColor( 255, 255, 255 )
                 , borderColor = QtWidgets.QColor( 0, 0, 0 )
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
        o_pixmap = QtWidgets.QPixmap( self.o_size )
        o_pixmap.fill( _o_color )

        if self.u_borderWidth > 0:
            o_pen = QtWidgets.QPen(QtCore.Qt.SolidLine)
            o_pen.setWidth(self.u_borderWidth)
            o_pen.setColor(self.o_borderColor)

            o_painter = QtWidgets.QPainter( o_pixmap )
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
        o_w = QArkClickableFilledRect( borderWidth=1, fillColor=QtWidgets.QColor(255,0,0) )
        #o_w.setText('click me!')
        o_w.show()
        o_app.exec_()

if __name__ == '__main__':
    unittest.main()
