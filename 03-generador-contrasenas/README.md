# Día 3: Generador de Contraseñas Seguras (CLI)

Tercer proyecto práctico donde exploramos la manipulación de cadenas, listas y la diferencia entre números pseudoaleatorios y seguridad criptográfica.

## 🎯 Objetivos de aprendizaje
- Descubrir la diferencia entre el módulo `random` (para juegos/simulaciones) y `secrets` (para criptografía y seguridad).
- Uso del módulo `string` (`ascii_lowercase`, `ascii_uppercase`, `digits`).
- Técnicas de listas: `.append()`, `.extend()`, `.join()` y mezcla aleatoria (`random.shuffle`).
- Algoritmo de garantía de tipos (asegurar al menos 1 número, 1 mayúscula y 1 símbolo si fueron solicitados).
- Función de auditoría/evaluación simple de robustez de contraseñas.

## 🚀 Cómo ejecutar
```bash
python generador_passwords.py
```

## 🔐 Características
- Longitud personalizable (con alerta si es menor a 6 caracteres).
- Filtros opcionales para mayúsculas, dígitos y símbolos.
- Generación con aleatoriedad criptográfica (`secrets`).
- Medidor visual de seguridad (Débil, Media, Muy Fuerte).
