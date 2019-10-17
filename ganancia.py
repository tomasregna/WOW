#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 10:06:22 2019

@author: tregna
"""
#%% #################################
import numpy as np
from pyraf import iraf
#import pyraf
#import matplotlib.pyplot as plt
#import numpy.polynomial as P
 
#%% ##################################
"""
Vamos a armar un programa que calcule la ganancia, el ruido de lectura,
 ¿y la corriente de oscuridad? (si supiera la formula)
 
 Para esto, usaremos las formulas obtenidas de la practica de CCDs:
     
     g = [(<flat1> + <flat2>) - (<bias1> + <bias2>)] / [std(flat1-2)^2 - std(bias1-2)^2]
     
     preguntas varias: ¿si tengo n flats y n bias en vez de un par, cómo es la fórmula?
                       ¿qué significa la desviacion estandar de la resta?¿fórmula?
                       ¿qué significa el valor medio de bias o flat (<>)?¿es tomar el 
                        valor medio de los pixeles del flat/bias?
     
     ruido_detector=rdnoise = g * std(bias1-2) / sqrt(2)
     
Con esto en mente, ni bien responda esas preguntas, resta resolver:
    1.¿Cómo llamo a las imágenes que no están en un archivo .in, y tomarlas de la carpeta?
    ¿Se puede? carpetas io y sys (para hacer cosas con el bash desde python/fortran(¿?), etc)
    2.¿Cómo selecciono sólo las que son de bias, o solo las de flat? 
    3.¿Cómo obtengo los parámetros estadísticos (de qué tarea los calculo)?
    
3. En la tarea imstat...          


"""

flat_b= np.genfromtxt('flatb.in', dtype=None)
flat_v= np.genfromtxt('flatv.in', dtype=None)

#%% ############################################
'''cortamos la region de borde y donde hay un gradiente pronunciado en el flat'''

imagen_cut= []

for im in flat_b:
    imagen_cut.append( im + '[120:300,120:300]' )

#el operador + depende de que variables tenga, hace una operacion u otra: adicion, si son reales o enteros,
#...yyyy concatenacion, si son caracteres    
print '\n'
print imagen_cut

lista_flat_b= ','.join(imagen_cut)
lista_flat_v= ','.join(flat_v)
#%% ############################################
v=[]
stats=iraf.imstat(lista_flat_v, fields='mean,mode,stddev', Stdout=1)
#acordate, Stdout=1 te lo guarda en una lista, si no lo pones, no te guarda nada nabo!!!
print stats

#v=stats[1].split()
#print v
#...

mean= []
mode= []
stddev= []

for i in stats[1:]:
    #le pedimos for...tata...[1] porque el primer elemento no nos interesa, ya que es el titulo nomas
    #print i, i.split()
    #el i no funciona como indice, sino como elemento (por eso cuando pedis que imprima
    #el i, no te imprime un numero, sino todo el elemento)
    mean.append( float( i.split()[0] ) )
    mode.append( float( i.split()[1] ) )
    stddev.append( float( i.split()[2] ) )
    
print '\n'
print 'mean-f=', mean
print 'mode-f=', mode
print 'stddev-f=', stddev

#manera alternativa de usar el for
#for i in range(1,len(stats)):
#    v.append(stats[i].split())
#    print i, stats[i], v[i-1]
    #i.split('\t')[1]
 
# otra manera alternativa de usar el for    
#for i,s in enumerate(stats):
#    print i, s
#%%
'''Hacemos lo mismo para los bias gg'''
bias= np.genfromtxt('bias.in', dtype=None)
lista_bias= ','.join(bias)

statsb=iraf.imstat(lista_bias, fields='mean,mode,stddev', Stdout=1)
#acordate, Stdout=1 te lo guarda en una lista, si no lo pones, no te guarda nada nabo!!!
print statsb

#v=stats[1].split()
#print v
#...

meanb= []
modeb= []
stddevb= []

for i in statsb[1:]:
    #le pedimos for...tata...[1] porque el primer elemento no nos interesa, ya que es el titulo nomas
    #print i, i.split()
    #el i no funciona como indice, sino como elemento (por eso cuando pedis que imprima
    #el i, no te imprime un numero, sino todo el elemento)
    meanb.append( float( i.split()[0] ) )
    modeb.append( float( i.split()[1] ) )
    stddevb.append( float( i.split()[2] ) )
    
print '\n'
print 'mean-b=', meanb
print 'mode-b=', modeb
print 'stddev-b=', stddevb
    
#%% ###########################################
'''laburamos haciendo las cuentas ahora...
el problema es que hay que tomar la desviacion estandar de la resta de las fotos...
simplemente, restamos las fotos con la tarea imarit, y pedimos la estadistica de esa resta!
imarit: tarea para sumar, restar, multip, div, etc etc a las imagenes!! (pixel a pixel)

'''
#iraf.imarith('ffcv0001.fit','-','ffcv0002.fit',result='flat1-2_v_test1.fit',title='flat1-2.fit')
#iraf.imarith('bias0001.fit','-','bias0002.fit',result='bias1-2_v_test1.fit',title='bias1-2.fit')

'''importando la lib. os , para saber si E el archivo, hago os.path.exist('el_archivo') y me tira un V o F --------> haciendo un if, 
puedo elegir borrarlo...

cómo? haciendo os.delete('archivo') o os.remove('archivo')

'''

std_flat12=iraf.imstat('flat1-2_v_test1.fit', fields='stddev', Stdout=1)[1]
std_bias12=iraf.imstat('bias1-2_v_test1.fit', fields='stddev', Stdout=1)[1]

print 'desv_flat=', std_flat12
print 'desv_bias=', std_bias12

#print std_bias12, std_flat12
g = (mean[0]+mean[1] - (meanb[0]+meanb[1]))/((float(std_flat12))**2 - (float(std_bias12)**2))
print 'ganancia=',g

#me da 2.09, lo que uno esperarìaaaaaaaaaaaaaa

#%%
'''Veamos el ruido (rdnoise)
sale con la formula:
    
    rdnoise=g*stddev_bias_resta/sqrt(2)
    
'''

rdnoise = float(g)*float(std_bias12)/np.sqrt(2.)

print 'rdnoise=',rdnoise




