# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
# 
#
# Widgets.QArkListWidgetNavigationWidget.QArkListWidgetNavigationWidget
# 
#
# @author : Arnaud Kelbert
# @date : 2019/03/19
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
from PyQt5 import QtCore, QtWidgets

from pyQArk.Core.QArkUiLoader import loadUi
from . import PKGPATH
Ui_QArkListWidgetNavigationWidget = loadUi(PKGPATH('./QArkListWidgetNavigationWidget.ui'), pkgname=__package__)

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

class SubWidget(QtWidgets.QWidget):
    
    def __init__(self,parent,wrappedWidget,*args,**kwargs):
        QtWidgets.QWidget.__init__(self, parent, *args, **kwargs)
        self.wrappedWidget = wrappedWidget
        self.initUi()
        
    def getWrappedWidget(self):
        return self.wrappedWidget
    
    def initUi(self):
        o_layout = QtWidgets.QVBoxLayout()
        o_layout.addWidget(self.wrappedWidget)
        o_layout.addStretch()
        self.setLayout(o_layout)

class QArkListWidgetNavigationWidget( QtWidgets.QWidget, Ui_QArkListWidgetNavigationWidget ):
    """
    """
    def __init__( self
                 , parent
                 , _t_widgets
                 ):
        """
        _t_widgets : list of tuple ('widgetLabel', o_widget) 
        """
        super( QArkListWidgetNavigationWidget, self).__init__( parent = parent )
        self.t_widgets = _t_widgets
        self.initUi()
        self.initConnection()
        self.setCurrentIndex(0)

    def initUi( self ):
        """
        @brief init user interface
        """
        self.ui = Ui_QArkListWidgetNavigationWidget()
        self.ui.setupUi(self)
        self.setObjectName( _fromUtf8("qArkListWidgetNavigationWidget") )
        self.setAttribute( QtCore.Qt.WA_DeleteOnClose )
        self.setLabel('')
        
        for s_widgetLabel, o_widget in self.t_widgets:
            self.ui.listWidget.addItem(s_widgetLabel)
            self.ui.stackedWidget.addWidget(SubWidget(self.ui.stackedWidget, o_widget))

    def initConnection( self ):
        """
        @brief init connection
        """
        self.ui.listWidget.currentRowChanged.connect( self.handleListWidgetCurrentRowChanged )

    def setLabel( self, _s_label ):
        self.ui.label.setText(_s_label)

    def getCurrentWidget(self):
        return self.ui.stackedWidget.currentWidget().getWrappedWidget()

    def setCurrentIndex(self, _u_index):
        self.ui.stackedWidget.currentWidget().setSizePolicy( QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored )
        self.ui.stackedWidget.setCurrentIndex(_u_index)
        self.ui.stackedWidget.currentWidget().setSizePolicy( QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding )
        self.ui.label.setText(self.t_widgets[_u_index][0])
    
    @QtCore.pyqtSlot(int)
    def handleListWidgetCurrentRowChanged(self, _u_index):
        self.setCurrentIndex(_u_index)

if __name__ == '__main__':
    o_app = QtWidgets.QApplication( sys.argv )
    o_w = QArkListWidgetNavigationWidget( parent = None
                                          , _t_widgets = [
                                                          ('label', QtWidgets.QLabel('testlabel'))
                                                         ,('lineedit', QtWidgets.QLineEdit('line edit'))
                                                          ]
                                         )
    o_w.show()

    sys.exit( o_app.exec_() )
