# Datetime'daki time silindi
# NaN Place'ler silindi
import pandas as pd

# CSV dosyasını oku
df = pd.read_csv("../Datasets/Bakery Sales.csv")  # Burada kendi dosya adını kullan

# Tarih kolonu adını belirle (örneğin, 'datetime_column' adında olduğunu varsayalım)
datetime_col = "datetime"  # Gerçek kolon adını buraya yaz

# Saat kısmını kaldır ve sadece tarih kısmını al
df["Date"] = pd.to_datetime(df[datetime_col]).dt.date

# Eski kolonu kaldır
df = df.drop(columns=[datetime_col])

# Sola getir
cols = ["Date"] + [col for col in df.columns if col != "Date"]
df = df[cols]

# NaN Place'leri sil
df = df.dropna(subset=["place"])

# Güncellenmiş CSV dosyasını kaydet
df.to_csv("../Datasets/KoreanDataset_1.1.csv", index=False)