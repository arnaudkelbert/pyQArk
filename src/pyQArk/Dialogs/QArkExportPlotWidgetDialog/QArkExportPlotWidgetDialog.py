# -*- coding: utf-8 -*-
import os
from PyQt5 import QtCore, QtWidgets

from pyQArk.Core.QArkUiLoader import loadUi
from pyQArk.Dialogs.QArkExportPlotWidgetDialog import PKGPATH
Ui_QArkExportPlotWidgetDialog = loadUi(PKGPATH('./QArkExportPlotWidgetDialog.ui'), pkgname=__name__.rpartition('.')[0])

from pyQArk.Widgets.QArkPlotWidget.QArkPlotWidget import QArkPlotWidget

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

class QArkExportPlotWidgetDialog( QtWidgets.QDialog, Ui_QArkExportPlotWidgetDialog ):

    def __init__( self
                 , parent = None
                 , _s_directory = None
                 ):
        super( QArkExportPlotWidgetDialog, self ).__init__( parent = parent )
        if not _s_directory is None:
            self.s_currentDirectory = _s_directory
        else:
            self.s_currentDirectory = os.getcwd()
        self.initUi()
        self.initConnection()

    def initUi( self ):
        self.ui = Ui_QArkExportPlotWidgetDialog()
        self.ui.setupUi(self)
        self.setObjectName(_fromUtf8("qArkExportPlotWidgetDialog"))
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.ui.directoryLineEdit.setText( self.s_currentDirectory )
        self.ui.formatComboBox.addItems( QArkPlotWidget.T_ACCEPTED_EXPORT_FORMATS )

    def initConnection( self ):
        """
        """
        self.ui.directoryToolButton.clicked.connect( self.openDirectoryDialogSlot )

    def getFilename(self):
        return self.s_filename

    def getWidth(self):
        return self.u_width

    def accept( self ):
        s_filename = QtCore.QFileInfo( self.ui.fileLineEdit.text() ).completeBaseName()
        if len(s_filename) == 0:
            QtWidgets.QMessageBox.critical( self, ''
                                    , 'Fichier incorrect'
                                    , QtWidgets.QMessageBox.Ok
                                    )
        self.s_filename = '.'.join( [ os.path.join( str(self.ui.directoryLineEdit.text())
                                                   , str(s_filename)
                                                   )
                                     , str(self.ui.formatComboBox.currentText())
                                     ]
                                    )

        self.u_width = self.ui.widthSpinBox.value()
        QtWidgets.QDialog.accept( self )

#---------------------------------------------------------------
#
#  SLOTS
#
#---------------------------------------------------------------
    @QtCore.pyqtSlot()
    def openDirectoryDialogSlot( self ):
        s_dirname = QtWidgets.QFileDialog.getExistingDirectory(self
                                                            , 'Repertoire de sortie'
                                                            , self.ui.directoryLineEdit.text()
                                                            )
        self.ui.directoryLineEdit.setText(s_dirname)

