"""Executado dentro do conteiner api, usando topico exclusivo de teste."""
import json
import os
import time
import urllib.request
import urllib.error
import paho.mqtt.client as mqtt


def consultar(url):
    try:
        with urllib.request.urlopen(url, timeout=5) as response:
            return response.status, response.read().decode()
    except urllib.error.HTTPError as error:
        return error.code, error.read().decode()


for tentativa in range(40):
    try:
        status, body = consultar("http://api:5000/dados")
        break
    except (OSError, urllib.error.URLError):
        time.sleep(1)
else:
    raise AssertionError("API nao iniciou")
assert status == 503, (status, body)
assert json.loads(body) == {"mensagem": "Aguardando dados do ESP32"}
for tentativa in range(20):
    try:
        assert "Aguardando dados" in consultar("http://dashboard:5001/")[1]
        break
    except (OSError, urllib.error.URLError):
        time.sleep(1)
else:
    raise AssertionError("Dashboard nao iniciou")

publisher = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2,
                        client_id="pub-" + os.environ["MQTT_CLIENT_ID"])
publisher.connect("broker.hivemq.com", 1883, 60)
publisher.loop_start()
try:
    # Cada publicacao ocorre no topico de CI, sem misturar dados da simulacao.
    for temperatura, estado in [(30, "NORMAL"), (35, "NORMAL"),
                                 (36, "ALERTA"), (30, "NORMAL")]:
        payload = {"temperatura": temperatura, "umidade": 60, "estado": estado}
        for tentativa in range(30):
            publisher.publish(os.environ["MQTT_TOPIC"], json.dumps(payload),
                              qos=1, retain=False).wait_for_publish(timeout=5)
            time.sleep(1)
            status, body = consultar("http://api:5000/dados")
            if status == 200 and json.loads(body) == payload:
                break
        else:
            raise AssertionError(f"MQTT nao chegou a API: {payload}; ultimo: {body}")
        html = consultar("http://dashboard:5001/")[1]
        assert estado in html and str(temperatura) in html, html
        print(f"OK: MQTT -> API -> dashboard: {temperatura} C / {estado}", flush=True)
        time.sleep(5)
finally:
    publisher.disconnect()
    publisher.loop_stop()
