# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QArkMessageTabWidget.ui'
#
# Created: Sat Mar  7 20:32:39 2015
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

class Ui_QArkMessageTabWidget(object):
    def setupUi(self, QArkMessageTabWidget):
        QArkMessageTabWidget.setObjectName(_fromUtf8("QArkMessageTabWidget"))
        QArkMessageTabWidget.resize(577, 255)
        QArkMessageTabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        QArkMessageTabWidget.setAutoFillBackground(False)
        QArkMessageTabWidget.setTabPosition(QtGui.QTabWidget.North)
        QArkMessageTabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        QArkMessageTabWidget.setElideMode(QtCore.Qt.ElideNone)
        QArkMessageTabWidget.setDocumentMode(True)
        QArkMessageTabWidget.setMovable(True)
        self.messageTab = QtGui.QWidget()
        self.messageTab.setObjectName(_fromUtf8("messageTab"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.messageTab)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.messageListView = QtGui.QListView(self.messageTab)
        self.messageListView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.messageListView.setAlternatingRowColors(True)
        self.messageListView.setIconSize(QtCore.QSize(16, 16))
        self.messageListView.setProperty("isWrapping", False)
        self.messageListView.setSpacing(3)
        self.messageListView.setWordWrap(True)
        self.messageListView.setSelectionRectVisible(True)
        self.messageListView.setObjectName(_fromUtf8("messageListView"))
        self.verticalLayout_3.addWidget(self.messageListView)
        QArkMessageTabWidget.addTab(self.messageTab, _fromUtf8(""))
        self.warningTab = QtGui.QWidget()
        self.warningTab.setObjectName(_fromUtf8("warningTab"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.warningTab)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.warningListView = QtGui.QListView(self.warningTab)
        self.warningListView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.warningListView.setAlternatingRowColors(True)
        self.warningListView.setIconSize(QtCore.QSize(16, 16))
        self.warningListView.setProperty("isWrapping", False)
        self.warningListView.setSpacing(3)
        self.warningListView.setWordWrap(True)
        self.warningListView.setSelectionRectVisible(True)
        self.warningListView.setObjectName(_fromUtf8("warningListView"))
        self.verticalLayout_2.addWidget(self.warningListView)
        QArkMessageTabWidget.addTab(self.warningTab, _fromUtf8(""))
        self.errorTab = QtGui.QWidget()
        self.errorTab.setObjectName(_fromUtf8("errorTab"))
        self.verticalLayout = QtGui.QVBoxLayout(self.errorTab)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.errorListView = QtGui.QListView(self.errorTab)
        self.errorListView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.errorListView.setAlternatingRowColors(True)
        self.errorListView.setIconSize(QtCore.QSize(16, 16))
        self.errorListView.setProperty("isWrapping", False)
        self.errorListView.setSpacing(3)
        self.errorListView.setModelColumn(0)
        self.errorListView.setUniformItemSizes(False)
        self.errorListView.setWordWrap(True)
        self.errorListView.setSelectionRectVisible(True)
        self.errorListView.setObjectName(_fromUtf8("errorListView"))
        self.verticalLayout.addWidget(self.errorListView)
        QArkMessageTabWidget.addTab(self.errorTab, _fromUtf8(""))

        self.retranslateUi(QArkMessageTabWidget)
        QArkMessageTabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(QArkMessageTabWidget)

    def retranslateUi(self, QArkMessageTabWidget):
        QArkMessageTabWidget.setWindowTitle(_translate("QArkMessageTabWidget", "TabWidget", None))
        QArkMessageTabWidget.setTabText(QArkMessageTabWidget.indexOf(self.messageTab), _translate("QArkMessageTabWidget", "Message", None))
        QArkMessageTabWidget.setTabText(QArkMessageTabWidget.indexOf(self.warningTab), _translate("QArkMessageTabWidget", "Warning", None))
        QArkMessageTabWidget.setTabText(QArkMessageTabWidget.indexOf(self.errorTab), _translate("QArkMessageTabWidget", "Error", None))

