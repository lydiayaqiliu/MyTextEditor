from flask import Flask, request, render_template, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save', methods=['POST'])
def save():
    data = request.json
    content = data.get("content", "")
    filename = data.get("filename", "saved_note.txt")

    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

    return jsonify({"message": f"Saved to {filename}"})
