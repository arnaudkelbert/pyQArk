# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
# 
#
# Core.QArkFuncArg
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
class QArkFuncArg( object ):
    
    def __init__(self, _s_key, _x_value=None, _cls_type=None, _b_required = True,  **kwargs ):
        self.s_key = _s_key
        self.cls_type = _cls_type
        self.x_value = _x_value
        self.b_required = _b_required
    
    def getKey(self):
        return self.s_key
    
    def setKey(self, _s_key):
        self.s_key = _s_key
    
    def getType(self):
        return self.cls_type
    
    def setType(self, _cls_type):
        self.cls_type = _cls_type
    
    def getValue(self):
        return self.x_value
    
    def setValue(self, _x_value):
        self.x_value = _x_value

    def isRequired(self):
        return self.b_required
    
    def setRequired(self, _b_bool):
        self.b_required = _b_bool
