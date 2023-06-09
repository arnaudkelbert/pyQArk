# -*- coding: utf-8 -*-
class QArkRange(object):
    
    def __init__(self, _x_min, _x_max):
        #self.t_range = sorted([_x_min, _x_max])
        self.t_range = [_x_min, _x_max ]
    
    def __getitem__(self, index):
        if index == 'min': index = 0
        elif index == 'max': index = 1
        return self.t_range[index]
    
    def __setitem__(self, index, value):
        if index == 'min': index = 0
        elif index == 'max': index = 1
        self.t_range[index] = value
    
    def min(self):
        return self.t_range[0]
    
    def max(self):
        return self.t_range[1]
    
    def __repr__(self):
        return self.t_range.__repr__()
    
    def __str__(self):
        return self.t_range.__str__()
