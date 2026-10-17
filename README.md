# CP06 - Smart Factory

**Primeiro acesso:** veja [COMECE_AQUI.md](COMECE_AQUI.md). No Windows, use `INICIAR.cmd` depois de preparar o Docker.

## Identificação
- Turma: 2CCPH
- Equipe: Equipe 11
- Integrantes:
  - Auro Vanetti de Moura Andrade — RA 563761
  - Bruno Soares de Santanna — RA 562235
  - Enzo Hideki Kobayashi Nishida — RA 565052
  - Enzo Yokokura Araujo — RA 564177
  - Marco Antonio Ferreira Fonseca — RA 566434
  - Renan Mano Otero — RA 554911
- Projeto Wokwi: https://wokwi.com/projects/478094294106915841
- Vídeo YouTube (Não listado): PENDENTE DE GRAVAÇÃO E PUBLICAÇÃO

## Arquitetura
ESP32 → HiveMQ → API → dashboard.

O ESP32 lê o DHT22, decide o estado e controla os LEDs localmente. Temperatura > 35 °C acende vermelho (ALERTA); temperatura ≤ 35 °C acende verde (NORMAL). A umidade não interfere na decisão. O HiveMQ transporta as mensagens. A API assina o tópico e guarda apenas a última leitura válida em memória. O backend do dashboard consulta a API pela rede interna do Compose.

## MQTT
- Broker público: `broker.hivemq.com:1883`
- Tópico completo: `edge/2ano/2CCPH/equipe11/ff84fafa1219/dados`
- Clientes distintos: ESP32 usa identificador derivado do chip; API usa `api-ff84fafa1219`.
- Publicação a cada 5 segundos enquanto conectado, sem mensagens retidas.
- Exemplo: `{"temperatura":36.0,"umidade":60.0,"estado":"ALERTA"}`
- Somente dados simulados. O tópico exclusivo não oferece privacidade.

## Executar
1. Instale e inicie Docker com Compose e mantenha acesso à internet.
2. Na pasta deste README, execute `docker compose up --build`.
3. Abra a API em http://localhost:5000/dados e o dashboard em http://localhost:5001.
4. Abra o projeto Wokwi e inicie a simulação conforme a seção abaixo.
5. Aguarde a conexão e a próxima publicação; clique em **Atualizar** no dashboard.
6. Para encerrar: `docker compose down`.

São somente dois serviços: `api` e `dashboard`. Não há broker local. As duas aplicações escutam em `0.0.0.0`. Não há banco de dados ou histórico. A API começa com HTTP 503 e `{"mensagem":"Aguardando dados do ESP32"}`. O dashboard mostra **Aguardando dados** quando não consegue obter uma leitura.

## Preparar o Wokwi
1. Crie um projeto ESP32 em https://wokwi.com/projects/new/esp32.
2. Substitua `sketch.ino` e `diagram.json` pelos arquivos da pasta `wokwi`.
3. Adicione as bibliotecas de `libraries.txt` pelo gerenciador de bibliotecas.
4. Salve o projeto e copie o link público para a identificação deste README.
5. Inicie a simulação. Clique no DHT22 para ajustar temperatura e umidade.

Ligações: DHT22 VCC em 3V3, GND em GND, SDA em GPIO15; LEDs verde e vermelho em GPIO18 e GPIO19, cada um com resistor de 220 Ω em série e cátodo no GND.

## Teste integrado obrigatório
| Temperatura | LED verde | LED vermelho | Estado |
|---|---|---|---|
| 30 °C | Aceso | Apagado | NORMAL |
| 35 °C | Aceso | Apagado | NORMAL |
| 36 °C | Apagado | Aceso | ALERTA |
| 30 °C | Aceso | Apagado | NORMAL |

Em cada etapa, espere a próxima publicação (5 segundos), consulte GET /dados e clique em Atualizar no dashboard. Compare temperatura, umidade e estado com o monitor serial e os LEDs. Antes da primeira leitura, confirme HTTP 503. Desconecte a API e atualize a página para confirmar Aguardando dados. Variações de umidade não devem mudar o estado.

## Dificuldade técnica e solução
Uma indisponibilidade do MQTT não pode impedir a decisão na borda. O firmware lê o sensor e atualiza os LEDs antes de tentar reconectar ao broker; as tentativas são espaçadas e o tempo de espera MQTT é limitado. Mensagens inválidas são ignoradas pela API para preservar a última leitura válida. Após perda de conexão, a última leitura permanece na memória, sem indicação de atualização; não há histórico nem detecção de dados antigos neste escopo.

## Vídeo (2 a 5 minutos)
Siga `ROTEIRO_VIDEO.md`. Grave a execução real e publique como **Não listado**. Inclua o link neste README.

## Finalizar a entrega
- Complete identificação e links reais; não entregue com pendências.
- Publique todos estes arquivos em um repositório público GitHub.
- Valide GitHub, Wokwi e vídeo em janela anônima, sem convite ou autorização.
- Confirme no YouTube a visibilidade Não listado.
- Envie o link do repositório no canal do professor e mantenha os três links acessíveis até a avaliação.

## Validação local
Veja `VALIDACAO.md` para os testes executados e as pendências. A aba Actions do GitHub executa a construção dos dois contêineres e um teste MQTT → API → dashboard em tópico exclusivo de teste. A execução normal usa o tópico da equipe indicado acima; variáveis de ambiente só substituem esse tópico durante testes isolados.
