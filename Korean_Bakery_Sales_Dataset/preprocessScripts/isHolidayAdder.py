import pandas as pd

# Verilen tatil tarihlerinin listesi (MM DD formatında)
holidays = [
    "01 01", "02 07", "02 08", "02 09", "02 10", "03 01", "05 01", "05 05", "05 14", "06 06", "09 10", "12 25"
]

# CSV dosyasını oku
df = pd.read_csv("../Datasets/KoreanDataset_4.0.csv")

# Date kolonundan "MM DD" değerini çıkart
df['MM DD'] = df['Date'].astype(str).apply(lambda x: x[5:])  # YYYY-MM-DD → MM-DD alır
df['MM DD'] = df['MM DD'].str.replace("-", " ")  # "MM-DD" → "MM DD" dönüşümü

# Tatil olup olmadığını kontrol eden sütunu ekle
df['isHoliday'] = df['MM DD'].apply(lambda x: 1 if x in holidays else 0)

# Geçici "MM DD" kolonunu kaldır
df.drop(columns=['MM DD'], inplace=True)

# 'isHoliday' sütununu belirli bir sıraya yerleştirme
cols = df.columns.tolist()
if 'pres' in cols:
    pres_index = cols.index('pres')  # 'pres' kolonunun indeksini al
    cols.insert(pres_index + 1, cols.pop(cols.index('isHoliday')))  # 'pres' kolonundan sonra ekle
    df = df[cols]  # Kolon sırasını güncelle

# Güncellenmiş dosyayı kaydet
df.to_csv("../Datasets/KoreanDataset_5.0.csv", index=False)

print("İşlem tamamlandı: 'isHoliday' sütunu eklendi ve dosya kaydedildi.")
