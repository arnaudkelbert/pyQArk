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

from pyQArk.Core import QArkMessageSender
from pyQArk.Core import QArkWarningSender
from pyQArk.Core.QArkExceptionHandler import QArkExceptionHandler
from pyQArk.Core.QArkExceptionHandableObject import QArkExceptionHandableObject
from pyQArk.Core.QArkWorker import QArkWorker
from pyQArk.Core.QArkWorkerThreadController import QArkWorkerThreadController
import time
#from threading import Lock

def print_lock(str, _o_mutex):
    # Obliger de stocker le QMutexLocker dans une variable pour pas qu'il soit detruit : la portee du Mutex couvre ici l'ensemble de la methode
    # On peut aussi utiliser acquire() et release() sur _o_mutex => mais il ne faut pas oublier de release !
    o_locker = QtCore.QMutexLocker(_o_mutex)
    print(str)

class MyWorker(QArkWorker):
    @classmethod
    def run( cls, _t_param, _o_interruptor ):
        print_lock('[Id {}] QArkWorker.run():start'.format(_t_param['wid']), _t_param['print_lock'])

        # define here what to do
        print_lock('[Id {}] Waiting {} seconds'.format(_t_param['wid'], _t_param['wait']), _t_param['print_lock'])
        i = 0
        while i < _t_param['wait']:
            #print_lock(_o_interruptor, _o_interruptor.checkInterrupt())
            _o_interruptor.checkInterrupt()
            time.sleep(0.5)

            if i > 0.5*_t_param['wait'] and _t_param['wid'] == 1:
                # Raise an exception on thread id 1
                print_lock('[Id {}] raise exception'.format(_t_param['wid']), _t_param['print_lock'])
                raise Exception('raise exception test message')

            _o_interruptor.checkInterrupt()
            time.sleep(0.5)
            i+= 1

        print_lock('[Id {}] QArkWorker.run():end'.format(_t_param['wid']), _t_param['print_lock'])
        return _t_param['wid']

class MainProgram(QtCore.QObject, QArkExceptionHandableObject):

    def __init__(self):
        """Constructeur"""
        super(MainProgram, self).__init__()
        QArkExceptionHandableObject.__init__(self, QArkExceptionHandler(parent=self, _s_logDir='./'))
        self.o_messageSender = QArkMessageSender.QARK_MESSAGE_SENDER
        self.o_warningSender = QArkWarningSender.QARK_WARNING_SENDER
        self.getExceptionHandler().setEnableExceptHook(False)

    def run(self):
        print('Main program run...')

        self.o_printLock = QtCore.QMutex()
        self.t_controllers = []

        t_waitingTime = [ 6.,5.,7.]

        for i in range(3):
            o_controller = QArkWorkerThreadController(_cls_worker=MyWorker
                                                           , _t_workerParameters={'wid':i,'wait':t_waitingTime[i],'print_lock':self.o_printLock}
                                                           , _o_exceptionHandler=self.getExceptionHandler()
                                                           , _b_selfIO=False
                                                           )
            o_controller.workerError.connect(self.handleErrorHandledSlot)
            o_controller.workerFinished.connect(self.handleWorkerHasFinished)
            o_controller.writeStdOutRequest.connect(self.handleMessageSentSlot)
            self.t_controllers.append(o_controller)

        #o_timerInterruptCtrl2 = QtCore.QTimer()
        #o_timerInterruptCtrl2.start(int(0.2 * t_waitingTime[2] * 1000))
        #o_timerInterruptCtrl2.timeout.connect(self.simuUserInterrupt)

        for o_ctrl in self.t_controllers:
            print_lock('start {}'.format(o_ctrl), self.o_printLock)
            o_ctrl.startThread()

    def simuUserInterrupt(self):
        print_lock('send user interrupt to controller 2', self.o_printLock)
        self.t_controllers[2].interrupt()
        print_lock('sent', self.o_printLock)

    @QtCore.pyqtSlot(object)
    def handleWarningSentSlot(self, _o_warning):
        print_lock(_o_warning, self.o_printLock)

    @QtCore.pyqtSlot(object)
    def handleErrorHandledSlot(self, _o_error):
        print_lock(_o_error, self.o_printLock)

    @QtCore.pyqtSlot(object)
    def handleMessageSentSlot(self, _o_message):
        print_lock(_o_message, self.o_printLock)

    @QtCore.pyqtSlot()
    def handleWorkerHasFinished(self):
        print_lock('Id {} finished : {}'.format(self.sender().t_workerParameters['wid'], self.sender().getReturnedData()), self.o_printLock)

class QArkWorkerThreadControllerTest(unittest.TestCase):
    """
    Test
    """
    def test_widget(self):
        o_app = QtCore.QCoreApplication(sys.argv)
        o_timerStop = QtCore.QTimer()
        o_timerStop.start(8*1000)
        o_timerStop.timeout.connect(o_app.quit)

        o_mp = MainProgram()
        o_mp.run()

        o_timerUserInt = QtCore.QTimer()
        o_timerUserInt.singleShot(5000, o_mp.simuUserInterrupt)

        o_app.exec_()

if __name__ == '__main__':
    unittest.main()