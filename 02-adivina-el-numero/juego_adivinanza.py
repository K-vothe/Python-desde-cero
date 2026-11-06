"""
Proyecto Día 2: Juego Adivina el Número Secreto
Conceptos aprendidos:
- Importación y uso de módulos estándar (random)
- Bucles while y contadores de intentos
- Niveles de dificultad con rangos y límites
- Manejo de excepciones (try / except) para validar entradas
- Lógica de juego interactivo en consola
"""

import random

def seleccionar_dificultad():
    print("\nSelecciona un nivel de dificultad:")
    print("1. Fácil (Rango 1-50, 10 intentos)")
    print("2. Medio (Rango 1-100, 7 intentos)")
    print("3. Difícil (Rango 1-200, 5 intentos)")

    while True:
        opcion = input("Elige tu dificultad (1-3): ").strip()
        if opcion == "1":
            return 50, 10
        elif opcion == "2":
            return 100, 7
        elif opcion == "3":
            return 200, 5
        print("Opción inválida. Ingresa 1, 2 o 3.")

def jugar_partida():
    rango_maximo, intentos_maximos = seleccionar_dificultad()
    numero_secreto = random.randint(1, rango_maximo)
    intentos_realizados = 0

    print(f"\n¡He elegido un número entre 1 y {rango_maximo}!")
    print(f"Tienes {intentos_maximos} intentos para adivinarlo. ¡Buena suerte!\n")

    while intentos_realizados < intentos_maximos:
        intentos_restantes = intentos_maximos - intentos_realizados
        try:
            intento = int(input(f"[Intento {intentos_realizados + 1} | Quedan {intentos_restantes}] Tu número: "))
        except ValueError:
            print("⚠️ Entrada inválida: Por favor ingresa un número entero.\n")
            continue

        if intento < 1 or intento > rango_maximo:
            print(f"⚠️ El número debe estar entre 1 y {rango_maximo}.\n")
            continue

        intentos_realizados += 1

        if intento == numero_secreto:
            print(f"\n🎉 ¡EXCELENTE! Adivinaste el número {numero_secreto} en {intentos_realizados} intentos.")
            return True
        elif intento < numero_secreto:
            print("⬆️  Pista: El número secreto es MAYOR.")
        else:
            print("⬇️  Pista: El número secreto es MENOR.")

        print("-" * 35)

    print(f"\n💀 Te quedaste sin intentos. El número secreto era: {numero_secreto}")
    return False

def main():
    print("=" * 50)
    print("       🎯 JUEGO: ADIVINA EL NÚMERO SECRETO")
    print("=" * 50)

    partidas_ganadas = 0
    total_partidas = 0

    while True:
        total_partidas += 1
        gano = jugar_partida()
        if gano:
            partidas_ganadas += 1

        print(f"\nEstadísticas: Partidas ganadas: {partidas_ganadas}/{total_partidas}")
        repetir = input("\n¿Deseas jugar otra vez? (s/n): ").strip().lower()
        if repetir != "s":
            print("\n¡Gracias por jugar! Sigue practicando tu lógica de programación.")
            break

if __name__ == "__main__":
    main()
