# -*- coding: utf-8 -*-
import os
import inspect
LOCAL_PATH = os.path.abspath(os.path.join( inspect.getfile(inspect.currentframe()), '..' ))
def PKGPATH(_s_file): return os.path.normpath(os.path.join(LOCAL_PATH, _s_file))