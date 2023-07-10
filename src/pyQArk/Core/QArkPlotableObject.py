# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui

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
