# -*- coding: utf-8 -*-
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
