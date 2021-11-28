from PySide2.QtCore import SLOT, Slot
from PySide2.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from views.ui_mainwindow import Ui_MainWindow
from database import producto

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.agregar_producto_pushButton.clicked.connect(self.agregar_producto_window)
        self.ui.eliminar_producto_pushButton.clicked.connect(self.eliminar_producto)
        self.ui.editar_producto_pushButton.clicked.connect(self.editar_producto_window)
        self.ui.realizar_venta_pushButton.clicked.connect(self.realizar_venta_window)

        self.iniciar_tabla_productos()
        self.mostrar_productos(producto.mostrar_todos())

    @Slot()
    def agregar_producto_window(self):
        from controllers.agregar_producto_window import AgregarProductoWindow
        window = AgregarProductoWindow(self)
        window.show()

    @Slot()
    def eliminar_producto(self):
        items = self.ui.productos_tableWidget.selectedItems()
        if len(items) == 0:
            QMessageBox.warning(self, "Atención", "Seleccione algún producto")
        elif len(items) == 1:
            row = items[0].row()
            nombre = self.ui.productos_tableWidget.item(row, 0).text()
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
            nombres = []
            for item in items:
                nombres.append(self.ui.productos_tableWidget.item(item.row(), 0).text())

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

        row = self.ui.productos_tableWidget.currentRow()
        nombre = self.ui.productos_tableWidget.item(row, 0)
        if nombre:
            nombre = nombre.text()
            msg = QMessageBox()
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

    @Slot()
    def editar_producto_window(self):
        from controllers.editar_producto_window import EditarProductoWindow
        window = EditarProductoWindow(self)
        window.show()

    @Slot()
    def realizar_venta_window(self):
        from controllers.realizar_venta_window import RealizarVentaWindow
        window = RealizarVentaWindow(self)
        window.show()

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
