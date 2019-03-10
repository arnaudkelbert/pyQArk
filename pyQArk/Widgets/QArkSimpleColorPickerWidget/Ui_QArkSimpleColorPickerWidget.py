# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QArkSimpleColorPickerWidget.ui'
#
# Created: Fri Aug  1 14:36:36 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_QArkSimpleColorPickerWidget(object):
    def setupUi(self, QArkSimpleColorPickerWidget):
        QArkSimpleColorPickerWidget.setObjectName(_fromUtf8("QArkSimpleColorPickerWidget"))
        QArkSimpleColorPickerWidget.resize(268, 118)
        self.horizontalLayout = QtGui.QHBoxLayout(QArkSimpleColorPickerWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.colorLabel = QArkClickableFilledRect(QArkSimpleColorPickerWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorLabel.sizePolicy().hasHeightForWidth())
        self.colorLabel.setSizePolicy(sizePolicy)
        self.colorLabel.setFrameShape(QtGui.QFrame.Box)
        self.colorLabel.setFrameShadow(QtGui.QFrame.Sunken)
        self.colorLabel.setObjectName(_fromUtf8("colorLabel"))
        self.verticalLayout_2.addWidget(self.colorLabel)
        spacerItem = QtGui.QSpacerItem(20, 68, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.redSlider = QArkHorizontalSlider(QArkSimpleColorPickerWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.redSlider.sizePolicy().hasHeightForWidth())
        self.redSlider.setSizePolicy(sizePolicy)
        self.redSlider.setObjectName(_fromUtf8("redSlider"))
        self.verticalLayout.addWidget(self.redSlider)
        self.greenSlider = QArkHorizontalSlider(QArkSimpleColorPickerWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.greenSlider.sizePolicy().hasHeightForWidth())
        self.greenSlider.setSizePolicy(sizePolicy)
        self.greenSlider.setObjectName(_fromUtf8("greenSlider"))
        self.verticalLayout.addWidget(self.greenSlider)
        self.blueSlider = QArkHorizontalSlider(QArkSimpleColorPickerWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.blueSlider.sizePolicy().hasHeightForWidth())
        self.blueSlider.setSizePolicy(sizePolicy)
        self.blueSlider.setObjectName(_fromUtf8("blueSlider"))
        self.verticalLayout.addWidget(self.blueSlider)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(QArkSimpleColorPickerWidget)
        QtCore.QMetaObject.connectSlotsByName(QArkSimpleColorPickerWidget)

    def retranslateUi(self, QArkSimpleColorPickerWidget):
        QArkSimpleColorPickerWidget.setWindowTitle(QtGui.QApplication.translate("QArkSimpleColorPickerWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.colorLabel.setText(QtGui.QApplication.translate("QArkSimpleColorPickerWidget", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))

from ..QArkHorizontalSlider.QArkHorizontalSlider import QArkHorizontalSlider
from ..QArkClickableFilledRect.QArkClickableFilledRect import QArkClickableFilledRect
