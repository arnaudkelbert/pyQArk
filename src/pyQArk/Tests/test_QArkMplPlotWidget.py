# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------
# @author : Arnaud Kelbert
# @date : 2019/07/23
# @version : 0.2
#
# Historic:
# 0.1 : init version
# 0.2 : add python 2/3 compatibility
# -----------------------------------------------------------------------
# {-- Pyhton 2/3 compatibility ------------------------------------------
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
# }-- Pyhton 2/3 compatibility ------------------------------------------
import unittest
from pyQArk.QArkConfig import QARK_QT_GENERATION

if QARK_QT_GENERATION == 4:
    from PyQt4 import QtCore, QtGui
    QtWidgets=QtGui
elif QARK_QT_GENERATION == 5:
    from PyQt5 import QtCore, QtWidgets

from pyQArk.Widgets.QArkMplPlotWidget.QArkMplPlotWidget import QArkMplPlotWidget
from pyQArk.Widgets.QArkMplPlotWidget.QArkMplPlotter import QArkMplPlotter

#import matplotlib
#print(matplotlib.rcParams['backend.qt4'])
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

TEST_CLASS = QArkMplPlotWidget
class QArkMplPlotWidgetTest(unittest.TestCase):
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
            x = np.arange(25)
            y = np.sin(x)*np.cos(3*x)
            o_data = [x,y]
            self.o_plotter = MyPlotter(parent=self,_o_data=o_data)
            self.o_widget.setPlotter(self.o_plotter)
            self.o_plotter.dataChanged.connect( self.o_widget.updatePlot)

        def initUi(self):
            self.o_layout = QtWidgets.QVBoxLayout(self)
            self.o_widget = TEST_CLASS(self)

            self.o_layout.addWidget(self.o_widget)
            self.o_button0 = QtWidgets.QPushButton('Test')
            self.o_layout.addWidget(self.o_button0)

        def initConnection(self):
            self.o_button0.clicked.connect(self.handleButton0Clicked)

        def handleButton0Clicked(self):
            x = np.random.randn(100)*np.pi
            y = np.sin(x)*np.cos(x/3)
            self.o_plotter.setData(x,y)
            #self.o_widget.updatePlot()

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