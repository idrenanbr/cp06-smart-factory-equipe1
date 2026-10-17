#include <WiFi.h>
#include <PubSubClient.h>
#include <DHT.h>

constexpr int DHT_PIN = 15;
constexpr int LED_VERDE = 18;
constexpr int LED_VERMELHO = 19;
const char* TOPICO = "edge/2ano/2CCPH/equipe11/ff84fafa1219/dados";
DHT dht(DHT_PIN, DHT22);
WiFiClient rede;
PubSubClient mqtt(rede);
unsigned long ultimaLeitura = 0;
unsigned long ultimaTentativa = 0;
float temperatura = NAN;
float umidade = NAN;
bool alerta = false;

void setup() {
  Serial.begin(115200);
  pinMode(LED_VERDE, OUTPUT);
  pinMode(LED_VERMELHO, OUTPUT);
  digitalWrite(LED_VERDE, LOW);
  digitalWrite(LED_VERMELHO, LOW);
  dht.begin();
  WiFi.begin("Wokwi-GUEST", "", 6);
  mqtt.setServer("broker.hivemq.com", 1883);
  mqtt.setSocketTimeout(1);
}

void loop() {
  unsigned long agora = millis();
  // A decisao local acontece antes de qualquer tentativa MQTT.
  if (agora - ultimaLeitura >= 5000) {
    ultimaLeitura = agora;
    temperatura = dht.readTemperature();
    umidade = dht.readHumidity();
    if (!isnan(temperatura) && !isnan(umidade)) {
      alerta = temperatura > 35.0;
      digitalWrite(LED_VERDE, alerta ? LOW : HIGH);
      digitalWrite(LED_VERMELHO, alerta ? HIGH : LOW);
      char payload[128];
      snprintf(payload, sizeof(payload), "{\"temperatura\":%.1f,\"umidade\":%.1f,\"estado\":\"%s\"}", temperatura, umidade, alerta ? "ALERTA" : "NORMAL");
      Serial.println(payload);
      if (mqtt.connected()) mqtt.publish(TOPICO, payload, false);
    } else {
      Serial.println("Falha na leitura DHT22; publicacao ignorada");
    }
  }
  if (WiFi.status() == WL_CONNECTED) {
    if (!mqtt.connected() && agora - ultimaTentativa >= 5000) {
      ultimaTentativa = agora;
      String id = "esp32-" + String((uint32_t)ESP.getEfuseMac(), HEX);
      mqtt.connect(id.c_str());
    }
    if (mqtt.connected()) mqtt.loop();
  }
  delay(10);
}
