from PySide2.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from PySide2.QtCore import Qt, Slot
from views.ui_realizar_venta_window import Ui_realizar_venta_window
from database import venta, listaproductos, producto

class RealizarVentaWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_realizar_venta_window()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.Window)

        self.ui.cancelar_pushButton.clicked.connect(self.cancelar_venta)
        self.ui.agregar_producto_pushButton.clicked.connect(self.agregar_producto)
        self.ui.aumentar_pushButton.clicked.connect(self.aumentar_producto)
        self.ui.disminuir_pushButton.clicked.connect(self.disminuir_producto)
        self.ui.eliminar_producto_pushButton.clicked.connect(self.eliminar_producto)

        self.ui.termino_producto_lineEdit.returnPressed.connect(self.agregar_producto)

        self.venta = venta.Venta()
        self.last_row = -1

        self.iniciar_tabla_venta()
        self.iniciar_productos_comboBox()
        
    @Slot()
    def cancelar_venta(self):
        self.close()

    @Slot()
    def agregar_producto(self):
        termino = self.ui.termino_producto_lineEdit.text()
        if termino:
            criterio = self.ui.buscar_producto_por_comboBox.currentText()
            if criterio == "Nombre":
                for pro in producto.mostrar_con_nombre(termino):
                    self.venta.agregar_producto(pro["id"], 1)

            elif criterio == "Precio":
                if not termino.isalpha():
                    for pro in producto.mostrar_con_precio(termino):
                        self.venta.agregar_producto(pro["id"], 1)
                else:
                    QMessageBox.warning(self, "Atención", "Termino invalido")

            elif criterio == "Código":
                for pro in producto.mostrar_con_codigo(termino):
                    self.venta.agregar_producto(pro["id"], 1)

        self.actualizar_vista_venta()

    @Slot()
    def aumentar_producto(self):
        row = self.ui.venta_tableWidget.currentRow()
        if row >= 0:
            self.last_row = row

        if self.last_row < 0:
            QMessageBox.warning(self, "Atención", "Seleccione algún producto")
        else:
            id_producto = self.ui.venta_tableWidget.item(self.last_row, 0).text()
            self.venta.agregar_producto(id_producto, 1)
            self.actualizar_vista_venta()

    @Slot()
    def disminuir_producto(self):
        row = self.ui.venta_tableWidget.currentRow()
        if row >= 0:
            self.last_row = row

        if self.last_row < 0:
            QMessageBox.warning(self, "Atención", "Seleccione algún producto")
        else:
            id_producto = self.ui.venta_tableWidget.item(self.last_row, 0).text()
            self.venta.agregar_producto(id_producto, -1)
            self.actualizar_vista_venta()
        
    @Slot()
    def eliminar_producto(self):
        row = self.ui.venta_tableWidget.currentRow()
        if row < 0:
            QMessageBox.warning(self, "Atención", "Seleccione algún producto")
        else:
            id_producto = self.ui.venta_tableWidget.item(row, 0).text()
            self.venta.quitar_producto(id_producto)
            self.actualizar_vista_venta()

    def iniciar_tabla_venta(self):
        self.ui.venta_tableWidget.setColumnCount(5)
        self.ui.venta_tableWidget.setColumnWidth(1, 502)
        self.ui.venta_tableWidget.setColumnWidth(2, 169)
        self.ui.venta_tableWidget.setColumnWidth(3, 169)
        self.ui.venta_tableWidget.setColumnWidth(4, 169)
        self.ui.venta_tableWidget.setHorizontalHeaderLabels(["id", "Producto", "Precio Unitario", "Cantidad", "Subtotal"])
        self.ui.venta_tableWidget.hideColumn(0)

    def insertar_subtotal_en_tabla(self, lp:listaproductos.ProductoVenta, pos):
        self.ui.venta_tableWidget.insertRow(pos)
        self.ui.venta_tableWidget.setItem(pos, 0, QTableWidgetItem(str(lp.id_producto)))
        self.ui.venta_tableWidget.setItem(pos, 1, QTableWidgetItem(str(lp.nombre_producto)))
        self.ui.venta_tableWidget.setItem(pos, 2, QTableWidgetItem(str(lp.precio_producto)))
        self.ui.venta_tableWidget.setItem(pos, 3, QTableWidgetItem(str(lp.cantidad)))
        self.ui.venta_tableWidget.setItem(pos, 4, QTableWidgetItem(str(lp.sub_total)))

    def vaciar_tabla_venta(self):
        self.ui.venta_tableWidget.setRowCount(0)

    def actualizar_vista_venta(self):
        self.vaciar_tabla_venta()
        for i, lp in enumerate(self.venta.lista_productos):
            self.insertar_subtotal_en_tabla(lp, i)
        total = f'<html><head/><body><p><span style=" font-size:24pt;">${str(self.venta.total)}</span></p></body></html>'
        self.ui.total_label.setText(total)

    def iniciar_productos_comboBox(self):
        self.ui.buscar_producto_por_comboBox.addItem("Nombre")
        self.ui.buscar_producto_por_comboBox.addItem("Precio")
        self.ui.buscar_producto_por_comboBox.addItem("Código")
