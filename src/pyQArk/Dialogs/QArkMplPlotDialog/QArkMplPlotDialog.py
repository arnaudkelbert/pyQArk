# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
from pyQArk.Widgets.QArkMplPlotWidget.QArkMplPlotWidget import QArkMplPlotWidget

class QArkMplPlotDialog(QtWidgets.QDialog):
    
    def __init__(self, _s_id, *args, **kwargs):
        QtWidgets.QDialog.__init__(self, *args, **kwargs)
        self.s_id = _s_id
        self.initUi()
    
    def initUi(self):    
        o_layout = QtWidgets.QVBoxLayout(self)
        self.o_plotWidget = QArkMplPlotWidget(self)
        o_layout.addWidget(self.o_plotWidget)    
        self.setLayout(o_layout)
    
    def getPlotWidget(self):
        return self.o_plotWidget
