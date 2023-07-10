import sys
import unittest
from PyQt5 import QtWidgets

from pyQArk.Widgets.QArkMessageTabWidget.QArkMessageTabWidget import QArkMessageTabWidget
from pyQArk.Core import QArkMessageSender
from pyQArk.Core import QArkWarningSender
from pyQArk.Core.QArkExceptionHandler import QArkExceptionHandler
from pyQArk.Core.QArkWarning import QArkWarning
#from pyQArk.Core.QArkExceptionHandableObject import QArkExceptionHandableObject


TEST_CLASS = QArkMessageTabWidget
class QArkMessageTabWidgetTest(unittest.TestCase):
    """
    Test
    """
    class _ControllerWidget(QtWidgets.QWidget):
        def __init__(self, parent):
            super(self.__class__, self).__init__(parent)
            self.initUi()
            self.initConnection()
            self.initSpecifics()

        def initSpecifics(self):
            self.o_exceptionHandler = QArkExceptionHandler(self, '.')
            self.o_exceptionHandler.setEnableExceptHook(True)

            self.o_messageSender = QArkMessageSender.QARK_MESSAGE_SENDER
            self.o_warningSender = QArkWarningSender.QARK_WARNING_SENDER

            self.o_widget.setMessageSender(self.o_messageSender)
            self.o_widget.setWarningSender(self.o_warningSender)
            self.o_widget.setExceptionHandler(self.o_exceptionHandler)
            self.o_widget.setAsSystemOutput()

        def initUi(self):
            self.o_layout = QtWidgets.QVBoxLayout(self)
            self.o_widget = TEST_CLASS(self)

            self.o_layout.addWidget(self.o_widget)
            self.o_button0 = QtWidgets.QPushButton('Test')
            self.o_layout.addWidget(self.o_button0)

        def initConnection(self):
            self.o_button0.clicked.connect(self.handleButton0Clicked)

        def handleButton0Clicked(self):
            try:
                print('test message')
                self.o_warningSender.send(QArkWarning('test warning'))
                raise Exception('test error')
            except Exception as e:
                self.o_exceptionHandler.handleException(e)

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