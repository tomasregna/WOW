# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WOW(object):
    def setupUi(self, WOW):
        WOW.setObjectName("WOW")
        WOW.resize(497, 559)
        WOW.setFocusPolicy(QtCore.Qt.TabFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../WOW/wowlogo5.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        WOW.setWindowIcon(icon)
        WOW.setAutoFillBackground(True)
        WOW.setSizeGripEnabled(True)
        self.MainWindow = QtWidgets.QTabWidget(WOW)
        self.MainWindow.setEnabled(True)
        self.MainWindow.setGeometry(QtCore.QRect(0, 0, 491, 511))
        self.MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.MainWindow.setAutoFillBackground(True)
        self.MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Argentina))
        self.MainWindow.setDocumentMode(False)
        self.MainWindow.setObjectName("MainWindow")
        self.Inicio = QtWidgets.QWidget()
        self.Inicio.setObjectName("Inicio")
        self.layoutWidget = QtWidgets.QWidget(self.Inicio)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 481, 481))
        self.layoutWidget.setObjectName("layoutWidget")
        self.Iniciolayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.Iniciolayout.setContentsMargins(0, 0, 0, 0)
        self.Iniciolayout.setObjectName("Iniciolayout")
        self.logoWOW = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logoWOW.sizePolicy().hasHeightForWidth())
        self.logoWOW.setSizePolicy(sizePolicy)
        self.logoWOW.setText("")
        self.logoWOW.setPixmap(QtGui.QPixmap("wowlogo5.png"))
        self.logoWOW.setAlignment(QtCore.Qt.AlignCenter)
        self.logoWOW.setObjectName("logoWOW")
        self.Iniciolayout.addWidget(self.logoWOW)
        self.titulo = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.titulo.setFont(font)
        self.titulo.setTextFormat(QtCore.Qt.RichText)
        self.titulo.setScaledContents(True)
        self.titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.titulo.setOpenExternalLinks(False)
        self.titulo.setObjectName("titulo")
        self.Iniciolayout.addWidget(self.titulo)
        self.creadopor = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.creadopor.setFont(font)
        self.creadopor.setAlignment(QtCore.Qt.AlignCenter)
        self.creadopor.setObjectName("creadopor")
        self.Iniciolayout.addWidget(self.creadopor)
        self.dequetrata = QtWidgets.QLabel(self.layoutWidget)
        self.dequetrata.setAlignment(QtCore.Qt.AlignCenter)
        self.dequetrata.setWordWrap(True)
        self.dequetrata.setObjectName("dequetrata")
        self.Iniciolayout.addWidget(self.dequetrata)
        self.MainWindow.addTab(self.Inicio, "")
        self.Backup = QtWidgets.QWidget()
        self.Backup.setObjectName("Backup")
        self.formLayoutWidget = QtWidgets.QWidget(self.Backup)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 120, 471, 121))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.Backform = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.Backform.setContentsMargins(0, 0, 0, 0)
        self.Backform.setObjectName("Backform")
        self.hacerbackupLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.hacerbackupLabel.setObjectName("hacerbackupLabel")
        self.Backform.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.hacerbackupLabel)
        self.hacerbackupCheckBox = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.hacerbackupCheckBox.setChecked(True)
        self.hacerbackupCheckBox.setObjectName("hacerbackupCheckBox")
        self.Backform.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.hacerbackupCheckBox)
        self.nombreDelArchivoLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.nombreDelArchivoLabel.setObjectName("nombreDelArchivoLabel")
        self.Backform.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.nombreDelArchivoLabel)
        self.nombreDelArchivoLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.nombreDelArchivoLineEdit.setObjectName("nombreDelArchivoLineEdit")
        self.Backform.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.nombreDelArchivoLineEdit)
        self.formatoLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.formatoLabel.setObjectName("formatoLabel")
        self.Backform.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.formatoLabel)
        self.formatoselect = QtWidgets.QComboBox(self.formLayoutWidget)
        self.formatoselect.setDuplicatesEnabled(False)
        self.formatoselect.setObjectName("formatoselect")
        self.Backform.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.formatoselect)
        self.EXPLICACIONBACKUP = QtWidgets.QLabel(self.Backup)
        self.EXPLICACIONBACKUP.setGeometry(QtCore.QRect(10, 10, 471, 71))
        self.EXPLICACIONBACKUP.setTextFormat(QtCore.Qt.RichText)
        self.EXPLICACIONBACKUP.setScaledContents(True)
        self.EXPLICACIONBACKUP.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.EXPLICACIONBACKUP.setWordWrap(True)
        self.EXPLICACIONBACKUP.setObjectName("EXPLICACIONBACKUP")
        self.pathcarpeta = QtWidgets.QLineEdit(self.Backup)
        self.pathcarpeta.setGeometry(QtCore.QRect(10, 250, 321, 23))
        self.pathcarpeta.setObjectName("pathcarpeta")
        self.navegarselectcarpeta = QtWidgets.QPushButton(self.Backup)
        self.navegarselectcarpeta.setGeometry(QtCore.QRect(340, 250, 141, 23))
        self.navegarselectcarpeta.setObjectName("navegarselectcarpeta")
        self.liniaseparadorabackup = QtWidgets.QFrame(self.Backup)
        self.liniaseparadorabackup.setGeometry(QtCore.QRect(10, 90, 471, 20))
        self.liniaseparadorabackup.setFrameShape(QtWidgets.QFrame.HLine)
        self.liniaseparadorabackup.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.liniaseparadorabackup.setObjectName("liniaseparadorabackup")
        self.Carpetaselecttext = QtWidgets.QLabel(self.Backup)
        self.Carpetaselecttext.setGeometry(QtCore.QRect(10, 220, 401, 16))
        self.Carpetaselecttext.setObjectName("Carpetaselecttext")
        self.MainWindow.addTab(self.Backup, "")
        self.Reduccion = QtWidgets.QWidget()
        self.Reduccion.setObjectName("Reduccion")
        self.label_reducexplicacion = QtWidgets.QLabel(self.Reduccion)
        self.label_reducexplicacion.setGeometry(QtCore.QRect(10, 10, 461, 31))
        self.label_reducexplicacion.setTextFormat(QtCore.Qt.RichText)
        self.label_reducexplicacion.setWordWrap(True)
        self.label_reducexplicacion.setObjectName("label_reducexplicacion")
        self.line = QtWidgets.QFrame(self.Reduccion)
        self.line.setGeometry(QtCore.QRect(10, 50, 461, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.Reducircheck = QtWidgets.QCheckBox(self.Reduccion)
        self.Reducircheck.setGeometry(QtCore.QRect(10, 70, 451, 21))
        self.Reducircheck.setTristate(False)
        self.Reducircheck.setObjectName("Reducircheck")
        self.hacereldark = QtWidgets.QCheckBox(self.Reduccion)
        self.hacereldark.setEnabled(False)
        self.hacereldark.setGeometry(QtCore.QRect(10, 190, 451, 21))
        self.hacereldark.setAutoRepeatDelay(304)
        self.hacereldark.setTristate(False)
        self.hacereldark.setProperty("ifreduc", True)
        self.hacereldark.setObjectName("hacereldark")
        self.editdark = QtWidgets.QLineEdit(self.Reduccion)
        self.editdark.setEnabled(False)
        self.editdark.setGeometry(QtCore.QRect(80, 220, 261, 23))
        self.editdark.setText("")
        self.editdark.setProperty("ifreduc", True)
        self.editdark.setObjectName("editdark")
        self.label_dark = QtWidgets.QLabel(self.Reduccion)
        self.label_dark.setEnabled(False)
        self.label_dark.setGeometry(QtCore.QRect(10, 220, 71, 21))
        self.label_dark.setObjectName("label_dark")
        self.pushButton_fdarks = QtWidgets.QPushButton(self.Reduccion)
        self.pushButton_fdarks.setEnabled(False)
        self.pushButton_fdarks.setGeometry(QtCore.QRect(350, 220, 61, 23))
        self.pushButton_fdarks.setObjectName("pushButton_fdarks")
        self.labelfilterfieldexpl = QtWidgets.QLabel(self.Reduccion)
        self.labelfilterfieldexpl.setEnabled(False)
        self.labelfilterfieldexpl.setGeometry(QtCore.QRect(10, 380, 461, 61))
        self.labelfilterfieldexpl.setTextFormat(QtCore.Qt.RichText)
        self.labelfilterfieldexpl.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.labelfilterfieldexpl.setWordWrap(True)
        self.labelfilterfieldexpl.setObjectName("labelfilterfieldexpl")
        self.lineEdit_keyword = QtWidgets.QLineEdit(self.Reduccion)
        self.lineEdit_keyword.setEnabled(False)
        self.lineEdit_keyword.setGeometry(QtCore.QRect(80, 450, 391, 23))
        self.lineEdit_keyword.setProperty("ifreduc", True)
        self.lineEdit_keyword.setObjectName("lineEdit_keyword")
        self.label_keyword = QtWidgets.QLabel(self.Reduccion)
        self.label_keyword.setEnabled(False)
        self.label_keyword.setGeometry(QtCore.QRect(10, 450, 71, 21))
        self.label_keyword.setObjectName("label_keyword")
        self.line_3 = QtWidgets.QFrame(self.Reduccion)
        self.line_3.setGeometry(QtCore.QRect(10, 350, 451, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.groupreduc = QtWidgets.QGroupBox(self.Reduccion)
        self.groupreduc.setEnabled(False)
        self.groupreduc.setGeometry(QtCore.QRect(10, 82, 461, 101))
        self.groupreduc.setObjectName("groupreduc")
        self.gridReduc = QtWidgets.QGridLayout(self.groupreduc)
        self.gridReduc.setObjectName("gridReduc")
        self.label_imagenes = QtWidgets.QLabel(self.groupreduc)
        self.label_imagenes.setObjectName("label_imagenes")
        self.gridReduc.addWidget(self.label_imagenes, 0, 0, 1, 1)
        self.lineedit_obj = QtWidgets.QLineEdit(self.groupreduc)
        self.lineedit_obj.setProperty("ifreduc", True)
        self.lineedit_obj.setObjectName("lineedit_obj")
        self.gridReduc.addWidget(self.lineedit_obj, 0, 1, 1, 1)
        self.pushButton_obj = QtWidgets.QPushButton(self.groupreduc)
        self.pushButton_obj.setObjectName("pushButton_obj")
        self.gridReduc.addWidget(self.pushButton_obj, 0, 2, 1, 1)
        self.label_bias = QtWidgets.QLabel(self.groupreduc)
        self.label_bias.setObjectName("label_bias")
        self.gridReduc.addWidget(self.label_bias, 1, 0, 1, 1)
        self.lineEdit_bias = QtWidgets.QLineEdit(self.groupreduc)
        self.lineEdit_bias.setProperty("ifreduc", True)
        self.lineEdit_bias.setObjectName("lineEdit_bias")
        self.gridReduc.addWidget(self.lineEdit_bias, 1, 1, 1, 1)
        self.pushButton_bias = QtWidgets.QPushButton(self.groupreduc)
        self.pushButton_bias.setObjectName("pushButton_bias")
        self.gridReduc.addWidget(self.pushButton_bias, 1, 2, 1, 1)
        self.label_flat = QtWidgets.QLabel(self.groupreduc)
        self.label_flat.setObjectName("label_flat")
        self.gridReduc.addWidget(self.label_flat, 2, 0, 1, 1)
        self.lineEdit_flats = QtWidgets.QLineEdit(self.groupreduc)
        self.lineEdit_flats.setProperty("ifreduc", True)
        self.lineEdit_flats.setObjectName("lineEdit_flats")
        self.gridReduc.addWidget(self.lineEdit_flats, 2, 1, 1, 1)
        self.pushButton_flats = QtWidgets.QPushButton(self.groupreduc)
        self.pushButton_flats.setObjectName("pushButton_flats")
        self.gridReduc.addWidget(self.pushButton_flats, 2, 2, 1, 1)
        self.line_6 = QtWidgets.QFrame(self.Reduccion)
        self.line_6.setGeometry(QtCore.QRect(10, 250, 451, 20))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.Reduccion)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 270, 451, 80))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.trimoverscangroup = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.trimoverscangroup.setContentsMargins(0, 0, 0, 0)
        self.trimoverscangroup.setObjectName("trimoverscangroup")
        self.secciNDeTrimmingLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.secciNDeTrimmingLabel.setEnabled(False)
        self.secciNDeTrimmingLabel.setObjectName("secciNDeTrimmingLabel")
        self.trimoverscangroup.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.secciNDeTrimmingLabel)
        self.secciNDeTrimmingLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.secciNDeTrimmingLineEdit.setEnabled(False)
        self.secciNDeTrimmingLineEdit.setObjectName("secciNDeTrimmingLineEdit")
        self.trimoverscangroup.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.secciNDeTrimmingLineEdit)
        self.secciNDeOverscanLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.secciNDeOverscanLabel.setEnabled(False)
        self.secciNDeOverscanLabel.setObjectName("secciNDeOverscanLabel")
        self.trimoverscangroup.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.secciNDeOverscanLabel)
        self.secciNDeOverscanLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.secciNDeOverscanLineEdit.setEnabled(False)
        self.secciNDeOverscanLineEdit.setObjectName("secciNDeOverscanLineEdit")
        self.trimoverscangroup.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.secciNDeOverscanLineEdit)
        self.sinosedea = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.sinosedea.setEnabled(False)
        self.sinosedea.setTextFormat(QtCore.Qt.RichText)
        self.sinosedea.setObjectName("sinosedea")
        self.trimoverscangroup.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.sinosedea)
        self.MainWindow.addTab(self.Reduccion, "")
        self.fotometria = QtWidgets.QWidget()
        self.fotometria.setObjectName("fotometria")
        self.label_fotometria_explicacion = QtWidgets.QLabel(self.fotometria)
        self.label_fotometria_explicacion.setGeometry(QtCore.QRect(10, 10, 471, 101))
        self.label_fotometria_explicacion.setTextFormat(QtCore.Qt.RichText)
        self.label_fotometria_explicacion.setWordWrap(True)
        self.label_fotometria_explicacion.setObjectName("label_fotometria_explicacion")
        self.line_4 = QtWidgets.QFrame(self.fotometria)
        self.line_4.setGeometry(QtCore.QRect(10, 99, 461, 41))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.scrollArea = QtWidgets.QScrollArea(self.fotometria)
        self.scrollArea.setGeometry(QtCore.QRect(10, 120, 471, 361))
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 457, 490))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Doph_2 = QtWidgets.QGridLayout()
        self.Doph_2.setObjectName("Doph_2")
        self.hacerphotlabel_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.hacerphotlabel_2.setObjectName("hacerphotlabel_2")
        self.Doph_2.addWidget(self.hacerphotlabel_2, 0, 0, 1, 1)
        self.hacerphot_2 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.hacerphot_2.setObjectName("hacerphot_2")
        self.Doph_2.addWidget(self.hacerphot_2, 0, 1, 1, 1)
        self.imageneslabel_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.imageneslabel_2.setEnabled(False)
        self.imageneslabel_2.setObjectName("imageneslabel_2")
        self.Doph_2.addWidget(self.imageneslabel_2, 1, 0, 1, 1)
        self.imagenesedit_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.imagenesedit_2.setEnabled(False)
        self.imagenesedit_2.setObjectName("imagenesedit_2")
        self.Doph_2.addWidget(self.imagenesedit_2, 1, 1, 1, 1)
        self.findphots_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.findphots_2.setEnabled(False)
        self.findphots_2.setObjectName("findphots_2")
        self.Doph_2.addWidget(self.findphots_2, 1, 2, 1, 1)
        self.buscestrelabel_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.buscestrelabel_2.setEnabled(False)
        self.buscestrelabel_2.setObjectName("buscestrelabel_2")
        self.Doph_2.addWidget(self.buscestrelabel_2, 2, 0, 1, 1)
        self.buscestre_2 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.buscestre_2.setEnabled(False)
        self.buscestre_2.setChecked(True)
        self.buscestre_2.setTristate(False)
        self.buscestre_2.setObjectName("buscestre_2")
        self.Doph_2.addWidget(self.buscestre_2, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.Doph_2)
        self.grupobuscestrellas_2 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.grupobuscestrellas_2.setEnabled(False)
        self.grupobuscestrellas_2.setObjectName("grupobuscestrellas_2")
        self.gridLayout = QtWidgets.QGridLayout(self.grupobuscestrellas_2)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.ruidoDeCieloLabel_2 = QtWidgets.QLabel(self.grupobuscestrellas_2)
        self.ruidoDeCieloLabel_2.setEnabled(False)
        self.ruidoDeCieloLabel_2.setObjectName("ruidoDeCieloLabel_2")
        self.gridLayout.addWidget(self.ruidoDeCieloLabel_2, 1, 2, 1, 1)
        self.calcularFWHMCheckBox_2 = QtWidgets.QCheckBox(self.grupobuscestrellas_2)
        self.calcularFWHMCheckBox_2.setChecked(True)
        self.calcularFWHMCheckBox_2.setObjectName("calcularFWHMCheckBox_2")
        self.gridLayout.addWidget(self.calcularFWHMCheckBox_2, 0, 1, 1, 1)
        self.calcularRuidoDelCieloCheckBox_2 = QtWidgets.QCheckBox(self.grupobuscestrellas_2)
        self.calcularRuidoDelCieloCheckBox_2.setChecked(True)
        self.calcularRuidoDelCieloCheckBox_2.setObjectName("calcularRuidoDelCieloCheckBox_2")
        self.gridLayout.addWidget(self.calcularRuidoDelCieloCheckBox_2, 1, 1, 1, 1)
        self.calcularRuidoDelCieloLabel_2 = QtWidgets.QLabel(self.grupobuscestrellas_2)
        self.calcularRuidoDelCieloLabel_2.setObjectName("calcularRuidoDelCieloLabel_2")
        self.gridLayout.addWidget(self.calcularRuidoDelCieloLabel_2, 1, 0, 1, 1)
        self.fWHMLabel_2 = QtWidgets.QLabel(self.grupobuscestrellas_2)
        self.fWHMLabel_2.setEnabled(False)
        self.fWHMLabel_2.setObjectName("fWHMLabel_2")
        self.gridLayout.addWidget(self.fWHMLabel_2, 0, 2, 1, 1)
        self.calcularFWHMLabel_2 = QtWidgets.QLabel(self.grupobuscestrellas_2)
        self.calcularFWHMLabel_2.setObjectName("calcularFWHMLabel_2")
        self.gridLayout.addWidget(self.calcularFWHMLabel_2, 0, 0, 1, 1)
        self.fWHMLineEdit_2 = QtWidgets.QLineEdit(self.grupobuscestrellas_2)
        self.fWHMLineEdit_2.setEnabled(False)
        self.fWHMLineEdit_2.setObjectName("fWHMLineEdit_2")
        self.gridLayout.addWidget(self.fWHMLineEdit_2, 0, 3, 1, 1)
        self.ruidoDeCieloLineEdit_2 = QtWidgets.QLineEdit(self.grupobuscestrellas_2)
        self.ruidoDeCieloLineEdit_2.setEnabled(False)
        self.ruidoDeCieloLineEdit_2.setObjectName("ruidoDeCieloLineEdit_2")
        self.gridLayout.addWidget(self.ruidoDeCieloLineEdit_2, 1, 3, 1, 1)
        self.verticalLayout.addWidget(self.grupobuscestrellas_2)
        self.grouptres_2 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.grouptres_2.setEnabled(False)
        self.grouptres_2.setObjectName("grouptres_2")
        self.tR_2 = QtWidgets.QGridLayout(self.grouptres_2)
        self.tR_2.setObjectName("tR_2")
        self.trlabel_2 = QtWidgets.QLabel(self.grouptres_2)
        self.trlabel_2.setObjectName("trlabel_2")
        self.tR_2.addWidget(self.trlabel_2, 0, 0, 1, 1)
        self.trinput_2 = QtWidgets.QLineEdit(self.grouptres_2)
        self.trinput_2.setObjectName("trinput_2")
        self.tR_2.addWidget(self.trinput_2, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.grouptres_2)
        self.groupcords_2 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupcords_2.setObjectName("groupcords_2")
        self.Coord_2 = QtWidgets.QGridLayout(self.groupcords_2)
        self.Coord_2.setObjectName("Coord_2")
        self.coordenadasLabel_2 = QtWidgets.QLabel(self.groupcords_2)
        self.coordenadasLabel_2.setEnabled(False)
        self.coordenadasLabel_2.setObjectName("coordenadasLabel_2")
        self.Coord_2.addWidget(self.coordenadasLabel_2, 0, 0, 1, 1)
        self.coordenadasLineEdit_2 = QtWidgets.QLineEdit(self.groupcords_2)
        self.coordenadasLineEdit_2.setEnabled(False)
        self.coordenadasLineEdit_2.setObjectName("coordenadasLineEdit_2")
        self.Coord_2.addWidget(self.coordenadasLineEdit_2, 0, 1, 1, 1)
        self.buscarcoordenadas_2 = QtWidgets.QPushButton(self.groupcords_2)
        self.buscarcoordenadas_2.setEnabled(False)
        self.buscarcoordenadas_2.setObjectName("buscarcoordenadas_2")
        self.Coord_2.addWidget(self.buscarcoordenadas_2, 0, 2, 1, 1)
        self.verticalLayout.addWidget(self.groupcords_2)
        self.groupannulus_2 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupannulus_2.setEnabled(False)
        self.groupannulus_2.setObjectName("groupannulus_2")
        self.ANNDANN_2 = QtWidgets.QGridLayout(self.groupannulus_2)
        self.ANNDANN_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.ANNDANN_2.setObjectName("ANNDANN_2")
        self.annulusLabel_2 = QtWidgets.QLabel(self.groupannulus_2)
        self.annulusLabel_2.setObjectName("annulusLabel_2")
        self.ANNDANN_2.addWidget(self.annulusLabel_2, 0, 0, 1, 1)
        self.annulusLineEdit_2 = QtWidgets.QLineEdit(self.groupannulus_2)
        self.annulusLineEdit_2.setObjectName("annulusLineEdit_2")
        self.ANNDANN_2.addWidget(self.annulusLineEdit_2, 0, 1, 1, 1)
        self.dannulusLabel_2 = QtWidgets.QLabel(self.groupannulus_2)
        self.dannulusLabel_2.setObjectName("dannulusLabel_2")
        self.ANNDANN_2.addWidget(self.dannulusLabel_2, 0, 2, 1, 1)
        self.dannulusLineEdit_2 = QtWidgets.QLineEdit(self.groupannulus_2)
        self.dannulusLineEdit_2.setObjectName("dannulusLineEdit_2")
        self.ANNDANN_2.addWidget(self.dannulusLineEdit_2, 0, 3, 1, 1)
        self.verticalLayout.addWidget(self.groupannulus_2)
        self.groupapertura_2 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupapertura_2.setEnabled(False)
        self.groupapertura_2.setObjectName("groupapertura_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupapertura_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.apertexplicacion_2 = QtWidgets.QLabel(self.groupapertura_2)
        self.apertexplicacion_2.setObjectName("apertexplicacion_2")
        self.gridLayout_3.addWidget(self.apertexplicacion_2, 0, 0, 1, 4)
        self.aperturaAtumTicaLabel_2 = QtWidgets.QLabel(self.groupapertura_2)
        self.aperturaAtumTicaLabel_2.setObjectName("aperturaAtumTicaLabel_2")
        self.gridLayout_3.addWidget(self.aperturaAtumTicaLabel_2, 1, 0, 1, 1)
        self.aperturaAtumTicaCheckBox_2 = QtWidgets.QCheckBox(self.groupapertura_2)
        self.aperturaAtumTicaCheckBox_2.setChecked(True)
        self.aperturaAtumTicaCheckBox_2.setObjectName("aperturaAtumTicaCheckBox_2")
        self.gridLayout_3.addWidget(self.aperturaAtumTicaCheckBox_2, 1, 1, 1, 1)
        self.aperturaLabel_2 = QtWidgets.QLabel(self.groupapertura_2)
        self.aperturaLabel_2.setEnabled(False)
        self.aperturaLabel_2.setObjectName("aperturaLabel_2")
        self.gridLayout_3.addWidget(self.aperturaLabel_2, 1, 2, 1, 1)
        self.aperturaLineEdit_2 = QtWidgets.QLineEdit(self.groupapertura_2)
        self.aperturaLineEdit_2.setEnabled(False)
        self.aperturaLineEdit_2.setObjectName("aperturaLineEdit_2")
        self.gridLayout_3.addWidget(self.aperturaLineEdit_2, 1, 3, 1, 1)
        self.verticalLayout.addWidget(self.groupapertura_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.MainWindow.addTab(self.fotometria, "")
        self.Tablas = QtWidgets.QWidget()
        self.Tablas.setObjectName("Tablas")
        self.grouptablas = QtWidgets.QGroupBox(self.Tablas)
        self.grouptablas.setEnabled(False)
        self.grouptablas.setGeometry(QtCore.QRect(10, 130, 461, 141))
        self.grouptablas.setObjectName("grouptablas")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.grouptablas)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tablasPhotLabel = QtWidgets.QLabel(self.grouptablas)
        self.tablasPhotLabel.setObjectName("tablasPhotLabel")
        self.gridLayout_2.addWidget(self.tablasPhotLabel, 0, 0, 1, 1)
        self.tablasPhotLineEdit = QtWidgets.QLineEdit(self.grouptablas)
        self.tablasPhotLineEdit.setObjectName("tablasPhotLineEdit")
        self.gridLayout_2.addWidget(self.tablasPhotLineEdit, 0, 1, 1, 1)
        self.navegartablasphot = QtWidgets.QPushButton(self.grouptablas)
        self.navegartablasphot.setObjectName("navegartablasphot")
        self.gridLayout_2.addWidget(self.navegartablasphot, 0, 2, 1, 1)
        self.formatoDeSalidaComboBox = QtWidgets.QComboBox(self.grouptablas)
        self.formatoDeSalidaComboBox.setObjectName("formatoDeSalidaComboBox")
        self.gridLayout_2.addWidget(self.formatoDeSalidaComboBox, 2, 1, 1, 2)
        self.esquemaLabel = QtWidgets.QLabel(self.grouptablas)
        self.esquemaLabel.setObjectName("esquemaLabel")
        self.gridLayout_2.addWidget(self.esquemaLabel, 1, 0, 1, 1)
        self.esquemaComboBox = QtWidgets.QComboBox(self.grouptablas)
        self.esquemaComboBox.setObjectName("esquemaComboBox")
        self.gridLayout_2.addWidget(self.esquemaComboBox, 1, 1, 1, 2)
        self.formatoDeSalidaLabel = QtWidgets.QLabel(self.grouptablas)
        self.formatoDeSalidaLabel.setObjectName("formatoDeSalidaLabel")
        self.gridLayout_2.addWidget(self.formatoDeSalidaLabel, 2, 0, 1, 1)
        self.explicaciontablas = QtWidgets.QLabel(self.Tablas)
        self.explicaciontablas.setGeometry(QtCore.QRect(10, 10, 461, 101))
        self.explicaciontablas.setTextFormat(QtCore.Qt.RichText)
        self.explicaciontablas.setWordWrap(True)
        self.explicaciontablas.setObjectName("explicaciontablas")
        self.line_5 = QtWidgets.QFrame(self.Tablas)
        self.line_5.setGeometry(QtCore.QRect(10, 110, 461, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.hacerTablaCheckBox = QtWidgets.QCheckBox(self.Tablas)
        self.hacerTablaCheckBox.setGeometry(QtCore.QRect(130, 130, 233, 15))
        self.hacerTablaCheckBox.setChecked(False)
        self.hacerTablaCheckBox.setObjectName("hacerTablaCheckBox")
        self.hacerTablaLabel = QtWidgets.QLabel(self.Tablas)
        self.hacerTablaLabel.setGeometry(QtCore.QRect(16, 130, 108, 15))
        self.hacerTablaLabel.setObjectName("hacerTablaLabel")
        self.MainWindow.addTab(self.Tablas, "")
        self.layoutWidget1 = QtWidgets.QWidget(WOW)
        self.layoutWidget1.setGeometry(QtCore.QRect(160, 520, 331, 31))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.buttons = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.buttons.setContentsMargins(0, 0, 0, 0)
        self.buttons.setObjectName("buttons")
        self.Save = QtWidgets.QPushButton(self.layoutWidget1)
        self.Save.setObjectName("Save")
        self.buttons.addWidget(self.Save)
        self.Run = QtWidgets.QPushButton(self.layoutWidget1)
        self.Run.setObjectName("Run")
        self.buttons.addWidget(self.Run)
        self.Close = QtWidgets.QPushButton(self.layoutWidget1)
        self.Close.setObjectName("Close")
        self.buttons.addWidget(self.Close)

        self.retranslateUi(WOW)
        self.MainWindow.setCurrentIndex(0)
        self.formatoselect.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(WOW)

    def retranslateUi(self, WOW):
        _translate = QtCore.QCoreApplication.translate
        WOW.setWindowTitle(_translate("WOW", "WOW"))
        self.titulo.setText(_translate("WOW", "Wow Observational Work 1.1"))
        self.creadopor.setText(_translate("WOW", "Creado por Tomás Regna y Natalia Guevara"))
        self.dequetrata.setText(_translate("WOW", "Programa destinado a realizar la reducción de imágenes fotométricas, el backup de archivos, la fotometría de apertura estelar y la estilización de tablas daophot para los telescopios HSH y JS de CASLEO."))
        self.MainWindow.setTabText(self.MainWindow.indexOf(self.Inicio), _translate("WOW", "Inicio"))
        self.hacerbackupLabel.setText(_translate("WOW", "Hacer backup"))
        self.nombreDelArchivoLabel.setText(_translate("WOW", "Nombre del archivo comprimido"))
        self.formatoLabel.setText(_translate("WOW", "Formato de compresión"))
        self.EXPLICACIONBACKUP.setText(_translate("WOW", "Podrá realizarse un backup de todos los archivos contenidos en una carpeta, recomendamos dejar esta opción habilitada. Los backup serán guardados en la carpeta \"Backup\" en el home de su usuario. El nombre del archivo es opcional, de no indicarse se usará uno con la fecha actual."))
        self.navegarselectcarpeta.setText(_translate("WOW", "Navegar"))
        self.Carpetaselecttext.setText(_translate("WOW", "Carpeta a la cual realizar el backup:"))
        self.MainWindow.setTabText(self.MainWindow.indexOf(self.Backup), _translate("WOW", "Backup"))
        self.label_reducexplicacion.setText(_translate("WOW", "Se realizará la reducción fotométrica de las imágenes ingresadas. Por defecto se agegará una \"R\" a las imágenes ya reducidas."))
        self.Reducircheck.setText(_translate("WOW", "Hacer reducción de imágenes"))
        self.hacereldark.setText(_translate("WOW", "Hacer corrección por dark"))
        self.label_dark.setText(_translate("WOW", "Dark"))
        self.pushButton_fdarks.setText(_translate("WOW", "Navegar"))
        self.labelfilterfieldexpl.setText(_translate("WOW", "Este software considera que la información de los filtros en el header de la imágen se encuentra en el formato usado en CASLEO (\"FILTER01\" y \"FILTER02\"), de no ser así indicar el keyword que contiene estos datos. Este Keyword debera usar una letra para indicar el filtro."))
        self.label_keyword.setText(_translate("WOW", "Keyword"))
        self.label_imagenes.setText(_translate("WOW", "Imágenes"))
        self.pushButton_obj.setText(_translate("WOW", "Navegar"))
        self.label_bias.setText(_translate("WOW", "Bias"))
        self.pushButton_bias.setText(_translate("WOW", "Navegar"))
        self.label_flat.setText(_translate("WOW", "Flats"))
        self.pushButton_flats.setText(_translate("WOW", "Navegar"))
        self.secciNDeTrimmingLabel.setText(_translate("WOW", "Sección de Trimming"))
        self.secciNDeOverscanLabel.setText(_translate("WOW", "Sección de Overscan"))
        self.sinosedea.setText(_translate("WOW", "Si no se desea hacer trim u overscan dejar los campos vacíos."))
        self.MainWindow.setTabText(self.MainWindow.indexOf(self.Reduccion), _translate("WOW", "Reduccion"))
        self.label_fotometria_explicacion.setText(_translate("WOW", "Realiza la fotometría de apertura de una o varias imágenes. Si se indica, correrá un script para identificar estrellas. Dentro del mismo se podrán ingresar los parámetros necesarios u optar por calcularlos automáticamente. La apertura automática toma el valor de 1FWHM y 2FWHM."))
        self.hacerphotlabel_2.setText(_translate("WOW", "Hacer fotometría"))
        self.imageneslabel_2.setText(_translate("WOW", "Imágenes"))
        self.findphots_2.setText(_translate("WOW", "Navegar"))
        self.buscestrelabel_2.setText(_translate("WOW", "Buscar estrellas"))
        self.ruidoDeCieloLabel_2.setText(_translate("WOW", "Ruido de cielo"))
        self.calcularRuidoDelCieloLabel_2.setText(_translate("WOW", "Calcular ruido del cielo"))
        self.fWHMLabel_2.setText(_translate("WOW", "FWHM"))
        self.calcularFWHMLabel_2.setText(_translate("WOW", "Calcular FWHM"))
        self.trlabel_2.setText(_translate("WOW", "Threshold"))
        self.trinput_2.setText(_translate("WOW", "4"))
        self.coordenadasLabel_2.setText(_translate("WOW", "Coordenadas"))
        self.buscarcoordenadas_2.setText(_translate("WOW", "Navegar"))
        self.annulusLabel_2.setText(_translate("WOW", "Annulus"))
        self.dannulusLabel_2.setText(_translate("WOW", "Dannulus"))
        self.apertexplicacion_2.setText(_translate("WOW", "La apertura debe ingresarse en el formato de IRAF"))
        self.aperturaAtumTicaLabel_2.setText(_translate("WOW", "Apertura automática"))
        self.aperturaLabel_2.setText(_translate("WOW", "Apertura"))
        self.MainWindow.setTabText(self.MainWindow.indexOf(self.fotometria), _translate("WOW", "Fotometría"))
        self.tablasPhotLabel.setText(_translate("WOW", "Tablas phot"))
        self.navegartablasphot.setText(_translate("WOW", "Navegar"))
        self.esquemaLabel.setText(_translate("WOW", "Esquema"))
        self.formatoDeSalidaLabel.setText(_translate("WOW", "Formato de salida"))
        self.explicaciontablas.setText(_translate("WOW", "Ingresando una o varias tablas del formato por defecto de daophot, se generarán tablas con un esquema a seleccionar, en el formato que se indique. Los esquemas disponibles serán \"imagen\", una tabla por imagen que contenga en cada linea información de cada estrella, o \"estrella\" una tabla por cada estrella donde cada linea contiene información según el radio de apertura."))
        self.hacerTablaLabel.setText(_translate("WOW", "Hacer tabla"))
        self.MainWindow.setTabText(self.MainWindow.indexOf(self.Tablas), _translate("WOW", "Tablas"))
        self.Save.setText(_translate("WOW", "Guardar"))
        self.Run.setText(_translate("WOW", "Guardar y Correr"))
        self.Close.setText(_translate("WOW", "Cerrar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WOW = QtWidgets.QDialog()
    ui = Ui_WOW()
    ui.setupUi(WOW)
    WOW.show()
    sys.exit(app.exec_())

