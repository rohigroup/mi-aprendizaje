reservas = [
    {"habitacion": "101", "tipo": "sencilla", "noches": 3, "precio_noche": 180000},
    {"habitacion": "202", "tipo": "doble",    "noches": 2, "precio_noche": 280000},
    {"habitacion": "305", "tipo": "suite",    "noches": 5, "precio_noche": 450000},
    {"habitacion": "102", "tipo": "doble",    "noches": 1, "precio_noche": 180000},
    {"habitacion":"203",  "tipo":"twin",      "noches": 4, "precio_noche": 280000},
    {"habitacion":"208",  "tipo":"triple",    "noches": 2, "precio_noche": 450000},

]
print("===== Reporte Hotel Urak - Marzo 2026 =====")

for reserva in reservas:
    total_reserva = reserva["noches"] * reserva["precio_noche"]
    print(f"Habitacion {reserva['habitacion']} | {reserva['tipo']} | {reserva['noches']} noches | $ {total_reserva:,}")

total_ingresos = 0
for reserva in reservas:
    total_ingresos += reserva["noches"] * reserva["precio_noche"]

print("-------------------------------------------")
print(f"Total reservas: {len(reservas)}")
print(f"Total ingresos: $ {total_ingresos:,}")