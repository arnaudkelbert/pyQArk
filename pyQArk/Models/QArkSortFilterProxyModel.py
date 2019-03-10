# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#
#
# QArkSortFilterProxyModel
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
from PyQt4 import QtCore, QtGui

class QArkSortFilterProxyModel( QtGui.QSortFilterProxyModel ):

    def lessThan( self, _o_leftIndex, _o_rightIndex ):
        o_leftData = _o_leftIndex.data(QtCore.Qt.DisplayRole)
        o_rightData = _o_rightIndex.data(QtCore.Qt.DisplayRole)
        return o_leftData < o_rightData
