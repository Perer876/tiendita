from PySide2.QtCore import Slot
from PySide2.QtWidgets import QMainWindow
from agregar_producto_window import AgregarProductoWindow
from ui_mainwindow import Ui_MainWindow
import agregar_producto_window

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.agregar_producto_pushButton.clicked.connect(self.agregar_producto_window)

    @Slot()
    def agregar_producto_window(self):
        window = AgregarProductoWindow(self)
        window.show()