# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#
#
# QArkPlotableObjectTreeItem
#
# Tree item for QArkPlotableObject
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

from pyQArk.Core.QArkMimeData import QArkMimeData

class QArkPlotableObjectTreeItem( object ):

    def __init__( self
                 , parent
                 , _o_data
                 ):
        """
        The constructor is only used to record the item's parent and
        the data associated with each column.
        """
        self.o_parentItem = parent
        self.o_data = _o_data
        self.t_childItems = []
        self.setChildClass( self.__class__ )

    def getChildren(self):
        return self.t_childItems

    def setParent(self, parent):
        self.o_parentItem = parent

    def getItemData(self):
        return self.o_data

    def setChildClass( self, _cls_childClass ):
        """
        """
        self.cls_childClass = _cls_childClass

    def getChildClass( self ):
        return self.cls_childClass

    def isItemMultiDimensional( self ):
        """
        """
        return isinstance(self.o_data, list) or isinstance(self.o_data,tuple)

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

    def childNumber( self ):
        """
        The childNumber() function is used to determine the index of the
        child in its parent's list of children.
        It accesses the parent's childItems member directly to obtain
        this information
        """
        if self.o_parentItem:
            return self.o_parentItem.t_childItems.index( self )

        # The root item has no parent item; for this item, we return
        # zero to be consistent with the other items.
        return 0

    def row( self ):
        """
        The row() function reports the item's location within its parent's list of items

        Note that, although the root item (with no parent item) is
        automatically assigned a row number of 0, this information is
        never used by the model.
        """
        if not self.o_data is None and not self.o_parentItem is None:
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
        if not self.o_data is None:
            if self.isItemMultiDimensional():
                return len(self.o_data)
            else:
                return 1
        else:
            return 1

    def data( self, _u_index, role ):
        """
        Column data is returned by the data() function
        """
        if role == QtCore.Qt.DisplayRole:
            return self.dataDisplayRole(_u_index)

        if role == QtCore.Qt.EditRole:
            return self.dataEditRole(_u_index)

        if role == QtCore.Qt.UserRole:
            return self.dataUserRole(_u_index)

        if role == QtCore.Qt.DecorationRole:
            return self.dataDecorationRole(_u_index)

        if role == QtCore.Qt.CheckStateRole:
            return self.dataCheckStateRole(_u_index)

        return QtCore.QVariant()

    def dataEditRole( self, _u_index ):
        if self.isItemMultiDimensional():
            return str(self.o_data[_u_index])
        else:
            return str(self.o_data)

    def dataUserRole( self, _u_index ):
        return QtCore.QVariant()

    def dataDisplayRole( self, _u_index ):
        if self.isItemMultiDimensional():
            return str(self.o_data[_u_index])
        else:
            return str(self.o_data)

    def dataDecorationRole( self, _u_index ):
        return QtCore.QVariant()

    def dataCheckStateRole( self, _u_index ):
        return QtCore.QVariant()

    def parent( self ):
        """
        The item's parent is found with parent()
        """
        return self.o_parentItem

    def setData( self, _u_index, _x_value, role ):
        """
        Data is set using the setData() function, which only stores
        values in the itemData list for valid list indexes, corresponding
        to column values in the model

        To make implementation of the model easier, we return true to
        indicate whether the data was set successfully, or false if
        an invalid column
        """
        if _u_index < 0 or _u_index >= self.columnCount():
            return False

        if role == QtCore.Qt.DisplayRole:
            return self.setDataDisplayRole(_u_index, _x_value)

        if role == QtCore.Qt.EditRole:
            return self.setDataEditRole(_u_index, _x_value)

        if role == QtCore.Qt.UserRole:
            return self.setDataUserRole(_u_index, _x_value)

        if role == QtCore.Qt.DecorationRole:
            return self.setDataDecorationRole(_u_index, _x_value)

        if role == QtCore.Qt.CheckStateRole:
            return self.setDataCheckStateRole(_u_index, _x_value)

        return False

    def setDataDisplayRole( self, _u_index, _x_value ):
        return False

    def setDataEditRole( self, _u_index, _x_value ):
        if self.isItemMultiDimensional():
            self.o_data[ _u_index ] = _x_value
        else:
            self.o_data = _x_value
        return True

    def setDataUserRole( self, _u_index, _x_value ):
        return False

    def setDataDecorationRole( self, _u_index, _x_value ):
        return False

    def setDataCheckStateRole( self, _u_index, _x_value ):
        return False

    def insertChildren( self
                       , _u_position
                       , _u_count
                       , _u_columns
                       ):
        """
        Editable models often need to be resizable, enabling rows and
        columns to be inserted and removed. The insertion of rows
        beneath a given model index in the model leads to the insertion
        of new child items in the corresponding item, handled by the
        insertChildren() function
        """
        if _u_position < 0 or _u_position > self.childCount():
            return False
        for u_row in range( _u_count ):
            if _u_columns > 1:
                o_data = [ QtCore.QVariant() ]*_u_columns
            else:
                o_data = QtCore.QVariant()
            o_item = self.cls_childClass( self, o_data )
            self.t_childItems.insert( _u_position, o_item )
        return True

    def  removeChildren( self
                        , _u_position
                        , _u_count
                        ):
        """
        """
        if _u_position < 0 or _u_position + _u_count > self.childCount():
            return False
        for _ in range( _u_count ):
            self.t_childItems.pop( _u_position )
        return True

    def removeChild( self, _o_child ):
        """
        """
        u_position = self.childNumber()
        if u_position >= 0:
            self.removeChildren( u_position, 1 )

    def insertColumns( self
                      , _u_position
                      , _u_columns
                      ):
        """
        """
        if _u_columns < 0 or _u_columns >= self.columnCount():
            return False

        if _u_columns > 0 and not self.isItemMultiDimensional():
            self.o_data = [ self.o_data ]

        for _ in range(_u_columns):
            self.o_data.insert( _u_position, QtCore.QVariant() )

        for o_child in self.t_childItems:
            o_child.insertColumns( _u_position, _u_columns )

        return True

    def cloneItemOnly( self, parent ):
        """
        Only clone item (and keep data reference)
        Can be used during drag'n drop
        """
        o_item = self.__class__( parent, self.o_data )
        o_item.setChildClass( self.cls_childClass )

        for o_child in self.t_childItems:
            o_item.appendChild( o_child.cloneItemOnly(o_item) )

        return o_item

    def checkDataForwardExists( self, _o_nodeToCheck ):
        """
        Test if _o_nodeToCheck data exists in current Node or
        one of its child
        """
        b_ret = False
        o_existingItem = None

        if self.getItemData() is _o_nodeToCheck.getItemData():
            b_ret = True
            o_existingItem = self

        else:
            for o_child in self.t_childItems:
                b_ret, o_existingItem = o_child.checkDataForwardExists( _o_nodeToCheck )
                if b_ret:
                    break

        return b_ret, o_existingItem

    def checkDataBackwardExists( self, _o_nodeToCheck ):
        """
        Test if one of _o_nodeToCheck data or childs data exists in current Node
        or one of its child
        It also return the node
        """
        b_ret = False
        o_existingItem = None

        b_ret, o_existingItem = self.checkDataForwardExists( _o_nodeToCheck )

        if not b_ret:
            for o_child in _o_nodeToCheck.t_childItems:
                b_ret, o_existingItem = self.checkDataBackwardExists( o_child )

                if b_ret:
                    break

        return b_ret, o_existingItem

    def getListOfItemDataIsInstance( self, _cls_class, _t_items ):
        """
        Returns all items from _o_item whose data are instance of
        class _cls_class
        _t_items is the list to fill
        """
        if isinstance(self.getItemData(), _cls_class):
            _t_items.append( self )

        for o_child in self.getChildren():
            o_child.getListOfItemDataIsInstance( _cls_class, _t_items )
