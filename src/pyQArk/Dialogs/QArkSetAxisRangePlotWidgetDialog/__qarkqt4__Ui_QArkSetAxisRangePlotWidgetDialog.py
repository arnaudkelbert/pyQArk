# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\kelbera\Documents\DEV\PYTHON\pyQArk_base\pyQArk\Dialogs\QArkSetAxisRangePlotWidgetDialog\QArkSetAxisRangePlotWidgetDialog.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_QArkSetAxisRangePlotWidgetDialog(object):
    def setupUi(self, QArkSetAxisRangePlotWidgetDialog):
        QArkSetAxisRangePlotWidgetDialog.setObjectName(_fromUtf8("QArkSetAxisRangePlotWidgetDialog"))
        QArkSetAxisRangePlotWidgetDialog.resize(304, 113)
        self.verticalLayout = QtGui.QVBoxLayout(QArkSetAxisRangePlotWidgetDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.xLabel = QtGui.QLabel(QArkSetAxisRangePlotWidgetDialog)
        self.xLabel.setObjectName(_fromUtf8("xLabel"))
        self.gridLayout.addWidget(self.xLabel, 0, 0, 1, 1)
        self.xminLineEdit = QtGui.QLineEdit(QArkSetAxisRangePlotWidgetDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xminLineEdit.sizePolicy().hasHeightForWidth())
        self.xminLineEdit.setSizePolicy(sizePolicy)
        self.xminLineEdit.setObjectName(_fromUtf8("xminLineEdit"))
        self.gridLayout.addWidget(self.xminLineEdit, 0, 1, 1, 1)
        self.xdashLabel = QtGui.QLabel(QArkSetAxisRangePlotWidgetDialog)
        self.xdashLabel.setObjectName(_fromUtf8("xdashLabel"))
        self.gridLayout.addWidget(self.xdashLabel, 0, 2, 1, 1)
        self.xmaxLineEdit = QtGui.QLineEdit(QArkSetAxisRangePlotWidgetDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xmaxLineEdit.sizePolicy().hasHeightForWidth())
        self.xmaxLineEdit.setSizePolicy(sizePolicy)
        self.xmaxLineEdit.setObjectName(_fromUtf8("xmaxLineEdit"))
        self.gridLayout.addWidget(self.xmaxLineEdit, 0, 3, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 4, 1, 1)
        self.yLabel = QtGui.QLabel(QArkSetAxisRangePlotWidgetDialog)
        self.yLabel.setObjectName(_fromUtf8("yLabel"))
        self.gridLayout.addWidget(self.yLabel, 1, 0, 1, 1)
        self.yminLineEdit = QtGui.QLineEdit(QArkSetAxisRangePlotWidgetDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yminLineEdit.sizePolicy().hasHeightForWidth())
        self.yminLineEdit.setSizePolicy(sizePolicy)
        self.yminLineEdit.setObjectName(_fromUtf8("yminLineEdit"))
        self.gridLayout.addWidget(self.yminLineEdit, 1, 1, 1, 1)
        self.ydashLabel = QtGui.QLabel(QArkSetAxisRangePlotWidgetDialog)
        self.ydashLabel.setObjectName(_fromUtf8("ydashLabel"))
        self.gridLayout.addWidget(self.ydashLabel, 1, 2, 1, 1)
        self.ymaxLineEdit = QtGui.QLineEdit(QArkSetAxisRangePlotWidgetDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ymaxLineEdit.sizePolicy().hasHeightForWidth())
        self.ymaxLineEdit.setSizePolicy(sizePolicy)
        self.ymaxLineEdit.setObjectName(_fromUtf8("ymaxLineEdit"))
        self.gridLayout.addWidget(self.ymaxLineEdit, 1, 3, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 4, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem2 = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.buttonBox = QtGui.QDialogButtonBox(QArkSetAxisRangePlotWidgetDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(QArkSetAxisRangePlotWidgetDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), QArkSetAxisRangePlotWidgetDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), QArkSetAxisRangePlotWidgetDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(QArkSetAxisRangePlotWidgetDialog)

    def retranslateUi(self, QArkSetAxisRangePlotWidgetDialog):
        QArkSetAxisRangePlotWidgetDialog.setWindowTitle(_translate("QArkSetAxisRangePlotWidgetDialog", "Dialog", None))
        self.xLabel.setText(_translate("QArkSetAxisRangePlotWidgetDialog", "Axe X", None))
        self.xdashLabel.setText(_translate("QArkSetAxisRangePlotWidgetDialog", "-", None))
        self.yLabel.setText(_translate("QArkSetAxisRangePlotWidgetDialog", "Axe Y", None))
        self.ydashLabel.setText(_translate("QArkSetAxisRangePlotWidgetDialog", "-", None))

