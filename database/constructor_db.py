import database.sensores as s
import database.temperaturahumedad as th

def inicializar_db():
    print("Inicializando la base de datos...")
    s.crear_tabla_sensor()

    s.inicializar_sensores()
    
    th.crear_tabla_TH()

inicializar_db() #solucion temporal para evitar el error de importación circular

