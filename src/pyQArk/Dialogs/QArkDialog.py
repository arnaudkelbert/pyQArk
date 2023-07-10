# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets

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
            if QtWidgets.QDesktopWidget().isVirtualDesktop() and useVirtualDesktop:
                hostGeometry = QtWidgets.QDesktopWidget().screen().rect()
            else:
                hostGeometry = QtWidgets.QDesktopWidget().screenGeometry(screenId)

            x = (hostGeometry.width() - size.width()) // 2
            y = (hostGeometry.height() - size.height()) // 2
            dialog.move(x,y)

        else:
            dialogSize = dialog.sizeHint()
            hostCenter = host.mapToGlobal( host.rect().center() )
            dialog.move( hostCenter.x() - dialogSize.width()//2
                        ,hostCenter.y() - dialogSize.height()//2
                        )
