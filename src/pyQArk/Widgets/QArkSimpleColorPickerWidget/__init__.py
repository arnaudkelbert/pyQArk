# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#
#
# __init__.py
#
#
# @author : Arnaud Kelbert
# @date : 2019/03/05
# @version : 0.2
#
# Historic:
# 0.2 : init version
#
# This __init__ is defined to support both PyQt4 and PyQt5
# It enables to import modules from name without __qarkqt{}__ prefix
#
#-----------------------------------------------------------------------
import os
import sys
import inspect
import pkgutil
import importlib
from pyQArk.QArkConfig import QARK_QT_MODULE_PREFIX
LOCAL_PATH = os.path.abspath(os.path.join( inspect.getfile(inspect.currentframe()), '..' ))
def PKGPATH(_s_file): return os.path.normpath(os.path.join(LOCAL_PATH, _s_file))

# Local package specifics
#=> must load QArkInputWidget first
T_DO_FIRST = [
]
T_MODULE_NAMES_FIRST = [ '{}{}'.format(QARK_QT_MODULE_PREFIX,n) for n in T_DO_FIRST ]
T_MODULE_NAMES = T_MODULE_NAMES_FIRST + [ n for (_,n,_) in pkgutil.iter_modules([LOCAL_PATH]) if not n in T_MODULE_NAMES_FIRST ]

for name in T_MODULE_NAMES:
    if name.startswith(QARK_QT_MODULE_PREFIX):
        # import the module
        imported_module = importlib.import_module('.'+name, package=__name__)
        # add an attribute to the current package to module with name without prefix
        setattr(sys.modules[__name__], name[len(QARK_QT_MODULE_PREFIX):], imported_module)
        # find all references to the module with a prefixed name and replace them without prefix
        refs = [k for k in sys.modules.keys() if '{}.{}'.format(__name__,name) in k]
        for entry in refs:
            sys.modules[entry.replace('{}.{}'.format(__name__,QARK_QT_MODULE_PREFIX),'{}.'.format(__name__))] = sys.modules[entry]
            # erase reference with prefix
            #print('***',entry.replace('{}.{}'.format(__name__,QARK_QT_MODULE_PREFIX),'{}.'.format(__name__)), entry, sys.modules[entry])
            del sys.modules[entry]