# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
# 
#
# Core.QArkFunctionFactory
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
import copy

from pyQArk.Widgets.QArkInputWidgetGrid.QArkInputWidgetGrid import QArkInputWidgetGrid
from pyQArk.Widgets.QArkInputListWidget.QArkInputListWidget import QArkInputListWidget
from pyQArk.Core.QArkFuncArg import QArkFuncArg

class QArkFunctionFactory():
    
    @classmethod
    def functionToWidget(cls
                        , parent
                        , _cls_functionClass
                        ):
        """
        Construct a generic widget to enter the function arguments
        @param _cls_functionClass : the function class for which we want to generate a widget
        """
        t_argsTuples = []
        
        if len(_cls_functionClass.getCstArgs()) == 0:
            return None
               
        # Then consruct for constant args
        for t_tuple in _cls_functionClass.getCstArgs():
            
            # Copy the kwargs dictionary
            t_widgetArgs = copy.copy( t_tuple[ _cls_functionClass.U_CST_ARG_KWARGS_INDEX ] )
            
            s_key = t_tuple[ _cls_functionClass.U_CST_ARG_KEY_INDEX ]
            s_label = t_widgetArgs.pop( '_s_label' )
            x_defaultValue = t_tuple[ _cls_functionClass.U_CST_ARG_DEFAULT_VALUE_INDEX ]
            cls_dataClass = t_tuple[ _cls_functionClass.U_CST_ARG_CLASS_INDEX ]
            cls_widgetClass = t_tuple[ _cls_functionClass.U_CST_ARG_UICLASS_INDEX ]
                        
            # If function argument class is a list we change the widget to be a list of widget
            # Note : should not be the case
            if isinstance( cls_dataClass, list ):
                
                t_widgetArgs[ '_cls_inputWidgetClass' ] = cls_widgetClass
                t_widgetArgs[ '_u_size' ] = len(cls_dataClass)
                cls_widgetClass = QArkInputListWidget
                
                # We get the actual type
                cls_dataClass = cls_dataClass[0]
                        
            t_argsTuples.append( [ s_key
                                      , cls_widgetClass
                                      , s_label
                                      , x_defaultValue
                                      , t_widgetArgs
                                      ] )

        o_widget = QArkInputWidgetGrid( parent, t_argsTuples )
        
        return o_widget
            
    @classmethod
    def widgetToFunction(cls
                        , _o_widget
                        , _cls_functionClass
                        ):
        """
        Generate a function from arguments set in a widget
        @param _o_widget : a QArkInputWidgetGrid
        @type _o_widget : L{QArkInputWidgetGrid}
        @param _cls_functionClass : function class that we want to instantiate from the widget
        @type _cls_functionClass : C{type}
        @return: the function
        @rtype: L{QArkFunction}
        """
        if _o_widget is None:
            return _cls_functionClass()
            
        t_args = _o_widget.getRegisteredValues()        
        t_functionArgs = {}
                
        for t_tuple in  _cls_functionClass.getCstArgs():
            
            s_key = t_tuple[ _cls_functionClass.U_CST_ARG_KEY_INDEX ]
            cls_dataClass = t_tuple[ _cls_functionClass.U_CST_ARG_CLASS_INDEX ]
            b_required = t_tuple[ _cls_functionClass.U_CST_ARG_REQUIRED_INDEX ]
            
            t_functionArgs[ s_key ] = QArkFuncArg( _s_key = s_key
                                                     , _x_value = t_args[s_key]
                                                     , _cls_type = cls_dataClass
                                                     , _b_required = b_required
                                                     )
        
        return _cls_functionClass( **t_functionArgs )
