# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#
#
# QArkWorkerThreadController
#
# This implementation uses QThread subclassing.
# => Should reimplement it with so that the usage is transparent
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
from pyQArk import QArkConfig

if QArkConfig.QARK_QT_THREADING_MECHANISM == QArkConfig.QARK_QT_THREADING_QTHREAD_SUBCLASSING:
    from pyQArk.Core.QArkWorkerThreadController_QThreadSubclassing import QArkWorkerThreadController_QThreadSubclassing
    QArkWorkerThreadController = QArkWorkerThreadController_QThreadSubclassing

elif QArkConfig.QARK_QT_THREADING_MECHANISM == QArkConfig.QARK_QT_THREADING_EVENT_DRIVEN:
    from pyQArk.Core.QArkWorkerThreadController_EventDriven import QArkWorkerThreadController_EventDriven
    QArkWorkerThreadController = QArkWorkerThreadController_EventDriven

