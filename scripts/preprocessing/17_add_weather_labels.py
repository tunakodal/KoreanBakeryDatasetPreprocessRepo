import requests
import csv

# CSV dosyasının yolu
input_file = '../../data/processed/KoreanDataset_2.3.csv'
output_file = '../../data/processed/KoreanDataset_2.4.csv'

# Hava durumu etiketleri
weather_labels = {
    "clear": "Sunny",
    "partly-cloudy": "Cloudy",
    "mostly-cloudy": "Cloudy",
    "overcast": "Cloudy",
    "rain": "Rainy",
    "showers": "Rainy",
    "drizzle": "Drizzle",
    "snow": "Snowy",
    "thunderstorms": "Thunderstorm",
    "fog": "Foggy",
    "mist": "Foggy",
    "haze": "Foggy",
    "wind": "Windy"
}


# Visual Crossing Weather API URL (Ücretsiz, API anahtarı gerekmez!)
def get_historical_weather(latitude, longitude, date):
    base_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
    api_key = "REMOVED"  # Ücretsiz bir API anahtarı oluşturmanız gerekebilir

    # API isteği için URL oluştur
    complete_url = f"{base_url}{latitude},{longitude}/{date}?unitGroup=metric&include=days&key={api_key}&contentType=json"

    response = requests.get(complete_url)

    if response.status_code != 200:
        print(f"API Error ({response.status_code}): {response.text}")
        return "N/A"

    data = response.json()

    # API yanıtını yazdır (Hata tespiti için)
    print(f"API Response for {date} at {latitude}, {longitude}: {data}")

    # Günlük hava durumunu kontrol et
    if "days" in data and len(data["days"]) > 0:
        conditions = data["days"][0]["conditions"].lower()
        for key in weather_labels:
            if key in conditions:
                return weather_labels[key]

    return "Unknown"


# CSV dosyasını okuma ve yazma
with open(input_file, mode='r', encoding='utf-8') as infile, open(output_file, mode='w', newline='',
                                                                  encoding='utf-8') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Başlık satırını yazma
    header = next(reader)
    header.append('Weather Label')  # Yeni sütun başlığını ekliyoruz
    writer.writerow(header)

    # Verileri işleyip ekleme
    for row in reader:
        city_name = row[2]  # Şehir adı 2. sütunda
        latitude = float(row[3])  # Latitude 3. sütunda
        longitude = float(row[4])  # Longitude 4. sütunda
        date = row[0]  # Date sütunu 0. sütunda

        # Visual Crossing API ile tarihsel hava durumu çekme
        weather_label = get_historical_weather(latitude, longitude, date)

        row.append(weather_label)  # Yeni etiketi son sütuna ekle
        print(f"City: {city_name}, Date: {date}, Weather: {weather_label}")  # Ekrana yazdır
        writer.writerow(row)  # Veriyi yazma

print(f"Weather labels have been added to {output_file}")
