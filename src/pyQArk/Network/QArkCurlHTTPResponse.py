# -*- coding: utf-8 -*-
try:
    import pycurl
except ImportError:
    print('Warning : pyCurl package not available')

from pyQArk.Network.QArkAbstractHTTPResponse import QArkAbstractHTTPResponse
from pyQArk.Network.QArkNetworkException import QArkHTTPResponseStatusCodeError

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
