# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#
#
# QArkExceptionHandler
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
import os
import traceback
import time
try:
    # Python 2
    from cStringIO import StringIO
except:
    # Python 3
    from io import StringIO

from PyQt5 import QtCore, QtGui, QtWidgets

from .QArkException import QArkException

class QArkExceptionHandler( QtCore.QObject ):
    """
    Class to handle QArkException.
    Basic python exception are also handled
    Specifics callbacks can be set for both kind of exception
    """
    errorHandledSignal = QtCore.pyqtSignal( object )
    basicExceptionHandledSignal = QtCore.pyqtSignal( object )

    def __init__( self
                 , parent
                 , _s_logDir
                 ):
        """
        @brief Constructs a QArkExceptionHandler instance
        @param parent : parent object
        @type parent : L{QtCore.QObject}
        @param _s_logDir : directory to save the error log
        @type _s_logDir : C{str}
        """
        QtCore.QObject.__init__( self, parent = parent )
        self.parent = parent

        # Define the directory to store the error log file
        self.s_logDir = _s_logDir

        # Save the current excepthook
        self.b_excepthookEnabled = False
        self.o_sys__excepthook__ = sys.excepthook

        self.x_qArkExceptionCallback = None
        self.t_qArkExceptionCallbackArgs = None
        self.x_basicExceptionCallback = None
        self.t_basicExceptionCallbackArgs = None

    def setLogDir( self, _s_logDir ):
        self.s_logDir = _s_logDir

    def restoreSystemExceptHook(self):
        sys.excepthook = self.o_sys__excepthook__
    
    def restoreLocalExceptHook( self ):
        if self.b_excepthookEnabled :
            sys.excepthook = self.excepthook

    def setQArkExceptionCallback( self, _x_func ):
        """
        Set callback function to call when an QArkException is raised
        The callback first argument should be the Exception
        @param _x_func : callback function
        @type _x_func : L{function}
        @experimental
        """
        self.x_qArkExceptionCallback = _x_func

    def setQArkExceptionCallbackArgs( self, **kwargs ):
        """
        Set arguments used for x_qArkExceptionCallback
        @experimental
        """
        self.t_qArkExceptionCallbackArgs = kwargs

    def setBasicExceptionCallback( self, _x_func ):
        """
        Set callback function to call when a basic Exception is raised
        The callback first argument should be the Exception
        @param _x_func : callback function
        @type _x_func : L{function}
        @experimental
        """
        self.x_basicExceptionCallback = _x_func

    def setBasicExceptionCallbackArgs( self, **kwargs ):
        """
        Set arguments used for x_qBasicExceptionCallback
        @experimental
        """
        self.t_basicExceptionCallbackArgs = kwargs

    def setEnableExceptHook( self
                            , _b_enable = True
                            ):
        """
        Enable class specific excepthook function, otherwise the default
        behaviour occurs (usually print a bunch of traces in terminal).
        The sys.excepthook function is the function called when an unhandled
        exception occurs. (not in a try/except clause)
        The function defined in self.excepthook displays a graphical message box
        with details about the exception.
        @param _b_enable : boolean to enable/disable the feature
        @type _b_enable : C{bool}
        """
        if _b_enable:
            self.b_excepthookEnabled = True
            sys.excepthook = self.excepthook
        else:
            sys.excepthook = self.o_sys__excepthook__

    def handleException( self
                        , _o_exception
                        ):
        """
        Handle the exception.
        Callback functions can be set before its call (as well as arguments)
        by calling the specifics set functions.
        In any case the args are set to None after the callback call.
        """
        if isinstance( _o_exception, QArkException ):
            # Specific behaviour for QArkException
            # Those are exceptions that are willing to be emitted to others objects
            # like a log interface
            self.errorHandledSignal.emit( _o_exception )

            if not self.x_qArkExceptionCallback is None:
                # Call the callback if set
                self.x_qArkExceptionCallback( _o_exception, **self.t_qArkExceptionCallbackArgs )
                # Reset the callback arguments
                self.t_qArkExceptionCallbackArgs = None
        else:
            self.basicExceptionHandledSignal.emit( _o_exception )

            # The callback function can for instance re-raise the exception.
            if not self.x_basicExceptionCallback is None:
                # Call the callback if set
                self.x_basicExceptionCallback( _o_exception, **self.t_basicExceptionCallbackArgs )
                # Reset the callback arguments
                self.t_basicExceptionCallbackArgs = None

    def excepthook( self
                   , excType
                   , excValue
                   , tracebackobj
                   ):
        """
        @brief Function to catch unhandled exceptions.
        @param excType exception type
        @param excValue exception value
        @param tracebackobj traceback object
        """
        s_separator = '-' * 80
        s_logFile = os.path.join( self.s_logDir, "error.log" )
        s_timeString = time.strftime("%Y-%m-%d, %H:%M:%S")
        # init a buffer to write traceback
        fp_tbinfofile = StringIO()
        # print traceback in buffer
        traceback.print_tb( tracebackobj, None, fp_tbinfofile )
        # read buffer
        fp_tbinfofile.seek(0)
        s_tbinfo = fp_tbinfofile.read()

        t_msg = [ 'An unhandled exception occurred'
                    ,'A log has been written to {}'.format( s_logFile )
                    ,'\n'
                    , s_separator
                    ,'Error information:'
                    , s_timeString
                    , s_separator
                    ,'{0} : {1}'.format( str(excType), str(excValue) )
                    , s_separator
                    , s_tbinfo
                    ]

        s_msg = '\n'.join(t_msg)

        try:
            f = open(s_logFile, "w")
            f.write(s_msg)
            f.close()
        except IOError:
            pass
        try:
            o_errorbox = QtWidgets.QMessageBox( parent = self.parent )
            o_errorbox.setText( s_msg )
            o_errorbox.exec_()
        except:
            pass
