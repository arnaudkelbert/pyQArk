# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
# 
#
# Core.QArkRange
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
class QArkRange(object):
    
    def __init__(self, _x_min, _x_max):
        #self.t_range = sorted([_x_min, _x_max])
        self.t_range = [_x_min, _x_max ]
    
    def __getitem__(self, index):
        if index == 'min': index = 0
        elif index == 'max': index = 1
        return self.t_range[index]
    
    def __setitem__(self, index, value):
        if index == 'min': index = 0
        elif index == 'max': index = 1
        self.t_range[index] = value
    
    def min(self):
        return self.t_range[0]
    
    def max(self):
        return self.t_range[1]
    
    def __repr__(self):
        return self.t_range.__repr__()
    
    def __str__(self):
        return self.t_range.__str__()
