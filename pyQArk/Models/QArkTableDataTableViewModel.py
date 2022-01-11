# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#
# CNES - DNO/OT/PE
#
# @author : Arnaud Kelbert (DNO/OT/PE)
# @date : 2020/02/02
# @version : 0.1
#
# Historic:
# 0.1 : init version
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
import datetime
from pyQArk.QArkConfig import QARK_QT_GENERATION

if QARK_QT_GENERATION == 4:
    from PyQt4 import QtGui, QtCore
    QtWidgets=QtGui
elif QARK_QT_GENERATION == 5:
    from PyQt5 import QtWidgets, QtCore, QtGui

class QArkTableDataTableViewModel(QtCore.QAbstractTableModel):

    def __init__(self
                 , parent
                 , _o_data
                 , _o_filteredData
                 , _o_styleManager
                 , _b_enableFilteredDataBackground=True
                 ):
        """
        """
        super(QArkTableDataTableViewModel, self).__init__(parent)
        self.o_parentDataTableView = parent
        self.o_styleManager = _o_styleManager
        self.o_data = _o_data
        self.o_filteredData = _o_filteredData
        self.b_enableFilteredDataBackground = _b_enableFilteredDataBackground
        self.b_itemIsUserCheckable = False
        parent.filteredDataChanged.connect(self.handleParentFilteredDataChanged)

    def setFilteredData(self, _o_filteredData):
        """
        """
        if not self.o_filteredData is _o_filteredData:
            self.o_filteredData = _o_filteredData
            # self.dataChanged.emit( QtCore.QModelIndex(), QtCore.QModelIndex() )

    def setEnableFilteredDataBackground(self, _b_enable):
        self.b_enableFilteredDataBackground = _b_enable

    def setItemIsUserCheckable(self, _b_enabled=True):
        self.b_itemIsUserCheckable = _b_enabled

    def rowCount(self, parent=None):
        """
        The rowCount() function simply returns the number of items
        """
        return self.o_data.getNbLines()

    def columnCount(self, parent=None):
        """
        Should be implemented in child class
        """
        return self.o_data.getNbColumns()

    def data(self, index, role):
        """
        Returns data
        """
        if not index.isValid():
            return QtCore.QVariant()
        if role == QtCore.Qt.DisplayRole:
            return str(self.o_data.cell(index.row(), index.column()))
        if role == QtCore.Qt.CheckStateRole:
            pass
        if role == QtCore.Qt.UserRole:
            # Mis en place pour le sort
            try:
                return float(self.o_data.cell(index.row(), index.column()))
            except:
                return str(self.o_data.cell(index.row(), index.column()))
                #return QtCore.QString(str(self.o_data.cell(index.row(), index.column())))
        if role == QtCore.Qt.FontRole:
            try:
                return self.o_styleManager.getFontRole(self.o_data.criticityLevel(index.row(), index.column()))
            except:
                pass
            # o_font = QtGui.QFont()
            # if index.column()%2:
            #     o_font.setBold(True)
            #     o_font.setPointSize(8)
            # return o_font
        if role == QtCore.Qt.ForegroundRole:
            try:
                return self.o_styleManager.getForegroundRole(self.o_data.criticityLevel(index.row(), index.column()))
            except:
                pass
        if role == QtCore.Qt.BackgroundRole:
            try:
                return self.o_styleManager.getBackgroundRole(self.o_data.criticityLevel(index.row(), index.column()))
            except:
                pass
        return QtCore.QVariant()

    def flags(self, index):
        """
        To enable items to be edited and selected, the flags() function
        needs to be implemented so that it returns a combination of flags
        that includes the Qt::ItemIsEditable and Qt::ItemIsSelectable
        flags as well as Qt::ItemIsEnabled
        """
        if not index.isValid():
            return 0;
        u_flag = QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable
        if self.b_itemIsUserCheckable and index.column() == 0:
            u_flag = u_flag | QtCore.Qt.ItemIsUserCheckable
        return u_flag

    def headerData(self, column, orientation, role):
        if (orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole):
            return self.o_data.getSafeKey(column)
        return QtCore.QVariant()

    def insertColumns(self, position, columns, parent=QtCore.QModelIndex()):
        """
        """
        if position < 0 or position >= self.columnCount():
            return False
        self.beginInsertColumns(parent, position, position + columns - 1)
        self.endInsertColumns()
        return True

    def insertRows(self, position, rows, parent=QtCore.QModelIndex()):
        """
        """
        if position < 0 or position >= self.rowCount():
            return False
        self.beginInsertRows(parent, position, position + rows - 1)
        b_success = True
        self.endInsertRows()
        return b_success

    def removeColumns(self, position, columns, parent=QtCore.QModelIndex()):
        """
        """
        if position < 0 or position + columns >= self.columnCount():
            return False
        self.beginRemoveColumns(parent, position, position + columns - 1)
        self.endRemoveColumns()
        return True

    def removeRows(self, position, rows, parent=QtCore.QModelIndex()):
        """
        """
        if position < 0 or position + rows >= self.rowCount():
            return False
        self.beginRemoveRows(parent, position, position + rows - 1)
        self.endRemoveRows()
        return True

    def refreshLayout(self):
        """
        """
        self.layoutAboutToBeChanged.emit()
        self.layoutChanged.emit()

    @QtCore.pyqtSlot()
    def handleParentFilteredDataChanged(self):
        self.setFilteredData(self.o_parentDataTableView.o_filteredData)

