import pandas as pd

# Örnek dataset
df = pd.read_csv("../../data/processed/KoreanDataset_2.0.csv")  # Kendi dosyanın adını buraya yaz

# Gün isimlerini sayısal değerlere çevirme
day_mapping = {
    "Mon": 1, "Tue": 2, "Wed": 3, "Thur": 4,
    "Fri": 5, "Sat": 6, "Sun": 7
}

df["Day"] = df["Day"].map(day_mapping)

# Güncellenmiş dataset'i kaydet
df.to_csv("../../data/processed/KoreanDataset_2.1.csv", index=False)

print("Day sütunu sayısal değerlere çevrildi ve dosyaya kaydedildi.")
