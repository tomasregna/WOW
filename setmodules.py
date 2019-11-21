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
    from pyraf import iraf
    os.chdir(dire)
    import numpy as np
    import yaml 
    
    import auxfunctions as aux
    import reduc
    from backup import backup
    from filterseparator import filtersep2
    import wheelee as wh
    from starfinder import starfinder
    from photom import photom
    from tablemaker import gentable
    from cieloruidoso import skynoise
    from fullwidth import fullwidth