import json
import math
import os
from threading import Lock
from flask import Flask, jsonify
import paho.mqtt.client as mqtt

app = Flask(__name__)
lock = Lock()
ultima = None

def validar(payload):
    data = json.loads(payload)
    if not isinstance(data, dict):
        raise ValueError("Objeto JSON esperado")
    for campo in ("temperatura", "umidade"):
        valor = data.get(campo)
        if isinstance(valor, bool) or not isinstance(valor, (int, float)) or not math.isfinite(valor):
            raise ValueError("Medida invalida")
    if not 0 <= data["umidade"] <= 100:
        raise ValueError("Umidade invalida")
    if data.get("estado") not in ("NORMAL", "ALERTA"):
        raise ValueError("Estado invalido")
    if data["estado"] != ("ALERTA" if data["temperatura"] > 35 else "NORMAL"):
        raise ValueError("Estado inconsistente com a regra do ESP32")
    return {k: data[k] for k in ("temperatura", "umidade", "estado")}

def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        client.subscribe(os.environ["MQTT_TOPIC"])

def on_message(client, userdata, message):
    global ultima
    try:
        leitura = validar(message.payload)
    except (ValueError, TypeError, UnicodeError):
        app.logger.warning("Mensagem MQTT invalida ignorada")
        return
    with lock:
        ultima = leitura

@app.get("/dados")
def dados():
    with lock:
        leitura = ultima
    if leitura is None:
        return jsonify(mensagem="Aguardando dados do ESP32"), 503
    return jsonify(leitura)

def iniciar():
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id=os.environ.get("MQTT_CLIENT_ID", "smart-factory-api"))
    client.on_connect = on_connect
    client.on_message = on_message
    client.reconnect_delay_set(min_delay=1, max_delay=30)
    client.connect_async("broker.hivemq.com", 1883, 60)
    client.loop_start()
    return client

if __name__ == "__main__":
    client = iniciar()
    app.run(host="0.0.0.0", port=5000, debug=False, use_reloader=False)
