# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Dev\python\pyQArk\pyQArk\Widgets\QArkStatusWidget\QArkStatusWidget.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_QArkStatusWidget(object):
    def setupUi(self, QArkStatusWidget):
        QArkStatusWidget.setObjectName(_fromUtf8("QArkStatusWidget"))
        QArkStatusWidget.resize(668, 36)
        self.verticalLayout = QtGui.QVBoxLayout(QArkStatusWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.statusLabel = QtGui.QLabel(QArkStatusWidget)
        self.statusLabel.setObjectName(_fromUtf8("statusLabel"))
        self.gridLayout.addWidget(self.statusLabel, 0, 0, 1, 2)
        self.progressLabel = QtGui.QLabel(QArkStatusWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressLabel.sizePolicy().hasHeightForWidth())
        self.progressLabel.setSizePolicy(sizePolicy)
        self.progressLabel.setObjectName(_fromUtf8("progressLabel"))
        self.gridLayout.addWidget(self.progressLabel, 1, 0, 1, 1)
        self.progressBar = QtGui.QProgressBar(QArkStatusWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setMinimumSize(QtCore.QSize(200, 16))
        self.progressBar.setMaximumSize(QtCore.QSize(200, 16))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QtGui.QProgressBar.TopToBottom)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.gridLayout.addWidget(self.progressBar, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(QArkStatusWidget)
        QtCore.QMetaObject.connectSlotsByName(QArkStatusWidget)

    def retranslateUi(self, QArkStatusWidget):
        QArkStatusWidget.setWindowTitle(_translate("QArkStatusWidget", "Form", None))
        self.statusLabel.setText(_translate("QArkStatusWidget", "StatusMessage", None))
        self.progressLabel.setText(_translate("QArkStatusWidget", "ProcessingMessage", None))

