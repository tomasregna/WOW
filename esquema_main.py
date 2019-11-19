#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 12:39:59 2019

@author: intel
"""
#%%
import os

dire=os.getcwd()
user=os.getenv('USER')
os.chdir('/home/'+user)
from pyraf import iraf
os.chdir(dire)

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

#%%
reducir=True
heditar=True
filtros=True
dodark=True
dophot=True
dotab=True

backup()

#%%
if heditar :
    aux.hedit()

#%%
if reducir :
    reduc.masterbias()
    if dodark :
        reduc.masterdark()

    if filtros is True :
        filtersep2()
        wh.flatw(Dark=dodark)
        wh.proc(Dark=dodark)
    else:
        reduc.masterflat(Dark=dodark)
        reduc.process(Dark=dodark)
   
#%%
if dophot :
    cielo=skynoise()
    fw=fullwidth()
    starfinder(fwhm=fw,sigma=cielo)
    photom()

#%%

if dotab is True :
    gentable()
    
 
