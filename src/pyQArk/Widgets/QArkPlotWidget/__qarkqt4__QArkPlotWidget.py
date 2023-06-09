# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#
#
# QArkPlotWidget
#
#
# @author : Arnaud Kelbert
# @date : 2019/08/07
# @version : 0.2
#
# Historic:
# 0.1 : init version
# 0.2 : add python 2/3 compatibility
# -----------------------------------------------------------------------
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
"""
Error when there are no ticks to plot (to small range)

I am getting this error apparently when my plot is very small on the screen and the left axis tick mechanism seems to decide that the number of ticks is zero.


Traceback (most recent call last):
  File "C:\Users\j\Documents\projects\navala\3rd-lib\pyqtgraph-0.9.8\pyqtgraph\graphicsItems\AxisItem.py", line 412, in paint
    specs = self.generateDrawSpecs(painter)
  File "C:\Users\j\Documents\projects\navala\3rd-lib\pyqtgraph-0.9.8\pyqtgraph\graphicsItems\AxisItem.py", line 812, in generateDrawSpecs
    textSize2 = np.max([r.width() for r in textRects])
  File "C:\Python27\lib\site-packages\numpy\core\fromnumeric.py", line 2125, in amax
    out=out, keepdims=keepdims)
  File "C:\Python27\lib\site-packages\numpy\core\_methods.py", line 17, in _amax
    out=out, keepdims=keepdims)
ValueError: zero-size array to reduction operation maximum which has no identity


I replaced one line which read "            if i > 0:  ## always draw top level"
by "            if i > 0 and len(textRects) > 0:  ## always draw top level" as a workaround.

Julio
"""
from PyQt4 import QtCore, QtGui

import pyqtgraph as pg

class CustomViewBox(pg.ViewBox):
    def __init__(self, *args, **kwds):
        pg.ViewBox.__init__(self, *args, **kwds)
        self.setMouseMode(self.RectMode)

    ## reimplement right-click to zoom out
    def mouseClickEvent(self, ev):
        if ev.button() == QtCore.Qt.RightButton:
            self.autoRange()

    def mouseDragEvent(self, ev):
        if ev.button() == QtCore.Qt.RightButton:
            ev.ignore()
        else:
            pg.ViewBox.mouseDragEvent(self, ev)

