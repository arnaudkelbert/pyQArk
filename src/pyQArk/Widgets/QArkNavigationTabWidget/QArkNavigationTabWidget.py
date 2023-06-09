# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#
#
# QArkNavigationTabWidget
#
#
# @author : Arnaud Kelbert
# @date : 2014/07/26
# @version : 0.1
#-----------------------------------------------------------------------
import sys
import os

from PyQt4 import QtCore, QtGui

from .Ui_QArkNavigationTabWidget import Ui_QArkNavigationTabWidget


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




class QArkNavigationTabWidget( QtGui.QTabWidget, Ui_QArkNavigationTabWidget ):
    """
    Class to represents a navigation tab widget.
    Tabs can be TreeView or ListView
    """
    NAVIGATION_TREEVIEW = 0
    NAVIGATION_LISTVIEW = 1

    itemInsertedSignal = QtCore.pyqtSignal(object)

    # emit a selection change
    # params : view / selected / deselected
    selectionChanged = QtCore.pyqtSignal(object, object, object)


    def __init__( self
                 , parent = None
                 ):
        super( QArkNavigationTabWidget, self).__init__( parent = parent )

        self.initUi()
        self.initConnection()



    def initUi( self ):
        """
        @brief init user interface
        """
        self.ui = Ui_QArkNavigationTabWidget()
        self.ui.setupUi(self)

        self.setObjectName( _fromUtf8("qArkNavigationTabWidget") )
        self.setAttribute( QtCore.Qt.WA_DeleteOnClose )



    def initConnection( self ):
        """
        @brief init connection
        """
        pass




    def initSelectionChangedConnection( self, _u_index ):
        """
        Call this methode once the model is set
        """
        o_view = self.getNavigationTab(_u_index)

        if o_view.model():
            o_selectionModel = QtGui.QItemSelectionModel( o_view.model(), o_view )
            o_view.setSelectionModel(o_selectionModel)
            o_selectionModel.selectionChanged.connect( self.handleSelectionChanged )



    def addNavigationTab( self
                         , _u_type
                         , _s_label
                         , _o_model
                         , _b_hideHeader = True
                         , _b_enableContextMenu = False
                         , _b_enableSorting = False
                         ):
        """
        @brief add a navigationTab
        """
        if _u_type is self.__class__.NAVIGATION_TREEVIEW:

            # Create a treeview tab
            o_treeviewTab = QtGui.QTreeView(self)

            if not _o_model is None:
                o_treeviewTab.setModel( _o_model )
                _o_model.itemAddedSignal.connect( self.handleItemAddedSignal )
                _o_model.expandRequestSignal.connect( self.handleExpandRequestSlot )

            #setattr( self, 'tab{}'.format(self.count()), o_treeviewTab )
            self.addTab( o_treeviewTab, _s_label )

            if _b_hideHeader:
                o_treeviewTab.header().hide()

            if _b_enableContextMenu:
                o_treeviewTab.setContextMenuPolicy( QtCore.Qt.CustomContextMenu )
                o_treeviewTab.customContextMenuRequested.connect( self.handleContextMenuRequested )

            o_treeviewTab.setSortingEnabled(_b_enableSorting)

            self.initSelectionChangedConnection( self.count()-1 )


        elif _u_type is self.__class__.NAVIGATION_LISTVIEW:

            # Create a listview tab
            o_listviewTab = QtGui.QListView(self)

            if not _o_model is None:
                o_listviewTab.setModel( _o_model )
                _o_model.itemAddedSignal.connect( self.handleItemAddedSignal )

            #setattr( self, 'tab{}'.format(self.count()), o_listviewTab )
            self.addTab( o_listviewTab, _s_label )

            self.initSelectionChangedConnection( self.count()-1 )



    def getNavigationTab( self
                             , _u_index
                             ):
        """
        Return the view for a tab
        """
        assert( _u_index < self.count() )
        try:
            #return getattr( self, 'tab{}'.format(_u_index) )
            return self.widget( _u_index )
        except Exception as e:
            return None




    def getNavigationTabModel( self
                             , _u_index
                             ):
        """
        Return the view for a tab
        """
        assert( _u_index < self.count() )
        try:
            #return getattr( self, 'tab{}'.format(_u_index) )
            return self.getNavigationTab( _u_index ).model()

        except Exception as e:
            return None




    def sortNavigationTabModel( self
                               , _u_index
                               , _u_order
                               ):
        """
        """
        assert( _u_index < self.count() )
        try:
            self.getNavigationTabModel( _u_index ).sort(0, order=_u_order)

        except Exception as e:
            print e




    def setAcceptDrops(self, _u_index, _b_accept):
        assert( _u_index < self.count() )
        self.getNavigationTab(_u_index).setAcceptDrops(_b_accept)




    def getViewFromModel( self, _o_model ):
        for u_idx in xrange(self.count()):
            if self.getNavigationTab(u_idx).model() is _o_model:
                return self.getNavigationTab(u_idx)
        return None




    def getCurrentTabSelection( self ):
        o_currentView = self.getNavigationTab( self.currentIndex() )

        if not o_currentView.model() is None:
            return map( lambda idx : o_currentView.model().getItem( idx )
                    ,o_currentView.selectionModel().selectedIndexes()
                    )

        else:
            return []




    def getCurrentTabSelectionIndexes( self ):
        o_currentView = self.getNavigationTab( self.currentIndex() )

        if not o_currentView.model() is None:
            return o_currentView.selectionModel().selectedIndexes()

        else:
            return []




    def emitDataChangedCurrentTabSelection( self ):
        o_currentView = self.getNavigationTab( self.currentIndex() )

        if not o_currentView.model() is None:
            for o_index in o_currentView.selectionModel().selectedIndexes():
                o_currentView.model().dataChanged.emit(o_index, o_index)



    def emitDataChangedCurrentTab( self ):
        o_currentModel = self.getNavigationTabModel( self.currentIndex() )

        if not o_currentModel is None:
            o_currentModel.emitAllDataChanged()




    def getTabItems( self, _u_tabIndex ):
        o_view = self.getNavigationTab( _u_tabIndex )

        if not o_view.model() is None:
            return o_view.model().getItems()
        else:
            return []



    def getCurrentTabItems( self ):
        return self.getTabItems( self.currentIndex() )



    def getCurrentNavigationTabModel( self ):
        return self.getNavigationTabModel( self.currentIndex() )



