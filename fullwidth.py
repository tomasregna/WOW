#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 15:57:23 2019

@author: guevaran
"""
#%%

def fullwidth(obser,binning=1,RF=False):
    seeing=2.5 #seeing promedio de casleo en "
    if obser=='HSH' :
        escala= 0.5424 #  arcsec/pix
    elif obser=='JS':
        if not RF:
            escala= 0.15  #  arcsec/pix
    else:
         escala= 0.45  #  arcsec/pix
    
    full=seeing/(escala*binning)
    return full