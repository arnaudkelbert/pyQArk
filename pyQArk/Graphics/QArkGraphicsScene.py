# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#
#
# QArkGraphicsScene
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
    QtWidgets = QtGui
elif QArkConfig.QARK_QT_GENERATION == 5:
    from PyQt5 import QtCore, QtGui, QtWidgets

class QArkGraphicsScene( QtWidgets.QGraphicsScene ):

    NO_MOUSE_EVENT_MODE \
    ,CREATION_MOUSE_EVENT_MODE \
    ,EDITION_MOUSE_EVENT_MODE = range(3)

    def __init__(self):
        QtWidgets.QGraphicsScene.__init__(self)

        self.o_currentItem = None

        self.u_mouseEventMode = self.__class__.NO_MOUSE_EVENT_MODE
        self.b_mouseEventCreateState = False

        self.o_pen = QtGui.QPen(QtCore.Qt.green, 1)
        self.o_penCreate = QtGui.QPen(QtCore.Qt.red, 1)
        self.o_penOver = QtGui.QPen(QtCore.Qt.green, 1)


    def setMouseEventMode( self, _u_mode ):
        self.u_mouseEventMode = _u_mode


    def mousePressEvent( self, e ):
        if self.u_mouseEventMode is self.__class__.NO_MOUSE_EVENT_MODE:
            QtWidgets.QGraphicsScene.mousePressEvent(self, e)

        elif e.button() == QtCore.Qt.LeftButton \
                and self.u_mouseEventMode is self.__class__.CREATION_MOUSE_EVENT_MODE:
            self.o_creationFirstPoint = e.scenePos()
            self.o_currentItem = self.createItem()
            self.o_currentItem.setPen( self.o_penCreate )
            self.addItem( self.o_currentItem )
            self.b_mouseEventCreateState = True

        else:
            QtWidgets.QGraphicsScene.mousePressEvent(self, e)


    def mouseReleaseEvent( self, e ):
        if self.u_mouseEventMode is self.__class__.NO_MOUSE_EVENT_MODE:
            QtWidgets.QGraphicsScene.mouseReleaseEvent(self, e)

        elif e.button() == QtCore.Qt.LeftButton \
                and self.u_mouseEventMode is self.__class__.CREATION_MOUSE_EVENT_MODE:

            if e.scenePos() == self.o_creationFirstPoint:
                # delete current item
                self.removeItem( self.o_currentItem )
                del self.o_currentItem
                self.o_currentItem = None

            else:
                self.o_currentItem.setPen( self.o_pen )

            self.b_mouseEventCreateState = False

        else:
            QtWidgets.QGraphicsScene.mouseReleaseEvent(self, e)



    def mouseMoveEvent(self, e):
        if self.b_mouseEventCreateState:
            self.o_currentItem.resize( self.o_creationFirstPoint, e.scenePos() )

        else:
            QtWidgets.QGraphicsScene.mouseMoveEvent(self, e)


    def removeSelection(self):
        t_items = self.selectedItems()
        map( self.removeItem, t_items)
        for o_item in t_items:
            del o_item


    def setItemType( self, _cls_class ):
        self.cls_itemClass = _cls_class


    def createItem(self):
        return self.cls_itemClass()

