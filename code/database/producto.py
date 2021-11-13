from database.conexion import insert, update, select, delete

def agregar(datos:dict):
    return insert("producto", **datos)

def mostrar_todos():
    return select("producto")

def editar(datos:dict, condicion:str=None, **condiciones):
    return update("producto", datos, condition=condicion, **condiciones)

def eliminar(condicion:str=None, **condiciones):
    return delete("producto", condition=condicion, **condiciones)

def mostrar(id_producto:int):
    return select("producto", "nombre", "precio", "codigo", id=id_producto)

def cantidad(condicion:str=None, **condiciones):
    return select("producto", "count(*)", condition=condicion, **condiciones)[0]["count(*)"]

def existe(id_producto:int):
    return True if cantidad(id=id_producto) else False
