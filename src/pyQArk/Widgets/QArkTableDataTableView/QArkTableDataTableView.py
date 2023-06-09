# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#
# QArkDataTableTableView
#
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
from pyQArk.QArkConfig import QARK_QT_GENERATION

if QARK_QT_GENERATION == 4:
    from PyQt4 import QtGui, QtCore
    QtWidgets=QtGui
elif QARK_QT_GENERATION == 5:
    from PyQt5 import QtWidgets, QtCore

from pyQArk.Models.QArkTableDataTableViewModel import QArkTableDataTableViewModel
from pyQArk.Models.QArkTableDataTableViewProxyModel import QArkTableDataTableViewProxyModel

class QArkTableDataTableView(QtWidgets.QTableView):
    filteredDataChanged = QtCore.pyqtSignal()

    def __init__(self, parent, _o_data=None, *args, **kwargs):
        QtWidgets.QTableView.__init__(self, parent, *args, **kwargs)

        self.setFilteredData(_o_data)
        self.setData(_o_data)

        # Flag d'activation du filtrage
        # les lignes non filtrees sont masquees si True
        # sinon elles sont affichees dans une autre couleur
        self.b_enableFiltering = True

    def setStyleManager(self, _o_styleManager):
        self.o_styleManager = _o_styleManager

    def setEnableFiltering(self, _b_enableFiltering):
        self.b_enableFiltering = _b_enableFiltering

    def setData(self, _o_data):
        """
        """
        self.o_data = _o_data
        if self.o_data is None:
            return
        o_sourceModel = QArkTableDataTableViewModel(parent=self
                                           , _o_styleManager=self.o_styleManager
                                           , _o_data=self.o_data
                                           , _o_filteredData=self.o_filteredData
                                           , _b_enableFilteredDataBackground=not self.b_enableFiltering
                                           )
        o_proxyModel = QArkTableDataTableViewProxyModel(self)
        o_proxyModel.setEnableFiltering(self.b_enableFiltering)
        o_proxyModel.setData(self.o_data)
        o_proxyModel.setFilteredData(self.o_filteredData)
        o_proxyModel.setSourceModel(o_sourceModel)
        self.setModel(o_proxyModel)
        # row height
        self.verticalHeader().setDefaultSectionSize(20)
        # select whole row
        self.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

    def setFilteredData(self, _o_filteredData):
        """
        """
        self.o_filteredData = _o_filteredData
        self.filteredDataChanged.emit()

    def initUi(self, _o_initUi):
        """
        """
        pass

    @QtCore.pyqtSlot()
    def refreshLayout(self):
        """
        """
        self.model().sourceModel().refreshLayout()

    @QtCore.pyqtSlot(object)
    def handleFilterDisplayModeToggled(self, _b_toggled):
        # Si _b_toggled est a True alors il faut masquer les valeurs
        # Sinon les afficher dans une autre couleur
        self.b_enableFiltering = _b_toggled
        self.model().sourceModel().setEnableFilteredDataBackground(not _b_toggled)
        self.model().setEnableFiltering(_b_toggled)
