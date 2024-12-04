def calcular_descuento(monto_total, porcentaje_descuento=10):
    # Calculamos el descuento
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


def main():
    # Primera llamada a la función con el valor predeterminado del descuento (10%)
    monto1 = 180.0  # Ejemplo de monto total de la compra
    descuento1 = calcular_descuento(monto1)
    monto_final1 = monto1 - descuento1

    # Segunda llamada a la función con un porcentaje de descuento especificado (por ejemplo, 15%)
    monto2 = 250.0  # Ejemplo de monto total de la compra
    descuento2 = calcular_descuento(monto2, 15)
    monto_final2 = monto2 - descuento2

    # Mostrar los resultados de ambas llamadas
    print(f"Compra 1: Monto total: ${monto1}, Descuento: ${descuento1}, Monto final: ${monto_final1}")
    print(f"Compra 2: Monto total: ${monto2}, Descuento: ${descuento2}, Monto final: ${monto_final2}")


# Ejecutar el programa principal
if __name__ == "__main__":
    main()