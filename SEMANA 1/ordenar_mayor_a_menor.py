def quicksort(lista):
    if len(lista)<=1:
        return lista
    pivote = lista[0]
    izquierda=[]
    derecha=[]
    for i in range(1, len(lista)):
        izquierda.append(lista[i]) if lista[i]<pivote else derecha.append(lista[i])
    return quicksort(izquierda) + [pivote] + quicksort(derecha)

numeros =[26,6,12,88,55]
listaOrdenada = quicksort(numeros)
print(listaOrdenada)