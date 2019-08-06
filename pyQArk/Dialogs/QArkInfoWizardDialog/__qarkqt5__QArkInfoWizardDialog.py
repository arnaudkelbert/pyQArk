# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#
#
# QArkInfoWizardDialog
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

from PyQt5 import QtWidgets

from pyQArk.Core import QArkDomXml
from pyQArk.Dialogs.QArkInfoWizardDialog.QArkInfoWizardWelcomePage import QArkInfoWizardWelcomePage
from pyQArk.Dialogs.QArkInfoWizardDialog.QArkInfoWizardPage import QArkInfoWizardPage
from pyQArk.QArkDialog import QArkDialog

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
