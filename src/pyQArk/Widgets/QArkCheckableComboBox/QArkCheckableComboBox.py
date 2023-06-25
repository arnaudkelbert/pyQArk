# -*- coding: utf-8 -*-
import unittest
import numpy as np
from PyQt5 import QtCore, QtWidgets, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)

class QArkCheckBoxStyledItemDelegate(QtWidgets.QStyledItemDelegate):
    pass

    # def paint(self, painter, option, index):
    #      #refToNonConstOption = QtGui.QStyleOptionViewItem()
    #      #refToNonConstOption.showDecorationSelected = False
    #      QStyledItemDelegate.paint(self, painter, option, index)

class QArkCheckableComboBox(QtWidgets.QWidget):
    """
    """
    dataChanged = QtCore.pyqtSignal()

    def __init__(self, *args, **kwargs):
        try:
            self.b_firstIsAll = kwargs.pop('firstIsAll')
        except KeyError:
            self.b_firstIsAll = False
        super(QArkCheckableComboBox, self).__init__(*args,**kwargs)
        self.initUi()
        self.initConnection()

    def initUi(self):
        o_layout = QtWidgets.QHBoxLayout(self)
        o_layout.setContentsMargins(0,0,0,0)
        self.o_combobox = QtWidgets.QComboBox(self)
        o_layout.addWidget(self.o_combobox)
        self.setLayout(o_layout)

    def initConnection(self):
        pass

    def getSelection(self):
        u_nrows = self.o_itemModel.rowCount()
        if self.b_firstIsAll:
            return [self.o_itemModel.item(i + 2).text() for i in range(u_nrows - 2)
                    if self.o_itemModel.item(i + 2).checkState() == QtCore.Qt.Checked]
        else:
            return [self.o_itemModel.item(i + 1).text() for i in range(u_nrows - 1)
                    if self.o_itemModel.item(i + 1).checkState() == QtCore.Qt.Checked]

    def insertCheckableItems(self, _s_title, _t_list, _b_fistItemIsAll=False):
        self.b_firstIsAll = _b_fistItemIsAll
        self.o_itemModel = QtGui.QStandardItemModel(len(_t_list), 1)
        u_cIdx = 0
        # First item - title
        o_item = QtGui.QStandardItem(_s_title)
        self.o_itemModel.setItem(u_cIdx, 0, o_item)
        u_cIdx += 1
        # items
        if self.b_firstIsAll:
            o_item = QtGui.QStandardItem('Select all')
            o_item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            t_cs = [ c[1] for c in _t_list ]
            if np.all(t_cs):
                o_item.setData(QtCore.Qt.Checked, QtCore.Qt.CheckStateRole)
            elif np.any(t_cs):
                o_item.setData(QtCore.Qt.PartiallyChecked, QtCore.Qt.CheckStateRole)
            else:
                o_item.setData(QtCore.Qt.Unchecked, QtCore.Qt.CheckStateRole)
            self.o_itemModel.setItem(u_cIdx, 0, o_item)
            u_cIdx += 1
        for s_str, b_checked in _t_list:
            o_item = QtGui.QStandardItem(s_str)
            o_item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            if b_checked:
                o_item.setData(QtCore.Qt.Checked, QtCore.Qt.CheckStateRole)
            else:
                o_item.setData(QtCore.Qt.Unchecked, QtCore.Qt.CheckStateRole)
            self.o_itemModel.setItem(u_cIdx, 0, o_item)
            u_cIdx += 1
        self.o_combobox.setModel(self.o_itemModel)
        self.o_delegate = QArkCheckBoxStyledItemDelegate(self)
        self.o_combobox.setItemDelegate(self.o_delegate)
        self.t_checkState = [self.o_itemModel.item(i).checkState() for i in range(1,u_cIdx)]
        self.b_checkStateLock = False
        self.o_itemModel.dataChanged.connect(self.handleDataChanged)

    def updateCheckState(self, _b_emit=True):
        if self.b_checkStateLock:
            return
        u_nrows = self.o_itemModel.rowCount()
        t_cCheckState = [self.o_itemModel.item(i + 1).checkState() for i in range(u_nrows-1)]
        t_changed = np.not_equal(t_cCheckState, self.t_checkState)

        if np.any(t_changed):
            # at least one change (should not be more...)
            self.b_checkStateLock = True
            self.o_itemModel.dataChanged.disconnect(self.handleDataChanged)

            if self.b_firstIsAll:
                if t_changed[0]:
                    #print('all changed')
                    # the "all" item has been changed by user
                    if t_cCheckState[0] == QtCore.Qt.Checked:
                        # lets check all
                        for i in range(2, u_nrows):
                            self.o_itemModel.item(i).setCheckState(QtCore.Qt.Checked)
                    elif t_cCheckState[0] == QtCore.Qt.Unchecked:
                        # lets uncheck all
                        for i in range(2, u_nrows):
                            self.o_itemModel.item(i).setCheckState(QtCore.Qt.Unchecked)
                else:
                    if np.all(t_cCheckState[1:]):
                        #print('all other selected')
                        self.o_itemModel.item(1).setData(QtCore.Qt.Checked, QtCore.Qt.CheckStateRole)
                    elif np.any(t_cCheckState[1:]):
                        #print('any other selected')
                        self.o_itemModel.item(1).setData(QtCore.Qt.PartiallyChecked, QtCore.Qt.CheckStateRole)
                    else:
                        #print('no other selected')
                        self.o_itemModel.item(1).setData(QtCore.Qt.Unchecked, QtCore.Qt.CheckStateRole)

            self.b_checkStateLock = False
            self.o_itemModel.dataChanged.connect(self.handleDataChanged)
            self.t_checkState = [self.o_itemModel.item(i + 1).checkState() for i in range(u_nrows-1)]
            if _b_emit:
                self.dataChanged.emit()

    def handleDataChanged(self):
        if not self.b_checkStateLock:
            self.updateCheckState(_b_emit=True)

class QArkCheckableComboBoxTest( unittest.TestCase ):
    """
    Test
    """
    def test_widget(self):
        o_app = QtWidgets.QApplication( sys.argv )
        o_w = QArkCheckableComboBox(firstIsAll=True)
        o_w.insertCheckableItems('title',[('item2',True),('item3',False),('item4',True)])
        #o_w.insertCheckableItems('title',[('item2',False),('item3',False),('item4',False)])
        #o_w.insertCheckableItems('title',[('item2',True),('item3',True),('item4',True)])
        #o_w.setText('click me!')
        o_w.show()
        o_app.exec_()

if __name__ == '__main__':
    unittest.main()