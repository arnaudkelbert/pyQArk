# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#
#
# QArkRequestHTTPEngine
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
import requests

from pyQArk.Network.QArkAbstractHTTPResponse import QArkAbstractHTTPResponse
from pyQArk.Network.QArkNetworkException import QArkHTTPResponseStatusCodeError

#https://www.codementor.io/aviaryan/downloading-files-from-urls-in-python-77q3bs0un
class QArkRequestsHTTPResponse(QArkAbstractHTTPResponse):

    def init(self, _b_stream=False):
        self.headers = self.x_response.headers
        if not _b_stream:
            self.text = self.x_response.text

    def contentType(self):
        return self.headers['content-type']

    def contentLength(self):
        return self.headers['content-length']

    def checkStatus(self):
        if self.x_response.status_code == requests.codes.ok:
            return True
        else:
            raise QArkHTTPResponseStatusCodeError(self.x_response.status_code,'')