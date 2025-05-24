import time
import msvcrt
import serial
from serial_utils import find_serial_port
from sensor_utils import initialize_csv, parse_sensor_data, write_to_csv
import datetime
import shutil
import subprocess
import psutil

def save_info_to_file(info, file_name):
    attempt = 0
    while True:
        try:
            with open(file_name, 'w') as file:
                file.write(info)
            print(f"Información guardada en {file_name}.")
            break
        except IOError:
            attempt += 1
            print(f"Intento {attempt}: El archivo {file_name} está en uso. Intentando de nuevo...")
            time.sleep(1)
        except Exception as e:
            print(f"Error al guardar la información en {file_name}: {e}")
            break

def log_error(error_message, error_file='error.txt'):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    full_message = f"[{timestamp}] {error_message}\n"
    try:
        with open(error_file, 'a') as file:
            file.write(full_message)
        print(f"Error guardado en {error_file}.")
    except Exception as e:
        print(f"Error al guardar el mensaje de error en {error_file}: {e}")

def create_csv_backup(csv_file, backup_file):
    try:
        shutil.copyfile(csv_file, backup_file)
        print(f"Copia de seguridad creada: {backup_file}")
    except Exception as e:
        print(f"Error al crear la copia de seguridad: {e}")
        log_error(f"Error al crear la copia de seguridad: {e}")

def handle_sensor_data(ser, csv_file):
    initialize_csv(csv_file)

    sensor_data = {
        'Sensor1': {'temperatura': '', 'humedad': ''},
        'Sensor2': {'temperatura': '', 'humedad': ''},
        'Sensor3': {'temperatura': '', 'humedad': ''}
    }

    paused = False
    read_count = 0
    collected_data = ""
    while True:
        try:
            if not paused:
                line = ser.readline().decode('utf-8').strip()
                if line:
                    print(line)
                    collected_data += line + "\n"
                    
                    if parse_sensor_data(line, sensor_data):
                        write_to_csv(csv_file, sensor_data)
                        for sensor_key in sensor_data:
                            sensor_data[sensor_key]['temperatura'] = ''
                            sensor_data[sensor_key]['humedad'] = ''
                        read_count += 1
                        if read_count % 3 == 0:
                            info = f"Toma de datos número {read_count}:\n{collected_data}"
                            save_info_to_file(info, 'infos.txt')
                            collected_data = ""
                        if read_count % 20 == 0:
                            create_csv_backup(csv_file, 'backup.csv')

            if msvcrt.kbhit():
                key = msvcrt.getch().decode().lower()
                if key == 'p':
                    paused = not paused
                    status = "en pausa" if paused else "reanudado"
                    print(f"Programa {status}.")
                    info = f"El sistema se encuentra {status}.\n"
                    save_info_to_file(info, 'infos.txt')
                elif key == 'c':
                    print("Programa terminado por el usuario.")
                    info = "El sistema se encuentra apagado.\n"
                    save_info_to_file(info, 'infos.txt')
                    break
            
        except serial.SerialException as e:
            print(f'Error de comunicación serial: {e}')
            print("Reintentando la conexión en 30 segundos...")
            log_error(f'Error de comunicación serial: {e}')
            time.sleep(30)
            ser.close()
            ser = find_serial_port()
        except Exception as e:
            print(f'Ocurrió un error: {e}')
            log_error(f'Ocurrió un error: {e}')
            break

    ser.close()

def terminate_existing_bot_process():
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            if 'python' in proc.info['name'] and 'telegram_bot.py' in proc.info['cmdline']:
                print(f"Terminando proceso existente del bot de Telegram con PID: {proc.info['pid']}")
                proc.terminate()
                proc.wait()
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

if __name__ == '__main__':
    try:
        terminate_existing_bot_process()
        
        # Ejecutar el bot de Telegram en segundo plano sin mostrar una ventana
        si = subprocess.STARTUPINFO()
        si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        si.wShowWindow = subprocess.SW_HIDE
        subprocess.Popen(['python', 'telegram_bot.py'], startupinfo=si)

        # Ejecutar la interfaz gráfica en segundo plano sin mostrar una ventana
        subprocess.Popen(['python', 'gui.py'], startupinfo=si)

        ser = find_serial_port()
        handle_sensor_data(ser, 'sensor_data.csv')
    except serial.SerialException as e:
        print(f'Error al buscar puertos seriales: {e}')
        log_error(f'Error al buscar puertos seriales: {e}')
        exit()
    except Exception as e:
        print(f'Ocurrió un error en el programa principal: {e}')
        log_error(f'Ocurrió un error en el programa principal: {e}')
