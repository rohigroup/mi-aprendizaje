habitaciones = [
    {"numero": "101", "tipo": "sencilla", "precio_noche": 180000},
    {"numero": "202", "tipo": "doble",    "precio_noche": 280000},
    {"numero": "305", "tipo": "suite",    "precio_noche": 450000},
]

reservas = [
    {"habitacion": "101", "huesped": "Carlos Perez",   "noches": 3},
    {"habitacion": "202", "huesped": "Ana Gomez",      "noches": 2},
    {"habitacion": "305", "huesped": "Luis Torres",    "noches": 5},
    {"habitacion": "101", "huesped": "Maria Salcedo",  "noches": 1},
    {"habitacion": "202", "huesped": "Pedro Marin",    "noches": 4},
]
print("==== Reporte Hotel Urak - Marzo 2026 ====")

total_ingresos = 0

for reserva in reservas:
    for habitacion in habitaciones:
        if reserva["habitacion"] == habitacion["numero"]:
            total = reserva["noches"]*habitacion["precio_noche"]
            total_ingresos +=total
            print(f"{reserva['huesped']} | hab {reserva['habitacion']} | {habitacion['tipo']} | {reserva['noches']} noches | ${total:,}")
print("-------------------------------------------")
print(f"Total reservas: {len(reservas)}")
print(f"Total ingresos: $ {total_ingresos:,}")