# Día 4: Gestor de Tareas Pendientes (CLI To-Do List)

Cuarto proyecto práctico que introduce la persistencia en disco de datos y operaciones CRUD (Create, Read, Update, Delete).

## 🎯 Objetivos de aprendizaje
- Manejo de estructuras de datos complejas: listas con diccionarios internos.
- Persistencia de archivos usando el módulo `json` (`json.dump` y `json.load`).
- Manejo seguro de archivos con contexto `with open(...)`.
- Métodos de listas como `.append()`, `.pop()` y uso de `enumerate()`.
- Marcado de fechas con `datetime.now()`.

## 🚀 Cómo ejecutar
```bash
python gestor_tareas.py
```

## 📋 Funcionalidades
- **Listar tareas:** Muestra un resumen formateado de pendientes y completadas con su fecha.
- **Agregar tarea:** Añade una nueva tarea y la persiste en `tareas.json`.
- **Completar tarea:** Cambia el estado de `[ ] Pendiente` a `[✓] Completada`.
- **Eliminar tarea:** Elimina el elemento de la lista y actualiza el archivo en disco.
- **Persistencia automática:** Todo cambio queda guardado entre ejecuciones.
