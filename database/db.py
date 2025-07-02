import sqlite3 as sql
from config.config import config

if config["entorno"]["sin_conexion"]:
    NOOMBRE_DB = 'registros_ejemplo.db'
else:
    NOOMBRE_DB = 'registros.db'

def conectar(timeout=5):
    conexion = sql.connect(NOOMBRE_DB, timeout=timeout)
    return conexion