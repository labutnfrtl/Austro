from database.constructor_db import inicializar
from core.mainLoop import mainLoop
import core.carga_th    as ds

if __name__ == '__main__':    
    inicializar()
    mainLoop()  # Inicia el bucle principal del programa  
    
