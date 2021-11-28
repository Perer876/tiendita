from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Qt, Slot
from views.ui_editar_producto_window import Ui_editar_producto_window
from database.producto import Producto, editar, mostrar_todos

class EditarProductoWindow(QMainWindow):
    def __init__(self, parent=None, producto:Producto()=None):
        super().__init__(parent)
        self.ui = Ui_editar_producto_window()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.Window)

        self.ui.editar_pushButton.clicked.connect(self.modificar)
        self.ui.cancelar_pushButton.clicked.connect(self.cancelar)
        
        self.producto_a_modificar = producto
        if producto is not None:
            self.ui.nombre_lineEdit.setText(producto.nombre)
            self.ui.precio_doubleSpinBox.setValue(float(producto.precio))
            self.ui.codigo_lineEdit.setText(producto.codigo)

    @Slot()
    def modificar(self):
        self.ui.nombre_warning.clear()
        self.ui.precio_warning.clear()
        self.ui.codigo_warning.clear()

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
            editar(p.to_dict(), nombre=self.producto_a_modificar.nombre)
            self.parent().mostrar_productos(mostrar_todos())
            self.close()
        
    @Slot()
    def cancelar(self):
        self.close()
