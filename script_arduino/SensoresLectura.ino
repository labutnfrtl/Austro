#include <DHT.h>
#include <DHT_U.h>

#define DHTPIN1 7        // Pin para el primer sensor DHT
#define DHTPIN2 8        // Pin para el segundo sensor DHT
#define DHTPIN3 9        // Pin para el tercer sensor DHT
#define DHTTYPE DHT22    // Tipo de sensor DHT22
#define MQ7PIN A0        // Pin analógico para MQ-7
#define PIRPIN 2         // Pin digital para sensor PIR

DHT dht1(DHTPIN1, DHTTYPE);
DHT dht2(DHTPIN2, DHTTYPE);
DHT dht3(DHTPIN3, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht1.begin();
  dht2.begin();
  dht3.begin();
  pinMode(PIRPIN, INPUT); // Configurar pin del PIR como entrada
}

void loop() {
  delay(2000);

  String salida = "";

  // Sensor 1
  float h1 = dht1.readHumidity();
  float t1 = dht1.readTemperature();
  if (isnan(h1) || isnan(t1)) {
    salida += "100000000";
  } else {
    String h = String(h1, 2);
    String t = String(t1, 2);
    while (h.length() < 5) h = "0" + h;
    while (t.length() < 5) t = "0" + t;
    h.replace(".", "");
    t.replace(".", "");
    if (h.length() > 4) h = h.substring(0, 4);
    if (t.length() > 4) t = t.substring(0, 4);
    salida += "1" + h + t;
  }

  // Sensor 2
  float h2 = dht2.readHumidity();
  float t2 = dht2.readTemperature();
  if (isnan(h2) || isnan(t2)) {
    salida += "200000000";
  } else {
    String h = String(h2, 2);
    String t = String(t2, 2);
    while (h.length() < 5) h = "0" + h;
    while (t.length() < 5) t = "0" + t;
    h.replace(".", "");
    t.replace(".", "");
    if (h.length() > 4) h = h.substring(0, 4);
    if (t.length() > 4) t = t.substring(0, 4);
    salida += "2" + h + t;
  }

  // Sensor 3
  float h3 = dht3.readHumidity();
  float t3 = dht3.readTemperature();
  if (isnan(h3) || isnan(t3)) {
    salida += "300000000";
  } else {
    String h = String(h3, 2);
    String t = String(t3, 2);
    while (h.length() < 5) h = "0" + h;
    while (t.length() < 5) t = "0" + t;
    h.replace(".", "");
    t.replace(".", "");
    if (h.length() > 4) h = h.substring(0, 4);
    if (t.length() > 4) t = t.substring(0, 4);
    salida += "3" + h + t;
  }

  // Mostrar datos de sensores DHT
  for (int i = 0; i < salida.length(); i += 9) {
    String sensor = salida.substring(i, i + 1);
    String humedad = salida.substring(i + 1, i + 5);
    String temperatura = salida.substring(i + 5, i + 9);

    humedad = humedad.substring(0, 2) + "." + humedad.substring(2);
    temperatura = temperatura.substring(0, 2) + "." + temperatura.substring(2);

    //Serial.print(sensor);
    //Serial.print(";"); 
    Serial.print(humedad);
    Serial.print(";");
    Serial.print(temperatura);
    Serial.print(";");
  }

  // Lectura del sensor MQ-7
  int mq7Value = analogRead(MQ7PIN);
  Serial.print(mq7Value);
  Serial.print(";");

  // Lectura del sensor PIR
  int pirValue = digitalRead(PIRPIN); // 1 = movimiento, 0 = sin movimiento
  Serial.println(pirValue);
}
