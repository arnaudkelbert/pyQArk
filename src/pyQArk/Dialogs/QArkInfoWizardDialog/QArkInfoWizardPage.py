# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from pyQArk.Core import QArkDomXml

class QArkInfoWizardPage( QtWidgets.QWizardPage ):
    """
    A wizard page to show an information message
    """
    def __init__( self
                 , parent = None
                 , _s_title = ''
                 , _s_subtitle = ''
                 , _s_text = ''
                 , _s_image=None
                 ):
        """Constructor"""
        super( QArkInfoWizardPage, self ).__init__(parent)
        self.s_title = _s_title
        self.s_subtitle = _s_subtitle
        self.s_text = _s_text
        self.s_image = _s_image
        self.initUi()

    def initUi(self):
        self.setTitle( self.s_title )
        self.setSubTitle( self.s_subtitle )

        if not self.s_image is None:
            o_image = QtGui.QImage( str(self.s_image) )
            o_pixmap = QtGui.QPixmap.fromImage(o_image)
            self.setPixmap( QtWidgets.QWizard.WatermarkPixmap, o_pixmap )

        if not self.s_text is None:
            o_layout = QtWidgets.QVBoxLayout(self)
            o_textLabel = QtWidgets.QLabel( self.s_text )
            o_textLabel.setWordWrap(True)
            o_textLabel.setAlignment( QtCore.Qt.AlignJustify )
            o_layout.addWidget( o_textLabel )
            self.setLayout(o_layout)

    @classmethod
    def createFromNode( cls, parent, _o_node ):
        """
        Instanciate a class object from a XML node
        @param _o_node : XML DOM Node
        @type _o_node : L{Node}
        """
        s_title = QArkDomXml.getNodeValue( _o_node, 'Title' )
        s_subtitle = QArkDomXml.getNodeValue( _o_node, 'Subtitle' )
        s_text = QArkDomXml.getNodeInnerContent( QArkDomXml.getNode(_o_node, 'Text' ) )
        s_image = QArkDomXml.getNodeValue( _o_node, 'Image' )

        return QArkInfoWizardPage( parent = parent
                              ,_s_title = s_title
                              ,_s_subtitle = s_subtitle
                              ,_s_text = s_text
                              ,_s_image = s_image
                              )