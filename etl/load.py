import os
import pandas as pd

def load_weather_data():
    processed_dir = os.path.join("data", "processed")
    merged_dir = os.path.join("data", "merged")
    os.makedirs(merged_dir, exist_ok=True)

    # Trouver tous les fichiers CSV
    csv_files = sorted([
        f for f in os.listdir(processed_dir) if f.endswith(".csv")
    ])

    if not csv_files:
        print("[ERREUR] Aucun fichier transformé trouvé dans data/processed/")
        return

    # Charger et concaténer tous les CSV
    all_dfs = []
    for file in csv_files:
        df = pd.read_csv(os.path.join(processed_dir, file), parse_dates=["timestamp"])
        all_dfs.append(df)

    merged_df = pd.concat(all_dfs, ignore_index=True)

    # Supprimer les doublons éventuels
    merged_df.drop_duplicates(subset=["timestamp", "city"], inplace=True)

    # Enregistrer dans data/merged
    merged_path = os.path.join(merged_dir, "weather_data.csv")
    merged_df.to_csv(merged_path, index=False, encoding="utf-8")

    print(f"[OK] Données fusionnées enregistrées dans {merged_path}")

if __name__ == "__main__":
    load_weather_data()
