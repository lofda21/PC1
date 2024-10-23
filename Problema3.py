peso_payaso = 112
peso_muneca = 75
num_payasos = int(input("¿Cuántos payasos se vendieron? "))
num_munecas = int(input("¿Cuántas muñecas se vendieron? "))
peso_total = (num_payasos * peso_payaso) + (num_munecas * peso_muneca)
print(f"El peso total del paquete es: {peso_total} gramos")
