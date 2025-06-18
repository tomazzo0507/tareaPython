from boltons.dictutils import FrozenDict

# Lista donde se guardarán las tareas
tareas = []

print("Bienvenido al registro de tareas con boltons\n")

while True:
    # Captura de datos
    titulo = input("Título de la tarea: ")
    prioridad = input("Prioridad (número entero): ")
    descripcion = input("Descripción de la tarea: ")

    # Validación básica
    if not prioridad.isdigit():
        print("La prioridad debe ser un número entero positivo. Intenta de nuevo.\n")
        continue

    prioridad = int(prioridad)

    # Crear tarea y agregarla como FrozenDict
    tarea = FrozenDict({
        "titulo": titulo,
        "prioridad": prioridad,
        "descripcion": descripcion
    })
    tareas.append(tarea)

    # ¿Desea agregar otra tarea?
    continuar = input("\n¿Deseas agregar otra tarea? (s/n): ").strip().lower()
    if continuar != "s":
        break
    print()

# Ordenar las tareas por prioridad (menor primero)
tareas_ordenadas = sorted(tareas, key=lambda x: x["prioridad"])

# Mostrar tareas ordenadas
print("\nLista de tareas ordenadas por prioridad:\n")
for t in tareas_ordenadas:
    print(f"[{t['prioridad']}] {t['titulo']}: {t['descripcion']}")
