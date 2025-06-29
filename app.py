from flask import Flask, request, render_template, jsonify, send_file
import os

app = Flask(__name__)
FILE_PATH = "main_note.txt"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/load', methods=['GET'])
def load_text():
    if not os.path.exists(FILE_PATH):
        return jsonify({"content": ""})
    with open(FILE_PATH, 'r', encoding='utf-8') as f:
        return jsonify({"content": f.read()})

@app.route('/save', methods=['POST'])
def save_text():
    data = request.json
    content = data.get("content", "")
    with open(FILE_PATH, 'w', encoding='utf-8') as f:
        f.write(content)
    return jsonify({"status": "saved"})

@app.route('/download', methods=['GET'])
def download():
    if os.path.exists(FILE_PATH):
        return send_file(FILE_PATH, as_attachment=True)
    else:
        return {"error": "File not found"}, 404
