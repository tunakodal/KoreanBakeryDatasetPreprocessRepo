import pandas as pd

# CSV dosyasını oku
df = pd.read_csv("../../data/processed/KoreanDataset_1.1.csv")  # Kendi dosya adını yaz

# 'Total' kolonunu sil
if "total" in df.columns:
    df = df.drop(columns=["total"])

# Kolon adlarının baş harflerini büyük yap
df.columns = [col.capitalize() for col in df.columns]

# Güncellenmiş CSV dosyasını kaydet
df.to_csv("../../data/processed/KoreanDataset_1.2.csv", index=False)
