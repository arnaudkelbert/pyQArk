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
sys._excepthook = sys.excepthook
def exception_hook(exctype, value, traceback):
    print(exctype, value, traceback)
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)
sys.excepthook = exception_hook

import time
from pyQArk.QArkConfig import QARK_QT_GENERATION

if QARK_QT_GENERATION == 4:
    from PyQt4 import QtGui, QtCore
    QtWidgets=QtGui
elif QARK_QT_GENERATION == 5:
    from PyQt5 import QtWidgets, QtCore

from pyQArk.Dialogs.QArkWorkerThreadRunDialog.QArkWorkerThreadRunDialog import QArkWorkerThreadRunDialog
from pyQArk.Core.QArkWorker import QArkWorker

class MyWorker(QArkWorker):
    @QtCore.pyqtSlot()
    def handleInterruptRequest(self):
        print('my handleInterruptRequest')
        QArkWorker.handleInterruptRequest(self)

    @classmethod
    def run( cls, _t_param, _o_interruptor ):
        print('[Id {}] QArkWorker.run():start'.format(_t_param['wid']))
        print(QArkWorker.__name__)

        # define here what to do
        print('[Id {}] Waiting {} seconds'.format(_t_param['wid'], _t_param['wait']))
        i = 0
        while i < _t_param['wait']:
            #print_lock(_o_interruptor, _o_interruptor.checkInterrupt())
            _o_interruptor.checkInterrupt()
            time.sleep(0.5)
            #_o_interruptor.doInterrupt()

            if i > 0.8*_t_param['wait'] and _t_param['wid'] == 1:
                # Raise an exception on thread id 1
                print('raising an exception for test')
                raise Exception('raise exception test message')

            _o_interruptor.checkInterrupt()
            time.sleep(0.5)
            i+= 1

        print('[Id {}] QArkWorker.run():end'.format(_t_param['wid']))
        return _t_param['wid']

TEST_CLASS = QArkWorkerThreadRunDialog
class QArkWorkerThreadRunDialogTest(unittest.TestCase):
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
            o_dialog = TEST_CLASS(parent=self)
            o_dialog.setWorker(_cls_workerClass=MyWorker, _t_workerParam={'wid':1, 'wait':10})

            if QARK_QT_GENERATION == 5:
                o_dialog.setModal(True)
                o_dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
                o_dialog.show()

            elif QARK_QT_GENERATION == 4:
                o_dialog.setModal(True)
                o_dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
                o_dialog.show()
                #o_dialog.exec_()

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