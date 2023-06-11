# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\VMShare\MyProjects\pyQArk\pyQArk\Widgets\QArkMessageTabWidget\QArkMessageTabWidget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QArkMessageTabWidget(object):
    def setupUi(self, QArkMessageTabWidget):
        QArkMessageTabWidget.setObjectName("QArkMessageTabWidget")
        QArkMessageTabWidget.resize(577, 255)
        QArkMessageTabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        QArkMessageTabWidget.setAutoFillBackground(False)
        QArkMessageTabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        QArkMessageTabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        QArkMessageTabWidget.setElideMode(QtCore.Qt.ElideNone)
        QArkMessageTabWidget.setDocumentMode(True)
        QArkMessageTabWidget.setMovable(True)
        self.messageTab = QtWidgets.QWidget()
        self.messageTab.setObjectName("messageTab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.messageTab)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.messageListView = QtWidgets.QListView(self.messageTab)
        self.messageListView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.messageListView.setAlternatingRowColors(True)
        self.messageListView.setIconSize(QtCore.QSize(16, 16))
        self.messageListView.setProperty("isWrapping", False)
        self.messageListView.setWordWrap(True)
        self.messageListView.setSelectionRectVisible(True)
        self.messageListView.setObjectName("messageListView")
        self.verticalLayout_3.addWidget(self.messageListView)
        QArkMessageTabWidget.addTab(self.messageTab, "")
        self.warningTab = QtWidgets.QWidget()
        self.warningTab.setObjectName("warningTab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.warningTab)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.warningListView = QtWidgets.QListView(self.warningTab)
        self.warningListView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.warningListView.setAlternatingRowColors(True)
        self.warningListView.setIconSize(QtCore.QSize(16, 16))
        self.warningListView.setProperty("isWrapping", False)
        self.warningListView.setWordWrap(True)
        self.warningListView.setSelectionRectVisible(True)
        self.warningListView.setObjectName("warningListView")
        self.verticalLayout_2.addWidget(self.warningListView)
        QArkMessageTabWidget.addTab(self.warningTab, "")
        self.errorTab = QtWidgets.QWidget()
        self.errorTab.setObjectName("errorTab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.errorTab)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.errorListView = QtWidgets.QListView(self.errorTab)
        self.errorListView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.errorListView.setAlternatingRowColors(True)
        self.errorListView.setIconSize(QtCore.QSize(16, 16))
        self.errorListView.setProperty("isWrapping", False)
        self.errorListView.setModelColumn(0)
        self.errorListView.setUniformItemSizes(False)
        self.errorListView.setWordWrap(True)
        self.errorListView.setSelectionRectVisible(True)
        self.errorListView.setObjectName("errorListView")
        self.verticalLayout.addWidget(self.errorListView)
        QArkMessageTabWidget.addTab(self.errorTab, "")

        self.retranslateUi(QArkMessageTabWidget)
        QArkMessageTabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(QArkMessageTabWidget)

    def retranslateUi(self, QArkMessageTabWidget):
        _translate = QtCore.QCoreApplication.translate
        QArkMessageTabWidget.setWindowTitle(_translate("QArkMessageTabWidget", "TabWidget"))
        QArkMessageTabWidget.setTabText(QArkMessageTabWidget.indexOf(self.messageTab), _translate("QArkMessageTabWidget", "Message"))
        QArkMessageTabWidget.setTabText(QArkMessageTabWidget.indexOf(self.warningTab), _translate("QArkMessageTabWidget", "Warning"))
        QArkMessageTabWidget.setTabText(QArkMessageTabWidget.indexOf(self.errorTab), _translate("QArkMessageTabWidget", "Error"))

