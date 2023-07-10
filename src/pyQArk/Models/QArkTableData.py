# -*- coding: utf-8 -*-

class QArkTableData(object):
    def __init__(self, *args, **kwargs):
        pass

    def cell(self, _row, _col):
        """
        This method must be defined
        """
        raise NotImplemented

    def criticityLevel(self, _row, _col):
        raise NotImplemented