"""
Proyecto Día 4: Gestor de Tareas Pendientes (CLI To-Do List)
Conceptos aprendidos:
- Manejo de estructuras de datos compuestas (listas de diccionarios)
- Persistencia de datos en disco usando el módulo estándar `json`
- Operaciones CRUD (Crear, Leer, Actualizar, Borrar)
- Uso de `enumerate()` y funciones con retorno de estado
- Manejo de excepciones al trabajar con archivos (`FileNotFoundError`)
"""

import json
import os
from datetime import datetime

ARCHIVO_TAREAS = "tareas.json"

def cargar_tareas():
    """Lee el archivo JSON de tareas si existe; si no, retorna una lista vacía."""
    if not os.path.exists(ARCHIVO_TAREAS):
        return []
    try:
        with open(ARCHIVO_TAREAS, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        print("⚠️ Advertencia: No se pudo leer el archivo de tareas. Iniciando lista vacía.")
        return []

def guardar_tareas(tareas):
    """Escribe la lista actual de tareas en formato JSON con indentación legible."""
    try:
        with open(ARCHIVO_TAREAS, "w", encoding="utf-8") as f:
            json.dump(tareas, f, indent=4, ensure_ascii=False)
    except IOError as e:
        print(f"❌ Error al guardar tareas en disco: {e}")

def listar_tareas(tareas):
    """Muestra todas las tareas registradas con su estado y fecha de creación."""
    print("\n" + "=" * 55)
    print("                📋 LISTA DE TAREAS")
    print("=" * 55)
    if not tareas:
        print("No tienes tareas pendientes. ¡Buen trabajo!")
        print("=" * 55)
        return

    for idx, tarea in enumerate(tareas, start=1):
        estado = "[✓] Completada" if tarea.get("completada") else "[ ] Pendiente "
        titulo = tarea.get("titulo", "Sin título")
        fecha = tarea.get("creada_el", "N/D")
        print(f"{idx}. {estado} | {titulo:<25} (Creada: {fecha})")
    print("=" * 55)

def agregar_tarea(tareas):
    """Solicita el nombre de una tarea y la añade a la lista."""
    titulo = input("\nDescripción de la nueva tarea: ").strip()
    if not titulo:
        print("⚠️ La descripción no puede estar vacía.")
        return

    nueva_tarea = {
        "titulo": titulo,
        "completada": False,
        "creada_el": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    tareas.append(nueva_tarea)
    guardar_tareas(tareas)
    print(f"✅ Tarea agregada con éxito: '{titulo}'")

def marcar_completada(tareas):
    """Marca una tarea pendiente como completada por su número en la lista."""
    listar_tareas(tareas)
    if not tareas:
        return

    try:
        numero = int(input("\nIngresa el número de la tarea a marcar como completada: "))
        if 1 <= numero <= len(tareas):
            tarea = tareas[numero - 1]
            if tarea["completada"]:
                print("ℹ️ Esta tarea ya estaba marcada como completada.")
            else:
                tarea["completada"] = True
                guardar_tareas(tareas)
                print(f"🎉 ¡Genial! Tarea '{tarea['titulo']}' marcada como completada.")
        else:
            print("⚠️ Número fuera de rango.")
    except ValueError:
        print("⚠️ Ingresa un número válido.")

def eliminar_tarea(tareas):
    """Elimina permanentemente una tarea por su índice."""
    listar_tareas(tareas)
    if not tareas:
        return

    try:
        numero = int(input("\nIngresa el número de la tarea a eliminar: "))
        if 1 <= numero <= len(tareas):
            eliminada = tareas.pop(numero - 1)
            guardar_tareas(tareas)
            print(f"🗑️ Tarea '{eliminada['titulo']}' eliminada correctamente.")
        else:
            print("⚠️ Número fuera de rango.")
    except ValueError:
        print("⚠️ Ingresa un número válido.")

def main():
    tareas = cargar_tareas()

    while True:
        print("\n" + "-" * 40)
        print("         GESTIÓN DE TAREAS")
        print("-" * 40)
        print("1. Listar tareas")
        print("2. Agregar nueva tarea")
        print("3. Marcar tarea como completada")
        print("4. Eliminar tarea")
        print("5. Salir")
        print("-" * 40)

        opcion = input("Elige una opción (1-5): ").strip()

        if opcion == "1":
            listar_tareas(tareas)
        elif opcion == "2":
            agregar_tarea(tareas)
        elif opcion == "3":
            marcar_completada(tareas)
        elif opcion == "4":
            eliminar_tarea(tareas)
        elif opcion == "5":
            print("\n¡Hasta luego! Tus tareas se han guardado automáticamente.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
