from database.conexion import insert, update, select, delete

def agregar(datos:dict):
    return insert("producto", **datos)

def mostrar_todos():
    return select("producto")

def editar(datos:dict, condicion:str=None, **condiciones):
    return update("producto", datos, condition=condicion, **condiciones)

def eliminar(condicion:str=None, **condiciones):
    return delete("producto", condition=condicion, **condiciones)

def mostrar(id_producto:int, *columnas):
    if len(columnas) != 1:
        columnas = ["nombre", "precio", "codigo"]
        consulta = select("producto", *columnas, id=id_producto)
        return consulta[0] if consulta else None
    else:
        consulta = select("producto", *columnas, id=id_producto)
        return consulta[0][columnas[0]] if consulta else None

def mostrar_con_nombre(nombre):
    return select("producto", condition=f"nombre LIKE '%{nombre}%'")

def mostrar_con_precio(precio):
    return select("producto", condition=f"precio = {precio}")

def mostrar_con_codigo(codigo):
    return select("producto", condition=f"codigo LIKE '%{codigo}%'")

def cantidad(condicion:str=None, **condiciones):
    return select("producto", "count(*)", condition=condicion, **condiciones)[0]["count(*)"]

def existe(id_producto:int):
    return True if cantidad(id=id_producto) else False

class Producto:
    def __init__(self, id=None, nombre=None, precio=0, codigo=None):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.codigo = codigo
    
    def to_dict(self):
        return {
            "nombre" : self.nombre,
            "precio" : self.precio,
            "codigo" : self.codigo
        }
