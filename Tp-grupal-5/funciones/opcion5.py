import funciones.ventas
import funciones.validacion
import json
import funciones.menu
import funciones.recursividad

def imprimir_estadistica_ventas_por_clientes(archivo_clientes):
    try:
        with open(archivo_clientes, "r", encoding="UTF-8") as datos:
            clientes = json.load(datos)
        ventas = funciones.ventas.txt_a_matriz("funciones/ventas.txt","r")
        estadisticas=[]
        for cliente in clientes:
            cliente_a_buscar= cliente['ID']
            cliente_a_buscar= str(cliente_a_buscar).zfill(2)
            nombre_cliente=cliente['nombre']
            cantidad_compras=0
            lista_importes = []
            for i in range (len(ventas)):
                if ventas[i][5]==cliente_a_buscar:
                    cantidad_compras+=1
                    monto=ventas[i][4][:-3]
                    monto=int(monto)
                    lista_importes.append(monto)
            cantidad_dinero = funciones.recursividad.sumarRecursivo(lista_importes)
            cantidad_dinero=str(cantidad_dinero)
            cantidad_dinero+=".00"
            compras_cliente=[cliente_a_buscar,nombre_cliente,cantidad_compras,cantidad_dinero]
            if cantidad_compras!=0:
                estadisticas.append(compras_cliente)
        encabezado=["ID del cliente","Nombre","Cantidad de compras","Importe"]
        print(f"{encabezado[0]:<20} | {encabezado[1]:<20} | {encabezado[2]:20} | {encabezado[3]:<20}")
        for fila in estadisticas:
            IDcliente, nombre, compras, importe = fila
            nombre_corto = funciones.validacion.cortar(nombre)
            print(f"{IDcliente:<20} | {nombre_corto:<20} | {compras:<20} | ${importe:<20}")
    except(FileNotFoundError, OSError) as error:
        print(f"Error! {error}")
    funciones.menu.mostrar_interfaz()

if __name__ == "__main__":
    # Este código solo se ejecutará cuando se ejecute ventas.py directamente
    print("Fin de la ejecucion")