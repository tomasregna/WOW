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
    if data['backup']['dobackup']:
        dirname=data['backup']['dirname']
        path0=data['backup']['path']
        formato=data['backup']['bformat']
        backup(dirname,path0,formato)
    
#%%
    '''
    Reduccion
    '''
    if data['reducir']['doreducir']:
        imagenes=data['reducir']['imobj']
        path1=data['reducir']['path']
        bias=data['reducir']['imbias']
        flat=data['reducir']['imflat']
        dark=data['reducir']['opciones']['imdark']
        
        reduc.masterbias(bias,path=path1)
        if data['reducir']['opciones']['dark']:
            reduc.masterdark(dark,path=path1)
        filters,flats=filtersep2(flat,path=path1)
        filters2,objs=filtersep2(imagenes,path=path1)
        if not filters==filters2:
            print "Los filtros de los flats y las imagenes de ciencia"
            print "no coinciden."
            print " Go home you're drunk"
        wh.flatw(filters,flats,dark=data['reducir']['opciones']['dark'],path=path1)
        wh.procw(filters2,objs,dark=data['reducir']['opciones']['dark'],path=path1)
        
#%%  
    '''
    Fotometria
    '''
    if data['fotometria']['dofotometria']:
        images=data['fotometria']['imobj']
        path2=data['fotometria']['path']
        if data['fotometria']['opciones']['buscarest']:
            cielo=skynoises(images,path=path2)
            tel=data['fotometria']['opciones']['telescope']
            fw=multifull(images,tel,RF=data['fotometria']['opciones']['RF'],path=path2)
            tres=data['fotometria']['opciones']['tr']
            multifinder(images,farr=fw,sarr=cielo,tres,path=path2)
            an=data['fotometria']['opciones']['annulus']
            dan=data['fotometria']['opciones']['dannulus']
            ap=data['fotometria']['opciones']['apertura']
            photom(images,an,dan,ap,path=path2)
#%%
    if data['tabla']['dotabla']:
        path3=data['tabla']['path']
        gentable(data['tabla']['phouts'],data['tabla']['opciones']['apertura'],
                 formato=data['tabla']['opciones']['formato'],path=path3)
#%%
  
if __name__== "__main__":
    main()
