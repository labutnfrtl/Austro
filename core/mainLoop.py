from datetime import datetime
import time
import core.carga_th as th


def mainLoop():
    count = 0
    minutos_validos = [0, 15, 30, 45]
    print("Iniciando toma de datos cada 15 minutos... ⏰")
    while True:
        try:
            ahora = datetime.now()
            minuto_actual = ahora.minute
            if minuto_actual in minutos_validos:
                exito = th.cargar_datos_TH()
                if exito:
                    print(f"Lectura número: {count + 1}", flush=True)
                    count += 1
                time.sleep(60)
            else:
                time.sleep(1)
        except Exception as e:
            print(f"Error en el bucle principal: {e}")
            time.sleep(5)