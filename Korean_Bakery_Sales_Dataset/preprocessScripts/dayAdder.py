import pandas as pd

# Datasetleri yükleme
dataset1 = pd.read_csv("../Datasets/KoreanDataset_1.2.csv")
dataset2 = pd.read_csv("../Datasets/KoreanDataset_1.7.csv")

# Dataset1'de Day of Week sütununun ismini kontrol et
day_col_name = "Day of week" if "Day of week" in dataset1.columns else "day_of_week"

# Date sütunlarına göre birleştirme ve duplicate kayıtları önleme
dataset1 = dataset1[['Date', day_col_name]].drop_duplicates()
dataset2 = dataset2.merge(dataset1, on='Date', how='left')

# Yeni eklenen kolonu 'Day' olarak yeniden adlandırma
dataset2.rename(columns={day_col_name: 'Day'}, inplace=True)

# Day kolonunu Date ve Place arasına ekleme
cols = dataset2.columns.tolist()
date_index = cols.index('Date')
cols.insert(date_index + 1, cols.pop(cols.index('Day')))
dataset2 = dataset2[cols]

# Sonuçları kaydetme
dataset2.to_csv("../Datasets/KoreanDataset_1.8.csv", index=False)

print("İşlem tamamlandı. Güncellenmiş dosya 'updated_dataset2.csv' olarak kaydedildi.")
