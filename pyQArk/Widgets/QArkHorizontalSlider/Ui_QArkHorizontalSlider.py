# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QArkHorizontalSlider.ui'
#
# Created: Fri Aug  1 14:36:28 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_QArkHorizontalSlider(object):
    def setupUi(self, QArkHorizontalSlider):
        QArkHorizontalSlider.setObjectName(_fromUtf8("QArkHorizontalSlider"))
        QArkHorizontalSlider.resize(213, 31)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(QArkHorizontalSlider.sizePolicy().hasHeightForWidth())
        QArkHorizontalSlider.setSizePolicy(sizePolicy)
        QArkHorizontalSlider.setMinimumSize(QtCore.QSize(0, 0))
        self.horizontalLayout = QtGui.QHBoxLayout(QArkHorizontalSlider)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setMargin(5)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(QArkHorizontalSlider)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.horizontalSlider = QtGui.QSlider(QArkHorizontalSlider)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QtGui.QSlider.NoTicks)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.horizontalLayout.addWidget(self.horizontalSlider)
        self.spinBox = QtGui.QSpinBox(QArkHorizontalSlider)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.horizontalLayout.addWidget(self.spinBox)

        self.retranslateUi(QArkHorizontalSlider)
        QtCore.QMetaObject.connectSlotsByName(QArkHorizontalSlider)

    def retranslateUi(self, QArkHorizontalSlider):
        QArkHorizontalSlider.setWindowTitle(QtGui.QApplication.translate("QArkHorizontalSlider", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("QArkHorizontalSlider", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))

