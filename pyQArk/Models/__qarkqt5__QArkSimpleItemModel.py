# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#
#
# QArkSimpleItemModel
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
from PyQt5 import QtCore


class QArkSimpleItemModel( QtCore.QAbstractItemModel ):
    """
    A simple item model implementation with 1 row and 1 column
    """

    def __init__( self
                 , parent
                 , _o_item
                 ):
        """
        @brief Constructor
        @param parent : parent QObject
        @type parent : L{QtCore.QObject)
        @param _o_item : an item
        @type _o_item : C{object}
        """
        super( QArkSimpleItemModel, self ).__init__(parent)
        self.o_item = _o_item

    def getItem(self):
        return self.o_item

    def rowCount( self, parent ):
        """
        Returns number of rows. Here always returns 1.
        @param parent : parent QObject
        @type parent : L{QtCore.QObject)
        """
        return 1

    def columnCount( self, parent ):
        """
        Returns number of columns. Here always returns 1.
        @param parent : parent QObject
        @type parent : L{QtCore.QObject)
        """
        return 1

    def data( self, index, role ):
        """
        Simple implementation of data method.
        Just show the string representation of the item for a DisplayRole
        Other roles returns a QVariant object
        @param index : Index to perform
        @type index : C{int}
        @param role : Qt Role
        @type index : C{int}
        """
        if role == QtCore.Qt.DisplayRole:
            return self.getDisplayRoleData( index )

        if role == QtCore.Qt.DecorationRole:
            return self.getDecorationRoleData( index )

        return QtCore.QVariant()

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
        return QtCore.QVariant()
