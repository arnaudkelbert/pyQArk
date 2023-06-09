# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#
#
# QArkPixmapFrame
#
#
# @author : Arnaud Kelbert
# @date : 2014/008/01
# @version : 0.1
# {-- Pyhton 2/3 compatibility ------------------------------------------
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
# }-- Pyhton 2/3 compatibility ------------------------------------------
from PyQt5 import QtCore, QtGui, QtWidgets

from pyQArk.Core.QArkException import QArkException
from pyQArk.Image.QArkPixmap import QArkPixmap
from pyQArk.Image.QArkHistogramEqualization import QArkHistogramEqualization
from pyQArk.Image.QArkColorMapManager import QArkColorMapManager

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class QArkPixmapFrame( QtWidgets.QFrame ):
    """
    """
    DEFAULT_EQUALIZATION_MODE = QArkHistogramEqualization.LINEAR
    DEFAULT_COLORMAP = 'GREY'
    selectionChanged = QtCore.pyqtSignal()

    def __init__( self
                 , parent = None
                 , _t_data = None
                 , _s_colorMap = DEFAULT_COLORMAP
                 , _u_equalizationMode = DEFAULT_EQUALIZATION_MODE
                 ):
        super( QArkPixmapFrame, self).__init__( parent = parent )
        self.o_colorMapManager = QArkColorMapManager()
        self.o_colorMap = self.o_colorMapManager.getColorMap( _s_colorMap )
        self.u_equalizationMode = _u_equalizationMode
        self.t_originalData = _t_data
        self.o_imagePixmap = None
        self.o_imagePixmapItem = None
        if not self.t_originalData is None:
            self.loadPixmap()
        self.initUi()
        self.initConnection()

    def setColorMap( self, _s_colorMap ):
        self.o_colorMap = self.o_colorMapManager.getColorMap( _s_colorMap )

    def setEqualizationMode( self, _u_equalizationMode ):
        self.u_equalizationMode = _u_equalizationMode

    def setBackground(self):
        # Initialisation du fond
        u_gridSize = 10
        o_backgroundPixmap = QtGui.QPixmap(u_gridSize*2, u_gridSize*2)
        o_backgroundPixmap.fill(QtGui.QColor("white"))
        o_painter = QtGui.QPainter(o_backgroundPixmap)
        o_backgroundColor = QtGui.QColor("white")
        o_painter.fillRect(0, 0, u_gridSize, u_gridSize, o_backgroundColor)
        o_painter.fillRect(u_gridSize, u_gridSize, u_gridSize, u_gridSize, o_backgroundColor)
        o_painter.end()
        self.o_scene.setBackgroundBrush( QtGui.QBrush(o_backgroundPixmap) )

    def initUi(self):
        self.o_scene = QtWidgets.QGraphicsScene()
        self.o_graphicView = QtWidgets.QGraphicsView(self.o_scene)
        self.setBackground()
        self.o_graphicView.setRenderHint( QtGui.QPainter.SmoothPixmapTransform )
        self.o_graphicView.setStyleSheet( "QGraphicsView { border-style: none; }" )
        o_layout = QtWidgets.QGridLayout()
        o_layout.setContentsMargins(0, 0, 0, 0)
        o_layout.addWidget(self.o_graphicView, 0, 0)
        self.setLayout(o_layout)
        if not self.o_imagePixmap is None:
            self.paintImagePixmap()

    def initConnection(self):
        pass

    def reset(self):
        if not self.o_imagePixmapItem is None:
            self.o_scene.removeItem( self.o_imagePixmapItem )
            del self.o_imagePixmapItem
            self.o_imagePixmapItem = None
        if not self.o_imagePixmap is None:
            del self.o_imagePixmap
            self.o_imagePixmap = None

    def setData( self, _t_data ):
        self.reset()
        if not _t_data is None:
            self.t_originalData = _t_data
            self.loadPixmap()
            if not self.o_imagePixmap is None:
                self.paintImagePixmap()

    def getData( self ):
        return self.t_originalData

    def loadPixmap(self):
        # Equalization (transform so that data is between 0-255)
        self.t_equalizedData = QArkHistogramEqualization.computePreDefined( _t_data = self.t_originalData
                                                                           , _t_outLimits = (0,255)
                                                                           , _u_mode = self.u_equalizationMode
                                                                           )
        self.o_imagePixmap = QArkPixmap()
        self.o_imagePixmap.initFromGreyData( _t_data = self.t_equalizedData
                                            , _o_colorMap = self.o_colorMap
                                            )

    def paintImagePixmap(self):
        """
        """
        self.o_graphicView.resetTransform()
        self.o_imagePixmapItem = QtWidgets.QGraphicsPixmapItem()
        self.o_scene.addItem(self.o_imagePixmapItem)
        o_pixmap = self.o_imagePixmap.getPixmap()
        self.o_imagePixmapItem.setPixmap(o_pixmap)
        # Centrage
        self.o_imagePixmapItem.setOffset(-o_pixmap.width()//2, -o_pixmap.height()//2)
        self.o_imagePixmapItem.setTransformationMode(QtCore.Qt.SmoothTransformation)
        self.updateFitInView()

    @QtCore.pyqtSlot()
    def updateFitInView(self):
        if not self.o_imagePixmapItem is None:
            self.o_graphicView.fitInView( self.o_imagePixmapItem, QtCore.Qt.KeepAspectRatio )
            self.o_scene.setSceneRect(self.o_imagePixmapItem.boundingRect())