# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#
#
# QArkInfoWizardGenericPageDialog
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