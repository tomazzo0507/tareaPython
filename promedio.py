cantidad = int(input("¿Cuántas notas vas a ingresar? "))

suma_notas = 0

for i in range(cantidad):
    nota = float(input(f"Ingrese la nota #{i+1}: "))
    suma_notas += nota

promedio = suma_notas / cantidad

print(f"\nEl promedio de las {cantidad} notas es: {promedio:.2f}")
