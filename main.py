from core.mainLoop import mainLoop
from core.setup import setup


if __name__ == '__main__':
        print("Iniciando el programa...")
        setup()
        print("Base de datos inicializada.")
        print("Iniciando el bucle principal...")    
        mainLoop()
        print("Bucle principal iniciado.")