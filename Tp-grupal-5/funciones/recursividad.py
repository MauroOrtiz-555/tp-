def sumarRecursivo(lista):
    lista
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + sumarRecursivo(lista[1:])

def maximoRecursivo(lista, i=0):
    ''' Objetivo: obtener el valor máximo de una lista de forma recursiva. '''
    if i < len(lista):
        if i == len(lista) - 1:
            return lista[i]  # caso base
        elif lista[i] >= maximoRecursivo(lista, i + 1):
            return lista[i]
        else:
            return maximoRecursivo(lista, i + 1)

if __name__ == "__main__":
    # Este código solo se ejecutará cuando se ejecute recursividad.py directamente
    print("Fin de la ejecucion")
    

