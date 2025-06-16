from .db import conectar

def crear_tabla_sensor():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Sensor (
            idSensor INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            descripcion TEXT
        )
    ''')
    conexion.commit()
    conexion.close()

def inicializar_sensores():
    sensores = [
        (1, 'Sensor 1', 'Sensor en parte inferior'),
        (2, 'Sensor 2', 'Sensor en parte superior'),
        (3, 'Sensor 3', 'Sensor en parte medio'),
    ]

    conexion = conectar()
    cursor = conexion.cursor()
    for idSensor, nombre, descripcion in sensores:
        cursor.execute('''
            INSERT OR IGNORE INTO Sensor (idSensor, nombre, descripcion)
            VALUES (?, ?, ?)
        ''', (idSensor, nombre, descripcion))
    conexion.commit()
    conexion.close()
