from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Qt
from views.ui_editar_producto_window import Ui_editar_producto_window

class EditarProductoWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_editar_producto_window()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.Window)