# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1103, 820)
        icon = QIcon()
        icon.addFile(u":/images/112-shop.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 10, 1071, 741))
        self.productos_tab = QWidget()
        self.productos_tab.setObjectName(u"productos_tab")
        self.frame_2 = QFrame(self.productos_tab)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 10, 514, 83))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.agregar_producto_pushButton = QPushButton(self.frame_2)
        self.agregar_producto_pushButton.setObjectName(u"agregar_producto_pushButton")
        icon1 = QIcon()
        icon1.addFile(u":/images/035-clothes.png", QSize(), QIcon.Normal, QIcon.Off)
        self.agregar_producto_pushButton.setIcon(icon1)
        self.agregar_producto_pushButton.setIconSize(QSize(50, 50))

        self.horizontalLayout.addWidget(self.agregar_producto_pushButton)

        self.eliminar_producto_pushButton = QPushButton(self.frame_2)
        self.eliminar_producto_pushButton.setObjectName(u"eliminar_producto_pushButton")
        icon2 = QIcon()
        icon2.addFile(u":/images/041-clothes.png", QSize(), QIcon.Normal, QIcon.Off)
        self.eliminar_producto_pushButton.setIcon(icon2)
        self.eliminar_producto_pushButton.setIconSize(QSize(50, 50))

        self.horizontalLayout.addWidget(self.eliminar_producto_pushButton)

        self.editar_producto_pushButton = QPushButton(self.frame_2)
        self.editar_producto_pushButton.setObjectName(u"editar_producto_pushButton")
        self.editar_producto_pushButton.setMinimumSize(QSize(0, 59))
        icon3 = QIcon()
        icon3.addFile(u":/images/040-clothes.png", QSize(), QIcon.Normal, QIcon.Off)
        self.editar_producto_pushButton.setIcon(icon3)
        self.editar_producto_pushButton.setIconSize(QSize(50, 50))

        self.horizontalLayout.addWidget(self.editar_producto_pushButton)

        self.frame_3 = QFrame(self.productos_tab)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 100, 1051, 71))
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
        self.termino_producto_lineEdit.setGeometry(QRect(350, 20, 551, 31))
        self.termino_producto_lineEdit.setClearButtonEnabled(True)
        self.buscar_producto_pushButton = QPushButton(self.frame_3)
        self.buscar_producto_pushButton.setObjectName(u"buscar_producto_pushButton")
        self.buscar_producto_pushButton.setGeometry(QRect(920, 20, 111, 31))
        icon4 = QIcon()
        icon4.addFile(u":/images/003-open-book-8.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buscar_producto_pushButton.setIcon(icon4)
        self.buscar_producto_pushButton.setIconSize(QSize(25, 25))
        self.label_4 = QLabel(self.productos_tab)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 660, 221, 21))
        self.cantidad_productos_label = QLabel(self.productos_tab)
        self.cantidad_productos_label.setObjectName(u"cantidad_productos_label")
        self.cantidad_productos_label.setGeometry(QRect(260, 660, 161, 21))
        self.productos_tableWidget = QTableWidget(self.productos_tab)
        self.productos_tableWidget.setObjectName(u"productos_tableWidget")
        self.productos_tableWidget.setGeometry(QRect(30, 180, 1011, 461))
        self.productos_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.productos_tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabWidget.addTab(self.productos_tab, "")
        self.ventas_tab = QWidget()
        self.ventas_tab.setObjectName(u"ventas_tab")
        self.frame_4 = QFrame(self.ventas_tab)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(20, 90, 761, 81))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_8 = QLabel(self.frame_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(90, 30, 47, 41))
        font = QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.inicio_dateEdit = QDateEdit(self.frame_4)
        self.inicio_dateEdit.setObjectName(u"inicio_dateEdit")
        self.inicio_dateEdit.setGeometry(QRect(150, 30, 141, 41))
        self.inicio_dateEdit.setFont(font)
        self.label_7 = QLabel(self.frame_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(350, 30, 47, 41))
        self.label_7.setFont(font)
        self.fin_dateEdit = QDateEdit(self.frame_4)
        self.fin_dateEdit.setObjectName(u"fin_dateEdit")
        self.fin_dateEdit.setGeometry(QRect(400, 30, 141, 41))
        self.fin_dateEdit.setFont(font)
        self.buscar_ventas_pushButton = QPushButton(self.frame_4)
        self.buscar_ventas_pushButton.setObjectName(u"buscar_ventas_pushButton")
        self.buscar_ventas_pushButton.setGeometry(QRect(590, 30, 101, 41))
        self.buscar_ventas_pushButton.setIcon(icon4)
        self.buscar_ventas_pushButton.setIconSize(QSize(25, 25))
        self.frame_6 = QFrame(self.ventas_tab)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(10, 10, 551, 80))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.realizar_venta_pushButton = QPushButton(self.frame_6)
        self.realizar_venta_pushButton.setObjectName(u"realizar_venta_pushButton")
        self.realizar_venta_pushButton.setGeometry(QRect(10, 10, 244, 58))
        icon5 = QIcon()
        icon5.addFile(u":/images/001-cart.png", QSize(), QIcon.Normal, QIcon.Off)
        self.realizar_venta_pushButton.setIcon(icon5)
        self.realizar_venta_pushButton.setIconSize(QSize(50, 50))
        self.consultar_ventas_pushButton = QPushButton(self.frame_6)
        self.consultar_ventas_pushButton.setObjectName(u"consultar_ventas_pushButton")
        self.consultar_ventas_pushButton.setGeometry(QRect(290, 10, 244, 58))
        self.consultar_ventas_pushButton.setIcon(icon4)
        self.consultar_ventas_pushButton.setIconSize(QSize(50, 50))
        self.label_6 = QLabel(self.ventas_tab)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 660, 221, 21))
        self.cantidad_ventas_label = QLabel(self.ventas_tab)
        self.cantidad_ventas_label.setObjectName(u"cantidad_ventas_label")
        self.cantidad_ventas_label.setGeometry(QRect(250, 660, 161, 21))
        self.ventas_tableWidget = QTableWidget(self.ventas_tab)
        self.ventas_tableWidget.setObjectName(u"ventas_tableWidget")
        self.ventas_tableWidget.setGeometry(QRect(30, 180, 1011, 461))
        self.ventas_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ventas_tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabWidget.addTab(self.ventas_tab, "")
        self.estadisticas_tab = QWidget()
        self.estadisticas_tab.setObjectName(u"estadisticas_tab")
        self.gridLayout = QGridLayout(self.estadisticas_tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.estadisticas_tab)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(90, 200, 501, 141))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.promedio_lineEdit = QLineEdit(self.frame_5)
        self.promedio_lineEdit.setObjectName(u"promedio_lineEdit")
        self.promedio_lineEdit.setMinimumSize(QSize(170, 30))
        font1 = QFont()
        font1.setPointSize(12)
        self.promedio_lineEdit.setFont(font1)
        self.promedio_lineEdit.setReadOnly(True)

        self.gridLayout_2.addWidget(self.promedio_lineEdit, 1, 1, 1, 1)

        self.cantidad_est_lineEdit = QLineEdit(self.frame_5)
        self.cantidad_est_lineEdit.setObjectName(u"cantidad_est_lineEdit")
        self.cantidad_est_lineEdit.setMinimumSize(QSize(170, 30))
        self.cantidad_est_lineEdit.setFont(font1)
        self.cantidad_est_lineEdit.setReadOnly(True)

        self.gridLayout_2.addWidget(self.cantidad_est_lineEdit, 0, 1, 1, 1)

        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(190, 30))

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(190, 30))

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(10, 80, 761, 81))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.label_10 = QLabel(self.frame_7)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(90, 30, 47, 41))
        self.label_10.setFont(font)
        self.inicio_est_dateEdit = QDateEdit(self.frame_7)
        self.inicio_est_dateEdit.setObjectName(u"inicio_est_dateEdit")
        self.inicio_est_dateEdit.setGeometry(QRect(150, 30, 141, 41))
        self.inicio_est_dateEdit.setFont(font)
        self.label_11 = QLabel(self.frame_7)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(350, 30, 47, 41))
        self.label_11.setFont(font)
        self.fin_est_dateEdit = QDateEdit(self.frame_7)
        self.fin_est_dateEdit.setObjectName(u"fin_est_dateEdit")
        self.fin_est_dateEdit.setGeometry(QRect(400, 30, 141, 41))
        self.fin_est_dateEdit.setFont(font)
        self.filtrar_est_pushButton = QPushButton(self.frame_7)
        self.filtrar_est_pushButton.setObjectName(u"filtrar_est_pushButton")
        self.filtrar_est_pushButton.setGeometry(QRect(590, 30, 101, 41))
        self.filtrar_est_pushButton.setIcon(icon4)
        self.filtrar_est_pushButton.setIconSize(QSize(25, 25))
        self.grafica_pushButton = QPushButton(self.frame)
        self.grafica_pushButton.setObjectName(u"grafica_pushButton")
        self.grafica_pushButton.setGeometry(QRect(10, 10, 244, 58))
        icon6 = QIcon()
        icon6.addFile(u":/images/069-profits-2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.grafica_pushButton.setIcon(icon6)
        self.grafica_pushButton.setIconSize(QSize(50, 50))
        self.mostrar_estadisticas_pushButton = QPushButton(self.frame)
        self.mostrar_estadisticas_pushButton.setObjectName(u"mostrar_estadisticas_pushButton")
        self.mostrar_estadisticas_pushButton.setGeometry(QRect(270, 10, 271, 58))
        icon7 = QIcon()
        icon7.addFile(u":/images/073-info.png", QSize(), QIcon.Normal, QIcon.Off)
        self.mostrar_estadisticas_pushButton.setIcon(icon7)
        self.mostrar_estadisticas_pushButton.setIconSize(QSize(50, 50))

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.tabWidget.addTab(self.estadisticas_tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1103, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Tiendita", None))
        self.agregar_producto_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar producto", None))
        self.eliminar_producto_pushButton.setText(QCoreApplication.translate("MainWindow", u"Eliminar producto", None))
        self.editar_producto_pushButton.setText(QCoreApplication.translate("MainWindow", u"Editar producto", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Buscar por:</span></p></body></html>", None))
        self.termino_producto_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Termino de busqueda", None))
        self.buscar_producto_pushButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Cantidad de Resultados:</span></p></body></html>", None))
        self.cantidad_productos_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">#</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.productos_tab), QCoreApplication.translate("MainWindow", u"Productos", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Inicio:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Fin:", None))
        self.buscar_ventas_pushButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.realizar_venta_pushButton.setText(QCoreApplication.translate("MainWindow", u"Realizar venta", None))
        self.consultar_ventas_pushButton.setText(QCoreApplication.translate("MainWindow", u"Consultar ventas", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Cantidad de Resultados:</span></p></body></html>", None))
        self.cantidad_ventas_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">#</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ventas_tab), QCoreApplication.translate("MainWindow", u"Ventas", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Cantidad ventas</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Promedio de venta</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Inicio:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Fin:", None))
        self.filtrar_est_pushButton.setText(QCoreApplication.translate("MainWindow", u"Filtrar", None))
        self.grafica_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar gr\u00e1fica", None))
        self.mostrar_estadisticas_pushButton.setText(QCoreApplication.translate("MainWindow", u"Estadisticas de todas las ventas", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.estadisticas_tab), QCoreApplication.translate("MainWindow", u"Estad\u00edsticas", None))
    # retranslateUi

