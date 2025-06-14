import re

cortar = lambda texto: texto[:15] + "..." if len(texto) > 15 else texto

def buscar_numeros(matriz, id):          
    for fila in matriz:
        if fila[0] == id:
            return True
    return False

def validar_numeros(mensaje):
    while True:
        valor = input(mensaje)
        try:
            valor = int(valor)
            break
        except ValueError:
            if valor == "":
                print("No se admiten espacios en blanco!\n")
            elif valor != "":
                print("Solo se admiten numeros!\n")
    return valor

def validar_palabras(mensaje):
    palabra = input(mensaje)
    while True:
        coincide = re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ ]+", palabra)
        if coincide == None:
            print("Solo se permiten el ingreso de letras")
            palabra = input("Ingrese nuevamente el nombre:\n").strip()
        else:
            break
    return palabra        

def validar_cliente(clientes):
    cliente_encontrado=True
    while cliente_encontrado:
        cliente_a_buscar=validar_numeros("Ingrese el ID del cliente\n")
        cliente_a_buscar=int(cliente_a_buscar)
        for cliente in clientes:
            if cliente['ID']==cliente_a_buscar:
                cliente_encontrado=False
        if cliente_encontrado==True:
            print(f"No existe un Cliente con ID N°{cliente_a_buscar}")
    
    return cliente_a_buscar

def validar_existencia(matriz, mensaje):
    numeroCorrecto = False
    validacion = True
    while validacion:
        if numeroCorrecto == True:
            validacion = False
        else:
            id = validar_numeros(mensaje)
            id = str(id).zfill(2)
            valor = buscar_numeros(matriz, id)
            if valor == True:
                numeroCorrecto = True
            else:
                print(f"El ID {id} no fue encontrado. Por favor intente de nuevo!")
    return id

if __name__ == "__main__":
    # Este código solo se ejecutará cuando se ejecute ventas.py directamente
    print("Fin de la ejecucion")
    