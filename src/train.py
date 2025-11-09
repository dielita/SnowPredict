import argparse
import pandas as pd
import json
from pathlib import Path
import random

def train(data_path, model_path, lr, batch_size, model_name):
    # Чтение данных
    df = pd.read_csv(data_path)

    # Псевдо-обучение: создаём случайную метрику
    score = random.uniform(0.7, 0.95)
    metrics = {
        "accuracy": round(score, 3),
        "lr": lr,
        "batch_size": batch_size
    }

    # Сохраняем модель (фейковые данные)
    Path(model_path).parent.mkdir(parents=True, exist_ok=True)
    Path(model_path).write_text("fake model data")

    # Сохраняем метрики под имя, ожидаемое DVC
    metrics_path = Path("metrics") / f"{model_name}_{Path(model_path).stem}.json"
    metrics_path.parent.mkdir(exist_ok=True)
    with open(metrics_path, "w") as f:
        json.dump(metrics, f, indent=4)

    print(f"Trained model saved to {model_path}")
    print(f"Metrics saved to {metrics_path}")
    print(f"Metrics content: {metrics}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", required=True)
    parser.add_argument("--model", required=True)
    parser.add_argument("--lr", type=float, default=0.001)
    parser.add_argument("--batch_size", type=int, default=32)
    parser.add_argument("--model_name", required=True)
    args = parser.parse_args()
    train(args.data, args.model, args.lr, args.batch_size, args.model_name)