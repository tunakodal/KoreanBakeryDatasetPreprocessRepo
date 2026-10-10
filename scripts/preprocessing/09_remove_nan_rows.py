import pandas as pd

# Dosya yolları
csv_file_path = "../../data/processed/KoreanDataset_1.6.1.csv"
log_file_path = "../../logs/removed_nan_rows.txt"
output_csv_path = "../../data/processed/KoreanDataset_1.6.2.csv"

# CSV dosyasını oku
try:
    df = pd.read_csv(csv_file_path)

    # NaN içeren satırları tespit et
    nan_rows = df[df.isna().any(axis=1)]

    # Eğer NaN içeren satırlar varsa, bunları log dosyasına kaydet
    if not nan_rows.empty:
        nan_rows.to_csv(log_file_path, index=False, sep="\t")

    # NaN içeren satırları sil
    df_cleaned = df.dropna()

    # Temizlenmiş CSV'yi kaydet
    df_cleaned.to_csv(output_csv_path, index=False)

    print(f"İşlem tamamlandı! Temizlenen veri '{output_csv_path}' olarak kaydedildi.")
    print(f"Silinen satırlar '{log_file_path}' dosyasına eklendi.")

except FileNotFoundError:
    print(f"Hata: '{csv_file_path}' dosyası bulunamadı. Lütfen dosya yolunu kontrol edin.")
