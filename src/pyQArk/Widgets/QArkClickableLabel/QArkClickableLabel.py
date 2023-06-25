# -*- coding: utf-8 -*-
import unittest
from PyQt5 import QtCore, QtWidgets, QtWidgets

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
