import pandas as pd

# Dosya adını belirle
input_file = "../../data/processed/KoreanDataset_2.3.csv"
output_file = "../../data/processed/KoreanDataset_2.4.csv"

# CSV dosyasını oku
df = pd.read_csv(input_file)

# Latitude değeri 37.20'den küçük olan satırları sil
df_filtered = df[df["Latitude"] >= 36.20]

# Yeni CSV dosyasını kaydet
df_filtered.to_csv(output_file, index=False)

print(f"İşlem tamamlandı! Yeni dosya: {output_file}")