#https://doc.qt.io/qt-5/qt.html#ItemDataRole-enum
# Each item in the model has a set of data elements associated with it, each with its own role. The roles are used by the view to indicate to the model which type of data it needs. Custom models should return data in these types.
#
# The general purpose roles (and the associated types) are:
# Constant	Value	Description
# Qt::DisplayRole	0	The key data to be rendered in the form of text. (QString)
# Qt::DecorationRole	1	The data to be rendered as a decoration in the form of an icon. (QColor, QIcon or QPixmap)
# Qt::EditRole	2	The data in a form suitable for editing in an editor. (QString)
# Qt::ToolTipRole	3	The data displayed in the item's tooltip. (QString)
# Qt::StatusTipRole	4	The data displayed in the status bar. (QString)
# Qt::WhatsThisRole	5	The data displayed for the item in "What's This?" mode. (QString)
# Qt::SizeHintRole	13	The size hint for the item that will be supplied to views. (QSize)
#
# Roles describing appearance and meta data (with associated types):
# Constant	Value	Description
# Qt::FontRole	6	The font used for items rendered with the default delegate. (QFont)
# Qt::TextAlignmentRole	7	The alignment of the text for items rendered with the default delegate. (Qt::Alignment)
# Qt::BackgroundRole	8	The background brush used for items rendered with the default delegate. (QBrush)
# Qt::BackgroundColorRole	BackgroundRole	This role is obsolete. Use BackgroundRole instead.
# Qt::ForegroundRole	9	The foreground brush (text color, typically) used for items rendered with the default delegate. (QBrush)
# Qt::TextColorRole	ForegroundRole	This role is obsolete. Use ForegroundRole instead.
# Qt::CheckStateRole	10	This role is used to obtain the checked state of an item. (Qt::CheckState)
# Qt::InitialSortOrderRole	14	This role is used to obtain the initial sort order of a header view section. (Qt::SortOrder). This role was introduced in Qt 4.8.
#
# Accessibility roles (with associated types):
# Constant	Value	Description
# Qt::AccessibleTextRole	11	The text to be used by accessibility extensions and plugins, such as screen readers. (QString)
# Qt::AccessibleDescriptionRole	12	A description of the item for accessibility purposes. (QString)
#
# User roles:
# Constant	Value	Description
# Qt::UserRole	0x0100	The first role that can be used for application-specific purposes.
#
# For user roles, it is up to the developer to decide which types to use and ensure that components use the correct types when accessing and setting data.