# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#
#
# QArkUiLoader
#
#
# @author : Arnaud Kelbert
# @date : 2019/03/05
# @version : 0.2
#
# Historic:
# 0.2 : init version
# -----------------------------------------------------------------------
# {-- Python 2/3 compatibility ------------------------------------------
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
# }-- Python 2/3 compatibility ------------------------------------------
import inspect
import os
import datetime
import importlib
from pyQArk.QArkConfig import QARK_QT_MODULE_PREFIX
from pyQArk.Core.QArkUiCompiler import QArkUiCompiler

def loadUi(_s_uiFile, pkgname, **kwargs):
    """
    Load a ui file. Tries to load corresponding compiled python file according
    to pyQArk naming.
    If python file does not exists then a compilation is performed using QArkUiCompiler
    module.

    Args:
        _s_uiFile (str): ui file path
        pkgname (str): parent package name (used for import)

    Returns:
        The python class corresponding to the ui.
    """
    try:
        s_kwClassname = kwargs.pop('classname')
    except KeyError:
        s_kwClassname = None
    o_uimdate = datetime.datetime.fromtimestamp(os.path.getmtime(_s_uiFile))
    b_compile = False
    s_pyfile = QArkUiCompiler.autoname(_s_uiFile)
    # Check if python file exists
    if not os.path.exists( s_pyfile ):
        b_compile = True
    else:
        # Check if ui file has been modified since last compilation
        o_pymdate = datetime.datetime.fromtimestamp(os.path.getmtime(s_pyfile))
        if o_uimdate > o_pymdate:
            # Ui file has been modified -> recompile
            print('Ui file date is newer than its compiled python file')
            b_compile = True
    if b_compile:
        print('Compilation of ui file {}'.format(_s_uiFile))
        QArkUiCompiler.compile(_s_uiFile, s_pyfile, **kwargs)

    # Import the module
    s_mod = os.path.basename(s_pyfile).split('.')[0]
    #print('module:{}\npck : {}'.format(s_mod, pkgname))
    #s_mod = s_mod.replace(QARK_QT_MODULE_PREFIX,'')
    o_mod = importlib.import_module(pkgname+'.'+s_mod, pkgname)

    # Find the class
    t_members = inspect.getmembers(o_mod, inspect.isclass)
    assert(len(t_members)>0)
    if len(t_members) == 1:
        return t_members[0][1]
    else:
        if s_kwClassname is None:
            raise Exception('You should give the name of the compiled class to the loadUi method (classname parameter)')
        try:
            return [m[1] for m in t_members if m[0] == 'Ui_{}'.format(s_kwClassname)][0]
        except Exception as e:
            raise Exception('Cannot find class Ui_{} : \n{}'.format(s_kwClassname, str(e)))

