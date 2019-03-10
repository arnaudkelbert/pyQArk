# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#
#
# QArkControlledStackedWidget
#
#
# @author : Arnaud Kelbert
# @date : 2019/03/05
# @version : 0.2
#
# Historic:
# 0.1 : init version
# 0.2 : add python 2/3 compatibility
#-----------------------------------------------------------------------
#{-- Pyhton 2/3 compatibility ------------------------------------------
from __future__ import (absolute_import, division, print_function, unicode_literals)
import sys
try:
    from future import standard_library
    standard_library.install_aliases()

    from builtins import (ascii, bytes, chr, dict, filter, hex, input,
                          int, map, next, oct, open, pow, range, round,
                          str, super, zip)
except ImportError:
    if sys.version_info.major == 2:
        print('Warning : future package is missing - compatibility issues between python 2 and 3 may occur')
try:
    # Python 2 : basestring exists (for isinstance test)
    basestring
except:
    # Python 3 : basestring does not exist
    basestring = str
#}-- Pyhton 2/3 compatibility ------------------------------------------
import unittest

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

class QArkControlledStackedWidget( QtGui.QWidget ):
    
    currentChanged = QtCore.pyqtSignal( 'int' )
    widgetRemoved = QtCore.pyqtSignal( 'int' )
    widgetAdded = QtCore.pyqtSignal( 'int' )
    widgetInserted = QtCore.pyqtSignal( 'int' )
    
    def __init__( self
                 ,parent
                 ):
        super( QArkControlledStackedWidget, self ).__init__(parent)
        self.initUi()
        self.initValues(  )
        self.initConnection()
        
    def initUi(self):
        self.setObjectName(_fromUtf8("qArkControlledStackedWidget"))

        #--------------------------------------------------------------------------------
        # Ligne d'information et controle de la StackedWidget
        #--------------------------------------------------------------------------------       
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        
        # Texte d'information a cote des fleches
        self.infoLabel = QtGui.QLabel(self)
        self.infoLabel.setObjectName(_fromUtf8("infoLabel"))
        
        # Fleche gauche
        self.leftToolButton = QtGui.QToolButton(self)
        self.leftToolButton.setMinimumSize(QtCore.QSize(16, 16))
        self.leftToolButton.setMaximumSize(QtCore.QSize(16, 16))
        self.leftToolButton.setText(_fromUtf8(""))
        self.leftToolButton.setArrowType(QtCore.Qt.LeftArrow)
        self.leftToolButton.setObjectName(_fromUtf8("leftToolButton"))
        
        # Fleche droite
        self.rightToolButton = QtGui.QToolButton(self)
        self.rightToolButton.setMinimumSize(QtCore.QSize(16, 16))
        self.rightToolButton.setMaximumSize(QtCore.QSize(16, 16))
        self.rightToolButton.setText(_fromUtf8(""))
        self.rightToolButton.setArrowType(QtCore.Qt.RightArrow)
        self.rightToolButton.setObjectName(_fromUtf8("rightToolButton"))
        
        # Layout        
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.horizontalLayout.addItem(spacerItem)
        self.horizontalLayout.addWidget(self.infoLabel)
        self.horizontalLayout.addWidget(self.leftToolButton)
        self.horizontalLayout.addWidget(self.rightToolButton)
        
        #--------------------------------------------------------------------------------
        # Le StackedWidget lui meme
        #--------------------------------------------------------------------------------
        self.stackedWidget = QtGui.QStackedWidget(self)
        self.stackedWidget.setFrameShape(QtGui.QFrame.StyledPanel)
        self.stackedWidget.setFrameShadow(QtGui.QFrame.Plain)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        
        # Ne contient pas de page par defaut

        #--------------------------------------------------------------------------------
        # Layout generale
        #--------------------------------------------------------------------------------        
        #self.gridLayout = QtGui.QGridLayout(self)
        #self.gridLayout.setObjectName(_fromUtf8("gridLayout"))        
        #self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        #self.gridLayout.addWidget(self.stackedWidget, 1, 0, 1, 1)
        self.vLayout = QtGui.QVBoxLayout(self)
        self.vLayout.addLayout(self.horizontalLayout)
        self.vLayout.addWidget(self.stackedWidget)
        
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)

    def addWidget( self, w ):
        index = self.stackedWidget.addWidget( w )
        self.widgetAdded.emit(index)
        return index

    def clear(self):
        for i in range(self.count(),0 , -1):
            self.removeWidget( self.widget(i-1) )

    def count( self ):
        return self.stackedWidget.count()
    
    def currentIndex( self ):
        return self.stackedWidget.currentIndex()

    def currentWidget(self):
        return self.stackedWidget.currentWidget()

    #def event(self, e):
        #return self.stackedWidget.event(e)

    def indexOf(self, w):
        return self.stackedWidget.indexOf(w)

    def insertWidget(self, index, w):
        index = self.stackedWidget.insertWidget(index,w)
        self.widgetInserted.emit(index)
        return index

    def removeWidget(self, w):
        self.stackedWidget.removeWidget(w)
        del w

    def setCurrentIndex(self, index):
        self.stackedWidget.setCurrentIndex(index)

    def setCurrentWidget(self, w):
        self.stackedWidget.setCurrentWidget(w)

    def widget(self, i):
        return self.stackedWidget.widget(i)

    def initValues( self
                   ):
        """
        """
        pass

    def updateInfoLabel(self, index):
        try:
            self.infoLabel.setText( self.stackedWidget.widget(index).objectName() + " | Page %s/%s" % (index+1,self.count()) )
        except:
            pass

    def checkInfoLabel(self):
        try:
            index = self.stackedWidget.currentIndex()
            self.infoLabel.setText( self.stackedWidget.currentWidget().objectName() + " | Page %s/%s" % (index+1, self.count()) )
        except:
            pass
    
    def initConnection( self ):
        """
        """
        # Reception des signaux du QStackWidget
        self.stackedWidget.currentChanged.connect( self.currentChangedSlot )
        self.stackedWidget.widgetRemoved.connect( self.widgetRemovedSlot )
        
        # Verication des boutons a activer si changement d'etat
        self.stackedWidget.currentChanged.connect( self.checkNavButton )
        self.stackedWidget.widgetRemoved.connect( self.checkNavButton )
        self.widgetAdded.connect( self.checkNavButton )
        self.widgetInserted.connect( self.checkNavButton )
        
        self.stackedWidget.currentChanged.connect( self.updateInfoLabelSlot )
        self.stackedWidget.widgetRemoved.connect( self.checkInfoLabelSlot )
        self.widgetAdded.connect( self.checkInfoLabelSlot )
        self.widgetInserted.connect( self.checkInfoLabelSlot )

        self.rightToolButton.clicked.connect( self.goToNextPageSlot )
        self.leftToolButton.clicked.connect( self.goToPreviousPageSlot )

