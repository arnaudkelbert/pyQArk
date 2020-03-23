# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#
#
# QArkWorkerInterruptor
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
from pyQArk.Core.QArkException import QArkException

class QArkWorkerInterruptException( QArkException ):
    def __init__( self ):
        super( self.__class__, self ).__init__( T_ERROR_MESSAGES[self.__class__] )

T_ERROR_MESSAGES = {
  QArkWorkerInterruptException : 'User interrupt'
}

class QArkWorkerInterruptor(object):
    
    def __init__(self):
        """
        """
        self.b_interrupt = False

    def doInterrupt(self):
        self.b_interrupt = True
        
    def checkInterrupt(self):
        """
        Check interrupt
        This method should be called in the worker run function
        """
        if self.b_interrupt:
            raise QArkWorkerInterruptException()
    