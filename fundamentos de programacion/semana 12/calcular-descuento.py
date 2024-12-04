""
# Crea una función llamada calcular_descuento que tome dos parámetros:
#el monto total de la compra y un valor predeterminado para el porcentaje de descuento
#(por ejemplo, 10% por defecto).
#La función debe calcular el descuento aplicando el porcentaje al monto total de la compra.

#La función debe devolver el monto del descuento calculado.

#Llamada a la Función:

#Llama a la función calcular_descuento al menos dos veces desde el programa principal.
#En una llamada, proporciona el monto total de la compra y
#, en la otra, proporciona tanto el monto total de la compra como el porcentaje de descuento.

 #crear una funcion calcular descu...

def calcular_descuento(monto_total,descuento=10):
    descuento = monto_total*descuento/100
    return descuento

#1 forma de llamar

monto_total = float(input("imgrese el monto:"))
descuento= calcular_descuento(2000)
print(f"el descuento es ",descuento )

#2 segunda forma

monto_total2 = float(input("ingrese el monto:"))
descuento2 = calcular_descuento(monto_total2,descuento 50 )
print(f"el descuento es ",descuento )




