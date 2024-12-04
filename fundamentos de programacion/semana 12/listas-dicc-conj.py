# creacion de una lista
numeros = [1, 2, 3, 4,"cinco",6.0, "hola"]
print(numeros)
print(numeros[0])
print(numeros[1])
print(numeros[2])
print(numeros[3])
print(numeros[4])

# AGREGAR ITEM A UNA LISTA
numeros.append(7)
print(numeros)

# agregar item
numeros.insert(3,7)
print(numeros)
# tipos de eliminacion eliminar por la posicion
numeros.pop(0)
print(numeros)
# tipos de eliminacion
numeros.remove(4)
print(numeros)

print("******** diccionario *********")
# crear un diccionario de persona
persona ={
    "nombre": "Julio",
    "apellido": "Trujillo",
    "edad": 39,
    "ciudad": "Otavalo",
}
print(persona)
print(persona["nombre"])
print(persona["apellido"])
print(persona["edad"])
print(persona["ciudad"])

# modificar
persona["ciudad"] = "quito"
print(persona)

# agregar elemento
persona ["profesion"] = "mecanico industrial"
print(persona)
persona ["telefono"] = "0991222367"
print(persona)

# acceder a las claves
claves =persona.keys()
print(claves)
valores = persona.values()
print(valores)

for clave,valor in persona.items():
    print(clave,": ",valor)


# eliminar
del persona["edad"]
print(persona)

print("*********conjuntos*********")
# ejemplos de conjuntos
frutas ={"guanabana", "banana", "fresa"}
print(frutas)
# añadir un elemento
frutas.add("sandia")
print(frutas)

# elementos unicos ,  ni se agrega un duplicado
frutas.add("guanabana")

# eliminar
frutas.remove("banana")
print(frutas)












