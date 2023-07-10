# -*- coding: utf-8 -*-
from PyQt5 import QtCore

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

