# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\VMShare\MyProjects\pyQArk\pyQArk\Widgets\QArkListWidgetNavigationWidget\QArkListWidgetNavigationWidget.ui'
#
# Created: Fri Mar 29 21:34:28 2019
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

class Ui_QArkListWidgetNavigationWidget(object):
    def setupUi(self, QArkListWidgetNavigationWidget):
        QArkListWidgetNavigationWidget.setObjectName(_fromUtf8("QArkListWidgetNavigationWidget"))
        QArkListWidgetNavigationWidget.resize(703, 432)
        self.gridLayout = QtGui.QGridLayout(QArkListWidgetNavigationWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.listWidget = QtGui.QListWidget(QArkListWidgetNavigationWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMinimumSize(QtCore.QSize(250, 0))
        self.listWidget.setMaximumSize(QtCore.QSize(250, 16777215))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.gridLayout.addWidget(self.listWidget, 0, 0, 4, 1)
        self.label = QtGui.QLabel(QArkListWidgetNavigationWidget)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setMargin(5)
        self.label.setIndent(10)
        self.label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.line = QtGui.QFrame(QArkListWidgetNavigationWidget)
        self.line.setFrameShadow(QtGui.QFrame.Plain)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 1, 1, 1, 2)
        self.stackedWidget = QtGui.QStackedWidget(QArkListWidgetNavigationWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.gridLayout.addWidget(self.stackedWidget, 2, 1, 1, 2)
        spacerItem = QtGui.QSpacerItem(20, 189, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 2, 1, 1)

        self.retranslateUi(QArkListWidgetNavigationWidget)
        self.stackedWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(QArkListWidgetNavigationWidget)

    def retranslateUi(self, QArkListWidgetNavigationWidget):
        QArkListWidgetNavigationWidget.setWindowTitle(_translate("QArkListWidgetNavigationWidget", "Form", None))
        self.label.setText(_translate("QArkListWidgetNavigationWidget", "Please select an item", None))

