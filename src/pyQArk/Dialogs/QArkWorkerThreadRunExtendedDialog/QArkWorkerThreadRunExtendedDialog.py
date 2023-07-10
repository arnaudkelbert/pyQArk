# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from pyQArk.Core.QArkUiLoader import loadUi
from pyQArk.Dialogs.QArkWorkerThreadRunExtendedDialog import PKGPATH
Ui_QArkWorkerThreadRunExtendedDialog = loadUi(PKGPATH('./QArkWorkerThreadRunExtendedDialog.ui'), pkgname=__name__.rpartition('.')[0])
from pyQArk.Core.QArkWorkerThreadController import QArkWorkerThreadController
from pyQArk import QArkConfig

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

class QArkWorkerThreadRunExtendedDialog( QtWidgets.QDialog, Ui_QArkWorkerThreadRunExtendedDialog ):
    """
    Class to represents a run dialog.
    It starts a threaded Worker on show.
    StdOut and StdErr are handled and displayed in a tabWidget.
    This widget can also be defined as the default system output (call
    the setAsSystemOutput() method to do so - can be undone by calling
    the restoreDefaultSystemOutput() method)
    """
    STDOUT_TAB_INDEX = 0
    STDERR_TAB_INDEX = 1
    returnedDataReady = QtCore.pyqtSignal(object)

    def __init__( self
                 , parent = None
                 , _b_workIsInterruptable = True
                 , _b_enableProgressBar = False
                 , _b_keepDialogOpen = True
                 , _b_showDetails = False
                 , _s_promptMessage = 'Please wait...'
                 , _s_loaderAnimationFile = None
                 ):
        super( QArkWorkerThreadRunExtendedDialog, self).__init__( parent = parent )
        self.o_exceptionHandler = None
        self.t_workerResult = None
        self.b_workIsInterruptable = _b_workIsInterruptable
        self.b_enableProgressBar = _b_enableProgressBar
        self.b_keepDialogOpen = _b_keepDialogOpen
        self.b_showDetails = _b_showDetails
        self.s_promptMessage = _s_promptMessage
        self.s_loaderAnimationFile = _s_loaderAnimationFile
        if not self.s_loaderAnimationFile:
            self.s_loaderAnimationFile = QArkConfig.QARK_MEDIA_LOADER_GIF
        self.initUi()
        self.initConnection()

    def setMessageSender( self, _o_sender ):
        """
        Set the message sender member and set the connection with
        the current object.
        The message sender will be used to send message if the current object
        is considered as system output.
        @param _o_sender : the message sender
        @type _o_sender : L{QArkMessageSender}
        """
        self.o_messageSender = _o_sender
        self.o_messageSender.messageSentSignal.connect( self.handleMessageSentSlot )

    def setWarningSender( self, _o_sender ):
        """
        Set the warning sender member and set the connection with
        the current object.
        @param _o_sender : the warning sender
        @type _o_sender : L{QArkWarningSender}
        """
        self.o_warningSender = _o_sender
        self.o_warningSender.warningSentSignal.connect( self.handleWarningSentSlot )

    def setExceptionHandler( self, _o_handler ):
        """
        Set the exception handler member and set the connection with
        the current object.
        @param _o_handler : the exception handler
        @type _o_handler : L{QArkExceptionHandler}
        """
        self.o_exceptionHandler = _o_handler
        self.o_exceptionHandler.errorHandledSignal.connect( self.handleErrorHandledSlot )
        self.o_exceptionHandler.basicExceptionHandledSignal.connect( self.handleErrorHandledSlot )

    #def write( self, _s_str ):
        #"""
        #Define a write method so that an object can be considered as
        #system output
        #"""
        ## Check the message length and do not send newline only
        #if len(_s_str.replace('\r','')) > 0 and _s_str != '\n':
            #self.updateStdOut( _s_str )

    #def flush( self ):
        #"""
        #Define a write method so that an object can be considered as
        #system output
        #"""
        ## Do nothing
        #pass

    #def setAsSystemOutput( self ):
        #"""
        #Set the current object as system output
        #"""
        #self.o_systemStdOut = sys.stdout
        #self.o_systemStdErr = sys.stderr
        #sys.stdout = self
        #sys.stderr = self

    #def restoreDefaultSystemOutput( self ):
        #"""
        #Restore the default system output
        #"""
        #sys.stdout = self.o_systemStdOut
        #sys.stderr = self.o_systemStdErr

    def initUi( self ):
        """
        @brief init user interface
        """
        self.ui = Ui_QArkWorkerThreadRunExtendedDialog()
        self.ui.setupUi(self)
        self.setObjectName(_fromUtf8("qArkWorkerRunDialog"))
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        # Set icons
        #---------------------------------------------------------------
        self.ui.tabWidget.setTabIcon( self.__class__.STDOUT_TAB_INDEX, QtGui.QIcon.fromTheme("dialog-information") )
        self.ui.tabWidget.setTabIcon( self.__class__.STDERR_TAB_INDEX, QtGui.QIcon.fromTheme("dialog-error") )
        # Set current tab
        self.ui.tabWidget.setCurrentIndex( self.__class__.STDOUT_TAB_INDEX )
        self.ui.buttonBox.button( QtWidgets.QDialogButtonBox.Close ).setEnabled(False)
        self.ui.buttonBox.button( QtWidgets.QDialogButtonBox.Abort ).setEnabled(self.b_workIsInterruptable)

        if not self.b_enableProgressBar:
            self.ui.progressBar.setVisible(False)
            # Set movie
            self.o_progressMovie = QtGui.QMovie( self.s_loaderAnimationFile )
            if self.o_progressMovie.isValid():
                self.ui.movieLabel.setMovie( self.o_progressMovie )
            else:
                self.o_progressMovie = None
        else:
            self.ui.movieLabel.setVisible(False)
            self.o_progressMovie = None

        self.ui.keepOpenCheckBox.setChecked(self.b_keepDialogOpen)
        self.ui.tabWidget.setVisible(self.b_showDetails)
        self.checkShowDetailsLabel()
        self.ui.promptLabel.setText(self.s_promptMessage)

    def initConnection( self ):
        """
        @brief init connection
        """
        self.ui.showDetailsPushButton.clicked.connect( self.handleShowDetailsPushButtonClicked )

    def checkShowDetailsLabel( self ):
        if self.ui.tabWidget.isVisible():
            self.ui.showDetailsPushButton.setText('Hide details')
        else:
            self.ui.showDetailsPushButton.setText('Show details')

        #self.adjustSize()
        #self.resize( self.sizeHint() )

    def addWarning( self, _o_warning ):
        """
        Add a warning to StdOut plainTextEdit
        @param _o_warning : warning object
        @type _o_warning : L{QArkWarning}
        """
        self.updateStdOut(str(_o_warning))

    def addError( self, _o_error ):
        """
        Add an error to StdErr plainTextEdit
        @param _o_error : error object
        @type _o_error : L{QArkException}
        """
        self.updateStdErr(str(_o_error))

    def addMessage( self, _o_message ):
        """
        Add a message to StdOut plainTextEdit
        @param _o_message : message object
        @type _o_message : L{QArkMessage}
        """
        self.updateStdOut(str(_o_message))

    def updateStdOut(self, _s_str):
        if _s_str != '':
            self.ui.stdoutPlainTextEdit.moveCursor( QtGui.QTextCursor.End, QtGui.QTextCursor.MoveAnchor )
            self.ui.stdoutPlainTextEdit.insertPlainText(_s_str)
            self.ui.stdoutPlainTextEdit.moveCursor(QtGui.QTextCursor.End, QtGui.QTextCursor.MoveAnchor)

    def updateStdErr(self, _s_str):
        if _s_str != '':
            self.ui.stderrPlainTextEdit.moveCursor( QtGui.QTextCursor.End, QtGui.QTextCursor.MoveAnchor )
            self.ui.stderrPlainTextEdit.insertPlainText(_s_str)
            self.ui.stderrPlainTextEdit.moveCursor(QtGui.QTextCursor.End, QtGui.QTextCursor.MoveAnchor)
            self.ui.tabWidget.setCurrentIndex( self.__class__.STDERR_TAB_INDEX )
            self.b_errorOccured = True

    def accept(self):
        QtGui.QDialog.accept(self)

    def reject(self):
        if not self.o_controller.hasWorkerFinished():
            if self.b_workIsInterruptable:
                answer = QtWidgets.QMessageBox.question( self, '', 'Abort and close window ?'
                                                    , QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No )
                if answer == QtWidgets.QMessageBox.Yes:
                    self.o_controller.interrupt()
                #self.restoreDefaultSystemOutput()
                #QtGui.QDialog.reject(self)
        else:
            self.t_workerResult = self.o_controller.getReturnedData()
            self.returnedDataReady.emit( self.t_workerResult )
            #self.restoreDefaultSystemOutput()
            QtWidgets.QDialog.reject(self)

    def setWorker(self, _cls_workerClass, _t_workerParam):
        """
        """
        self.b_workerHasStarted = False
        self.o_controller = QArkWorkerThreadController( _cls_worker = _cls_workerClass
                                                        , _t_workerParameters = _t_workerParam
                                                        , _o_exceptionHandler = self.o_exceptionHandler
                                                        #, _o_exceptionHandler = None
                                                        )
        self.o_controller.workerError.connect( self.handleErrorHandledSlot )
        self.o_controller.workerFinished.connect( self.handleWorkerHasFinished )
        self.o_controller.writeStdOutRequest.connect( self.handleMessageSentSlot )

    def startWorker(self):
        self.b_errorOccured = False
        #self.setAsSystemOutput()
        if not self.o_progressMovie is None:
            self.o_progressMovie.start()
        self.o_controller.startThread()

    def showEvent(self, evt):
        if not self.b_workerHasStarted:
            self.b_workerHasStarted = True
            self.startWorker()

    def closeEvent(self, evt):
        if not self.o_controller.hasWorkerFinished():
            answer = QtWidgets.QMessageBox.question( self, '', 'Abort and close window ?'
                                                , QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No )
            if answer == QtWidgets.QMessageBox.Yes:
                self.o_controller.interrupt()
                #self.restoreDefaultSystemOutput()
                evt.accept()
            else:
                evt.ignore()
        else:
            evt.accept()

    def getWorkerResult(self):
        return self.t_workerResult

#---------------------------------------------------------------
#
#  SLOTS
#
#---------------------------------------------------------------
    @QtCore.pyqtSlot( object )
    def handleWarningSentSlot( self, _o_warning ):
        self.addWarning( _o_warning )

    @QtCore.pyqtSlot( object )
    def handleErrorHandledSlot( self, _o_error ):
        self.addError( _o_error )

    @QtCore.pyqtSlot( object )
    def handleMessageSentSlot( self, _o_message ):
        self.addMessage( _o_message )

    @QtCore.pyqtSlot()
    def handleWorkerHasFinished(self):
        if not self.o_progressMovie is None:
            self.o_progressMovie.stop()
        self.ui.buttonBox.button( QtWidgets.QDialogButtonBox.Close ).setEnabled(True)
        self.ui.buttonBox.button( QtWidgets.QDialogButtonBox.Abort ).setEnabled(False)
        if not self.ui.keepOpenCheckBox.isChecked() and not self.b_errorOccured:
            self.reject()

    @QtCore.pyqtSlot()
    def handleShowDetailsPushButtonClicked(self):
        self.ui.tabWidget.setVisible( not self.ui.tabWidget.isVisible() )
        self.checkShowDetailsLabel()