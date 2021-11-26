# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'editar_producto_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_editar_producto_window(object):
    def setupUi(self, editar_producto_window):
        if not editar_producto_window.objectName():
            editar_producto_window.setObjectName(u"editar_producto_window")
        editar_producto_window.resize(591, 466)
        icon = QIcon()
        icon.addFile(u":/images/040-clothes.png", QSize(), QIcon.Normal, QIcon.Off)
        editar_producto_window.setWindowIcon(icon)
        self.centralwidget = QWidget(editar_producto_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 531, 41))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(30, 110, 531, 31))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(190, 340, 93, 28))
        self.doubleSpinBox = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setGeometry(QRect(30, 190, 531, 31))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 80, 71, 21))
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(30, 270, 531, 31))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 240, 71, 21))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 160, 71, 21))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(300, 340, 93, 28))
        editar_producto_window.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(editar_producto_window)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 591, 21))
        editar_producto_window.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(editar_producto_window)
        self.statusbar.setObjectName(u"statusbar")
        editar_producto_window.setStatusBar(self.statusbar)

        self.retranslateUi(editar_producto_window)

        QMetaObject.connectSlotsByName(editar_producto_window)
    # setupUi

    def retranslateUi(self, editar_producto_window):
        editar_producto_window.setWindowTitle(QCoreApplication.translate("editar_producto_window", u"Editar Producto", None))
        self.label.setText(QCoreApplication.translate("editar_producto_window", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Modificar Producto</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("editar_producto_window", u"Aceptar", None))
        self.label_2.setText(QCoreApplication.translate("editar_producto_window", u"<html><head/><body><p><span style=\" font-size:10pt;\">Nombre</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("editar_producto_window", u"<html><head/><body><p><span style=\" font-size:10pt;\">C\u00f3digo</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("editar_producto_window", u"<html><head/><body><p><span style=\" font-size:10pt;\">Precio</span></p></body></html>", None))
        self.pushButton_2.setText(QCoreApplication.translate("editar_producto_window", u"Cancelar", None))
    # retranslateUi

