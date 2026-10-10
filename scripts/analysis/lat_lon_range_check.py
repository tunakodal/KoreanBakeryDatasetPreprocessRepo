import pandas as pd

# Dataset'i oku
df = pd.read_csv("../../data/processed/KoreanDataset_2.2.csv")  # Dosyanın adını kendi dosyana göre değiştir

# Filtreleme kriterleri
filtered_df = df[
    (df["Latitude"] >= 37.80) & (df["Latitude"] <= 38.00) &
    (df["Longitude"] >= 127.60) & (df["Longitude"] <= 127.90)
]

# Sonuçları hesapla
filtered_count = len(filtered_df)
total_count = len(df)
ratio = filtered_count / total_count if total_count > 0 else 0  # Bölme hatasını önlemek için

# Sonuçları dosyaya yaz
with open("../../logs/lat_lon_range_check.txt", "w", encoding="utf-8") as f:
    f.write(f"Belirtilen aralıktaki satır sayısı: {filtered_count}\n")
    f.write(f"Toplam satır sayısı: {total_count}\n")
    f.write(f"Oran: {ratio:.6f}\n")  # Oranı 6 ondalık basamakla yazıyor

print("İşlem tamamlandı, sonuçlar 'lat_lon_range_check.txt' dosyasına kaydedildi.")
