# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#
#
# QArkTreeItemModel
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

class QArkTreeItem( object ):

    def __init__( self
                 , parent
                 , _t_items
                 ):
        """
        The constructor is only used to record the item's parent and
        the data associated with each column.
        """
        self.o_parentItem = parent
        self.t_items = _t_items

        self.t_childItems = []



    def appendChild( self, _o_item ):
        """
        Since each of the child items are constructed when the model is
        initially populated with data, the function to add child items
        is straightforward:
        """
        self.t_childItems.append( _o_item )



    def child( self, _u_row ):
        """
        Each item is able to return any of its child items when given a
        suitable row number.

        The child() function returns the child that corresponds to the
        specified row number in the item's list of child items
        """
        return self.t_childItems[ _u_row ]



    def childCount( self ):
        """
        The number of child items held can be found with childCount()
        """
        return len(self.t_childItems)



    def row( self ):
        """
        The row() function reports the item's location within its parent's list of items

        Note that, although the root item (with no parent item) is
        automatically assigned a row number of 0, this information is
        never used by the model.
        """
        if not self.o_parentItem is None:
            try:
                return self.o_parentItem.t_childItems.index( self )

            except:
                return 0

        return 0



    def columnCount( self ):
        """
        The number of columns of data in the item is trivially returned
        by the columnCount() function.
        """
        if isinstance(self.t_items, list):
            return len(self.t_items)

        else:
            return 1



    def data( self, _u_index ):
        """
        Column data is returned by the data() function
        """
        try:
            return self.t_items[_u_index]

        except:
            return QtCore.QVariant()



    def parent( self ):
        """
        The item's parent is found with parent()
        """
        return self.o_parentItem




