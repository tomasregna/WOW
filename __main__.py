#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import yaml
#%%
def main():
    '''
    Este archivo lee el archivo de parametros yaml y ejecuta cada proceso
    segun este indicado.
    '''
    from setmodules import setmodules
    setmodules()
    import funciones.auxfunctions as aux
    from reduccion import reduc
    from funciones.backup import backup
    from reduccion.filterseparator import filtersep2
    import reduccion.wheelee as wh
    from fotometria.starfinder import multisf
    from fotometria.photom import photom
    from fotometria.tablemaker import gentable
    from fotometria.cieloruidoso import skynoises
    from fotometria.fullwidth import multifull

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
     
        path0=data['backup']['path']
    
        backup(path=path0)
    
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
            multisf(images,farr=fw,sarr=cielo,thold=tres,path=path2)
            an=data['fotometria']['opciones']['annulus']
            dan=data['fotometria']['opciones']['dannulus']
            ap=data['fotometria']['opciones']['apertura']
            photom(images,an,dan,ap,path=path2)
#%%
    '''
    Tabla
    '''
    if data['tabla']['dotabla']:
        path3=data['tabla']['path']
        form=data['tabla']['opciones']['formato']
        esque=data['tabla']['opciones']['esquema']
        gentable(data['tabla']['phouts'],formato=form,tabesq=esque,path=path3)
#%%
  
if __name__== "__main__":
    main()
