import pandas as pd
import yfinance as yf

# SPY verilerini çek
data = yf.download("SPY", start="2023-01-01", end="2024-07-15")

def calculate_entropy(window=20):
    data['SMA'] = data['Close'].rolling(window).mean()
    data['STD'] = data['Close'].rolling(window).std()
    data['Entropy'] = data['STD'] / data['SMA']
    return data

# Sinyal üret
df = calculate_entropy()
df['Signal'] = df['Entropy'].apply(lambda x: 'SHORT' if x > 1.65 else 'CASH')

# Sonuçları CSV'ye kaydet
df.to_csv('trading_signals.csv')
print("Sinyaller oluşturuldu! GitHub Actions otomatik güncelleyecek.")