from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Qt
from views.ui_realizar_venta_window import Ui_realizar_venta_window

class RealizarVentaWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_realizar_venta_window()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.Window)
        