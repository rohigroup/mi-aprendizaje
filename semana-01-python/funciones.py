def saludar(nombre):
    print(f"Hola, {nombre}!")

saludar("Jessica")
saludar("Hotel Urak")

def calcular_reserva(noches, precio_noche):
    total = noches * precio_noche
    return total

resultado = calcular_reserva(3, 180000)

print(f"Total de la reserva: $ {resultado:,}")
reserva1 = calcular_reserva(3, 180000)
reserva2 = calcular_reserva(2, 280000)
reserva3 = calcular_reserva(5, 450000)

total_hotel = reserva1 + reserva2 + reserva3
print(f"Total del hotel: $ {total_hotel:,}")

def describir_habitacion(numero, tipo, precio_noche):
    print(f"Habitacion {numero} | {tipo} $ {precio_noche:,} por noche")
describir_habitacion("101","sencilla", 180000)
describir_habitacion("202","doble", 280000)
