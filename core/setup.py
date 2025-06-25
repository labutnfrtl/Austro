from database.constructor_db import inicializar_db
import time

def setup():
    
    inicializar_db()
    time.sleep(5)  # Espera para asegurar que la base de datos esté lista
    