import network
import time
from machine import Pin
import ujson
from umqtt.simple import MQTTClient
from hcsr04 import HCSR04
from time import sleep

# ===== CONFIGURAÇÕES MQTT =====
MQTT_CLIENT_ID = "esp32_alerta_cidadao"
MQTT_BROKER = "test.mosquitto.org"
MQTT_USER = ""
MQTT_PASSWORD = ""
MQTT_TOPIC = "alerta_cidadao/sensor"

# ===== CONFIGURAÇÃO DOS SENSORES =====
sensor1 = HCSR04(trigger_pin=5, echo_pin=18, echo_timeout_us=100000)
sensor_chuva = Pin(15, Pin.IN)

# ===== CONECTANDO AO WIFI =====
print("Conectando no WiFi...", end="")
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('Wokwi-GUEST', '')  # rede Wokwi Guest (sem senha)

while not sta_if.isconnected():
    print(".", end="")
    time.sleep(0.1)
print(" Conectado!")

# ===== CONECTANDO AO BROKER MQTT =====
print("Conectando MQTT...", end="")
client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, user=MQTT_USER, password=MQTT_PASSWORD)
client.connect()
print(" Conectado!")

# ===== LOOP PRINCIPAL =====
prev_message = ""

while True:
    try:
        # Leitura dos sensores
        distancia = round(sensor1.distance_cm(), 1)
        chuva = sensor_chuva.value()  # 0 = sem chuva, 1 = chuva detectada

        print(f"Distância: {distancia} cm | Chuva: {'Sim' if chuva else 'Não'}")

        # Criar mensagem JSON esperada pelo HTML
        message = ujson.dumps({
            "nivel_agua_cm": distancia,
            "chuva": chuva
        })

        # Enviar apenas se os dados mudarem
        if message != prev_message:
            print("🔄 Publicando dados no MQTT...")
            client.publish(MQTT_TOPIC, message)
            prev_message = message
        else:
            print("Sem alteração nos dados")

        # Exibir alerta no console se necessário
        if distancia > 200:
            print("🚨 ALERTA: Enchente iminente! Nível de água elevado.")

    except Exception as e:
        print("Erro ao ler sensores ou enviar MQTT:", str(e))

    sleep(5)
