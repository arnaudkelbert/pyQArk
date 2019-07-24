# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#
#
# QArkPlotableObject
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
from PyQt4 import QtCore, QtGui

class QArkPlotableObject( QtCore.QObject ):
    """
    QArk interface to make object plotable

    @warning : if this object (or subclassed object) is used to be drag
    and drop (model/view framework), you have to handle specific mimedata
    and dropmimedata function
    (you cannot therefore use QArkTreeViewModel functions : it will fail
    at encoding the QObject)
    """
    STYLE__SOLIDLINE = QtCore.Qt.SolidLine
    STYLE__DASHLINE = QtCore.Qt.DashLine
    STYLE__DOTLINE = QtCore.Qt.DotLine

    T_LIST_STYLES = {
        STYLE__SOLIDLINE:'Solid'
        ,STYLE__DASHLINE:'Dash'
        ,STYLE__DOTLINE:'Dot'
    }

    DEFAULT_COLOR = QtGui.QColor(0, 0, 0)
    DEFAULT_LISSAGE = 1
    DEFAULT_PEN_WIDTH = 1
    DEFAULT_LINE_STYLE = STYLE__SOLIDLINE

    valueChangedSignal = QtCore.pyqtSignal()
    toDisplayChangedSignal = QtCore.pyqtSignal(object)

    def __init__(self):
        super(QArkPlotableObject, self).__init__()
        self.o_color = self.DEFAULT_COLOR
        self.u_penWidth = self.DEFAULT_PEN_WIDTH
        self.u_lineStyle = self.STYLE__SOLIDLINE
        self.b_toDisplay = True

    def setColor( self, _o_color ):
        self.o_color = _o_color

    def getColor( self ):
        return self.o_color

    def setPenWidth( self, _u_width ):
        self.u_penWidth = _u_width

    def getPenWidth( self ):
        return self.u_penWidth

    def setLineStyle( self, _u_style ):
        self.u_lineStyle = _u_style

    def getLineStyle( self ):
        return self.u_lineStyle

    def setToDisplay( self, _b_toDisplay = True ):
        if _b_toDisplay != self.b_toDisplay:
            self.toDisplayChangedSignal.emit( _b_toDisplay )
        self.b_toDisplay = _b_toDisplay

    def getToDisplay( self ):
        return self.b_toDisplay

    def getData2D( self ):
        raise NotImplementedError

    def resetToDefault(self):
        self.o_color = self.DEFAULT_COLOR
        self.u_penWidth = self.DEFAULT_PEN_WIDTH
        self.u_lineStyle = self.STYLE__SOLIDLINE
