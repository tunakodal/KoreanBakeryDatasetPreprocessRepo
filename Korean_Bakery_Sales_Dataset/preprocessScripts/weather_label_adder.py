import requests
import csv

# OpenWeatherMap API Key
#api key yedek : REMOVED
api_key = 'REMOVED'
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# CSV dosyasının yolu
input_file = '/Users/ebrarsudedogan/PycharmProjects/KoreanBakeryDatasetPreprocessRepo/Korean_Bakery_Sales_Dataset/Datasets/KoreanDataset_2.0.csv'
output_file = '/Users/ebrarsudedogan/PycharmProjects/KoreanBakeryDatasetPreprocessRepo/Korean_Bakery_Sales_Dataset/Datasets/KoreanDataset_3.0.csv'

# Hava durumu etiketleri
weather_labels = {
    "Clear": 1,  # Sunny
    "Clouds": 2,  # Cloudy
    "Rain": 3,  # Rainy
    "Thunderstorm": 4,  # Thunderstorm
    "Snow": 5,  # Snow
    "Wind": 6,  # Windy
    "Fog": 7,  # Foggy
    "Drizzle": 8  # Drizzle
}


def get_weather_by_coords(latitude, longitude):
    complete_url = f"{base_url}lat={latitude}&lon={longitude}&appid={api_key}"
    response = requests.get(complete_url)

    # Yanıtı yazdırarak inceleme
    print(f"Request URL: {complete_url}")
    print(f"Response Status Code: {response.status_code}")
    data = response.json()
    print(f"API Response: {data}")

    if data["cod"] == 200:
        weather_condition = data["weather"][0]["main"]
        return weather_labels.get(weather_condition, None)  # None if not found
    else:
        print(f"Error: {data.get('message', 'Unknown error')}")
        return None


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

        # Hava durumu etiketini koordinatlarla çekme
        weather_label = get_weather_by_coords(latitude, longitude)

        if weather_label is not None:
            row.append(weather_label)  # Yeni etiketi son sütuna ekle
            print(f"City: {city_name}, Weather Label: {weather_label}")  # Ekrana yazdır
            writer.writerow(row)  # Veriyi yazma
        else:
            print(f"City: {city_name}, Weather Label: N/A")  # Hava durumu bulunmazsa N/A yazdır

print(f"Weather labels have been added to {output_file}")
