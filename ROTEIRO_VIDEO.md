# Roteiro de gravação — cerca de 3 minutos

0:00–0:25 — Apresente equipe e arquitetura ESP32 → HiveMQ → API → dashboard. Explique que os LEDs são controlados no ESP32.

0:25–0:45 — Mostre os dois serviços ativos com `docker compose ps`, o Wokwi, a API e o dashboard.

0:45–1:15 — Ajuste para 30 °C. Aguarde a publicação, mostre LED verde, GET /dados e clique Atualizar. Estado NORMAL.

1:15–1:45 — Ajuste para exatamente 35 °C. Aguarde, mostre LEDs, JSON e dashboard atualizado. Estado NORMAL.

1:45–2:15 — Ajuste para 36 °C. Aguarde, mostre LED vermelho, JSON e dashboard atualizado. Estado ALERTA.

2:15–2:45 — Volte a 30 °C. Aguarde, mostre LED verde, JSON e dashboard atualizado. Estado NORMAL.

2:45–3:10 — Mostre a umidade e explique que ela não muda o estado. Mostre README, tópico exclusivo e links.

Publique no YouTube como Não listado, copie o endereço para o README e valide em janela anônima. Não grave credenciais ou informações particulares.
