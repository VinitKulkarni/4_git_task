from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

DATA_FILE = 'data.json'

@app.route('/api', methods=['GET'])
def get_data():
    if not os.path.exists(DATA_FILE):
        return jsonify({"error": "Data file not found"}), 404

    try:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
        return jsonify(data)
    except json.JSONDecodeError:
        return jsonify({"error": "Error decoding JSON"}), 500

if __name__ == '__main__':
    app.run(debug=True)
