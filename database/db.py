import sqlite3 as sql

NOOMBRE_DB = 'registros.db'

def conectar(timeout=5):
    conexion = sql.connect(NOOMBRE_DB, timeout=timeout)
    return conexion