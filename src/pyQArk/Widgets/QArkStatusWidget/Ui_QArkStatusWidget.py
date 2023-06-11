# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Dev\python\pyQArk\pyQArk\Widgets\QArkStatusWidget\QArkStatusWidget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QArkStatusWidget(object):
    def setupUi(self, QArkStatusWidget):
        QArkStatusWidget.setObjectName("QArkStatusWidget")
        QArkStatusWidget.resize(668, 36)
        self.verticalLayout = QtWidgets.QVBoxLayout(QArkStatusWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.statusLabel = QtWidgets.QLabel(QArkStatusWidget)
        self.statusLabel.setObjectName("statusLabel")
        self.gridLayout.addWidget(self.statusLabel, 0, 0, 1, 2)
        self.progressLabel = QtWidgets.QLabel(QArkStatusWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressLabel.sizePolicy().hasHeightForWidth())
        self.progressLabel.setSizePolicy(sizePolicy)
        self.progressLabel.setObjectName("progressLabel")
        self.gridLayout.addWidget(self.progressLabel, 1, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(QArkStatusWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setMinimumSize(QtCore.QSize(200, 16))
        self.progressBar.setMaximumSize(QtCore.QSize(200, 16))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(QArkStatusWidget)
        QtCore.QMetaObject.connectSlotsByName(QArkStatusWidget)

    def retranslateUi(self, QArkStatusWidget):
        _translate = QtCore.QCoreApplication.translate
        QArkStatusWidget.setWindowTitle(_translate("QArkStatusWidget", "Form"))
        self.statusLabel.setText(_translate("QArkStatusWidget", "StatusMessage"))
        self.progressLabel.setText(_translate("QArkStatusWidget", "ProcessingMessage"))

