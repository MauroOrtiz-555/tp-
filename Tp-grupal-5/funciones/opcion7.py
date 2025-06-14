import funciones.ventas
import funciones.validacion
import json
import funciones.menu

def imprimir_estadistica_ventas_por_clientes_especifico(archivo_clientes):
    try:
        with open(archivo_clientes, "r", encoding="UTF-8") as datos:
            clientes = json.load(datos)
        ventas = funciones.ventas.txt_a_matriz("funciones/ventas.txt","r")
        validacion=True
        while validacion:
            cliente_a_buscar=funciones.validacion.validar_cliente(clientes)
            cliente_a_buscar= str(cliente_a_buscar).zfill(2)
            for fila in ventas:
                if fila[5] == cliente_a_buscar:
                    validacion=False
            if validacion==True:
                print("Cliente sin registro de venta")
        cliente_numero=int(cliente_a_buscar)
        for cliente in clientes:
            if cliente['ID']==cliente_numero:
                nombre_cliente=cliente['nombre']
        cantidad_compras=0
        cantidad_dinero=0    
        for i in range (len(ventas)):
            if ventas[i][5]==cliente_a_buscar:
                cantidad_compras+=1
                monto=ventas[i][4][:-3]
                monto=int(monto)
                cantidad_dinero+=monto
        cantidad_dinero=str(cantidad_dinero)
        cantidad_dinero+=".00"
        encabezado=["ID del cliente","Nombre","Cantidad de compras","Importe"]
        print(f"{encabezado[0]:<20} | {encabezado[1]:<20} | {encabezado[2]:20} | {encabezado[3]:<20}")
        nombre_corto = funciones.validacion.cortar(nombre_cliente)
        print(f"{cliente_a_buscar:<20} | {nombre_corto:<20} | {cantidad_compras:<20} | ${cantidad_dinero:<20}")
    except(FileNotFoundError, OSError) as error:
        print(f"Error! {error}")
    funciones.menu.mostrar_interfaz()

if __name__ == "__main__":
    # Este código solo se ejecutará cuando se ejecute ventas.py directamente
    print("Fin de la ejecucion")