# ejercicio 2 matriz de 3x3
matriz =[
    [1, 19, 15],
    [2, 11,7],
    [4, 8, 6]
]

print(matriz)
# metodo de ordenamiento buble_sort

def buble_sort(fila):
    #algoritmo buble sort
    n = len(fila)
    for i in range(n):
        for j in range(n-1, i,-1):
            if fila[j]>fila[j-1]:
                fila[j], fila[j-1] = fila[j-1], fila[j]
                print(fila)
print("matriz original")
print(matriz)
buble_sort(matriz[0])
print(matriz)


