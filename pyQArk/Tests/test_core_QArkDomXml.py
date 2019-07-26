# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------
# @author : Arnaud Kelbert
# @date : 2019/03/19
# @version : 0.2
#
# Historic:
# 0.1 : init version
# 0.2 : add python 2/3 compatibility
# -----------------------------------------------------------------------
# {-- Pyhton 2/3 compatibility ------------------------------------------
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
# }-- Pyhton 2/3 compatibility ------------------------------------------
import unittest
from pyQArk.QArkConfig import QARK_QT_GENERATION

if QARK_QT_GENERATION == 4:
    from PyQt4 import QtGui
    QtWidgets=QtGui
elif QARK_QT_GENERATION == 5:
    from PyQt5 import QtWidgets

from pyQArk.Core import QArkDomXml

class QArkDomXmlTest(unittest.TestCase):
    """
    Test
    """
    def test_widget(self):
        s='<root><elt>0</elt><elt>1</elt></root>'
        print(QArkDomXml.toPrettyXmlString(s))

if __name__ == '__main__':
    unittest.main()