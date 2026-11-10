# 🐍 Mi Ruta de Aprendizaje en Python (Desde Cero)

¡Hola! 👋 Este repositorio documenta mi proceso de aprendizaje de **Python desde cero**, construyendo proyectos prácticos diarios para consolidar fundamentos de programación, estructuras de datos, modularización y buenas prácticas de desarrollo.

---

## 🗓️ Bitácora de Progreso (Primeros 5 Días)

| Día | Proyecto | Temas y Conceptos Aprendidos | Estado |
|:---:|:---|:---|:---:|
| **01** | [Calculadora y Conversor CLI](./01-calculadora-conversor) | Tipos de datos (`int`, `float`, `str`), entrada y salida (`input`/`print`), control de flujo (`if`/`elif`/`else`), funciones y control básico de división por cero. | ✅ Completado |
| **02** | [Adivina el Número Secreto](./02-adivina-el-numero) | Librería estándar `random`, bucles `while`, contadores, niveles de dificultad y validación robusta con `try/except ValueError`. | ✅ Completado |
| **03** | [Generador de Contraseñas](./03-generador-contrasenas) | Seguridad y números pseudoaleatorios vs criptográficos (`secrets`), manipulación de cadenas con `string`, listas y mezclas (`random.shuffle`). | ✅ Completado |
| **04** | [Gestor de Tareas To-Do](./04-gestor-tareas-todo) | Estructuras de datos complejas (listas de diccionarios), persistencia en disco con `json`, operaciones CRUD y fechas con `datetime`. | ✅ Completado |
| **05** | [Panel Centralizador](./menu_principal.py) | Modularización de proyectos, ejecución de subprocesos (`subprocess`), gestión de rutas con `os.path` e integración general. | ✅ Completado |

---

## ⚡ Ejecución Rápida

Puedes probar cualquiera de los proyectos lanzando el panel principal:

```bash
python menu_principal.py
```

O ingresar directamente a la carpeta de cada día:

```bash
# Ejemplo: probar el generador de contraseñas
cd 03-generador-contrasenas
python generador_passwords.py
```

---

## 🧠 Buenas Prácticas Aplicadas
- **Nombres descriptivos:** Variables y funciones con nombres claros en lugar de abreviaciones ambiguas.
- **Manejo de errores:** Bloques `try/except` para prevenir caídas por entradas inválidas del usuario.
- **Legibilidad (PEP 8):** Código formateado, espaciado uniforme y comentarios explicativos.
- **Control de versiones:** Commits semánticos y organizados por etapas de desarrollo.

---

## 🎯 Próximos Pasos (Roadmap)
- [ ] **Día 6:** Consumo de APIs REST públicas con la librería `requests`.
- [ ] **Día 7:** Introducción a la Programación Orientada a Objetos (POO) y Clases.
- [ ] **Día 8:** Manejo de datos y lectura de archivos CSV / Excel.
