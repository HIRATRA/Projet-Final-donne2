import os
import json
import pandas as pd
from datetime import datetime, timezone

def transform_weather_data():
    raw_dir = os.path.join("data", "raw")
    processed_dir = os.path.join("data", "processed")
    os.makedirs(processed_dir, exist_ok=True)

    # Trouver le dernier fichier .json
    raw_files = sorted([
        f for f in os.listdir(raw_dir) if f.endswith(".json")
    ], reverse=True)

    if not raw_files:
        print("[ERREUR] Aucun fichier JSON trouvé dans data/raw/")
        return

    latest_file = raw_files[0]
    file_path = os.path.join(raw_dir, latest_file)

    # Charger le fichier JSON
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Convertir en DataFrame
    df = pd.DataFrame([data])

    # Nettoyage / transformation
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["city"] = df["city"].str.title().str.strip()
    df["temperature"] = pd.to_numeric(df["temperature"], errors="coerce")
    df["humidity"] = pd.to_numeric(df["humidity"], errors="coerce")
    df["wind_speed"] = pd.to_numeric(df["wind_speed"], errors="coerce")
    df["rain"] = pd.to_numeric(df["rain"], errors="coerce")
    df["weather"] = df["weather"].str.strip().str.lower()

    # Gérer les valeurs manquantes : ex. remplacer NaN pluie par 0
    df["rain"].fillna(0.0, inplace=True)

    # Enregistrer au format CSV
    date_str = df["timestamp"].dt.strftime("%Y-%m-%d").iloc[0]
    output_file = os.path.join(processed_dir, f"{date_str}.csv")
    df.to_csv(output_file, index=False, encoding="utf-8")

    print(f"[OK] Données transformées et sauvegardées dans {output_file}")

if __name__ == "__main__":
    transform_weather_data()
