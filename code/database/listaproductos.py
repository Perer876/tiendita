from database.conexion import insert, update, select, delete
from database import producto 

def agregar(id_venta:int, lista_productos:tuple):
    for registro in lista_productos:
        registro["id_venta"] = id_venta
        insert("lista_productos", **registro)

def mostrar(id_venta:int, *columnas):
    if len(columnas) == 0:
        columnas = ["id_producto", "precio_producto", "cantidad"]
    return select("lista_productos", *columnas, id_venta=id_venta)

def eliminar_lista(id_venta:int):
    return delete("lista_productos", id_venta=id_venta)

def cantidad(condicion:str=None, **condiciones):
    return select("lista_productos", "count(*)", condition=condicion, **condiciones)[0]["count(*)"]

def existe(id_venta:int, id_producto:int):
    return True if cantidad(id_venta=id_venta, id_producto=id_producto) else False

class ProductoVenta:
    def __init__(self, id_producto, cantidad=1, nombre_producto=None, precio_producto=None):
        self.id_producto = id_producto
        self.cantidad = cantidad
        self.nombre_producto = nombre_producto if nombre_producto else producto.mostrar(id_producto, "nombre")
        self.precio_producto = precio_producto if precio_producto else producto.mostrar(id_producto, "precio")
        self.sub_total = self.cantidad * self.precio_producto

    def modificar(self, cantidad):
        self.cantidad += cantidad
        self.sub_total = self.cantidad * self.precio_producto

    def to_dict(self):
        return {
            "id_producto" : self.id_producto,
            "cantidad" : self.cantidad,
            "precio_producto" : self.precio_producto
        }