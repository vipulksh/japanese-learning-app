from flask import Flask, render_template, jsonify
from data.passage import PASSAGES
from data.kanji import KANJI_DB

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/passages")
def get_passages():
    return jsonify(PASSAGES)


@app.route("/api/passage/<level>")
def get_passage(level):
    passage = PASSAGES.get(level)
    if not passage:
        return jsonify({"error": "Passage not found"}), 404
    return jsonify(passage)


@app.route("/api/kanji")
def get_kanji_db():
    return jsonify(KANJI_DB)


@app.route("/api/kanji/<character>")
def get_kanji(character):
    data = KANJI_DB.get(character)
    if not data:
        return jsonify({"error": "Not found"}), 404
    return jsonify({"character": character, **data})


if __name__ == "__main__":
    app.run(debug=True, port=5001)
