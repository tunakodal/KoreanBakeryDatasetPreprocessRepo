import pandas as pd

# Datasetleri yükleme
dataset1 = pd.read_csv("../../data/processed/KoreanDataset_1.7.csv")
dataset2 = pd.read_csv("../../data/processed/KoreanDataset_1.8.csv")

# Dataset1'de BrentPrice, WTIPrice, AveragePrice sütunlarını kontrol et
dataset1 = dataset1[['Date', 'BrentPrice', 'WTIPrice', 'AveragePrice']].drop_duplicates()

# Date sütunlarına göre birleştirme
dataset2 = dataset2.merge(dataset1, on='Date', how='left')

# Sonuçları kaydetme
dataset2.to_csv("../../data/processed/KoreanDataset_1.9.csv", index=False)
