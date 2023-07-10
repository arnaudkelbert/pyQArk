# -*- coding: utf-8 -*-
from pyQArk import QArkConfig
if QArkConfig.QARK_QT_GENERATION == 4:
    from PyQt4 import QtCore, QtGui
    QtWidgets = QtGui
elif QArkConfig.QARK_QT_GENERATION == 5:
    from PyQt5 import QtCore, QtGui, QtWidgets

from pyQArk.Graphics.QArkGraphicsVirtualItem import QArkGraphicsVirtualItem

class QArkGraphicsRectItem( QtWidgets.QGraphicsRectItem, QArkGraphicsVirtualItem ):

    def __init__(self, parent = None):
        QtWidgets.QGraphicsRectItem.__init__(self)
        self.parent = parent
        QArkGraphicsVirtualItem.__init__(self)

    def resize(self, p1, p2):
        self.setRect(QtCore.QRectF(p1, p2))
