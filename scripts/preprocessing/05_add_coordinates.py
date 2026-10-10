import pandas as pd
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

# CSV dosyanı oku
df = pd.read_csv("../../data/processed/KoreanDataset_1.4.csv")

# Nominatim Geocoder
geolocator = Nominatim(user_agent="your_app_name")

# RateLimiter ile API çağrılarını hızlandır
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

# Önce benzersiz "Place" değerleri için koordinatları çekelim
unique_places = df["Place"].dropna().unique()

# Dictionary ile daha önce bulunan koordinatları sakla (cache mekanizması)
coordinates_dict = {}

for place in unique_places:
    location = geocode(place)
    if location:
        coordinates_dict[place] = (location.latitude, location.longitude)
    else:
        coordinates_dict[place] = (None, None)

# Şimdi tüm satırlara koordinatları ekleyelim
df["Latitude"] = df["Place"].map(lambda x: coordinates_dict.get(x, (None, None))[0])
df["Longitude"] = df["Place"].map(lambda x: coordinates_dict.get(x, (None, None))[1])

# Yeni dataset'i kaydet
df.to_csv("../../data/processed/KoreanDataset_1.5.0.csv", index=False)

print("Koordinatlar hızlandırılmış şekilde eklendi! 🚀")
