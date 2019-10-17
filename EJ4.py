#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 15:03:09 2019
Ejercicio 4 de la  pr\'actica 9 de pre-reducci\'on de imagenes.

Utilizando las f\'ormulas obtenidas en los ejercicios 7 y 8 de la pr\'actica de "CCDs":
\begin{itemize}
\item Calcular la ganancia expresada en $\frac{e^-}{ADU}$.
\item Calcular el ruido de lectura expresado en $e^-$.
\item Calcular la corriente de oscuridad expresada en $\frac{e^- seg}{pix}$
\item Comparar los valores obtenidos con los dados por el fabricante (C\'amara CCD ROPER Scientific Versarray 2048B).
\item Completar los "headers" de las imágenes con los campos:
\begin{itemize}[noitemsep]
    \item GAINEADU: La ganancia del detector en $\frac{e^-}{ADU}$
    \item RDNOISE: El ruido de lectura del detector en $e^-$
\end{itemize}
\end{itemize}
@author: guevaran
"""
#%% ############################################################################
import numpy as np
from pyraf import iraf
import os
#%% ############################################################################

listabias=('bias0001.fit,bias0002.fit')
listaflats=('cielob0001.fit,cielob0002.fit')
listadarks=('dark0001.fit,dark0002.fit,dark0003.fit')
campos_print= ','.join(['image', 'mean', 'midpt', 'stddev'])
imagenes= np.genfromtxt('bias.in', dtype=None)
bias= ','.join(imagenes)
ciencia=np.genfromtxt('imagenesciencia.in', dtype=None)
objetos=','.join(ciencia)
#%% ############################################################################
"""
Hago la estasdística de las imágenes bias y flats
Lo guardo en un array.
"""
imstat_bias= iraf.imstat(listabias, fields=campos_print, Stdout=1)
imstat_flat= iraf.imstat(listaflats, fields=campos_print, Stdout=1)

meanb= []
meanf= []
for i in imstat_bias[1:]:
    meanb.append( float( i.split()[1] ) )
    
for i in imstat_flat[1:]:
    meanf.append( float( i.split()[1] ) )
#%% ############################################################################
"""
 Resto las imágenes y las guardo en una imágen distinta
 Hago la estadística de esa imágen.
 Lo guardo en una array.
"""
restab='restab.fit'
restaf='restaf.fit'
os.remove(restab)
os.remove(restaf)
iraf.imarith(operand1='bias0001.fit', op= '-', operand2='bias0002.fit', result=restab)
iraf.imarith(operand1='cielob0001.fit', op= '-', operand2='cielob0002.fit', result=restaf)

imstat_restabias= iraf.imstat(restab, fields=campos_print, Stdout=1)
imstat_restaflat= iraf.imstat(restaf, fields=campos_print, Stdout=1)
stddevrestab=[]
stddevrestaf=[]
for i in imstat_restabias[1:]:
    stddevrestab.append( float( i.split()[3] ) )
for i in imstat_restaflat[1:]:
    stddevrestaf.append( float( i.split()[3] ) )

#%% ############################################################################
'''
AYUDA

fijarse de que el imtype este bien !

'''
iraf.imred()
iraf.ccdred()
os.remove('Zero.fits')
os.remove('Dark.fits')
iraf.zerocombine(bias)
iraf.ccdpro.zerocor='yes'
iraf.ccdpro.zero='Zero.fits'
iraf.darkcombine(listadarks) 

hselectout=iraf.hselect('Dark.fits',fields='exptime',expr='yes',Stdout=1)
exptime=float(hselectout[0])
darkstat=iraf.imstat('Dark.fits', fields='mean',Stdout=1)
dk=float(darkstat[1])

#%% ############################################################################
'''
Calculo la ganancia, el ruido de lectura y la corriente de oscuridad.
'''
gain = ((meanf[0] + meanf[1]) - (meanb[0] + meanb[1]))/(stddevrestaf[0]**2 - stddevrestab[0]**2)
print 'Ganancia:',gain

rdn= gain * stddevrestab[0] / np.sqrt(2)
print rdn 

darkc= gain * dk / exptime
print darkc
#%% ############################################################################
'''
Completo los headers
'''

iraf.hedit(objetos, fields='GAINEADU',value=gain)
iraf.hedit(objetos, fields='RDNOISE',value=rdn)
iraf.hedit(objetos, fields='IMTYPE',value='object')
iraf.hedit(objetos, fields='OBJECT',value='Berkley75')
#%% ############################################################################
