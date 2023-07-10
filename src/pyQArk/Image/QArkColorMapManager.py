# -*- coding: utf-8 -*-
import os
import math
import inspect
from PyQt5 import QtCore, QtGui


class QArkColorMapManager( QtCore.QObject ):

    def __init__( self ):
        """Constructeur
        @param _s_filename : fichier image
        @type _s_filename : C{str}
        """
        QtCore.QObject.__init__( self )
        self.t_colorMap = {}

        self.loadColorMapRepository( os.path.abspath( os.path.join( os.path.dirname( inspect.getfile(inspect.currentframe()) ), 'colormap' ) ) )

        self.genColorMap_GREY()
        self.genColorMap_BLUE()
        self.genColorMap_RED()
        self.genColorMap_GREEN()
        self.genColorMap_SINUS()

        self.s_default = 'GREY'

    def getColorMapIdList( self ):
        return self.t_colorMap.keys()

    def getColorMapList( self ):
        return self.t_colorMap

    def genColorMap_GREY( self ):
        self.t_colorMap[ 'GREY' ] = [ QtGui.qRgb(k,k,k) for k in range(256) ]

    def genColorMap_BLUE( self):
        self.t_colorMap[ 'BLUE' ] = [ QtGui.qRgb(0,0,k) for k in range(256) ]

    def genColorMap_RED( self):
        self.t_colorMap[ 'RED' ] = [ QtGui.qRgb(k,0,0) for k in range(256) ]

    def genColorMap_GREEN( self):
        self.t_colorMap[ 'GREEN' ] = [ QtGui.qRgb(0,k,0) for k in range(256) ]

    def genColorMap_SINUS( self):
        self.t_colorMap[ 'SINUS' ] = [ QtGui.qRgb(int(math.sin(k*2.0*math.pi/255.0))*255,
                                                  int(math.sin(k*2.0*math.pi/255.0))*255,
                                                  int(math.sin(k*2.0*math.pi/255.0))*255)
                                                  for k in range(256) ]

    def getColorMap( self, _s_colorMapKey ):
        return self.t_colorMap[ _s_colorMapKey ]

    def getDefaultColorMap( self ):
        return self.t_colorMap[ self.s_default ]

    def loadColorMapFile( self, _s_file ):
        fp = open( _s_file, 'r' )
        t_lines = fp.read().split('\n')
        fp.close()

        s_key = t_lines[0]
        #print "Loading colormap %s : %s" % (s_key,_s_file)

        def colorLineToRGB( _s_line ):
            c = [int(x) for x in _s_line.split(',')]
            return QtGui.qRgb( c[0], c[1], c[2] )

        self.t_colorMap[ s_key ] = [colorLineToRGB(v) for v in t_lines[1:257]]

    def loadColorMapRepository( self, _s_dir ):

        o_dirWalk = QtCore.QDirIterator( _s_dir, QtCore.QDirIterator.Subdirectories )

        while o_dirWalk.hasNext():
            o_dirWalk.next()

            if o_dirWalk.fileInfo().completeSuffix() == 'cmap':
                self.loadColorMapFile( o_dirWalk.filePath() )
