"""
funciones.py - Archivo centralizado con todas las funciones del sistema.
Contiene funciones para CRUD, validación, búsqueda y persistencia de tareas.

Compatibilidad: Python 3.8+
"""

# ============================================================================
# FUNCIONES DE VALIDACIÓN
# ============================================================================


def validar_titulo(titulo):
    """
    Valida que el título no esté vacío y tenga longitud válida.

    Parámetros:
        titulo (str): Título a validar.

    Retorna:
        tuple: (es_válido: bool, mensaje: str)
    """
    if not titulo or not titulo.strip():
        return False, "El título no puede estar vacío."
    if len(titulo) > 100:
        return False, "El título no puede exceder 100 caracteres."
    return True, "Título válido."


def validar_descripcion(descripcion):
    """
    Valida que la descripción tenga longitud válida.

    Parámetros:
        descripcion (str): Descripción a validar.

    Retorna:
        tuple: (es_válido: bool, mensaje: str)
    """
    if not descripcion or not descripcion.strip():
        return False, "La descripción no puede estar vacía."
    if len(descripcion) > 500:
        return False, "La descripción no puede exceder 500 caracteres."
    return True, "Descripción válida."


def validar_estado(estado):
    """
    Valida que el estado sea un número válido (1-3).

    Mapeo: 1=pendiente, 2=en_progreso, 3=completada

    Parámetros:
        estado (str): Estado a validar (número 1-3).

    Retorna:
        tuple: (es_válido: bool, estado_convertido: str o None)
    """
    try:
        num_estado = int(estado.strip())
        mapeo_estados = {1: "pendiente", 2: "en_progreso", 3: "completada"}

        if num_estado in mapeo_estados:
            return True, mapeo_estados[num_estado]
        return False, None
    except ValueError:
        return False, None


def validar_prioridad(prioridad):
    """
    Valida que la prioridad sea un número válido (1-3).

    Mapeo: 1=baja, 2=media, 3=alta

    Parámetros:
        prioridad (str): Prioridad a validar (número 1-3).

    Retorna:
        tuple: (es_válido: bool, prioridad_convertida: str o None)
    """
    try:
        num_prioridad = int(prioridad.strip())
        mapeo_prioridades = {1: "baja", 2: "media", 3: "alta"}

        if num_prioridad in mapeo_prioridades:
            return True, mapeo_prioridades[num_prioridad]
        return False, None
    except ValueError:
        return False, None


def validar_id(id_str):
    """
    Valida que el ID sea un número entero válido.

    Parámetros:
        id_str (str): ID a validar como string.

    Retorna:
        tuple: (es_válido: bool, id_convertido: int o None)
    """
    try:
        id_num = int(id_str)
        if id_num > 0:
            return True, id_num
        return False, None
    except ValueError:
        return False, None


# ============================================================================
# FUNCIONES DE PERSISTENCIA
# ============================================================================


def guardar_tareas(tareas, archivo="tareas.txt"):
    """
    Guarda las tareas en un archivo de texto.

    Parámetros:
        tareas (list): Lista de diccionarios con las tareas.
        archivo (str): Nombre del archivo donde guardar. Por defecto 'tareas.txt'.
    """
    try:
        with open(archivo, "w", encoding="utf-8") as f:
            for tarea in tareas:
                # Formato: id|titulo|descripcion|estado|prioridad
                linea = f"{tarea['id']}|{tarea['titulo']}|{tarea['descripcion']}|{tarea['estado']}|{tarea['prioridad']}\n"
                f.write(linea)
    except IOError as e:
        print(f"Error al guardar tareas: {e}")


def cargar_tareas(archivo="tareas.txt"):
    """
    Carga las tareas desde un archivo de texto.

    Parámetros:
        archivo (str): Nombre del archivo a cargar. Por defecto 'tareas.txt'.

    Retorna:
        list: Lista de diccionarios con las tareas cargadas.
    """
    tareas = []
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if linea:
                    # Desglosar formato: id|titulo|descripcion|estado|prioridad
                    partes = linea.split("|")
                    if len(partes) == 5:
                        tarea = {
                            "id": int(partes[0]),
                            "titulo": partes[1],
                            "descripcion": partes[2],
                            "estado": partes[3],
                            "prioridad": partes[4],
                        }
                        tareas.append(tarea)
    except FileNotFoundError:
        # Si el archivo no existe, retorna lista vacía
        pass
    except IOError as e:
        print(f"Error al cargar tareas: {e}")

    return tareas


