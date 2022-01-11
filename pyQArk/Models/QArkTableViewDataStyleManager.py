# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#
#
# QArkTableViewDataStyle
#
#
# @author : Arnaud Kelbert
# @date : 2022/01/10
#
#-----------------------------------------------------------------------
#{-- Python 2/3 compatibility ------------------------------------------
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
from pyQArk.QArkConfig import QARK_QT_GENERATION
from pyQArk.Core.QArkCriticityLevel import QArkCriticityLevel
from pyQArk.Models.QArkTableViewDataStyle import QArkTableViewDataStyle, createGradientBrush

if QARK_QT_GENERATION == 4:
    from PyQt4 import QtGui, QtCore
    QtWidgets=QtGui
elif QARK_QT_GENERATION == 5:
    from PyQt5 import QtWidgets, QtCore, QtGui

class QArkTableViewDataStyleManager(object):
    def __init__(self):
        self.t_styles = {}
    def addStyle(self, _x_key, _o_style):
        self.t_styles[_x_key] = _o_style
    def getStyle(self, _x_key):
        return self.t_styles[_x_key]
    def getForegroundRole(self, _x_key):
        o_ret = self.t_styles[_x_key].getForegroundRole()
        if o_ret is None:
            return QtCore.QVariant()
        return o_ret
    def getBackgroundRole(self, _x_key):
        o_ret = self.t_styles[_x_key].getBackgroundRole()
        if o_ret is None:
            return QtCore.QVariant()
        return o_ret
    def getFontRole(self, _x_key):
        o_ret = self.t_styles[_x_key].getFontRole()
        if o_ret is None:
            return QtCore.QVariant()
        return o_ret

O_COLOR_RED001 = QtGui.QColor(165,0,0)
O_COLOR_RED001_c = QtGui.QColor(255,255,255)
O_GRADIENT_RED001 = createGradientBrush(_o_color1=O_COLOR_RED001, _o_color2=QtGui.QColor(215,0,0))

O_COLOR_RED002 = QtGui.QColor(195,0,0)
O_COLOR_RED002_c = QtGui.QColor(255,255,255)
O_GRADIENT_RED002 = createGradientBrush(_o_color1=O_COLOR_RED002, _o_color2=QtGui.QColor(245,0,0))

O_COLOR_RED003 = QtGui.QColor(225,0,0)
O_COLOR_RED003_c = QtGui.QColor(255,255,255)
O_GRADIENT_RED003 = createGradientBrush(_o_color1=O_COLOR_RED003, _o_color2=QtGui.QColor(255,20,20))

O_COLOR_RED004 = QtGui.QColor(255,70,70)
O_COLOR_RED004_c = QtGui.QColor(255,255,255)
O_GRADIENT_RED004 = createGradientBrush(_o_color1=O_COLOR_RED004, _o_color2=QtGui.QColor(255,120,120))

O_COLOR_RED005 = QtGui.QColor(255,130,130)
O_COLOR_RED005_c = QtGui.QColor(255,255,255)
O_GRADIENT_RED005 = createGradientBrush(_o_color1=O_COLOR_RED005, _o_color2=QtGui.QColor(255,180,180))

O_COLOR_ORANGE001 = QtGui.QColor(253,165,20)
O_COLOR_ORANGE001_c = QtGui.QColor(0,20,65)
O_GRADIENT_ORANGE001 = createGradientBrush(_o_color1=O_COLOR_ORANGE001, _o_color2=QtGui.QColor(255,215,100))

O_COLOR_ORANGE002 = QtGui.QColor(255,200,85)
O_COLOR_ORANGE002_c = QtGui.QColor(0,20,65)
O_GRADIENT_ORANGE002 = createGradientBrush(_o_color1=O_COLOR_ORANGE002, _o_color2=QtGui.QColor(255,220,140))

O_COLOR_ORANGE003 = QtGui.QColor(255,220,140)
O_COLOR_ORANGE003_c = QtGui.QColor(0,20,65)
O_GRADIENT_ORANGE003 = createGradientBrush(_o_color1=O_COLOR_ORANGE003, _o_color2=QtGui.QColor(255,235,190))

O_COLOR_YELLOW001 = QtGui.QColor(255,255,157)
O_COLOR_YELLOW001_c = QtGui.QColor(0,20,65)
O_GRADIENT_YELLOW001 = createGradientBrush(_o_color1=O_COLOR_YELLOW001, _o_color2=QtGui.QColor(255,255,200))