class QArkPlotWidget( QtGui.QWidget ):

    T_ACCEPTED_EXPORT_FORMATS = [ 'png' ]

    def __init__(self
                 , parent = None
                 , _o_focusColor = QtGui.QColor( 255, 0, 0 )
                 ):
        super( QArkPlotWidget, self ).__init__(parent)
        self.s_title = ''
        self.s_xLabel = ''
        self.s_yLabel = ''
        self.initUi()
        self.t_plots = []
        #self.t_indexFocusPlot = []
        self.o_focusColor = _o_focusColor

    def initUi( self ):
        """
        #"""
        pg.setConfigOption('background', 'w')
        pg.setConfigOption('foreground', 'k')
        self.setMinimumSize(100,100)
        o_layout = QtGui.QVBoxLayout(self)
        o_layout.setSpacing( 0 )
        o_layout.setMargin(0)
        self.o_viewBox = CustomViewBox()
        self.o_plotWidget = pg.PlotWidget( parent = self
                                           ,viewBox = self.o_viewBox
                                           )
        #self.o_plotWidget.plot( x=range(1000), y=range(1000) )
        o_layout.addWidget( self.o_plotWidget )
        self.setLayout( o_layout )

    def getTitle(self):
        return self.s_title
    
    def getXLabel(self):
        return self.s_xLabel
    
    def getYLabel(self):
        return self.s_yLabel

    def setTitle(self, _s_title):
        self.s_title = _s_title
        self.o_plotWidget.setTitle( _s_title )

    def setXLabel(self, _s_xLabel):
        self.s_xLabel = _s_xLabel
        self.o_plotWidget.setLabel('bottom', _s_xLabel)

    def setYLabel(self, _s_yLabel):
        self.s_yLabel = _s_yLabel
        self.o_plotWidget.setLabel('left', _s_yLabel)

    def clear(self):
        self.t_plots = []
        self.o_plotWidget.clear()

    def getIndexFromPlotableObject( self, _o_plotableObject ):
        try:
            return map( lambda p:p[0], self.t_plots ).index( _o_plotableObject )
        except:
            return -1

    def getPlotFromPlotableObject( self, _o_plotableObject ):
        try:
            u_idx = self.getIndexFromPlotableObject(_o_plotableObject)
            return self.t_plots[u_idx][1]
        except:
            return None

    def addPlotObject( self, _o_plotableObject ):
        """
        """
        t_x, t_y = _o_plotableObject.getData2D()
        
        if len(t_x) > 1:
            self.b_scatterPlot = False
            o_plot = self.o_plotWidget.plot( x=t_x
                                            , y=t_y
                                            , pen={'color': _o_plotableObject.getColor()
                                                   , 'width': _o_plotableObject.getPenWidth()
                                                   , 'style': _o_plotableObject.getLineStyle()
                                                   }
                                            )
        else:
            # scatter plot if len <= 1
            self.b_scatterPlot = True
            o_plot = self.o_plotWidget.plot( x=t_x
                                            , y=t_y
#                                             , symbolPen={'color': _o_plotableObject.getColor()
#                                                    , 'width': _o_plotableObject.getPenWidth()
#                                                    }
                                            , symbol = 'x'
                                            , symbolPen = {'color': _o_plotableObject.getColor() }
                                            , symbolBrush = pg.mkBrush( color = _o_plotableObject.getColor() ) #{'color': _o_plotableObject.getColor() }
                                            , symbolSize = _o_plotableObject.getPenWidth()
                                            , pxMode = True
                                            )
        o_plot.setZValue( 0 )
        self.t_plots.append( (_o_plotableObject, o_plot) )

    def removePlotObject( self, _o_plotableObject ):
        o_plot = self.getPlotFromPlotableObject( _o_plotableObject )
        self.o_plotWidget.removeItem( o_plot )
        self.t_plots.pop( self.getIndexFromPlotableObject( _o_plotableObject ) )

    def setPlotColor( self, _u_index, _o_color ):
        """
        """
        o_object, o_plot = self.t_plots[ _u_index ]
        if self.b_scatterPlot:
            o_plot.setSymbolPen( {'color': _o_color }  )
            o_plot.setSymbolBrush( pg.mkBrush( color = _o_color )  )
            o_plot.setSymbolSize( o_object.getPenWidth()  )
        else:
            o_plot.setPen( color = _o_color
                      , width = o_object.getPenWidth()
                      , style = o_object.getLineStyle()
                      )

    def setPlotZValue( self, _u_index, _u_value ):
        o_object, o_plot = self.t_plots[ _u_index ]
        o_plot.setZValue( _u_value )

    def updatePlotPen( self, _u_index ):
        """
        Update the plot to the original configuration
        as described in the plotObject
        """
        o_object, o_plot = self.t_plots[ _u_index ]
        if self.b_scatterPlot:
            o_plot.setSymbolPen( {'color': o_object.getColor() }  )
            o_plot.setSymbolBrush( pg.mkBrush( color = o_object.getColor() )  )
            o_plot.setSymbolSize( o_object.getPenWidth()  )
        else:
            o_plot.setPen( color = o_object.getColor()
                      , width = o_object.getPenWidth()
                      , style = o_object.getLineStyle()
                      )

    def updatePlotPenFromPlotObject( self, _o_plotableObject ):
        u_idx = self.getIndexFromPlotableObject(_o_plotableObject)
        if u_idx >= 0:
            self.updatePlotPen(u_idx)

    def setFocusPlot( self, _u_index ):
        """
        """
        o_object, o_plot = self.t_plots[ _u_index ]
        
        if self.b_scatterPlot:
            o_plot.setSymbolPen( {'color': self.o_focusColor }  )
            o_plot.setSymbolBrush( pg.mkBrush( color = self.o_focusColor )  )
            o_plot.setSymbolSize( o_object.getPenWidth()  )
        else:
            o_plot.setPen( color = self.o_focusColor
                      , width = o_object.getPenWidth()
                      , style = o_object.getLineStyle()
                      )
        o_plot.setZValue( 1 )

    def unsetFocusPlot( self, _u_index ):
        """
        """
        self.updatePlotPen( _u_index )
        self.setPlotZValue( _u_index, 0 )

    def setFocusPlotableObject( self, _o_plotableObject ):
        """
        """
        u_idx = self.getIndexFromPlotableObject( _o_plotableObject )
        self.setFocusPlot( u_idx )

    def unsetFocusPlotableObject( self, _o_plotableObject ):
        """
        """
        u_idx = self.getIndexFromPlotableObject( _o_plotableObject )
        self.unsetFocusPlot( u_idx )

    def savePlotToFile( self, _s_fileName, _u_width=256 ):
        """
        Save current scene to file
        """
        o_export = pg.exporters.ImageExporter.ImageExporter( self.o_plotWidget.getPlotItem() )
        o_export.parameters()['width'] = _u_width
        o_export.export( _s_fileName )

    def setXRange( self, _f_xmin, _f_xmax ):
        self.o_plotWidget.getViewBox().setXRange( _f_xmin, _f_xmax )

    def setYRange( self, _f_ymin, _f_ymax ):
        self.o_plotWidget.getViewBox().setYRange( _f_ymin, _f_ymax )

    def setRange( self, _f_xmin, _f_xmax, _f_ymin, _f_ymax ):
        self.o_plotWidget.getViewBox().setRange( rect=None
                                                ,xRange=(_f_xmin, _f_xmax)
                                                ,yRange=(_f_ymin, _f_ymax)
                                                )

    def getXRange( self ):
        return self.o_plotWidget.getViewBox().viewRange()[0]

    def getYRange( self ):
        return self.o_plotWidget.getViewBox().viewRange()[1]
