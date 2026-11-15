# © 2026 asergom. Todos los derechos reservados (ver LICENSE).
"""Ajustes de la ciudad (data/ciudad.json) para los generadores de tools/.

Los algoritmos son generales; lo propio de cada ciudad (festivos, zona del relieve, URL de la API
de tiempos, alias de sitios…) está en data/ciudad.json. Otra ruta: variable CIUDAD_JSON.
"""
import json
import math
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUTA = os.environ.get("CIUDAD_JSON") or os.path.join(RAIZ, "data", "ciudad.json")

with open(RUTA, encoding="utf-8") as _f:
    CIUDAD = json.load(_f)


def get(clave, defecto=None):
    return CIUDAD.get(clave, defecto)


# Metros por grado de longitud a la latitud de la ciudad (los de latitud, ~111.320 en todas partes).
M_LON = 111320 * math.cos(math.radians(CIUDAD.get("latitud", 0)))
