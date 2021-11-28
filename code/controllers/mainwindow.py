from PySide2.QtCore import Slot
from PySide2.QtWidgets import QMainWindow, QTableWidgetItem
from views.ui_mainwindow import Ui_MainWindow
from database import producto

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.agregar_producto_pushButton.clicked.connect(self.agregar_producto_window)
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
        self.ui.productos_tableWidget.setColumnCount(3)
        self.ui.productos_tableWidget.setColumnWidth(0, 625)
        self.ui.productos_tableWidget.setColumnWidth(1, 168)
        self.ui.productos_tableWidget.setColumnWidth(2, 168)
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
