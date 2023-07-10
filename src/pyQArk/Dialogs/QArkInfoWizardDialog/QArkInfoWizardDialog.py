# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
from pyQArk.Core import QArkDomXml
from pyQArk.Dialogs.QArkInfoWizardDialog.QArkInfoWizardWelcomePage import QArkInfoWizardWelcomePage
from pyQArk.Dialogs.QArkInfoWizardDialog.QArkInfoWizardPage import QArkInfoWizardPage
from pyQArk.Dialogs.QArkDialog import QArkDialog

class QArkInfoWizardDialog( QtWidgets.QWizard ):
    """
    A wizard info dialog to show tips at start-up.
    The informations to show is described in a XML file. (see template.xml)
    """
    MODE_XML_FILE, MODE_XML_STRING = range(2)

    def __init__( self
                 , parent
                 , _s_xml
                 , _u_mode
                 , _s_encoding = 'utf-8'
                 ):

        """Constructeur"""
        super( QArkInfoWizardDialog, self ).__init__(parent)
        self.__parseXml( _s_xml, _u_mode, _s_encoding )
        self.setWizardStyle(QtWidgets.QWizard.ModernStyle)

    def __parseXml( self, _s_xml, _u_mode, _s_encoding ):
        if _u_mode is self.__class__.MODE_XML_FILE:
            o_rootNode, _ = QArkDomXml.getRootNode( _s_xml, 'InfoWizard', _s_encoding )
        else:
            o_rootNode, _ = QArkDomXml.getRootNodeFromString( _s_xml, 'InfoWizard', _s_encoding )

        o_welcomeNode = QArkDomXml.getNode(o_rootNode, 'IntroPage')
        self.addPage( QArkInfoWizardWelcomePage.createFromNode(self, o_welcomeNode) )

        for o_node in QArkDomXml.getChildrenElementNodes( QArkDomXml.getNode( o_rootNode, 'ListOfPages' ), 'Page' ):
            self.addPage( QArkInfoWizardPage.createFromNode(self, o_node) )

    def exec_(self, _b_centered=True, **kwargs):
        # Reimplemented to get it centered
        if _b_centered:
            QArkDialog.centerDialog( self, **kwargs )
        QtWidgets.QWizard.exec_(self)
