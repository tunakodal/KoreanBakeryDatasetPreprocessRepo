import pandas as pd

# Dataset'i oku
df = pd.read_csv("../Datasets/KoreanDataset_2.2.csv")  # Dosya adını kendi dosyana göre değiştir

# 'pres' sütunundaki değerleri 1000'e böl
df["pres"] = df["pres"] / 1000

# Güncellenmiş dataset'i kaydet
df.to_csv("../Datasets/KoreanDataset_2.3.csv", index=False)

print("pres sütunundaki değerler 1000'e bölündü ve dosya kaydedildi.")
