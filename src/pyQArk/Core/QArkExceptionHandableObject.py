# -*- coding: utf-8 -*-
from pyQArk.Core.QArkExceptionHandler import QArkExceptionHandler

class QArkExceptionHandableObject( object ):
    """
    Class interface for object that can handle exception.
    The purpose of this class is to set a convenient way to handle
    exception for subclasses without the definition of a QArkExceptionHandler
    instance.
    This class only implements the handleException methods that calls the
    object QArkExceptionHandler member.
    If not set a construction time, the class member QARK_EXCEPTION_HANDLER is used
    """
    QARK_EXCEPTION_HANDLER = QArkExceptionHandler(None,'.')

    def __init__( self, _o_handler = None ):
        """
        @brief Constructor
        @param _o_handler : the handler to use by the object. If None the class member
                            QARK_EXCEPTION_HANDLER is used.
        @type _o_handler : L{QArkExceptionHandler]
        """
        if not _o_handler is None:
            self.setExceptionHandler( _o_handler )
        else:
            self.setExceptionHandler( self.__class__.QARK_EXCEPTION_HANDLER )

    def setExceptionHandler( self, _o_handler ):
        """
        @brief set a handler
        @param _o_handler : the handler to use by the object
        @type _o_handler : L{QArkExceptionHandler]
        """
        self.o_exceptionHandler = _o_handler

    def getExceptionHandler( self ):
        """
        @brief Handler accessor
        @return : The handler instance member
        @rtype : L{QArkExceptionHandler}
        """
        return self.o_exceptionHandler

    def handleException( self, _o_exception ):
        """
        Call the handleException of the handler member
        @param _o_exception : an exception
        @type _o_exception : L{Exception}
        """
        self.o_exceptionHandler.handleException( _o_exception )
