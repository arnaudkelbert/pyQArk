# -*- coding: utf-8 -*-
import time

class QArkException( Exception ):
    """
    A class that represents an exception.
    The time is stored at object creation.
    """
    def __init__( self
                  , _s_message
                  ):
        Exception.__init__( self, _s_message )
        self.s_time = time.strftime("%H:%M:%S")

    def __repr__( self ):
        return '[ERROR][{0}] {1}'.format( self.s_time, self.message )

    def getMessage(self):
        return self.message

    def getTime(self):
        return self.s_time
