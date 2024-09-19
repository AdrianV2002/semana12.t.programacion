# Funcion para aplicar el decuento por defecto.

def calcular_descuento(monto_total, porcentaje_descuento=12):
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


if __name__ == "__main__":

#Primer monto con el descuento por defecto "12%"
    monto1 = 240
    descuento1 = calcular_descuento(monto1)
    print(f"Monto total sin Descuento: ${monto1:.2f}")
    print(f"Cantidad a descontar: ${descuento1:.2f} (12% de descuento)")
    print(f"Monto final a pagar con descuento: ${monto1 - descuento1:.2f}\n")


#Segundo monto con el decuento custom del "17%"

    monto2 = 624
    porcentaje_descuento_personalizado = 17
    descuento2 = calcular_descuento(monto2, porcentaje_descuento_personalizado)
    print(f"Monto total sin Descuento: ${monto2:.2f}")
    print(f"Cantidad a descontar: ${descuento2:.2f} ({porcentaje_descuento_personalizado}% de descuento)")
    print(f"Monto final a pagar con descuento: ${monto2 - descuento2:.2f}")
