# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#
#
# QArkCurlHTTPEngine
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
try:
    from io import BytesIO
except ImportError:
    from StringIO import StringIO as BytesIO
# }-- Pyhton 2/3 compatibility ------------------------------------------
try:
    import pycurl
except ImportError:
    print('Warning : pyCurl package not available')

from .QArkAbstractHTTPResponse import QArkAbstractHTTPResponse
from .QArkNetworkException import QArkHTTPResponseStatusCodeError

# TODO
class QArkCurlHTTPResponse(QArkAbstractHTTPResponse):

    def init(self, _b_stream=False):
        self.headers =  None
        self.text = None

    def contentType(self):
        return self.headers['content-type']

    def contentLength(self):
        return self.headers['content-length']

    def checkStatus(self):
        if self.x_response.status_code == requests.codes.ok:
            return True
        else:
            raise QArkHTTPResponseStatusCodeError(self.x_response.status_code,'')




#
# def transfer(ipaddr, username, password, commandfile, trackprogress):
#     #transfers commandfile to camera
#     storage = StringIO()
#     c = pycurl.Curl()
#     c.setopt(c.URL, 'http://' + ipaddr + '/admin/remoteconfig')
#     c.setopt(c.POST, 1)
#     c.setopt(c.CONNECTTIMEOUT, 5)
#     c.setopt(c.TIMEOUT, TIMEOUT)
#     filesize = os.path.getsize(commandfile)
#     f = open(commandfile, 'rb')
#     c.setopt(c.FAILONERROR, True)
#     c.setopt(pycurl.POSTFIELDSIZE, filesize)
#     c.setopt(pycurl.READFUNCTION, FileReader(f).read_callback)
#     if trackprogress:
#         c.setopt(pycurl.NOPROGRESS, 0)
#         c.setopt(pycurl.PROGRESSFUNCTION, progresscallback)
#         starttime = time.time()
#     else:
#         c.setopt(pycurl.NOPROGRESS, 1)
#     c.setopt(c.WRITEFUNCTION, storage.write)
#     c.setopt(pycurl.HTTPHEADER, ["application/x-www-form-urlencoded"])
#     c.setopt(c.VERBOSE, VERBOSE)
#     c.setopt(pycurl.HTTPAUTH, pycurl.HTTPAUTH_BASIC)
#     c.setopt(pycurl.USERPWD, username + ':' + password)
#     try:
#         c.perform()
#     except pycurl.error, error:
#         errno, errstr = error
#         print 'An error occurred: ', errstr
#         return False, ''
#     c.close()
#     content = storage.getvalue()
#     f.close()
#     return True, content
#
# Example 3
# Project: Mobotix-tools   Author: keptenkurk   File: mxpgm.py    (license) View Source Project 	5 votes 	vote down vote up
#
# def transfer(ipaddr, username, password, commandfile):
#     #transfers commandfile to camera
#     storage = StringIO()
#     c = pycurl.Curl()
#     c.setopt(c.URL, 'http://' + ipaddr + '/admin/remoteconfig')
#     c.setopt(c.POST, 1)
#     c.setopt(c.CONNECTTIMEOUT, 5)
#     c.setopt(c.TIMEOUT, 60)
#     filesize = os.path.getsize(commandfile)
#     f = open(commandfile, 'rb')
#     c.setopt(c.FAILONERROR, True)
#     c.setopt(pycurl.POSTFIELDSIZE, filesize)
#     c.setopt(pycurl.READFUNCTION, FileReader(f).read_callback)
#     c.setopt(c.WRITEFUNCTION, storage.write)
#     c.setopt(pycurl.HTTPHEADER, ["application/x-www-form-urlencoded"])
#     c.setopt(c.VERBOSE, 0)
#     c.setopt(pycurl.HTTPAUTH, pycurl.HTTPAUTH_BASIC)
#     c.setopt(pycurl.USERPWD, username + ':' + password)
#     try:
#         c.perform()
#     except pycurl.error, error:
#         errno, errstr = error
#         print 'An error occurred: ', errstr
#         return False, ''
#     c.close()
#     content = storage.getvalue()
#     f.close()
#     return True, content
