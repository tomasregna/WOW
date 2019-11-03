#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 13:09:36 2019

@author: guevaran
"""
#%%

import os
os.chdir('/home/natalia')
from pyraf import iraf
os.system('ds9 -fifo dev/imt1 &')
os.chdir('/home/natalia/Documentos/Materias/Observacional/tp10')

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
if os.path.exists('phot.out'):
    os.remove('phot.out')
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
        fields="Id,Rapert["+str(j)+"],Mag["+str(j)+"],Merr["+str(j
                          )+"],Area["+str(j)+"],Flux["+str(j
                             )+"],Annulus,Dannulus,MSky,Stdev,NSky,Sum["+str(j
                             )+"],XCenter,YCenter"
        iraf.txdump.fields=fields
        test=iraf.txdump("phot.out",expr="Id == "+str(i),headers='no',Stdout=1)
        print >> f,test[0]
    f.close()
#%%

import matplotlib.pyplot as plt
import numpy as np

data1= np.genfromtxt('star1.tab', dtype=float)
data2= np.genfromtxt('star2.tab', dtype=float)
data3= np.genfromtxt('star3.tab', dtype=float)

plt.plot(data1[:,1],data1[:,5]/data1[:,4],'r*')

plt.xlabel('Radio de apertura [pix]')
plt.ylabel('Intensidad')

#plt.show()
plt.savefig('ej6.eps')
#%%
def perf_gauss(x, G, sigma):
    return G*np.exp(-(x)**2/(2*sigma**2))

def perf_moffat(x,M0,a,b):
    return M0/(1.+ ((x/a)**2)**b )

#def perf_lorentz(x,M0,a,b):
#    return (M0/(1.+(x/a)**2))**b
def perf_lorentz(x,L0,a):
    return L0/(1.+(x/a)**2)

from scipy.optimize import curve_fit

poptg, pcovg = curve_fit(perf_gauss,data1[:,1],data1[:,5]/data1[:,4])
poptm, pcovm = curve_fit(perf_moffat,data1[:,1],data1[:,5]/data1[:,4])
poptl, pcovl = curve_fit(perf_lorentz, data1[:,1], data1[:,5]/data1[:,4])
x=np.linspace(0,30,num=1000)
plt.figure()

plt.xlabel('Radio de apertura [pix]')
plt.ylabel('Intensidad')

plt.plot(data1[:,1],data1[:,5]/data1[:,4],'r*', label='Data')
plt.plot(x,perf_gauss(x, *poptg), label='Gauss')
plt.plot(x,perf_lorentz(x, *poptl),label='Lorentz')
plt.plot(x,perf_moffat(x, *poptm),label='Moffat')
plt.legend()
plt.savefig('ej6ajustes.eps')
#%%
import math
import numpy as np

g0=perf_gauss(0,poptg[0],poptg[1])/2
fwg = math.sqrt(2.*math.log( poptg[0]/g0 ))*(poptg[1])

m0=perf_moffat(0,poptm[0],poptm[1],poptm[2])/2
fwm= math.pow(((poptm[0]/m0)-1.),1/(2*poptm[2])) * poptm[1]

l0=perf_lorentz(0,poptl[0],poptl[1])/2
fwl= math.sqrt((poptl[0]/l0) -1.)*poptl[1]


print ',Gauss,Moffat,Lorentz'
print 'FWHM,',"%5.2f"%(fwg),"%5.2f"%(fwm),"%5.2f"%(fwl)
print 'errores'
print np.sqrt(np.diag(pcovg)) # bochoa de error en gauss
print np.sqrt(np.diag(pcovm))
print np.sqrt(np.diag(pcovl))
#%%
plt.figure()

plt.xlabel('Radio de apertura [pix]')
plt.ylabel('Magnitud Instrumental')
plt.gca().invert_yaxis()
plt.errorbar(data1[:,1],data1[:,2]-data1[:,8],yerr=data1[:,3],fmt='.',label='Brillo Alto')
plt.errorbar(data2[:,1],data2[:,2]-data2[:,8],yerr=data1[:,3],fmt='.',label='Brillo Medio')
plt.errorbar(data3[:,1],data3[:,2]-data3[:,8],yerr=data1[:,3],fmt='.',label='Brillo Bajo')

plt.legend()
plt.savefig('ej6curvadecrecimientoccd.eps')

#%%

