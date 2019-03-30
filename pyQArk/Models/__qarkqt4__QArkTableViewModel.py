# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#
#
# QArkTableViewModel
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

from .QArkItem import QArkItem
from pyQArk.Core.QArkMimeData import QArkMimeData

import copy

class QArkItemMimeData(QArkMimeData):
    MIME_TYPE = QtCore.QString('application/qarkitem-instance')

class QArkTableViewModel( QtCore.QAbstractTableModel ):

    itemAddedSignal = QtCore.pyqtSignal(object)

    def __init__( self
                 , parent
                 , _cls_itemClass
                 , _t_data = None
                 ):
        """
        """
        super( QArkTableViewModel, self ).__init__( parent )

        self.t_items = []
        self.cls_itemClass = _cls_itemClass

        if not _t_data is None:
            self.setupModelData( _t_data )

        self.b_itemIsEditable = False
        self.b_itemIsDragEnabled = False
        self.b_itemIsDropEnabled = False
        self.b_itemIsUserCheckable = False

        # If True : item data are also copied
        # Else only item are cloned and data
        # keeps the same reference
        # This is used when dropping
        self.b_dropDataDeepCopy = False

        # Force data to be unique when drop
        self.b_forceDropDataUnicity = True

        self.cls_mimetype = QArkItemMimeData

    def getAllItems( self ):
        return self.t_items

    def getItemDataRow( self, _o_itemData ):
        """
        Retourne la liste des lignes correspondante a une donnee
        """
        t_row = []
        print( _o_itemData )

        for u_row, o_data in enumerate( map(lambda o:o.getItemData(), self.t_items) ):
            #print 'row : %d' % u_row
            #print 'data row : %s' % o_data
            #print 'data : %s' % _o_itemData
            #print o_data is _o_itemData
            if o_data is _o_itemData:
                t_row.append(u_row)

        return t_row

    def getItemIndex( self, _o_item ):
        for u_row, o_item in enumerate(self.t_items):
            if o_item is _o_item:
                return self.index( u_row, 0 )
        return QtCore.QModelIndex()

    def setMimeType( self, _cls_class ):
        self.cls_mimetype = _cls_class

    def encodeMime( self, _x_object ):
        return self.cls_mimetype(_x_object)

    def setForceDropDataUnicity( self, _b_bool=True ):
        self.b_forceDropDataUnicity = _b_bool

    def setItemIsEditable( self, _b_enabled=True ):
        self.b_itemIsEditable = _b_enabled

    def setItemIsDropEnabled( self, _b_enabled=True ):
        self.b_itemIsDropEnabled = _b_enabled

    def setItemIsDragEnabled( self, _b_enabled=True ):
        self.b_itemIsDragEnabled = _b_enabled

    def setItemIsUserCheckable( self, _b_enabled=True ):
        self.b_itemIsUserCheckable = _b_enabled

    def setDropDataDeepCopy( self, _b_bool=True ):
        self.b_dropDataDeepCopy = _b_bool

    def rowCount( self, parent=None ):
        """
        The rowCount() function simply returns the number of items
        """
        return len(self.t_items)

    def columnCount( self, parent=None ):
        """
        Should be implemented in child class
        """
        if self.rowCount() > 0:
            return self.t_items[0].columnCount()
        return 1

    def data( self, index, role ):
        """
        Returns data
        """
        if not index.isValid():
            return QtCore.QVariant()
        item = self.getItem(index)
        return item.data(index.column(), role)

    def flags( self, index ):
        """
        To enable items to be edited and selected, the flags() function
        needs to be implemented so that it returns a combination of flags
        that includes the Qt::ItemIsEditable and Qt::ItemIsSelectable
        flags as well as Qt::ItemIsEnabled
        """
        if not index.isValid():
            if self.b_itemIsDropEnabled:
                QtCore.Qt.ItemIsDropEnabled
            else:
                return 0

        u_flag = QtCore.Qt.ItemIsEnabled\
               | QtCore.Qt.ItemIsSelectable

        if self.b_itemIsEditable:
            u_flag = u_flag | QtCore.Qt.ItemIsEditable

        if self.b_itemIsDragEnabled:
            u_flag = u_flag | QtCore.Qt.ItemIsDragEnabled

        if self.b_itemIsDropEnabled:
            u_flag = u_flag | QtCore.Qt.ItemIsDropEnabled

        if self.b_itemIsUserCheckable:
            u_flag = u_flag | QtCore.Qt.ItemIsUserCheckable

        return u_flag

    def headerData( self, column, orientation, role ):
        if (orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole ):
            return self.cls_itemClass.getHeader(column)
        return QtCore.QVariant()

    def setupModelData( self, _t_data ):
        for _o_item in _t_data:
            self.t_items.append( _o_item )

    def getItem(self, o_index ):
        if o_index.isValid():
            return self.t_items[o_index.row()]
        return None

    def insertColumns( self
                      , position
                      , columns
                      , parent=QtCore.QModelIndex()
                      ):
        """
        """
        if position < 0 or position >= self.columnCount():
            return False

        self.beginInsertColumns( parent, position, position + columns - 1)

        for o_item in self.t_items:
            o_item.insertColumns( position, columns )

        self.endInsertColumns()
        return True

    def insertRows( self
                   , position
                   , rows
                   , parent=QtCore.QModelIndex()
                   ):
        """
        """
        if position < 0 or position >= self.rowCount():
            return False

        self.beginInsertRows(parent, position, position + rows - 1)

        for _ in range(rows):
            self.t_items.insert( position, QArkItem(None) )

        #check this code
        b_success = parent.insertChildren(position, rows, self.columnCount())
        self.endInsertRows()

        return b_success

    def removeColumns(self
                      , position
                      , columns
                      , parent=QtCore.QModelIndex()
                      ):
        """
        """
        if position < 0 or position+columns >= self.columnCount():
            return False
        self.beginRemoveColumns( parent, position, position + columns - 1)

        for o_item in self.t_items:
            o_item.removeColumns( position, columns )
        self.endRemoveColumns()

        return True

    def removeRows( self
                    , position
                    , rows
                    , parent=QtCore.QModelIndex()
                    ):
        """
        """
        if position < 0 or position+rows >= self.rowCount():
            return False

        self.beginRemoveRows( parent, position, position + rows - 1)

        for _ in range(rows):
            self.t_items.pop(position)

        self.endRemoveRows()

        return True

    def setData( self
                , index
                , value
                , role
                ):
        """
        """
        if not index.isValid():
            return False

        item = self.getItem(index)
        b_result = item.setData( index.column(), value, role )

        if b_result:
            self.dataChanged.emit(index, index)

        return b_result

    def supportedDropActions(self):
        return QtCore.Qt.CopyAction | QtCore.Qt.MoveAction

    def addItem( self, o_item, o_parent=QtCore.QModelIndex() ):
        """
        """
        u_position = self.rowCount()-1

        self.beginInsertRows( o_parent, u_position, u_position )
        self.t_items.append( o_item )
        self.endInsertRows()
        self.itemAddedSignal.emit( o_item )

    def mimeTypes(self):
        types = QtCore.QStringList()
        types.append( self.cls_mimetype.MIME_TYPE )
        return types

    def mimeData(self, indexes):
        """
        This function is used for drag
        """
        raise NotImplementedError

    def dropMimeData(self, mimedata, action, row, column, parentIndex):
        """
        This function is used for drop
        """
        raise NotImplementedError

    def emitAllDataChanged( self ):
        """
        Emission du signal dataChanged avec index par defaut
        pour prendre en compte tout le modele
        """
        self.dataChanged.emit( QtCore.QModelIndex(), QtCore.QModelIndex() )

    def emitRowDataChanged( self, _u_row ):
        """
        Emission du signal dataChanged avec index par defaut
        pour prendre en compte tout le modele
        """
        for u_col in range( self.columnCount() ):
            o_index = self.index( _u_row, u_col )
            self.dataChanged.emit( o_index, o_index )

    @QtCore.pyqtSlot( object )
    def handleItemDataChanged( self, _o_itemData ):
        """
        Gestion de modification d'une donnee
        """
        # Recherche des items correspondant
        for u_row in self.getItemDataRow( _o_itemData ):
            # on emet un signal dataChanged
            #o_index = self.index( u_row, 0 )
            #self.dataChanged.emit( o_index, o_index )
            self.emitRowDataChanged(u_row)
