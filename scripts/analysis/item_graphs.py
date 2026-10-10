# Gerekli kütüphaneleri içe aktarma
import pandas as pd
import matplotlib.pyplot as plt

# CSV dosyanı oku (Dosya adını değiştir)
file_path = "../../data/processed/KoreanDataset_5.0.csv"  # Gerçek dosya adını buraya yaz
df = pd.read_csv(file_path)

# Tarih sütununun adını kontrol et ve datetime formatına çevir
date_column = "Date"  # Eğer farklı bir sütun adı varsa güncelle
df[date_column] = pd.to_datetime(df[date_column])

# Ürün sütunlarını belirleme
product_columns = [
    'Latte Varieties', 'Sweets and Cakes', 'Croissant Varieties',
    'Fruity and Refreshing Drinks', 'Snacks', 'Classic Breads and Toasts', 'Americano'
]

# Her ürün için ayrı bir pencerede grafik oluşturma
for column in product_columns:
    plt.figure(figsize=(10, 5))  # Her grafik için ayrı pencere boyutu
    plt.plot(df[date_column], df[column], marker='o', linestyle='-')
    plt.title(f"Time Series of {column}", fontsize=14)
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Sales Count", fontsize=12)
    plt.xticks(rotation=45)
    plt.grid()
    plt.show()  # Her grafiği farklı bir sekmede açar
