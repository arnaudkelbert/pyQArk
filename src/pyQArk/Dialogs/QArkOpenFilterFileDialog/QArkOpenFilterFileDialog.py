# -*- coding: utf-8 -*-
import os
from PyQt5 import QtCore, QtWidgets
from pyQArk.Core.QArkUiLoader import loadUi
from pyQArk.Dialogs.QArkOpenFilterFileDialog import PKGPATH
Ui_QArkOpenFilterFileDialog = loadUi(PKGPATH('./QArkOpenFilterFileDialog.ui'), pkgname=__name__.rpartition('.')[0])

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

class QArkOpenFilterFileDialog( QtWidgets.QDialog, Ui_QArkOpenFilterFileDialog ):

    directoryChangedSignal = QtCore.pyqtSignal(str)
    acceptedSelectionSignal = QtCore.pyqtSignal(str)

    def __init__( self
                 , parent = None
                 , _s_directory = None
                 , _s_filter = None
                 , _u_selectionMode = QtWidgets.QAbstractItemView.ExtendedSelection
                 ):
        super( QArkOpenFilterFileDialog, self ).__init__( parent = parent )

        if not _s_directory is None:
            self.s_currentDirectory = _s_directory
        else:
            self.s_currentDirectory = os.getcwd()

        if not _s_filter is None \
           and not _s_filter.isEmpty() \
           and len(_s_filter) > 0:
            self.s_currentFilter = _s_filter
        else:
            self.s_currentFilter = '*'

        self.u_selectionMode = _u_selectionMode
        self.initUi()
        self.initConnection()
        self.handleDirectoryChangedSlot( self.s_currentDirectory )
        self.t_selectedFiles = None

    def initUi( self ):
        self.ui = Ui_QArkOpenFilterFileDialog()
        self.ui.setupUi(self)
        self.setObjectName(_fromUtf8("qArkOpenFilterFileDialog"))
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.ui.fileListWidget.setSelectionMode(self.u_selectionMode)
        self.ui.urlLineEdit.setText( self.s_currentDirectory )
        self.ui.urlLineEdit.setReadOnly( True )
        self.ui.filterLineEdit.setText( self.s_currentFilter )
        self.ui.buttonBox.button(QtWidgets.QDialogButtonBox.Open).setEnabled(False)

    def initConnection( self ):
        """
        """
        self.ui.urlToolButton.clicked.connect( self.openDirectoryDialogSlot )
        self.directoryChangedSignal.connect( self.handleDirectoryChangedSlot )
        self.ui.directoryListWidget.itemActivated.connect( self.handleDirectoryListWidgetItemActivatedSlot )
        self.ui.fileListWidget.itemSelectionChanged.connect( self.handleFileListWidgetSelectionChangedSlot )
        self.ui.filterLineEdit.returnPressed.connect( self.handleFilterChangedSlot )

    def keyPressEvent( self, evt ):
        """
        Overwrite default keyPressEvent
        The following events are ignored in order to keep the dialog open
        and so that they are connected to child widgets (ie filterLineEdit)
          - Key_Enter
          - Key_Return
        """
        if evt.key() == QtCore.Qt.Key_Enter \
            or evt.key() == QtCore.Qt.Key_Return :
            evt.ignore()
        else:
            super( QtWidgets.QDialog, self ).keyPressEvent(evt)

    def updateFileListWidget( self ):
        self.ui.fileListWidget.clear()
        o_rx = QtCore.QRegExp( self.s_currentFilter )
        o_rx.setPatternSyntax( QtCore.QRegExp.Wildcard )

        # On filtre avec exactMatch (la fonction filter de QStringList n'applique pas un exact match)
        #t_filteredFileList = self.t_allFilesInCurrentDirectory.filter( o_rx )
        t_filteredFileList = [ f for f in self.t_allFilesInCurrentDirectory
                               if o_rx.exactMatch(f)
                               ]

        if len(t_filteredFileList) > 0:
            self.ui.fileListWidget.setEnabled(True)
            self.ui.fileListWidget.addItems( t_filteredFileList )
            o_qdir = QtCore.QDir( self.s_currentDirectory )
            o_qFileIconProvider = QtWidgets.QFileIconProvider()

            for o_item in self.iterAllFiles():
                o_item.setIcon( o_qFileIconProvider.icon( QtCore.QFileInfo(o_qdir, o_item.text()) ) )
        else:
            self.ui.fileListWidget.setEnabled(False)

    def iterAllDirectories(self):
        for i in range( self.ui.directoryListWidget.count() ):
            yield self.ui.directoryListWidget.item(i)

    def iterAllFiles(self):
        for i in range( self.ui.fileListWidget.count() ):
            yield self.ui.fileListWidget.item(i)

    def getSelectedFileList( self ):
        return self.ui.fileListWidget.selectedItems()

    def getSelectedFileNameList( self ):
        return map( lambda i: os.path.join( self.s_currentDirectory, str(i.text()) )
                    , self.ui.fileListWidget.selectedItems()
                    )

    def getSafeFilter( self ):
        s_filter = self.ui.filterLineEdit.text()
        if len(s_filter) == 0:
            s_filter = '*'
            self.ui.filterLineEdit.setText('*')
        return s_filter

    def getSelectedFiles( self ):
        """
        Method to be called after exec_ in order to retrieve the selection
        """
        return self.t_selectedFiles

    def accept( self ):
        #self.setVisible(False)
        self.t_selectedFiles = self.getSelectedFileNameList()
        QtWidgets.QDialog.accept( self )
        #print 'after accept'
        #self.acceptedSelectionSignal.emit( self.getSelectedFileNameList() )
        #print 'after emit'

