import os
import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.get("/")
def index():
    leitura = None
    try:
        response = requests.get(os.environ.get("API_URL", "http://api:5000/dados"), timeout=3)
        response.raise_for_status()
        data = response.json()
        if (isinstance(data, dict) and data.get("estado") in ("NORMAL", "ALERTA")
            and all(isinstance(data.get(k), (int, float)) and not isinstance(data.get(k), bool)
                    for k in ("temperatura", "umidade"))):
            leitura = data
    except (requests.RequestException, ValueError):
        pass
    return render_template("index.html", leitura=leitura)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=False)
