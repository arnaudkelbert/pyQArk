# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#
#
# QArkTreeView
#
#
# @author : Arnaud Kelbert
# @date : 2014/08/01
# @version : 0.1
#-----------------------------------------------------------------------
from PyQt4 import QtCore, QtGui


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




class QArkTreeView( QtGui.QTreeView ):
    """
    """
    selectionChangedSignal = QtCore.pyqtSignal( object, object )


    def __init__( self, *args, **kwargs ):
        super( QArkTreeView, self).__init__( *args, **kwargs )

        self.b_enableContextMenu = False




    def __initContextMenu( self, _x_handleFunction = None ):
        self.setContextMenuPolicy( QtCore.Qt.CustomContextMenu )

        if _x_handleFunction is None:
            self.customContextMenuRequested.connect( self.handleContextMenuRequested )

        else:
            self.customContextMenuRequested.connect( _x_handleFunction )

        self.t_contextMenuActions = []
        #self.t_contextMenuActionGroups = []



    def setExtendedSelectionMode( self ):
        self.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)



    def setSingleSelectionMode( self ):
        self.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)



    def setEnableContextMenu( self, _b_enable ):
        self.b_enableContextMenu = _b_enable



    def enableContextMenu( self, _x_handleFunction = None ):
        self.setEnableContextMenu( True )

        self.__initContextMenu(_x_handleFunction)



    def appendContextMenuSlot( self
                              , _s_id
                              , _s_label
                              , _fct_slot
                              , _b_uniqueSelectionEnabled
                              , _b_multiSelectionEnabled
                              ):
        """
        """
        if _s_id == 'SEPARATOR':
            self.t_contextMenuActions.append( ('SEPARATOR',None, None, None) )

        else:
            o_action = QtGui.QAction( _s_label
                                 , self
                                 , triggered = _fct_slot
                                 )

            self.t_contextMenuActions.append( (_s_id, o_action, _b_uniqueSelectionEnabled, _b_multiSelectionEnabled) )


    #def createContextMenuActionGroup( self, _s_actionGroupId, _t_listId ):
        #"""
        #"""
        #t_listAction = []

        #o_actionGroup = QtGui.QActionGroup( self )

        #for s_actionId, o_action, b_uniqueEnable, b_multiEnable in self.t_contextMenuActions:
            #if s_actionId in _t_listId:
                #o_actionGroup.addAction(


        #self.t_contextMenuActionGroups.append( (_s_actionGroupId, o_actionGroup) )


    def getSelection( self ):
        o_selectionModel = self.selectionModel()

        t_uniqueRowIndexes = dict( (o_index.row(), o_index)
                                   for o_index in o_selectionModel.selectedIndexes()
                                   ).values()

        return map( lambda o_index:self.model().getItem(o_index)
                   , t_uniqueRowIndexes
                   )



    def getSelectionIndexes( self ):
        return self.selectionModel().selectedIndexes()




    def getSelectionData( self ):
        return map( lambda o_item:o_item.getItemData()
                   , self.getSelection()
                   )




    def __createContextMenu( self, _o_index ):
        """
        """
        t_selectedItemData = self.getSelectionData()

        o_menu = QtGui.QMenu( self )

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
        o_selectionModel = QtGui.QItemSelectionModel( self.model()
                                                     , self
                                                     )

        self.setSelectionModel(o_selectionModel)

        o_selectionModel.selectionChanged.connect( self.handleSelectionChanged )



    def setModel( self, *args, **kwargs ):
        super( QArkTreeView, self).setModel( *args, **kwargs )
        if not self.model() is None:
            self.model().expandRequestSignal.connect( self.handleExpandViewRequested )





    @QtCore.pyqtSlot( object, object )
    def handleSelectionChanged( self, selected, deselected ):
        self.selectionChangedSignal.emit( selected, deselected )





    @QtCore.pyqtSlot(object)
    def handleContextMenuRequested( self, _o_point ):
        """
        """
        o_menu = self.__createContextMenu( self.indexAt(_o_point) )

        if not o_menu is None:
            o_menu.exec_( QtGui.QCursor.pos() )



    @QtCore.pyqtSlot(object)
    def handleExpandViewRequested( self, _o_index ):
        self.expand( _o_index )


