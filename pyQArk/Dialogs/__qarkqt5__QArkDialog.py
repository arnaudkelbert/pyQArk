# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#
#
# QArkMplPlotter
#
#
# @author : Arnaud Kelbert
# @date : 2019/03/05
# @version : 0.2
#
# Historic:
# 0.1 : init version
# 0.2 : add python 2/3 compatibility
#-----------------------------------------------------------------------
#{-- Pyhton 2/3 compatibility ------------------------------------------
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
#}-- Pyhton 2/3 compatibility ------------------------------------------
from PyQt5 import QtCore, QtGui

class QArkDialog(object):

    @classmethod
    def centerDialog( cls, dialog, host=None, screenId=0, useVirtualDesktop=False ):
        """
        Inspired from C++ code :

        inline void CenterWidgets(QWidget *widget, QWidget *host = 0) {
            if (!host)
                host = widget->parentWidget();

            if (host) {
                auto hostRect = host->geometry();
                widget->move(hostRect.center() - widget->rect().center());
            }
            else {
                QRect screenGeometry = QApplication::desktop()->screenGeometry();
                int x = (screenGeometry.width() - widget->width()) / 2;
                int y = (screenGeometry.height() - widget->height()) / 2;
                widget->move(x, y);
            }
        }
        """
        size = dialog.sizeHint()
        if host is None:
            # use screen
            if QtGui.QDesktopWidget().isVirtualDesktop() and useVirtualDesktop:
                hostGeometry = QtGui.QDesktopWidget().screen().rect()
            else:
                hostGeometry = QtGui.QDesktopWidget().screenGeometry(screenId)

            x = (hostGeometry.width() - size.width()) // 2
            y = (hostGeometry.height() - size.height()) // 2
            dialog.move(x,y)

        else:
            dialogSize = dialog.sizeHint()
            hostCenter = host.mapToGlobal( host.rect().center() )
            dialog.move( hostCenter.x() - dialogSize.width()//2
                        ,hostCenter.y() - dialogSize.height()//2
                        )
