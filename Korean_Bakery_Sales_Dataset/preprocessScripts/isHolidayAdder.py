import pandas as pd

# Verilen tatil tarihlerinin listesi
holidays = [
    "01 01", "02 07", "02 08", "02 09", "02 10", "03 01", "05 01", "05 05", "05 14", "06 06", "09 10", "12 25"
]

# CSV dosyasını yükle (dosya adını güncelle)
df = pd.read_csv("../Datasets/KoreanDataset_1.6.2.csv")

# Date kolonu YY MM DD formatında olduğu varsayılıyor, sadece MM DD kısmını alıyoruz
df['MM DD'] = df['Date'].apply(lambda x: ' '.join(x.split()[1:]))

# Tatil olup olmadığını kontrol eden kolon ekle
df['isHoliday'] = df['MM DD'].apply(lambda x: 1 if x in holidays else 0)

# Geçici MM DD kolonunu kaldır
df.drop(columns=['MM DD'], inplace=True)

# isHoliday kolonunu 'pres' ve 'Angbutter' arasına ekleme
cols = df.columns.tolist()
pres_index = cols.index('pres')
cols.insert(pres_index + 1, cols.pop(cols.index('isHoliday')))
df = df[cols]

# Sonuç dosyasını kaydet
df.to_csv("../Datasets/KoreanDataset_1.7.csv", index=False)

print("İşlem tamamlandı")
