import pandas as pd

# Datasetleri yükleme
dataset2 = pd.read_csv("../Datasets/KoreanDataset_1.9.csv")

# Dataset2'deki kolonları sadece kaydırarak BrentPrice, WTIPrice, AveragePrice'ı Longitude ve tmax arasına taşıma
cols = dataset2.columns.tolist()
longitude_index = cols.index('Longitude')
tmax_index = cols.index('tmax')

# İlgili kolonları çıkartıp tmax öncesine ekleme
moving_cols = ['BrentPrice', 'WTIPrice', 'AveragePrice']
for col in moving_cols:
    cols.remove(col)
    cols.insert(tmax_index, col)

dataset2 = dataset2[cols]

# Sonuçları kaydetme
dataset2.to_csv("../Datasets/KoreanDataset_2.0.cs", index=False)
