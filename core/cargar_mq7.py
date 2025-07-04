from database.mq7 import insertar_datos_MQ7
import hardware.arduino as dato
import time

def cargar_datos_MQ7(max_reintentos=3, espera=2):
    """
    Lee los datos de CO desde el Arduino
    y los almacena en la base de datos con timestamp automático.
    Reintenta si no recibe datos válidos.
    """
    intentos = 0
    while intentos < max_reintentos:
        array = dato.leer_datos()
        if array and len(array) >= 1:
            try:
                # Convertir el dato a float
                co_value = float(array[6])
                
                # Insertar datos en la tabla MQ7 (con idSensor 1)
                insertar_datos_MQ7(4, co_value)
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