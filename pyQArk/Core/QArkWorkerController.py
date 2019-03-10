# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#
#
# QArkWorkerController
#
#
# @author : Arnaud Kelbert
# @date : 2019/03/05
# @version : 0.2
#
# Historic:
# 0.1 : init version
# 0.2 : add python 2/3 compatibility
#-----------------------------------------------------------------------
#{-- Pyhton 2/3 compatibility ------------------------------------------
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
#}-- Pyhton 2/3 compatibility ------------------------------------------

from PyQt4 import QtCore

from .QArkWorker import QArkWorker

class QArkThread(QtCore.QThread):
    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)

     # this class is solely needed for these two methods, there
     # appears to be a bug in PyQt 4.6 that requires you to
     # explicitly call run and start from the subclass in order
     # to get the thread to actually start an event loop
    def start(self):
        QtCore.QThread.start(self)

    def run(self):
        QtCore.QThread.run(self)
    
    def __del__(self):
        self.quit()
        self.wait()

class QArkWorkerController(QtCore.QObject):

    def __init__( self
                 , _cls_worker
                 , _o_exceptionHandler = None
                 ):
        """
        """
        QtCore.QObject.__init__(self)
        #self.o_thread = QtCore.QThread()
        #self.o_thread = QArkThread()

        self.cls_worker = _cls_worker
        self.o_exceptionHandler = _o_exceptionHandler

    def __del__(self):
        running = self.o_thread.running()
        self.o_thread.stop()
        if not self.o_thread.finished():
            self.o_thread.wait()

    def start( self, _t_param = {}, app = None ):
        t_param = _t_param
        #self.o_worker = self.cls_worker()
        self.o_thread = QtCore.QThread()
        #self.o_thread = QArkThread()   
        self.o_worker = self.cls_worker()
        #self.o_worker.dataReady.connect(onDataReady)
        self.o_worker.moveToThread( self.o_thread )
        self.o_worker.errorOccured.connect( self.handleError )
        self.o_worker.error.connect( self.handleStringError )
        self.o_worker.message.connect( self.handleMessage )
        #self.o_thread.started.connect( self.o_worker.process )
        self.o_worker.finished.connect( self.o_thread.quit )
        self.o_worker.finished.connect( self.o_worker.deleteLater )
        self.o_thread.finished.connect( self.o_thread.deleteLater )
        #o_worker.moveToThread( o_thread )

        if not app is None:
            self.o_thread.finished.connect(app.exit)

        print( 'start' )
        self.o_thread.start()

        QtCore.QMetaObject.invokeMethod( self.o_worker
                                         , 'process'
                                         #, QtCore.Qt.QueuedConnection
                                         , QtCore.Qt.DirectConnection
                                         , QtCore.Q_ARG(dict, t_param)
                                        )

        #self.o_worker.moveToThread( self.o_thread )
        #self.o_worker.errorOccured.connect( self.handleError )
        #self.o_worker.message.connect( self.handleMessage )
        #self.o_worker.finished.connect( self.o_thread.quit )

        #if not app is None:
            #self.o_thread.finished.connect(app.exit)

        #self.o_thread.start()

        #QtCore.QMetaObject.invokeMethod( self.o_worker
                                         #, 'process'
                                         #, QtCore.Qt.QueuedConnection
                                         ##, QtCore.Qt.DirectConnection
                                         #, QtCore.Q_ARG(dict, self.t_param)
                                        #)

    @QtCore.pyqtSlot(object)
    def handleStringError( self, _s_error ):
        print( 'handleError workerController' )
        print( _s_error )

    @QtCore.pyqtSlot(object)
    def handleError( self, _o_error ):
        print( 'handleError workerController' )
        #self.o_exceptionHandler.handleException( _o_error )

    @QtCore.pyqtSlot(str)
    def handleMessage( self, _s_message ):
        print( _s_message )