# ============================================================================
# FUNCIONES CRUD
# ============================================================================


def obtener_proximo_id(tareas):
    """
    Obtiene el próximo ID disponible para una nueva tarea.

    Parámetros:
        tareas (list): Lista actual de tareas.

    Retorna:
        int: Próximo ID a utilizar.
    """
    if not tareas:
        return 1
    # Usar recursión para encontrar el máximo ID
    return max_id_recursivo(tareas, 0) + 1


def max_id_recursivo(tareas, indice=0, max_actual=0):
    """
    Función recursiva para encontrar el ID máximo en la lista.

    Parámetros:
        tareas (list): Lista de tareas.
        indice (int): Índice actual en la recursión.
        max_actual (int): Máximo encontrado hasta ahora.

    Retorna:
        int: ID máximo en la lista.
    """
    # Caso base: si llegamos al final de la lista, retornar máximo
    if indice >= len(tareas):
        return max_actual

    # Comparar el ID actual con el máximo
    if tareas[indice]["id"] > max_actual:
        max_actual = tareas[indice]["id"]

    # Recursión: pasar al siguiente elemento
    return max_id_recursivo(tareas, indice + 1, max_actual)


def crear_tarea(tareas, titulo, descripcion, estado, prioridad):
    """
    Crea una nueva tarea y la agrega a la lista.

    Parámetros:
        tareas (list): Lista actual de tareas.
        titulo (str): Título de la tarea.
        descripcion (str): Descripción de la tarea.
        estado (str): Estado inicial de la tarea.
        prioridad (str): Prioridad de la tarea.

    Retorna:
        dict: La tarea creada.
    """
    nueva_tarea = {
        "id": obtener_proximo_id(tareas),
        "titulo": titulo,
        "descripcion": descripcion,
        "estado": estado.lower(),
        "prioridad": prioridad.lower(),
    }
    tareas.append(nueva_tarea)
    return nueva_tarea


def obtener_tarea_por_id(tareas, tarea_id):
    """
    Busca una tarea específica por su ID.

    Parámetros:
        tareas (list): Lista de tareas.
        tarea_id (int): ID de la tarea a buscar.

    Retorna:
        dict o None: La tarea si existe, None en caso contrario.
    """
    for tarea in tareas:
        if tarea["id"] == tarea_id:
            return tarea
    return None


def actualizar_tarea(
    tareas, tarea_id, titulo=None, descripcion=None, estado=None, prioridad=None
):
    """
    Actualiza los datos de una tarea existente.

    Parámetros:
        tareas (list): Lista de tareas.
        tarea_id (int): ID de la tarea a actualizar.
        titulo (str, optional): Nuevo título.
        descripcion (str, optional): Nueva descripción.
        estado (str, optional): Nuevo estado.
        prioridad (str, optional): Nueva prioridad.

    Retorna:
        bool: True si la tarea fue actualizada, False si no existe.
    """
    tarea = obtener_tarea_por_id(tareas, tarea_id)

    if tarea is None:
        return False

    # Actualizar solo los campos proporcionados
    if titulo is not None:
        tarea["titulo"] = titulo
    if descripcion is not None:
        tarea["descripcion"] = descripcion
    if estado is not None:
        tarea["estado"] = estado.lower()
    if prioridad is not None:
        tarea["prioridad"] = prioridad.lower()

    return True


def eliminar_tarea(tareas, tarea_id):
    """
    Elimina una tarea del sistema.

    Parámetros:
        tareas (list): Lista de tareas.
        tarea_id (int): ID de la tarea a eliminar.

    Retorna:
        bool: True si la tarea fue eliminada, False si no existe.
    """
    for i, tarea in enumerate(tareas):
        if tarea["id"] == tarea_id:
            tareas.pop(i)
            return True
    return False


# ============================================================================
# FUNCIONES DE BÚSQUEDA Y FILTRADO
# ============================================================================


