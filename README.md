# Korean Bakery Sales – Dataset Preprocessing

Preprocessing pipeline that turns a raw Korean bakery sales log (`bakery_sales.csv`) into a clean, daily, per-location dataset enriched with weather, oil price, and holiday information. It is meant for sales / demand forecasting.

**Final dataset:** `data/processed/KoreanDataset_5.1.csv`

## Structure

```
data/
  raw/                  original sales data
  processed/            every intermediate version (KoreanDataset_<version>.csv)
scripts/
  preprocessing/        numbered pipeline steps (01 → 20)
  analysis/             exploration and plotting helpers
logs/                   outputs of cleaning / analysis steps
```

## Pipeline overview

Each script in `scripts/preprocessing/` reads one dataset version and writes the next, so running them in numeric order reproduces the dataset:

1. **Cleaning** – fix missing datetimes, drop unused columns, aggregate transactions to daily totals
2. **Enrichment** – add coordinates, weather (temperature, wind, pressure), oil prices, holiday flag
3. **Encoding & merging** – encode day/place, merge individual products into item categories
4. **Final fixes** – correct Tuesday rows, handle remaining NaN rows

Run scripts from inside their own folder (paths are relative), e.g.:

```bash
cd scripts/preprocessing
python 01_clean_datetime.py
```

## Final dataset columns

`Date, Day, Place, Latitude, Longitude, AveragePrice, WTIPrice, BrentPrice, tmax, tmin, tavg, wspd, pres, isHoliday` plus daily sales counts per item category (Americano, Classic Breads and Toasts, Croissant Varieties, Fruity and Refreshing Drinks, Snacks, Latte Varieties, Sweets and Cakes).

## Requirements

Python 3 with `pandas`, `matplotlib`, `geopy` (coordinates) and `meteostat` (weather).

## Notes

Some versions (e.g. 1.7, 5.1) were edited by hand and have no script. Script comments and console messages are partly in Turkish.
