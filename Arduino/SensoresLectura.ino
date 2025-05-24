#include <DHT.h>
#include <DHT_U.h>

#define DHTPIN1 7     // Pin para el primer sensor
#define DHTPIN2 8     // Pin para el segundo sensor
#define DHTPIN3 9     // Pin para el tercer sensor
#define DHTTYPE DHT22 // Tipo de sensor DHT

DHT dht1(DHTPIN1, DHTTYPE);
DHT dht2(DHTPIN2, DHTTYPE);
DHT dht3(DHTPIN3, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht1.begin();
  dht2.begin();
  dht3.begin();
}

void loop() {
  // Esperamos unos segundos entre las mediciones
  delay(2000);

  String salida = leerSensor(dht1, "1") + leerSensor(dht2, "2") + leerSensor(dht3, "3");
  imprimirDatos(salida);
}

String leerSensor(DHT &dht, String nombreSensor) {
  float h = dht.readHumidity();
  float t = dht.readTemperature();
  String valor;

  if (isnan(h) || isnan(t)) {
    valor = nombreSensor + "00000000";
  } else {
    // Formatear la humedad y temperatura con dos decimales
    String humedad = String(h, 2); // Formatear humedad con 2 decimales
    String temperatura = String(t, 2); // Formatear temperatura con 2 decimales

    // Asegurarse de que la longitud de las cadenas sea siempre 4 caracteres para humedad y 4 para temperatura
    humedad = String(h, 2);
    temperatura = String(t, 2);
    
    // Si la longitud es menor a 4, añadir ceros a la izquierda
    while (humedad.length() < 5) {
      humedad = "0" + humedad;
    }
    while (temperatura.length() < 5) {
      temperatura = "0" + temperatura;
    }

    // Eliminar el punto decimal y asegurar que longitud de la cadena sea 4 para humedad y 4 para temperatura
    humedad.replace(".", "");
    temperatura.replace(".", "");

    // Ajustar longitud de las cadenas para humedad y temperatura
    if (humedad.length() > 4) {
      humedad = humedad.substring(0, 4);
    }
    if (temperatura.length() > 4) {
      temperatura = temperatura.substring(0, 4);
    }

    valor = nombreSensor + humedad + temperatura;
  }

  return valor;
}

void imprimirDatos(String salida) {
  for (int i = 0; i < salida.length(); i += 9) {
    String sensor = salida.substring(i, i + 1);
    String humedad = salida.substring(i + 1, i + 5);
    String temperatura = salida.substring(i + 5, i + 9);

    // Asegurarse de que humedad y temperatura tengan un punto decimal
    humedad = humedad.substring(0, 2) + "." + humedad.substring(2);
    temperatura = temperatura.substring(0, 2) + "." + temperatura.substring(2);

    Serial.print("Sensor ");
    Serial.print(sensor);
    Serial.print(": Humedad = ");
    Serial.print(humedad);
    Serial.print("%, Temperatura = ");
    Serial.print(temperatura);
    Serial.println("°C");
    Serial.println("");
  }
}
