from flask import Flask, render_template
from flask_socketio import SocketIO
import paho.mqtt.client as mqtt
import json

app = Flask(__name__)
socketio = SocketIO(app)

mqtt_broker = 'test.mosquitto.org'
mqtt_topic = 'alerta_cidadao/sensor'  # Altere se necessário

@app.route('/')
def index():
    return render_template('index.html')

def on_connect(client, userdata, flags, rc):
    print("Conectado ao MQTT com código:", rc)
    client.subscribe(mqtt_topic)

def on_message(client, userdata, msg):
    try:
        payload = msg.payload.decode()
        print("Mensagem recebida:", payload)
        socketio.emit('distance_update', {'distance': payload})
    except Exception as e:
        print("Erro ao processar mensagem:", e)


mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message
mqtt_client.connect(mqtt_broker, 1883, 60)
mqtt_client.loop_start()

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)