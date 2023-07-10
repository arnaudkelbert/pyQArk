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

from pyQArk.Widgets.QArkInputWidget.QArkInputWidget import QArkInputWidget

class QArkInputListWidget(QArkInputWidget):
    """
    Dynamic input widget list of a given QArkInputWidget class
    """
    U_COLSIZE = 1
    
    def __init__(self
                 , parent
                 , _s_labelPrefix
                 , _x_defaultValue
                 , _cls_inputWidgetClass
                 , _u_size = 1
                 , **kwargs
                 ):
        """
        @param _cls_inputWidgetClass : class for input widget
        @type _cls_inputWidgetClass : L{class}
        @param _s_labelPrefix : default prefix for input widget label
        @type _s_labelPrefix : L{str}
        @param _x_defaultValue : default value for input widget
        @type _x_defaultValue : L{instance}
        @param _u_size : init size
        @type _u_size : L{class}
        """
        self.cls_inputWidgetClass = _cls_inputWidgetClass
        self.u_size = _u_size
        self.t_widgets = []
        self.t_kwargs = kwargs
        self.b_useScrollArea = False
        QArkInputWidget.__init__(self, parent, _s_labelPrefix, _x_defaultValue, **kwargs)

    def initUi(self,_s_labelPrefix, _x_defaultValue):
        self.s_labelPrefix = _s_labelPrefix
        self.x_defaultValue = _x_defaultValue
        
        if self.b_useScrollArea:
            self.o_scrollArea = QtWidgets.QScrollArea()
        
        self.o_widget = QtWidgets.QWidget(self)
        self.o_vLayout = QtWidgets.QVBoxLayout(self)
        self.o_gridLayout = QtWidgets.QGridLayout()
        
        u_initSize = self.u_size
        for _ in range(u_initSize):
            self.addInputWidget()

        self.o_vLayout.addChildLayout(self.o_gridLayout)
        self.o_vLayout.addItem(self.o_gridLayout)
        o_hLayout = QtWidgets.QHBoxLayout()
        self.o_addWidgetPushButton = QtWidgets.QPushButton(' + ')
        o_hLayout.addWidget(self.o_addWidgetPushButton)
        o_hLayout.addStretch()
        self.o_vLayout.addItem(o_hLayout)
        self.o_widget.setLayout(self.o_vLayout)
        
        if self.b_useScrollArea:
            self.o_scrollArea.setWidgetResizable(True)
            self.o_scrollArea.setWidget( self.o_widget )
            self.o_scrollArea.setSizePolicy(QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Expanding )

    def addInputWidget(self):
        u_widgetIndex = self.o_gridLayout.rowCount()
        o_widget = self.cls_inputWidgetClass( self
                                        , '{0}_{1:d}'.format( self.s_labelPrefix, u_widgetIndex )
                                        , self.x_defaultValue
                                        , **self.t_kwargs
                                        )
        self.t_widgets.append( o_widget )
            
        # Set grid layout
        for u_childWidgetIdx in range( o_widget.U_COLSIZE ):
               
            self.o_gridLayout.addWidget( o_widget.getChildWidget(u_childWidgetIdx)
                                         , u_widgetIndex
                                         , u_childWidgetIdx
                                         , 1
                                         , 1
                                         )
            
        # Add a del button and connect it
        o_delButton = QtWidgets.QToolButton(self)
        o_delButton.setText('-')
        o_delButton.clicked.connect( self.handleDeleteButtonClicked )
        self.o_gridLayout.addWidget( o_delButton
                                         , u_widgetIndex
                                         , u_childWidgetIdx + 1
                                         , 1
                                         , 1
                                         )
        self.u_size = len(self.t_widgets)

    def initConnection(self):
        self.o_addWidgetPushButton.clicked.connect( self.handleAddWidgetClicked )

    def getChildWidget(self, _u_index):
        if _u_index == 0:
            if self.b_useScrollArea:
                return self.o_scrollArea
            else:
                return self.o_widget
        else:
            return QtCore.QVariant()

    def getValue(self):
        return [o_widget.getValue() for o_widget in self.t_widgets]

    def setValue( self, *args, **kwargs ):
        """
        Sets the widget value from the value returned by getValue()
        args[0] contains the retur of getValue fonction
        """
        for o_widget, x_value in zip( self.t_widgets, args[0] ):
            o_widget.setValue( x_value )

    @QtCore.pyqtSlot()
    def handleAddWidgetClicked(self):
        self.addInputWidget()

    @QtCore.pyqtSlot()
    def handleDeleteButtonClicked(self):
        o_delButton = self.sender()
        o_index = self.o_gridLayout.indexOf(o_delButton)
        u_row, u_column, u_colspan, u_rowspan = self.o_gridLayout.getItemPosition(o_index)
        
        # Lets get the parent QArkInputWidget
        # (calling parent does not work)
        o_childWidget0 = self.o_gridLayout.itemAtPosition(u_row, 0).widget()
        o_widget = None
                
        for o_w in self.t_widgets:
            if o_childWidget0 is o_w.getChildWidget(0):
                o_widget = o_w
        
        if not o_widget is None:
            u_index = self.t_widgets.index(o_widget)
            self.t_widgets.pop(u_index)
        
        for u_colIdx in range(self.o_gridLayout.columnCount()):
            o_colWidget = self.o_gridLayout.itemAtPosition( u_row, u_colIdx ).widget()
            
            if o_colWidget:
                self.o_gridLayout.removeWidget(o_colWidget)
                o_colWidget.deleteLater()
        
        o_delButton.deleteLater()
        if o_widget:
            o_widget.deleteLater()
