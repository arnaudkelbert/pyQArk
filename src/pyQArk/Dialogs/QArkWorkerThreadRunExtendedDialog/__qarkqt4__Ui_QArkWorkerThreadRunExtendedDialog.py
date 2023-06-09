# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\kelbera\Documents\DEV\PYTHON\pyQArk_base\pyQArk\Dialogs\QArkWorkerThreadRunExtendedDialog\QArkWorkerThreadRunExtendedDialog.ui'
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

class Ui_QArkWorkerThreadRunExtendedDialog(object):
    def setupUi(self, QArkWorkerThreadRunExtendedDialog):
        QArkWorkerThreadRunExtendedDialog.setObjectName(_fromUtf8("QArkWorkerThreadRunExtendedDialog"))
        QArkWorkerThreadRunExtendedDialog.setWindowModality(QtCore.Qt.WindowModal)
        QArkWorkerThreadRunExtendedDialog.resize(477, 334)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(QArkWorkerThreadRunExtendedDialog.sizePolicy().hasHeightForWidth())
        QArkWorkerThreadRunExtendedDialog.setSizePolicy(sizePolicy)
        QArkWorkerThreadRunExtendedDialog.setModal(True)
        self.verticalLayout_5 = QtGui.QVBoxLayout(QArkWorkerThreadRunExtendedDialog)
        self.verticalLayout_5.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.frame = QtGui.QFrame(QArkWorkerThreadRunExtendedDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Plain)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.movieLabel = QtGui.QLabel(self.frame)
        self.movieLabel.setText(_fromUtf8(""))
        self.movieLabel.setObjectName(_fromUtf8("movieLabel"))
        self.gridLayout.addWidget(self.movieLabel, 0, 0, 3, 1)
        spacerItem = QtGui.QSpacerItem(20, 2, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.promptLabel = QtGui.QLabel(self.frame)
        self.promptLabel.setObjectName(_fromUtf8("promptLabel"))
        self.gridLayout.addWidget(self.promptLabel, 1, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 2, 2, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 2, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem2, 2, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.progressBar = QtGui.QProgressBar(self.frame)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout_3.addWidget(self.progressBar)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.keepOpenCheckBox = QtGui.QCheckBox(self.frame)
        self.keepOpenCheckBox.setChecked(True)
        self.keepOpenCheckBox.setObjectName(_fromUtf8("keepOpenCheckBox"))
        self.horizontalLayout.addWidget(self.keepOpenCheckBox)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.showDetailsPushButton = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.showDetailsPushButton.sizePolicy().hasHeightForWidth())
        self.showDetailsPushButton.setSizePolicy(sizePolicy)
        self.showDetailsPushButton.setObjectName(_fromUtf8("showDetailsPushButton"))
        self.horizontalLayout.addWidget(self.showDetailsPushButton)
        spacerItem4 = QtGui.QSpacerItem(18, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.buttonBox = QtGui.QDialogButtonBox(self.frame)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Abort|QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout.addWidget(self.buttonBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_5.addWidget(self.frame)
        self.tabWidget = QtGui.QTabWidget(QArkWorkerThreadRunExtendedDialog)
        self.tabWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tabWidget.setTabPosition(QtGui.QTabWidget.South)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.stdoutTab = QtGui.QWidget()
        self.stdoutTab.setObjectName(_fromUtf8("stdoutTab"))
        self.verticalLayout = QtGui.QVBoxLayout(self.stdoutTab)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.stdoutPlainTextEdit = QtGui.QPlainTextEdit(self.stdoutTab)
        self.stdoutPlainTextEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.stdoutPlainTextEdit.setLineWrapMode(QtGui.QPlainTextEdit.NoWrap)
        self.stdoutPlainTextEdit.setReadOnly(True)
        self.stdoutPlainTextEdit.setObjectName(_fromUtf8("stdoutPlainTextEdit"))
        self.verticalLayout.addWidget(self.stdoutPlainTextEdit)
        self.tabWidget.addTab(self.stdoutTab, _fromUtf8(""))
        self.stderrTab = QtGui.QWidget()
        self.stderrTab.setObjectName(_fromUtf8("stderrTab"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.stderrTab)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.stderrPlainTextEdit = QtGui.QPlainTextEdit(self.stderrTab)
        self.stderrPlainTextEdit.setLineWrapMode(QtGui.QPlainTextEdit.NoWrap)
        self.stderrPlainTextEdit.setObjectName(_fromUtf8("stderrPlainTextEdit"))
        self.verticalLayout_2.addWidget(self.stderrPlainTextEdit)
        self.tabWidget.addTab(self.stderrTab, _fromUtf8(""))
        self.verticalLayout_5.addWidget(self.tabWidget)

        self.retranslateUi(QArkWorkerThreadRunExtendedDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), QArkWorkerThreadRunExtendedDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), QArkWorkerThreadRunExtendedDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(QArkWorkerThreadRunExtendedDialog)

    def retranslateUi(self, QArkWorkerThreadRunExtendedDialog):
        QArkWorkerThreadRunExtendedDialog.setWindowTitle(_translate("QArkWorkerThreadRunExtendedDialog", "Dialog", None))
        self.promptLabel.setText(_translate("QArkWorkerThreadRunExtendedDialog", "Please wait...", None))
        self.keepOpenCheckBox.setText(_translate("QArkWorkerThreadRunExtendedDialog", "Keep dialog open", None))
        self.showDetailsPushButton.setText(_translate("QArkWorkerThreadRunExtendedDialog", "Show details", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.stdoutTab), _translate("QArkWorkerThreadRunExtendedDialog", "StdOut", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.stderrTab), _translate("QArkWorkerThreadRunExtendedDialog", "StdErr", None))

