# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui
from pyQArk.Models.QArkTreeItem import QArkTreeItem

class QArkPlotableObjectTreeItem( QArkTreeItem ):

    def dataCheckStateRole( self, _u_index ):
        if self.o_data.getToDisplay():
            return QtCore.Qt.Checked
        else:
            return QtCore.Qt.Unchecked

    def setDataCheckStateRole( self, _u_index, _x_value ):
        self.o_data.setToDisplay( _x_value == QtCore.Qt.Checked )
        return True

    def dataDecorationRole( self, _u_index ):
        """
        Plot a fill rectangle with item data color
        and a black border
        """
        o_pixmap = QtGui.QPixmap( QtCore.QSize(7,11) )
        o_pixmap.fill( self.getItemData().getColor() )

        o_pen = QtGui.QPen(QtCore.Qt.SolidLine)
        o_pen.setWidth(1)
        o_pen.setColor(QtGui.QColor(0,0,0))

        o_painter = QtGui.QPainter( o_pixmap )
        o_painter.setPen(o_pen)
        o_painter.drawRect(0,0,6,10)
        o_painter.end()

        return o_pixmap
