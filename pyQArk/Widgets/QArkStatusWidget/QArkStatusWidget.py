# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#
#
# QArkStatusWidget
#
#
# @author : Arnaud Kelbert
# @date : 2014/08/01
# @version : 0.1
#-----------------------------------------------------------------------
from PyQt4 import QtCore, QtGui

from .Ui_QArkStatusWidget import Ui_QArkStatusWidget


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




class QArkStatusWidget( QtGui.QWidget ):
    """
    """
    def __init__( self
                 , parent=None
                 ):
        super( QArkStatusWidget, self).__init__( parent )

        self.initUi()



    def initUi( self ):
        """
        @brief init user interface
        """
        self.ui = Ui_QArkStatusWidget()
        self.ui.setupUi(self)

        self.setObjectName( _fromUtf8("qArkStatusWidget") )
        self.setAttribute( QtCore.Qt.WA_DeleteOnClose )

        self.setProgressBarValue(0)
        self.setProgressLabel('')
        self.setMessageLabel('')



    def enableMessageStatus( self, _b_enable = True ):
        self.ui.statusLabel.setVisible( _b_enable )
        self.ui.statusLabel.setEnabled( _b_enable )


    def enableProgressStatus( self, _b_enable = True ):
        self.ui.progressLabel.setVisible( _b_enable )
        self.ui.progressLabel.setEnabled( _b_enable )
        self.ui.progressBar.setVisible( _b_enable )
        self.ui.progressBar.setEnabled( _b_enable )


    def setProgressLabel( self, _s_text ):
        self.ui.progressLabel.setText( _s_text )


    def setProgressBarValue( self, _u_progress ):
        self.ui.progressBar.setValue( _u_progress )


    def setMessageLabel( self, _s_text ):
        self.ui.statusLabel.setText( _s_text )


    def switchToProgress( self, _b_reset = True, _s_label = 'Progress...' ):
        self.enableProgressStatus(True)
        self.enableMessageStatus(False)

        if _b_reset:
            self.setProgressLabel( _s_label )
            self.setProgressBarValue( 0 )

    def switchToMessage( self ):
        self.enableProgressStatus(False)
        self.enableMessageStatus(True)


    def isMessageEnabled(self):
        return self.ui.statusLabel.isEnabled()

    def isProgressEnabled(self):
        return self.ui.progressBar.isEnabled()



    @QtCore.pyqtSlot(object)
    def setMessageSlot( self, _s_message ):

        if not self.isMessageEnabled():
            self.switchToMessage()

        self.setMessageLabel( _s_message )


    @QtCore.pyqtSlot(int)
    def setProgressValueSlot( self, _u_progress ):

        if not self.isProgressEnabled():
            self.switchToProgress()

        self.setProgressBarValue( _u_progress )


    @QtCore.pyqtSlot(object)
    def setProgressLabelSlot( self, _s_message ):

        if not self.isProgressEnabled():
            self.switchToProgress()

        self.setProgressLabel( _s_message )



    @QtCore.pyqtSlot()
    def handleSwitchToMessageRequest( self ):
        self.switchToMessage()


    @QtCore.pyqtSlot(object)
    def handleSwitchToProgressRequest( self, _s_label ):
        self.switchToProgress(_b_reset = True, _s_label = _s_label)


    #@QtCore.pyqtSlot(object)
    #def handleSlidersValueChangedSlot( self, _u_value ):
        #o_newColor = QtGui.QColor( self.ui.redSlider.getValue()
                                  #,self.ui.greenSlider.getValue()
                                  #,self.ui.blueSlider.getValue()
                                  #)

        #if o_newColor != self.ui.colorLabel.getFillColor():
            #self.ui.colorLabel.setFillColor( o_newColor )



    #@QtCore.pyqtSlot()
    #def handleColorLabelClickedSlot( self ):
        #o_colorDialog = QtGui.QColorDialog( self )
        #o_colorDialog.setCurrentColor( self.ui.colorLabel.getFillColor() )

        #o_newColor = o_colorDialog.getColor()

        #if o_newColor != self.ui.colorLabel.getFillColor():
            #self.ui.colorLabel.setFillColor( o_newColor )






