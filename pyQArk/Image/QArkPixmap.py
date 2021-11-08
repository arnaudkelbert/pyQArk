# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#
#
# QArkPixmap
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

import numpy as np

from pyQArk import QArkConfig
if QArkConfig.QARK_QT_GENERATION == 4:
    from PyQt4 import QtGui
elif QArkConfig.QARK_QT_GENERATION == 5:
    from PyQt5 import QtGui

class QArkPixmap( object ):

    def __init__( self ):
        super( QArkPixmap, self ).__init__()
        self.o_qimage = None
        self.o_qpixmap = None

    def initFromGreyData( self, _t_data, _o_colorMap ):
        self.createQImageFromGreyData( _t_data )
        self.setColorMap( _o_colorMap )
        self.qimageToQPixmap()

    def createQImageFromGreyData( self, _t_data ):
        t_data = _t_data.astype( np.int )

        u_mod4 = np.shape( t_data )[1] % 4
        
        if u_mod4 != 0:
            t_data4 = np.zeros( (np.shape(t_data)[0], np.shape(t_data)[1] + 4 - u_mod4), dtype=np.int )
            t_data4[ 0:np.shape(t_data)[0],0:np.shape(t_data)[1] ] = t_data[ 0:np.shape(t_data)[0],0:np.shape(t_data)[1] ]
            t_data = t_data4
        
        t_data = np.require( t_data, np.uint8, 'C' )
        #print "TODO : Gerer le 32-bit aligned"
        self.o_qimage = QtGui.QImage( t_data.data
                                     , np.shape( t_data )[1]
                                     , np.shape( t_data )[0]
                                     , QtGui.QImage.Format_Indexed8
                                     )
        self.o_qimage.ndarray = t_data

    def setColorMap( self, _o_colorMap ):
        self.o_qimage.setColorTable( _o_colorMap )

    def qimageToQPixmap( self ):
        self.o_qpixmap = QtGui.QPixmap.fromImage( self.o_qimage )

    def getPixmap( self ):
        return self.o_qpixmap

    def reload( self ):
        self.qimageToQPixmap()
