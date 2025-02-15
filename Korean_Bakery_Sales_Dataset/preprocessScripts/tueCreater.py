import pandas as pd


def add_tuesday_rows(df):
    # Günleri sayılarla eşleştiren bir liste
    relevant_days = [7, 1, 3, 4]  # Ortalaması alınacak günler: Sunday, Monday, Wednesday, Thursday
    avg_columns = [
        "Latitude", "Longitude", "AveragePrice", "WTIPrice", "BrentPrice",
        "tmin", "tmax", "tavg", "wspd", "pres", "isHoliday",
        "Latte Varieties", "Sweets and Cakes", "Croissant Varieties",
        "Fruity and Refreshing Drinks", "Snacks", "Classic Breads and Toasts"
    ]

    # Tarih sütununu datetime formatına çevir
    df['Date'] = pd.to_datetime(df['Date'])

    # Yeni 'Tuesday' satırlarını saklamak için liste
    new_rows = []

    # Haftalık gruplama (aynı haftada olan günleri gruplayarak işlem yapacağız)
    df['Week'] = df.groupby('Date').ngroup()

    for week, group in df.groupby('Week'):
        # Yalnızca ilgili günleri içeren alt küme
        relevant_group = group[group['Day'].isin(relevant_days)]

        # Eğer ilgili günlerden en az biri varsa 'Tuesday' ekle
        if not relevant_group.empty:
            # Ortalama değerleri hesapla
            avg_values = relevant_group[avg_columns].mean()

            # Pazartesi gününün tarihini al ve +1 gün ekleyerek 'Tuesday' tarihini oluştur
            monday_row = relevant_group[relevant_group['Day'] == 1]
            if not monday_row.empty:
                tuesday_date = monday_row.iloc[0]['Date'] + pd.Timedelta(days=1)
            else:
                continue  # Eğer Pazartesi yoksa 'Tuesday' eklenmez

            # Yeni 'Tuesday' satırı oluştur
            new_row = avg_values.to_dict()
            new_row['Day'] = 2  # 'Tuesday' olarak işaretle
            new_row['Date'] = tuesday_date
            new_row['Place'] = relevant_group['Place'].mode()[0]  # En sık geçen 'Place'

            # Yeni satırı ekle
            new_rows.append(new_row)

    # Yeni 'Tuesday' satırlarını DataFrame'e ekle
    tuesday_df = pd.DataFrame(new_rows)
    df = pd.concat([df, tuesday_df], ignore_index=True)

    # 'Week' sütununu kaldır
    df.drop(columns=['Week'], inplace=True)

    # Tarihe ve güne göre sıralama yaparak doğal düzeni koru
    df.sort_values(by=['Date', 'Day'], inplace=True)

    # Yeni indeks oluştur
    df.reset_index(drop=True, inplace=True)

    return df


# Örnek kullanım
file_path = "../Datasets/KoreanDataset_3.0.csv"  # Dosyanın adını kendi dosyanla değiştir
df = pd.read_csv(file_path)

df_updated = add_tuesday_rows(df)
df_updated.to_csv("../Datasets/KoreanDataset_4.0.csv", index=False)
