# -*- coding: utf-8 -*-
def _exec(obj,*args,**kwargs):
    if hasattr(obj, 'exec'):
        return getattr(obj, 'exec')(*args, **kwargs)
    elif hasattr(obj, 'exec_'):
        return obj.exec_(*args, **kwargs)
