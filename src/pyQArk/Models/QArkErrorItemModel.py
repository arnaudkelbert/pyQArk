# -*- coding: utf-8 -*-
from PyQt5 import QtGui
from pyQArk.Models.QArkSimpleItemModel import QArkSimpleItemModel


class QArkErrorItemModel( QArkSimpleItemModel ):
    """
    A simple item model implementation with 1 row and 1 column
    """

    def getDisplayRoleData( self, index ):
        """
        New method used by data in a display role
        This method should be overwritten for subclasses.
        @param index : Index to perform
        @type index : C{int}
        """
        return '{}'.format( self.o_item )


    def getDecorationRoleData( self, index ):
        """
        New method used by data in a decoration role (icon or other)
        This method should be overwritten for subclasses.
        @param index : Index to perform
        @type index : C{int}
        """
        return QtGui.QIcon.fromTheme("dialog-error")
