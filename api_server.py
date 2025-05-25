from flask import Flask, jsonify
import random
import string

app = Flask(__name__)

# صفحة رئيسية
@app.route('/')
def home():
    return "API is running!"

# دالة توليد مفتاح عشوائي بصيغة FT9Q-XZPW-MJ38-KLVT
def generate_key():
    parts = []
    for _ in range(4):
        part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
        parts.append(part)
    return '-'.join(parts)

# نقطة نهاية توليد المفتاح
@app.route('/generate_key')
def get_key():
    key = generate_key()
    return jsonify({"key": key})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
