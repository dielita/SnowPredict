import argparse, json, random
from pathlib import Path
import pandas as pd

def train(data_path, model_path, lr, batch_size):
    df = pd.read_csv(data_path)
    score = random.uniform(0.7, 0.95)  # псевдо-метрика
    metrics = {"accuracy": round(score, 3), "lr": lr, "batch_size": batch_size}

    Path(model_path).parent.mkdir(parents=True, exist_ok=True)
    Path(model_path).write_text("fake model data")

    metrics_path = f"metrics/{Path(model_path).stem}.json"
    Path(metrics_path).parent.mkdir(exist_ok=True)
    with open(metrics_path, "w") as f:
        json.dump(metrics, f, indent=4)

    print(f"Trained model saved to {model_path}")
    print(f"Metrics: {metrics}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", required=True)
    parser.add_argument("--model", required=True)
    parser.add_argument("--lr", type=float, default=0.001)
    parser.add_argument("--batch_size", type=int, default=32)
    args = parser.parse_args()
    train(args.data, args.model, args.lr, args.batch_size)