# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\kelbera\Documents\DEV\PYTHON\pyQArk_base\pyQArk\Dialogs\QArkSetNotationPlotWidgetDialog\QArkSetNotationPlotWidgetDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QArkSetNotationPlotWidgetDialog(object):
    def setupUi(self, QArkSetNotationPlotWidgetDialog):
        QArkSetNotationPlotWidgetDialog.setObjectName("QArkSetNotationPlotWidgetDialog")
        QArkSetNotationPlotWidgetDialog.resize(386, 161)
        self.gridLayout = QtWidgets.QGridLayout(QArkSetNotationPlotWidgetDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.titleLabel = QtWidgets.QLabel(QArkSetNotationPlotWidgetDialog)
        self.titleLabel.setObjectName("titleLabel")
        self.gridLayout.addWidget(self.titleLabel, 0, 0, 1, 1)
        self.titleLineEdit = QtWidgets.QLineEdit(QArkSetNotationPlotWidgetDialog)
        self.titleLineEdit.setObjectName("titleLineEdit")
        self.gridLayout.addWidget(self.titleLineEdit, 0, 1, 1, 1)
        self.xLabel = QtWidgets.QLabel(QArkSetNotationPlotWidgetDialog)
        self.xLabel.setObjectName("xLabel")
        self.gridLayout.addWidget(self.xLabel, 1, 0, 1, 1)
        self.xLabelLineEdit = QtWidgets.QLineEdit(QArkSetNotationPlotWidgetDialog)
        self.xLabelLineEdit.setObjectName("xLabelLineEdit")
        self.gridLayout.addWidget(self.xLabelLineEdit, 1, 1, 1, 1)
        self.yLabel = QtWidgets.QLabel(QArkSetNotationPlotWidgetDialog)
        self.yLabel.setObjectName("yLabel")
        self.gridLayout.addWidget(self.yLabel, 2, 0, 1, 1)
        self.yLabelLineEdit = QtWidgets.QLineEdit(QArkSetNotationPlotWidgetDialog)
        self.yLabelLineEdit.setObjectName("yLabelLineEdit")
        self.gridLayout.addWidget(self.yLabelLineEdit, 2, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 8, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(QArkSetNotationPlotWidgetDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 4, 1, 1, 1)

        self.retranslateUi(QArkSetNotationPlotWidgetDialog)
        self.buttonBox.accepted.connect(QArkSetNotationPlotWidgetDialog.accept)
        self.buttonBox.rejected.connect(QArkSetNotationPlotWidgetDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(QArkSetNotationPlotWidgetDialog)

    def retranslateUi(self, QArkSetNotationPlotWidgetDialog):
        _translate = QtCore.QCoreApplication.translate
        QArkSetNotationPlotWidgetDialog.setWindowTitle(_translate("QArkSetNotationPlotWidgetDialog", "Dialog"))
        self.titleLabel.setText(_translate("QArkSetNotationPlotWidgetDialog", "Title"))
        self.xLabel.setText(_translate("QArkSetNotationPlotWidgetDialog", "X - Label"))
        self.yLabel.setText(_translate("QArkSetNotationPlotWidgetDialog", "Y - Label"))

