# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#
#
# QArkMessageTabWidget
#
#
# @author : Arnaud Kelbert
# @date : 2019/03/19
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
from PyQt4 import QtCore, QtGui

from pyQArk.Core.QArkUiLoader import loadUi
from pyQArk.Widgets.QArkMessageTabWidget import PKGPATH
Ui_QArkMessageTabWidget = loadUi(PKGPATH('./QArkMessageTabWidget.ui'), pkgname=__package__)

from pyQArk.Models.QArkMessageItemModel import QArkMessageItemModel
from pyQArk.Models.QArkWarningItemModel import QArkWarningItemModel
from pyQArk.Models.QArkErrorItemModel import QArkErrorItemModel
from pyQArk.Models.QArkSimpleItemListModel import QArkSimpleItemListModel
from pyQArk.Core.QArkMessage import QArkMessage
from pyQArk.Core.QArkMessageSender import QArkMessageSender
from pyQArk.Core.QArkWarningSender import QArkWarningSender
from pyQArk.Core.QArkExceptionHandler import QArkExceptionHandler

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

class QArkMessageTabWidget( QtGui.QTabWidget, Ui_QArkMessageTabWidget ):
    """
    Class to represents a tab widget with 3 tabs for messages, warnings
    and errors to be displayed as ListView.
    A QArkMessageTabWidget must be connected to a QArkMessageSender, a
    QArkWarningSender and a QArkExceptionHandler.
    This widget can also be defined as the default system output (call
    the setAsSystemOutput() method to do so - can be undone by calling
    the restoreDefaultSystemOutput() method)
    """
    MESSAGE_TAB_INDEX = 0
    WARNING_TAB_INDEX = 1
    ERROR_TAB_INDEX = 2

    def __init__( self
                 , parent = None
                 ):
        super( QArkMessageTabWidget, self).__init__( parent = parent )
        # A python list to handle warnings
        self.t_warningList = []
        # A python list to handle exceptions
        self.t_errorList = []
        # A python list to handle messages
        self.t_messageList = []
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

    def write( self, _s_str ):
        """
        Define a write method so that an object can be considered as
        system output
        """
        # Check the message length and do not send newline only
        if len(_s_str.replace('\r','')) > 0 and _s_str != '\n':
            self.o_messageSender.send( QArkMessage( _s_str ) )

    def flush( self ):
        """
        Define a write method so that an object can be considered as
        system output
        """
        # Do nothing
        pass

    def setAsSystemOutput( self ):
        """
        Set the current object as system output
        """
        self.o_systemStdOut = sys.stdout
        self.o_systemStdErr = sys.stderr
        sys.stdout = self
        sys.stderr = self

    def restoreDefaultSystemOutput( self ):
        """
        Restore the default system output
        """
        sys.stdout = self.o_systemStdOut
        sys.stderr = self.o_systemStdErr

    def initUi( self ):
        """
        @brief init user interface
        """
        self.ui = Ui_QArkMessageTabWidget()
        self.ui.setupUi(self)
        self.setObjectName(_fromUtf8("qArkMessageTabWidget"))
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        # Initialisation des modeles
        self.o_warningListModel = QArkSimpleItemListModel( self, self.t_warningList )
        self.ui.warningListView.setModel( self.o_warningListModel )

        self.o_errorListModel = QArkSimpleItemListModel( self, self.t_errorList )
        self.ui.errorListView.setModel( self.o_errorListModel )

        self.o_messageListModel = QArkSimpleItemListModel( self, self.t_messageList )
        self.ui.messageListView.setModel( self.o_messageListModel )

        # Set icons
        self.setTabIcon( self.__class__.MESSAGE_TAB_INDEX, QtGui.QIcon.fromTheme("dialog-information") )
        self.setTabIcon( self.__class__.WARNING_TAB_INDEX, QtGui.QIcon.fromTheme("dialog-warning") )
        self.setTabIcon( self.__class__.ERROR_TAB_INDEX, QtGui.QIcon.fromTheme("dialog-error") )

        # Set current tab
        self.setCurrentIndex( self.__class__.MESSAGE_TAB_INDEX )

    def initConnection( self ):
        """
        @brief init connection
        """
        self.o_warningListModel.rowsInserted.connect( self.ui.warningListView.scrollToBottom )
        self.o_messageListModel.rowsInserted.connect( self.ui.messageListView.scrollToBottom )
        self.o_errorListModel.rowsInserted.connect( self.ui.errorListView.scrollToBottom )

    def addWarning( self, _o_warning ):
        """
        Add a warning item
        @param _o_warning : warning object
        @type _o_warning : L{QArkWarning}
        """
        self.o_warningListModel.addItem( QArkWarningItemModel(self,_o_warning) )
        self.setTabText( self.__class__.WARNING_TAB_INDEX, 'Warning ({})'.format(len(self.t_warningList)) )

    def addError( self, _o_error ):
        """
        Add an error item
        @param _o_error : error object
        @type _o_error : L{QArkException}
        """
        self.o_errorListModel.addItem( QArkErrorItemModel(self,_o_error) )
        self.setTabText( self.__class__.ERROR_TAB_INDEX, 'Erreur ({})'.format(len(self.t_errorList)) )

    def addMessage( self, _o_message ):
        """
        Add a message item
        @param _o_message : message object
        @type _o_message : L{QArkMessage}
        """
        self.o_messageListModel.addItem( QArkMessageItemModel(self,_o_message) )

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
