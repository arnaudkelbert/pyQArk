# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#
#
# QArkUiLoader
#
#
# @author : Arnaud Kelbert
# @date : 2017/09/26
# @version : 0.1
#-----------------------------------------------------------------------
from __future__ import (absolute_import, division, print_function, unicode_literals)

import inspect
import os
from PyQt4 import uic

def loadUiType(**kwargs):
    """
    Load Ui for calling module
    Inspect the stack to retrieve the calling module and constructs its ui name by replacing .py with .ui
    @see uic.loadUiType
    """
    return uic.loadUiType( os.path.abspath(inspect.stack()[1][1]).replace('.py','.ui'), **kwargs )
