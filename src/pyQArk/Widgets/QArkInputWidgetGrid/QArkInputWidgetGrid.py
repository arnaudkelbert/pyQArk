# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets

class QArkInputWidgetGrid(QtWidgets.QWidget):

    def __init__(self
                 , parent
                 , _t_initTuple
                 ):
        """
        _t_initTuple : ( key, class<QArkInputWidget>, label, _x_initValue, **kwargs )
        """
        QtWidgets.QWidget.__init__(self, parent)
        self.t_initTuple = _t_initTuple
        self.t_widgets = {}
        self.initUi()

    def initUi(self):
        """
        """
        # First compute grid col size
        # Get widget col size
        u_gridColumnSize = max( map( lambda x:x[1].U_COLSIZE, self.t_initTuple ) )
        o_mainLayout = QtWidgets.QGridLayout(self)

        for u_widgetIdx, (s_key, cls_inputWidget, s_label, x_initValue, kwargs) in enumerate(self.t_initTuple):
            o_widget = cls_inputWidget( self, s_label, x_initValue, **kwargs )

            for u_idx in range( o_widget.U_COLSIZE ):
                # QGridLayout::addWidget ( QWidget * widget, int fromRow, int fromColumn, int rowSpan, int columnSpan, Qt::Alignment alignment = 0 )
                if u_idx == o_widget.U_COLSIZE - 1:
                    u_colSpan = u_gridColumnSize - o_widget.U_COLSIZE + 1
                else:
                    u_colSpan = 1
                o_mainLayout.addWidget( o_widget.getChildWidget(u_idx), u_widgetIdx, u_idx, 1, u_colSpan)

            self.t_widgets[ s_key ] = o_widget
        self.setLayout(o_mainLayout)

    def registerValues(self):
        """
        Check and save values into a dict
        """
        self.t_widgetsValues = {}
        
        for s_key, o_widget in self.t_widgets.items():
            try:
                self.t_widgetsValues[ s_key ] = o_widget.getValue()
            except Exception as e:
                o_errorbox = QtWidgets.QMessageBox( parent = self.parent() )
                o_errorbox.setText( 'Parameter value error' )
                o_errorbox.setStandardButtons( QtWidgets.QMessageBox.Ok )
                o_errorbox.setIcon( QtWidgets.QMessageBox.Critical )
                o_errorbox.setDetailedText( str(e) )
                o_errorbox.exec_()
                return False
        return True

    def getRegisteredValues(self):
        """
        Get widget values : can only be called after registerValues
        """
        return self.t_widgetsValues

    def setValues( self, _t_widgetsValues ):
        """
        Set widget values from the getRegisteredValues returned value
        ie a dictionnary (@see registerValues)
        """
        for s_key, o_widget in self.t_widgets.items():
            try:
                o_widget.setValue( _t_widgetsValues[s_key] )
            except Exception as e:
                o_errorbox = QtWidgets.QMessageBox( parent = self.parent() )
                o_errorbox.setText( 'Setting parameter value error' )
                o_errorbox.setStandardButtons( QtWidgets.QMessageBox.Ok )
                o_errorbox.setIcon( QtWidgets.QMessageBox.Critical )
                o_errorbox.setDetailedText( str(e) )
                o_errorbox.exec_()
                