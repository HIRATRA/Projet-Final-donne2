import os
import requests
import json
from datetime import datetime, timezone
from dotenv import load_dotenv

# Charger les variables d’environnement
load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
CITY_NAME = os.getenv("CITY_NAME", "Antananarivo")

# URL de l’API OpenWeather
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}&units=metric"

def fetch_weather():
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()

        # Extraire les données importantes
        extracted = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "city": data.get("name"),
            "temperature": data["main"].get("temp"),
            "humidity": data["main"].get("humidity"),
            "wind_speed": data["wind"].get("speed"),
            "weather": data["weather"][0].get("description"),
            "rain": data.get("rain", {}).get("1h", 0.0)  # pluie sur 1h en mm
        }

        # Créer le dossier de sortie si besoin
        output_dir = os.path.join("data", "raw")
        os.makedirs(output_dir, exist_ok=True)

        # Nom de fichier basé sur la date
        date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        file_path = os.path.join(output_dir, f"{date_str}.json")

        # Enregistrer en JSON
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(extracted, f, indent=4)

        print(f"[OK] Données enregistrées dans {file_path}")
    else:
        print(f"[ERREUR] API OpenWeather : {response.status_code} - {response.text}")

if __name__ == "__main__":
    fetch_weather()
