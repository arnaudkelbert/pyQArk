# -*- coding: utf-8 -*-
from pyQArk.Core.QArkException import QArkException
from pyQArk.Core.QArkWarning import QArkWarning

class QArkFunctionWarning( QArkWarning ): pass

T_WARNING_MESSAGES = {
}

class QArkFunctionError( QArkException ): pass

class QArkFunctionMissingRequiredFunctionArgError( QArkFunctionError ):
    def __init__( self, *message ):
        super( self.__class__, self ).__init__( T_ERROR_MESSAGES[self.__class__].format(*message)
                                               )
T_ERROR_MESSAGES = {
  QArkFunctionMissingRequiredFunctionArgError : 'Error while instantiating {} : Missing function argument {}'
}

class QArkFunction(object):
    """
    QArkFunction class
    This class should not be instanciated : create subclasses.
    Subclasses should at least define :
     -  T_FUNC_ARGS
     -  function function
     
    @see QArkFunctionFactory
    @see QArkFuncArg
    """
    S_NAME ='QArkFunction'
    S_INFO = ''
    U_CST_ARG_KEY_INDEX\
    ,U_CST_ARG_CLASS_INDEX\
    ,U_CST_ARG_REQUIRED_INDEX\
    ,U_CST_ARG_DEFAULT_VALUE_INDEX\
    ,U_CST_ARG_UICLASS_INDEX\
    ,U_CST_ARG_KWARGS_INDEX = range(6)
        
    # Function constant arguments defined as a list of tuple 
    # ( 'key', type, required, x_defaultValue, widgetClass, **kwargs )
    # where :
    # - key : the key to store and access the argument
    # - type : argument type (functor subclass can check the argtype to validate)
    #         Note : the type can be a list of a unique type (f.i. : [int])
    #                this is used for functor with variable vector dimension
    # - required : required flag (if a required arg is missing a QArkFunctionMissingRequiredFunctionArgError is thrown)
    # - defaultValue : default value (can be None)
    # - widgetClass : QArkInputWidget subclass to instantiate to represent the functor argument (should match the type)
    # - kwargs : optional parameters dictionary used for both instantiation of type and widgetClass
    T_CST_ARGS = [
                  ]
    
    def __init__(self
                 , **kwargs
                 ):
        """
        Init check that all required arguments are passed. If it is the case the function is created.
        The kwargs dict should have a key for each required function argument defined in T_FUNC_ARGS
        and associate a key to a QArkFunctionArg object, ie : kwargs : { 'arg_key' : QArkFuncArg() }
        """
        self.t_cstArgs = {}
        
        # Get the constant value parameters
        for t_cstArgTuple in self.__class__.getCstArgs():
            
            s_cstArgKey = t_cstArgTuple[ self.U_CST_ARG_KEY_INDEX ]
            b_required = t_cstArgTuple[ self.U_CST_ARG_REQUIRED_INDEX ]        
            
            if not kwargs.has_key( s_cstArgKey ):
                if b_required:
                    raise QArkFunctionMissingRequiredFunctionArgError( self.__class__.__name__, s_cstArgKey )
                else:
                    self.t_cstArgs[ s_cstArgKey ] = None            
            else:
                # Get the QArkFunctionArg
                o_cstArg = kwargs[ s_cstArgKey ]
                self.t_cstArgs[ s_cstArgKey ] = o_cstArg.getValue()

    def function(self, *args):
        """
        function function to define
        The args parameter is the vectored field to pass to a mapping function
        This function can access other parameters
        """
        raise NotImplemented

    def function_wrapper(self, _t):
        """
        Another function function interface
        """
        return self.function(*_t)
        
    @classmethod
    def getCstArgs(cls):
        return cls.T_CST_ARGS
        
    @classmethod
    def getCstArgsKeys(cls):
        return [t[cls.U_CST_ARG_KEY_INDEX] for t in cls.getCstArgs()]
    