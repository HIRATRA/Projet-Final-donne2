import os
import pandas as pd

def generate_star_schema():
    merged_path = os.path.join("data", "merged", "weather_data.csv")
    output_dir = os.path.join("data", "star_schema")
    os.makedirs(output_dir, exist_ok=True)

    # Charger les données fusionnées
    df = pd.read_csv(merged_path, parse_dates=["timestamp"])

    # --- Dimension Temps ---
    df["date"] = df["timestamp"].dt.date
    dim_time = df[["date"]].drop_duplicates().copy()
    dim_time["time_id"] = dim_time["date"].astype(str)
    dim_time["day"] = pd.to_datetime(dim_time["date"]).dt.day
    dim_time["month"] = pd.to_datetime(dim_time["date"]).dt.month
    dim_time["year"] = pd.to_datetime(dim_time["date"]).dt.year
    dim_time["weekday"] = pd.to_datetime(dim_time["date"]).dt.day_name()

    # --- Dimension Ville ---
    dim_city = df[["city"]].drop_duplicates().copy()
    dim_city["city_id"] = dim_city["city"].str.lower().str.replace(" ", "_")

    # --- Dimension Condition météo ---
    dim_condition = df[["weather"]].drop_duplicates().copy()
    dim_condition["condition_id"] = dim_condition["weather"].str.lower().str.replace(" ", "_")

    # --- Table de faits ---
    fact_weather = df.copy()
    fact_weather["time_id"] = fact_weather["date"].astype(str)
    fact_weather["city_id"] = fact_weather["city"].str.lower().str.replace(" ", "_")
    fact_weather["condition_id"] = fact_weather["weather"].str.lower().str.replace(" ", "_")

    fact_weather = fact_weather[[
        "timestamp", "time_id", "city_id", "condition_id",
        "temperature", "humidity", "wind_speed", "rain"
    ]]

    # Enregistrer les fichiers
    dim_time.to_csv(os.path.join(output_dir, "dim_time.csv"), index=False)
    dim_city.to_csv(os.path.join(output_dir, "dim_city.csv"), index=False)
    dim_condition.to_csv(os.path.join(output_dir, "dim_condition.csv"), index=False)
    fact_weather.to_csv(os.path.join(output_dir, "fact_weather.csv"), index=False)

    print(f"[OK] Modèle en étoile généré dans {output_dir}")

if __name__ == "__main__":
    generate_star_schema()
