import pandas as pd
from meteostat import Point, Daily
import time

# Dosyayı oku (parse_dates KULLANMADAN)
df = pd.read_csv("../../data/processed/KoreanDataset_1.5.1.csv")

# Date sütununu datetime formatına çevir
df["Date"] = pd.to_datetime(df["Date"], errors="coerce", format="%Y-%m-%d")

# Yeni sütunlar oluştur
for col in ["tmax", "tmin", "tavg", "wspd", "pres"]:
    df[col] = None  # Başlangıçta None olarak ayarla

# Hava durumu verilerini çekme işlemi
for index, row in df.iterrows():
    try:
        # Longitude ve Latitude değerlerini al
        lat, lon = row["Latitude"], row["Longitude"]

        # Tarih bilgisini al
        date = row["Date"]

        # Eğer tarih NaT (boş) ise atla
        if pd.isna(date):
            continue

        # Meteostat için konum belirleme
        location = Point(lat, lon)

        # Günlük hava durumu verilerini çekme
        weather_data = Daily(location, date, date)
        weather_data = weather_data.fetch()

        if not weather_data.empty:
            df.at[index, "tmax"] = weather_data["tmax"].values[0]
            df.at[index, "tmin"] = weather_data["tmin"].values[0]
            df.at[index, "tavg"] = weather_data["tavg"].values[0]
            df.at[index, "wspd"] = weather_data["wspd"].values[0]
            df.at[index, "pres"] = weather_data["pres"].values[0]

        # API'ye aşırı yüklenmemek için bekleme süresi
        time.sleep(1)

    except Exception as e:
        print(f"Hata (Satır {index}): {e}")

# Güncellenmiş dosyayı kaydet
df.to_csv("../../data/processed/KoreanDataset_1.6.0.csv", index=False)

print("İşlem tamamlandı! Güncellenmiş dosya kaydedildi.")
