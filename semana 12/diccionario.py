
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
