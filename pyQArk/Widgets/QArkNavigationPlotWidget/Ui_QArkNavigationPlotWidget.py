# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QArkNavigationPlotWidget.ui'
#
# Created: Wed Jul 30 07:56:32 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_QArkNavigationPlotWidget(object):
    def setupUi(self, QArkNavigationPlotWidget):
        QArkNavigationPlotWidget.setObjectName(_fromUtf8("QArkNavigationPlotWidget"))
        QArkNavigationPlotWidget.resize(717, 503)
        self.splitterH = QtGui.QSplitter(QArkNavigationPlotWidget)
        self.splitterH.setGeometry(QtCore.QRect(10, 10, 681, 491))
        self.splitterH.setOrientation(QtCore.Qt.Horizontal)
        self.splitterH.setObjectName(_fromUtf8("splitterH"))
        self.plotAreaWidget = QtGui.QWidget(self.splitterH)
        self.plotAreaWidget.setObjectName(_fromUtf8("plotAreaWidget"))
        self.splitterV = QtGui.QSplitter(self.splitterH)
        self.splitterV.setOrientation(QtCore.Qt.Vertical)
        self.splitterV.setObjectName(_fromUtf8("splitterV"))
        self.treeView = QtGui.QTreeView(self.splitterV)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeView.sizePolicy().hasHeightForWidth())
        self.treeView.setSizePolicy(sizePolicy)
        self.treeView.setObjectName(_fromUtf8("treeView"))
        self.colorBoxContainer = QtGui.QWidget(self.splitterV)
        self.colorBoxContainer.setObjectName(_fromUtf8("colorBoxContainer"))

        self.retranslateUi(QArkNavigationPlotWidget)
        QtCore.QMetaObject.connectSlotsByName(QArkNavigationPlotWidget)

    def retranslateUi(self, QArkNavigationPlotWidget):
        QArkNavigationPlotWidget.setWindowTitle(QtGui.QApplication.translate("QArkNavigationPlotWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))

