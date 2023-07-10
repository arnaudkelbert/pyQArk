# -*- coding: utf-8 -*-
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from pyQArk.Graphics.QArkGraphicsVirtualItem import QArkGraphicsVirtualItem

class QArkGraphicsSquareItem( QtWidgets.QGraphicsRectItem, QArkGraphicsVirtualItem ):

    def __init__(self, parent = None):
        QtWidgets.QGraphicsRectItem.__init__(self)
        self.parent = parent
        QArkGraphicsVirtualItem.__init__(self)


    def resize(self, p1, p2):
        f_dx = p2.x() - p1.x()
        f_dy = p2.y() - p1.y()
        f_r = (f_dx**2 + f_dy ** 2) ** 0.5

        o_p1 = QtCore.QPointF( np.floor( p1.x() - 2**0.5 * f_r), np.floor( p1.y() - 2**0.5 * f_r) )
        o_p2 = QtCore.QPointF( np.floor( p1.x() + 2**0.5 * f_r), np.floor( p1.y() + 2**0.5 * f_r) )

        self.setRect(QtCore.QRectF(o_p1, o_p2))

