import pytest
#Esta funcion funciona correctamente ya que elimina el ID especificado
def eliminar_producto():
    matriz =[
    ["01", "silla", "10000.00"], 
    ["02","mesa","30000.00"],
    ["03","escritorio","25000.00"],
    ]
    valor= "03"
    while True:
        posicion = -1
        for i in range(len(matriz)):
            if matriz[i][0] == valor:
                posicion = i
                break 
        if posicion != -1:
            matriz.pop(posicion)
            break
    largo_matriz = len(matriz)
    return largo_matriz

#Esta funcion agrega 
def agregar_producto():
    matriz =[
    ["01", "silla", "10000.00"], 
    ["02","mesa","30000.00"],
    ["03","escritorio","25000.00"],
    ]
    matriz.pop()
    largo_matriz = len(matriz)
    return largo_matriz

def test_validar1():
    largo = eliminar_producto()
#AssertioError
    if largo != 2:
        raise AssertionError("El largo de la matriz deberia ser 3")
    
def test_validar2():
    largo = agregar_producto()
#AssertionError
    if largo < 4:
        raise AssertionError("El largo de la matriz deberia ser 4")