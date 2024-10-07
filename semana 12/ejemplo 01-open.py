#  Ejemplo de Apertura de Archivo en python

# Definimos el nombre del archivo
file_name = " my_notes.txt"

# Modo de apertura: "r" para lectura (read)
# Abrimos el archivo que acabamos de crear
archivo = open(file_name, "w")

archivo.write("loja\n")
archivo.write("los rios\n")
archivo.write("pichincha\n")
archivo.write("otavalo\n")

# cerramos el archivo despues de leer
archivo.close()
