import csv
import datetime

def initialize_csv(csv_file):
    """
    Inicializa el archivo CSV con el encabezado si está vacío.

    Args:
        csv_file (str): Nombre del archivo CSV.
    """
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        if file.tell() == 0:
            writer.writerow(['Timestamp', 'Sensor1_Temperatura (°C)', 'Sensor1_Humedad (%)',
                             'Sensor2_Temperatura (°C)', 'Sensor2_Humedad (%)',
                             'Sensor3_Temperatura (°C)', 'Sensor3_Humedad (%)'])

def parse_sensor_data(line, sensor_data):
    """
    Analiza una línea de datos del sensor y actualiza los datos en el diccionario proporcionado.

    Args:
        line (str): Línea de datos del sensor recibida del puerto serial.
        sensor_data (dict): Diccionario para almacenar los datos de los sensores.

    Returns:
        bool: True si los datos de todos los sensores están completos, False de lo contrario.
    """
    if 'Sensor' in line:
        parts = line.split(':')
        if len(parts) == 2:
            sensor_info = parts[0].strip()
            sensor_data_str = parts[1].strip()
            
            if 'Sensor 1' in sensor_info:
                sensor_key = 'Sensor1'
            elif 'Sensor 2' in sensor_info:
                sensor_key = 'Sensor2'
            elif 'Sensor 3' in sensor_info:
                sensor_key = 'Sensor3'
            else:
                return False
            
            try:
                temperatura = sensor_data_str.split(',')[1].split('=')[1].strip().replace('°C', '')
                humedad = sensor_data_str.split(',')[0].split('=')[1].strip().replace('%', '')
                
                sensor_data[sensor_key]['temperatura'] = temperatura
                sensor_data[sensor_key]['humedad'] = humedad
                
                if all(sensor_data[sensor_key]['temperatura'] != '' and sensor_data[sensor_key]['humedad'] != '' for sensor_key in sensor_data):
                    return True
            except IndexError:
                pass
    return False

def write_to_csv(csv_file, sensor_data):
    """
    Escribe los datos de los sensores en el archivo CSV.

    Args:
        csv_file (str): Nombre del archivo CSV.
        sensor_data (dict): Diccionario que contiene los datos de los sensores.
    """
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp,
                         sensor_data['Sensor1']['temperatura'], sensor_data['Sensor1']['humedad'],
                         sensor_data['Sensor2']['temperatura'], sensor_data['Sensor2']['humedad'],
                         sensor_data['Sensor3']['temperatura'], sensor_data['Sensor3']['humedad']])
