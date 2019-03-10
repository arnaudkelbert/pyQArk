# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#
#
# QArkSimpleItemListModel
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
from PyQt4 import QtCore

from .QArkSimpleItemModel import QArkSimpleItemModel


class QArkSimpleItemListModel( QtCore.QAbstractListModel ):
    """
    Implementation of a list model to handle QArkSimpleItemModel elements
    """

    def __init__( self
                 , parent
                 , _t_items
                 ):
        """
        @brief Constructor
        @param parent : parent QObject
        @type parent : L{QtCore.QObject)
        @param _t_items : list of items
        @type _t_items : C{list}
        """
        super( QArkSimpleItemListModel, self ).__init__(parent)
        self.t_items = _t_items

    def rowCount( self, parent ):
        """
        Returns number of rows, ie the number of items
        @param parent : parent QObject
        @type parent : L{QtCore.QObject)
        """
        return len(self.t_items)

    def columnCount( self, parent ):
        """
        Returns number of rows. Here always returns 1.
        @param parent : parent QObject
        @type parent : L{QtCore.QObject)
        """
        return 1

    def data( self, index, role ):
        """
        Simple implementation of data method.
        Just calls the data of the item
        @param index : Index to perform
        @type index : L{QtCore.QModelIndex}
        @param role : Qt Role
        @type index : C{int}
        """
        if not index.isValid():
            return QtCore.QVariant()

        return self.t_items[index.row()].data( index.column(), role )

    def addItem( self, _o_item ):
        """
        Method to add an item
        @param _o_item : the item to add
        @type _o_item : L{QArkSimpleItemModel}
        """
        self.beginInsertRows( QtCore.QModelIndex(), len(self.t_items), len(self.t_items))
        self.t_items.append( _o_item )
        self.endInsertRows()

    def getItem( self, o_index ):
        """
        Since the model's interface to the other model/view components
        is based on model indexes, and the internal data structure is
        item-based, many of the functions implemented by the model need
        to be able to convert any given model index to its corresponding
        item. For convenience and consistency, we have defined a getItem()
        function to perform this repetitive task

        This function assumes that each model index it is passed
        corresponds to a valid item in memory. If the index is invalid,
        or its internal pointer does not refer to a valid item, None is returned.
        """
        u_row = o_index.row()

        if u_row < 0 or u_row >= len( self.t_items):
            return None

        return self.t_items[o_index.row()].getItem()

