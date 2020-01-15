 #!/usr/bin/env python2
# -*- coding: utf-8 -*-
from GUIesqueleto import *
import sys
import yaml
import os

#%%
'''
Defino una clase que llama al objeto que use y el que genere
en el designer. Quiero separar el diseño de la funcionalidad.
'''
class MainWindow(QtWidgets.QDialog, Ui_WOW):
    '''
     Sobreescribo el constructor
     Aca pongo todo lo que quiero que haga la clase.
    '''
    def __init__(self,*args,**kwargs):
        QtWidgets.QMainWindow.__init__(self,*args,**kwargs)
        self.setupUi(self)

        self.setWindowIcon(QtGui.QIcon('wowlogo5.png'))
        
       
        '''
        Ahora voy a definir las funcionalidades de los botones principales
        '''
        self.Close.clicked.connect(self.close) # cierra
        # esta funcion ya se reconoce porque esta definida.
        self.Save.clicked.connect(self.guardar) # guarda
        # voy a tener que definir guardar mas adelante.

        '''
-----------------------------------------------------
        BACKUP
-----------------------------------------------------
        '''
        
        #esto inhabilita todas las opciones si no se chekea el box
        # nota: mas adelante reemplace esto por funciones
        self.hacerbackupCheckBox.stateChanged.connect(
            lambda state:
            self.nombreDelArchivoLabel.setEnabled(
                state!=QtCore.Qt.Unchecked))
        self.hacerbackupCheckBox.stateChanged.connect(
            lambda state:
            self.nombreDelArchivoLineEdit.setEnabled(
                state!=QtCore.Qt.Unchecked))
        self.hacerbackupCheckBox.stateChanged.connect(
            lambda state:
            self.formatoLabel.setEnabled(
                state!=QtCore.Qt.Unchecked))
        self.hacerbackupCheckBox.stateChanged.connect(
            lambda state:
            self.formatoselect.setEnabled(
                state!=QtCore.Qt.Unchecked))
        self.hacerbackupCheckBox.stateChanged.connect(
            lambda state:
            self.pathcarpeta.setEnabled(
                state!=QtCore.Qt.Unchecked))
        self.hacerbackupCheckBox.stateChanged.connect(
            lambda state:
            self.navegarselectcarpeta.setEnabled(
                state!=QtCore.Qt.Unchecked))
        self.hacerbackupCheckBox.stateChanged.connect(
            lambda state:
            self.Carpetaselecttext.setEnabled(
                state!=QtCore.Qt.Unchecked))
        #---------
        # defino lista de formatos
        self.formatoselect.addItems(('zip','tar','gztar','bztar'))
        #---------
        # seteo el buscador de carpetas
        self.navegarselectcarpeta.clicked.connect(self.direcbrowser)
        #---------


        '''
-----------------------------------------------------
        REDUCCION
-----------------------------------------------------
        '''
        #esto inhabilita todas las opciones si no se chekea el box de reduc
        self.Reducircheck.stateChanged.connect(
            lambda state:
            self.hacereldark.setEnabled(
                state!=QtCore.Qt.Unchecked))
        self.Reducircheck.stateChanged.connect(
            lambda state:
            self.groupreduc.setEnabled(
                state!=QtCore.Qt.Unchecked))
        self.Reducircheck.stateChanged.connect(
            lambda state:
            self.lineEdit_keyword.setEnabled(
                state!=QtCore.Qt.Unchecked))
        self.Reducircheck.stateChanged.connect(
            lambda state:
            self.label_keyword.setEnabled(
                state!=QtCore.Qt.Unchecked))
        self.Reducircheck.stateChanged.connect(
            lambda state:
            self.labelfilterfieldexpl.setEnabled(
                state!=QtCore.Qt.Unchecked))
        self.Reducircheck.stateChanged.connect(
            lambda state:
            self.secciNDeOverscanLineEdit.setEnabled(
                state!=QtCore.Qt.Unchecked))
        self.Reducircheck.stateChanged.connect(
            lambda state:
            self.secciNDeTrimmingLineEdit.setEnabled(
                state!=QtCore.Qt.Unchecked))
        self.Reducircheck.stateChanged.connect(
            lambda state:
            self.secciNDeTrimmingLabel.setEnabled(
                state!=QtCore.Qt.Unchecked))
        self.Reducircheck.stateChanged.connect(
            lambda state:
            self.secciNDeOverscanLabel.setEnabled(
                state!=QtCore.Qt.Unchecked))
        self.Reducircheck.stateChanged.connect(
            lambda state:
            self.sinosedea.setEnabled(
                state!=QtCore.Qt.Unchecked))
        #seteo los del dark
        
        self.hacereldark.stateChanged.connect(
            lambda state:
            self.editdark.setEnabled(
                state!=QtCore.Qt.Unchecked))
        self.hacereldark.stateChanged.connect(
            lambda state:
            self.label_dark.setEnabled(
                state!=QtCore.Qt.Unchecked))
        self.hacereldark.stateChanged.connect(
            lambda state:
            self.pushButton_fdarks.setEnabled(
                state!=QtCore.Qt.Unchecked))
            
  
        #----------------
        # seteo los botones para encontrar las imagenes
        self.pushButton_obj.clicked.connect(self.objbrow)
        self.pushButton_bias.clicked.connect(self.biasbrow)
        self.pushButton_flats.clicked.connect(self.flatbrow)
        self.pushButton_fdarks.clicked.connect(self.darkbrow)
      
        '''
-----------------------------------------------------
        FOTOMETRIA
-----------------------------------------------------     
        '''

         #inhabilito todo si no se chekea para hacer fotometria.
        self.hacerphot_2.stateChanged.connect(self.checkearphot)
        #inhabilito si no se quiere buscar estrellas
        self.buscestre_2.stateChanged.connect(self.checkbuscest)
       # inhabilito si selecciono autoFWHM
        self.calcularFWHMCheckBox_2.stateChanged.connect(
            self.checkautofw)
       # inhabilito si selecciono autoCielo
        self.calcularRuidoDelCieloCheckBox_2.stateChanged.connect(
            self.checkautocielo)
        #inhabilito si selecciono autoapertura
        self.aperturaAtumTicaCheckBox_2.stateChanged.connect(
            self.checkapert)
        #---------------
        #seteo botones
        self.buscarcoordenadas_2.clicked.connect(self.coordbrow)
        self.findphots_2.clicked.connect(self.imbrow)
        #---------------
        # seteo lista de telescopios
        self.selectelescopi_3.addItems(('JS','HSH'))
        #todo: if telescopio X habilitar el RF

        # dejo estos valores x defecto
        self.fWHMLineEdit_2.setText('0')
        self.ruidoDeCieloLineEdit_2.setText('0')
        self.aperturaLineEdit_2.setText('0')
        self.trinput_2.setText('0')
        self.aperturaLineEdit_2.setText('0')
        self.annulusLineEdit_2.setText('0')
        self.dannulusLineEdit_2.setText('0')
        
        '''
-----------------------------------------------------
        TABLEMAKER
-----------------------------------------------------     
        '''
        # inhabilito todo si no esta chekeado hacertabla
        self.hacerTablaCheckBox.stateChanged.connect(self.checktable)
        #-----------
        # seteo listas
        self.esquemaComboBox.addItems(('imagen','estrella'))
        formatos=('aastex','basic','commented_header','csv',
                  'ecsv','fixed_width','fixed_width_no_header',
                  'fixed_width_two_line','html','ipac','latex',
                  'no_header','rbd','rst','tab')
        self.formatoDeSalidaComboBox.addItems(formatos)
        #-----------
        # seteo boton
        self.navegartablasphot.clicked.connect(self.tabbrow)
        
        #------------------------------------------------------------
        self.load() # precarga datos en el configfile
        '''
----------------------------------------------------------------
        '''
            # funciones usadas por botones de navegar
    def objbrow(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, 'Single File')
        self.lineedit_obj.setText(fileName)
        
    def biasbrow(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, 'Single File')
        self.lineEdit_bias.setText(fileName)
    def flatbrow(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, 'Single File')
        self.lineEdit_flats.setText(fileName)
    def darkbrow(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, 'Single File')
        self.editdark.setText(fileName)
    def direcbrowser(self):
        dirName = QtWidgets.QFileDialog.getExistingDirectory(
            self,options = QtWidgets.QFileDialog.ShowDirsOnly)
        self.pathcarpeta.setText(dirName)
    def coordbrow(self):
        fileName, _= QtWidgets.QFileDialog.getOpenFileName(
            self, 'Single File')
        self.coordenadasLineEdit_2.setText(fileName)
    def imbrow(self):
        fileName, _= QtWidgets.QFileDialog.getOpenFileName(
            self, 'Single File')        
        self.imagenesedit_2.setText(fileName)
    def tabbrow(self):
        fileName, _= QtWidgets.QFileDialog.getOpenFileName(
            self, 'Single File')        
        self.tablasPhotLineEdit.setText(fileName)

            # funciones que inhablitan sectores del GUI 
    def checkearphot(self,int):
        if self.hacerphot_2.isChecked():
            habilita=True
            if self.buscestre_2.isChecked():
                habilita2=False
            else:
                habilita2=True
            if self.calcularFWHMCheckBox_2.isChecked():
                habilita3=True
            else:
                habilita3=False
        else:
            habilita=False
            habilita2=False
            habilita3=False
            
        self.groupapertura_2.setEnabled(habilita)
        self.groupannulus_2.setEnabled(habilita)
        self.buscestre_2.setEnabled(habilita)
        self.imageneslabel_2.setEnabled(habilita)
        self.imagenesedit_2.setEnabled(habilita)
        self.findphots_2.setEnabled(habilita)
        self.groupcords_2.setEnabled(habilita2)
        self.coordenadasLineEdit_2.setEnabled(habilita2)
        self.coordenadasLabel_2.setEnabled(habilita2)
        self.buscarcoordenadas_2.setEnabled(habilita2)
        self.buscestrelabel_2.setEnabled(habilita)
        self.grouptelescop_2.setEnabled(habilita3)
        self.grupobuscestrellas_2.setEnabled(habilita)
        self.grouptres_2.setEnabled(habilita)
        
    def checkbuscest(self,int):
        if self.buscestre_2.isChecked():
            habilita=True
        else:
            habilita=False
        self.grupobuscestrellas_2.setEnabled(habilita)
        self.grouptres_2.setEnabled(habilita)
        self.groupcords_2.setEnabled(not habilita)
        self.coordenadasLineEdit_2.setEnabled(not habilita)
        self.coordenadasLabel_2.setEnabled(not habilita)
        self.buscarcoordenadas_2.setEnabled(not habilita)
        
    def checkautofw(self,int):
        if self.calcularFWHMCheckBox_2.isChecked():
            habilita=False
        else:
            habilita=True
        self.fWHMLineEdit_2.setEnabled(habilita)
        self.fWHMLabel_2.setEnabled(habilita)
        self.grouptelescop_2.setEnabled(not habilita)   
    def checkautocielo(self,int):
        if self.calcularRuidoDelCieloCheckBox_2.isChecked():
            habilita=False
        else:
            habilita=True
        self.ruidoDeCieloLabel_2.setEnabled(habilita)
        self.ruidoDeCieloLineEdit_2.setEnabled(habilita)

    def checkapert(self,int):
        if self.aperturaAtumTicaCheckBox_2.isChecked():
            habilita=False
        else:
            habilita=True
        self.aperturaLabel_2.setEnabled(habilita)
        self.aperturaLineEdit_2.setEnabled(habilita)

    def checktable(self,int):
        if self.hacerTablaCheckBox.isChecked():
            habilita=True
        else:
            habilita=False
        self.grouptablas.setEnabled(habilita)
            
        #  funciones que sirven para volcar los inputs en 
        # variables y en un archivo yaml.
    def guardar(self):   # defino que significa guardar
        data3=self.savedata()
        f=open('parameters.yaml','w+')
        yaml.dump(data3,f)
        f.close()

    def savedata(self):
        g=open('parameters.yaml','r') # opens yaml file read only
        maindict=yaml.load(g)   # loads yaml dict
        g.close()
        
        
        #######
        #backup
        maindict['backup']['dobackup']=self.hacerbackupCheckBox.isChecked()
        maindict['backup']['path']= self.strn(self.pathcarpeta.text())
        maindict['backup']['opciones']['formato']=self.strn(self.formatoselect.currentText())
        maindict['backup']['opciones']['filename']=self.strn(self.nombreDelArchivoLineEdit.text())
        #######
        #reduccion
        maindict['reducir']['doreducir']=self.Reducircheck.isChecked()
        fileandpath=os.path.split(self.strn(self.lineedit_obj.text()))
        maindict['reducir']['pathim']=self.strn(fileandpath[0])
        maindict['reducir']['imobj']=self.strn(fileandpath[-1])
        fileandpath=os.path.split(self.strn(self.lineEdit_bias.text()))
        maindict['reducir']['imbias']=self.strn(fileandpath[-1])
        maindict['reducir']['pathbi']=self.strn(fileandpath[-0])
        fileandpath=os.path.split(self.strn(self.lineEdit_flats.text()))
        maindict['reducir']['imflat']=self.strn(fileandpath[-1])
        maindict['reducir']['pathfl']=self.strn(fileandpath[-0])
        
        maindict['reducir']['overscan']=self.strn(self.secciNDeOverscanLineEdit.text())
        maindict['reducir']['trim']=self.strn( self.secciNDeTrimmingLineEdit.text())

        maindict['reducir']['opciones']['dark']=self.hacereldark.isChecked()
        maindict['reducir']['opciones']['filterfield']=self.strn(self.lineEdit_keyword.text())
        fileandpath=os.path.split(self.strn(self.editdark.text()))
        maindict['reducir']['opciones']['imdark']=self.strn(fileandpath[-1])
        maindict['reducir']['opciones']['pathdk']=self.strn(fileandpath[0])
        #######
        #fotometria
        maindict['fotometria']['dofotometria']=self.hacerphot_2.isChecked()
        fileandpath=os.path.split(self.strn(self.imagenesedit_2.text()))
        maindict['fotometria']['imobj']=self.strn(fileandpath[-1])
        maindict['fotometria']['path']=self.strn(fileandpath[0])
        
        maindict['fotometria']['opciones']['RF']=self.redfocal_3.isChecked()
        maindict['fotometria']['opciones']['annulus']=float(
            self.annulusLineEdit_2.text())
        maindict['fotometria']['opciones']['dannulus']=float(
            self.dannulusLineEdit_2.text())
        maindict['fotometria']['opciones']['apertura']=float(
            self.aperturaLineEdit_2.text())
        maindict['fotometria']['opciones']['autocielo']=self.calcularRuidoDelCieloCheckBox_2.isChecked()
        maindict['fotometria']['opciones']['autofwhm']=self.calcularFWHMCheckBox_2.isChecked()
        maindict['fotometria']['opciones']['buscarest']=self.buscestre_2.isChecked()
        maindict['fotometria']['opciones']['cielo']=float(
            self.ruidoDeCieloLineEdit_2.text())
        fileandpath=os.path.split(self.strn(self.coordenadasLineEdit_2.text()))
        maindict['fotometria']['opciones']['coords']=self.strn(fileandpath[-1])
        maindict['fotometria']['opciones']['pathc']=self.strn(fileandpath[-0])
        maindict['fotometria']['opciones']['fwhm']=float(
            self.fWHMLineEdit_2.text())
        maindict['fotometria']['opciones']['telescopio']=self.strn(
            self.selectelescopi_3.currentText())
        maindict['fotometria']['opciones']['tr']=float(self.trinput_2.text())
        maindict['fotometria']['opciones']['autoapertura']=self.aperturaAtumTicaCheckBox_2.isChecked()
        ########
        # tablemaker

        maindict['tabla']['dotabla']=self.hacerTablaCheckBox.isChecked()
        fileandpath=os.path.split(self.strn(self.tablasPhotLineEdit.text()))
        maindict['tabla']['path']=self.strn(fileandpath[0])
        maindict['tabla']['phouts']=self.strn(fileandpath[-1])
        maindict['tabla']['opciones']['esquema']=self.strn(
            self.esquemaComboBox.currentText())
        maindict['tabla']['opciones']['formato']=self.strn(
            self.formatoDeSalidaComboBox.currentText())
        
        return maindict
    '''
    Carga el yaml con la configuracion para hacer un display de la ultima
    configuracion guardada.
    '''
    def load(self):
        g=open('parameters.yaml','r') # opens yaml file read only
        maindict=yaml.load(g)   # loads yaml dict
        g.close()
        
        #######
        #backup
  #      self.hacerbackupCheckBox.setChecked(maindict['backup']['dobackup'])
        self.pathcarpeta.setText(maindict['backup']['path'])
        self.formatoselect.setCurrentIndex(('zip','tar','gztar','bztar').index(maindict['backup']['opciones']['formato']))
        self.nombreDelArchivoLineEdit.setText(maindict['backup']['opciones']['filename'])
        
        #######
        #reduccion
     #   self.Reducircheck.setChecked(maindict['reducir']['doreducir'])
     
        self.secciNDeOverscanLineEdit.setText(self.strn(maindict['reducir']['overscan']))
        self.secciNDeTrimmingLineEdit.setText(self.strn(maindict['reducir']['trim']))
        fileandpath=self.strn(maindict['reducir']['pathim'])+'/'+ self.strn(maindict['reducir']['imobj'])
        self.lineedit_obj.setText(fileandpath)
        fileandpath=str(maindict['reducir']['pathbi'])+'/'+str(maindict['reducir']['imbias'])
        self.lineEdit_bias.setText(fileandpath)
        fileandpath=str(maindict['reducir']['pathfl'])+'/'+str(maindict['reducir']['imflat'])
        self.lineEdit_flats.setText(fileandpath)
        
        self.hacereldark.setChecked(maindict['reducir']['opciones']['dark'])
        self.lineEdit_keyword.setText(maindict['reducir']['opciones']['filterfield'])
        fileandpath=str(maindict['reducir']['opciones']['pathdk'])+'/'+str(maindict['reducir']['opciones']['imdark'])
        self.editdark.setText(fileandpath)
        
        #######
        #fotometria
  #      self.hacerphot_2.setChecked(maindict['fotometria']['dofotometria'])
        
        fileandpath=self.strn(maindict['fotometria']['path'])+'/'+self.strn(maindict['fotometria']['imobj'])
        self.imagenesedit_2.setText(fileandpath)

        self.redfocal_3.setChecked(maindict['fotometria']['opciones']['RF'])
        self.annulusLineEdit_2.setText(self.strn(maindict['fotometria']['opciones']['annulus']))
        self.dannulusLineEdit_2.setText(self.strn(maindict['fotometria']['opciones']['dannulus']))
        self.aperturaLineEdit_2.setText(self.strn(maindict['fotometria']['opciones']['apertura']))
        self.calcularRuidoDelCieloCheckBox_2.setChecked(maindict['fotometria']['opciones']['autocielo'])
        self.calcularFWHMCheckBox_2.setChecked(maindict['fotometria']['opciones']['autofwhm'])
        self.buscestre_2.setChecked(maindict['fotometria']['opciones']['buscarest'])
        self.ruidoDeCieloLineEdit_2.setText(self.strn(maindict['fotometria']['opciones']['cielo']))
        fileandpath=str(maindict['fotometria']['opciones']['pathc'])+'/'+str(maindict['fotometria']['opciones']['coords'])
        self.coordenadasLineEdit_2.setText(fileandpath)
        self.fWHMLineEdit_2.setText(self.strn(maindict['fotometria']['opciones']['fwhm']))
        self.selectelescopi_3.setCurrentIndex(('JS','HSH').index(maindict['fotometria']['opciones']['telescopio']))
        self.trinput_2.setText(self.strn(maindict['fotometria']['opciones']['tr']))
        self.aperturaAtumTicaCheckBox_2.setChecked(maindict['fotometria']['opciones']['autoapertura'])

        ########
        # tablemaker

     #   self.hacerTablaCheckBox.setChecked(maindict['tabla']['dotabla'])
        
        fileandpath=str(maindict['tabla']['path'])+'/'+str(maindict['tabla']['phouts'])
        self.tablasPhotLineEdit.setText(fileandpath)
        self.esquemaComboBox.setCurrentIndex(('imagen','estrella').index(maindict['tabla']['opciones']['esquema']))
        formatos=('aastex','basic','commented_header','csv',
                  'ecsv','fixed_width','fixed_width_no_header',
                  'fixed_width_two_line','html','ipac','latex',
                  'no_header','rbd','rst','tab')
        self.formatoDeSalidaComboBox.setCurrentIndex(formatos.index(maindict['tabla']['opciones']['formato']))
      
        
    def strn(self,x):
        if x=='' or x=='None' or x=='null':
            a=None
        else:
            a=str(x)
        return a
            

        




if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
