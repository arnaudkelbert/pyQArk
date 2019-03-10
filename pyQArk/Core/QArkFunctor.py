# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
# 
#
# Core.QArkFunctor
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
from .QArkException import QArkException
from .QArkWarning import QArkWarning
from .QArkFuncArg import QArkFuncArg

class QArkFunctorWarning( QArkWarning ): pass

T_WARNING_MESSAGES = {
}

class QArkFunctorError( QArkException ): pass

class QArkFunctorMissingRequiredFunctorArgError( QArkFunctorError ):
    def __init__( self, *message ):
        super( self.__class__, self ).__init__( T_ERROR_MESSAGES[self.__class__].format(*message)
                                               )
T_ERROR_MESSAGES = {
  QArkFunctorMissingRequiredFunctorArgError : 'Error while instanciating {} : Missing functor argument {}'
}

class QArkFunctor(object):
    """
    QArkFunctor class
    This class should not be instanciated : create subclasses.
    Subclasses should at least define :
     -  T_FUNC_ARGS
     -  functor function
     
    @see QArkFunctorFactory
    @see QArkFuncArg
    """ 
    S_NAME ='QArkFunctor'    
    S_INFO = ''    
    U_FUNC_ARG_KEY_INDEX\
    ,U_FUNC_ARG_CLASS_INDEX\
    ,U_FUNC_ARG_REQUIRED_INDEX\
    ,U_FUNC_ARG_DEFAULT_VALUE_INDEX\
    ,U_FUNC_ARG_UICLASS_INDEX\
    ,U_FUNC_ARG_KWARGS_INDEX = range(6)
    
    # Functor arguments defined as a list of tuple 
    # ( 'key', type, required, x_defaultValue, widgetClass, **kwargs )
    # where :
    # - key : the key to store and access the argument
    # - type : argument type (functor subclass can check the argtype to validate)
    #         Note : the type can be a list of a unique type (f.i. : [int])
    #                this is used for functor with variable vector dimension
    # - required : required flag (if a required arg is missing a QArkFunctorMissingRequiredFunctorArgError is thrown)
    # - defaultValue : default value (can be None)
    # - widgetClass : QArkInputWidget subclass to instantiate to represent the functor argument (should match the type)
    # - kwargs : optional parameters dictionnary used for both instanciation of type and widgetClass
    T_FUNCTOR_ARGS = [
               ]
    
    # Those are constant argument definition used by the functor function
    # Its definition is the same as T_FUNCTOR_ARGS
    # Those arguments are not iterated by the mapping, ie their values do not change
    T_CST_ARGS = [
                  ]
    
    def __init__(self
                 , **kwargs
                 ):
        """
        Init check that all required arguments are passed. If it is the case the functor is created.
        The kwargs dict should have a key for each required functor argument defined in T_FUNC_ARGS
        and associate a key to a QArkFunctorArg object, ie : kwargs : { 'arg_key' : QArkFunctorArg() }
        """
        self.t_functorArgs = {}
        self.t_cstArgs = {}
        
        # The data to which the functor is applied
        self.o_vectorDataSet = None
        
        # The functor returned data
        self.x_fData = None
            
        # First get T_FUNCTOR_ARGS
        for t_funcArgTuple in self.__class__.getFunctorArgs():
                    
            s_funcArgKey = t_funcArgTuple[ self.U_FUNC_ARG_KEY_INDEX ]
            b_required = t_funcArgTuple[ self.U_FUNC_ARG_REQUIRED_INDEX ]
                    
            if not kwargs.has_key( s_funcArgKey ):
                if b_required:
                    raise QArkFunctorMissingRequiredFunctorArgError( self.__class__.__name__, s_funcArgKey )
                else:
                    self.t_functorArgs[ s_funcArgKey ] = None        
            else:
                # Get the QArkFunctorArg
                o_functorArg = kwargs[ s_funcArgKey ]
                self.t_functorArgs[ s_funcArgKey ] = o_functorArg.getValue()
            
        # Get the constant value parameters
        for t_cstArgTuple in self.__class__.getCstArgs():
            
            s_cstArgKey = t_cstArgTuple[ self.U_FUNC_ARG_KEY_INDEX ]
            b_required = t_cstArgTuple[ self.U_FUNC_ARG_REQUIRED_INDEX ]
                    
            if not kwargs.has_key( s_cstArgKey ):
                if b_required:
                    raise QArkFunctorMissingRequiredFunctorArgError( self.__class__.__name__, s_cstArgKey )
                else:
                    self.t_cstArgs[ s_cstArgKey ] = None        
            else:
                # Get the QArkFunctorArg
                o_cstArg = kwargs[ s_cstArgKey ]
                self.t_cstArgs[ s_cstArgKey ] = o_cstArg.getValue()
 
    @classmethod
    def constructQArkFuncArgDict(cls, **kwargs):
        """
        """
        t_args = {}
        
        for t_funcArgTuple in cls.getFunctorArgs():
                    
            s_funcArgKey = t_funcArgTuple[ cls.U_FUNC_ARG_KEY_INDEX ]
            b_required = t_funcArgTuple[ cls.U_FUNC_ARG_REQUIRED_INDEX ]
             
            if not kwargs.has_key( s_funcArgKey ):
                if b_required:
                    raise QArkFunctorMissingRequiredFunctorArgError( cls.__name__, s_funcArgKey )
                else:
                    t_args[ s_funcArgKey ] = None 
            else:
                # Get the QArkFunctorArg
                t_args[s_funcArgKey] = QArkFuncArg( s_funcArgKey, kwargs.pop(s_funcArgKey) )
         
        # Get the constant value parameters
        for t_cstArgTuple in cls.getCstArgs():
            
            s_cstArgKey = t_cstArgTuple[ cls.U_FUNC_ARG_KEY_INDEX ]
            b_required = t_cstArgTuple[ cls.U_FUNC_ARG_REQUIRED_INDEX ]
                 
            if not kwargs.has_key( s_cstArgKey ):
                if b_required:
                    raise QArkFunctorMissingRequiredFunctorArgError( cls.__name__, s_cstArgKey )
                else:
                    t_args[ s_cstArgKey ] = None     
            else:
                # Get the QArkFunctorArg
                t_args[s_cstArgKey] = QArkFuncArg( s_cstArgKey, kwargs.pop(s_cstArgKey) )
        
        return t_args
        
    def apply(self):
        """
        Apply the function and store the result into x_fData
        Its definition depends of the data type on which the functor is applied
        _x_data should have a [] operator keyable by the T_FUNCTOR_ARGS values
        """
        t_dataToMap = [ self.o_vectorDataSet[ self.t_functorArgs[s_key] ]
                       for s_key in map( lambda t:t[self.U_FUNC_ARG_KEY_INDEX], self.__class__.getFunctorArgs() )
                       ]
        self.preFunctor_wrapper(t_dataToMap)
        self.x_fData = map( self.functor_wrapper, t_dataToMap )

    def getFData(self):
        """
        Return a previous computed application of the functor on a data
        """
        return self.x_fData

    def preFunctor(self, *args):
        """
        A preparation to call before functor application
        This function can be used to store aggregation value (mean, std) from a vectorDataSet
        This function can also access other parameters (constant parameters, class parameters)
        """
        pass

    def preFunctor_wrapper(self, _t):
        """
        Another preFunctor function interface
        """
        return self.preFunctor(*_t)

    def functor(self, *args):
        """
        functor function to define
        The args parameter is the of the vectored field to pass to a mapping function
        This function can access other parameters
        """
        raise NotImplemented

    def functor_wrapper(self, _t):
        """
        Another functor function interface
        """
        return self.functor(*_t)

    @classmethod
    def getFunctorArgsInstanceOfKeys(cls, _cls_class):
        """
        Return
        """
        def instanceOf(_cls):
            if isinstance(_cls, list):
                return issubclass( _cls[0], _cls_class[0] )
            else:
                return issubclass( _cls, _cls_class )
        
        return [ t_funcArgTuple[ cls.U_FUNC_ARG_KEY_INDEX ]
                   for t_funcArgTuple in cls.getFunctorArgs()
                   if instanceOf( t_funcArgTuple[cls.U_FUNC_ARG_CLASS_INDEX] )
                ]

    @classmethod
    def getFunctorArgs(cls):
        return cls.T_FUNCTOR_ARGS

    @classmethod
    def getFunctorArgsKeys(cls):
        return map( lambda t:t[cls.U_FUNC_ARG_KEY_INDEX], cls.getFunctorArgs() )
    
    @classmethod
    def getCstArgs(cls):
        return cls.T_CST_ARGS
    
    def setDataToApply(self
                       , _o_vectorDataSet
                       ):
        """
        Set the data to which the Functor is applied
        _x_data should have a [] operator keyable by the T_FUNCTOR_ARGS values
        _x_data should inherit from QArkVectorDataSet
        """
        self.o_vectorDataSet = _o_vectorDataSet
    
    @classmethod
    def getFilteredVectorDataSetLabels(cls, _o_vectorDataSet):
        """
        Filtered the vector data set labels.
        By default returns all labels.
        This function is used by QArkFunctorFactor
        """
        return _o_vectorDataSet.getVectorLabels()
    
    def reset(self):
        self.o_vectorDataSet = None

    def toString(self):
        t_args = [ '('
                  ,','.join( [ '{0}={1}'.format(k, v) 
                              for k, v in self.t_functorArgs.iteritems()
                              ]
                            )
                  ]
        
        if len( self.t_cstArgs.keys() ) > 0:
            t_args.append(',')
        
        t_args.extend( [','.join( [ '{0}={1}'.format(k, v) 
                                    for k, v in self.t_cstArgs.iteritems()
                                    ]
                                  )
                        ,')']
                      )
        
        return '{}{}'.format( self.S_NAME,''.join(t_args))

    def toStringOnlyFuncArgs(self, _s_prefix=''):
        t_args = [ '('
                  ,','.join( [ '{0}={1}'.format(k, v) 
                              for k, v in self.t_functorArgs.iteritems()
                              ]
                            )
                  ,')'
                  ]
                   
        return '{}{}{}'.format( _s_prefix,self.S_NAME,''.join(t_args))

    def toFancyString(self):
        t_args = [ '{0}={1}'.format(k, v) 
                  for k, v in self.t_functorArgs.iteritems()
                  ]
        t_args.extend(
                 [ '{0}={1}'.format(k, v) 
                  for k, v in self.t_cstArgs.iteritems()
                  ]     
                      )
        
        return '{}\n  - {}'.format( self.S_NAME,'\n  - '.join(t_args))
