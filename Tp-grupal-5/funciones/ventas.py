import funciones.validacion
import funciones.articulos
import json
import funciones.recursividad

multiplicar = lambda x, y: x * y  

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
        lineas = [f"{codigo_venta};{cantProductos};{codigo_articulo};{nombre_articulo};{importe_venta};{codigo_cliente}\n" for codigo_venta, cantProductos, codigo_articulo, nombre_articulo, importe_venta, codigo_cliente in matriz]
        arch = open(archivo,"wt")
        arch.writelines(lineas)
    except OSError as mensaje:
        print("no se puede grabar el archivo", mensaje)
    finally:
        try:
            arch.close()
        except NameError:
            pass

def agregar_venta(matriz, matriz_producto, listaID):
    ultimoID = funciones.recursividad.maximoRecursivo(listaID)
    cantidad = funciones.validacion.validar_numeros("Cuantos registros de venta desea agregar?\n")
    bandera = True
    contador = 0
    while bandera:
        ultimoID = funciones.recursividad.maximoRecursivo(listaID)
        idNuevo = str(int(ultimoID) + 1).zfill(3) 
        listaID.append(idNuevo)
        if contador == cantidad:
             bandera = False
        else:
            contador += 1
            cantidadProductos = int(funciones.validacion.validar_numeros(f"Ingrese la cantidad de productos de la venta N°{idNuevo}\n"))
            numeroCorrecto = False
            validacion = True
            while validacion:
                if numeroCorrecto == True:
                    validacion = False
                else:
                    IDarticulo = funciones.validacion.validar_numeros(f"Ingrese el N° de ID del artículo de la venta N°{idNuevo}\n")
                    IDarticulo = str(IDarticulo).zfill(2)
                    valor = funciones.validacion.buscar_numeros(matriz_producto, IDarticulo)
                    if valor == True:
                        numeroCorrecto = True
                    else:
                        print(f"El ID {IDarticulo} no fue encontrado. Por favor intente de nuevo!")
            try:
                with open("funciones/clientes.json", "r", encoding="UTF-8") as datos:
                    clientes = json.load(datos)
            except(FileNotFoundError, OSError) as error:
                print(f"Error! {error}")
            IDcliente = funciones.validacion.validar_cliente(clientes)
            IDcliente = str(IDcliente).zfill(2)
            posicion = -1
            for i in range(len(matriz_producto)):
                if matriz_producto[i][0] == IDarticulo:
                    posicion = i
            precio = matriz_producto[posicion][2][:-3]
            precio = int(precio)
            importe = str(multiplicar(precio, cantidadProductos))
            importe += ".00"
            producto = matriz_producto[posicion][1]
            datos = [idNuevo, cantidadProductos, IDarticulo, producto , importe, IDcliente]
            matriz.append(datos)
    return matriz, listaID

def editar_venta(matriz, matriz_producto):
    cantidad = funciones.validacion.validar_numeros("Cuántos registros de venta desea editar?\n")
    bandera = True
    contador = 0
    while bandera:
        if cantidad == contador:
            bandera=False
        else:
            contador+=1
            print("1. Cantidad")
            print("2. ID Articulo")
            print("3. ID Cliente")
            cambio = funciones.validacion.validar_numeros("Qué valor desea editar?\n")
            while cambio > 4 or cambio < 1:
                cambio = funciones.validacion.validar_numeros("Ingrese una opción valida\n")
            idVenta= funciones.validacion.validar_existencia(matriz, "Ingrese el ID de la venta a modificar")
            enteroVenta = int(idVenta)
            if cambio == 1:
                matriz[enteroVenta-1][1] = funciones.validacion.validar_numeros("Ingrese la cantidad de articulos\n")
                int(matriz [enteroVenta-1][1])
            elif cambio == 2:
                IDarticulo = funciones.validacion.validar_existencia(matriz_producto, "Ingrese el ID del producto\n")
                posicion = -1
                for i in range(len(matriz_producto)):
                    if matriz_producto[i][0] == IDarticulo:
                        posicion = i
                precio = matriz_producto[posicion][2]
                producto = matriz_producto[posicion][1]
                matriz[enteroVenta-1][2] = str(IDarticulo).zfill(2)
                matriz[enteroVenta-1][4] = str(precio)
                matriz[enteroVenta-1][3] = str(producto)
            else:
                ID_cliente = funciones.validacion.validar_numeros("Ingrese el ID del cliente\n")
                matriz[enteroVenta-1][5] = str(ID_cliente).zfill(2)
    return matriz

def eliminar_venta(matriz):
    id_a_eliminar = funciones.validacion.validar_existencia(matriz, "Ingrese el ID de la venta a eliminar\n")
    posicion = -1
    for i in range(len(matriz)):
        if matriz[i][0] == id_a_eliminar:
            posicion = i
    if posicion != -1:
        matriz.pop(posicion)
        print(f"La venta con ID N°{id_a_eliminar} fue eliminada correctamente.")
    return matriz

encabezado = ["IDventa", "cantidad", "IDarticulo", "articulo", "importe", "IDcliente"]

if __name__ == "__main__":
    # Este código solo se ejecutará cuando se ejecute ventas.py directamente
    print("Fin de la ejecución")