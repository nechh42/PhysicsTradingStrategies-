import requests
import pandas as pd
from datetime import datetime

# GitHub'dan sinyalleri çek
def get_signals():
    url = "https://raw.githubusercontent.com/nechh42/PhysicsTradingStrategies/main/trading_signals.csv"
    return pd.read_csv(url)

# Son sinyali al
signals = get_signals()
last_signal = signals.iloc[-1]['Signal']

# Telegram'a gönder
bot_token = "8168877430:AAE4Ob5wZr1L5QhG8MMsA8jFNpF_BFcOTrA"  # @BotFather'dan aldığın token
chat_id = "7858725560"  # Kanal oluşturup ID'sini al
message = f"🚀 {datetime.now().strftime('%d.%m.%Y')} Sinyali: {last_signal}"
url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}"
requests.get(url)