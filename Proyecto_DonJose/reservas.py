"""
reservas.py
Contiene toda la lógica de negocio: CRUD de reservas y validación de aforo.
"""

from almacenamiento import guardar_datos
from modelo import crear_reserva

CAPACIDAD_MAXIMA = 50  # Capacidad total del restaurante de Don José


def mostrar_reservas(reservas: list) -> None:
    """Muestra todas las reservas actuales en el 'cuaderno digital'."""
    print("\n--- LISTA ACTUAL DE RESERVAS ---")
    if not reservas:
        print("No hay reservas anotadas.")
    else:
        for i, r in enumerate(reservas, 1):
            print(f"{i}. Cliente: {r['nombre']} | Personas: {r['personas']} | Hora: {r['hora']}")

    total_ocupado = sum(r['personas'] for r in reservas)
    print(f"Ocupación total: {total_ocupado}/{CAPACIDAD_MAXIMA}")


def registrar_reserva(reservas: list) -> None:
    """Captura nombre, personas y hora; verifica aforo antes de confirmar la reserva."""
    print("\n--- NUEVA RESERVA ---")

    nombre = input("Nombre del cliente: ").strip()
    if not nombre:
        print("El nombre no puede estar vacío.")
        return

    try:
        personas = int(input("¿Cuántas personas vienen?: "))
        if personas <= 0:
            print("Número de personas no válido.")
            return
    except ValueError:
        print("Por favor, ingrese un número entero para las personas.")
        return

    hora = input("Hora de la reserva (ej. 20:00): ").strip()
    if not hora:
        print("La hora no puede estar vacía.")
        return

    total_actual = sum(r['personas'] for r in reservas)

    if total_actual + personas <= CAPACIDAD_MAXIMA:
        reserva = crear_reserva(nombre, personas, hora)
        reservas.append(reserva)
        print(f"¡Reserva confirmada para {nombre} a las {hora}!")
        guardar_datos(reservas)
    else:
        disponible = CAPACIDAD_MAXIMA - total_actual
        print(f"No hay mesas libres para {personas} personas.")
        print(f"Espacio disponible actual: {disponible}")


def modificar_reserva(reservas: list) -> None:
    """Busca y modifica una reserva existente validando aforo y datos."""
    nombre_buscar = input("\nNombre del cliente a modificar: ").strip().lower()

    for r in reservas:
        if r['nombre'].lower() == nombre_buscar:
            print(f"Reserva encontrada: {r['nombre']} | {r['personas']} personas | Hora: {r['hora']}")
            try:
                nuevo_num = int(input("Nuevo número de personas: "))
                if nuevo_num <= 0:
                    print("El número de personas debe ser mayor a cero.")
                    return
            except ValueError:
                print("Dato inválido. Ingrese un número entero.")
                return

            nueva_hora = input(f"Nueva hora (Enter para mantener '{r['hora']}'): ").strip()
            if not nueva_hora:
                nueva_hora = r['hora']

            # Validar capacidad considerando la diferencia del cambio
            diferencia = nuevo_num - r['personas']
            total_actual = sum(res['personas'] for res in reservas)

            if total_actual + diferencia <= CAPACIDAD_MAXIMA:
                r['personas'] = nuevo_num
                r['hora'] = nueva_hora
                print("Reserva modificada con éxito.")
                guardar_datos(reservas)
            else:
                print("Error: El cambio supera la capacidad del restaurante.")
            return

    print("No se encontró ninguna reserva a ese nombre.")


def eliminar_reserva(reservas: list) -> None:
    """Borra una reserva si el cliente cancela, previa confirmación."""
    nombre_buscar = input("\nNombre del cliente que desea cancelar: ").strip().lower()

    for i, r in enumerate(reservas):
        if r['nombre'].lower() == nombre_buscar:
            confirmar = input(f"¿Seguro que desea eliminar la reserva de {r['nombre']}? (s/n): ")
            if confirmar.lower() == 's':
                reservas.pop(i)
                print("Reserva eliminada.")
                guardar_datos(reservas)
            else:
                print("Operación cancelada.")
            return

    print("No se encontró la reserva.")
