
#  Modélisation des données – Schéma en étoile

Ce document décrit la modélisation des données utilisée dans le cadre du projet météo-tourisme. Le choix d'un **schéma en étoile (star schema)** a été fait pour structurer les données de manière claire, évolutive et orientée analyse.

---

##  Objectif du modèle

Permettre l’analyse météo selon plusieurs axes (ville, mois, saison, condition météo) afin de répondre à la problématique :
> **Quand voyager ? Quelles sont les meilleures périodes pour visiter une ville selon les conditions météo ?**

---

##  Table de faits : `mesures_meteo`

Cette table contient les données quantitatives mesurées chaque jour pour chaque ville.

| Champ         | Type     | Description                                 |
|---------------|----------|---------------------------------------------|
| id            | int (PK) | Identifiant unique                          |
| date_id       | int (FK) | Référence vers la date                      |
| ville_id      | int (FK) | Référence vers la ville                     |
| condition_id  | int (FK) | Référence vers la condition météo           |
| temperature   | float    | Température quotidienne moyenne (°C)        |
| humidite      | float    | Humidité (%)                                |
| vent          | float    | Vitesse du vent (km/h)                      |
| pluie         | float    | Précipitation (mm)                          |
| score_meteo   | int      | Score météo calculé (de 0 à 3)              |

---

##  Dimension : `dim_ville`

Contient les métadonnées géographiques.

| Champ        | Type      | Description                  |
|--------------|-----------|------------------------------|
| ville_id     | int (PK)  | Identifiant de la ville      |
| nom_ville    | varchar   | Nom de la ville              |
| pays         | varchar   | Pays                         |
| latitude     | float     | Latitude géographique        |
| longitude    | float     | Longitude géographique       |

---

##  Dimension : `dim_date`

Permet l’analyse temporelle.

| Champ     | Type      | Description                  |
|-----------|-----------|------------------------------|
| date_id   | int (PK)  | Identifiant de la date       |
| jour      | int       | Jour du mois                 |
| mois      | int       | Mois                         |
| annee     | int       | Année                        |
| saison    | varchar   | Saison correspondante        |

---

##  Dimension : `dim_condition`

Permet de regrouper les types de conditions météo.

| Champ            | Type      | Description                         |
|------------------|-----------|-------------------------------------|
| condition_id     | int (PK)  | Identifiant de la condition météo  |
| description      | varchar   | Description (ex. "Ciel clair")     |
| code_openweather | int       | Code API OpenWeather               |

---

##  Relations

- `mesures_meteo.ville_id` → `dim_ville.ville_id`
- `mesures_meteo.date_id` → `dim_date.date_id`
- `mesures_meteo.condition_id` → `dim_condition.condition_id`

---

##  Pourquoi ce modèle ?

Le modèle en étoile est parfaitement adapté pour des analyses multidimensionnelles comme :
- Comparer les conditions météo entre plusieurs villes
- Évaluer les tendances météo selon les mois / saisons
- Calculer des scores météo agrégés par ville / mois

Il est optimisé pour les tableaux de bord et outils comme Looker Studio ou Power BI.

