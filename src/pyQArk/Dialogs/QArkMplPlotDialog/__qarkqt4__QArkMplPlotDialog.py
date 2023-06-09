# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#
#
# QArkMplPlotDialog
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
from PyQt4 import QtGui
from pyQArk.Widgets.QArkMplPlotWidget.QArkMplPlotWidget import QArkMplPlotWidget

class QArkMplPlotDialog(QtGui.QDialog):
    
    def __init__(self, _s_id, *args, **kwargs):
        QtGui.QDialog.__init__(self, *args, **kwargs)
        self.s_id = _s_id
        self.initUi()
    
    def initUi(self):    
        o_layout = QtGui.QVBoxLayout(self)
        self.o_plotWidget = QArkMplPlotWidget(self)
        o_layout.addWidget(self.o_plotWidget)    
        self.setLayout(o_layout)
    
    def getPlotWidget(self):
        return self.o_plotWidget
