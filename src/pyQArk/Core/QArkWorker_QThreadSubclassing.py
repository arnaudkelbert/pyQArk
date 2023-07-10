# -*- coding: utf-8 -*-
from PyQt5 import QtCore

class QArkWorker_QThreadSubclassing(QtCore.QObject):

    @classmethod
    def run( cls, _t_param, _o_interruptor ):
        """
        Run method : should be called in a QThread subclass mechanism where a QArkWorker instantiation is not needed
        """
        print('QArkWorker.run():start')
        # define here what to do
        print( _t_param )
        _o_interruptor.checkInterrupt()
        print( 'QArkWorker.run():end' )


