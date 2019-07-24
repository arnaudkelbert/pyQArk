# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#
#
# QArkNavigationPlotWidget
#
#
# @author : Arnaud Kelbert
# @date : 2019/07/24
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
from PyQt5 import QtCore, QtGui, QtWidgets

#from pyQArk.Core.QArkUiLoader import loadUi
#from . import PKGPATH
#Ui_QArkNavigationPlotWidget = loadUi(PKGPATH('./QArkNavigationPlotWidget.ui'), pkgname=__package__)

from pyQArk.Widgets.QArkNavigationTabWidget.QArkNavigationTabWidget import QArkNavigationTabWidget
try:
    from pyQArk.Widgets.QArkPlotWidget.QArkPlotWidget import QArkPlotWidget
except ImportError as e:
    print('Exception : ')
    print(str(e))
    print('Continue...')
from pyQArk.Dialogs.QArkExportPlotWidgetDialog.QArkExportPlotWidgetDialog import QArkExportPlotWidgetDialog
from pyQArk.Dialogs.QArkSetAxisRangePlotWidgetDialog.QArkSetAxisRangePlotWidgetDialog import QArkSetAxisRangePlotWidgetDialog
from pyQArk.Dialogs.QArkSetNotationPlotWidgetDialog.QArkSetNotationPlotWidgetDialog import QArkSetNotationPlotWidgetDialog
from pyQArk.Widgets.QArkPlotPenSettingsWidget.QArkPlotPenSettingsWidget import QArkPlotPenSettingsWidget
from pyQArk.Core.QArkPlotableObject import QArkPlotableObject

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

