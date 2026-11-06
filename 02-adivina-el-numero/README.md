# Día 2: Adivina el Número Secreto (Juego CLI)

Segundo proyecto práctico enfocado en generación de números aleatorios, bucles iterativos y validación de entradas.

## 🎯 Objetivos de aprendizaje
- Uso de la librería estándar `random` (`random.randint`).
- Implementación de bucles `while` con condiciones de corte y límites de intentos.
- Manejo robusto de errores mediante `try/except ValueError` para que el programa nunca falle si el usuario ingresa texto.
- Modularización de código dividiendo la lógica en funciones especializadas (`seleccionar_dificultad`, `jugar_partida`, `main`).

## 🚀 Cómo ejecutar
```bash
python juego_adivinanza.py
```

## 🎮 Características
- 3 niveles de dificultad (Fácil, Medio, Difícil).
- Pistas dinámicas ("mayor" o "menor") en cada intento.
- Contador de intentos restantes en tiempo real.
- Marcador de estadísticas entre partidas jugadas.
