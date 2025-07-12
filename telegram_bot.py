import requests
import pandas as pd
from datetime import datetime
import os

def get_signals():
    url = "https://raw.githubusercontent.com/nechh42/PhysicsTradingStrategies-/main/trading_signals.csv"
    return pd.read_csv(url)

signals = get_signals()
last_signal = signals.iloc[-1]['Signal']

bot_token = os.environ["TELEGRAM_BOT_TOKEN"]
chat_id = os.environ["TELEGRAM_CHAT_ID"]
message = f"🚀 {datetime.now().strftime('%d.%m.%Y')} Sinyali: {last_signal}"
url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}"

response = requests.get(url)
if response.status_code == 200:
    print("Mesaj başarıyla gönderildi.")
else:
    print(f"Mesaj gönderilemedi. Hata kodu: {response.status_code}")