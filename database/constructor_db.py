import database.sensores as s
import database.temperaturahumedad as th
import database.mq7 as mq7

def inicializar_db():
    print("Inicializando la base de datos...")
    s.crear_tabla_sensor()

    s.inicializar_sensores()
    
    th.crear_tabla_TH()

    mq7.crear_tabla_MQ7()

inicializar_db() #solucion temporal para evitar el error de importación circular

