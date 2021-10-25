# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\kelbera\Documents\DEV\PYTHON\pyQArk_base\pyQArk\Dialogs\QArkSetAxisRangePlotWidgetDialog\QArkSetAxisRangePlotWidgetDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QArkSetAxisRangePlotWidgetDialog(object):
    def setupUi(self, QArkSetAxisRangePlotWidgetDialog):
        QArkSetAxisRangePlotWidgetDialog.setObjectName("QArkSetAxisRangePlotWidgetDialog")
        QArkSetAxisRangePlotWidgetDialog.resize(304, 113)
        self.verticalLayout = QtWidgets.QVBoxLayout(QArkSetAxisRangePlotWidgetDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.xLabel = QtWidgets.QLabel(QArkSetAxisRangePlotWidgetDialog)
        self.xLabel.setObjectName("xLabel")
        self.gridLayout.addWidget(self.xLabel, 0, 0, 1, 1)
        self.xminLineEdit = QtWidgets.QLineEdit(QArkSetAxisRangePlotWidgetDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xminLineEdit.sizePolicy().hasHeightForWidth())
        self.xminLineEdit.setSizePolicy(sizePolicy)
        self.xminLineEdit.setObjectName("xminLineEdit")
        self.gridLayout.addWidget(self.xminLineEdit, 0, 1, 1, 1)
        self.xdashLabel = QtWidgets.QLabel(QArkSetAxisRangePlotWidgetDialog)
        self.xdashLabel.setObjectName("xdashLabel")
        self.gridLayout.addWidget(self.xdashLabel, 0, 2, 1, 1)
        self.xmaxLineEdit = QtWidgets.QLineEdit(QArkSetAxisRangePlotWidgetDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xmaxLineEdit.sizePolicy().hasHeightForWidth())
        self.xmaxLineEdit.setSizePolicy(sizePolicy)
        self.xmaxLineEdit.setObjectName("xmaxLineEdit")
        self.gridLayout.addWidget(self.xmaxLineEdit, 0, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 4, 1, 1)
        self.yLabel = QtWidgets.QLabel(QArkSetAxisRangePlotWidgetDialog)
        self.yLabel.setObjectName("yLabel")
        self.gridLayout.addWidget(self.yLabel, 1, 0, 1, 1)
        self.yminLineEdit = QtWidgets.QLineEdit(QArkSetAxisRangePlotWidgetDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yminLineEdit.sizePolicy().hasHeightForWidth())
        self.yminLineEdit.setSizePolicy(sizePolicy)
        self.yminLineEdit.setObjectName("yminLineEdit")
        self.gridLayout.addWidget(self.yminLineEdit, 1, 1, 1, 1)
        self.ydashLabel = QtWidgets.QLabel(QArkSetAxisRangePlotWidgetDialog)
        self.ydashLabel.setObjectName("ydashLabel")
        self.gridLayout.addWidget(self.ydashLabel, 1, 2, 1, 1)
        self.ymaxLineEdit = QtWidgets.QLineEdit(QArkSetAxisRangePlotWidgetDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ymaxLineEdit.sizePolicy().hasHeightForWidth())
        self.ymaxLineEdit.setSizePolicy(sizePolicy)
        self.ymaxLineEdit.setObjectName("ymaxLineEdit")
        self.gridLayout.addWidget(self.ymaxLineEdit, 1, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 4, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.buttonBox = QtWidgets.QDialogButtonBox(QArkSetAxisRangePlotWidgetDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(QArkSetAxisRangePlotWidgetDialog)
        self.buttonBox.accepted.connect(QArkSetAxisRangePlotWidgetDialog.accept)
        self.buttonBox.rejected.connect(QArkSetAxisRangePlotWidgetDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(QArkSetAxisRangePlotWidgetDialog)

    def retranslateUi(self, QArkSetAxisRangePlotWidgetDialog):
        _translate = QtCore.QCoreApplication.translate
        QArkSetAxisRangePlotWidgetDialog.setWindowTitle(_translate("QArkSetAxisRangePlotWidgetDialog", "Dialog"))
        self.xLabel.setText(_translate("QArkSetAxisRangePlotWidgetDialog", "Axe X"))
        self.xdashLabel.setText(_translate("QArkSetAxisRangePlotWidgetDialog", "-"))
        self.yLabel.setText(_translate("QArkSetAxisRangePlotWidgetDialog", "Axe Y"))
        self.ydashLabel.setText(_translate("QArkSetAxisRangePlotWidgetDialog", "-"))

