#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 13:09:36 2019

@author: guevaran
"""
#%%

import os
os.chdir('/home/guevaran')
from pyraf import iraf
os.system('ds9 -fifo dev/imt1 &')
os.chdir('/home/guevaran/Documents/Observacional/tp9/111214')
os.chdir('/home/guevaran/Documents/Observacional/tp10')

#%%
image='nav.fit'
iraf.images.tv.display(image)
#iraf.imexamine()
coord='coords.coo'
#%%
iraf.noao()
iraf.digiphot()
iraf.apphot()

iraf.datapars.ccdread="rdnoise"
iraf.datapars.gain="gain"
iraf.datapars.exposure="exptime"
iraf.datapars.airmass="airmass"
iraf.datapars.filter="filter"
iraf.datapars.obstime="time-obs"
iraf.fitskypars.annulus=30
iraf.fitskypars.dannulus=5
iraf.photpars.apertures="0.5,1:30:1"

iraf.phot.image=image
iraf.phot.coords=coord
iraf.phot.output='phot.out'
iraf.phot.interac='no'
iraf.phot()

#%%

for i in range(1,4):
    name='star'+ str(i) + '.tab'
    if os.path.exists(name):
        os.remove(name)
    f=open(name,'w+')
    for j in range(1,32):
        fields="Id,Rapert["+str(j)+"],Mag["+str(j)+"],Merr["+str(j)+"],Area["+str(j)+"],Flux["+str(j)+"],Annulus,Dannulus,MSky,Stdev,NSky,Sum["+str(j)+"],XCenter,YCenter"
        iraf.txdump.fields=fields
        test=iraf.txdump("phot.out",expr="Id == "+str(i),headers='no',Stdout=1)
        print >> f,test[0]
    f.close()
#%%

import matplotlib.pyplot as plt
import numpy as np

data1= np.genfromtxt('star1.tab', dtype=float)
#data2= np.genfromtxt('star2.tab', dtype=float)
#data3= np.genfromtxt('star3.tab', dtype=float)

plt.plot(data1[:,1],data1[:,5]/data1[:,4],'r*')

plt.xlabel('Radio de apertura [pix]')
plt.ylabel('Intensidad')

#plt.show()
plt.savefig('ej6.eps')
#%%
import math
def perf_gauss(x, G, sigma2):
    return G*np.exp(-(x)**2/(2*sigma2))
def perf_moffat(x,L0,a,b):
    return L0/(1.+ ((x/a)**2)**b )
def perf_lorentz(x,M0,a,b):
    return (M0/(1.+(x/a)**2))**b

from scipy.optimize import curve_fit

poptg, pcovg = curve_fit(perf_gauss,data1[:,1],data1[:,5]/data1[:,4])
poptm, pcovm = curve_fit(perf_moffat,data1[:,1],data1[:,5]/data1[:,4])
poptl, pcovl = curve_fit(perf_lorentz, data1[:,1], data1[:,5]/data1[:,4])
x=np.linspace(0,30,num=1000)
plt.figure()
plt.legend()
plt.plot(data1[:,1],data1[:,5]/data1[:,4],'r*')
plt.plot(x,perf_gauss(x, *poptg), label='Gauss')
plt.plot(x,perf_lorentz(x, *poptl),label='Lorentz')
plt.plot(x,perf_moffat(x, *poptm),label='Moffat')
plt.show()
