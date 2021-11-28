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
        editar_producto_window.resize(591, 430)
        icon = QIcon()
        icon.addFile(u":/images/035-clothes.png", QSize(), QIcon.Normal, QIcon.Off)
        editar_producto_window.setWindowIcon(icon)
        self.centralwidget = QWidget(editar_producto_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 531, 41))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 80, 71, 21))
        self.nombre_lineEdit = QLineEdit(self.centralwidget)
        self.nombre_lineEdit.setObjectName(u"nombre_lineEdit")
        self.nombre_lineEdit.setGeometry(QRect(30, 110, 531, 31))
        font = QFont()
        font.setPointSize(10)
        self.nombre_lineEdit.setFont(font)
        self.nombre_lineEdit.setStyleSheet(u"")
        self.nombre_lineEdit.setMaxLength(255)
        self.nombre_lineEdit.setClearButtonEnabled(True)
        self.codigo_lineEdit = QLineEdit(self.centralwidget)
        self.codigo_lineEdit.setObjectName(u"codigo_lineEdit")
        self.codigo_lineEdit.setGeometry(QRect(30, 270, 531, 31))
        self.codigo_lineEdit.setFont(font)
        self.codigo_lineEdit.setMaxLength(13)
        self.codigo_lineEdit.setReadOnly(False)
        self.codigo_lineEdit.setClearButtonEnabled(True)
        self.precio_doubleSpinBox = QDoubleSpinBox(self.centralwidget)
        self.precio_doubleSpinBox.setObjectName(u"precio_doubleSpinBox")
        self.precio_doubleSpinBox.setGeometry(QRect(30, 190, 531, 31))
        self.precio_doubleSpinBox.setFont(font)
        self.precio_doubleSpinBox.setProperty("showGroupSeparator", False)
        self.precio_doubleSpinBox.setMaximum(999999.989999999990687)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 160, 71, 21))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 240, 71, 21))
        self.cancelar_pushButton = QPushButton(self.centralwidget)
        self.cancelar_pushButton.setObjectName(u"cancelar_pushButton")
        self.cancelar_pushButton.setGeometry(QRect(300, 340, 93, 28))
        self.editar_pushButton = QPushButton(self.centralwidget)
        self.editar_pushButton.setObjectName(u"editar_pushButton")
        self.editar_pushButton.setGeometry(QRect(190, 340, 93, 28))
        self.nombre_warning = QLabel(self.centralwidget)
        self.nombre_warning.setObjectName(u"nombre_warning")
        self.nombre_warning.setGeometry(QRect(190, 80, 361, 20))
        self.nombre_warning.setStyleSheet(u"color: rgb(255, 85, 0);")
        self.nombre_warning.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.precio_warning = QLabel(self.centralwidget)
        self.precio_warning.setObjectName(u"precio_warning")
        self.precio_warning.setGeometry(QRect(190, 160, 371, 20))
        self.precio_warning.setStyleSheet(u"color: rgb(255, 85, 0);")
        self.precio_warning.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.codigo_warning = QLabel(self.centralwidget)
        self.codigo_warning.setObjectName(u"codigo_warning")
        self.codigo_warning.setGeometry(QRect(190, 240, 371, 20))
        self.codigo_warning.setStyleSheet(u"color: rgb(255, 85, 0);")
        self.codigo_warning.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        editar_producto_window.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(editar_producto_window)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 591, 26))
        editar_producto_window.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(editar_producto_window)
        self.statusbar.setObjectName(u"statusbar")
        editar_producto_window.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.nombre_lineEdit, self.precio_doubleSpinBox)
        QWidget.setTabOrder(self.precio_doubleSpinBox, self.codigo_lineEdit)
        QWidget.setTabOrder(self.codigo_lineEdit, self.editar_pushButton)
        QWidget.setTabOrder(self.editar_pushButton, self.cancelar_pushButton)

        self.retranslateUi(editar_producto_window)

        QMetaObject.connectSlotsByName(editar_producto_window)
    # setupUi

    def retranslateUi(self, editar_producto_window):
        editar_producto_window.setWindowTitle(QCoreApplication.translate("editar_producto_window", u"Editar Producto", None))
        self.label.setText(QCoreApplication.translate("editar_producto_window", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Editar Producto</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("editar_producto_window", u"<html><head/><body><p><span style=\" font-size:10pt;\">Nombre</span></p></body></html>", None))
        self.nombre_lineEdit.setPlaceholderText("")
        self.codigo_lineEdit.setInputMask("")
        self.codigo_lineEdit.setText("")
        self.precio_doubleSpinBox.setPrefix("")
        self.label_3.setText(QCoreApplication.translate("editar_producto_window", u"<html><head/><body><p><span style=\" font-size:10pt;\">Precio</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("editar_producto_window", u"<html><head/><body><p><span style=\" font-size:10pt;\">C\u00f3digo</span></p></body></html>", None))
        self.cancelar_pushButton.setText(QCoreApplication.translate("editar_producto_window", u"Cancelar", None))
        self.editar_pushButton.setText(QCoreApplication.translate("editar_producto_window", u"Editar", None))
        self.nombre_warning.setText("")
        self.precio_warning.setText("")
        self.codigo_warning.setText("")
    # retranslateUi