#---------------------------------------------------------------
#
#  SLOTS
#
#---------------------------------------------------------------
    @QtCore.pyqtSlot()
    def openDirectoryDialogSlot( self ):
        s_directoryName = QtWidgets.QFileDialog.getExistingDirectory( self
                                                , caption='Selection du repertoire'
                                                , directory = self.s_currentDirectory
                                                )

        if len(s_directoryName) > 0 and s_directoryName != self.s_currentDirectory:
            self.directoryChangedSignal.emit( s_directoryName )

    @QtCore.pyqtSlot(str)
    def handleDirectoryChangedSlot( self, _s_directory ):
        self.ui.directoryListWidget.clear()
        self.s_currentDirectory = os.path.normpath( os.path.abspath( str(_s_directory) ) )
        self.ui.urlLineEdit.setText( self.s_currentDirectory )
        o_qdir = QtCore.QDir( self.s_currentDirectory )

        # Mise a jour liste des repertoires
        #---------------------------------------------------------------
        o_qdir.setFilter( QtCore.QDir.Dirs )
        t_dirList = o_qdir.entryList()

        if len(t_dirList) > 0:
            self.ui.directoryListWidget.setEnabled(True)
            self.ui.directoryListWidget.addItems( t_dirList )
            o_qFileIconProvider = QtWidgets.QFileIconProvider()

            for o_item in self.iterAllDirectories():
                o_item.setIcon( o_qFileIconProvider.icon( QtCore.QFileInfo(o_qdir, o_item.text()) ) )
        else:
            self.ui.directoryListWidget.setEnabled(False)

        # Mise a jour de la liste de tous les fichiers (hors filtre) contenu
        # dans le repertoire courant
        #---------------------------------------------------------------
        o_qdir.setFilter( QtCore.QDir.Files | QtCore.QDir.NoDotAndDotDot )
        self.t_allFilesInCurrentDirectory = o_qdir.entryList()
        self.updateFileListWidget()

    @QtCore.pyqtSlot()
    def handleDirectoryListWidgetItemActivatedSlot( self ):
        s_currentItemString = str( self.ui.directoryListWidget.currentItem().text() )
        s_directoryName = os.path.join( self.s_currentDirectory, s_currentItemString )
        self.directoryChangedSignal.emit( s_directoryName )

    @QtCore.pyqtSlot()
    def handleFileListWidgetSelectionChangedSlot( self ):
        if( len( self.getSelectedFileList() ) > 0 ):
            self.ui.buttonBox.button(QtWidgets.QDialogButtonBox.Open).setEnabled(True)
        else:
            self.ui.buttonBox.button(QtWidgets.QDialogButtonBox.Open).setEnabled(False)

    @QtCore.pyqtSlot()
    def handleFilterChangedSlot( self ):
        self.s_currentFilter = self.getSafeFilter()
        self.updateFileListWidget()
