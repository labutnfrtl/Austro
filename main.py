import logging
from database.constructor_db import inicializar
from core.mainLoop import mainLoop
import core.carga_th as ds

logging.basicConfig(filename='app.log', level=logging.ERROR)

if __name__ == '__main__':
    try:
        inicializar()

    except Exception as e:
        logging.error(f"Error al inicializar: {e}")

    try:
        mainLoop()
    except Exception as e:
        logging.error(f"Error en mainLoop: {e}")
