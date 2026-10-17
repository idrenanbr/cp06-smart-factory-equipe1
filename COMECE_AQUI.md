# Equipe 11 - 2CCPH: passos para entregar

## 1. Preparar Docker (uma vez)
Instale Docker Desktop para Windows pelo site oficial: https://docs.docker.com/desktop/setup/install/windows-install/.
Se o instalador indicar WSL ausente, siga o procedimento oficial: https://learn.microsoft.com/windows/wsl/install.
Pode ser necessário autorizar como administrador, ativar virtualização e reiniciar o computador. Depois abra Docker Desktop e espere ficar pronto.

## 2. Iniciar o projeto
Extraia o ZIP inteiro. Dentro da pasta smart-factory, dê dois cliques em INICIAR.cmd. Ele constrói e inicia os dois contêineres e abre API e dashboard. Alternativa: `docker compose up --build` nessa pasta.

Sem Wokwi publicando, é esperado que a API mostre Aguardando dados do ESP32 e o dashboard mostre Aguardando dados.

## 3. Salvar a simulação
A simulação já foi salva e compilada: https://wokwi.com/projects/478094294106915841.
Abra esse projeto e clique no botão verde de iniciar. Não precisa montar novamente.
Os arquivos da pasta wokwi são uma cópia para consulta e recuperação.

## 4. Conferir o funcionamento
Ajuste o DHT22 para 30, 35, 36 e 30 °C. Para cada ajuste, aguarde a publicação seguinte, recarregue a API e clique Atualizar no dashboard. A sequência deve ser NORMAL, NORMAL, ALERTA, NORMAL. Compare os LEDs com os estados.

## 5. Gravar
Deixe Wokwi, API e dashboard abertos. Mostre os contêineres em execução no Docker Desktop. Grave a tela seguindo ROTEIRO_VIDEO.md. O vídeo precisa ter 2 a 5 minutos e mostrar a execução real.
Publique no YouTube com visibilidade Não listado e coloque o endereço no README.

## 6. Publicar GitHub
O projeto já está publicado: https://github.com/idrenanbr/cp06-smart-factory-equipe1.
Após publicar o vídeo, falta incluir seu link no README. Você pode enviar o link ao assistente para essa atualização.

## 7. Entregar
Abra os três links em janela anônima: GitHub, Wokwi e YouTube. Confira se abrem sem convite. No canal definido pelo professor, envie o link do GitHub.

## Se algo falhar
- Docker não inicia: confira WSL, virtualização e eventual reinício pendente.
- Portas ocupadas: encerre outra aplicação que use 5000 ou 5001.
- API aguardando: confira se Wokwi está rodando, MQTT conectado e tópico igual nos arquivos.
- Dashboard aguardando: aguarde nova publicação e clique Atualizar; veja os registros do contêiner api no Docker Desktop.
