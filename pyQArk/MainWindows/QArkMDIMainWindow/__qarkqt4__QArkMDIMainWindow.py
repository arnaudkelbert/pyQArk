# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#
#
# QArkMDIMainWindow
#
#
# @author : Arnaud Kelbert
# @date : 2019/03/05
# @version : 0.2
#
# Historic:
# 0.1 : init version
# 0.2 : add python 2/3 compatibility
#-----------------------------------------------------------------------
#{-- Pyhton 2/3 compatibility ------------------------------------------
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
#}-- Pyhton 2/3 compatibility ------------------------------------------

from PyQt4 import QtCore, QtGui

from pyQArk.Core import QArkMessageSender
from pyQArk.Core import QArkWarningSender
from pyQArk.Core.QArkExceptionHandler import QArkExceptionHandler
from pyQArk.Core.QArkExceptionHandableObject import QArkExceptionHandableObject
from pyQArk.Widgets.QArkMessageTabWidget.QArkMessageTabWidget import QArkMessageTabWidget
from pyQArk.Widgets.QArkStatusWidget.QArkStatusWidget import QArkStatusWidget

class QArkMDIMainWindow( QtGui.QMainWindow, QArkExceptionHandableObject ):
    """
    A main window framework for multi-document area.
    Here are the main components :
        - a central MDIArea
        - a bottom message tab widget to log messages, warnings et errors
    """

    def __init__( self
                 ,_s_logDir='.'
                 ):

        """Constructeur"""
        super( QArkMDIMainWindow, self ).__init__()
        QArkExceptionHandableObject.__init__( self, QArkExceptionHandler( parent = self, _s_logDir = _s_logDir ) )
        self.o_messageSender = QArkMessageSender.QARK_MESSAGE_SENDER
        self.o_warningSender = QArkWarningSender.QARK_WARNING_SENDER
        self.getExceptionHandler().setEnableExceptHook( True )
        self.initUi()
        self.initConnection()
        self.initAction()
        self.initMenu()
        self.createActions()
        self.createMenus()
        print( 'Starting application' )

    def initUi( self ):
        """
        @brief init user interface
        """
        self.initUiComponents()
        self.initUiSplitter()
        self.initStatusBar()

    def initStatusBar( self ):
        self.o_statusWidget = QArkStatusWidget( parent = self )
        self.statusBar().addWidget( self.o_statusWidget, 1 )
        self.o_statusWidget.switchToMessage()

    def getStatusWidget(self):
        return self.o_statusWidget

    def initUiComponents( self ):
        """
        @brief init ui components
        Overwrite to add components (do not forget to call parent method first)
        """
        # init the mdiArea
        self.ui_mdiArea = QtGui.QMdiArea()
        self.ui_mdiArea.setOption(QtGui.QMdiArea.DontMaximizeSubWindowOnActivation)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        self.ui_mdiArea.setSizePolicy( sizePolicy )

        # init the message tab widget
        self.ui_QArkMessageTabWidget = QArkMessageTabWidget( self )
        self.ui_QArkMessageTabWidget.setMessageSender( self.o_messageSender )
        self.ui_QArkMessageTabWidget.setWarningSender( self.o_warningSender )
        self.ui_QArkMessageTabWidget.setExceptionHandler( self.getExceptionHandler() )
        self.ui_QArkMessageTabWidget.setAsSystemOutput()

    def initUiSplitter( self ):
        """
        @brief init ui splitter
        """
        # create a splitter and add main components
        self.ui_qSplitter = QtGui.QSplitter()
        self.ui_qSplitter.setOrientation( QtCore.Qt.Vertical )
        self.ui_qSplitter.addWidget( self.ui_mdiArea )
        self.ui_qSplitter.addWidget( self.ui_QArkMessageTabWidget )
        self.setCentralWidget( self.ui_qSplitter )
        policy = self.ui_QArkMessageTabWidget.sizePolicy()
        policy.setVerticalStretch(0)
        policy.setHorizontalStretch(0)
        self.ui_QArkMessageTabWidget.setSizePolicy(policy)

    def initConnection( self ):
        """
        @brief init connection between qobjects
        """
        pass

    def addMenu( self
                , _s_id
                , _s_label
                , _s_parent = None
                ):
        """
        Add a menu.
        @param _s_id : id to access the menu from dictionnary member
        @type _s_id : C{str}
        @param _s_label : label shown in menu
        @type _s_label : C{str}
        @param _s_parent : parent menu id or None
        @param _s_parent : C{str}
        """
        if self.getMenu( _s_id ) is None:
            if _s_parent is None:
                o_parent = self.menuBar()
            else:
                o_parent = self.getMenu( _s_parent )
            self.t_menus[ _s_id ] = o_parent.addMenu( _s_label )

    def addActionMenu( self
                , _s_id
                , _s_label
                , _s_parent = None
                , _t_listOfActions = None
                ):
        """
        Add actions to a menu. If menu already exists the actions are
        added to it. Otherwise it is created.
        @param _s_id : id to access the menu from dictionnary member
        @type _s_id : C{str}
        @param _s_label : label shown in menu
        @type _s_label : C{str}
        @param _s_parent : parent menu id or None
        @param _s_parent : C{str}
        @param _t_listOfActions : list of actions id to add to a menu
        @param _t_listOfActions : C{list}
        """
        if self.getMenu( _s_id ) is None:
            if _s_parent is None:
                o_parent = self.menuBar()
            else:
                o_parent = self.getMenu( _s_parent )
            self.t_menus[ _s_id ] = o_parent.addMenu( _s_label )

        if not _t_listOfActions is None:
            for s_action in _t_listOfActions:
                if s_action is None:
                    self.t_menus[ _s_id ].addSeparator()
                else:
                    self.t_menus[ _s_id ].addAction( self.getRegisteredAction(s_action) )

    def registerAction( self
                       , _s_id
                       , _o_action
                       ):
        """
        Register an action (store it in the current object)
        @param _s_id : id to access the action from dictionnary member
        @type _s_id : C{str}
        @type _o_action : optional action to be added
        @type _o_action : L{QtCore.QAction}
        """
        self.t_actions[ _s_id ] = _o_action

    def getMenu( self, _s_id ):
        """
        Get a menu from its id
        @param _s_id : id of the menu
        @type _s_id : C{str}
        """
        if self.t_menus.has_key( _s_id ):
            return self.t_menus[ _s_id ]
        else:
            return None

    def getRegisteredAction( self, _s_id ):
        """
        Get an action from its id
        @param _s_id : id of the action
        @type _s_id : C{str}
        """
        if self.t_actions.has_key( _s_id ):
            return self.t_actions[ _s_id ]
        else:
            return None

    def initMenu( self ):
        self.t_menus = {}

    def initAction( self ):
        self.t_actions = {}

    def closeEvent( self, event ):
        """
        Overwrite closeEvent to make sure all subwindows are closed
        """
        self.ui_mdiArea.closeAllSubWindows()
        event.accept()

    def createActions( self ):
        """Create action
        Overwrite to add actions
        """
        self.registerAction( 'QUIT_ACTION', QtGui.QAction( "&Quit", self, triggered = self.close ) )

    def createMenus( self ):
        """
        Create menus
        Overwrite to add menu
        """
        self.addActionMenu( 'FILE_MENU', 'File', None, ('QUIT_ACTION',) )

    def createSubWindow( self
                        , _cls_dialogClass
                        , **kwargs
                        ):
        """
        Create a MDI child window using a QDialog subclass
        The dialog construction parameters are passed through kwargs
        """
        # First try to get parent arg.
        # It is not taken into account, the parent is force to the current
        # object
        try:
            _ = kwargs.pop('parent')
        except KeyError:
            pass

        # Size can be modified by passing _o_size arg
        try:
            o_size = kwargs.pop('_o_size')
        except KeyError:
            o_size = None

        # Title can be modified by passing _s_windowTitle arg
        try:
            s_windowTitle = kwargs.pop('_s_windowTitle')
        except KeyError:
            s_windowTitle = QtCore.QString()

        try:
            b_showTitleButtons = kwargs.pop('_b_showTitleButtons')
        except KeyError:
            b_showTitleButtons = True


        try:
            b_onlyMinMaxButtons = kwargs.pop('_b_onlyMinMaxButtons')
        except KeyError:
            b_onlyMinMaxButtons = False

        # Force window to stay on top
        try:
            b_stayOnTop = kwargs.pop('_b_stayOnTop')
        except KeyError:
            b_stayOnTop = False

        if issubclass( _cls_dialogClass, QtGui.QDialog ):
            o_dialog = _cls_dialogClass( parent = self, **kwargs )
        else:
            # A QWidget has been passed : create a QDialog and put it in
            o_dialog = QtGui.QDialog( parent = self )
            o_widget = _cls_dialogClass( parent = o_dialog, **kwargs )
            o_layout = QtGui.QVBoxLayout(o_dialog)
            o_layout.setSpacing( 0 )
            o_layout.setMargin(0)
            o_layout.addWidget( o_widget )
            o_dialog.setLayout( o_layout )

            if not o_size is None:
                o_widget.resize(o_size)

        o_dialog.setWindowTitle( s_windowTitle )
        o_window = QtGui.QMdiSubWindow( self.ui_mdiArea )
        o_window.setWidget( o_dialog )
        o_window.setAttribute( QtCore.Qt.WA_DeleteOnClose )

        # Try to comment this line if crash at dialog closing
        o_dialog.finished.connect( o_window.deleteLater )

        o_dialog.destroyed.connect( o_window.deleteLater )
        self.ui_mdiArea.addSubWindow( o_window )

        if not b_showTitleButtons:
            o_window.setWindowFlags( QtCore.Qt.CustomizeWindowHint
                                    |QtCore.Qt.WindowTitleHint
                                    )

        if b_onlyMinMaxButtons:
            o_window.setWindowFlags( QtCore.Qt.CustomizeWindowHint
                                    |QtCore.Qt.WindowTitleHint
                                    |QtCore.Qt.WindowMaximizeButtonHint
                                    |QtCore.Qt.WindowMinimizeButtonHint
                                    )

        if b_stayOnTop:
            o_window.setWindowFlags( o_window.windowFlags()
                                    |QtCore.Qt.WindowStaysOnTopHint
                                    )

        if not o_size is None:
            o_window.resize(o_size)

        o_window.setGeometry( QtGui.QStyle.alignedRect( QtCore.Qt.LeftToRight
                                                         , QtCore.Qt.AlignCenter
                                                         , o_window.size()
                                                         , self.ui_mdiArea.geometry()
                                                         )
                              )

        return o_dialog
