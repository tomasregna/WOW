#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 14:54:21 2019

@author: natalia
"""
import matplotlib.pyplot as plt
import numpy as np
import numpy.polynomial as pol

data= np.genfromtxt('ej4tabla2.dat', dtype=float)
#%%

for i in [0,2]:
    if i==0:
        for j in range(1,5):
            if j==1:
                plt.plot(data[i][0],data[i][j],'bo',label='MB')
                plt.plot(data[i+1][0],data[i+1][j],'bo')
            else:
                plt.plot(data[i][0],data[i][j],'bo')
                plt.plot(data[i+1][0],data[i+1][j],'bo')
        
    else:
        for j in range(1,5):
            if j==1:
                plt.plot(data[i][0],data[i][j],'g.',label='MV')
                plt.plot(data[i+1][0],data[i+1][j],'g.')
            else:   
                plt.plot(data[i][0],data[i][j],'g.')
                plt.plot(data[i+1][0],data[i+1][j],'g.')
#    if i==1:
#        plt.plot([data[i][0]]*2,data[i][1:3],'bo',label='MB')
#        plt.plot([data[i][0]]*2,data[i][3:],'g.',label='MV')
#    else:
#        plt.plot([data[i][0]]*2,data[i][1:3],'bo')
#        plt.plot([data[i][0]]*2,data[i][3:],'g.')

plt.xlabel('X')
plt.ylabel('M')
plt.gca().invert_yaxis()
plt.legend()
#plt.show()
plt.savefig('Ej4d.eps')
#%%
coef= [None] *8
h=0
for j in range(1,5):
    for i in [0,2]: 
        a = pol.polynomial.polyfit([data[i][0],data[i+1][0]],[data[i][j],data[i+1][j]],deg=1)
        print [data[i][0],data[i+1][0]],[data[i][j],data[i+1][j]]
        coef[h]=a
        h=h+1
#for i in range(1,5):   
#    for j in [1,3]:
#        a = pol.polynomial.polyfit([data[j-1][0],data[j][0]],[data[j-1][i],data[j][i]],deg=1)
#        coef[h]=a
#        h=h+1
#%%
plt.figure()
plt.xlabel('X')
plt.ylabel('M')
plt.gca().invert_yaxis()
h=0

for i in [0,2]:
    if i==0:
        for j in range(1,5):
            if j==1:
                plt.plot(data[i][0],data[i][j],'bo',label='MB')
                plt.plot(data[i+1][0],data[i+1][j],'bo')
            else:
                plt.plot(data[i][0],data[i][j],'bo')
                plt.plot(data[i+1][0],data[i+1][j],'bo')
        
    else:
        for j in range(1,5):
            if j==1:
                plt.plot(data[i][0],data[i][j],'g.',label='MV')
                plt.plot(data[i+1][0],data[i+1][j],'g.')
            else:   
                plt.plot(data[i][0],data[i][j],'g.')
                plt.plot(data[i+1][0],data[i+1][j],'g.')
        
x=np.linspace(0,2.48,num=1001)

for i in coef:
    y=pol.polynomial.polyval(x,i)
    if not h%2:
        plt.plot(x,y,'b',linewidth=1,alpha=.5)
    else:   
        plt.plot(x,y,'g-',linewidth=1,alpha=.5)
    h=h+1

plt.legend()
#plt.show()
plt.savefig('Ej4e.eps')
#%%
#print 'MAGNITUDES FUERA DE LA ATMOSFERA'
#for i in range(8):
#    if not i%2:
#        j=i/2 +1
#        w='M_{B0}^{'+str(j)+'}='
#    else:
#        w='M_{V0}^{'+str(j)+'}='
#    print w,coef[i][0]   
#print 'COEFICIENTES DE EXTINCIÓN'
#for i in range(8):
#    if not i%2:
#        j=i/2 +1
#        w='k_{B}^{'+str(j)+'}='
#    else:
#        w='k_{V}^{'+str(j)+'}='
#    print w,coef[i][1]   
print ",","k_B,","k_V,","M_{B0},","M_{V0}"
for i in [0,2,4,6]:
    print 'Star A ,',"%5.2f"%(coef[i][1]),',',"%5.2f"%(coef[i+1][1]),',',"%5.2f"%(coef[i][0]),',',"%5.2f"%(coef[i+1][0])

    
    
