# -*- coding: utf-8 -*-
from PyQt5 import QtCore

class QArkSortFilterProxyModel( QtCore.QSortFilterProxyModel ):

    def lessThan( self, _o_leftIndex, _o_rightIndex ):
        o_leftData = _o_leftIndex.data(QtCore.Qt.DisplayRole)
        o_rightData = _o_rightIndex.data(QtCore.Qt.DisplayRole)
        return o_leftData < o_rightData
