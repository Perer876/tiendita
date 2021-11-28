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

        self.venta = venta.Venta()

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
                    for pro in self.mostrar_productos(producto.mostrar_con_precio(termino)):
                        self.venta.agregar_producto(pro["id"], 1)
                else:
                    QMessageBox.warning(self, "Atención", "Termino invalido")

            elif criterio == "Código":
                for pro in self.mostrar_productos(producto.mostrar_con_codigo(termino)):
                    self.venta.agregar_producto(pro["id"], 1)

        self.actualizar_vista_venta()

    def iniciar_tabla_venta(self):
        self.ui.venta_tableWidget.setColumnCount(4)
        self.ui.venta_tableWidget.setColumnWidth(0, 502)
        self.ui.venta_tableWidget.setColumnWidth(1, 169)
        self.ui.venta_tableWidget.setColumnWidth(1, 169)
        self.ui.venta_tableWidget.setColumnWidth(1, 169)
        self.ui.venta_tableWidget.setHorizontalHeaderLabels(["Producto", "Precio Unitario", "Cantidad", "Subtotal"])

    def insertar_subtotal_en_tabla(self, lp:listaproductos.ProductoVenta, pos):
        self.ui.venta_tableWidget.insertRow(pos)
        self.ui.venta_tableWidget.setItem(pos, 0, QTableWidgetItem(str(lp.nombre_producto)))
        self.ui.venta_tableWidget.setItem(pos, 1, QTableWidgetItem(str(lp.precio_producto)))
        self.ui.venta_tableWidget.setItem(pos, 2, QTableWidgetItem(str(lp.cantidad)))
        self.ui.venta_tableWidget.setItem(pos, 3, QTableWidgetItem(str(lp.sub_total)))

    def vaciar_tabla_venta(self):
        self.ui.venta_tableWidget.setRowCount(0)

    def actualizar_vista_venta(self):
        self.vaciar_tabla_venta()
        for i, lp in enumerate(self.venta.lista_productos):
            self.insertar_subtotal_en_tabla(lp, i)
        self.ui.total_label.setText(str(self.venta.total))

    def iniciar_productos_comboBox(self):
        self.ui.buscar_producto_por_comboBox.addItem("Nombre")
        self.ui.buscar_producto_por_comboBox.addItem("Precio")
        self.ui.buscar_producto_por_comboBox.addItem("Código")
