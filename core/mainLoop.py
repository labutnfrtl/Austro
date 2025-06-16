
import time
import core.carga_th as th
import time
from datetime import datetime
import core.carga_th as th

def mainLoop():
    count = 0
    minutos_validos = [0, 15, 30, 45]  # Cambialos si querés otros minutos

    print("Iniciando toma de datos cada 15 minutos...")

    while True:
        ahora = datetime.now()
        minuto_actual = ahora.minute

        if minuto_actual in minutos_validos:
            th.cargar_datos_TH()
            print("Datos de temperatura y humedad almacenados correctamente.")
            print(f"Lectura número: {count + 1}")
            count += 1
            time.sleep(60)  # Espera un minuto completo para evitar repetir
        else:
            time.sleep(1)  # Revisa cada segundo hasta que llegue el momento correcto


