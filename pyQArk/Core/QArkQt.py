# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#
#
# QArkQt
#
#
# @author : Arnaud Kelbert
# @date : 2021/10/29
# @version : 0.1
#
# Historic:
# 0.1 : init version
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

def _exec(obj,*args,**kwargs):
    if hasattr(obj, 'exec'):
        return obj.exec(*args, **kwargs)
    elif hasattr(obj, 'exec_'):
        return obj.exec_(*args, **kwargs)
