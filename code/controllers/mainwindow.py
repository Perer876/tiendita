from PySide2.QtCore import Slot
from PySide2.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from views.ui_mainwindow import Ui_MainWindow
from database import producto, venta

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.agregar_producto_pushButton.clicked.connect(self.agregar_producto_window)
        self.ui.eliminar_producto_pushButton.clicked.connect(self.eliminar_producto)
        self.ui.editar_producto_pushButton.clicked.connect(self.editar_producto_window)
        self.ui.realizar_venta_pushButton.clicked.connect(self.realizar_venta_window)
        self.ui.buscar_producto_pushButton.clicked.connect(self.buscar_producto)
        self.ui.consultar_ventas_pushButton.clicked.connect(self.consultar_ventas)

        self.iniciar_tabla_productos()
        self.mostrar_productos(producto.mostrar_todos())
        self.iniciar_tabla_ventas()
        self.mostrar_ventas(venta.mostrar_todos())
        self.iniciar_productos_comboBox()

    @Slot()
    def agregar_producto_window(self):
        from controllers.agregar_producto_window import AgregarProductoWindow
        window = AgregarProductoWindow(self)
        window.show()

    @Slot()
    def eliminar_producto(self):
        items = self.ui.productos_tableWidget.selectedItems()
        nombres = []
        for i in range(0, int(len(items) / 3)):
            pos = i * 3
            nombres.append(items[pos].text())

        if len(nombres) == 0:
            QMessageBox.warning(self, "Atención", "Seleccione algún producto")
        elif len(nombres) == 1:
            nombre = nombres[0]
            msg = QMessageBox(parent=self)
            msg.setWindowTitle("Eliminar producto")
            msg.setText('¿Estas seguro que quieres eliminar?')
            msg.setIcon(QMessageBox.Question)
            msg.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Cancel)
            msg.setInformativeText(f'El producto a eliminar es "{nombre}"')
            msg.exec_()
            if msg.clickedButton().text() == "OK":
                producto.eliminar(nombre=nombre)
                self.mostrar_productos(producto.mostrar_todos())
        else:
            msg = QMessageBox(parent=self)
            msg.setWindowTitle("Eliminar productos")
            msg.setText('¿Estas seguro que quieres eliminar los productos seleccionados?')
            msg.setIcon(QMessageBox.Question)
            msg.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Cancel)
            msg.setDetailedText("\n".join(nombres))
            msg.exec_()
            if msg.clickedButton().text() == "OK":
                for nombre in nombres:
                    producto.eliminar(nombre=nombre)
                self.mostrar_productos(producto.mostrar_todos())

    @Slot()
    def editar_producto_window(self):
        from controllers.editar_producto_window import EditarProductoWindow
        row = self.ui.productos_tableWidget.currentRow()
        if row < 0:
            QMessageBox.warning(self, "Atención", "Seleccione algún producto")
        else:
            p = producto.Producto()
            p.nombre = self.ui.productos_tableWidget.item(row, 0).text()
            p.precio = self.ui.productos_tableWidget.item(row, 1).text()
            p.codigo = self.ui.productos_tableWidget.item(row, 2).text()
            window = EditarProductoWindow(self, p)
            window.show()

    @Slot()
    def realizar_venta_window(self):
        from controllers.realizar_venta_window import RealizarVentaWindow
        window = RealizarVentaWindow(self)
        window.show()

    @Slot()
    def buscar_producto(self):
        termino = self.ui.termino_producto_lineEdit.text()
        if termino:
            criterio = self.ui.buscar_producto_por_comboBox.currentText()
            if criterio == "Nombre":
                self.mostrar_productos(producto.mostrar_con_nombre(termino))
            elif criterio == "Precio":
                if not termino.isalpha():
                    self.mostrar_productos(producto.mostrar_con_precio(termino))
                else:
                    QMessageBox.warning(self, "Atención", "Termino invalido")
            elif criterio == "Código":
                self.mostrar_productos(producto.mostrar_con_codigo(termino))
        else:
            self.mostrar_productos(producto.mostrar_todos())

    @Slot()
    def consultar_ventas(self):
        self.mostrar_ventas(venta.mostrar_todos())

    def iniciar_tabla_productos(self):
        self.ui.productos_tableWidget.verticalHeader().setVisible(False)
        self.ui.productos_tableWidget.setColumnCount(3)
        self.ui.productos_tableWidget.setColumnWidth(0, 674)
        self.ui.productos_tableWidget.setColumnWidth(1, 168)
        self.ui.productos_tableWidget.setColumnWidth(2, 167)
        self.ui.productos_tableWidget.setHorizontalHeaderLabels(["Nombre", "Precio", "Código"])

    def insertar_producto_en_tabla(self, pro, pos):
        self.ui.productos_tableWidget.insertRow(pos)
        self.ui.productos_tableWidget.setItem(pos, 0, QTableWidgetItem(str(pro["nombre"])))
        self.ui.productos_tableWidget.setItem(pos, 1, QTableWidgetItem(str(pro["precio"])))
        self.ui.productos_tableWidget.setItem(pos, 2, QTableWidgetItem(str(pro["codigo"])))

    def vaciar_tabla_productos(self):
        self.ui.productos_tableWidget.setRowCount(0)

    def mostrar_productos(self, productos):
        self.vaciar_tabla_productos()
        for i, pro in enumerate(productos):
            self.insertar_producto_en_tabla(pro, i)
        self.ui.cantidad_productos_label.setText(str(len(productos)))

    def iniciar_tabla_ventas(self):
        self.ui.ventas_tableWidget.verticalHeader().setVisible(False)
        self.ui.ventas_tableWidget.setColumnCount(2)
        self.ui.ventas_tableWidget.setColumnWidth(0, 609)
        self.ui.ventas_tableWidget.setColumnWidth(1, 400)
        self.ui.ventas_tableWidget.setHorizontalHeaderLabels(["Fecha Realización", "Total"])

    def insertar_venta_en_tabla(self, ven, pos):
        self.ui.ventas_tableWidget.insertRow(pos)
        self.ui.ventas_tableWidget.setItem(pos, 0, QTableWidgetItem(str(ven["fecha_realizada"])))
        self.ui.ventas_tableWidget.setItem(pos, 1, QTableWidgetItem(str(ven["total"])))

    def vaciar_tabla_ventas(self):
        self.ui.ventas_tableWidget.setRowCount(0)

    def mostrar_ventas(self, ventas):
        self.vaciar_tabla_ventas()
        for i, pro in enumerate(ventas):
            self.insertar_venta_en_tabla(pro, i)
        self.ui.cantidad_ventas_label.setText(str(len(ventas)))

    def iniciar_productos_comboBox(self):
        self.ui.buscar_producto_por_comboBox.addItem("Nombre")
        self.ui.buscar_producto_por_comboBox.addItem("Precio")
        self.ui.buscar_producto_por_comboBox.addItem("Código")
    