# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QArkRangeSliderWidget.ui'
#
# Created: Fri Jun 19 13:05:07 2015
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

class Ui_QArkRangeSliderWidget(object):
    def setupUi(self, QArkRangeSliderWidget):
        QArkRangeSliderWidget.setObjectName(_fromUtf8("QArkRangeSliderWidget"))
        QArkRangeSliderWidget.resize(248, 37)
        self.verticalLayout = QtGui.QVBoxLayout(QArkRangeSliderWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.slider = QxtSpanSlider(QArkRangeSliderWidget)
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setObjectName(_fromUtf8("slider"))
        self.verticalLayout.addWidget(self.slider)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.minValueLabel = QtGui.QLabel(QArkRangeSliderWidget)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.minValueLabel.setFont(font)
        self.minValueLabel.setObjectName(_fromUtf8("minValueLabel"))
        self.horizontalLayout.addWidget(self.minValueLabel)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.maxValueLabel = QtGui.QLabel(QArkRangeSliderWidget)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.maxValueLabel.setFont(font)
        self.maxValueLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.maxValueLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.maxValueLabel.setObjectName(_fromUtf8("maxValueLabel"))
        self.horizontalLayout.addWidget(self.maxValueLabel)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(QArkRangeSliderWidget)
        QtCore.QMetaObject.connectSlotsByName(QArkRangeSliderWidget)

    def retranslateUi(self, QArkRangeSliderWidget):
        QArkRangeSliderWidget.setWindowTitle(_translate("QArkRangeSliderWidget", "Form", None))
        self.minValueLabel.setText(_translate("QArkRangeSliderWidget", "Min", None))
        self.maxValueLabel.setText(_translate("QArkRangeSliderWidget", "Max", None))

from QxtSpanSlider import QxtSpanSlider
