import time
import sqlite3
from .db import conectar

def crear_tabla_MQ7():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS MQ7 (
            idSensor INTEGER,
            CO REAL,
            fecha_hora TEXT DEFAULT (datetime('now', 'localtime')),
            FOREIGN KEY (idSensor) REFERENCES Sensor(idSensor)
        )
    ''')
    conexion.commit()
    conexion.close()

def insertar_datos_MQ7(idSensor, CO, reintentos=5, espera=1):
    """
    Inserta datos en la tabla MQ7.
    Reintenta si la base de datos está bloqueada.
    """
    intento = 0
    while intento < reintentos:
        try:
            with conectar(timeout=10) as conexion:
                cursor = conexion.cursor()
                cursor.execute('''
                    INSERT INTO MQ7 (idSensor, CO)
                    VALUES (?, ?)
                ''', (idSensor, CO))
                conexion.commit()
            return  # Éxito
        except sqlite3.OperationalError as e:
            if "database is locked" in str(e):
                print(f"[DB] Base de datos bloqueada, reintentando ({intento+1}/{reintentos})...")
                time.sleep(espera)
                intento += 1
            else:
                print(f"[DB] Error inesperado: {e}")
                raise
        except Exception as e:
            print(f"[DB] Error al insertar datos: {e}")
            raise
    print("[DB] No se pudo insertar datos después de varios intentos por base de datos bloqueada.")


