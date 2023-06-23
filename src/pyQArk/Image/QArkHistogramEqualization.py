# -*- coding: utf-8 -*-
import numpy as np
QARK_HISTOGRAM_BINS = 1000

class QArkHistogramEqualization( object ):

    (LINEAR, LINEAR_1PC, LINEAR_2PC, LINEAR_4PC, GAUSSIAN, SQRT) = range(6)

    AVAILABLE_MODES = { 'LINEAR':LINEAR
                      , 'LINEAR_1PC':LINEAR_1PC
                      , 'LINEAR_2PC':LINEAR_2PC
                      , 'LINEAR_4PC':LINEAR_4PC
                      , 'GAUSSIAN':GAUSSIAN
                      , 'SQRT':SQRT
                      }

    @classmethod
    def equalize_LINEAR( cls, _t_data, _t_outLimits ):
        """Egalisation lineaire de la matrice en entree
        @param _t_data : donnee en entree
        @type _t_data : L{np.nparray}
        @param _t_outLimits : (min, max)
        @type _t_outLimits : C{tuple}
        @rtype : L{np.nparray}
        """
        t_data = np.copy( _t_data.astype(np.float) )
        t_data = (_t_outLimits[1] - _t_outLimits[0]) * ( t_data - t_data.min() ) / ( t_data.max() - t_data.min() ) + _t_outLimits[0]
        return t_data

    @classmethod
    def equalize_LINEAR_XPC( cls, _t_data, _t_outLimits, _f_pc ):
        """Egalisation lineaire de la matrice en entree en ignorant une proportion de valeurs extremes
        @param _t_data : donnee en entree
        @type _t_data : L{np.nparray}
        @param _t_outLimits : (min, max)
        @type _t_outLimits : C{tuple}
        @param _f_pc : proportion des pixels a ignorer dans [0,1]
        @type _f_pc : C{float}
        @rtype : L{np.nparray}
        """
        t_data = np.copy( _t_data.astype(np.float) )
        t_hist = np.histogram( t_data, QARK_HISTOGRAM_BINS )
        t_histCumul = np.cumsum( (1.0*t_hist[0])/(np.shape(t_data)[0]*np.shape(t_data)[1]) )

        u_indexMin = np.where( t_histCumul > 0.5 * _f_pc )[0][0]
        u_indexMax = np.where( t_histCumul >= 1 - 0.5 * _f_pc )[0][0]
        f_valueMin = t_hist[1][u_indexMin]
        f_valueMax = t_hist[1][u_indexMax]
        t_data[ np.where(t_data < f_valueMin) ] = f_valueMin
        t_data[ np.where(t_data > f_valueMax) ] = f_valueMax

        t_data = 1.0*(_t_outLimits[1] - _t_outLimits[0]) * (t_data - f_valueMin) / ( f_valueMax - f_valueMin ) + _t_outLimits[0]

        return t_data

    @classmethod
    def computePreDefined( cls, _t_data, _t_outLimits = (0,255), _u_mode = LINEAR ):
        """Egalisation pre-definie de la matrice en entree
        @param _t_data : donnee en entree
        @type _t_data : L{np.nparray}
        @param _t_outLimits : (min, max)
        @type _t_outLimits : C{tuple}
        @param _u_mode : mode d'egalisation (LINEAR, LINEAR_1PC, LINEAR_2PC, LINEAR_4PC, GAUSSIAN, SQRT)
        @type _u_mode : C{int}
        @rtype : L{np.nparray}
        """
        t_data = None

        if _u_mode == cls.LINEAR:
            t_data = cls.equalize_LINEAR( _t_data, _t_outLimits )
        elif _u_mode == cls.LINEAR_1PC:
            t_data = cls.equalize_LINEAR_XPC( _t_data, _t_outLimits, 0.01 )         
        elif _u_mode == cls.LINEAR_2PC:
            t_data = cls.equalize_LINEAR_XPC( _t_data, _t_outLimits, 0.02 )           
        elif _u_mode == cls.LINEAR_4PC:
            t_data = cls.equalize_LINEAR_XPC( _t_data, _t_outLimits, 0.04 ) 
        return t_data
