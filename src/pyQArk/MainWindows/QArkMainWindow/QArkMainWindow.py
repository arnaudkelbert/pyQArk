# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets
from pyQArk.Core import QArkMessageSender
from pyQArk.Core import QArkWarningSender
from pyQArk.Core.QArkExceptionHandler import QArkExceptionHandler
from pyQArk.Core.QArkExceptionHandableObject import QArkExceptionHandableObject
from pyQArk.Widgets.QArkMessageTabWidget.QArkMessageTabWidget import QArkMessageTabWidget
from pyQArk.Widgets.QArkStatusWidget.QArkStatusWidget import QArkStatusWidget

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class QArkMainWindow( QtWidgets.QMainWindow, QArkExceptionHandableObject ):
    """
    A main window framework with a central tab widget.
    Here are the main components :
        - a central tab widget
        - a bottom message tab widget to log messages, warnings et errors
    """
    def __init__( self
                 ,_s_logDir='.'
                 ):
        """Constructeur"""
        super( QArkMainWindow, self ).__init__()
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
        Must be defined in
        """
        self.ui_mainWidget = QtWidgets.QWidget()

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        self.ui_mainWidget.setSizePolicy( sizePolicy )
        #self.ui_mainWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ui_mainWidget.setAutoFillBackground(False)
        self.ui_mainLayout = QtWidgets.QVBoxLayout(self.ui_mainWidget)
        self.ui_mainLayout.setSpacing(0)
        self.ui_mainLayout.setContentsMargins(0,0,0,0)
        self.ui_mainLayout.setObjectName(_fromUtf8("ui_mainlayout"))

        #self.ui_mainWidget.setTabPosition(QtGui.QTabWidget.North)
        #self.ui_mainWidget.setTabShape(QtGui.QTabWidget.Rounded)
        #self.ui_mainWidget.setElideMode(QtCore.Qt.ElideNone)
        #self.ui_mainWidget.setDocumentMode(True)
        #self.ui_mainWidget.setMovable(True)

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
        self.ui_qSplitter = QtWidgets.QSplitter()
        self.ui_qSplitter.setOrientation( QtCore.Qt.Vertical )
        self.ui_qSplitter.addWidget( self.ui_mainWidget )
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

    def setMainWidget( self, _o_widget ):
        """
        Add a tab widget
        """
        self.ui_mainLayout.addWidget(_o_widget)

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
        try:
            return self.t_menus[_s_id]
        except KeyError:
            return None

    def getRegisteredAction( self, _s_id ):
        """
        Get an action from its id
        @param _s_id : id of the action
        @type _s_id : C{str}
        """
        try:
            return self.t_actions[_s_id]
        except KeyError:
            return None

    def initMenu( self ):
        self.t_menus = {}

    def initAction( self ):
        self.t_actions = {}

    def closeEvent( self, event ):
        """
        Overwrite closeEvent to make sure all subwindows are closed
        """
        event.accept()

    def createActions( self ):
        """Create action
        Overwrite to add actions
        """
        self.registerAction( 'QUIT_ACTION', QtWidgets.QAction( "&Quit", self, triggered = self.close ) )

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
        Create a child window using a QDialog subclass
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
            s_windowTitle = ''
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
        if issubclass( _cls_dialogClass, QtWidgets.QDialog ):
            o_dialog = _cls_dialogClass( parent = self, **kwargs )
        else:
            # A QWidget has been passed : create a QDialog and put it in
            o_dialog = QtWidgets.QDialog( parent = self )
            o_widget = _cls_dialogClass( parent = o_dialog, **kwargs )
            o_layout = QtWidgets.QVBoxLayout(o_dialog)
            o_layout.setSpacing( 0 )
            o_layout.setContentsMargins(0,0,0,0)
            o_layout.addWidget( o_widget )
            o_dialog.setLayout( o_layout )
            if not o_size is None:
                o_widget.resize(o_size)
        o_dialog.setWindowTitle( s_windowTitle )
        return o_dialog