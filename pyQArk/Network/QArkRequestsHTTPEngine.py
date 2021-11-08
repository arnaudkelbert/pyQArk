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
import unittest
import functools
import requests
import shutil

from pyQArk import QArkConfig

if QArkConfig.QARK_QT_GENERATION == 4:
    from PyQt4 import QtCore
elif QArkConfig.QARK_QT_GENERATION == 5:
    from PyQt5 import QtCore

from pyQArk.Network.QArkAbstractHTTPEngine import QArkAbstractHTTPEngine
from pyQArk.Network.QArkRequestsHTTPResponse import QArkRequestsHTTPResponse

#https://www.codementor.io/aviaryan/downloading-files-from-urls-in-python-77q3bs0un

class QArkRequestsHTTPEngine(QArkAbstractHTTPEngine):
    """

    HTTP Engine using requests python package

    """
    class _WithSession(object):
        """
        Inner class to use as a decorator for requests.session management
        """

        def __init__(self, func):
            self._func = func
            functools.update_wrapper(self, func)

        def __call__(self, obj, *args, **kwargs):
            """
            Decorator definition:
            Encapsulates the wrapped method in a requests.Session context
            This decorator set the o_session class attribute

            Args:
                obj: the current object
                *args: method argument list
                **kwargs: method argument dictionnary

            Returns:
                The returned value of wrapped method
            """
            try:
                _b_auth = kwargs['_b_auth']
            except KeyError:
                _b_auth = False
            with requests.Session() as obj.o_session:
                if _b_auth and not obj.o_httpUser is None:
                    obj.o_session.auth = (obj.o_httpUser.s_username, obj.o_httpUser.s_pwd)
                x_ret = self._func(obj, *args, **kwargs)
                obj.o_session = None
            return x_ret

        def __get__(self, obj, objtype):
            return functools.partial(self.__call__, obj)

    def __init__(self, *args, **kwargs):
        """
        Constructor

        Args:
            *args : list of arguments
            **kwargs : dictionnary of arguments
        """
        super(QArkRequestsHTTPEngine, self).__init__(*args, **kwargs)
        self.t_callkwargs = {}
        if not self.o_proxy is None:
            self.t_proxies = {k:'http://{0}:{1}@{2}:{3}'.format(self.o_proxy.s_username
                                                                 ,self.o_proxy.s_pwd
                                                                 ,self.o_proxy.s_url
                                                                 ,self.o_proxy.u_port
                                                                 )
                              for k in ('http', 'https', 'ftp')
                              }
            self.t_callkwargs['proxies'] = self.t_proxies
        if not self.s_cert is None:
            self.t_callkwargs['verify'] = self.s_cert

    @_WithSession
    def get(self, _s_url, _b_auth=False, **kwargs):
        """
        Establish a HTTP connexion to _s_url and retrieve the HTTP response

        Args:
            _s_url (:obj:str): url address
            _b_auth (bool): use HTTP authentification
            **kwargs : dictionnary of arguments (used for requests.get call)

        Returns:
            (str): the HTTP response
        """
        kwargs.update(self.t_callkwargs)
        o_response = self.o_session.get( _s_url, **kwargs)
        return QArkRequestsHTTPResponse(o_response)

    @_WithSession
    def isDownloadable(self, _s_url, _b_auth=False, **kwargs):
        """
        Check if url contains a downloadable content.
        The test is based on content-type header value.

        Args:
            _s_url (:obj:str): url address
            _b_auth (bool): use HTTP authentification
            **kwargs : dictionnary of arguments (used for requests.head call)

        Returns:
            (bool): True if url contains a downloadable content, False otherwise.
        """
        o_response = self.o_session.head(_s_url, **kwargs)
        if 'text' in o_response.headers['content-type'].lower():
            return False
        if 'html' in o_response.headers['content-type'].lower():
            return False
        return True

    @_WithSession
    def download(self, _s_url, _s_out, _b_auth=False, _b_stream=True, **kwargs):
        """
        Download a remote file from _s_url and saving it to given file

        Args:
            _s_url (:obj:str): url address
            _b_auth (bool): use HTTP authentification
            **kwargs : dictionnary of arguments

        Returns:
            (str): the output file
        """
        b_useRaw = True
        if _b_stream:
            kwargs.update(self.t_callkwargs)
            with self.o_session.get(_s_url, stream=True, **kwargs) as o_response:
                if QArkRequestsHTTPResponse(o_response, _b_stream=True).checkStatus():
                    if b_useRaw:
                        with open(_s_out, 'wb') as fp:
                            o_response.raw.decode_content = True
                            shutil.copyfileobj(o_response.raw, fp)
                    else:
                        try:
                            u_chunkSize = kwargs['_u_chunkSize']
                        except KeyError:
                            u_chunkSize = 1024
                        with open(_s_out, 'wb') as fp:
                            for chunk in o_response.iter_content(chunk_size=u_chunkSize):
                                fp.write(chunk)
                    return _s_out
        else:
            raise NotImplemented
            return None

class QArkRequestHTTPEngineTest( unittest.TestCase ):
    """
    Test
    """
    def test_widget(self):
        s_url = 'https://en.wikipedia.org/wiki/Monty_Python'
        o_engine = QArkRequestsHTTPEngine()
        o_response = o_engine.get(s_url)

        s_url = 'http://google.com/favicon.ico'
        o_engine.download(s_url, './favicon.ico')
        #print(o_response)

        #r = requests.session()
        #r= requests.get('http://google.com/favicon.ico', stream=True)
        #r = requests.session().get('http://google.com/favicon.ico', stream=True)
        #print(r.raw.read())

if __name__ == '__main__':
    unittest.main()