# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
# 
#
# Widgets.QArkListWidgetNavigationWidget.QArkListWidgetNavigationWidget
# 
#
# @author : Arnaud Kelbert
# @date : Nov 22, 2014
# @version : 0.1
#-----------------------------------------------------------------------
import sys
import os

from PyQt4 import QtCore, QtGui

from Ui_QArkListWidgetNavigationWidget import Ui_QArkListWidgetNavigationWidget


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


class SubWidget(QtGui.QWidget):
    
    def __init__(self,parent,wrappedWidget,*args,**kwargs):
        QtGui.QWidget.__init__(self, parent, *args, **kwargs)
        self.wrappedWidget = wrappedWidget
        self.initUi()
        
    def getWrappedWidget(self):
        return self.wrappedWidget
    
    def initUi(self):
        o_layout = QtGui.QVBoxLayout()
        o_layout.addWidget(self.wrappedWidget)
        o_layout.addStretch()
        self.setLayout(o_layout)


class QArkListWidgetNavigationWidget( QtGui.QWidget, Ui_QArkListWidgetNavigationWidget ):
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
        self.ui.stackedWidget.currentWidget().setSizePolicy( QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored )
        
        self.ui.stackedWidget.setCurrentIndex(_u_index)
        self.ui.stackedWidget.currentWidget().setSizePolicy( QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding )
        
        self.ui.label.setText(self.t_widgets[_u_index][0])
        
        #self.ui.stackedWidget.adjustSize()
    
    
    @QtCore.pyqtSlot(object)
    def handleListWidgetCurrentRowChanged(self, _u_index):
        self.setCurrentIndex(_u_index)







if __name__ == '__main__':
    o_app = QtGui.QApplication( sys.argv )
    o_w = QArkListWidgetNavigationWidget( parent = None
                                          , _t_widgets = [
                                                          ('label', QtGui.QLabel('testlabel'))
                                                         ,('lineedit', QtGui.QLineEdit('line edit'))
                                                          ]
                                         )
    o_w.show()

    sys.exit( o_app.exec_() )
