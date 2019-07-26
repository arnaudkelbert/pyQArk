# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\VMShare\MyProjects\pyQArk\pyQArk\Dialogs\QArkOpenFilterFileDialog\QArkOpenFilterFileDialog.ui'
#
# Created: Fri Jul 26 18:17:33 2019
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

class Ui_QArkOpenFilterFileDialog(object):
    def setupUi(self, QArkOpenFilterFileDialog):
        QArkOpenFilterFileDialog.setObjectName(_fromUtf8("QArkOpenFilterFileDialog"))
        QArkOpenFilterFileDialog.resize(727, 586)
        self.verticalLayout_3 = QtGui.QVBoxLayout(QArkOpenFilterFileDialog)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.urlLabel = QtGui.QLabel(QArkOpenFilterFileDialog)
        self.urlLabel.setObjectName(_fromUtf8("urlLabel"))
        self.horizontalLayout_2.addWidget(self.urlLabel)
        self.urlLineEdit = QtGui.QLineEdit(QArkOpenFilterFileDialog)
        self.urlLineEdit.setEnabled(True)
        self.urlLineEdit.setFrame(True)
        self.urlLineEdit.setObjectName(_fromUtf8("urlLineEdit"))
        self.horizontalLayout_2.addWidget(self.urlLineEdit)
        self.urlToolButton = QtGui.QToolButton(QArkOpenFilterFileDialog)
        self.urlToolButton.setObjectName(_fromUtf8("urlToolButton"))
        self.horizontalLayout_2.addWidget(self.urlToolButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.line = QtGui.QFrame(QArkOpenFilterFileDialog)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_3.addWidget(self.line)
        self.splitter = QtGui.QSplitter(QArkOpenFilterFileDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.widget = QtGui.QWidget(self.splitter)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.directoryLabel = QtGui.QLabel(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.directoryLabel.sizePolicy().hasHeightForWidth())
        self.directoryLabel.setSizePolicy(sizePolicy)
        self.directoryLabel.setObjectName(_fromUtf8("directoryLabel"))
        self.verticalLayout.addWidget(self.directoryLabel)
        self.directoryListWidget = QtGui.QListWidget(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.directoryListWidget.sizePolicy().hasHeightForWidth())
        self.directoryListWidget.setSizePolicy(sizePolicy)
        self.directoryListWidget.setObjectName(_fromUtf8("directoryListWidget"))
        self.verticalLayout.addWidget(self.directoryListWidget)
        self.widget1 = QtGui.QWidget(self.splitter)
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.fileLabel = QtGui.QLabel(self.widget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fileLabel.sizePolicy().hasHeightForWidth())
        self.fileLabel.setSizePolicy(sizePolicy)
        self.fileLabel.setObjectName(_fromUtf8("fileLabel"))
        self.verticalLayout_2.addWidget(self.fileLabel)
        self.fileListWidget = QtGui.QListWidget(self.widget1)
        self.fileListWidget.setObjectName(_fromUtf8("fileListWidget"))
        self.verticalLayout_2.addWidget(self.fileListWidget)
        self.verticalLayout_3.addWidget(self.splitter)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.filterLabel = QtGui.QLabel(QArkOpenFilterFileDialog)
        self.filterLabel.setObjectName(_fromUtf8("filterLabel"))
        self.horizontalLayout.addWidget(self.filterLabel)
        self.filterLineEdit = QtGui.QLineEdit(QArkOpenFilterFileDialog)
        self.filterLineEdit.setObjectName(_fromUtf8("filterLineEdit"))
        self.horizontalLayout.addWidget(self.filterLineEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.buttonBox = QtGui.QDialogButtonBox(QArkOpenFilterFileDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Open)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_3.addWidget(self.buttonBox)

        self.retranslateUi(QArkOpenFilterFileDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), QArkOpenFilterFileDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), QArkOpenFilterFileDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(QArkOpenFilterFileDialog)

    def retranslateUi(self, QArkOpenFilterFileDialog):
        QArkOpenFilterFileDialog.setWindowTitle(_translate("QArkOpenFilterFileDialog", "Dialog", None))
        self.urlLabel.setText(_translate("QArkOpenFilterFileDialog", "URL", None))
        self.urlToolButton.setText(_translate("QArkOpenFilterFileDialog", "...", None))
        self.directoryLabel.setText(_translate("QArkOpenFilterFileDialog", "Directories", None))
        self.fileLabel.setText(_translate("QArkOpenFilterFileDialog", "Files", None))
        self.filterLabel.setText(_translate("QArkOpenFilterFileDialog", "Filter", None))

