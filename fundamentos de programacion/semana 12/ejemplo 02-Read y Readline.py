# Ejemplo de Lecturas de Archivos en python usando read() y readline()

# Definimos el nombre del archivo
file_name = " my_notes.txt"

# Modo de apertura "w" para escritura (write)
archivo_escritura = open(file_name, "w")

# Escribimos algunas lineas en el archivo
archivo_escritura.write("linea 1: Esto en una prueba.\n")
archivo_escritura.write("linea 2: Esto en una prueba de python.\n")
archivo_escritura.write("linea 3: Esto en una prueba de java.\n")
archivo_escritura.write("linea 4: Esto en una prueba de clase 26/10/2024.\n")

# cerramos el archivo de escritura
archivo_escritura.close()



# Metodo read(): lee todo el contenido del archivo
contenido_completo = Archivo_lectura.read()
print("contenido_completo usando read():")
print(contenido_completo)

# Metodo readline(): lee una linea a la vez
archivo_lectura.seek(0) # Reiniciamos el cursor al principio del archivo
line_1 = archivo_lectura.readline()
line_2 = archivo_lectura.readline()
line_3 = archivo_lectura.readline()
line_4 = archivo_lectura.readline()

print("\ncontenido linea por linea usando readline():")
print(line_1.strip()) # strip() elimina el salto de linea al final
print(line_2.strip())
print(line_3.strip())
print(line_4.strip())

# cerramos el archivode lectura
archivo_lectura.close()
