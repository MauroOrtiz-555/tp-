import funciones.validacion
import json

encabezado = ["ID", "Nombre y Apellido"]
 
def agregar_cliente(archivo):
    try:
        with open(archivo, "r", encoding="UTF-8") as datos:
            clientes = json.load(datos)
        cantidad = funciones.validacion.validar_numeros("Cuantos clientes nuevos desea agregar?\n")
        contador = 0
        bandera = True
        while bandera:
            if cantidad == contador:
                bandera = False
            else:
                contador += 1
                if clientes:
                    nuevoID=max(cliente["ID"] for cliente in clientes) + 1
                nombre_cliente=funciones.validacion.validar_palabras("Ingrese el nombre y apellido del cliente:\n")
                nuevo_cliente={
                    "ID": nuevoID,
                    "nombre": nombre_cliente
                }
                clientes.append(nuevo_cliente)
                with open(archivo,"w",encoding="UTF-8") as datos:
                    json.dump(clientes,datos,ensure_ascii=False)
                print(f"Se ha agregado al ID N°:{nuevo_cliente['ID']} el cliente {nuevo_cliente['nombre']}")
    except(FileNotFoundError, OSError) as error:
        print(f"Error! {error}")
 
def modificar_cliente(archivo):
    try:
        with open(archivo,"r",encoding="UTF-8") as datos:
            clientes=json.load(datos)
        cantidad = funciones.validacion.validar_numeros("Cuantos clientes desea modificar?\n")
        contador = 0
        bandera = True
        while bandera:
            if cantidad == contador:
                bandera = False
            else:
                contador += 1
                ID=int(funciones.validacion.validar_cliente(clientes))
                nuevo_nombre=funciones.validacion.validar_palabras("Ingrese el nombre y apellido del cliente:\n")
                IDS=[cliente["ID"] for cliente in clientes]
                if ID in IDS:
                    indice=IDS.index(ID)
                    clientes[indice]["nombre"]=nuevo_nombre
                    with open(archivo,"w",encoding="UTF-8") as datos:
                        json.dump(clientes,datos,ensure_ascii=False,indent=4)
                    print(f"Se ha cambiado al cliente N° {ID} a {nuevo_nombre}")
    except (FileNotFoundError, OSError) as error:
        print(f"Error! {error}")
 
def eliminar_cliente(archivo):
    try:
        with open(archivo,"r",encoding="UTF-8") as datos:
            clientes=json.load(datos)
        cantidad = funciones.validacion.validar_numeros("Cuantos clientes desea eliminar?\n")
        contador = 0
        bandera = True
        while bandera:
            if cantidad == contador:
                bandera = False
            else:
                contador += 1
                ID=funciones.validacion.validar_cliente(clientes)
                IDS=[cliente["ID"] for cliente in clientes]
                if ID in IDS:
                    indice=IDS.index(ID)
                    clientes.pop(indice)
                    with open(archivo,"w",encoding="UTF-8") as datos:
                        json.dump(clientes,datos,ensure_ascii=False,indent=4)
                    print(f"Se ha eliminado al cliente N° {ID}")
    except (FileNotFoundError, OSError) as error:
        print(f"Error!{error}")
 
def imprimir_clientes(archivo):
    try:
        with open(archivo,"r",encoding="UTF-8") as datos:
            clientes=json.load(datos)
        for cliente in clientes:
            print(f"{cliente['ID']:<5}| {cliente['nombre']:<10}")
    except (FileNotFoundError, OSError) as error:
        print(f"Error!{error}")
 
if __name__ == "__main__":
    # Este código solo se ejecutará cuando se ejecute ventas.py directamente
    print("Fin de la ejecucion")