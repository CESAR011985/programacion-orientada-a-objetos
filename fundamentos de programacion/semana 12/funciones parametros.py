# Definición de una función con parámetros
def saludar(nombre, edad):
    print(f"quetal, {nombre} tienes {edad} años.")
# Llamada a la función y paso de argumentos
saludar("Rouse", 54)
saludar("Cesar", 39)
# Parámetros predeterminados
def saludar_con_saludo(nombre, edad, saludo="Hello"):
    print(f"{saludo}, {nombre} tengo {edad} años.")
# Llamada a la función con parámetro predeterminado
saludar_con_saludo("Margarita", 43)
saludar_con_saludo("Julio", 29, "¡mucho gusto")