#-----------------------------------------------------------------------------------------------------------------------------
#
# PYQT SLOTS
#
#-----------------------------------------------------------------------------------------------------------------------------
                
    @QtCore.pyqtSlot('int')
    def currentChangedSlot( self, index ):
        self.currentChanged.emit(index)

    @QtCore.pyqtSlot('int')
    def widgetRemovedSlot( self, index ):
        self.widgetRemoved.emit(index)

    @QtCore.pyqtSlot()
    def checkNavButton( self ):
        """
        """
        if self.currentIndex() >= self.count() - 1:
            self.rightToolButton.setEnabled(False)
        else:
            self.rightToolButton.setEnabled(True)

        if self.currentIndex() <= 0:
            self.leftToolButton.setEnabled(False)
        else:
            self.leftToolButton.setEnabled(True)
 
    @QtCore.pyqtSlot()
    def goToNextPageSlot(self):
        if self.currentIndex() <= self.count() - 1:
            self.setCurrentIndex( self.stackedWidget.currentIndex() + 1 )

    @QtCore.pyqtSlot()
    def goToPreviousPageSlot(self):
        if self.currentIndex() > 0:
            self.setCurrentIndex( self.stackedWidget.currentIndex() - 1 )

    @QtCore.pyqtSlot('int')
    def updateInfoLabelSlot(self, index):
        self.updateInfoLabel(index)

    @QtCore.pyqtSlot('int')
    def checkInfoLabelSlot(self, index):
        self.checkInfoLabel() 

class QArkControlledStackedWidgetControllerTest(QtGui.QWidget):

    def __init__(self, parent):
        super(self.__class__, self).__init__(parent)
        self.initUi()
        self.initConnection()

    def initUi(self):
        self.o_layout = QtGui.QVBoxLayout(self)
        self.o_widget = QArkControlledStackedWidget(self)
        self.o_layout.addWidget(self.o_widget)

        self.o_addButton = QtGui.QPushButton('addWidget')
        self.o_layout.addWidget(self.o_addButton)

        self.o_removeButton = QtGui.QPushButton('removeWidget')
        self.o_layout.addWidget(self.o_removeButton)

    def initConnection(self):
        self.o_addButton.clicked.connect(self.addButton)
        self.o_removeButton.clicked.connect(self.removeButton)

    def addButton(self):
        o_w = QtGui.QLabel()
        o_w.setText('widget {}'.format(self.o_widget.count()))
        self.o_widget.addWidget( o_w )

    def removeButton(self):
        self.o_widget.removeWidget(self.o_widget.currentWidget())

class QArkControlledStackedWidgetTest( unittest.TestCase ):
    """
    Test
    """

    def test_widget(self):
        o_app = QtGui.QApplication( sys.argv )
        o_mainWindow = QtGui.QDialog()
        o_layout = QtGui.QVBoxLayout(o_mainWindow)
        o_widget = QArkControlledStackedWidgetControllerTest(parent=o_mainWindow)
        o_layout.addWidget(o_widget)    
        o_mainWindow.setLayout(o_layout)
        o_mainWindow.setWindowTitle( 'QArkControlledStackedWidgetTest.test_widget' )    
        o_mainWindow.show()
        o_app.exec_()

if __name__ == '__main__':
    unittest.main()