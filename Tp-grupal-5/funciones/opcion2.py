import funciones.ventas
import funciones.articulos
import funciones.clientes
import funciones.validacion
import funciones.menu

def opciones_clientes():
    while True:
        print("OPCIÓN 2")
        print("1. Imprimir listado de clientes")
        print("2. agregar cliente/s")
        print("3. Editar cliente/s")
        print("4. Eliminar cliente/s")
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
            print(f"{funciones.clientes.encabezado[0]:<5}| {funciones.clientes.encabezado[1]:<10}")
            funciones.clientes.imprimir_clientes("funciones/clientes.json")
        elif opcion == 2:
            funciones.clientes.agregar_cliente("funciones/clientes.json")
            print(f"{funciones.clientes.encabezado[0]:<5}| {funciones.clientes.encabezado[1]:<10}")
            funciones.clientes.imprimir_clientes("funciones/clientes.json")
        elif opcion == 3:
            funciones.clientes.modificar_cliente("funciones/clientes.json")
            print(f"{funciones.clientes.encabezado[0]:<5}| {funciones.clientes.encabezado[1]:<10}")
            funciones.clientes.imprimir_clientes("funciones/clientes.json")
        elif opcion == 4:
            funciones.clientes.eliminar_cliente("funciones/clientes.json")
            print(f"{funciones.clientes.encabezado[0]:<5}| {funciones.clientes.encabezado[1]:<10}")
            funciones.clientes.imprimir_clientes("funciones/clientes.json")
        elif opcion == 0:
            funciones.menu.mostrar_interfaz()
            break
        else: 
            print(" ")
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
# Este código solo se ejecutará cuando se ejecute ventas.py directamente
    print("Fin de la ejecucion")