def buscar_por_titulo(tareas, titulo_busqueda):
    """
    Busca tareas que contengan el título especificado (búsqueda parcial).

    Parámetros:
        tareas (list): Lista de tareas.
        titulo_busqueda (str): Término a buscar en los títulos.

    Retorna:
        list: Lista de tareas que coinciden con la búsqueda.
    """
    titulo_lower = titulo_busqueda.lower()
    resultados = []

    # Usar for para iterar
    for tarea in tareas:
        if titulo_lower in tarea["titulo"].lower():
            resultados.append(tarea)

    return resultados


def filtrar_por_estado(tareas, estado):
    """
    Filtra las tareas por estado.

    Parámetros:
        tareas (list): Lista de tareas.
        estado (str): Estado por el cual filtrar.

    Retorna:
        list: Lista de tareas que coinciden con el estado.
    """
    estado_lower = estado.lower()
    resultados = []

    # Usar for para iterar
    for tarea in tareas:
        if tarea["estado"] == estado_lower:
            resultados.append(tarea)

    return resultados


def filtrar_por_prioridad(tareas, prioridad):
    """
    Filtra las tareas por nivel de prioridad.

    Parámetros:
        tareas (list): Lista de tareas.
        prioridad (str): Prioridad por la cual filtrar.

    Retorna:
        list: Lista de tareas que coinciden con la prioridad.
    """
    prioridad_lower = prioridad.lower()
    resultados = []

    # Usar for para iterar
    for tarea in tareas:
        if tarea["prioridad"] == prioridad_lower:
            resultados.append(tarea)

    return resultados


# ============================================================================
# FUNCIONES DE ESTADÍSTICAS
# ============================================================================


def obtener_estadisticas(tareas):
    """
    Calcula estadísticas sobre las tareas registradas.

    Parámetros:
        tareas (list): Lista de tareas.

    Retorna:
        dict: Diccionario con estadísticas del sistema.
    """
    total_tareas = len(tareas)

    # Contar tareas por estado
    pendientes = len(filtrar_por_estado(tareas, "pendiente"))
    en_progreso = len(filtrar_por_estado(tareas, "en_progreso"))
    completadas = len(filtrar_por_estado(tareas, "completada"))

    # Contar tareas por prioridad
    baja = len(filtrar_por_prioridad(tareas, "baja"))
    media = len(filtrar_por_prioridad(tareas, "media"))
    alta = len(filtrar_por_prioridad(tareas, "alta"))

    # Calcular tasa de finalización
    tasa_finalizacion = (completadas / total_tareas * 100) if total_tareas > 0 else 0

    return {
        "total_tareas": total_tareas,
        "pendientes": pendientes,
        "en_progreso": en_progreso,
        "completadas": completadas,
        "baja": baja,
        "media": media,
        "alta": alta,
        "tasa_finalizacion": tasa_finalizacion,
    }


# ============================================================================
# FUNCIONES DE VISUALIZACIÓN
# ============================================================================


def mostrar_tarea(tarea):
    """
    Muestra una tarea con formato legible.

    Parámetros:
        tarea (dict): Diccionario con los datos de la tarea.
    """
    print(f"\n  ID: {tarea['id']}")
    print(f"  Título: {tarea['titulo']}")
    print(f"  Descripción: {tarea['descripcion']}")
    print(f"  Estado: {tarea['estado'].replace('_', ' ').upper()}")
    print(f"  Prioridad: {tarea['prioridad'].upper()}")
    print("  " + "-" * 60)


def mostrar_tareas(tareas, titulo="TAREAS"):
    """
    Muestra múltiples tareas con formato.

    Parámetros:
        tareas (list): Lista de tareas a mostrar.
        titulo (str): Título de la sección.
    """
    print("\n" + "=" * 70)
    print(titulo)
    print("=" * 70)

    if not tareas:
        print("\nNo hay tareas para mostrar.\n")
        return

    for tarea in tareas:
        mostrar_tarea(tarea)
    print()


def mostrar_menu():
    """
    Muestra el menú principal en consola.
    """
    print("\n" + "=" * 70)
    print("SISTEMA DE GESTIÓN DE TAREAS - MENÚ PRINCIPAL")
    print("=" * 70)
    print("1. Crear nueva tarea")
    print("2. Ver todas las tareas")
    print("3. Buscar tarea por título")
    print("4. Filtrar tareas por estado")
    print("5. Filtrar tareas por prioridad")
    print("6. Actualizar tarea")
    print("7. Eliminar tarea")
    print("8. Ver estadísticas")
    print("0. Salir")
    print("=" * 70)
