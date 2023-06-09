# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#
#
# QArkAbstractHTTPEngine
#
#
# @author : Arnaud Kelbert
# @date : 2019/03/16
# @version : 0.2
#
# Historic:
# 0.2 : init version
#-----------------------------------------------------------------------
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

from pyQArk import QArkConfig

if QArkConfig.QARK_QT_GENERATION == 4:
    from PyQt4 import QtCore
elif QArkConfig.QARK_QT_GENERATION == 5:
    from PyQt5 import QtCore

#class QArkAbstractHTTPEngine(QtCore.QObject):
class QArkAbstractHTTPEngine(object):
    def __init__(self
                 ,_o_httpUser = None
                 ,_o_proxy = None
                 ,_s_cert = None
                 ):
        """
        Constructor

        Args:
            _o_httpUser (:obj:QArkHTTPUser): HTTP User defined as a QArkHTTPUser object
            _o_proxy (:obj:QArkHTTPProxy): Proxy defined as a QArkHTTPProxy object
            _s_cert (:obj:str): Certificate (to be implemented / not yet available)
        """
        super(QArkAbstractHTTPEngine, self).__init__()
        self.o_httpUser = _o_httpUser
        self.o_proxy = _o_proxy
        self.s_cert = _s_cert

    def close(self):
        try:
            self.o_session.close()
        except:
            pass

    def __exit__(self):
        self.close()

    def get(self, _s_url, _b_auth=False):
        """
        Establish a HTTP connexion to _s_url and retrieve the HTTP response

        Args:
            _s_url (:obj:str): url address
            _b_auth (bool): use HTTP authentification

        Returns:
            (str): the HTTP response
        """
        raise NotImplemented

    def download(self, _s_url, _s_out, _b_auth=False):
        """
        Download a remote file from _s_url and saving it to given file

        Args:
            _s_url (:obj:str): url address
            _b_auth (bool): use HTTP authentification

        Returns:
            (str): the HTTP response
        """
        raise NotImplemented