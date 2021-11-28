from database.conexion import insert, update, select, delete
from database import listaproductos, producto

def agregar(datos:dict):
    lista_productos = datos.pop("lista_productos")

    if len(lista_productos) == 0:
        return False 

    id_venta = insert("venta", **datos)
    if id_venta and listaproductos.agregar(id_venta, lista_productos):
        return True
    return False

def mostrar(id_venta:int):
    venta = select("venta", id=id_venta)[0]
    venta["lista_productos"] = listaproductos.mostrar(id_venta)
    return venta

def mostrar_todos():
    return select("venta")

def mostrar_todas_entre(fecha1, fecha2):
    return select("venta", condition=f"fecha_realizada BETWEEN CAST('{fecha1}' AS DATETIME) AND CAST('{fecha2}' AS DATETIME)")

def eliminar(id_venta:int):
    listaproductos.eliminar_lista(id_venta)
    delete("venta", id=id_venta)

def editar(datos:dict, id_venta:int):
    lista_productos = datos.pop("lista_productos")

    if len(lista_productos) == 0:
        return False

    listaproductos.eliminar_lista(id_venta)
    if update("venta", datos, id=id_venta) and listaproductos.agregar(id_venta, lista_productos):
        return True
    return False

class Venta:
    def __init__(self, id=None, fecha_realizada=None, lista_productos=None):
        self.id = id
        self.fecha_realizada = fecha_realizada
        self.total = 0
        self.lista_productos = list()
        if id:
            for datos in lista_productos:
                reg = listaproductos.ProductoVenta(
                    datos["id_producto"], 
                    datos["cantidad"], 
                    producto.mostrar(datos["id_producto"], "nombre"),
                    datos["precio_producto"]
                )
                self.lista_productos.append(reg)
                self.total += reg.sub_total
    
    def __pos_in_list(self, id_producto):
        pos = None
        for i, pro in enumerate(self.lista_productos):
            if pro.id_producto == int(id_producto): return i

    def agregar_producto(self, id_producto:int, cantidad):
        if producto.existe(id_producto):
            pos = self.__pos_in_list(id_producto)
            if pos is not None:
                sub_total = self.lista_productos[pos].sub_total
                self.lista_productos[pos].modificar(cantidad)
                self.total = self.total - sub_total + self.lista_productos[pos].sub_total
                if self.lista_productos[pos].cantidad == 0:
                    self.lista_productos.pop(pos)
            else:
                reg = listaproductos.ProductoVenta(id_producto, cantidad)
                self.lista_productos.append(reg)
                self.total += reg.sub_total
            return True
        return False

    def quitar_producto(self, id_producto:int):
        pos = self.__pos_in_list(id_producto)
        if pos:
            self.total -= self.lista_productos[pos].sub_total
            return self.lista_productos.pop(pos)
        return False

    def limpiar_lista(self):
        self.total = 0
        self.lista_productos.clear()

    def to_dict(self):
        return {
            "fecha_realizada" : self.fecha_realizada,
            "total" : self.total,
            "lista_productos": [p.to_dict() for p in self.lista_productos]
        }
