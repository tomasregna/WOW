#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 11:25:43 2019

@author: guevaran
"""

#%%

def setmodules():
    import os  
    dire=os.getcwd()
    user=os.getenv('USER')
    os.chdir('/home/'+user)
    if not os.path.exists('/home/'+user+'/WOW'):
        os.mkdir('/home/'+user+'/WOW')
    import sys
    from pyraf import iraf
    import numpy as np
    import yaml 
    sys.path.insert(1, '/home/'+user+'/WOW')
    
    import auxfunctions as aux
    import reduc
    from backup import backup
    from filterseparator import filtersep2
    import wheelee as wh
    from starfinder import multisf
    from photom import photom
    from tablemaker import gentable
    from cieloruidoso import skynoises
    from fullwidth import fullwidth
    
    os.chdir(dire)
