# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
# 
#
# Core.QArkFunctorFactory
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
import copy

from pyQArk.Widgets.QArkInputWidgetGrid.QArkInputWidgetGrid import QArkInputWidgetGrid
from pyQArk.Widgets.QArkInputListWidget.QArkInputListWidget import QArkInputListWidget
from pyQArk.Core.QArkFuncArg import QArkFuncArg

class QArkFunctorFactory():
    
    @classmethod
    def functorToWidget(cls
                        , parent
                        , _cls_functorClass
                        , _o_vectorDataSet
                        ):
        """
        Construct a generic widget to enter the functor arguments
        @param _cls_functorClass : the functor class for which we want to generate a widget
        @param _x_data : the data on which we want the functor to be applied
        """
        t_argsTuples = []
        
        # First construct widget for T_FUNC_ARGS
        for t_tuple in _cls_functorClass.getFunctorArgs():
            
            # Copy the kwargs dictionary
            t_widgetArgs = copy.copy( t_tuple[ _cls_functorClass.U_FUNC_ARG_KWARGS_INDEX ] )
            
            s_key = t_tuple[ _cls_functorClass.U_FUNC_ARG_KEY_INDEX ]
            s_label = t_widgetArgs.pop( '_s_label' )
            x_defaultValue = t_tuple[ _cls_functorClass.U_FUNC_ARG_DEFAULT_VALUE_INDEX ]
            cls_dataClass = t_tuple[ _cls_functorClass.U_FUNC_ARG_CLASS_INDEX ]
            cls_widgetClass = t_tuple[ _cls_functorClass.U_FUNC_ARG_UICLASS_INDEX ]
            
            # If functor argument class is a list we change the widget to be a list of widget
            # @see Widgets.QArkInputListWidget.QArkInputListWidget
            if isinstance( cls_dataClass, list ):
                
                t_widgetArgs[ '_cls_inputWidgetClass' ] = cls_widgetClass
                t_widgetArgs[ '_u_size' ] = len(cls_dataClass)
                cls_widgetClass = QArkInputListWidget
                
                # We get the actual type
                cls_dataClass = cls_dataClass[0]
            
            # Here we have functor args (not cst args)
            # We force x_defaultValue with vector labels
            # The affected widget should be a combobox or something like that
            x_defaultValue = _cls_functorClass.getFilteredVectorDataSetLabels( _o_vectorDataSet )

            t_argsTuples.append( [ s_key
                                      , cls_widgetClass
                                      , s_label
                                      , x_defaultValue
                                      , t_widgetArgs
                                      ] )
        
        # Then consruct for constant args
        for t_tuple in _cls_functorClass.getCstArgs():
            
            # Copy the kwargs dictionary
            t_widgetArgs = copy.copy( t_tuple[ _cls_functorClass.U_FUNC_ARG_KWARGS_INDEX ] )
            
            s_key = t_tuple[ _cls_functorClass.U_FUNC_ARG_KEY_INDEX ]
            s_label = t_widgetArgs.pop( '_s_label' )
            x_defaultValue = t_tuple[ _cls_functorClass.U_FUNC_ARG_DEFAULT_VALUE_INDEX ]
            cls_dataClass = t_tuple[ _cls_functorClass.U_FUNC_ARG_CLASS_INDEX ]
            cls_widgetClass = t_tuple[ _cls_functorClass.U_FUNC_ARG_UICLASS_INDEX ]
            
            # If functor argument class is a list we change the widget to be a list of widget
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
    def widgetToFunctor(cls
                        , _o_widget
                        , _cls_functorClass
                        ):
        """
        Generate a functor from arguments set in a widget
        @param _o_widget : a QArkInputWidgetGrid
        @type _o_widget : L{QArkInputWidgetGrid}
        @param _cls_functorClass : functor class tha we want to instanciate from the widget
        @type _cls_functorClass : C{type}
        @return: the functor
        @rtype: L{QArkFunctor}
        """
        t_args = _o_widget.getRegisteredValues()
        
        t_functorArgs = {}
        
        for t_tuple in  _cls_functorClass.getFunctorArgs():
            
            s_key = t_tuple[ _cls_functorClass.U_FUNC_ARG_KEY_INDEX ]
            cls_dataClass = t_tuple[ _cls_functorClass.U_FUNC_ARG_CLASS_INDEX ]
            b_required = t_tuple[ _cls_functorClass.U_FUNC_ARG_REQUIRED_INDEX ]
            
            t_functorArgs[ s_key ] = QArkFuncArg( _s_key = s_key
                                                     , _x_value = t_args[s_key]
                                                     , _cls_type = cls_dataClass
                                                     , _b_required = b_required
                                                     )
        
        
        for t_tuple in  _cls_functorClass.getCstArgs():
            
            s_key = t_tuple[ _cls_functorClass.U_FUNC_ARG_KEY_INDEX ]
            cls_dataClass = t_tuple[ _cls_functorClass.U_FUNC_ARG_CLASS_INDEX ]
            b_required = t_tuple[ _cls_functorClass.U_FUNC_ARG_REQUIRED_INDEX ]
            
            t_functorArgs[ s_key ] = QArkFuncArg( _s_key = s_key
                                                     , _x_value = t_args[s_key]
                                                     , _cls_type = cls_dataClass
                                                     , _b_required = b_required
                                                     )
        
        return _cls_functorClass( **t_functorArgs )
