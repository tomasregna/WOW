 #!/usr/bin/env python2
# -*- coding: utf-8 -*-
from wow import *
import sys
import yaml


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
        Ahora voy a definir las fucnionalidades de los botones principales
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
                state!=QtCore.Qt.Unchecked)
        )
        #---------
        # defino lista de formatos
        self.formatoselect.addItems(('zip','tar','gztar','bztar'))
        #---------
        # seteo el buscador de carpetas
        self.navegarselectcarpeta.clicked.connect(self.direcbrowser)
        #linkea buscador de carpetas con el lineedit
        #---------


        '''
-----------------------------------------------------
        REDUCCION
-----------------------------------------------------
        '''
        #esto inhabilita todas las opciones si no se chekea el box re reduc
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
        self.hacerphot_2.stateChanged.connect(
            lambda state:
            self.groupapertura_2.setEnabled(
                state!=QtCore.Qt.Unchecked))
        self.hacerphot_2.stateChanged.connect(
            lambda state:
            self.groupannulus_2.setEnabled(
                state!=QtCore.Qt.Unchecked))
        self.hacerphot_2.stateChanged.connect(
            lambda state:
            self.buscestre_2.setEnabled(
                state!=QtCore.Qt.Unchecked))
        self.hacerphot_2.stateChanged.connect(
            lambda state:
            self.imageneslabel_2.setEnabled(
                state!=QtCore.Qt.Unchecked))
        self.hacerphot_2.stateChanged.connect(
            lambda state:
            self.imagenesedit_2.setEnabled(
                state!=QtCore.Qt.Unchecked))
        self.hacerphot_2.stateChanged.connect(
            lambda state:
            self.findphots_2.setEnabled(
                state!=QtCore.Qt.Unchecked))
        #inhabilito si no se quiere buscar estrellas

        self.buscestre_2.stateChanged.connect(
            lambda state:
            self.grupobuscestrellas_2.setEnabled(
                state!=QtCore.Qt.Unchecked))
        self.buscestre_2.stateChanged.connect(
            lambda state:
            self.grouptres_2.setEnabled(
                state!=QtCore.Qt.Unchecked))
        #quiero que si esta se activa coords se desactive pero no me sale
        self.buscestre_2.stateChanged.connect(
            lambda state:
            self.groupcords_2.setEnabled(
                state!= QtCore.Qt.Unchecked))
       # inhabilito si selecciono autoFWHM
        self.calcularFWHMCheckBox_2.stateChanged.connect(
            lambda state:
            self.fWHMLineEdit_2.setEnabled(
                state!=QtCore.Qt.Unchecked))
        self.calcularFWHMCheckBox_2.stateChanged.connect(
            lambda state:
            self.fWHMLabel_2.setEnabled(
                state!=QtCore.Qt.Unchecked))
        self.calcularFWHMCheckBox_2.stateChanged.connect(
            lambda state:
            self.grouptelescop_2.setEnabled(
                state!=QtCore.Qt.Unchecked))
       # inhabilito si selecciono autoCielo

    def objbrow(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, 'Single File', QtCore.QDir.rootPath())
        self.lineedit_obj.setText(fileName)
    def biasbrow(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, 'Single File', QtCore.QDir.rootPath())
        self.lineEdit_bias.setText(fileName)
    def flatbrow(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, 'Single File', QtCore.QDir.rootPath())
        self.lineEdit_flats.setText(fileName)
    def darkbrow(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, 'Single File', QtCore.QDir.rootPath())
        self.editdark.setText(fileName)
    def direcbrowser(self):
        dirName = QtWidgets.QFileDialog.getExistingDirectory(
            self,options = QtWidgets.QFileDialog.ShowDirsOnly)
        self.pathcarpeta.setText(dirName)

    def enabler(self,check,other,*args):
        check.stateChanged.connect(
            lambda state:
            other.setEnabled(
                state!=QtCore.Unchecked))
        

        
    def guardar(self):   # defino que significa guardar
        f=open('conf.yaml','w+')
        # aca estaba testeando que funcara nomas
        data= dict(A='a',B=dict(C='c',D='d',E=True,))
        yaml.dump(data,f)
        f.close()

        




if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
