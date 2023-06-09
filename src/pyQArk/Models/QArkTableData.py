# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#
#
# QArkTableData
#
# Virtual class for data used in table view
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
#}-- Python 2/3 compatibility ------------------------------------------
class QArkTableData(object):
    def __init__(self, *args, **kwargs):
        pass

    def cell(self, _row, _col):
        """
        This method must be defined
        """
        raise NotImplemented

    def criticityLevel(self, _row, _col):
        raise NotImplemented