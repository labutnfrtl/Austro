import time
import serial
import random
from config.config import config

print(config)

PUERTO = config["arduino"]["puerto"]    
VELOCIDAD = config["arduino"]["baudrate"]     
ENTORNO = config["entorno"]["sin_conexion"]




def leer_datos():
    linea = leer_arduino()
    array = linea.decode('utf-8').strip().split(';')
    return array

def leer_arduino():
    if ENTORNO:
        return leer_arduino_mook()
    else:
        return leer_arduino_real()

def leer_arduino_real():
    try:
        arduino = serial.Serial(PUERTO, VELOCIDAD, timeout=2)
        time.sleep(2)
        linea = arduino.readline()
    except Exception as e:
        print(f"Error al leer del Arduino: {e}")
        return b""
    finally:
        try:
            arduino.close()
        except:
            pass
    return linea

def leer_arduino_mook(n=10):
    """
    Esta función simula la lectura de datos del Arduino
    generando los valores del 0 al 9 como strings separados por ';'.
    """
    valores = [str(i) for i in range(n)]
    linea = ";".join(valores)
    return linea.encode('ascii')
