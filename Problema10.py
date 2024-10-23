lista = ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']
nueva_lista = [lista[i] for i in range(len(lista)) if i not in [0, 4, 5]]
print(nueva_lista)
