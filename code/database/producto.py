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
    if len(columnas) == 0:
        columnas = ["nombre", "precio", "codigo"]
    return select("producto", *columnas, id=id_producto)[0]

def cantidad(condicion:str=None, **condiciones):
    return select("producto", "count(*)", condition=condicion, **condiciones)[0]["count(*)"]

def existe(id_producto:int):
    return True if cantidad(id=id_producto) else False
