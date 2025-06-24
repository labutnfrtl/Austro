import database.sensores as s
import database.temperaturahumedad as th

def inicializar():

    s.crear_tabla_sensor()

    s.inicializar_sensores()
    
    th.crear_tabla_TH()