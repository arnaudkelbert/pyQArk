# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\kelbera\Documents\DEV\PYTHON\pyQArk_base\pyQArk\Dialogs\QArkWorkerThreadRunDialog\QArkWorkerThreadRunDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QArkWorkerThreadRunDialog(object):
    def setupUi(self, QArkWorkerThreadRunDialog):
        QArkWorkerThreadRunDialog.setObjectName("QArkWorkerThreadRunDialog")
        QArkWorkerThreadRunDialog.resize(598, 353)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(QArkWorkerThreadRunDialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(QArkWorkerThreadRunDialog)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.South)
        self.tabWidget.setObjectName("tabWidget")
        self.stdoutTab = QtWidgets.QWidget()
        self.stdoutTab.setObjectName("stdoutTab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.stdoutTab)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stdoutPlainTextEdit = QtWidgets.QPlainTextEdit(self.stdoutTab)
        self.stdoutPlainTextEdit.setObjectName("stdoutPlainTextEdit")
        self.verticalLayout.addWidget(self.stdoutPlainTextEdit)
        self.tabWidget.addTab(self.stdoutTab, "")
        self.stderrTab = QtWidgets.QWidget()
        self.stderrTab.setObjectName("stderrTab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.stderrTab)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stderrPlainTextEdit = QtWidgets.QPlainTextEdit(self.stderrTab)
        self.stderrPlainTextEdit.setObjectName("stderrPlainTextEdit")
        self.verticalLayout_2.addWidget(self.stderrPlainTextEdit)
        self.tabWidget.addTab(self.stderrTab, "")
        self.verticalLayout_3.addWidget(self.tabWidget)
        self.buttonBox = QtWidgets.QDialogButtonBox(QArkWorkerThreadRunDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Abort|QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_3.addWidget(self.buttonBox)

        self.retranslateUi(QArkWorkerThreadRunDialog)
        self.tabWidget.setCurrentIndex(0)
        self.buttonBox.accepted.connect(QArkWorkerThreadRunDialog.accept)
        self.buttonBox.rejected.connect(QArkWorkerThreadRunDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(QArkWorkerThreadRunDialog)

    def retranslateUi(self, QArkWorkerThreadRunDialog):
        _translate = QtCore.QCoreApplication.translate
        QArkWorkerThreadRunDialog.setWindowTitle(_translate("QArkWorkerThreadRunDialog", "Dialog"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.stdoutTab), _translate("QArkWorkerThreadRunDialog", "StdOut"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.stderrTab), _translate("QArkWorkerThreadRunDialog", "StdErr"))

