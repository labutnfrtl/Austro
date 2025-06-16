# 🌞 Austro – Monitoreo de Muro Trombe

**Austro** es un proyecto de monitoreo ambiental diseñado para estudiar el comportamiento térmico y de humedad de un **muro Trombe**, utilizando sensores **DHT22**. El sistema está pensado para ser sencillo, funcional y extensible a futuro.

---

## 📌 Objetivo

El propósito del proyecto es **medir, registrar y analizar** datos de temperatura y humedad en distintos puntos de un muro Trombe para evaluar su eficiencia como sistema pasivo de calefacción solar.

---

## 🔧 Estado actual

- Sensores utilizados: **DHT22** (hasta 3 simultáneamente).
- Lectura mediante Arduino.
- Recepción de datos por puerto serie en Python.
- Almacenamiento en base de datos **SQLite**.
- Análisis estadístico básico desde consola o código Python.

---

## ⚙️ Requisitos

- Python 3.10 o superior
- Arduino IDE (para cargar el código al microcontrolador)
- Librerías de Python:
  - `pyserial`
  - `sqlite3` (incluida en Python)

Instalación de dependencias:

```bash
pip install pyserial
```

## 🚀 Uso básico
Conectá los sensores DHT22 al Arduino.

Cargá el código desde SensoresLectura.ino.

Ejecutá el script de Python:

```bash
python main.py
```
Los datos se guardarán automáticamente con fecha y hora en una base de datos SQLite.


## 🔄 Pensado para expandirse
Aunque actualmente solo se usan sensores DHT22, Austro está diseñado para facilitar la integración futura de sensores adicionales como:

MQ7 (Monóxido de carbono)

LDR (fotocélula)

PIR (movimiento)





