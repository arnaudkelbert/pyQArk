# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets

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

from pyQArk.Core import QArkQt

class QArkTableView(QtWidgets.QTableView):
    """
    """
    selectionChangedSignal = QtCore.pyqtSignal( object, object )

    def __init__( self, *args, **kwargs ):
        super(QArkTableView, self).__init__( *args, **kwargs )
        self.b_enableContextMenu = False

    def __initContextMenu( self ):
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect( self.handleContextMenuRequested )
        self.t_contextMenuActions = []

    def setExtendedSelectionMode( self ):
        self.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)

    def setEnableContextMenu( self, _b_enable ):
        self.b_enableContextMenu = _b_enable

    def enableContextMenu( self ):
        self.setEnableContextMenu( True )
        self.__initContextMenu()

    def appendContextMenuSlot( self
                              , _s_id
                              , _s_label
                              , _fct_slot
                              , _b_uniqueSelectionEnabled
                              , _b_multiSelectionEnabled
                              ):
        """
        """
        o_action = QtWidgets.QAction( _s_label
                                 , self
                                 , triggered = _fct_slot
                                 )
        self.t_contextMenuActions.append( (_s_id, o_action, _b_uniqueSelectionEnabled, _b_multiSelectionEnabled) )

    def getSelection( self ):
        o_selectionModel = self.selectionModel()
        t_uniqueRowIndexes = dict( (o_index.row(), o_index)
                                   for o_index in o_selectionModel.selectedIndexes()
                                   ).values()

        return [self.model().getItem(o_index) for o_index in t_uniqueRowIndexes]

    def getSelectionData( self ):
        return [o_item.getItemData() for o_item in self.getSelection()]

    def __createContextMenu( self, _o_index ):
        """
        """
        t_selectedItemData = self.getSelectionData()
        o_menu = QtWidgets.QMenu(self)
        for s_actionId, o_action, b_uniqueEnable, b_multiEnable in self.t_contextMenuActions:
            o_menu.addAction( o_action )
            if len(t_selectedItemData) == 1:
                if b_uniqueEnable:
                    o_action.setEnabled(True)
                else:
                    o_action.setEnabled(False)
            elif len(t_selectedItemData) > 1:
                if b_multiEnable:
                    o_action.setEnabled(True)
                else:
                    o_action.setEnabled(False)
            else:
                o_action.setEnabled(False)
        return o_menu

    def initSelectionModel( self ):
        o_selectionModel = QtCore.QItemSelectionModel(self.model(), self)
        self.setSelectionModel(o_selectionModel)
        o_selectionModel.selectionChanged.connect(self.handleSelectionChanged)

    @QtCore.pyqtSlot( object, object )
    def handleSelectionChanged( self, selected, deselected ):
        self.selectionChangedSignal.emit( selected, deselected )

    @QtCore.pyqtSlot(object)
    def handleContextMenuRequested( self, _o_point ):
        """
        """
        o_menu = self.__createContextMenu( self.indexAt(_o_point) )
        if not o_menu is None:
            QArkQt._exec(o_menu, QtGui.QCursor.pos())




