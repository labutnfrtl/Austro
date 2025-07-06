from database.pir import insertar_datos_PIR
import hardware.arduino as dato
import time

# Variables globales para acumular
acumulador_valores = []
acumulador_cantidad = 0

def promedio_pir(max_reintentos=3, espera=2):
    """
    Lee datos del Arduino y los acumula sin insertar nada.
    """
    global acumulador_valores, acumulador_cantidad

    intentos = 0
    while intentos < max_reintentos:
        array = dato.leer_datos()
        if array and len(array) >= 8:
            try:
                movimiento_value = float(array[7])
                acumulador_valores.append(movimiento_value)
                acumulador_cantidad += 1
                return True  # acumulación exitosa
            except Exception as e:
                print(f"Error al convertir el dato: {e}")
                return False
        else:
            print(f"Intento {intentos+1}: Sin datos válidos. Reintento en {espera} s...")
            time.sleep(espera)
            intentos += 1

    print("No se obtuvieron datos válidos del Arduino.")
    return False

def insertar_promedio():
    """
    Calcula el promedio de los datos acumulados y lo inserta en la base de datos.
    Luego reinicia el acumulador.
    """
    global acumulador_valores, acumulador_cantidad

    if acumulador_cantidad == 0:
        print("No hay datos acumulados para insertar.")
        return None, 0

    promedio_valor = sum(acumulador_valores) / acumulador_cantidad
    insertar_datos_PIR(5, promedio_valor)

    # Reiniciar acumulador
    cantidad = acumulador_cantidad
    acumulador_valores = []
    acumulador_cantidad = 0

    return promedio_valor, cantidad