#---------------------------------------------------------------
#
#  SLOTS
#
#---------------------------------------------------------------
    @QtCore.pyqtSlot(object)
    def handleItemAddedSignal( self, o_item ):
        """
        """
        #self.itemInsertedSignal.emit( o_item.getItemData() )
        self.itemInsertedSignal.emit( o_item )



    @QtCore.pyqtSlot(object)
    def handleExpandRequestSlot( self, _o_index ):
        """
        """
        o_view = self.getViewFromModel(self.sender())
        o_view.expand( _o_index )



    @QtCore.pyqtSlot(object)
    def handleSelectionChanged( self, selected, deselected ):
        # The sender is the selectionModel
        # we pass its parent corresponding to the view
        #print self.sender()
        #print self.sender().parent()
        self.selectionChanged.emit( self.sender().parent(), selected, deselected )



    @QtCore.pyqtSlot(object)
    def handleContextMenuRequested( self, _o_point ):
        """
        """
        o_view = self.sender()
        o_viewModel = o_view.model()
        o_selectionModel = o_view.selectionModel()

        o_index = o_view.indexAt(_o_point)
        o_item = o_viewModel.getItem( o_index )

        o_data = o_item.getItemData()
        print o_data
        print o_selectionModel.selectedIndexes()

        #for o_index in o_currentView.selectionModel().selectedIndexes()



