"""
Proyecto Día 3: Generador de Contraseñas Seguras
Conceptos aprendidos:
- Módulos estándar: `string` y `secrets` (generación criptográficamente segura)
- Manipulación de listas y cadenas (método .join, shuffle)
- Lógica de validación de reglas de seguridad
- Estimación básica de fortaleza de contraseña
"""

import string
import secrets
import random

def pedir_confirmacion(pregunta):
    """Solicita al usuario una respuesta s/n devolviendo un booleano."""
    while True:
        respuesta = input(f"{pregunta} (s/n): ").strip().lower()
        if respuesta in ["s", "si", "y", "yes"]:
            return True
        elif respuesta in ["n", "no"]:
            return False
        print("Por favor responde con 's' o 'n'.")

def evaluar_fortaleza(longitud, usa_mayus, usa_nums, usa_simb):
    """Determina la robustez de la contraseña generada."""
    puntuacion = 0
    if longitud >= 12:
        puntuacion += 2
    elif longitud >= 8:
        puntuacion += 1

    if usa_mayus:
        puntuacion += 1
    if usa_nums:
        puntuacion += 1
    if usa_simb:
        puntuacion += 1

    if puntuacion <= 2:
        return "🔴 Débil"
    elif puntuacion <= 4:
        return "🟡 Media"
    else:
        return "🟢 Muy Fuerte"

def generar_contrasena(longitud, incluir_mayus=True, incluir_numeros=True, incluir_simbolos=True):
    # Base: siempre incluimos minúsculas
    caracteres_disponibles = list(string.ascii_lowercase)
    password_caracteres = [secrets.choice(string.ascii_lowercase)]

    if incluir_mayus:
        caracteres_disponibles.extend(string.ascii_uppercase)
        password_caracteres.append(secrets.choice(string.ascii_uppercase))

    if incluir_numeros:
        caracteres_disponibles.extend(string.digits)
        password_caracteres.append(secrets.choice(string.digits))

    if incluir_simbolos:
        simbolos = "!@#$%^&*()-_=+[]{}<>?"
        caracteres_disponibles.extend(simbolos)
        password_caracteres.append(secrets.choice(simbolos))

    # Completar el resto de la longitud deseada
    caracteres_restantes = longitud - len(password_caracteres)
    for _ in range(caracteres_restantes):
        password_caracteres.append(secrets.choice(caracteres_disponibles))

    # Mezclar los caracteres para que el orden inicial no sea predecible
    random.shuffle(password_caracteres)
    return "".join(password_caracteres)

def main():
    print("=" * 55)
    print("      🔐 GENERADOR DE CONTRASEÑAS SEGURAS (CLI)")
    print("=" * 55)

    while True:
        try:
            longitud = int(input("\nIngresa la longitud deseada (mínimo 6, recomendado 12+): "))
            if longitud < 6:
                print("⚠️ La longitud mínima recomendada por seguridad es de 6 caracteres.")
                continue
        except ValueError:
            print("⚠️ Entrada inválida: ingresa un número entero.")
            continue

        print("\nConfigura las opciones de complejidad:")
        incluir_mayus = pedir_confirmacion("¿Incluir letras mayúsculas?")
        incluir_numeros = pedir_confirmacion("¿Incluir números?")
        incluir_simbolos = pedir_confirmacion("¿Incluir símbolos especiales?")

        password = generar_contrasena(longitud, incluir_mayus, incluir_numeros, incluir_simbolos)
        fortaleza = evaluar_fortaleza(longitud, incluir_mayus, incluir_numeros, incluir_simbolos)

        print("\n" + "-" * 55)
        print(f"🔑 Tu contraseña generada: {password}")
        print(f"🛡️  Nivel de seguridad:     {fortaleza}")
        print("-" * 55)

        otra = pedir_confirmacion("\n¿Deseas generar otra contraseña?")
        if not otra:
            print("\n¡Recuerda almacenar tus contraseñas en un gestor seguro! 👋")
            break

if __name__ == "__main__":
    main()
