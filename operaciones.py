import math

num1 = input("Ingresa el primer número: ")
num2 = input("Ingresa el segundo número: ")

num1 = int(num1)
num2 = int(num2)


suma = num1 + num2
print(f"La suma de {num1} y {num2} es: {suma}")


resta1 = num1 - num2
resta2 = num2 - num1
print(f"La resta de {num1} menos {num2} es: {resta1}")
print(f"La resta de {num2} menos {num1} es: {resta2}")


multi = num1 * num2
print(f"La multiplicación de {num1} x {num2} es: {multi}")


divi1 = num1 / num2
divi2 = num2 / num1
print(f"La división de {num1} entre {num2} es: {divi1}")
print(f"La división de {num2} entre {num1} es: {divi2}")


pot1 = num1 ** num2
pot2 = num2 ** num1
print(f"{num1} elevado a la {num2} es: {pot1}")
print(f"{num2} elevado a la {num1} es: {pot2}")


raiz1 = math.sqrt(num1)
raiz2 = math.sqrt(num2)
print(f"La raíz cuadrada de {num1} es: {raiz1}")
print(f"La raíz cuadrada de {num2} es: {raiz2}")


if num1 > 0 and num2 > 0:
    log1 = math.log10(num1)
    log2 = math.log10(num2)
    print(f"El logaritmo base 10 de {num1} es: {log1}")
    print(f"El logaritmo base 10 de {num2} es: {log2}")
else:
    print("No se puede calcular el logaritmo de números menores o iguales a 0.")

if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num2 > num1:
    print(f"{num2} es mayor que {num1}")
else:
    print(f"Ambos números son iguales")



mod1 = num1 % num2
mod2 = num2 % num1
print(f"El módulo (residuo) de {num1} % {num2} es: {mod1}")
print(f"El módulo (residuo) de {num2} % {num1} es: {mod2}")
