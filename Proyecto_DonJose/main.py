"""
main.py
Punto de entrada del Sistema de Gestión de Reservas "El Sazón de Don José".
"""

from almacenamiento import cargar_datos, guardar_datos
from reservas import (
    mostrar_reservas,
    registrar_reserva,
    modificar_reserva,
    eliminar_reserva,
)


def menu_principal() -> None:
    """Punto de entrada principal para Don José."""
    reservas = cargar_datos()

    while True:
        print("\n==============================")
        print("  SISTEMA DE RESERVAS DON JOSÉ")
        print("==============================")
        print("1. Ver reservas")
        print("2. Nueva reserva")
        print("3. Modificar reserva")
        print("4. Cancelar reserva")
        print("5. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            mostrar_reservas(reservas)
        elif opcion == "2":
            registrar_reserva(reservas)
        elif opcion == "3":
            modificar_reserva(reservas)
        elif opcion == "4":
            eliminar_reserva(reservas)
        elif opcion == "5":
            print("Guardando datos y cerrando sistema. ¡Hasta mañana, Don José!")
            guardar_datos(reservas)
            break
        else:
            print("Opción no válida, intente de nuevo.")


if __name__ == "__main__":
    menu_principal()
