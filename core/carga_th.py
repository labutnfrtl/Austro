from datetime import datetime
from database.temperaturahumedad import insertar_datos_TH   # donde está definida insertar_datos_TH
import hardware.arduino as dato  # tu módulo para leer del Arduino
import serial


def cargar_datos_TH():
    """
    Lee los datos de temperatura y humedad desde el Arduino
    y los almacena en la base de datos con timestamp automático.
    """

array = dato.leer_datos()

    # Convertir los datos a float
sensor1_temp = float(array[0])
sensor1_hum  = float(array[1])
sensor2_temp = float(array[2])
sensor2_hum  = float(array[3])
sensor3_temp = float(array[4])
sensor3_hum  = float(array[5])

    # Insertar datos por sensor (con idSensor 1, 2 y 3)
insertar_datos_TH(1, sensor1_temp, sensor1_hum)
insertar_datos_TH(2, sensor2_temp, sensor2_hum)
insertar_datos_TH(3, sensor3_temp, sensor3_hum)