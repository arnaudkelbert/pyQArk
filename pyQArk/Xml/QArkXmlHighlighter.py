# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#
#
# QArkXmlHighlighter
#
#
# @author : Arnaud Kelbert
# @date : 2019/03/05
# @version : 0.2
#
# Historic:
# 0.1 : init version
# 0.2 : add python 2/3 compatibility
#
# src : http://www.yasinuludag.com/blog/?p=49
#
# Usage:
# o_textEdit = QtGui.QTextEdit()
# o_xmlHighlighter = QArkXmlHighlighter( o_textEdit.document() )
# o_textEdit.setPlainText( 'XML string here !' )
#
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
from pyQArk import QArkConfig
if QArkConfig.QARK_QT_GENERATION == 4:
    from PyQt4 import QtCore, QtGui
    QtWidgets = QtGui
elif QArkConfig.QARK_QT_GENERATION == 5:
    from PyQt5 import QtCore, QtGui

class QArkXmlHighlighter(QtGui.QSyntaxHighlighter):

    #INIT THE STUFF
    def __init__(self, parent=None):
        super(QArkXmlHighlighter, self).__init__(parent)
        keywordFormat = QtGui.QTextCharFormat()
        keywordFormat.setForeground(QtCore.Qt.darkMagenta)
        keywordFormat.setFontWeight(QtGui.QFont.Bold)
        keywordPatterns = ["\\b?xml\\b", "/>", ">", "<"]
        self.highlightingRules = [(QtCore.QRegExp(pattern), keywordFormat)
                for pattern in keywordPatterns]
        xmlElementFormat = QtGui.QTextCharFormat()
        xmlElementFormat.setFontWeight(QtGui.QFont.Normal)
        xmlElementFormat.setForeground(QtCore.Qt.darkMagenta)
        self.highlightingRules.append((QtCore.QRegExp("\\b[A-Za-z0-9_]+(?=[\s/>])"), xmlElementFormat))
        xmlAttributeFormat = QtGui.QTextCharFormat()
        xmlAttributeFormat.setFontItalic(True)
        xmlAttributeFormat.setForeground(QtCore.Qt.darkGreen)
        self.highlightingRules.append((QtCore.QRegExp("\\b[A-Za-z0-9_]+(?=\\=)"), xmlAttributeFormat))
        self.valueFormat = QtGui.QTextCharFormat()
        self.valueFormat.setForeground(QtCore.Qt.red)
        self.valueStartExpression = QtCore.QRegExp("\"")
        self.valueEndExpression = QtCore.QRegExp("\"(?=[\s></])")
        singleLineCommentFormat = QtGui.QTextCharFormat()
        singleLineCommentFormat.setForeground(QtCore.Qt.gray)
        self.highlightingRules.append((QtCore.QRegExp("<!--[^\n]*-->"), singleLineCommentFormat))

    #VIRTUAL FUNCTION WE OVERRIDE THAT DOES ALL THE COLLORING
    def highlightBlock(self, text):
        #for every pattern
        for pattern, format in self.highlightingRules:
            #Create a regular expression from the retrieved pattern
            expression = QtCore.QRegExp(pattern)
            #Check what index that expression occurs at with the ENTIRE text
            index = expression.indexIn(text)
            #While the index is greater than 0
            while index >= 0:
                #Get the length of how long the expression is true, set the format from the start to the length with the text format
                length = expression.matchedLength()
                self.setFormat(index, length, format)
                #Set index to where the expression ends in the text
                index = expression.indexIn(text, index + length)
        #HANDLE QUOTATION MARKS NOW.. WE WANT TO START WITH " AND END WITH ".. A THIRD " SHOULD NOT CAUSE THE WORDS INBETWEEN SECOND AND THIRD TO BE COLORED
        self.setCurrentBlockState(0)
        startIndex = 0
        if self.previousBlockState() != 1:
            startIndex = self.valueStartExpression.indexIn(text)
        while startIndex >= 0:
            endIndex = self.valueEndExpression.indexIn(text, startIndex)
            if endIndex == -1:
                self.setCurrentBlockState(1)
                commentLength = len(text) - startIndex
            else:
                commentLength = endIndex - startIndex + self.valueEndExpression.matchedLength()
            self.setFormat(startIndex, commentLength, self.valueFormat)
            startIndex = self.valueStartExpression.indexIn(text, startIndex + commentLength)
