# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#
#
# QArkHTTPUser
#
#
# @author : Arnaud Kelbert
# @date : 2019/03/16
# @version : 0.2
#
# Historic:
# 0.2 : init version
#-----------------------------------------------------------------------
# {-- Pyhton 2/3 compatibility ------------------------------------------
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
# }-- Pyhton 2/3 compatibility ------------------------------------------

class QArkHTTPUser(object):
    """
    Class QArkHTTPUser
    Definition of a HTTP User
    """

    def __init__(self, _s_username, _s_pwd):
        """
        Constructor

        Args:
            _s_username (:obj:str): username
            _s_pwd (:obj:pwd): user password
        """
        self.s_username = _s_username
        self.s_pwd = _s_pwd
    