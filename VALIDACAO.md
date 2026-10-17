# Validação realizada

- Sintaxe dos arquivos Python verificada.
- Estrutura JSON do diagrama verificada.
- Função de validação da API executada com 30, 35, 36 e 30 °C: estados esperados aceitos.
- Mensagens inválidas, booleanos como medidas, umidade fora da faixa e estado inconsistente rejeitados.

- API Flask testada: HTTP 503 inicial e HTTP 200 nas quatro etapas, com mensagens MQTT simuladas.
- Dashboard renderizado nas quatro etapas; consulta interna verificada com resposta controlada.
- Indisponibilidade da API testada: página mostra Aguardando dados.

- Integração real via HiveMQ TCP 1883, API HTTP e dashboard HTTP validada com publicador de teste em tópico separado: 30/NORMAL, 35/NORMAL, 36/ALERTA, 30/NORMAL.
- Wokwi salvo como projeto público: https://wokwi.com/projects/478094294106915841

## Validação Wokwi
- Firmware compilado e executado no Wokwi; Wi-Fi conectado ao Wokwi-GUEST.
- DHT22 ajustado na sequência 30, 35, 36 e 30 °C. Monitor serial e API HTTP real confirmaram NORMAL, NORMAL, ALERTA e NORMAL.
- LED verde observado em 30 °C e vermelho em 36 °C; dashboard exibiu 36 °C / 60% / ALERTA com dados originados no ESP32.
- A integração ESP32 → HiveMQ → API → dashboard foi executada fora do Docker, em validação local. Isso não substitui o teste dos contêineres.

## Pendências de entrega
- Repositório GitHub público publicado e acessado sem autenticação.
- Construir e executar os dois contêineres: Docker não encontrado neste ambiente.
- Gravar e publicar o vídeo real e validar os links públicos.

Os testes de lógica não comprovam a integração completa. Os campos pendentes no README precisam ser preenchidos antes da entrega.
