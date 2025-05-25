from flask import Flask, jsonify, request
import random
import string
import os

app = Flask(__name__)

# توليد مفتاح بالشكل XXXX-XXXX-XXXX-XXXX
def generate_key():
    return '-'.join(
        ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
        for _ in range(4)
    )

# Endpoint يولد مفتاح
@app.route('/store_key', methods=['POST'])
def store_key():
    key = generate_key()

    # يحفظ المفتاح في ملف keys.txt
    with open("keys.txt", "a") as f:
        f.write(key + "\n")

    return jsonify({"key": key})

# Endpoint يرجع كل المفاتيح المحفوظة
@app.route('/get_keys', methods=['GET'])
def get_keys():
    if not os.path.exists("keys.txt"):
        return jsonify({"keys": []})
    
    with open("keys.txt", "r") as f:
        keys = f.read().splitlines()
    
    return jsonify({"keys": keys})

# تشغيـل السيرفر على المنفذ اللي تعطيه Railway
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # يستخدم منفذ البيئة
    app.run(host='0.0.0.0', port=port)
