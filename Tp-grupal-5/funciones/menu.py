import funciones.opcion1
import funciones.opcion2
import funciones.opcion3
import funciones.opcion4
import funciones.opcion5
import funciones.opcion6
import funciones.opcion7
import funciones.ventas
import funciones.articulos
import funciones.clientes
import funciones.validacion

def mostrar_interfaz():
    print(" ")
    print("*** MENÚ PRINCIPAL ***")
    print(" ")
    print("1. Listado de todos los articulos y precios")
    print("2. Listado de todos los clientes")
    print("3. Listado de todas las ventas")
    print("4. Estadísticas de ventas por articulos")
    print("5. Estadísticas de ventas por clientes")
    print("6. Estadísticas de ventas por producto en específico ")
    print("7. Estadísticas de ventas por cliente en específico ")
    print("0. Salir")

def mostrar_menu(): 
    mostrar_interfaz()   
    while True:
        eleccion = input("Seleccione su opción (0-7) \n").strip()
        try:
            eleccion = int(eleccion)
        except ValueError:
            if eleccion == "":
                print("No se admiten espacios en blanco!\n")
                continue
            else:
                print("Solo se admiten numeros!\n")
                continue
        if eleccion == 1:
            funciones.opcion1.opciones_articulos()
        elif eleccion == 2:
            funciones.opcion2.opciones_clientes()
        elif eleccion == 3:
            funciones.opcion3.opciones_ventas()
        elif eleccion == 4:
            funciones.opcion4.imprimir_estadistica_venta_articulo()
        elif eleccion == 5:
            funciones.opcion5.imprimir_estadistica_ventas_por_clientes("funciones/clientes.json")
        elif eleccion == 6:
            funciones.opcion6.imprimir_estadistica_ventas_por_productos_especifico()
        elif eleccion == 7:
            funciones.opcion7.imprimir_estadistica_ventas_por_clientes_especifico("funciones/clientes.json")
        elif eleccion == 0:
            print("Saliste del programa.")
            break
        else:
            print(" ")
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
# Este código solo se ejecutará cuando se ejecute ventas.py directamente
    print("Fin de la ejecucion")