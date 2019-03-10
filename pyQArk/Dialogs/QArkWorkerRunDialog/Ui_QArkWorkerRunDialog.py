# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QArkWorkerRunDialog.ui'
#
# Created: Sat Mar  7 20:53:10 2015
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

class Ui_QArkWorkerRunDialog(object):
    def setupUi(self, QArkWorkerRunDialog):
        QArkWorkerRunDialog.setObjectName(_fromUtf8("QArkWorkerRunDialog"))
        QArkWorkerRunDialog.resize(598, 353)
        self.verticalLayout_3 = QtGui.QVBoxLayout(QArkWorkerRunDialog)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.tabWidget = QtGui.QTabWidget(QArkWorkerRunDialog)
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
        self.buttonBox = QtGui.QDialogButtonBox(QArkWorkerRunDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Abort|QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_3.addWidget(self.buttonBox)

        self.retranslateUi(QArkWorkerRunDialog)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), QArkWorkerRunDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), QArkWorkerRunDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(QArkWorkerRunDialog)

    def retranslateUi(self, QArkWorkerRunDialog):
        QArkWorkerRunDialog.setWindowTitle(_translate("QArkWorkerRunDialog", "Dialog", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.stdoutTab), _translate("QArkWorkerRunDialog", "StdOut", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.stderrTab), _translate("QArkWorkerRunDialog", "StdErr", None))

