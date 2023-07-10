# -*- coding: utf-8 -*-
class QArkHTTPProxy(object):
    """
    Class QArkHTTPProxy
    Definition of a HTTP User
    """

    def __init__(self, _s_username, _s_pwd, _s_url, _u_port):
        """
        Constructor

        Args:
            _s_username (:obj:str): username
            _s_pwd (:obj:pwd): user password
            _s_url (:obj:pwd): proxy address
            _u_port (int): proxy port
        """
        self.s_username = _s_username
        self.s_pwd = _s_pwd
        self.s_url = _s_url
        self.u_port = _u_port