import sys
import unittest
from PyQt5 import QtWidgets

from pyQArk.Widgets.QArkInputWidget.QArkStringLineEditWidget import QArkStringLineEditWidget
from pyQArk.Widgets.QArkInputWidget.QArkIntegerSpinBoxWidget import QArkIntegerSpinBoxWidget
from pyQArk.Widgets.QArkInputWidgetGrid.QArkInputWidgetGrid import QArkInputWidgetGrid

TEST_CLASS = QArkInputWidgetGrid
class QArkInputWidgetGridTest(unittest.TestCase):
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
                                      ,_t_initTuple = [('key0', QArkStringLineEditWidget, 'label0', 'initvalue0', {})
                                                       ,('key1', QArkStringLineEditWidget, 'label1', 'initvalue1', {})
                                                       ,('key2', QArkIntegerSpinBoxWidget, 'label2', 11, {})
                                                       ]
                                       )

            self.o_layout.addWidget(self.o_widget)
            self.o_button0 = QtWidgets.QPushButton('Test')
            self.o_layout.addWidget(self.o_button0)
            o_spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum,
                                                 QtWidgets.QSizePolicy.MinimumExpanding)
            self.o_layout.addItem(o_spacerItem)

        def initConnection(self):
            self.o_button0.clicked.connect(self.handleButton0Clicked)

        def handleButton0Clicked(self):
            try:
                self.o_widget.registerValues()
            except Exception as e:
                print(e)
            for k,v in self.o_widget.getRegisteredValues().items(): print(k,v)

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