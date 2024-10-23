time = input("Introduce la hora en formato HH:MM: ")
hours, minutes = time.split(":")
time_float = float(hours) + float(minutes) / 60
if 7 <= time_float <= 8:
    print("Es la hora del desayuno")
elif 12 <= time_float <= 13:
    print("Es la hora del almuerzo")
elif 18 <= time_float <= 19:
    print("Es la hora de la cena")
