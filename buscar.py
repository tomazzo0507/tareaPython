frutas = {"pera", "manzana", "tomate", "sandía"}

fruta_buscada = input("Ingresa la fruta a buscar: ")

if fruta_buscada in frutas:
    print(f"La fruta '{fruta_buscada}' SÍ está en la lista.")
else:
    print(f"La fruta '{fruta_buscada}' NO está en la lista.")
