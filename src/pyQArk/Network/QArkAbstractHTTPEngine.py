# -*- coding: utf-8 -*-
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