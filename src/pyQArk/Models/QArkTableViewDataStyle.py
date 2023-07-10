# -*- coding: utf-8 -*-
from PyQt5 import QtGui

def createGradientBrush(_o_color1, _o_color2):
    verGradient = QtGui.QLinearGradient(0, 0, 0, 20)
    gradient = verGradient
    gradient.setColorAt(0.0, _o_color1)
    gradient.setColorAt(1.0, _o_color2)
    brush = QtGui.QBrush(gradient)
    return brush

class QArkTableViewDataStyle(object):
    def __init__(self, _o_background, _o_foreground, _o_font):
        self.o_background = _o_background
        self.o_foreground = _o_foreground
        self.o_font = _o_font
    def getBackgroundRole(self):
        return self.o_background
    def getForegroundRole(self):
        return self.o_foreground
    def getFontRole(self):
        return self.o_font

