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
    QSortFilterProxyModel = QtGui.QSortFilterProxyModel

elif QARK_QT_GENERATION == 5:
    from PyQt5 import QtWidgets, QtCore, QtGui
    QSortFilterProxyModel = QtCore.QSortFilterProxyModel

class QArkTableDataTableViewProxyModel(QSortFilterProxyModel):

    def __init__(self, parent, *args, **kwargs):
        QSortFilterProxyModel.__init__(self, parent, *args, **kwargs)
        self.b_enableFiltering = True
        # self.setDynamicSortFilter(True)
        self.o_data = None
        self.o_filteredData = None
        # On fait ca pour que le sort se base sur le role EditRole (defini dans le modele source)
        # On utilise alors les vrais types et pas des strings
        self.setSortRole(QtCore.Qt.UserRole)
        parent.filteredDataChanged.connect(self.handleParentFilteredDataChanged)

    def setData(self, _o_data):
        self.o_data = _o_data

    def setFilteredData(self, _o_filteredData):
        if not _o_filteredData is self.o_filteredData:
            self.o_filteredData = _o_filteredData
            # On reactualise la vue (changement de couleur par le modele source
            # si besoin
            self.dataChanged.emit(QtCore.QModelIndex(), QtCore.QModelIndex())
            self.invalidateFilter()

    def setEnableFiltering(self, _b_bool):
        self.b_enableFiltering = _b_bool
        self.invalidateFilter()

    #     def setSourceModel( self, *args, **kwargs ):
    #         super( FilterListViewProxyModel, self ).setSourceModel( *args, **kwargs )
    #
    #         #self.sourceModel().expandRequestSignal.connect( self.handleSrcExpandViewRequested )

    def filterAcceptsRow(self, sourceRow, sourceParent):
        if self.o_filteredData is None:
            return True
        if self.sourceModel().rowCount() <= sourceRow:
            return False
        if not self.b_enableFiltering:
            return True
        if sourceRow in self.o_filteredData.index():
            return True
        else:
            return False

    @QtCore.pyqtSlot()
    def handleParentFilteredDataChanged(self):
        self.setFilteredData(self.parent().o_filteredData)

