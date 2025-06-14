import funciones.ventas
import funciones.articulos
import funciones.validacion
import funciones.menu
 
def imprimir_estadistica_ventas_por_productos_especifico():
    productos = funciones.articulos.txt_a_matriz("funciones/productos.txt","r")
    ventas = funciones.ventas.txt_a_matriz("funciones/ventas.txt","r")
    validacion=True
    while validacion:
        idProducto = funciones.validacion.validar_existencia(productos, "Ingrese el ID del producto\n")
        idProducto= str(idProducto).zfill(2)
        for i in range(len(ventas)):
            if ventas[i][2] == idProducto:
                validacion=False
        if validacion==True:
            print("Articulo sin registro de venta")
    for i in range(len(productos)):
        if productos[i][0]==idProducto:
            nombre_producto=productos[i][1]
    cantidad_compras=0
    cantidad_dinero=0    
    for i in range (len(ventas)):
        if ventas[i][2]==idProducto:
            cantidad_compras+=1
            monto=ventas[i][4][:-3]
            monto=int(monto)
            cantidad_dinero+=monto
    cantidad_dinero=str(cantidad_dinero)
    cantidad_dinero+=".00"
    encabezado=["ID del producto","Nombre","Cantidad de compras","Importe"]
    print(f"{encabezado[0]:<20} | {encabezado[1]:<20} | {encabezado[2]:20} | {encabezado[3]:<20}")
    nombre_corto = funciones.validacion.cortar(nombre_producto)
    print(f"{idProducto:<20} | {nombre_corto:<20} | {cantidad_compras:<20} | ${cantidad_dinero:<20}")
    funciones.menu.mostrar_interfaz()
 
if __name__ == "__main__":
    # Este código solo se ejecutará cuando se ejecute ventas.py directamente
    print("Fin de la ejecucion")