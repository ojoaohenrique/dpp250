from flask import Flask, jsonify, request, send_file
import json
from pathlib import Path

app = Flask(__name__, static_folder="", static_url_path="")
DATA_FILE = Path(__file__).with_name("json")


def load_defaults():
    if DATA_FILE.exists():
        try:
            with DATA_FILE.open("r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}


@app.route("/")
def home():
    return send_file("index.html")


@app.route("/defaults")
def defaults():
    return jsonify(load_defaults())


@app.route("/imprimir", methods=["POST"])
def imprimir():
    data = request.form.to_dict() or request.get_json(silent=True) or {}
    lines = [f"{key.capitalize()}: {value}" for key, value in data.items() if value]
    body = "\n".join(lines) if lines else "Nenhum dado recebido."
    return (
        "<!DOCTYPE html>"
        "<html lang=\"pt-br\">"
        "<head><meta charset=\"UTF-8\"><title>Guia de Auto</title></head>"
        "<body><h1>Guia de auto de remoção</h1>"
        f"<pre>{body}</pre>"
        "<p><a href=\"/\">Voltar</a></p>"
        "</body></html>"
    )


if __name__ == "__main__":
    app.run(debug=True, port=8000)


    