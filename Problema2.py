consumo = float(input("¿Cuál fue el consumo en el restaurante? "))
porcentaje_propina = float(input("¿Qué porcentaje de propina deseas dejar? "))
propina = consumo * (porcentaje_propina / 100)
print(f"La propina a dejar es: {propina:.2f}")
