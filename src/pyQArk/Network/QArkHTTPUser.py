# -*- coding: utf-8 -*-

class QArkHTTPUser(object):
    """
    Class QArkHTTPUser
    Definition of a HTTP User
    """

    def __init__(self, _s_username, _s_pwd):
        """
        Constructor

        Args:
            _s_username (:obj:str): username
            _s_pwd (:obj:pwd): user password
        """
        self.s_username = _s_username
        self.s_pwd = _s_pwd
    