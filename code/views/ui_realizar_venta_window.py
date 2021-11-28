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
        self.venta_tableWidget = QTableWidget(self.centralwidget)
        self.venta_tableWidget.setObjectName(u"venta_tableWidget")
        self.venta_tableWidget.setGeometry(QRect(30, 180, 1031, 351))
        self.venta_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.venta_tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.venta_tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.venta_tableWidget.setGridStyle(Qt.DashLine)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 550, 61, 41))
        self.total_label = QLabel(self.centralwidget)
        self.total_label.setObjectName(u"total_label")
        self.total_label.setGeometry(QRect(100, 550, 201, 51))
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
        font = QFont()
        font.setPointSize(10)
        self.termino_producto_lineEdit.setFont(font)
        self.termino_producto_lineEdit.setClearButtonEnabled(True)
        self.agregar_producto_pushButton = QPushButton(self.frame_3)
        self.agregar_producto_pushButton.setObjectName(u"agregar_producto_pushButton")
        self.agregar_producto_pushButton.setGeometry(QRect(880, 20, 171, 31))
        icon1 = QIcon()
        icon1.addFile(u":/images/020-cart.png", QSize(), QIcon.Normal, QIcon.Off)
        self.agregar_producto_pushButton.setIcon(icon1)
        self.agregar_producto_pushButton.setIconSize(QSize(25, 25))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 1031, 41))
        self.finalizar_venta_pushButton = QPushButton(self.centralwidget)
        self.finalizar_venta_pushButton.setObjectName(u"finalizar_venta_pushButton")
        self.finalizar_venta_pushButton.setGeometry(QRect(350, 620, 171, 61))
        icon2 = QIcon()
        icon2.addFile(u":/images/021-cart.png", QSize(), QIcon.Normal, QIcon.Off)
        self.finalizar_venta_pushButton.setIcon(icon2)
        self.finalizar_venta_pushButton.setIconSize(QSize(50, 50))
        self.cancelar_pushButton = QPushButton(self.centralwidget)
        self.cancelar_pushButton.setObjectName(u"cancelar_pushButton")
        self.cancelar_pushButton.setGeometry(QRect(540, 620, 171, 61))
        icon3 = QIcon()
        icon3.addFile(u":/images/028-cart.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cancelar_pushButton.setIcon(icon3)
        self.cancelar_pushButton.setIconSize(QSize(50, 50))
        self.disminuir_pushButton = QPushButton(self.centralwidget)
        self.disminuir_pushButton.setObjectName(u"disminuir_pushButton")
        self.disminuir_pushButton.setGeometry(QRect(760, 540, 111, 31))
        icon4 = QIcon()
        icon4.addFile(u":/images/014-bookmark-5.png", QSize(), QIcon.Normal, QIcon.Off)
        self.disminuir_pushButton.setIcon(icon4)
        self.disminuir_pushButton.setIconSize(QSize(25, 25))
        self.aumentar_pushButton = QPushButton(self.centralwidget)
        self.aumentar_pushButton.setObjectName(u"aumentar_pushButton")
        self.aumentar_pushButton.setGeometry(QRect(640, 540, 111, 31))
        icon5 = QIcon()
        icon5.addFile(u":/images/019-bookmark.png", QSize(), QIcon.Normal, QIcon.Off)
        self.aumentar_pushButton.setIcon(icon5)
        self.aumentar_pushButton.setIconSize(QSize(25, 25))
        self.eliminar_producto_pushButton = QPushButton(self.centralwidget)
        self.eliminar_producto_pushButton.setObjectName(u"eliminar_producto_pushButton")
        self.eliminar_producto_pushButton.setGeometry(QRect(890, 540, 171, 31))
        icon6 = QIcon()
        icon6.addFile(u":/images/027-cart.png", QSize(), QIcon.Normal, QIcon.Off)
        self.eliminar_producto_pushButton.setIcon(icon6)
        self.eliminar_producto_pushButton.setIconSize(QSize(25, 25))
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
        self.total_label.setText(QCoreApplication.translate("realizar_venta_window", u"<html><head/><body><p><span style=\" font-size:24pt;\">$0</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("realizar_venta_window", u"<html><head/><body><p><span style=\" font-size:10pt;\">Agregar por:</span></p></body></html>", None))
        self.termino_producto_lineEdit.setPlaceholderText(QCoreApplication.translate("realizar_venta_window", u"Termino busqueda", None))
        self.agregar_producto_pushButton.setText(QCoreApplication.translate("realizar_venta_window", u"Agregar producto", None))
        self.label.setText(QCoreApplication.translate("realizar_venta_window", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Realizar Venta</span></p></body></html>", None))
        self.finalizar_venta_pushButton.setText(QCoreApplication.translate("realizar_venta_window", u"Finalizar Venta", None))
        self.cancelar_pushButton.setText(QCoreApplication.translate("realizar_venta_window", u"Cancelar", None))
        self.disminuir_pushButton.setText(QCoreApplication.translate("realizar_venta_window", u"Disminuir", None))
        self.aumentar_pushButton.setText(QCoreApplication.translate("realizar_venta_window", u"Aumentar", None))
        self.eliminar_producto_pushButton.setText(QCoreApplication.translate("realizar_venta_window", u"Eliminar producto", None))
    # retranslateUi

