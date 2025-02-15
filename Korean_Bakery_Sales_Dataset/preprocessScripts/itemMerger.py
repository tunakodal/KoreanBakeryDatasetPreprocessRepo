import pandas as pd

# Dosya yolları
input_file = "../Datasets/KoreanDataset_2.4.csv"
output_file = "../Datasets/KoreanDataset_3.0.csv"

# CSV dosyasını oku
df = pd.read_csv(input_file)

# İngilizce'ye çevrilen kolon isimleri ve gruplama yapısı
column_mapping = {
    "Plain bread": "Classic Breads and Toasts",
    "Croque monsieur": "Classic Breads and Toasts",
    "Mad garlic": "Classic Breads and Toasts",

    "Croissant": "Croissant Varieties",
    "Tiramisu croissant": "Croissant Varieties",
    "Pain au chocolat": "Croissant Varieties",
    "Almond croissant": "Croissant Varieties",

    "Tiramisu": "Sweets and Cakes",
    "Cheese cake": "Sweets and Cakes",
    "Gateau chocolat": "Sweets and Cakes",
    "Pandoro": "Sweets and Cakes",
    "Orange pgound": "Sweets and Cakes",

    "Americano": "Americano",  # Americano'yu ayrı kategori yapıyoruz
    "Caffe latte": "Latte Varieties",
    "Vanila latte": "Latte Varieties",

    "Lemon ade": "Fruity and Refreshing Drinks",
    "Berry ade": "Fruity and Refreshing Drinks",

    "Merinque cookies": "Snacks",
    "Angbutter": "Snacks",
    "Wiener": "Snacks"
}

# Yeni kategorileri içeren DataFrame oluştur
df_grouped = df.copy()

# Yeni kategorileri ekleyerek kolonları gruplama
for new_col in set(column_mapping.values()):
    df_grouped[new_col] = 0

# Verileri gruplara göre toplama
for old_col, new_col in column_mapping.items():
    df_grouped[new_col] += df_grouped[old_col]
    df_grouped.drop(columns=[old_col], inplace=True)  # Eski kolonları kaldır

# "Cacao deep", "Milk tea" ve "Jam" kolonlarını sil
columns_to_remove = ["Cacao deep", "Milk tea", "Jam"]
df_grouped.drop(columns=[col for col in columns_to_remove if col in df_grouped.columns], inplace=True)

# Yeni CSV dosyasını kaydet
df_grouped.to_csv(output_file, index=False)

print(f"İşlem tamamlandı! Yeni dosya kaydedildi: {output_file}")
