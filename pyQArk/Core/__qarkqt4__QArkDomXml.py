# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#
#
# QArkDomXML
#
#
# @author : Arnaud Kelbert
# @date : 2019/07/26
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
import xml.dom.minidom
from xml.dom import Node
from xml.etree import ElementTree

from PyQt4 import QtXml

def getRootNode( _s_file, _s_rootTag, _s_encoding='UTF-8' ):
    with open(_s_file,'r') as fp:
        return getRootNodeFromString( fp.read(), _s_rootTag, _s_encoding )

def getRootNodeFromString( _s_str, _s_rootTag, _s_encoding='UTF-8' ):
    """
    Return root DOM Node from _s_string
    """
    if not _s_encoding is None:
        _s_str = _s_str.decode(_s_encoding)
    s_str = ((_s_str.replace(u'\n','')).replace(u'\t','')).replace('    ','').replace('   ','').replace('  ','').replace(u'> <',u'><')
    o_doc = xml.dom.minidom.parseString( s_str.encode('UTF-8') )
    if not _s_rootTag is None:
        o_rootNode = getNode(o_doc,_s_rootTag)
    else:
        o_rootNode = o_doc
    return o_rootNode, o_doc

def getNode( _o_parent, _s_tag ):
    for o_currentNode in getChildrenElementNodes(_o_parent):
        if o_currentNode.tagName == _s_tag:
            return o_currentNode
    return None

def getNodeValue( _o_node, _s_tag=None ):
    try:
        if not _s_tag is None:
            return getNode(_o_node, _s_tag).childNodes[0].nodeValue
        else:
            return _o_node.childNodes[0].nodeValue
    except:
        return None

def getNodeInnerContent( _o_node ):
    try:
        o_et = ElementTree.fromstring( _o_node.toxml('utf-8') )
        return o_et.text + ''.join( [ElementTree.tostring(o_child) for o_child in o_et] )
    except Exception as e:
        raise e

def getChildrenElementNodes( _o_parent, _s_tag=None ):
    if _s_tag is None:
        return [ o_node for o_node in _o_parent.childNodes if o_node.nodeType is Node.ELEMENT_NODE ]
    else:
        return [ o_node for o_node in _o_parent.childNodes if o_node.nodeType is Node.ELEMENT_NODE and o_node.tagName == _s_tag ]

def toPrettyXmlString( _s_in ):
    o_doc = QtXml.QDomDocument()
    o_doc.setContent( _s_in )
    return str( o_doc.toString(4) )
