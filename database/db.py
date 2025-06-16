import sqlite3 as sql

NOOMBRE_DB = 'registros.db'

def conectar():
    conexion = sql.connect(NOOMBRE_DB)
    return conexion


