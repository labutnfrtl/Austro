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
        (1, 'DTH11-1', 'Sensor en parte inferior'),
        (2, 'DTH11-2', 'Sensor en parte superior'),
        (3, 'DTH11-3', 'Sensor en parte medio'),
        (4, 'mq-7', 'Sensor de gas MQ-7')
    ]

    conexion = conectar()
    cursor = conexion.cursor()

    for idSensor, nombre, descripcion in sensores:
        cursor.execute('''
            INSERT OR REPLACE INTO Sensor (idSensor, nombre, descripcion)
            VALUES (?, ?, ?)
        ''', (idSensor, nombre, descripcion))
        
    conexion.commit()
    conexion.close()
