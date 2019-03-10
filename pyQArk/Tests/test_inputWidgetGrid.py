# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
# 
#
# Tests.test_inputWidgetGrid
# 
#
# @author : Arnaud Kelbert
# @date : Nov 21, 2014
# @version : 0.1
#-----------------------------------------------------------------------
import sys
import os

from PyQt4 import QtCore, QtGui

from pyQArk.Widgets.QArkInputWidgetGrid.QArkInputWidgetGrid import QArkInputWidgetGrid
from pyQArk.Widgets.QArkInputWidget.QArkBooleanCheckBoxWidget import QArkBooleanCheckBoxWidget
from pyQArk.Widgets.QArkInputWidget.QArkFloatLineEditWidget import QArkFloatLineEditWidget
from pyQArk.Widgets.QArkInputWidget.QArkFloatSpinBoxWidget import QArkFloatSpinBoxWidget
from pyQArk.Widgets.QArkInputWidget.QArkIntegerSpinBoxWidget import QArkIntegerSpinBoxWidget
from pyQArk.Widgets.QArkInputWidget.QArkIntegerLineEditWidget import QArkIntegerLineEditWidget
from pyQArk.Widgets.QArkInputWidget.QArkStringComboBoxWidget import QArkStringComboBoxWidget
from pyQArk.Widgets.QArkInputWidget.QArkStringLineEditWidget import QArkStringLineEditWidget
from pyQArk.Widgets.QArkInputWidget.QArkStringLineEditRangeWidget import QArkStringLineEditRangeWidget
from pyQArk.Widgets.QArkInputListWidget.QArkInputListWidget import QArkInputListWidget
from pyQArk.Core.QArkRange import QArkRange

__version__ = "0.1.0"

COMPANY = "PYQARK"
DOMAIN = "NONE"
APPNAME = "QARKTEST"

def main():

    o_app = QtGui.QApplication( sys.argv )
    QtCore.QSettings.setDefaultFormat( QtCore.QSettings.IniFormat )

    o_app.setOrganizationName( COMPANY )
    o_app.setOrganizationDomain( DOMAIN )
    o_app.setApplicationName( APPNAME )

    o_mainWindow = QtGui.QDialog()
    
    o_layout = QtGui.QVBoxLayout(o_mainWindow)
    
    o_widget = QArkInputWidgetGrid( o_mainWindow
                                     , [
                                        ( 'key0', QArkBooleanCheckBoxWidget, 'check me', True, {})
                                        , ( 'key1', QArkFloatLineEditWidget, 'float', 1.2, {})
                                        , ( 'key2', QArkIntegerLineEditWidget, 'int', 10, {})
                                         , ( 'key3', QArkInputListWidget, 'var', '3.', { '_cls_inputWidgetClass' : QArkFloatLineEditWidget
                                                                                              , '_u_size' : 1
                                                                                              } )
                                        , ( 'key4', QArkStringLineEditWidget, 'str', 'test', {})
                                        , ( 'key5', QArkStringComboBoxWidget, 'combo', [ 'c1', 'c2', 'c3'], {} )
					, ( 'key6', QArkStringLineEditRangeWidget, 'range', QArkRange(2.,5.3), {} )
					, ( 'key7', QArkFloatSpinBoxWidget, 'fspinbox', 3, {} )
					, ( 'key8', QArkIntegerSpinBoxWidget, 'ispinbox', 4., {} )
                                        ])
#    o_widget = QArkInputWidgetGrid( o_mainWindow
#                                    , [
#                                         ( 'key3', QArkInputListWidget, 'var', 'test_var', { '_cls_inputWidgetClass' : QArkFloatLineEditWidget
#                                                                                             , '_u_size' : 2
#                                                                                             } )
#
#                                       ])
    o_layout.addWidget(o_widget)    
    o_mainWindow.setLayout(o_layout)
    o_mainWindow.setWindowTitle( APPNAME )    
    o_mainWindow.show()

    o_widget.registerValues()
    
    print( 'before' )
    print( o_widget.getRegisteredValues() )
    #{'key3': [3.0], 'key2': 10, 'key1': 1.2, 'key0': True, 'key5': 'c1', 'key4': 'test'}
    t_v = o_widget.getRegisteredValues()
    t_v['key3'][0] += 0.5
    t_v['key2'] = 11
    t_v['key1'] *= 2
    t_v['key0'] = False
    t_v['key5'] = 'c2'
    t_v['key4'] = 'replace test'
    t_v['key6'] = QArkRange(3., 6.2)
    t_v['key7'] = 23.53211
    t_v['key8'] = 5

    o_widget.setValues( t_v )
    
    print( 'after' )
    o_widget.registerValues()
    print( o_widget.getRegisteredValues() )
    
    o_app.exec_()
    os._exit(0)

if __name__ == '__main__':
    main()
