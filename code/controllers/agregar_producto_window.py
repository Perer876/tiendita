from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Qt, Slot
from views.ui_agregar_producto_window import Ui_agregar_producto_window

class AgregarProductoWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_agregar_producto_window()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.Window)
        self.ui.agregar_pushButton.clicked.connect(self.agregar)
        self.ui.cancelar_pushButton.clicked.connect(self.cancelar)

    @Slot()
    def agregar(self):
        self.ui.nombre_warning.clear()
        self.ui.precio_warning.clear()
        self.ui.codigo_warning.clear()

        from database.producto import Producto, agregar, mostrar_todos
        p = Producto()
        p.nombre = self.ui.nombre_lineEdit.text()
        p.precio = self.ui.precio_doubleSpinBox.value()
        p.codigo = self.ui.codigo_lineEdit.text()

        if len(p.nombre) == 0:
            self.ui.nombre_warning.setText("El nombre no puede estar en blanco")
        elif p.precio <= 0:
            self.ui.precio_warning.setText("el precio no puede ser cero")
        elif len(p.codigo) == 0:
            self.ui.codigo_warning.setText("El codigo no puede estar en blanco")
        else:
            agregar(p.to_dict())
            self.ui.nombre_lineEdit.clear()      
            self.ui.precio_doubleSpinBox.setValue(0.00)
            self.ui.codigo_lineEdit.clear()
            self.parent().mostrar_productos(mostrar_todos())
        
    @Slot()
    def cancelar(self):
        self.close()
