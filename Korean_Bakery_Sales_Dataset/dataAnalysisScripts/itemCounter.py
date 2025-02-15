import pandas as pd

# CSV dosyasını yükle
df = pd.read_csv("../Datasets/KoreanDataset_2.3.csv")  # Dosya adını değiştir

# Wiener sütunundaki değerleri toplama
toplam_wiener = df["Milk tea"].sum()

print("Item sütunu toplamı:", toplam_wiener)
