from datetime import datetime
import time
import core.carga_th as th
import core.cargar_mq7 as mq7
import core.carga_pir as pir
import core.carga_ldr as ldr

def mainLoop():
    count = 0
    minutos_validos = [0, 15, 30, 45]
    print("Iniciando toma de datos cada 15 minutos... ⏰")
    while True:
        try:
            ahora = datetime.now()
            minuto_actual = ahora.minute
            if minuto_actual in minutos_validos:
                exito = th.cargar_datos_TH() and mq7.cargar_datos_MQ7() and pir.insertar_promedio() and ldr.cargar_datos_LDR()
                if exito:
                    print(f"Lectura número: {count + 1}", flush=True)
                    count += 1
                time.sleep(60)
            else:
                pir.promedio_pir()
                time.sleep(1)
        except Exception as e:
            print(f"Error en el bucle principal: {e}")
            time.sleep(5)