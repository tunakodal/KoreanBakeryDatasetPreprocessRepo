import pandas as pd
import yfinance as yf

# CSV dosyanı oku
df = pd.read_csv("../Datasets/KoreanDataset_1.6.1.csv")

# Tarih formatını düzenle
df["Date"] = pd.to_datetime(df["Date"])

# yfinance sembolleri
brent_symbol = "BZ=F"  # Brent Crude Oil
wti_symbol = "CL=F"    # WTI Crude Oil

# Tarih aralığını belirle (30 gün geriye giderek çekiyoruz)
start_date = (df["Date"].min() - pd.Timedelta(days=30)).strftime("%Y-%m-%d")
end_date = (df["Date"].max() + pd.Timedelta(days=1)).strftime("%Y-%m-%d")

# Brent ve WTI fiyatlarını çekmeye çalış
brent_data = yf.download(brent_symbol, start=start_date, end=end_date, progress=False)
wti_data = yf.download(wti_symbol, start=start_date, end=end_date, progress=False)

# "Close" sütunu olup olmadığını kontrol et
if "Close" in brent_data.columns and "Close" in wti_data.columns:
    brent_data = brent_data["Close"]
    wti_data = wti_data["Close"]
else:
    print("Hata: Yahoo Finance 'Close' fiyatlarını sağlamıyor!")
    brent_data = pd.Series()
    wti_data = pd.Series()

# Boş olan fiyatları bir önceki güne doldur
brent_data.ffill(inplace=True)
wti_data.ffill(inplace=True)

# Date kolonunu string formatına çevir (eşleşmeyi doğru yapmak için)
df["Date"] = df["Date"].dt.strftime("%Y-%m-%d")

# Yakın tarihlerin fiyatlarını eşleştir
df["BrentPrice"] = df["Date"].map(brent_data.to_dict())
df["WTIPrice"] = df["Date"].map(wti_data.to_dict())

# Ortalama fiyatı hesapla
df["AveragePrice"] = df[["BrentPrice", "WTIPrice"]].mean(axis=1)

# Yeni dosyayı kaydet
df.to_csv("../Datasets/KoreanDataset_1.7.csv", index=False)

print("BrentPrice, WTIPrice ve AveragePrice başarıyla eklendi!")
