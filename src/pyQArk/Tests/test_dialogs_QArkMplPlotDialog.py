# -*- coding: utf-8 -*-
import sys
import unittest

from PyQt5 import QtWidgets, QtCore

from pyQArk.Dialogs.QArkMplPlotDialog.QArkMplPlotDialog import QArkMplPlotDialog
from pyQArk.Widgets.QArkMplPlotWidget.QArkMplPlotter import QArkMplPlotter

import matplotlib
#print(matplotlib.rcParams['backend.qt5'])
import numpy as np

class MyPlotter(QArkMplPlotter):
    dataChanged = QtCore.pyqtSignal()
    def plot(self, **kwargs):
        try:
            self.o_axe.clear()
        except AttributeError:
            self.o_axe = self.initAxe(111, QArkMplPlotter.VIEW_MODE__PLOT)
        self.o_plot = self.o_axe.plot(self.o_data[0], self.o_data[1])

    def setData(self,x,y):
        self.o_data=[x,y]
        self.dataChanged.emit()

TEST_CLASS = QArkMplPlotDialog
class QArkMplPlotDialogTest(unittest.TestCase):
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
            o_dialog = TEST_CLASS(parent=self, _s_id='test')
            o_plotter = MyPlotter(parent=self, _o_data=[[0,1],[2,3]])
            o_dialog.getPlotWidget().setPlotter(o_plotter)

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