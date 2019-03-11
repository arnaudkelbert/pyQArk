# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\VMShare\MyProjects\pyQArk\pyQArk\Widgets\QArkHorizontalSlider\QArkHorizontalSlider.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QArkHorizontalSlider(object):
    def setupUi(self, QArkHorizontalSlider):
        QArkHorizontalSlider.setObjectName("QArkHorizontalSlider")
        QArkHorizontalSlider.resize(213, 31)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(QArkHorizontalSlider.sizePolicy().hasHeightForWidth())
        QArkHorizontalSlider.setSizePolicy(sizePolicy)
        QArkHorizontalSlider.setMinimumSize(QtCore.QSize(0, 0))
        self.horizontalLayout = QtWidgets.QHBoxLayout(QArkHorizontalSlider)
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(QArkHorizontalSlider)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.horizontalSlider = QtWidgets.QSlider(QArkHorizontalSlider)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout.addWidget(self.horizontalSlider)
        self.spinBox = QtWidgets.QSpinBox(QArkHorizontalSlider)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)

        self.retranslateUi(QArkHorizontalSlider)
        QtCore.QMetaObject.connectSlotsByName(QArkHorizontalSlider)

    def retranslateUi(self, QArkHorizontalSlider):
        _translate = QtCore.QCoreApplication.translate
        QArkHorizontalSlider.setWindowTitle(_translate("QArkHorizontalSlider", "Form"))
        self.label.setText(_translate("QArkHorizontalSlider", "TextLabel"))

