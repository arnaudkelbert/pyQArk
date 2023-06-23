# -*- coding: utf-8 -*-
rom PyQt5 import QtWidgets, QtCore, QtGui
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

