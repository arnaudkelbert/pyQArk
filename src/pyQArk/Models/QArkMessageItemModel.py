# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#
#
# QArkMessageItemModel
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
from PyQt5 import QtCore, QtGui

from pyQArk.Models.QArkSimpleItemModel import QArkSimpleItemModel


class QArkMessageItemModel( QArkSimpleItemModel ):
    """
    A simple item model implementation with 1 row and 1 column
    """

    def getDisplayRoleData( self, index ):
        """
        New method used by data in a display role
        This method should be overwritten for subclasses.
        @param index : Index to perform
        @type index : C{int}
        """
        return '{}'.format( self.o_item )


    def getDecorationRoleData( self, index ):
        """
        New method used by data in a decoration role (icon or other)
        This method should be overwritten for subclasses.
        @param index : Index to perform
        @type index : C{int}
        """
        return QtGui.QIcon.fromTheme("dialog-information")
