# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QArkOptimizationParameterWidget.ui'
#
# Created: Mon Sep 11 16:01:17 2017
#      by: PyQt4 UI code generator 4.11.3
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

class Ui_QArkOptimizationParameterWidget(object):
    def setupUi(self, QArkOptimizationParameterWidget):
        QArkOptimizationParameterWidget.setObjectName(_fromUtf8("QArkOptimizationParameterWidget"))
        QArkOptimizationParameterWidget.resize(448, 39)
        self.horizontalLayout = QtGui.QHBoxLayout(QArkOptimizationParameterWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.valueLineEdit = QtGui.QLineEdit(QArkOptimizationParameterWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.valueLineEdit.sizePolicy().hasHeightForWidth())
        self.valueLineEdit.setSizePolicy(sizePolicy)
        self.valueLineEdit.setText(_fromUtf8(""))
        self.valueLineEdit.setObjectName(_fromUtf8("valueLineEdit"))
        self.horizontalLayout.addWidget(self.valueLineEdit)
        self.optimizeCheckBox = QtGui.QCheckBox(QArkOptimizationParameterWidget)
        self.optimizeCheckBox.setChecked(True)
        self.optimizeCheckBox.setObjectName(_fromUtf8("optimizeCheckBox"))
        self.horizontalLayout.addWidget(self.optimizeCheckBox)
        self.minCheckBox = QtGui.QCheckBox(QArkOptimizationParameterWidget)
        self.minCheckBox.setObjectName(_fromUtf8("minCheckBox"))
        self.horizontalLayout.addWidget(self.minCheckBox)
        self.minLineEdit = QtGui.QLineEdit(QArkOptimizationParameterWidget)
        self.minLineEdit.setObjectName(_fromUtf8("minLineEdit"))
        self.horizontalLayout.addWidget(self.minLineEdit)
        self.maxCheckBox = QtGui.QCheckBox(QArkOptimizationParameterWidget)
        self.maxCheckBox.setObjectName(_fromUtf8("maxCheckBox"))
        self.horizontalLayout.addWidget(self.maxCheckBox)
        self.maxLineEdit = QtGui.QLineEdit(QArkOptimizationParameterWidget)
        self.maxLineEdit.setObjectName(_fromUtf8("maxLineEdit"))
        self.horizontalLayout.addWidget(self.maxLineEdit)

        self.retranslateUi(QArkOptimizationParameterWidget)
        QtCore.QMetaObject.connectSlotsByName(QArkOptimizationParameterWidget)

    def retranslateUi(self, QArkOptimizationParameterWidget):
        QArkOptimizationParameterWidget.setWindowTitle(_translate("QArkOptimizationParameterWidget", "Form", None))
        self.optimizeCheckBox.setText(_translate("QArkOptimizationParameterWidget", "Optimize", None))
        self.minCheckBox.setText(_translate("QArkOptimizationParameterWidget", "Min", None))
        self.maxCheckBox.setText(_translate("QArkOptimizationParameterWidget", "Max", None))

