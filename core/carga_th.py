from database.temperaturahumedad import insertar_datos_TH
import hardware.arduino as dato
import time

def cargar_datos_TH(max_reintentos=3, espera=2):
    """
    Lee los datos de temperatura y humedad desde el Arduino
    y los almacena en la base de datos con timestamp automático.
    Reintenta si no recibe datos válidos.
    """
    intentos = 0
    while intentos < max_reintentos:
        array = dato.leer_datos()
        if True:
            try:
                # Convertir los datos a float
                sensor1_temp = float(array[1])
                sensor1_hum  = float(array[0])
                sensor2_temp = float(array[3])
                sensor2_hum  = float(array[2])
                sensor3_temp = float(array[5])
                sensor3_hum  = float(array[4])

                # Insertar datos por sensor (con idSensor 1, 2 y 3)
                insertar_datos_TH(1, sensor1_temp, sensor1_hum)
                insertar_datos_TH(2, sensor2_temp, sensor2_hum)
                insertar_datos_TH(3, sensor3_temp, sensor3_hum)
                return True  # Éxito
            except Exception as e:
                print(f"Error al convertir o insertar datos: {e}")
                return False
        else:
            print(f"Intento {intentos+1}: No se recibieron datos válidos del Arduino. Reintentando en {espera} segundos...")
            time.sleep(espera)
            intentos += 1
    print("No se pudieron obtener datos válidos del Arduino después de varios intentos.")
    return False
