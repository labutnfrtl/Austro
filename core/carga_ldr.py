from database.ldr import insertar_datos_LDR
import hardware.arduino as dato
import time

def cargar_datos_LDR(max_reintentos=3, espera=2):
    """
    Lee los datos de luz desde el Arduino
    y los almacena en la base de datos con timestamp automático.
    Reintenta si no recibe datos válidos.
    """
    intentos = 0
    while intentos < max_reintentos:
        array = dato.leer_datos()
        if array and len(array) >= 1:
            try:
                # Convertir el dato a float
                ldr_value = float(array[8])
                
                # Insertar datos en la tabla LDR (con idSensor 2)
                insertar_datos_LDR(6, ldr_value)
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