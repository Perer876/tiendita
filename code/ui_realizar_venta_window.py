# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'realizar_venta_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_realizar_venta_window(object):
    def setupUi(self, realizar_venta_window):
        if not realizar_venta_window.objectName():
            realizar_venta_window.setObjectName(u"realizar_venta_window")
        realizar_venta_window.resize(1090, 771)
        icon = QIcon()
        icon.addFile(u":/images/001-cart.png", QSize(), QIcon.Normal, QIcon.Off)
        realizar_venta_window.setWindowIcon(icon)
        self.centralwidget = QWidget(realizar_venta_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(30, 180, 1031, 351))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 550, 61, 41))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(100, 550, 201, 51))
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 90, 1071, 71))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 25, 101, 21))
        self.buscar_producto_por_comboBox = QComboBox(self.frame_3)
        self.buscar_producto_por_comboBox.setObjectName(u"buscar_producto_por_comboBox")
        self.buscar_producto_por_comboBox.setGeometry(QRect(120, 21, 211, 31))
        self.termino_producto_lineEdit = QLineEdit(self.frame_3)
        self.termino_producto_lineEdit.setObjectName(u"termino_producto_lineEdit")
        self.termino_producto_lineEdit.setGeometry(QRect(350, 20, 511, 31))
        self.buscar_producto_pushButton = QPushButton(self.frame_3)
        self.buscar_producto_pushButton.setObjectName(u"buscar_producto_pushButton")
        self.buscar_producto_pushButton.setGeometry(QRect(880, 20, 171, 31))
        icon1 = QIcon()
        icon1.addFile(u":/images/019-bookmark.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buscar_producto_pushButton.setIcon(icon1)
        self.buscar_producto_pushButton.setIconSize(QSize(25, 25))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 1031, 41))
        self.buscar_producto_pushButton_2 = QPushButton(self.centralwidget)
        self.buscar_producto_pushButton_2.setObjectName(u"buscar_producto_pushButton_2")
        self.buscar_producto_pushButton_2.setGeometry(QRect(350, 620, 171, 61))
        icon2 = QIcon()
        icon2.addFile(u":/images/020-cart.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buscar_producto_pushButton_2.setIcon(icon2)
        self.buscar_producto_pushButton_2.setIconSize(QSize(50, 50))
        self.buscar_producto_pushButton_3 = QPushButton(self.centralwidget)
        self.buscar_producto_pushButton_3.setObjectName(u"buscar_producto_pushButton_3")
        self.buscar_producto_pushButton_3.setGeometry(QRect(540, 620, 171, 61))
        icon3 = QIcon()
        icon3.addFile(u":/images/028-cart.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buscar_producto_pushButton_3.setIcon(icon3)
        self.buscar_producto_pushButton_3.setIconSize(QSize(50, 50))
        self.eliminar_producto_pushButton_2 = QPushButton(self.centralwidget)
        self.eliminar_producto_pushButton_2.setObjectName(u"eliminar_producto_pushButton_2")
        self.eliminar_producto_pushButton_2.setGeometry(QRect(890, 540, 171, 31))
        icon4 = QIcon()
        icon4.addFile(u":/images/014-bookmark-5.png", QSize(), QIcon.Normal, QIcon.Off)
        self.eliminar_producto_pushButton_2.setIcon(icon4)
        self.eliminar_producto_pushButton_2.setIconSize(QSize(25, 25))
        realizar_venta_window.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(realizar_venta_window)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1090, 26))
        realizar_venta_window.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(realizar_venta_window)
        self.statusbar.setObjectName(u"statusbar")
        realizar_venta_window.setStatusBar(self.statusbar)

        self.retranslateUi(realizar_venta_window)

        QMetaObject.connectSlotsByName(realizar_venta_window)
    # setupUi

    def retranslateUi(self, realizar_venta_window):
        realizar_venta_window.setWindowTitle(QCoreApplication.translate("realizar_venta_window", u"Realizar Venta", None))
        self.label_4.setText(QCoreApplication.translate("realizar_venta_window", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Total:</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("realizar_venta_window", u"<html><head/><body><p><span style=\" font-size:24pt;\">$0</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("realizar_venta_window", u"<html><head/><body><p><span style=\" font-size:10pt;\">Agregar por:</span></p></body></html>", None))
        self.buscar_producto_pushButton.setText(QCoreApplication.translate("realizar_venta_window", u"Agregar producto", None))
        self.label.setText(QCoreApplication.translate("realizar_venta_window", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Realizar Venta</span></p></body></html>", None))
        self.buscar_producto_pushButton_2.setText(QCoreApplication.translate("realizar_venta_window", u"Finalizar Venta", None))
        self.buscar_producto_pushButton_3.setText(QCoreApplication.translate("realizar_venta_window", u"Cancelar", None))
        self.eliminar_producto_pushButton_2.setText(QCoreApplication.translate("realizar_venta_window", u"Eliminar producto", None))
    # retranslateUi

