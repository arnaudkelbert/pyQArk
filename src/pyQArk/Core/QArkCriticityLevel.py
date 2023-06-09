# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#
#
# QArkCriticityLevel
#
#
#-----------------------------------------------------------------------
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

class QArkCriticityLevel(object):
    DEFAULT = 0
    CATASTROPHIC = 1
    DISASTER = 2
    EXTREMELY_CRITICAL = 3
    VERY_CRITICAL = 4
    CRITICAL = 5
    VERY_HIGH = 6
    HIGH = 7
    MEDIUM = 8
    LOW = 9
    NEGLIGIBLE = 10
    OK = 11
    VERY_OK = 12
    EXCLAMATION = 13