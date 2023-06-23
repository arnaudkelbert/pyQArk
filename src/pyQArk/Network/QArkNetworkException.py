# -*- coding: utf-8 -*-
from pyQArk.Core.QArkException import QArkException

class QArkHTTPResponseStatusCodeError(QArkException):
    def __init__( self, *message ):
        super( self.__class__, self ).__init__( T_ERROR_MESSAGES[self.__class__].format(*message) )

T_ERROR_MESSAGES = {
 QArkHTTPResponseStatusCodeError : 'HTTP Status Code Error {}\n{}'
}
