# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\VMShare\MyProjects\pyQArk\pyQArk\Widgets\QArkListWidgetNavigationWidget\QArkListWidgetNavigationWidget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QArkListWidgetNavigationWidget(object):
    def setupUi(self, QArkListWidgetNavigationWidget):
        QArkListWidgetNavigationWidget.setObjectName("QArkListWidgetNavigationWidget")
        QArkListWidgetNavigationWidget.resize(703, 432)
        self.gridLayout = QtWidgets.QGridLayout(QArkListWidgetNavigationWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.listWidget = QtWidgets.QListWidget(QArkListWidgetNavigationWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMinimumSize(QtCore.QSize(250, 0))
        self.listWidget.setMaximumSize(QtCore.QSize(250, 16777215))
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 0, 0, 4, 1)
        self.label = QtWidgets.QLabel(QArkListWidgetNavigationWidget)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setIndent(10)
        self.label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.line = QtWidgets.QFrame(QArkListWidgetNavigationWidget)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 1, 1, 2)
        self.stackedWidget = QtWidgets.QStackedWidget(QArkListWidgetNavigationWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setObjectName("stackedWidget")
        self.gridLayout.addWidget(self.stackedWidget, 2, 1, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 189, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 2, 1, 1)

        self.retranslateUi(QArkListWidgetNavigationWidget)
        self.stackedWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(QArkListWidgetNavigationWidget)

    def retranslateUi(self, QArkListWidgetNavigationWidget):
        _translate = QtCore.QCoreApplication.translate
        QArkListWidgetNavigationWidget.setWindowTitle(_translate("QArkListWidgetNavigationWidget", "Form"))
        self.label.setText(_translate("QArkListWidgetNavigationWidget", "Please select an item"))

