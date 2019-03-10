# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#
#
# QArk3DDataMplPlotter
#
#
# @author : Arnaud Kelbert
# @date : 2018/03/30
# @version : 0.1
#-----------------------------------------------------------------------
from PyQt4 import QtCore

import matplotlib
matplotlib.use('QT4Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from .QArkMplPlotter import QArkMplPlotter

class QArk3DDataMplPlotter( QArkMplPlotter ):

    dataChanged = QtCore.pyqtSignal()

    def __init__( self
                 , parent
                 ,_o_data
                 ,_s_title = None
                 ,_o_cmap = None
                 ,*args
                 ,**kwargs
                 ):
        QArkMplPlotter.__init__(self, parent, _o_data, *args, **kwargs)
        self.setColorMap(_o_cmap=_o_cmap)
        self.initData(_o_data=_o_data)
        if _s_title is None:
            self.s_title = ''
        else:
            self.s_title = _s_title

    def setData(self, _o_data, _b_emitDataChanged=True):
        self.o_data = _o_data
        self.initData(_o_data=self.o_data)
        if _b_emitDataChanged: self.dataChanged.emit()

    def setColorMap(self, _o_cmap):
        self.o_cmap = _o_cmap

    def initData(self, _o_data):
        try:
            self.t_x = _o_data[0]
            self.t_y = _o_data[1]
            self.t_z = _o_data[2]
        except:
            pass

    def plot(self):
        o_axe = self.initAxe( 111, QArkMplPlotter.VIEW_MODE__SCATTER_3D )
        self.o_figure.subplots_adjust(left=0.0, right=1.0, top=1.0, bottom=0.0)

        if not (self.t_x is None or self.t_y is None or self.t_z is None):
            t_kw = {}
            if not self.o_cmap is None:
                cm = plt.get_cmap(self.o_cmap)
                cNorm = matplotlib.colors.Normalize(vmin=min(self.t_z), vmax=max(self.t_z))
                scalarMap = matplotlib.cm.ScalarMappable(norm=cNorm, cmap=self.o_cmap)
                t_kw['c'] = scalarMap.to_rgba(self.t_z)

            o_axe.scatter( self.t_x
                         , self.t_y
                         , self.t_z
                         ,**t_kw
                         )
            o_axe.set_xlabel( 'X' )
            o_axe.set_ylabel( 'Y' )
            o_axe.set_zlabel( 'Z' )
            o_axe.set_title( self.s_title )
