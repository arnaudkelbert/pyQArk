# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QArkNavigationTabWidget.ui'
#
# Created: Mon Jul 28 09:03:57 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_QArkNavigationTabWidget(object):
    def setupUi(self, QArkNavigationTabWidget):
        QArkNavigationTabWidget.setObjectName(_fromUtf8("QArkNavigationTabWidget"))
        QArkNavigationTabWidget.resize(294, 551)

        self.retranslateUi(QArkNavigationTabWidget)
        QArkNavigationTabWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(QArkNavigationTabWidget)

    def retranslateUi(self, QArkNavigationTabWidget):
        QArkNavigationTabWidget.setWindowTitle(QtGui.QApplication.translate("QArkNavigationTabWidget", "TabWidget", None, QtGui.QApplication.UnicodeUTF8))