O_COLOR_GREEN001 = QtGui.QColor(215,255,155)
O_COLOR_GREEN001_c = QtGui.QColor(15,0,15)
O_GRADIENT_GREEN001 = createGradientBrush(_o_color1=O_COLOR_GREEN001, _o_color2=QtGui.QColor(235,255,205))

O_COLOR_GREEN002 = QtGui.QColor(180,255,180)
O_COLOR_GREEN002_c = QtGui.QColor(15,0,15)
O_GRADIENT_GREEN002 = createGradientBrush(_o_color1=O_COLOR_GREEN002, _o_color2=QtGui.QColor(240,255,240))

O_COLOR_BLUE001 = QtGui.QColor(130,180,255)
O_COLOR_BLUE001_c = QtGui.QColor(15,0,15)
O_GRADIENT_BLUE001 = createGradientBrush(_o_color1=O_COLOR_BLUE001, _o_color2=QtGui.QColor(180,215,255))

O_COLOR_ROSE001 = QtGui.QColor(240,95,235)
O_COLOR_ROSE001_c = QtGui.QColor(0,100,0)
O_GRADIENT_ROSE001 = createGradientBrush(_o_color1=O_COLOR_ROSE001, _o_color2=QtGui.QColor(240,160,235))

O_STYLE_MANAGER = QArkTableViewDataStyleManager()
O_STYLE_MANAGER.addStyle(QArkCriticityLevel.DEFAULT, QArkTableViewDataStyle(_o_background=None, _o_foreground=None, _o_font=None))
O_STYLE_MANAGER.addStyle(QArkCriticityLevel.CATASTROPHIC, QArkTableViewDataStyle(_o_background=O_GRADIENT_RED001, _o_foreground=O_COLOR_RED001_c, _o_font=None))
O_STYLE_MANAGER.addStyle(QArkCriticityLevel.DISASTER, QArkTableViewDataStyle(_o_background=O_GRADIENT_RED002, _o_foreground=O_COLOR_RED002_c, _o_font=None))
O_STYLE_MANAGER.addStyle(QArkCriticityLevel.EXTREMELY_CRITICAL, QArkTableViewDataStyle(_o_background=O_GRADIENT_RED003, _o_foreground=O_COLOR_RED003_c, _o_font=None))
O_STYLE_MANAGER.addStyle(QArkCriticityLevel.VERY_CRITICAL, QArkTableViewDataStyle(_o_background=O_GRADIENT_RED004, _o_foreground=O_COLOR_RED004_c, _o_font=None))
O_STYLE_MANAGER.addStyle(QArkCriticityLevel.CRITICAL, QArkTableViewDataStyle(_o_background=O_GRADIENT_RED005, _o_foreground=O_COLOR_RED005_c, _o_font=None))
O_STYLE_MANAGER.addStyle(QArkCriticityLevel.VERY_HIGH, QArkTableViewDataStyle(_o_background=O_GRADIENT_ORANGE001, _o_foreground=O_COLOR_ORANGE001_c, _o_font=None))
O_STYLE_MANAGER.addStyle(QArkCriticityLevel.HIGH, QArkTableViewDataStyle(_o_background=O_GRADIENT_ORANGE002, _o_foreground=O_COLOR_ORANGE002_c, _o_font=None))
O_STYLE_MANAGER.addStyle(QArkCriticityLevel.MEDIUM, QArkTableViewDataStyle(_o_background=O_GRADIENT_ORANGE003, _o_foreground=O_COLOR_ORANGE003_c, _o_font=None))
O_STYLE_MANAGER.addStyle(QArkCriticityLevel.LOW, QArkTableViewDataStyle(_o_background=O_COLOR_YELLOW001, _o_foreground=O_COLOR_YELLOW001_c, _o_font=None))
O_STYLE_MANAGER.addStyle(QArkCriticityLevel.NEGLIGIBLE, QArkTableViewDataStyle(_o_background=O_GRADIENT_GREEN001, _o_foreground=O_COLOR_GREEN001_c, _o_font=None))
O_STYLE_MANAGER.addStyle(QArkCriticityLevel.OK, QArkTableViewDataStyle(_o_background=O_GRADIENT_GREEN002, _o_foreground=O_COLOR_GREEN002_c, _o_font=None))
O_STYLE_MANAGER.addStyle(QArkCriticityLevel.VERY_OK, QArkTableViewDataStyle(_o_background=O_GRADIENT_BLUE001, _o_foreground=O_COLOR_BLUE001_c, _o_font=None))
O_STYLE_MANAGER.addStyle(QArkCriticityLevel.EXCLAMATION, QArkTableViewDataStyle(_o_background=O_GRADIENT_ROSE001, _o_foreground=O_COLOR_ROSE001_c, _o_font=None))
