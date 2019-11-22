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
    
    import funciones.auxfunctions as aux
    import reduccion.reduc
    from funciones.backup import backup
    from reduccion.filterseparator import filtersep2
    import reduccion.wheelee as wh
    from fotometria.starfinder import multisf
    from fotometria.photom import photom
    from fotometria.tablemaker import gentable
    from fotometria.cieloruidoso import skynoises
    from fotometria.fullwidth import multifull
    
    os.chdir(dire)
