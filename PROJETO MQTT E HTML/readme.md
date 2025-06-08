# 🚨 Alerta Cidadão – Sistema de Monitoramento de Enchentes

Este projeto tem como objetivo monitorar enchentes em tempo real utilizando sensores conectados a um ESP32, com transmissão de dados via MQTT para um dashboard web. A solução visa alertar moradores de áreas de risco com informações visuais e sonoras sobre o nível da água e condições climáticas.

## 📦 Tecnologias Utilizadas

- ESP32 (simulado no Wokwi)
- Sensor Ultrassônico HC-SR04 (nível da água)
- Sensor de chuva (digital)
- MicroPython
- MQTT (via test.mosquitto.org)
- HTML5 + CSS3 (Dashboard responsivo)
- Node-RED (integração e visualização)
- Socket.IO

⚙️ Funcionamento
ESP32 (Wokwi):

Mede a distância da água com HC-SR04.

Detecta presença de chuva.

Envia os dados em formato JSON via MQTT.

Servidor Python (MQTT + WebSocket):

Conecta-se ao broker MQTT.

Escuta o tópico alerta_cidadao/sensor.

Emite eventos para o dashboard HTML via Socket.IO.

Dashboard Web (HTML):

Interface responsiva que exibe o nível de água e estado do tempo.

Mostra alertas de enchente, número da polícia civil local e chuva detectada.


📡Exemplo de Payload JSON enviado

{
  "nivel_agua_cm": 32.45,
  "chuva": 1
}

🖥️ Como Rodar o Projeto
1. Rodando no Wokwi
Acesse https://wokwi.com

Importe o código main.py e conecte os sensores virtuais:

HC-SR04: Trigger no GPIO 5, Echo no GPIO 18

Sensor de chuva no GPIO 15 (digital)

Rode o simulador com o Wi-Fi Wokwi-GUEST

2. Rodando o servidor Python (MQTT + Socket.IO)
Certifique-se de que o Python 3.11+ está instalado. Em seguida, instale as dependências: pip install paho-mqtt flask flask-socketio

Execute: python mqtt_alerta.py

3. Acessando o Dashboard
Abra o arquivo index.html no seu navegador (com o servidor Python rodando).



🧠 Lógica de Alerta
Se a distância da água for menor que 20 cm, um alerta de enchente é gerado.

Se o sensor de chuva detectar chuva (valor 1), um alerta visual é emitido.

O dashboard exibe essas informações de forma clara e acessível.

🧰 Fluxo Node-RED
Importe o fluxo node-red-flow.json no seu ambiente Node-RED para visualizar e registrar os dados.

📞 Informações de Emergência
A interface mostra:

⚠️ Alerta de enchente próximo

☔️ Chuva detectada

📞 Contato da polícia civil local: 197