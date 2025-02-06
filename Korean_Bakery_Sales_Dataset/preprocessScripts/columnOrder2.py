import pandas as pd

# CSV dosyanı oku
df = pd.read_csv("../Datasets/KoreanDataset_1.6.0.csv")

# Kolonları yeniden sırala
columns = list(df.columns)
insert_cols = ["tmax", "tmin", "tavg", "wspd", "pres"]

# Longitude ve Angbutter kolonlarının yerini bul
longitude_idx = columns.index("Longitude")
angbutter_idx = columns.index("Angbutter")

# Mevcut veriyi koruyarak yeni sıralamaya uygun hale getir
moved_cols = df[insert_cols]  # Taşınacak kolonları kaydet
df = df.drop(columns=insert_cols)  # Eski yerlerinde olanları sil

# Yeni kolon sıralamasını oluştur
columns = list(df.columns)  # Güncellenmiş kolon listesini al
longitude_idx = columns.index("Longitude")  # Longitude’un yeni indeksini al
new_order = columns[:longitude_idx + 1] + insert_cols + columns[longitude_idx + 1:]

# Yeni kolon sıralamasıyla DataFrame’i oluştur
df = pd.concat([df.iloc[:, :longitude_idx + 1], moved_cols, df.iloc[:, longitude_idx + 1:]], axis=1)

# Yeni dosyayı kaydet
df.to_csv("../Datasets/KoreanDataset_1.6.1.csv", index=False)

print("Kolonlar başarıyla taşındı ve tekrar edenler silindi.")
