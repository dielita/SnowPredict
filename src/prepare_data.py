import argparse
import pandas as pd
from pathlib import Path
import sys

def prepare(region, param_set):
    raw_path = Path(f"data/raw/{region}/data.csv")
    
    if not raw_path.exists():
        print(f"Error: file {raw_path} does not exist!")
        sys.exit(1)

    # Чтение CSV с авто-удалением BOM
    try:
        df = pd.read_csv(raw_path, encoding='utf-8-sig')
    except UnicodeDecodeError:
        print("Failed to read CSV. Try opening it in Excel and saving as UTF-8.")
        sys.exit(1)

    # Убираем пробелы и BOM из заголовков
    df.columns = df.columns.str.strip()
    print("Columns in CSV:", df.columns.tolist())  # Проверяем колонки

    # Проверяем, есть ли нужные столбцы для выбранного набора параметров
    required_cols = []
    if param_set == "temp_snow":
        required_cols = ["temp", "snow_depth"]
    elif param_set == "wind_temp":
        required_cols = ["temp", "wind"]
    elif param_set == "wind_snow":
        required_cols = ["wind", "snow"]
    elif param_set == "wind_temp_snow":
        required_cols = ["temp", "wind","snow_depth"]
    else:
        print(f"Unknown param_set: {param_set}")
        sys.exit(1)

    for col in required_cols:
        if col not in df.columns:
            print(f"Error: required column '{col}' not found in CSV!")
            sys.exit(1)

    # Выбираем только нужные столбцы
    df = df[required_cols]

    # Сохраняем обработанный CSV
    out_path = Path(f"data/processed/{region}_{param_set}.csv")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out_path, index=False)
    print(f"Processed {region} with {param_set} → {out_path}")
    print(df.head())  # Показываем первые строки для проверки

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--region", required=True)
    parser.add_argument("--param_set", required=True)
    args = parser.parse_args()
    prepare(args.region, args.param_set)