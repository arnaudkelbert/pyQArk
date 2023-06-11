# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#
#
# QArkItem
#
# Method data and setData should be reimplemented according to item
# specifics
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

class QArkItem( object ):

    def __init__( self
                 , _o_data
                 ):
        """
        The constructor is only used to record the item's parent and
        the data associated with each column.
        """
        self.o_data = _o_data

    @classmethod
    def getHeader( cls, column ):
        return QtCore.QVariant()

    def getItemData(self):
        return self.o_data

    def isItemMultiDimensional( self ):
        """
        """
        return isinstance(self.o_data, list) or isinstance(self.o_data,tuple)

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

        if role == QtCore.Qt.BackgroundRole:
            return self.dataBackgroundRole(_u_index)

        if role == QtCore.Qt.ForegroundRole:
            return self.dataForegroundRole(_u_index)

        if role == QtCore.Qt.TextColorRole:
            return self.dataTextColorRole(_u_index)

        if role == QtCore.Qt.FontRole:
            return self.dataFontRole(_u_index)

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

    def dataBackgroundRole( self, _u_index ):
        return QtCore.QVariant()

    def dataForegroundRole( self, _u_index ):
        return QtCore.QVariant()

    def dataTextColorRole( self, _u_index ):
        return QtCore.QVariant()

    def dataFontRole( self, _u_index ):
        return QtCore.QVariant()

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

    def insertColumns( self
                      , _u_position
                      , _u_columns
                      ):
        """
        """
        if _u_position < 0 or _u_position >= self.columnCount():
            return False

        if _u_columns > 0 and not self.isItemMultiDimensional():
            self.o_data = [ self.o_data ]

        for _ in range(_u_columns):
            self.o_data.insert( _u_position, QtCore.QVariant() )

        return True

    def removeColumns( self
                      , _u_position
                      , _u_columns
                      ):
        if _u_position < 0 or _u_position+_u_columns >= self.columnCount():
            return False

        if _u_columns > 0 and not self.isItemMultiDimensional():
            self.o_data = [ self.o_data ]

        for _ in range(_u_columns):
            self.o_data.pop( _u_position )

        return True

    def cloneItemOnly( self, parent ):
        """
        Only clone item (and keep data reference)
        Can be used during drag'n drop
        """
        o_item = self.__class__( parent, self.o_data )

        return o_item
