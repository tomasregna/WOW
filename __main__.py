#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 12:39:59 2019

@author: intel
"""
import yaml
#%%
def main():
    '''
    Setea modulos
    '''
    from setmodules import setmodules
    setmodules()

#%%
    '''
    Lee archivo de parametros
    '''
    f=open('parameters.yaml','a+')
    data=yaml.load(f)
    f.close()
#%%
    '''
    Backup
    '''
    if data['backup']:
        backup()
    
#%%
    '''
    Reduccion
    '''
    if data['reducir']['doreducir']:
        imagenes=data['reducir']['imobj']
        bias=data['reducir']['imbias']
        flat=data['reducir']['imflat']
        dark=data['reducir']['opciones']['imdark']
        
        reduc.masterbias(bias)
        if data['reducir']['opciones']['dark']:
            reduc.masterdark(dark)
        filters,flats=filtersep2(flat)
        filters2,objs=filtersep2(imagenes)
        if not filters==filters2:
            print "Los filtros de los flats y las imagenes de ciencia"
            print "no coinciden."
            print " Go home you're drunk"
        wh.flatw(filters,flats,dark=data['reducir']['opciones']['dark'])
        wh.procw(filters2,objs,dark=data['reducir']['opciones']['dark'])
        
#%%  
    '''
    Fotometria
    '''
    if data['fotometria']['dofotometria']:
        images=data['fotometria']['imobj']
        if data['fotometria']['opciones']['buscarest']:
            cielo=skynoises(images)
            tel=data['fotometria']['opciones']['telescope']
            fw=multifull(images,tel,RF=data['fotometria']['opciones']['RF'])
            tres=data['fotometria']['opciones']['tr']
            multifinder(images,farr=fw,sarr=cielo,tres)
            an=data['fotometria']['opciones']['annulus']
            dan=data['fotometria']['opciones']['dannulus']
            ap=data['fotometria']['opciones']['apertura']
            photom(images,an,dan,ap)
#%%
    if data['tabla']['dotabla']:
        gentable(data['tabla']['phouts'],data['tabla']['opciones']['apertura'],
                 formato=data['tabla']['opciones']['formato'])
#%%
  
if __name__== "__main__":
    main()
