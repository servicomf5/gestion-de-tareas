# Sistema de Gestión de Tareas

## Descripción

Sistema simple de gestión de tareas desarrollado en Python.
Permite crear, ver, actualizar y eliminar tareas con validaciones, búsquedas,
filtrados y estadísticas.

## Requisitos

- Python 3.8 o superior
- No requiere instalación de dependencias externas (usa solo librería estándar)

## Instalación

1. Coloca los archivos en una carpeta:

   - `app.py` - Programa principal
   - `funciones.py` - Módulo con todas las funciones
   - `tareas.txt` - Base de datos de tareas (se crea automáticamente)

2. No requiere instalación adicional.

## Uso

Para ejecutar el programa:

```bash
python app.py
```

## Funcionalidades

### 1. Crear Nueva Tarea

- Ingresa título, descripción, estado y prioridad
- Las validaciones garantizan datos correctos
- Las tareas se guardan automáticamente

### 2. Ver Todas las Tareas

- Muestra todas las tareas registradas en el sistema
- Formato visual con separadores para legibilidad

### 3. Buscar Tarea por Título

- Busca tareas que contengan el término ingresado
- Búsqueda insensible a mayúsculas/minúsculas

### 4. Filtrar por Estado

- Muestra solo tareas con estado específico
- Estados disponibles: pendiente, en_progreso, completada

### 5. Filtrar por Prioridad

- Muestra solo tareas con prioridad específica
- Prioridades disponibles: baja, media, alta

### 6. Actualizar Tarea

- Modifica los datos de una tarea existente
- Presiona Enter para mantener el valor actual
- Se guardan los cambios automáticamente

### 7. Eliminar Tarea

- Elimina una tarea del sistema
- Pide confirmación antes de proceder
- Se guardan los cambios automáticamente

### 8. Ver Estadísticas

- Muestra:
  - Total de tareas
  - Cantidad por estado (pendiente, en_progreso, completada)
  - Cantidad por prioridad (baja, media, alta)
  - Tasa de finalización en porcentaje

### 0. Salir

- Cierra el programa

## Estructura de Datos

Las tareas se almacenan en `tareas.txt` en formato texto plano:

```
id|titulo|descripcion|estado|prioridad
```

Ejemplo:

```
1|Comprar leche|Ir al supermercado por leche|pendiente|media
2|Hacer tarea|Resolver ejercicios de Python|en_progreso|alta
```

## Conceptos Python Utilizados

El programa demuestra:

- ✅ **Funciones**: Múltiples funciones con parámetros y valores de retorno
- ✅ **Estructuras de control**: If/elif/else, while, for, break
- ✅ **Estructuras de datos**: Listas, diccionarios, tuplas
- ✅ **Validaciones**: Todas las entradas se validan
- ✅ **Recursión**: Función `max_id_recursivo()` implementada recursivamente
- ✅ **Manejo de archivos**: Lectura y escritura en `tareas.txt`
- ✅ **Entrada/Salida**: Input() y print() para interacción
- ✅ **Modularización**: Todas las funciones centralizadas en `funciones.py`
- ✅ **Buenas prácticas**: PEP 8, docstrings, comentarios en español

## Ejemplo de Uso

```
== MENÚ PRINCIPAL ==
1. Crear nueva tarea
2. Ver todas las tareas
3. Buscar tarea por título
4. Filtrar por estado
5. Filtrar por prioridad
6. Actualizar tarea
7. Eliminar tarea
8. Ver estadísticas
0. Salir

Seleccione una opción: 1

=== CREAR NUEVA TAREA ===
Ingrese el título: Estudiar Python
Ingrese la descripción: Aprender funciones y estructuras de datos
Seleccione el estado: pendiente
Seleccione la prioridad: alta

✓ Tarea creada exitosamente con ID: 1
```

## Archivos del Proyecto

- **app.py**: Punto de entrada principal del programa
- **funciones.py**: Módulo centralizado con todas las funciones:
  - Validaciones (título, descripción, estado, prioridad, ID)
  - CRUD (crear, obtener, actualizar, eliminar)
  - Búsqueda y filtrado
  - Estadísticas
  - Persistencia (guardar/cargar)
  - Visualización (mostrar tareas, menú)
- **tareas.txt**: Base de datos en formato texto plano
- **README.md**: Este archivo de documentación

## Notas Importantes

- El programa guarda automáticamente los cambios en `tareas.txt`
- Los IDs se asignan automáticamente comenzando desde 1
- No se puede actualizar el ID de una tarea (es identificador único)
- La búsqueda por título es parcial (no requiere coincidencia exacta)
- Los estados y prioridades deben ingresarse con guiones múmeros para minimizar el error: 1, 2 ó 3

## Mejoras Futuras (Más Allá del Scope Actual)

- Base de datos SQL (SQLite)
- Interfaz gráfica (tkinter)
- Sistema de usuarios con autenticación
- Exportación a CSV/JSON
- Categorías o proyectos
- Comentarios y notas en tareas
- Historial de cambios
- Recordatorios por correo
- API REST

## Autor

Desarrollado por Eduardo Muñoz como proyecto del bootcamp de Python - Módulo 3

## Licencia

Este código es educativo y puede ser usado libremente en el bootcamp.
