# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\VMShare\MyProjects\pyQArk\pyQArk\Dialogs\QArkOpenFilterFileDialog\QArkOpenFilterFileDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QArkOpenFilterFileDialog(object):
    def setupUi(self, QArkOpenFilterFileDialog):
        QArkOpenFilterFileDialog.setObjectName("QArkOpenFilterFileDialog")
        QArkOpenFilterFileDialog.resize(727, 586)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(QArkOpenFilterFileDialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.urlLabel = QtWidgets.QLabel(QArkOpenFilterFileDialog)
        self.urlLabel.setObjectName("urlLabel")
        self.horizontalLayout_2.addWidget(self.urlLabel)
        self.urlLineEdit = QtWidgets.QLineEdit(QArkOpenFilterFileDialog)
        self.urlLineEdit.setEnabled(True)
        self.urlLineEdit.setFrame(True)
        self.urlLineEdit.setObjectName("urlLineEdit")
        self.horizontalLayout_2.addWidget(self.urlLineEdit)
        self.urlToolButton = QtWidgets.QToolButton(QArkOpenFilterFileDialog)
        self.urlToolButton.setObjectName("urlToolButton")
        self.horizontalLayout_2.addWidget(self.urlToolButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.line = QtWidgets.QFrame(QArkOpenFilterFileDialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.splitter = QtWidgets.QSplitter(QArkOpenFilterFileDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.directoryLabel = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.directoryLabel.sizePolicy().hasHeightForWidth())
        self.directoryLabel.setSizePolicy(sizePolicy)
        self.directoryLabel.setObjectName("directoryLabel")
        self.verticalLayout.addWidget(self.directoryLabel)
        self.directoryListWidget = QtWidgets.QListWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.directoryListWidget.sizePolicy().hasHeightForWidth())
        self.directoryListWidget.setSizePolicy(sizePolicy)
        self.directoryListWidget.setObjectName("directoryListWidget")
        self.verticalLayout.addWidget(self.directoryListWidget)
        self.widget1 = QtWidgets.QWidget(self.splitter)
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.fileLabel = QtWidgets.QLabel(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fileLabel.sizePolicy().hasHeightForWidth())
        self.fileLabel.setSizePolicy(sizePolicy)
        self.fileLabel.setObjectName("fileLabel")
        self.verticalLayout_2.addWidget(self.fileLabel)
        self.fileListWidget = QtWidgets.QListWidget(self.widget1)
        self.fileListWidget.setObjectName("fileListWidget")
        self.verticalLayout_2.addWidget(self.fileListWidget)
        self.verticalLayout_3.addWidget(self.splitter)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.filterLabel = QtWidgets.QLabel(QArkOpenFilterFileDialog)
        self.filterLabel.setObjectName("filterLabel")
        self.horizontalLayout.addWidget(self.filterLabel)
        self.filterLineEdit = QtWidgets.QLineEdit(QArkOpenFilterFileDialog)
        self.filterLineEdit.setObjectName("filterLineEdit")
        self.horizontalLayout.addWidget(self.filterLineEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(QArkOpenFilterFileDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Open)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_3.addWidget(self.buttonBox)

        self.retranslateUi(QArkOpenFilterFileDialog)
        self.buttonBox.accepted.connect(QArkOpenFilterFileDialog.accept)
        self.buttonBox.rejected.connect(QArkOpenFilterFileDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(QArkOpenFilterFileDialog)

    def retranslateUi(self, QArkOpenFilterFileDialog):
        _translate = QtCore.QCoreApplication.translate
        QArkOpenFilterFileDialog.setWindowTitle(_translate("QArkOpenFilterFileDialog", "Dialog"))
        self.urlLabel.setText(_translate("QArkOpenFilterFileDialog", "URL"))
        self.urlToolButton.setText(_translate("QArkOpenFilterFileDialog", "..."))
        self.directoryLabel.setText(_translate("QArkOpenFilterFileDialog", "Directories"))
        self.fileLabel.setText(_translate("QArkOpenFilterFileDialog", "Files"))
        self.filterLabel.setText(_translate("QArkOpenFilterFileDialog", "Filter"))

