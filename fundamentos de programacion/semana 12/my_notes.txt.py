# Ejemplo de Apertura de Archivo en python

# Definimos el nombre del archivo
with open('my_notes.txt', 'w') as file:
    # Escribe tres líneas de notas personales en el archivo
    file.write("1. Recordar estudiar para el examen de cálculo integral.\n")
    file.write("2. Revisar la simulación del péndulo en Geogebra.\n")
    file.write("3. Subir el proyecto final al repositorio de GitHub.\n")

# Lectura del archivo my_notes.txt

# Abre el archivo en modo lectura
with open('my_notes.txt', 'r') as file:
    # Lee y muestra cada línea del archivo
    for line in file:
        print(line.strip())  # Imprime la línea eliminando saltos de línea innecesarios

# No es necesario cerrar los archivos manualmente, ya que el uso de 'with' lo hace automáticamente