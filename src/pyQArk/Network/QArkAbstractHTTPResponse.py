# -*- coding: utf-8 -*-
class QArkAbstractHTTPResponse(object):
    def __init__(self, _x_response, **kwargs):
        """
        Constructor

        Args:
            _x_response (:obj:object): a response object
        """
        self.x_response = _x_response
        self.init(**kwargs)

    def __str__(self):
        return self.text

    def __repr__(self):
        return str(self)

    def init(self, **kwargs):
        self.text = None
        self.headers = None

    def checkStatus(self):
        raise NotImplemented