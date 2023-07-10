# -*- coding: utf-8 -*-
class QArkFuncArg( object ):
    
    def __init__(self, _s_key, _x_value=None, _cls_type=None, _b_required = True,  **kwargs ):
        self.s_key = _s_key
        self.cls_type = _cls_type
        self.x_value = _x_value
        self.b_required = _b_required
    
    def getKey(self):
        return self.s_key
    
    def setKey(self, _s_key):
        self.s_key = _s_key
    
    def getType(self):
        return self.cls_type
    
    def setType(self, _cls_type):
        self.cls_type = _cls_type
    
    def getValue(self):
        return self.x_value
    
    def setValue(self, _x_value):
        self.x_value = _x_value

    def isRequired(self):
        return self.b_required
    
    def setRequired(self, _b_bool):
        self.b_required = _b_bool
