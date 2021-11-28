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

from pyQArk import QArkConfig
if QArkConfig.QARK_QT_GENERATION == 4:
    from PyQt4 import QtCore, QtGui
elif QArkConfig.QARK_QT_GENERATION == 5:
    from PyQt5 import QtCore, QtGui

from pyQArk.Graphics.QArkGraphicsScene import QArkGraphicsScene

class QArkGraphicsVirtualItem( object ):

    def __init__(self):
        self.setAcceptHoverEvents(False)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, False)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable, False)

    def hoverEnterEvent(self, e):
        self.setPen( self.parent.o_penOver )

    def hoverLeaveEvent(self, e):
        self.setPen( self.parent.o_pen )

    def mousePressEvent(self, e):
        QtWidgets.QGraphicsItem.mousePressEvent(self, e)

    def mouseReleaseEvent(self, e):
        QtWidgets.QGraphicsItem.mouseReleaseEvent(self, e)

    def changeMode(self, mode):
        if mode == QArkGraphicsScene.CREATION_MOUSE_EVENT_MODE:
            self.setAcceptHoverEvents(False)
            self.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, False)
            self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable, False)

        elif mode == QArkGraphicsScene.EDITION_MOUSE_EVENT_MODE:
            self.setAcceptHoverEvents(True)
            self.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, True)
            self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable, True)

        else:
            self.setAcceptHoverEvents(False)
            self.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, False)
            self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable, False)