class QArkNavigationPlotWidget( QtWidgets.QWidget ):
    """
    Class to represents a navigation plot widget.
    """

    def __init__( self
                 , parent = None
                 ):
        super( QArkNavigationPlotWidget, self).__init__( parent = parent )
        self.initUi()
        self.initConnection()
        self.t_plotObjects = []

    def initUi( self ):
        """
        @brief init user interface
        """
        self.resize( 600, 480 )
        self.setObjectName( _fromUtf8("qArkNavigationPlotWidget") )
        self.setAttribute( QtCore.Qt.WA_DeleteOnClose )
        o_layout = QtWidgets.QVBoxLayout(self)
        o_layout.setSpacing( 0 )
        o_layout.setMargin(0)
        self.ui_navigationTabWidget = QArkNavigationTabWidget( self )
        self.ui_plotWidget = QArkPlotWidget( self )
        self.ui_penSettingsWidget = QArkPlotPenSettingsWidget( self )
        self.ui_qSplitterV = QtWidgets.QSplitter( self )
        self.ui_qSplitterV.setOrientation( QtCore.Qt.Vertical )
        self.ui_qSplitterV.addWidget( self.ui_navigationTabWidget )
        self.ui_qSplitterV.addWidget( self.ui_penSettingsWidget )
        self.ui_qSplitterV.setStretchFactor( 0, 1 )
        self.ui_qSplitterV.setStretchFactor( 1, 0 )
        self.ui_qSplitterH = QtWidgets.QSplitter( self )
        self.ui_qSplitterH.setOrientation( QtCore.Qt.Horizontal )
        self.ui_qSplitterH.addWidget( self.ui_plotWidget )
        self.ui_qSplitterH.addWidget( self.ui_qSplitterV )
        self.ui_qSplitterH.setStretchFactor( 0, 1 )
        self.ui_qSplitterH.setStretchFactor( 1, 0 )
        o_layout.addWidget( self.ui_qSplitterH )
        self.setLayout( o_layout )

        # Adjust sizes
        u_navigationTabWidgetWidth = 200
        self.ui_qSplitterH.setSizes( [ self.geometry().width() - u_navigationTabWidgetWidth
                                      ,u_navigationTabWidgetWidth
                                      ]
                                      )
        self.ui_penSettingsWidget.setEnabled(False)

    def initConnection( self ):
        # Connect the tab widget to the plot request slot
        self.ui_navigationTabWidget.itemInsertedSignal.connect( self.handleItemInsertedSlot )
        # Set the connection for selection changed
        self.ui_navigationTabWidget.selectionChanged.connect( self.handleSelectionChangedSlot )
        # Tab changed
        self.ui_navigationTabWidget.currentChanged.connect( self.handleNavigationTabChangedSlot )
        self.ui_penSettingsWidget.applyClicked.connect( self.handleApplyPenSettingsSlot )

    def getPlotObjects( self ):
        return self.t_plotObjects

    def refresh(self):
        """
        Clear plot and reloadad
        """
        t_plotObjects = self.t_plotObjects
        self.t_plotObjects = []
        self.ui_plotWidget.clear()

        for o_object in t_plotObjects:
            self.addPlot( o_object, _b_setConnection=False )

    def addTab( self, _o_tab, _s_label ):
        """
        """
        self.ui_navigationTabWidget.addTab( _o_tab, _s_label )

    def addNavigationTab( self
                         , _u_type
                         , _s_label
                         , _o_model
                         , _b_hideHeader = True
                         ):
        """
        """
        self.ui_navigationTabWidget.addNavigationTab( _u_type
                                                     , _s_label
                                                     , _o_model
                                                     , _b_hideHeader
                                                     )

    def getNavigationTab( self, _u_index ):
        return self.ui_navigationTabWidget.getNavigationTab(_u_index)

    def getNavigationTabModel( self, _u_index ):
        return self.ui_navigationTabWidget.getNavigationTabModel(_u_index)

    def setAcceptDrops( self, _u_index, _b_accept ):
        # TODO : parent class signature is setAcceptDrops(bool)
        self.ui_navigationTabWidget.setAcceptDrops( _u_index, _b_accept )

    def getCurrentNavigationTabModel( self ):
        return self.ui_navigationTabWidget.getCurrentNavigationTabModel()

    def checkPlots( self ):
        """
        """
        print('checkPlots')

    def addPlotToDisplay( self, _o_item ):
        """
        """
        self.ui_plotWidget.addPlotObject(_o_item)

    def removePlotFromDisplay( self, _o_item ):
        """
        """
        self.ui_plotWidget.removePlotObject(_o_item)

    def addPlot( self, _o_item, _b_setConnection=True ):
        """
        """
        print( 'addPlot %s' % _o_item )
        self.t_plotObjects.append( _o_item )
        if _o_item.getToDisplay():
            self.addPlotToDisplay(_o_item)
        if _b_setConnection:
            _o_item.toDisplayChangedSignal.connect( self.handleToDisplayChangedSlot )
            _o_item.valueChangedSignal.connect( self.handleValueChangedSlot )

    def enablePenSettings( self, _o_plotableObject ):
        """
        """
        self.ui_penSettingsWidget.setEnabled(True)
        self.ui_penSettingsWidget.setSettingsFromObject( _o_plotableObject )

    def disablePenSettings( self ):
        self.ui_penSettingsWidget.setEnabled(False)

    def getPlotableObjectSelection( self ):
        """
        Returns all of selected plotable items data
        """
        # get current tab selection
        t_selectedItems = self.ui_navigationTabWidget.getCurrentTabSelection()
        t_plotableItems = []
        for o_item in t_selectedItems:
            o_item.getListOfItemDataIsInstance( QArkPlotableObject, t_plotableItems)
        # Ensure uniqueness
        t_plotableItems = list( set(t_plotableItems) )
        return [o_item.getItemData() for o_item in t_plotableItems]

    def getCurrentTabPlotableItems( self ):
        t_plotableItems = []
        try:
            o_rootItem = self.ui_navigationTabWidget.getCurrentNavigationTabModel().getRootItem()
            o_rootItem.getListOfItemDataIsInstance( QArkPlotableObject, t_plotableItems)
        except:
            pass
        finally:
            return t_plotableItems

    def resetCurrentTabToDefault( self ):
        """
        Reset all plots to default color, pen, line style, lissage
        """
        for o_item in self.getCurrentTabPlotableItems():
            o_item.getItemData().resetToDefault()

        self.refresh()
        self.ui_navigationTabWidget.emitDataChangedCurrentTab()

    def applyPenSettings( self ):
        o_color = self.ui_penSettingsWidget.getColor()
        u_lineWidth = self.ui_penSettingsWidget.getLineWidth()
        u_lineStyle = self.ui_penSettingsWidget.getLineStyle()
        t_plotableData = self.getPlotableObjectSelection()
        for o_data in t_plotableData:
            o_data.setColor( o_color )
            o_data.setPenWidth( u_lineWidth )
            o_data.setLineStyle( u_lineStyle )
            self.ui_plotWidget.updatePlotPenFromPlotObject( o_data )
        self.ui_navigationTabWidget.emitDataChangedCurrentTabSelection()

    def updatePenSettings( self ):
        """
        Get current selection and update pen settings according to
        the selected items.
        """
        t_plotableData = self.getPlotableObjectSelection()
        # Return if no item
        if len(t_plotableData) == 0:
            self.disablePenSettings()
            return
        # Set the pen settings according to the first item existing
        # settings in list.
        self.enablePenSettings( t_plotableData[0] )

    def savePlotToFile( self, _s_filename, _u_width=256 ):
        self.ui_plotWidget.savePlotToFile( _s_filename, _u_width )

    def openSavePlotToFileDialog(self):
        """
        Open a dialog to save the current plotItem
        """
        o_dialog = QArkExportPlotWidgetDialog( parent = self
                                              , _s_directory = None
                                              )
        if o_dialog.exec_() == QtWidgets.QDialog.Accepted:
            s_filename = o_dialog.getFilename()
            u_width = o_dialog.getWidth()
            self.ui_plotWidget.savePlotToFile( s_filename, u_width )

    def openSetAxisRangeDialog(self):
        """
        Open a dialog to set axis range for the current scene
        """
        o_dialog = QArkSetAxisRangePlotWidgetDialog( parent = self
                                                    , _o_plotWidget = self.ui_plotWidget
                                                    )
        if o_dialog.exec_() == QtWidgets.QDialog.Accepted:
            f_xmin, f_xmax, f_ymin, f_ymax = o_dialog.getRange()
            self.ui_plotWidget.setRange( f_xmin, f_xmax, f_ymin, f_ymax )

    def openSetNotationDialog(self):
        """
        Open a dialog to set title and axis labels
        """
        o_dialog = QArkSetNotationPlotWidgetDialog( parent = self
                                                    , _o_plotWidget = self.ui_plotWidget
                                                    )
        if o_dialog.exec_() == QtWidgets.QDialog.Accepted:
            s_title = o_dialog.getTitle()
            s_xLabel = o_dialog.getXLabel()
            s_yLabel = o_dialog.getYLabel()
            self.ui_plotWidget.setTitle(s_title)
            self.ui_plotWidget.setXLabel(s_xLabel)
            self.ui_plotWidget.setYLabel(s_yLabel)

    def replotPlotObject( self, _o_plotObject ):
        """
        Fonction d'actualisation du trace d'un objet
        """
        self.removePlotFromDisplay( _o_plotObject )
        self.addPlotToDisplay( _o_plotObject )

    @QtCore.pyqtSlot()
    def handleApplyPenSettingsSlot( self ):
        #self.updatePenSettings()
        self.applyPenSettings()

    @QtCore.pyqtSlot(object)
    def handleToDisplayChangedSlot( self, _b_display ):
        o_plotObject = self.sender()
        if _b_display:
            self.addPlotToDisplay( o_plotObject )
        else:
            self.removePlotFromDisplay( o_plotObject )
        self.ui_navigationTabWidget.getCurrentNavigationTabModel().dataChanged.emit( QtCore.QModelIndex(), QtCore.QModelIndex())

    @QtCore.pyqtSlot()
    def handleValueChangedSlot(self):
        o_plotObject = self.sender()
        self.replotPlotObject( o_plotObject )

    @QtCore.pyqtSlot(object)
    def handleItemInsertedSlot(self, _o_item ):
        """
        Cette fonction est appelee lors de l'insertion d'item dans
        le treeview
        """
        o_itemData = _o_item.getItemData()
        if isinstance(o_itemData, QArkPlotableObject):
            #print 'handleItemInsertedSlot %s' % _o_itemData
            o_itemData.resetToDefault()
            self.addPlot( o_itemData )

    @QtCore.pyqtSlot(object)
    def handleNavigationTabChangedSlot(self):
        """
        """
        self.updatePenSettings()

    @QtCore.pyqtSlot(object, object, object)
    def handleSelectionChangedSlot( self, sendingView, selected, deselected ):
        """
        sender : view sender (QAbstractViewItem)
        selected : QItemSelection
        deselected : QItemSelection
        """
        # Check for pen settings
        self.updatePenSettings()
        # First handle selected items
        #---------------------------------------------------------------
        t_selectedItemData = []
        for o_item in map( lambda o_index: sendingView.model().getItem( o_index )
                          , selected.indexes()
                          ):
            t_plotableItems = []
            o_item.getListOfItemDataIsInstance( QArkPlotableObject, t_plotableItems)
            # Get only data that are flagged to be displayed
            t_selectedItemData.extend( filter( lambda o_itemData: o_itemData.getToDisplay()
                                              , map( lambda i: i.getItemData()
                                                    , t_plotableItems
                                                    )
                                              )
                                      )
        t_selectedItemData = list(set(t_selectedItemData))

        # Next handle deselected items
        #---------------------------------------------------------------
        t_deselectedItemData = []
        for o_item in map( lambda o_index: sendingView.model().getItem( o_index )
                          , deselected.indexes()
                          ):
            t_plotableItems = []
            o_item.getListOfItemDataIsInstance( QArkPlotableObject, t_plotableItems)
            #t_deselectedItemData.extend( map( lambda i: i.getItemData(), t_plotableItems) )
            # Get only data that are flagged as displayed
            t_deselectedItemData.extend( filter( lambda o_itemData: o_itemData.getToDisplay()
                                              , map( lambda i: i.getItemData()
                                                    , t_plotableItems
                                                    )
                                              )
                                        )
        t_deselectedItemData = list(set(t_deselectedItemData))

        # Check if item are in both lists
        # This can happen for example if a parent is selected while
        # its child is deselected
        # We ensure that nothing is done for those items
        #---------------------------------------------------------------
        t_intersect = filter(lambda x: x in t_deselectedItemData
                            , t_selectedItemData)
        for o_object in t_intersect:
            t_deselectedItemData.pop( t_deselectedItemData.index(o_object) )
            t_selectedItemData.pop( t_selectedItemData.index(o_object) )

        # Now we can tell the plot widget to focus and unfocus
        for o_uniqueObject in t_deselectedItemData:
            self.ui_plotWidget.unsetFocusPlotableObject( o_uniqueObject )
        for o_uniqueObject in t_selectedItemData:
            self.ui_plotWidget.setFocusPlotableObject( o_uniqueObject )
