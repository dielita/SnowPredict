import argparse
import pandas as pd
from pathlib import Path

def prepare(region, param_set):
    raw_path = Path(f"data/raw/{region}/data.csv")
    df = pd.read_csv(raw_path)

    if param_set == "snow_temp":
        df = df[["temp", "snow_depth"]]
    elif param_set == "wind_temp":
        df = df[["temp", "wind"]]

    out_path = Path(f"data/processed/{region}_{param_set}.csv")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out_path, index=False)
    print(f"Processed {region} with {param_set} → {out_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--region", required=True)
    parser.add_argument("--param_set", required=True)
    args = parser.parse_args()
    prepare(args.region, args.param_set)