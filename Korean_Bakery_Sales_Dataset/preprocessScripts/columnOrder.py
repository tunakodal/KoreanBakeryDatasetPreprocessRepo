import pandas as pd

# Dosyayı oku
df = pd.read_csv("../Datasets/KoreanDataset_1.5.0.csv")

# Mevcut sütunları listele
columns = df.columns.tolist()

# Sütunları manuel olarak yeniden düzenle
new_order = columns.copy()  # Orijinal sütunları kopyala

# Önce Longitude ve Latitude'u çıkartalım
new_order.remove("Longitude")
new_order.remove("Latitude")

# Place sütununun olduğu konumu bul
place_index = new_order.index("Place")

# Longitude ve Latitude'u Place'ten sonraya ekleyelim
new_order = new_order[: place_index + 1] + ["Latitude", "Longitude"] + new_order[place_index + 1:]

# Yeni sıralamayı uygula
df = df[new_order]

# Güncellenmiş CSV dosyasını kaydet
df.to_csv("../Datasets/KoreanDataset_1.5.1.csv", index=False)
