import pandas as pd

# CSV dosyasını oku
df = pd.read_csv("../Datasets/KoreanDataset_1.2.csv")  # Kendi dosya adını buraya yaz

# Gruplama yapılacak kolonlar
group_cols = ["Date", "Place"]

# Toplanacak kolonlar
sum_cols = [
    "Angbutter", "Plain bread", "Jam", "Americano", "Croissant", "Caffe latte",
    "Tiramisu croissant", "Cacao deep", "Pain au chocolat", "Almond croissant",
    "Croque monsieur", "Mad garlic", "Milk tea", "Gateau chocolat", "Pandoro",
    "Cheese cake", "Lemon ade", "Orange pound", "Wiener", "Vanila latte",
    "Berry ade", "Tiramisu", "Merinque cookies"
]

# DataFrame'de eksik kolonları kontrol et ve sadece var olanları al
sum_cols = [col for col in sum_cols if col in df.columns]

# Date ve Place'e göre gruplama yap, belirttiğin kolonları topla
df_grouped = df.groupby(group_cols, as_index=False)[sum_cols].sum()

# Yeni CSV dosyasını kaydet
df_grouped.to_csv("../Datasets/KoreanDataset_1.3.csv", index=False)