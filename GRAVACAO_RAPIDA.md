# Gravação rápida — Equipe 11 / 2CCPH

Antes de gravar: use um computador com Docker ativo, inicie INICIAR.cmd, abra o projeto Wokwi https://wokwi.com/projects/478094294106915841, a API http://localhost:5000/dados e o dashboard http://localhost:5001. Não grave senhas ou outras abas pessoais.

## 0:00–0:25 — apresentação e contêineres
Mostre api e dashboard ativos no Docker Desktop ou em docker compose ps.
Fala: “Somos a Equipe 11 da turma 2CCPH. Este é o CP06 Smart Factory. O ESP32 lê temperatura e umidade e decide o estado localmente. Os dados passam pelo HiveMQ para uma API Flask e um dashboard Flask. As duas aplicações rodam em contêineres separados.”

## 0:25–0:50 — 30 graus
Inicie Wokwi e ajuste o DHT22 para 30 graus. Aguarde ao menos 5 segundos. Mostre LED verde, atualize a API e clique Atualizar no dashboard.
Fala: “Com 30 graus, o estado é NORMAL e o LED verde está aceso. A API e o dashboard mostram a mesma temperatura, umidade e estado enviados pelo ESP32.”

## 0:50–1:15 — exatamente 35 graus
Ajuste para 35 graus. Aguarde a publicação, mostre LEDs, atualize a API e o dashboard.
Fala: “Exatamente 35 graus ainda é NORMAL. O alerta ocorre somente quando a temperatura ultrapassa 35 graus.”

## 1:15–1:40 — 36 graus
Ajuste para 36 graus. Aguarde a publicação, mostre LED vermelho, atualize API e dashboard.
Fala: “Com 36 graus, o próprio ESP32 muda para ALERTA e acende o LED vermelho. Essa decisão não depende de comandos da API ou do dashboard.”

## 1:40–2:05 — retorno a 30 graus
Ajuste para 30 graus. Aguarde a publicação, mostre LED verde e atualize API e dashboard.
Fala: “Ao voltar a 30 graus, o estado retorna a NORMAL. A umidade é exibida, mas não altera o estado. As leituras são publicadas a cada cinco segundos em um tópico exclusivo da equipe.”

## 2:05–2:20 — repositório
Mostre o README.
Fala: “O repositório público contém firmware, circuito Wokwi, código das aplicações, Dockerfiles e Compose. O README explica como executar e reúne os links da simulação e desta demonstração.”

## Publicar e finalizar
Título: CP06 Smart Factory — Equipe 11 — 2CCPH
Descrição: Demonstração de ESP32 e DHT22 no Wokwi, MQTT HiveMQ, API Flask e dashboard Flask com Docker Compose. Repositório: https://github.com/idrenanbr/cp06-smart-factory-equipe1
Visibilidade: Não listado.
Envie o endereço do vídeo ao assistente para inclusão no README.

A execução do GitHub Actions comprova testes Docker, mas não substitui mostrar o sistema integrado na gravação exigida.
