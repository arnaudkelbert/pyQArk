# -*- coding: utf-8 -*-
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
