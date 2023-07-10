import sys
import unittest
from PyQt5 import QtWidgets

from pyQArk.Widgets.QArkInputWidget.QArkStringLineEditWidget import QArkStringLineEditWidget
from pyQArk.Widgets.QArkInputListWidget.QArkInputListWidget import QArkInputListWidget

TEST_CLASS = QArkInputListWidget
class QArkInputListWidgetTest(unittest.TestCase):
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
            self.o_widget = TEST_CLASS(self
                 , _s_labelPrefix = 'default label'
                 , _x_defaultValue = 'default text'
                 , _cls_inputWidgetClass = QArkStringLineEditWidget
                 , _u_size = 1)

            self.o_widget.setInternalLayout()
            self.o_layout.addWidget(self.o_widget)
            self.o_button0 = QtWidgets.QPushButton('Test')
            self.o_layout.addWidget(self.o_button0)

        def initConnection(self):
            self.o_button0.clicked.connect(self.handleButton0Clicked)

        def handleButton0Clicked(self):
            for v in self.o_widget.getValue(): print(v)

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