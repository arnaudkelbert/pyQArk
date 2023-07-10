# -*- coding: utf-8 -*-
import numpy as np
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
        t_data = _t_data.astype(np.int32)

        u_mod4 = np.shape( t_data )[1] % 4
        
        if u_mod4 != 0:
            t_data4 = np.zeros( (np.shape(t_data)[0], np.shape(t_data)[1] + 4 - u_mod4), dtype=np.int32 )
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
