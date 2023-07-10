# -*- coding: utf-8 -*-
import sys
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

if QARK_PYQT5_AVAILABLE:
    QARK_QT_GENERATION = 5
else:
    QARK_QT_GENERATION = -1

# Threading mechanism preferences
QARK_QT_THREADING_QTHREAD_SUBCLASSING\
, QARK_QT_THREADING_EVENT_DRIVEN = range(2)

if QARK_QT_GENERATION == 5:
    QARK_QT_THREADING_MECHANISM = QARK_QT_THREADING_EVENT_DRIVEN
    #QARK_QT_THREADING_MECHANISM = QARK_QT_THREADING_QTHREAD_SUBCLASSING

# Setting matplotlib backends
import matplotlib
if QARK_QT_GENERATION == 5:
    try:
        matplotlib.use('QT5Agg')
    except:
        pass
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

QARK_ROOT_DIR = os.path.normpath( os.path.join( os.path.abspath( inspect.stack()[0][1] ), '..' ) )

try:
    QARK_EXTENSION_DIR = os.environ['PYQARK_EXTENSION_DIR']
except:
    QARK_EXTENSION_DIR = QARK_ROOT_DIR

QARK_RESSOURCES_DIR = os.path.join( QARK_EXTENSION_DIR, 'Ressources' )
QARK_ICONS_DIR = os.path.join( QARK_RESSOURCES_DIR, 'icons' )
QARK_MEDIA_LOADER_GIF = os.path.join( QARK_RESSOURCES_DIR, 'loader.gif' )