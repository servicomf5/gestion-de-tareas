"""
app.py - Punto de entrada principal del Sistema de Gestión de Tareas.

Este archivo contiene el programa principal que utiliza las funciones
del módulo funciones.py para manejar el sistema de tareas.

Compatibilidad: Python 3.8+
Uso: python app.py
"""

# Importar todas las funciones del módulo centralizado
from funciones import (
    validar_titulo,
    validar_descripcion,
    validar_estado,
    validar_prioridad,
    validar_id,
    guardar_tareas,
    cargar_tareas,
    crear_tarea,
    obtener_tarea_por_id,
    actualizar_tarea,
    eliminar_tarea,
    buscar_por_titulo,
    filtrar_por_estado,
    filtrar_por_prioridad,
    obtener_estadisticas,
    mostrar_tarea,
    mostrar_tareas,
    mostrar_menu,
)


def main():
    """
    Función principal que ejecuta el programa.
    """
    # Cargar tareas existentes al iniciar
    tareas = cargar_tareas("tareas.txt")

    # Mostrar bienvenida
    print("\n" + "=" * 70)
    print("BIENVENIDO AL SISTEMA DE GESTIÓN DE TAREAS".center(70))
    print("=" * 70 + "\n")

    # Bucle principal del programa
    ejecutando = True
    while ejecutando:
        # Mostrar menú
        mostrar_menu()

        # Obtener opción del usuario
        opcion = input("\nSeleccione una opción (0-8): ").strip()

        # OPCIÓN 1: Crear nueva tarea
        if opcion == "1":
            print("\n" + "=" * 70)
            print("CREAR NUEVA TAREA")
            print("=" * 70)

            # Validar título
            while True:
                titulo = input("\nIngrese el título de la tarea: ").strip()
                es_valido, mensaje = validar_titulo(titulo)
                if es_valido:
                    break
                print(f"⚠ {mensaje}")

            # Validar descripción
            while True:
                descripcion = input("Ingrese la descripción: ").strip()
                es_valido, mensaje = validar_descripcion(descripcion)
                if es_valido:
                    break
                print(f"⚠ {mensaje}")

            # Validar estado
            while True:
                print("\nEstados disponibles:")
                print("  1. Pendiente")
                print("  2. En progreso")
                print("  3. Completada")
                estado_opcion = input("Seleccione el estado (1-3): ").strip()
                es_valido, estado = validar_estado(estado_opcion)
                if es_valido:
                    break
                print("⚠ Estado inválido. Ingrese un número entre 1 y 3.")

            # Validar prioridad
            while True:
                print("\nPrioridades disponibles:")
                print("  1. Baja")
                print("  2. Media")
                print("  3. Alta")
                prioridad_opcion = input("Seleccione la prioridad (1-3): ").strip()
                es_valido, prioridad = validar_prioridad(prioridad_opcion)
                if es_valido:
                    break
                print("⚠ Prioridad inválida. Ingrese un número entre 1 y 3.")

            # Crear la tarea
            tarea = crear_tarea(tareas, titulo, descripcion, estado, prioridad)
            print(f"\n✓ Tarea creada exitosamente con ID: {tarea['id']}\n")
            guardar_tareas(tareas, "tareas.txt")

        # OPCIÓN 2: Ver todas las tareas
        elif opcion == "2":
            mostrar_tareas(tareas, "TODAS LAS TAREAS")

        # OPCIÓN 3: Buscar tarea por título
        elif opcion == "3":
            print("\n" + "=" * 70)
            print("BUSCAR TAREA POR TÍTULO")
            print("=" * 70)

            termino = input("\nIngrese el término de búsqueda: ").strip()

            if not termino:
                print("⚠ El término de búsqueda no puede estar vacío.\n")
                continue

            resultados = buscar_por_titulo(tareas, termino)
            mostrar_tareas(resultados, f'RESULTADOS DE BÚSQUEDA: "{termino}"')

        # OPCIÓN 4: Filtrar por estado
        elif opcion == "4":
            print("\n" + "=" * 70)
            print("FILTRAR TAREAS POR ESTADO")
            print("=" * 70)

            while True:
                print("\nEstados disponibles:")
                print("  1. Pendiente")
                print("  2. En progreso")
                print("  3. Completada")
                estado_opcion = input("Seleccione el estado (1-3): ").strip()
                es_valido, estado = validar_estado(estado_opcion)
                if es_valido:
                    break
                print("⚠ Estado inválido. Ingrese un número entre 1 y 3.")

            resultados = filtrar_por_estado(tareas, estado)
            mostrar_tareas(resultados, f"TAREAS CON ESTADO: {estado.upper()}")

        # OPCIÓN 5: Filtrar por prioridad
        elif opcion == "5":
            print("\n" + "=" * 70)
            print("FILTRAR TAREAS POR PRIORIDAD")
            print("=" * 70)

            while True:
                print("\nPrioridades disponibles:")
                print("  1. Baja")
                print("  2. Media")
                print("  3. Alta")
                prioridad_opcion = input("Seleccione la prioridad (1-3): ").strip()
                es_valido, prioridad = validar_prioridad(prioridad_opcion)
                if es_valido:
                    break
                print("⚠ Prioridad inválida. Ingrese un número entre 1 y 3.")

            resultados = filtrar_por_prioridad(tareas, prioridad)
            mostrar_tareas(resultados, f"TAREAS CON PRIORIDAD: {prioridad.upper()}")

        # OPCIÓN 6: Actualizar tarea
        elif opcion == "6":
            print("\n" + "=" * 70)
            print("ACTUALIZAR TAREA")
            print("=" * 70)

            # Obtener ID de la tarea
            while True:
                id_str = input("\nIngrese el ID de la tarea a actualizar: ").strip()
                es_valido, tarea_id = validar_id(id_str)
                if es_valido:
                    break
                print("⚠ ID inválido. Por favor, ingrese un número positivo.")

            tarea = obtener_tarea_por_id(tareas, tarea_id)

            if tarea is None:
                print(f"⚠ No existe tarea con ID {tarea_id}.\n")
                continue

            print("\nTarea actual:")
            mostrar_tarea(tarea)

            # Obtener nuevos datos
            print(
                "Ingrese los nuevos datos (presione Enter para mantener el valor actual):\n"
            )

            nuevo_titulo = input("Nuevo título: ").strip()
            if not nuevo_titulo:
                nuevo_titulo = None

            nueva_descripcion = input("Nueva descripción: ").strip()
            if not nueva_descripcion:
                nueva_descripcion = None

            nuevo_estado = None
            opcion_cambio = input("¿Cambiar estado? (s/n): ").strip().lower()
            if opcion_cambio == "s":
                while True:
                    print("\nEstados disponibles:")
                    print("  1. Pendiente")
                    print("  2. En progreso")
                    print("  3. Completada")
                    estado_opcion = input("Seleccione el nuevo estado (1-3): ").strip()
                    es_valido, nuevo_estado = validar_estado(estado_opcion)
                    if es_valido:
                        break
                    print("⚠ Estado inválido. Ingrese un número entre 1 y 3.")

            nueva_prioridad = None
            opcion_cambio = input("¿Cambiar prioridad? (s/n): ").strip().lower()
            if opcion_cambio == "s":
                while True:
                    print("\nPrioridades disponibles:")
                    print("  1. Baja")
                    print("  2. Media")
                    print("  3. Alta")
                    prioridad_opcion = input(
                        "Seleccione la nueva prioridad (1-3): "
                    ).strip()
                    es_valido, nueva_prioridad = validar_prioridad(prioridad_opcion)
                    if es_valido:
                        break
                    print("⚠ Prioridad inválida. Ingrese un número entre 1 y 3.")

            # Actualizar tarea
            if actualizar_tarea(
                tareas,
                tarea_id,
                nuevo_titulo,
                nueva_descripcion,
                nuevo_estado,
                nueva_prioridad,
            ):
                print("\n✓ Tarea actualizada exitosamente.\n")
                guardar_tareas(tareas, "tareas.txt")
                tarea_actualizada = obtener_tarea_por_id(tareas, tarea_id)
                mostrar_tarea(tarea_actualizada)
            else:
                print("⚠ Error al actualizar la tarea.\n")

        # OPCIÓN 7: Eliminar tarea
        elif opcion == "7":
            print("\n" + "=" * 70)
            print("ELIMINAR TAREA")
            print("=" * 70)

            # Obtener ID de la tarea
            while True:
                id_str = input("\nIngrese el ID de la tarea a eliminar: ").strip()
                es_valido, tarea_id = validar_id(id_str)
                if es_valido:
                    break
                print("⚠ ID inválido. Por favor, ingrese un número positivo.")

            tarea = obtener_tarea_por_id(tareas, tarea_id)

            if tarea is None:
                print(f"⚠ No existe tarea con ID {tarea_id}.\n")
                continue

            print("\nTarea a eliminar:")
            mostrar_tarea(tarea)

            # Confirmación
            confirmacion = (
                input("¿Está seguro de que desea eliminar esta tarea? (s/n): ")
                .strip()
                .lower()
            )

            if confirmacion == "s":
                if eliminar_tarea(tareas, tarea_id):
                    print(f"\n✓ Tarea con ID {tarea_id} eliminada exitosamente.\n")
                    guardar_tareas(tareas, "tareas.txt")
                else:
                    print("⚠ Error al eliminar la tarea.\n")
            else:
                print("\nEliminación cancelada.\n")

        # OPCIÓN 8: Ver estadísticas
        elif opcion == "8":
            print("\n" + "=" * 70)
            print("ESTADÍSTICAS DEL SISTEMA")
            print("=" * 70)

            stats = obtener_estadisticas(tareas)

            print(f"\nTotal de tareas: {stats['total_tareas']}")
            print(f"\nTareas por estado:")
            print(f"  • Pendientes: {stats['pendientes']}")
            print(f"  • En progreso: {stats['en_progreso']}")
            print(f"  • Completadas: {stats['completadas']}")
            print(f"\nTareas por prioridad:")
            print(f"  • Baja: {stats['baja']}")
            print(f"  • Media: {stats['media']}")
            print(f"  • Alta: {stats['alta']}")
            print(f"\nTasa de finalización: {stats['tasa_finalizacion']:.1f}%\n")

        # OPCIÓN 0: Salir
        elif opcion == "0":
            print("\n" + "=" * 70)
            print("¡Gracias por usar el Sistema de Gestión de Tareas!")
            print("¡Adiós! 👋")
            print("=" * 70 + "\n")
            ejecutando = False

        # Opción no válida
        else:
            print(
                "\n⚠ Opción no válida. Por favor, seleccione una opción entre 0 y 8.\n"
            )


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nPrograma interrumpido por el usuario.\n")
    except Exception as e:
        print(f"\nError inesperado: {e}\n")
