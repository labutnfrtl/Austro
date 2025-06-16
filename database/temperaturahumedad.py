from .db import conectar

def crear_tabla_TH():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS TemperaturaHumedad (
            idSensor INTEGER,
            temperatura REAL,
            humedad REAL,
            fecha_hora TEXT DEFAULT (datetime('now', 'localtime')),
            FOREIGN KEY (idSensor) REFERENCES Sensor(idSensor)
        )
    ''')
    conexion.commit()
    conexion.close()

def insertar_datos_TH(idSensor, temperatura, humedad):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('''
        INSERT INTO TemperaturaHumedad (idSensor, temperatura, humedad)
        VALUES (?, ?, ?)
    ''', (idSensor, temperatura, humedad))
    conexion.commit()
    conexion.close()


def obtener_datos_TH():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM TemperaturaHumedad')
    datos = cursor.fetchall()
    conexion.close()
    return datos

def limpiar_tabla_TH():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('DELETE FROM TemperaturaHumedad')
    conexion.commit()
    conexion.close()
