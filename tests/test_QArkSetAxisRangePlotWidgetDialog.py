import sys
import unittest
sys._excepthook = sys.excepthook
def exception_hook(exctype, value, traceback):
    print(exctype, value, traceback)
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)
sys.excepthook = exception_hook

from PyQt5 import QtWidgets, QtCore

from pyQArk.Dialogs.QArkSetAxisRangePlotWidgetDialog.QArkSetAxisRangePlotWidgetDialog import QArkSetAxisRangePlotWidgetDialog
from pyQArk.Widgets.QArkMplPlotWidget.QArkMplPlotWidget import QArkMplPlotWidget

class MyPlotWidget(QArkMplPlotWidget):
    def getXRange(self): return (0, 10)
    def getYRange(self): return (0, 100)

TEST_CLASS = QArkSetAxisRangePlotWidgetDialog
class QArkSetAxisRangePlotWidgetDialogTest(unittest.TestCase):
    """
    Test
    """
    class _ControllerWidget(QtWidgets.QWidget):
        def __init__(self, parent):
            super(self.__class__, self).__init__(parent)
            self.initUi()
            self.initConnection()

        def initUi(self):
            self.o_layout = QtWidgets.QVBoxLayout(self)
            self.o_button0 = QtWidgets.QPushButton('Test')
            self.o_layout.addWidget(self.o_button0)

        def initConnection(self):
            self.o_button0.clicked.connect(self.handleButton0Clicked)

        def handleButton0Clicked(self):
            o_dialog = TEST_CLASS(parent=self, _o_plotWidget=MyPlotWidget())

            o_dialog.setModal(True)
            o_dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
            o_dialog.show()

    def test_widget(self):
        print(TEST_CLASS)
        o_app = QtWidgets.QApplication(sys.argv)
        o_mainWindow = QtWidgets.QDialog()
        o_layout = QtWidgets.QVBoxLayout(o_mainWindow)
        o_widget = self.__class__._ControllerWidget(parent=o_mainWindow)
        o_layout.addWidget(o_widget)
        o_mainWindow.setLayout(o_layout)
        o_mainWindow.setWindowTitle(self.__class__.__name__+'.test_widget')
        o_mainWindow.show()
        o_app.exec_()

if __name__ == '__main__':
    unittest.main()