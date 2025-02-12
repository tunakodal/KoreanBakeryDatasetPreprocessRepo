import pandas as pd

# Dataset'i oku
df = pd.read_csv("../Datasets/KoreanDataset_2.1.csv")  # Kendi dosyanın adını buraya yaz

# Benzersiz değerler için bir mapping oluştur
place_mapping = {}
counter = 1


# Place sütunundaki her değeri kontrol et ve sayısal değer ata
def map_place(place):
    global counter
    if place not in place_mapping:
        place_mapping[place] = counter
        counter += 1
    return place_mapping[place]


df["Place"] = df["Place"].apply(map_place)

# Güncellenmiş dataset'i kaydet
df.to_csv("../Datasets/KoreanDataset_2.2.csv", index=False)

print("Place sütunu sayısal değerlere çevrildi ve dosyaya kaydedildi.")
