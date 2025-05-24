import serial

def find_serial_port():
    """
    Encuentra un puerto COM disponible para la comunicación serial.

    Returns:
        serial.Serial: Objeto de conexión serial si se encuentra un puerto disponible.

    Raises:
        serial.SerialException: Si no se encuentra ningún puerto COM disponible.
    """

     
    for i in range(1, 11):
        try:
            ser = serial.Serial(f'COM3', 9600, timeout=1)
            print(f'Conectado al puerto COM{i}')
            return ser
        except serial.SerialException:
            print(f'Puerto COM{i} no disponible')
    raise serial.SerialException('No se encontró ningún puerto COM disponible')
     
