import pandas as pd
import yfinance as yf

# CSV dosyanı oku
df = pd.read_csv("../Datasets/KoreanDataset_1.6.1.csv")

# Tarih formatını düzenle
df["Date"] = pd.to_datetime(df["Date"])

# yfinance sembolleri
brent_symbol = "BZ=F"  # Brent Crude Oil
wti_symbol = "CL=F"  # WTI Crude Oil

# Tarih aralığını belirle (30 gün geriye giderek çekiyoruz)
start_date = (df["Date"].min() - pd.Timedelta(days=30)).strftime("%Y-%m-%d")
end_date = (df["Date"].max() + pd.Timedelta(days=1)).strftime("%Y-%m-%d")

# Brent ve WTI fiyatlarını çekme fonksiyonu
def fetch_yfinance_data(symbol):
    print(f"📡 {symbol} fiyatları çekiliyor... ({start_date} - {end_date})")
    data = yf.download(symbol, start=start_date, end=end_date, progress=False)

    if "Close" in data.columns:
        data = data[["Close"]].rename(columns={"Close": symbol})
    else:
        print(f"⚠️ Hata: {symbol} için 'Close' fiyatı alınamadı!")
        return pd.DataFrame(columns=["Date", symbol])

    # Index'i sıfırla ve Date sütununu oluştur
    data.reset_index(inplace=True)  # Index'i düzelt
    data["Date"] = pd.to_datetime(data["Date"])  # Formatı düzelt

    # Check if Date column exists after reset
    if "Date" not in data.columns:
        raise ValueError(f"Date sütunu eksik: {symbol}")

    print(f"✅ {symbol} fiyatları çekildi!\n", data.head())  # İlk 5 satırı terminale yazdır
    return data

# Verileri çek ve sütunları adlandır
brent_data = fetch_yfinance_data(brent_symbol)
wti_data = fetch_yfinance_data(wti_symbol)

# Sütun isimlerini düzle (MultiIndex'i düzleştir)
brent_data.columns = brent_data.columns.get_level_values(0) if isinstance(brent_data.columns, pd.MultiIndex) else brent_data.columns
wti_data.columns = wti_data.columns.get_level_values(0) if isinstance(wti_data.columns, pd.MultiIndex) else wti_data.columns

# DataFrame'leri kontrol et
print("Brent Data Sütunları:", brent_data.columns)
print("WTI Data Sütunları:", wti_data.columns)

# Sütunları doğru şekilde ayarla
brent_data = brent_data[["Date", brent_symbol]].rename(columns={brent_symbol: "BrentPrice"})
wti_data = wti_data[["Date", wti_symbol]].rename(columns={wti_symbol: "WTIPrice"})

# Date formatını eşitle (datetime64[ns] olarak)
brent_data["Date"] = pd.to_datetime(brent_data["Date"])
wti_data["Date"] = pd.to_datetime(wti_data["Date"])

# DataFrame'leri birleştir
df = df.merge(brent_data, on="Date", how="left")
df = df.merge(wti_data, on="Date", how="left")

# Eksik fiyatları doldur
df["BrentPrice"].ffill(inplace=True)
df["WTIPrice"].ffill(inplace=True)

# Ortalama fiyatı hesapla
df["AveragePrice"] = df[["BrentPrice", "WTIPrice"]].mean(axis=1, skipna=True)

# Yeni dosyayı kaydet
df.to_csv("../Datasets/KoreanDataset_1.7.csv", index=False)

print("\n📁 Yeni dosya başarıyla kaydedildi: KoreanDataset_1.7.csv")