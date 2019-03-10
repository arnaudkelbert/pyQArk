# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#
#
# QArkGraphicsVirtualItem
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
    
import numpy as np
from PyQt4 import QtCore, QtGui

from .QArkGraphicsVirtualItem import QArkGraphicsVirtualItem

class QArkGraphicsSquareItem( QtGui.QGraphicsRectItem, QArkGraphicsVirtualItem ):

    def __init__(self, parent = None):
        QtGui.QGraphicsRectItem.__init__(self)
        self.parent = parent
        QArkGraphicsVirtualItem.__init__(self)


    def resize(self, p1, p2):
        f_dx = p2.x() - p1.x()
        f_dy = p2.y() - p1.y()
        f_r = (f_dx**2 + f_dy ** 2) ** 0.5

        o_p1 = QtCore.QPointF( np.floor( p1.x() - 2**0.5 * f_r), np.floor( p1.y() - 2**0.5 * f_r) )
        o_p2 = QtCore.QPointF( np.floor( p1.x() + 2**0.5 * f_r), np.floor( p1.y() + 2**0.5 * f_r) )

        self.setRect(QtCore.QRectF(o_p1, o_p2))

