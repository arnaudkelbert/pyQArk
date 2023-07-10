# -*- coding: utf-8 -*-
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