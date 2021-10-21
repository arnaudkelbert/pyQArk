# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#
#
# QArkConfig
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
import inspect

if sys.platform in ['win32', 'win64']:
    QARK_PLATFORM = 'win'
elif os.name == 'posix':
    QARK_PLATFORM = 'posix'

try:
    import PyQt5
    QARK_PYQT5_AVAILABLE = True
except ImportError:
    QARK_PYQT5_AVAILABLE = False

try:
    import PyQt4
    QARK_PYQT4_AVAILABLE = True
except ImportError:
    QARK_PYQT4_AVAILABLE = False

if QARK_PYQT5_AVAILABLE:
    QARK_QT_GENERATION = 5
elif QARK_PYQT4_AVAILABLE:
    QARK_QT_GENERATION = 4
    # For matplotlib deprecation
    import PyQt4
else:
    QARK_QT_GENERATION = -1
    # For matplotlib deprecation
    import PyQt5

if QARK_QT_GENERATION == 5:
    QARK_QT_MODULE_PREFIX = '__qarkqt5__'
if QARK_QT_GENERATION == 4:
    QARK_QT_MODULE_PREFIX = '__qarkqt4__'

# Threading mechanism preferences
QARK_QT_THREADING_QTHREAD_SUBCLASSING\
, QARK_QT_THREADING_EVENT_DRIVEN = range(2)

if QARK_QT_GENERATION == 5:
    QARK_QT_THREADING_MECHANISM = QARK_QT_THREADING_EVENT_DRIVEN
    #QARK_QT_THREADING_MECHANISM = QARK_QT_THREADING_QTHREAD_SUBCLASSING
elif QARK_QT_GENERATION == 4:
    QARK_QT_THREADING_MECHANISM = QARK_QT_THREADING_QTHREAD_SUBCLASSING

# Setting matplotlib backends
import matplotlib
if QARK_QT_GENERATION == 5:
    matplotlib.use('QT5Agg')
elif QARK_QT_GENERATION == 4:
    matplotlib.use('QT4Agg')
# Tell matplotlib to use PyQt (instead of PySide if installed)
# This line is deprecated :
# => import Qt binding or set QT_API environment variable
try:
    QARK_QT_API = os.environ['QT_API']
    b_qtApiSet = True
except:
    QARK_QT_API = None
    b_qtApiSet = False
if not QARK_QT_API == 'PyQt{}'.format(QARK_QT_GENERATION):
    try:
        matplotlib.rcParams['backend.qt{}'.format(QARK_QT_GENERATION)] = 'PyQt{}'.format(QARK_QT_GENERATION)
    except KeyError as e:
        print('Cannot set matplotlib rcParams for key {}'.format('backend.qt{}'.format(QARK_QT_GENERATION)))
    #raise
    #print(matlotlib.rc)

# Qt4/5 compatibility
# List of widgets that have been moved from QtGui to QtWidgets
#T_QARK_QTWIDGETS={}
# def QARK_QTWIDGETS(name):
#     global T_QARK_QTWIDGETS
#     try:
#         return T_QARK_QTWIDGETS
#     except KeyError:
#
#     s = name.split('.')[1]
#     try:
#         return [ (n,o) for n,o in inspect.getmembers(QtWidgets) if n == s ][0][1]
#     except IndexError:
#         return [ (n,o) for n,o in inspect.getmembers(QtGui) if n == s ][0][1]
#QARK_QT_WIDGETS = {}
#if QARK_QT_GENERATION == 5:
#    import PyQt5.QtWidgets
#    QARK_QT_WIDGETS['QApplication'] = PyQt5.QtWidgets.QApplication
#    for n, o in inspect.getmembers(PyQt5.QtWidgets):
#        if inspect.isclass(o) and (issubclass(o, PyQt5.QtWidgets.QWidget) \
#                                   or issubclass(o, PyQt5.QtWidgets.QLayout)\
#                                   ):
#            QARK_QT_WIDGETS[o.__name__] = o
#if QARK_QT_GENERATION == 4:
#    import PyQt4.QtGui
#    QARK_QT_WIDGETS['QApplication'] = PyQt4.QtGui.QApplication
#    for n, o in inspect.getmembers(PyQt4.QtGui):
#        if inspect.isclass(o) and (issubclass(o, PyQt4.QtGui.QWidget) \
#                                   or issubclass(o, PyQt4.QtGui.QLayout)\
#                                   ):
#            QARK_QT_WIDGETS[o.__name__] = o

QARK_ROOT_DIR = os.path.normpath( os.path.join( os.path.abspath( inspect.stack()[0][1] ), '..' ) )

try:
    QARK_EXTENSION_DIR = os.environ['PYQARK_EXTENSION_DIR']
except:
    QARK_EXTENSION_DIR = QARK_ROOT_DIR

QARK_RESSOURCES_DIR = os.path.join( QARK_EXTENSION_DIR, 'Ressources' )
QARK_ICONS_DIR = os.path.join( QARK_RESSOURCES_DIR, 'icons' )
QARK_MEDIA_LOADER_GIF = os.path.join( QARK_RESSOURCES_DIR, 'loader.gif' )