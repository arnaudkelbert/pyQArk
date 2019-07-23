# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#
#
# QArkMplPlotter
#
#
# @author : Arnaud Kelbert
# @date : 2019/07/23
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
from PyQt5 import QtCore

import matplotlib
matplotlib.use('QT5Agg')
import matplotlib.pyplot as plt

class QArkMplPlotter( QtCore.QObject ):
    """
    Plot interface

    G{classtree}
    """
    VIEW_MODE__PLOT = 1
    VIEW_MODE__IMAGESHOW = 2
    VIEW_MODE__MATRIXSHOW = 4
    VIEW_MODE__WIREFRAME = 8
    VIEW_MODE__SURFACE = 16
    VIEW_MODE__COLORMESH = 32
    VIEW_MODE__SCATTER_3D = 64

    U_MAX_PLOT_ROW = 4

    def __init__(self
                 , parent
                 ,_o_data
                 , *args
                 , **kwargs
                 ):
        """
        Constructeur
        @param _o_data donnee
        @type L{TngData}
        """
        QtCore.QObject.__init__(self, parent)
        self.o_data = _o_data
        self.t_axes = {}
        self._t_args = args
        self._t_kwargs = kwargs

    def plot(self, **kwargs):
        raise NotImplemented

    def setFigure(self, _o_figure):
        self.o_figure = _o_figure

    def initAxe(self, _u_c, _u_mode, **kwargs ):
        if _u_mode is self.__class__.VIEW_MODE__PLOT:
            self.t_axes[_u_c] = self.o_figure.add_subplot(_u_c, **kwargs)
        elif _u_mode is self.__class__.VIEW_MODE__IMAGESHOW:
            self.t_axes[_u_c] = self.o_figure.add_subplot(_u_c, **kwargs)
        elif _u_mode is self.__class__.VIEW_MODE__MATRIXSHOW:
            self.t_axes[_u_c] = self.o_figure.add_subplot(_u_c, **kwargs)
        elif _u_mode is self.__class__.VIEW_MODE__WIREFRAME:
            self.t_axes[_u_c] = self.o_figure.add_subplot(_u_c, projection='3d', **kwargs)
        elif _u_mode is self.__class__.VIEW_MODE__SURFACE:
            self.t_axes[_u_c] = self.o_figure.add_subplot(_u_c, projection='3d', **kwargs)
        elif _u_mode is self.__class__.VIEW_MODE__COLORMESH:
            self.t_axes[_u_c] = self.o_figure.add_subplot(_u_c, **kwargs)
        elif _u_mode is self.__class__.VIEW_MODE__SCATTER_3D:
            self.t_axes[_u_c] = self.o_figure.add_subplot(_u_c, projection='3d', **kwargs)
        return self.t_axes[_u_c]

    @classmethod
    def getSubPlotTuple( cls, _u_plotIdx, _u_nbPlots):
        if _u_nbPlots <= cls.U_MAX_PLOT_ROW:
            return 1, _u_nbPlots, _u_plotIdx
        u_nbLines = _u_nbPlots // cls.U_MAX_PLOT_ROW
        if _u_nbPlots % cls.U_MAX_PLOT_ROW > 0:
            u_nbLines += 1
        return u_nbLines, cls.U_MAX_PLOT_ROW, _u_plotIdx

    def plotToFile( self, _s_fileOut, _u_dpi = 70, **kwargs ):
        o_figure = plt.figure()
        self.setFigure( o_figure )
        self.plot( **kwargs )
        o_figure.savefig( _s_fileOut, dpi=_u_dpi)
        plt.close(o_figure)

