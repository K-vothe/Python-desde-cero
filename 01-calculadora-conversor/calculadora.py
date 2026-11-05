"""
Proyecto Día 1: Calculadora y Conversor de Unidades
Conceptos aprendidos:
- Variables y tipos de datos (int, float, str)
- Entrada de usuario (input) y salida (print)
- Condicionales (if, elif, else)
- Manejo básico de división por cero
- Bucle while para mantener el programa activo
"""

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: No es posible dividir entre cero."
    return a / b

def celsius_a_fahrenheit(celsius):
    # Fórmula: (°C * 9/5) + 32
    return (celsius * 9/5) + 32

def km_a_millas(km):
    # Factor de conversión: 1 km ≈ 0.621371 millas
    return km * 0.621371

def mostrar_menu():
    print("\n" + "=" * 40)
    print("      MI PRIMERA CALCULADORA EN PYTHON")
    print("=" * 40)
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Convertir Celsius a Fahrenheit")
    print("6. Convertir Kilómetros a Millas")
    print("7. Salir")
    print("=" * 40)

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-7): ").strip()

        if opcion == "7":
            print("\n¡Gracias por usar la calculadora! Hasta la próxima.")
            break

        if opcion in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))
            except ValueError:
                print("Error: Por favor ingresa números válidos.")
                continue

            if opcion == "1":
                print(f"Resultado: {num1} + {num2} = {sumar(num1, num2)}")
            elif opcion == "2":
                print(f"Resultado: {num1} - {num2} = {restar(num1, num2)}")
            elif opcion == "3":
                print(f"Resultado: {num1} * {num2} = {multiplicar(num1, num2)}")
            elif opcion == "4":
                resultado = dividir(num1, num2)
                print(f"Resultado: {resultado}")

        elif opcion == "5":
            try:
                c = float(input("Ingresa los grados Celsius: "))
                print(f"{c}°C equivalen a {celsius_a_fahrenheit(c):.2f}°F")
            except ValueError:
                print("Error: Ingresa un valor numérico.")

        elif opcion == "6":
            try:
                km = float(input("Ingresa la distancia en Kilómetros: "))
                print(f"{km} km equivalen a {km_a_millas(km):.2f} millas")
            except ValueError:
                print("Error: Ingresa un valor numérico.")

        else:
            print("Opción inválida. Intenta nuevamente.")

if __name__ == "__main__":
    main()
