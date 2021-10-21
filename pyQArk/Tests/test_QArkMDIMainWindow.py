# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------
# @author : Arnaud Kelbert
# @date : 2019/03/19
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
#from pyQArk import QArkConfig
from pyQArk.QArkConfig import QARK_QT_GENERATION

if QARK_QT_GENERATION == 4:
    from PyQt4 import QtGui, QtCore
    QtWidgets=QtGui
elif QARK_QT_GENERATION == 5:
    from PyQt5 import QtWidgets, QtCore

from pyQArk.MainWindows.QArkMDIMainWindow.QArkMDIMainWindow import QArkMDIMainWindow

class MainUI(QArkMDIMainWindow):

    def __init__(self, _s_logDir):
        """Constructeur"""
        super(MainUI, self).__init__(_s_logDir)

    def initUiComponents(self):
        super(MainUI, self).initUiComponents()
        # self.ui_mdiArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        # self.ui_mdiArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)



        # self.o_aggregateCsvWidget = AggregateCsvWidget( parent = self )
        # self.addTabWidget( self.o_aggregateCsvWidget, 'CSV Aggregate')

        # self.o_plot3DWidget = Plot3DWidget( parent = self )
        # self.addTabWidget( self.o_plot3DWidget, 'Plot3D' )

    def initUiSplitter(self):
        super(MainUI, self).initUiSplitter()

    def afterShow(self):
        t_sizes = self.ui_qSplitter.sizes()
        self.ui_qSplitter.setSizes([sum(t_sizes) - 60, 60])
        self.ui_qSplitter.updateGeometry()

    def createActions(self):
        """
        """
        super(MainUI, self).createActions()

    def createMenus(self):
        """
        """
        self.addActionMenu('FILE_MENU', 'File', None, ('QUIT_ACTION',))

TEST_CLASS = QArkMDIMainWindow
class QArkMDIMainWindowTest(unittest.TestCase):
    """
    Test
    """
    def test_widget(self):
        print(TEST_CLASS)
        o_app = QtWidgets.QApplication(sys.argv)
        o_mainWindow = MainUI(_s_logDir='./log')
        o_mainWindow.setWindowTitle(self.__class__.__name__+'.test_widget')
        o_mainWindow.show()
        o_mainWindow.afterShow()
        o_app.exec_()

if __name__ == '__main__':
    unittest.main()