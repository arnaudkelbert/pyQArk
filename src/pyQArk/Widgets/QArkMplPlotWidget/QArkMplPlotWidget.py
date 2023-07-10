# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)

import matplotlib
matplotlib.use('QT5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
try:
    from matplotlib.backends.backend_qt5agg import NavigationToolbar2QTAgg as NavigationToolbar
except ImportError:
    from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
try:
    # This line was first commented
    from mpl_toolkits.mplot3d import axes3d
except:
    pass
try:
    from mpl_toolkits.mplot3d import Axes3D
except:
    pass

import matplotlib.pyplot as plt
matplotlib.rcParams[ 'font.size' ] = 9
matplotlib.rcParams[ 'font.family' ] = 'serif'
matplotlib.rcParams[ 'axes.labelsize' ] = 9
matplotlib.rcParams[ 'axes.titlesize' ] = 9
matplotlib.rcParams[ 'legend.fontsize' ] = 8

class QArkMplPlotWidget(QtWidgets.QWidget):
    """
    """
    VIEW_MODE__PLOT = 1
    VIEW_MODE__IMAGESHOW = 2
    VIEW_MODE__MATRIXSHOW = 4
    VIEW_MODE__WIREFRAME = 8
    VIEW_MODE__SURFACE = 16
    VIEW_MODE__COLORMESH = 32

    def __init__( self
                 , parent=None
                 ):
        """
        """
        super(QArkMplPlotWidget, self).__init__(parent = parent)
        self.initUi()
        self.initConnection()
        self.t_axes = {}

    def initUi(self):
        """
        """
        self.setObjectName(_fromUtf8("qArkMplPlotWidget"))
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        vbox = QtWidgets.QVBoxLayout()

        #--------------------------------------------------------------------------------
        # Plot zone
        #--------------------------------------------------------------------------------
        self.dpi = 70
        #self.figure = plt.Figure((10.0, 10.0), dpi=self.dpi)
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        print(self)
        self.canvas.setParent(self)
        self.mpl_toolbar = NavigationToolbar(self.canvas, self)
        vbox.addWidget(self.canvas)
        vbox.addWidget(self.mpl_toolbar)
        self.setLayout(vbox)

    def initConnection( self ):
        """
        """
        pass

    def initAxe(self, _u_c, _u_mode ):
        if _u_mode is self.__class__.VIEW_MODE__PLOT:
            self.t_axes[_u_c] = self.fig.add_subplot(_u_c)
        elif _u_mode is self.__class__.VIEW_MODE__IMAGESHOW:
            self.t_axes[_u_c] = self.fig.add_subplot(_u_c)
        elif _u_mode is self.__class__.VIEW_MODE__MATRIXSHOW:
            self.t_axes[_u_c] = self.fig.add_subplot(_u_c)
        elif _u_mode is self.__class__.VIEW_MODE__WIREFRAME:
            self.t_axes[_u_c] = self.fig.add_subplot(_u_c, projection='3d')
        elif _u_mode is self.__class__.VIEW_MODE__SURFACE:
            self.t_axes[_u_c] = self.fig.add_subplot(_u_c, projection='3d')
        elif _u_mode is self.__class__.VIEW_MODE__COLORMESH:
            self.t_axes[_u_c] = self.fig.add_subplot(_u_c)
        return self.t_axes[_u_c]

    def enableCurrentFigure(self):
        plt.figure( self.figure.number )

    def displayPlot(self):
        self.canvas.draw()

    def savePlot(self, _s_filename):
        self.canvas.print_figure(_s_filename)

    def setPlotter(self, _o_plotter):
        self.o_plotter = _o_plotter
        self.enableCurrentFigure()
        self.o_plotter.setFigure(self.figure)
        self.o_plotter.plot()
        self.displayPlot()

    @QtCore.pyqtSlot()
    def updatePlot(self):
        self.o_plotter.plot()
        self.displayPlot()
