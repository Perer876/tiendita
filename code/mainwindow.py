from PySide2.QtCore import Slot
from PySide2.QtWidgets import QMainWindow
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.agregar_producto_pushButton.clicked.connect(self.agregar_producto_window)
        self.ui.editar_producto_pushButton_3.clicked.connect(self.editar_producto_window)
        self.ui.realizar_venta_pushButton_2.clicked.connect(self.realizar_venta_window)

    @Slot()
    def agregar_producto_window(self):
        from agregar_producto_window import AgregarProductoWindow
        window = AgregarProductoWindow(self)
        window.show()

    @Slot()
    def editar_producto_window(self):
        from editar_producto_window import EditarProductoWindow
        window = EditarProductoWindow(self)
        window.show()

    @Slot()
    def realizar_venta_window(self):
        from realizar_venta_window import RealizarVentaWindow
        window = RealizarVentaWindow(self)
        window.show()
