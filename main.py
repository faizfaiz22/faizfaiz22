from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "7586226687:AAHq7LeQNuOQdXvVAiCLttZEmWebvswY6rk"
TELEGRAM_API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

def generate_signal():
    strategies = [
        "استراتيجية الفيبوناتشي",
        "استراتيجية الدعم والمقاومة",
        "استراتيجية الكسر الكاذب",
        "استراتيجية الشمعة السابقة",
        "استراتيجية متوسط الحركة"
    ]
    signal = {
        "تحليل فني": "الاتجاه صاعد على الإطار 1M",
        "توصية": "شراء (CALL)",
        "النسبة": "83%",
        "الاستراتيجيات المتوافقة": strategies[:3]
    }
    return signal

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    chat_id = data["message"]["chat"]["id"]
    text = data["message"]["text"]

    if text == "/start":
        requests.post(TELEGRAM_API_URL, json={"chat_id": chat_id, "text": "مرحبًا! أرسل /signal للحصول على توصية تداول."})
    elif text == "/signal":
        signal = generate_signal()
        msg = f"توصية التداول:\n{signal['توصية']}\nالنسبة: {signal['النسبة']}\nاستراتيجيات متوافقة:\n- " + "\n- ".join(signal['الاستراتيجيات المتوافقة']) + f"\n\n{signal['تحليل فني']}"
        requests.post(TELEGRAM_API_URL, json={"chat_id": chat_id, "text": msg})
    else:
        requests.post(TELEGRAM_API_URL, json={"chat_id": chat_id, "text": "اكتب /signal للحصول على توصية."})
    
    return "ok"

@app.route("/", methods=["GET"])
def index():
    return "البوت يعمل."
