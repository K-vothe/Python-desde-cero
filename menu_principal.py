"""
Día 5: Menú Centralizador de Proyectos
Permite ejecutar de forma interactiva cualquiera de los mini-proyectos desarrollados
durante estos primeros 5 días de aprendizaje.
"""

import subprocess
import sys
import os

PROYECTOS = {
    "1": ("Calculadora y Conversor de Unidades", os.path.join("01-calculadora-conversor", "calculadora.py")),
    "2": ("Juego: Adivina el Número Secreto", os.path.join("02-adivina-el-numero", "juego_adivinanza.py")),
    "3": ("Generador de Contraseñas Seguras", os.path.join("03-generador-contrasenas", "generador_passwords.py")),
    "4": ("Gestor de Tareas Pendientes (To-Do List)", os.path.join("04-gestor-tareas-todo", "gestor_tareas.py")),
}

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    while True:
        print("\n" + "=" * 60)
        print("     🚀 MI RUTA DE APRENDIZAJE PYTHON - PANEL PRINCIPAL")
        print("=" * 60)
        for clave, (nombre, _) in PROYECTOS.items():
            print(f"[{clave}] Día {clave}: {nombre}")
        print("[5] Salir")
        print("=" * 60)

        opcion = input("Selecciona qué proyecto deseas probar (1-5): ").strip()

        if opcion == "5":
            print("\n¡Gracias por revisar mis proyectos! Nos vemos en el Día 6. 🐍\n")
            break

        if opcion in PROYECTOS:
            nombre, ruta = PROYECTOS[opcion]
            print(f"\n▶️ Ejecutando: {nombre}...\n")
            try:
                # Ejecutamos el script correspondiente en su propio contexto
                directorio = os.path.dirname(ruta)
                script = os.path.basename(ruta)
                subprocess.run([sys.executable, script], cwd=directorio, check=True)
            except Exception as e:
                print(f"❌ Error al ejecutar el script: {e}")
        else:
            print("⚠️ Opción no válida. Ingresa un número del 1 al 5.")

if __name__ == "__main__":
    main()
