# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QArkWorkerThreadRunDialog.ui'
#
# Created: Sun Mar  8 14:39:20 2015
#      by: PyQt4 UI code generator 4.11.2
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

class Ui_QArkWorkerThreadRunDialog(object):
    def setupUi(self, QArkWorkerThreadRunDialog):
        QArkWorkerThreadRunDialog.setObjectName(_fromUtf8("QArkWorkerThreadRunDialog"))
        QArkWorkerThreadRunDialog.resize(598, 353)
        self.verticalLayout_3 = QtGui.QVBoxLayout(QArkWorkerThreadRunDialog)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.tabWidget = QtGui.QTabWidget(QArkWorkerThreadRunDialog)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.South)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.stdoutTab = QtGui.QWidget()
        self.stdoutTab.setObjectName(_fromUtf8("stdoutTab"))
        self.verticalLayout = QtGui.QVBoxLayout(self.stdoutTab)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.stdoutPlainTextEdit = QtGui.QPlainTextEdit(self.stdoutTab)
        self.stdoutPlainTextEdit.setObjectName(_fromUtf8("stdoutPlainTextEdit"))
        self.verticalLayout.addWidget(self.stdoutPlainTextEdit)
        self.tabWidget.addTab(self.stdoutTab, _fromUtf8(""))
        self.stderrTab = QtGui.QWidget()
        self.stderrTab.setObjectName(_fromUtf8("stderrTab"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.stderrTab)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.stderrPlainTextEdit = QtGui.QPlainTextEdit(self.stderrTab)
        self.stderrPlainTextEdit.setObjectName(_fromUtf8("stderrPlainTextEdit"))
        self.verticalLayout_2.addWidget(self.stderrPlainTextEdit)
        self.tabWidget.addTab(self.stderrTab, _fromUtf8(""))
        self.verticalLayout_3.addWidget(self.tabWidget)
        self.buttonBox = QtGui.QDialogButtonBox(QArkWorkerThreadRunDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Abort|QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_3.addWidget(self.buttonBox)

        self.retranslateUi(QArkWorkerThreadRunDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), QArkWorkerThreadRunDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), QArkWorkerThreadRunDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(QArkWorkerThreadRunDialog)

    def retranslateUi(self, QArkWorkerThreadRunDialog):
        QArkWorkerThreadRunDialog.setWindowTitle(_translate("QArkWorkerThreadRunDialog", "Dialog", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.stdoutTab), _translate("QArkWorkerThreadRunDialog", "StdOut", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.stderrTab), _translate("QArkWorkerThreadRunDialog", "StdErr", None))

