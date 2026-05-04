"""
almacenamiento.py
Maneja la carga y guardado de datos en el archivo JSON (persistencia).
"""

import json
import os

NOMBRE_ARCHIVO = "reservas.json"


def cargar_datos() -> list:
    """Carga las reservas desde el archivo JSON. Si no existe, retorna una lista vacía."""
    if not os.path.exists(NOMBRE_ARCHIVO):
        return []
    try:
        with open(NOMBRE_ARCHIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def guardar_datos(reservas: list) -> None:
    """Guarda la lista de reservas en el archivo JSON para persistencia."""
    try:
        with open(NOMBRE_ARCHIVO, "w", encoding="utf-8") as f:
            json.dump(reservas, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Error al guardar los datos: {e}")
