from flask import Flask, request, jsonify
import random
import string
import os

app = Flask(__name__)

KEY_FILE = "keys.txt"

def generate_key():
    sections = [''.join(random.choices(string.ascii_uppercase + string.digits, k=4)) for _ in range(4)]
    return '-'.join(sections)

@app.route('/store_key', methods=['POST'])
def store_key():
    key = generate_key()
    with open(KEY_FILE, "a") as f:
        f.write(key + "\n")
    return jsonify({"key": key})

@app.route('/get_keys', methods=['GET'])
def get_keys():
    if not os.path.exists(KEY_FILE):
        return jsonify({"keys": []})
    with open(KEY_FILE, "r") as f:
        keys = f.read().splitlines()
    return jsonify({"keys": keys})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
