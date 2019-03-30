# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#
#
# QArkPlotableObjectTreeItem
#
# Tree item for QArkPlotableObject
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

from .QArkTreeItem import QArkTreeItem

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
