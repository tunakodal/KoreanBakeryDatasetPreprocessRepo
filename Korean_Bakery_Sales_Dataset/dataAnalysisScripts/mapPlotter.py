import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# CSV dosyanı oku
df = pd.read_csv("../Datasets/KoreanDataset_2.0.csv")

# Harita oluştur
plt.figure(figsize=(10, 8))
m = Basemap(projection='merc',
            llcrnrlat=33, urcrnrlat=39,  # Güney Kore'nin enlem sınırları
            llcrnrlon=124, urcrnrlon=132,  # Güney Kore'nin boylam sınırları
            resolution='i')

m.drawcoastlines()
m.drawcountries()
m.drawmapboundary(fill_color='aqua')
m.fillcontinents(color='lightgray', lake_color='aqua')

# Noktaları haritaya ekleyelim
for idx, row in df.iterrows():
    x, y = m(row["Longitude"], row["Latitude"])  # Koordinatları haritaya dönüştür
    m.plot(x, y, marker='o', markersize=5, color='red', alpha=0.7)

plt.title("Güney Kore'deki Şehirlerde Bulunan Noktalar")
plt.show()
