import funciones.validacion
import funciones.recursividad

def txt_a_matriz(archivo, modo):
    try:
        matriz = []
        arch = open(archivo, modo, encoding="UTF-8")
        linea = arch.readline().strip()
        while linea:
            matriz.append(linea.split(";"))
            linea = arch.readline().strip()
    except OSError:
        print("No se pudo leer el archivo")
    finally:
        try:
            arch.close()
        except:
            print("No se pudo cerrar el archivo")
    return matriz

def escribir_txt(matriz,archivo):
    try:
        lineas = [f"{codigo};{productos};{precio}\n" for codigo, productos, precio in matriz]
        arch = open(archivo,"wt")
        arch.writelines(lineas)
    except OSError as mensaje:
        print("no se puede grabar el archivo", mensaje)
    finally:
        try:
            arch.close()
        except NameError:
            pass

def agregar_producto(matriz, listaID):
    cantidad = funciones.validacion.validar_numeros("Cuantos productos nuevos desea agregar?\n")
    bandera = True
    contador = 0
    while bandera:
        ultimoID = funciones.recursividad.maximoRecursivo(listaID)
        idNuevo = str(int(ultimoID) + 1).zfill(2) 
        listaID.append(idNuevo)
        if contador == cantidad:
            bandera = False
        else:
            contador += 1
            producto = funciones.validacion.validar_palabras(f"Ingrese el nombre del producto numero {idNuevo}\n")
            precio = funciones.validacion.validar_numeros(f"Ingrese el precio del producto numero {idNuevo}\n")
            cadena_precio = str(precio)
            cadena_precio += ".00"
            datos = [idNuevo, producto, cadena_precio]
            matriz.append(datos)
    return matriz, listaID
 
def editar_producto(matriz):
    cantidad = funciones.validacion.validar_numeros("Cuantos productos desea editar?\n")
    bandera = True
    contador = 0
    while bandera:
        if cantidad == contador:
            bandera=False
        else:
            contador+=1
            print("1- Nombre del producto")
            print("2- Precio del producto")
            cambio = funciones.validacion.validar_numeros("Ingrese la columna que desea editar\n")
            while cambio > 2 or cambio < 1:
                cambio = funciones.validacion.validar_numeros("Ingrese una opcion valida\n")
            idProducto = funciones.validacion.validar_existencia(matriz, "Ingrese el ID del producto a modificar\n")
            if cambio == 1:
                matriz [int(idProducto)-1][cambio] = funciones.validacion.validar_palabras("Ingrese el nombre del producto\n")
            elif cambio == 2:
                importe = funciones.validacion.validar_numeros("Ingrese el precio\n")
                matriz [int(idProducto)-1][cambio] = str(importe) + ".00"
    return matriz

def eliminar_producto(matriz):
    id_a_eliminar = funciones.validacion.validar_existencia(matriz, "Ingrese el ID del producto a eliminar\n")
    posicion = -1
    for i in range(len(matriz)):
         if matriz[i][0] == id_a_eliminar:
            posicion = i
    if posicion != -1:
        matriz.pop(posicion)
        print(f"El producto con ID N°{id_a_eliminar} fue eliminado correctamente.")
    return matriz

encabezado = ["IDarticulo", "articulo", "precio"]

if __name__ == "__main__":
    # Este código solo se ejecutará cuando se ejecute ventas.py directamente
    print("Fin de la ejecución")