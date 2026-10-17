@echo off
cd /d "%~dp0"
where docker >nul 2>nul
if errorlevel 1 (
 echo Docker nao encontrado. Consulte COMECE_AQUI.md.
 pause
 exit /b 1
)
docker info >nul 2>nul
if errorlevel 1 (
 echo Abra o Docker Desktop e aguarde iniciar. Depois tente novamente.
 pause
 exit /b 1
)
docker compose up --build -d
if errorlevel 1 (
 echo Nao foi possivel iniciar. Confira a mensagem acima.
 pause
 exit /b 1
)
echo Projeto iniciado. Inicie tambem a simulacao Wokwi.
start "" "http://localhost:5001"
start "" "http://localhost:5000/dados"
docker compose ps
pause
