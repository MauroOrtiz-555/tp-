import funciones.articulos
import funciones.ventas
import funciones.validacion
import funciones.menu
import funciones.recursividad
 
def imprimir_estadistica_venta_articulo():
    productos=funciones.articulos.txt_a_matriz("funciones/productos.txt","r")
    ventas=funciones.ventas.txt_a_matriz("funciones/ventas.txt","r")
    estadistica_producto=[]
    for i in range (len(productos)):
        productos_buscar=productos[i][0]
        nombre_producto=productos[i][1]
        cantidad_compras=0
        lista_importes = []
        for c in range(len(ventas)):
                if ventas[c][2]==productos_buscar:
                    cantidad_compras+=1
                    monto=ventas[c][4][:-3]
                    monto=int(monto)
                    lista_importes.append(monto)
        cantidad_plata = funciones.recursividad.sumarRecursivo(lista_importes)
        cantidad_plata=str(cantidad_plata)
        cantidad_plata+=".00"
        compra_producto=[productos_buscar, nombre_producto,cantidad_plata,cantidad_compras]
        if cantidad_compras!=0:
            estadistica_producto.append(compra_producto)
    encabezado= ["IDartico", "articulo", "Cantidad de Compras", "Importe"]
    print(f"{encabezado[0]:<20} | {encabezado[1]:<20} | {encabezado[2]:20} | {encabezado[3]:<20}")
    for fila in estadistica_producto:
        IDarticulo, articulo, importe, compras= fila
        nombre_corto = funciones.validacion.cortar(articulo)
        print(f"{IDarticulo:<20} | {nombre_corto:<20} | {compras:<20} | ${importe:<20}")
    funciones.menu.mostrar_interfaz()
 
if __name__ == "__main__":
    # Este código solo se ejecutará cuando se ejecute ventas.py directamente
    print("Fin de la ejecución")