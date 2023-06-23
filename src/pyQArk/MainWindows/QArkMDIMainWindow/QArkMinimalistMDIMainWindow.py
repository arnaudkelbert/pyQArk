# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets

class QArkMinimalistMDIMainWindow( QtWidgets.QMainWindow ):
    """
    A main window framework for multi-document area.
    Here are the main components :
        - a central MDIArea
        - a bottom message tab widget to log messages, warnings et errors
    """
    def __init__( self ):

        """Constructeur"""
        super( QArkMinimalistMDIMainWindow, self ).__init__()
        #self.o_exceptionHandler = QArkExceptionHandler( parent = self, _s_logDir = '.' )
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

    def initUiComponents( self ):
        """
        @brief init ui components
        Overwrite to add components (do not forget to call parent method first)
        """
        # init the mdiArea
        self.ui_mdiArea = QtWidgets.QMdiArea()
        self.ui_mdiArea.setOption(QtWidgets.QMdiArea.DontMaximizeSubWindowOnActivation)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        self.ui_mdiArea.setSizePolicy( sizePolicy )        
        self.setCentralWidget( self.ui_mdiArea )

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
            s_windowTitle = ""

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
            o_layout.setContentsMargins(0, 0, 0, 0)
            o_layout.addWidget( o_widget )
            o_dialog.setLayout( o_layout )


            if not o_size is None:
                o_widget.resize(o_size)

        o_dialog.setWindowTitle( s_windowTitle )
        o_window = QtWidgets.QMdiSubWindow( self.ui_mdiArea )
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
