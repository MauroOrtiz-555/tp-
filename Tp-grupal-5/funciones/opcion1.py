import funciones.ventas
import funciones.articulos
import funciones.clientes
import funciones.validacion
import funciones.menu

def opciones_articulos():
    matriz_productos = funciones.articulos.txt_a_matriz("funciones/productos.txt","r")
    producto_id = []
    for fila in matriz_productos:
        producto_id.append(fila[0]) 
    while True:
        print("OPCIÓN 1")
        print("1. Imprimir listado de articulos")
        print("2. agregar articulo/s")
        print("3. Editar articulo/s")
        print("4. Eliminar articulo/s")
        print("0. Volver al menú principal")
        print("")
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
            matriz_productos = funciones.articulos.txt_a_matriz("funciones/productos.txt","r")
            productos = [dict(zip(funciones.articulos.encabezado,fila))for fila in matriz_productos]
            print(f"{funciones.articulos.encabezado[0]:<15} | {funciones.articulos.encabezado[1]:<20} | {funciones.articulos.encabezado[2]:>5}")
            for producto in productos:
                articulo_corto = funciones.validacion.cortar(producto['articulo'])
                print(f"{producto['IDarticulo']:<15} | {articulo_corto:<20} | ${producto['precio']:>10}")
        elif opcion == 2:
            matriz_productos = funciones.articulos.txt_a_matriz("funciones/productos.txt","r")
            matriz_productos, producto_id = funciones.articulos.agregar_producto(matriz_productos, producto_id)
            funciones.articulos.escribir_txt(matriz_productos,"funciones/productos.txt")
            productos = [dict(zip(funciones.articulos.encabezado,fila))for fila in matriz_productos]
            print(f"{funciones.articulos.encabezado[0]:<15} | {funciones.articulos.encabezado[1]:<20} | {funciones.articulos.encabezado[2]:>5}")
            for producto in productos:
                articulo_corto = funciones.validacion.cortar(producto['articulo'])
                print(f"{producto['IDarticulo']:<15} | {articulo_corto:<20} | ${producto['precio']:>10}")
        elif opcion == 3:
            matriz_productos = funciones.articulos.txt_a_matriz("funciones/productos.txt","r")
            matriz_productos = funciones.articulos.editar_producto(matriz_productos)
            funciones.articulos.escribir_txt(matriz_productos,"funciones/productos.txt")
            productos = [dict(zip(funciones.articulos.encabezado,fila))for fila in matriz_productos]
            print(f"{funciones.articulos.encabezado[0]:<15} | {funciones.articulos.encabezado[1]:<20} | {funciones.articulos.encabezado[2]:>5}")
            for producto in productos:
                articulo_corto = funciones.validacion.cortar(producto['articulo'])
                print(f"{producto['IDarticulo']:<15} | {articulo_corto:<20} | ${producto['precio']:>10}")
        elif opcion == 4:
            matriz_productos = funciones.articulos.txt_a_matriz("funciones/productos.txt","r")
            matriz_productos = funciones.articulos.eliminar_producto(matriz_productos)
            funciones.articulos.escribir_txt(matriz_productos,"funciones/productos.txt")
            productos = [dict(zip(funciones.articulos.encabezado,fila))for fila in matriz_productos]
            print(f"funciones.{funciones.articulos.encabezado[0]:<15} | {funciones.articulos.encabezado[1]:<20} | {funciones.articulos.encabezado[2]:>5}")
            for producto in productos:
                articulo_corto = funciones.validacion.cortar(producto['articulo'])
                print(f"{producto['IDarticulo']:<15} | {articulo_corto:<20} | ${producto['precio']:>10}")
        elif opcion == 0:
            funciones.menu.mostrar_interfaz()
            break
        else: 
            print(" ")
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
# Este código solo se ejecutará cuando se ejecute ventas.py directamente
    print("Fin de la ejecucion")