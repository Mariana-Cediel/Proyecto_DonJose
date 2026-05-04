"""
modelo.py
Define la estructura de datos de una Reserva.
"""

def crear_reserva(nombre: str, personas: int, hora: str) -> dict:
    """Retorna un diccionario que representa una reserva."""
    return {
        "nombre": nombre,
        "personas": personas,
        "hora": hora
    }
