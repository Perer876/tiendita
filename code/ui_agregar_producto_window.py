# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'agregar_producto_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_agregar_producto_window(object):
    def setupUi(self, agregar_producto_window):
        if not agregar_producto_window.objectName():
            agregar_producto_window.setObjectName(u"agregar_producto_window")
        agregar_producto_window.resize(800, 600)
        icon = QIcon()
        icon.addFile(u":/images/035-clothes.png", QSize(), QIcon.Normal, QIcon.Off)
        agregar_producto_window.setWindowIcon(icon)
        self.centralwidget = QWidget(agregar_producto_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(300, 20, 121, 41))
        agregar_producto_window.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(agregar_producto_window)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        agregar_producto_window.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(agregar_producto_window)
        self.statusbar.setObjectName(u"statusbar")
        agregar_producto_window.setStatusBar(self.statusbar)

        self.retranslateUi(agregar_producto_window)

        QMetaObject.connectSlotsByName(agregar_producto_window)
    # setupUi

    def retranslateUi(self, agregar_producto_window):
        agregar_producto_window.setWindowTitle(QCoreApplication.translate("agregar_producto_window", u"Agregar Producto", None))
        self.label.setText(QCoreApplication.translate("agregar_producto_window", u"Agregar Producto", None))
    # retranslateUi

