# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
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
