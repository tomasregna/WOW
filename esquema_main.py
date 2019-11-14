#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 12:39:59 2019

@author: intel
"""
#%%
from pyraf import iraf
import auxfunctions as aux
import reduc
from backup import backup
from filterseparator import filtersep
import wheelee as wh
from starfinder import starfinder
from photom import photom
from tablemaker import gentable
from asciinator import asciinator
from fullwidth import fullwidth
#%%
filt=True
doflat=True
pytab=True
backup()

#%%
aux.hedit()
reduc.masterbias()
reduc.masterdark()

if filt is True :
    filtersep()
    if doflat is True :
        wh.flatw()
    wh.proc()
else:
    if doflat is True :
        reduc.masterflat()
    reduc.process()
   
#%%
fullwidth()
starfinder()

photom()

#%%

if pytab is True :
    gentable()
else :
    asciinator()
    
 
