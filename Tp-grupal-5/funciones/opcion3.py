import funciones.ventas
import funciones.articulos
import funciones.clientes
import funciones.validacion
import funciones.menu

def opciones_ventas(): 
    matriz_ventas = funciones.ventas.txt_a_matriz("funciones/ventas.txt","r")
    venta_id = []
    for fila in matriz_ventas:
        venta_id.append(fila[0])       
    while True:
        print("OPCIÓN 3")
        print("1. Imprimir listado de ventas")
        print("2. agregar venta/s")
        print("3. Editar venta/s")
        print("4. Eliminar venta/s")
        print("0. Volver al menú principal")
        opcion = input("Ingrese la opcion que desea\n")
        try:
            opcion = int(opcion)
        except ValueError:
            if opcion == "":
                print("No se admiten espacios en blanco!\n")
                continue
            else:
                print("Solo se admiten numeros!\n")
                continue
        if opcion == 1:
            matriz_ventas = funciones.ventas.txt_a_matriz("funciones/ventas.txt","r")
            print(f"{funciones.ventas.encabezado[0]:<10} | {funciones.ventas.encabezado[1]:<10} | {funciones.ventas.encabezado[2]:<15} | {funciones.ventas.encabezado[3]:<20} | {funciones.ventas.encabezado[4]:<16} | {funciones.ventas.encabezado[5]:<5}")
            for fila in matriz_ventas:
                IDnuevo, cantidadProductos, IDarticulo, nombre, importe, IDcliente = fila
                nombre_corto = funciones.validacion.cortar(nombre)
                print(f"{IDnuevo:<10} | {cantidadProductos:<10} | {IDarticulo:<15} | {nombre_corto:<20} | ${importe:<15} | {IDcliente:>10}")
        elif opcion == 2:
            matriz_ventas = funciones.ventas.txt_a_matriz("funciones/ventas.txt","r")
            matriz_productos = funciones.articulos.txt_a_matriz("funciones/productos.txt","r")
            matriz_ventas, venta_id = funciones.ventas.agregar_venta(matriz_ventas, matriz_productos, venta_id)
            funciones.ventas.escribir_txt(matriz_ventas,"funciones/ventas.txt")
            print(f"{funciones.ventas.encabezado[0]:<10} | {funciones.ventas.encabezado[1]:<10} | {funciones.ventas.encabezado[2]:<15} | {funciones.ventas.encabezado[3]:<20} | {funciones.ventas.encabezado[4]:<16} | {funciones.ventas.encabezado[5]:<5}")
            for fila in matriz_ventas:
                IDnuevo, cantidadProductos, IDarticulo, nombre, importe, IDcliente = fila
                nombre_corto = funciones.validacion.cortar(nombre)
                print(f"{IDnuevo:<10} | {cantidadProductos:<10} | {IDarticulo:<15} | {nombre_corto:<20} | ${importe:<15} | {IDcliente:>10}")
        elif opcion == 3:
            matriz_ventas = funciones.ventas.txt_a_matriz("funciones/ventas.txt","r")
            matriz_productos = funciones.articulos.txt_a_matriz("funciones/productos.txt","r")
            matriz_ventas = funciones.ventas.editar_venta(matriz_ventas, matriz_productos)
            funciones.ventas.escribir_txt(matriz_ventas,"funciones/ventas.txt")
            print(f"{funciones.ventas.encabezado[0]:<10} | {funciones.ventas.encabezado[1]:<10} | {funciones.ventas.encabezado[2]:<15} | {funciones.ventas.encabezado[3]:<20} | {funciones.ventas.encabezado[4]:<16} | {funciones.ventas.encabezado[5]:<5}")
            for fila in matriz_ventas:
                IDnuevo, cantidadProductos, IDarticulo, nombre, importe, IDcliente = fila
                nombre_corto = funciones.validacion.cortar(nombre)
                print(f"{IDnuevo:<10} | {cantidadProductos:<10} | {IDarticulo:<15} | {nombre_corto:<20} | ${importe:<15} | {IDcliente:>10}")
        elif opcion == 4:
            matriz_ventas = funciones.ventas.txt_a_matriz("funciones/ventas.txt","r")
            matriz_ventas = funciones.ventas.eliminar_venta(matriz_ventas)
            funciones.ventas.escribir_txt(matriz_ventas,"funciones/ventas.txt")
            print(f"{funciones.ventas.encabezado[0]:<10} | {funciones.ventas.encabezado[1]:<10} | {funciones.ventas.encabezado[2]:<15} | {funciones.ventas.encabezado[3]:<20} | {funciones.ventas.encabezado[4]:<16} | {funciones.ventas.encabezado[5]:<5}")
            for fila in matriz_ventas:
                IDnuevo, cantidadProductos, IDarticulo, nombre, importe, IDcliente = fila
                nombre_corto = funciones.validacion.cortar(nombre)
                print(f"{IDnuevo:<10} | {cantidadProductos:<10} | {IDarticulo:<15} | {nombre_corto:<20} | ${importe:<15} | {IDcliente:>10}")
        elif opcion == 0:
            funciones.menu.mostrar_interfaz()
            break
        else: 
            print(" ")
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
# Este código solo se ejecutará cuando se ejecute ventas.py directamente
    print("Fin de la ejecucion")