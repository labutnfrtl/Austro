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
    """
    esta función lee los datos del Arduino a través del puerto serie.
    Se espera que el Arduino envíe una línea de datos en formato
    "valor1;valor2;valor3;valor4;valor5;valor6".
    """
    arduino = serial.Serial(PUERTO, VELOCIDAD, timeout=2)
    time.sleep(2)
    linea = arduino.readline()
    arduino.close()
    return linea

def leer_arduino_mook(n=6, minimo=-56, maximo=70):
    """
    esta función simula la lectura de datos del Arduino
    generando valores aleatorios entre `minimo` y `maximo`.
    """
    valores = [f"{random.uniform(minimo, maximo):.1f}" for _ in range(n)]
    linea = ";".join(valores)
    return linea.encode('ascii')