# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QArkSetNotationPlotWidgetDialog.ui'
#
# Created: Sun Dec 14 15:05:41 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_QArkSetNotationPlotWidgetDialog(object):
    def setupUi(self, QArkSetNotationPlotWidgetDialog):
        QArkSetNotationPlotWidgetDialog.setObjectName(_fromUtf8("QArkSetNotationPlotWidgetDialog"))
        QArkSetNotationPlotWidgetDialog.resize(386, 161)
        self.gridLayout = QtGui.QGridLayout(QArkSetNotationPlotWidgetDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.titleLabel = QtGui.QLabel(QArkSetNotationPlotWidgetDialog)
        self.titleLabel.setObjectName(_fromUtf8("titleLabel"))
        self.gridLayout.addWidget(self.titleLabel, 0, 0, 1, 1)
        self.titleLineEdit = QtGui.QLineEdit(QArkSetNotationPlotWidgetDialog)
        self.titleLineEdit.setObjectName(_fromUtf8("titleLineEdit"))
        self.gridLayout.addWidget(self.titleLineEdit, 0, 1, 1, 1)
        self.xLabel = QtGui.QLabel(QArkSetNotationPlotWidgetDialog)
        self.xLabel.setObjectName(_fromUtf8("xLabel"))
        self.gridLayout.addWidget(self.xLabel, 1, 0, 1, 1)
        self.xLabelLineEdit = QtGui.QLineEdit(QArkSetNotationPlotWidgetDialog)
        self.xLabelLineEdit.setObjectName(_fromUtf8("xLabelLineEdit"))
        self.gridLayout.addWidget(self.xLabelLineEdit, 1, 1, 1, 1)
        self.yLabel = QtGui.QLabel(QArkSetNotationPlotWidgetDialog)
        self.yLabel.setObjectName(_fromUtf8("yLabel"))
        self.gridLayout.addWidget(self.yLabel, 2, 0, 1, 1)
        self.yLabelLineEdit = QtGui.QLineEdit(QArkSetNotationPlotWidgetDialog)
        self.yLabelLineEdit.setObjectName(_fromUtf8("yLabelLineEdit"))
        self.gridLayout.addWidget(self.yLabelLineEdit, 2, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 8, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(QArkSetNotationPlotWidgetDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 4, 1, 1, 1)

        self.retranslateUi(QArkSetNotationPlotWidgetDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), QArkSetNotationPlotWidgetDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), QArkSetNotationPlotWidgetDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(QArkSetNotationPlotWidgetDialog)

    def retranslateUi(self, QArkSetNotationPlotWidgetDialog):
        QArkSetNotationPlotWidgetDialog.setWindowTitle(_translate("QArkSetNotationPlotWidgetDialog", "Dialog", None))
        self.titleLabel.setText(_translate("QArkSetNotationPlotWidgetDialog", "Title", None))
        self.xLabel.setText(_translate("QArkSetNotationPlotWidgetDialog", "X - Label", None))
        self.yLabel.setText(_translate("QArkSetNotationPlotWidgetDialog", "Y - Label", None))

