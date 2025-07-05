# Projet Weather Tourism

Ce projet vise à analyser et visualiser l'impact des conditions météorologiques sur le tourisme à l'aide de pipelines ETL, d'Airflow et de tableaux de bord interactifs.

## Structure du projet

- **airflow_dags/** : Contient les DAGs Airflow pour l'automatisation des pipelines de données.
- **dashboard/** : Captures d'écran et liens vers les tableaux de bord de visualisation.
- **data/** :
  - **raw/** : Données brutes collectées.
  - **clean/** : Données nettoyées prêtes à l'analyse.
  - **processed/** : Données transformées pour des analyses spécifiques.
  - **merged/** : Données fusionnées issues de différentes sources.
  - **star_schema/** : Fichiers CSV du schéma en étoile pour l'entrepôt de données.
- **docs/** : Documentation du modèle et diagrammes.
- **etl/** : Scripts Python pour l'extraction, la transformation, le chargement et la modélisation des données.
- **notebooks/** : Notebooks Jupyter pour l'exploration et l'analyse des données.
- **requirements.txt** : Liste des dépendances Python nécessaires au projet.

## Fonctionnalités principales

- Collecte automatisée de données météorologiques et touristiques.
- Nettoyage, transformation et modélisation des données (schéma en étoile).
- Orchestration des pipelines avec Airflow.
- Visualisation des résultats via des tableaux de bord interactifs.

## Installation

1. Clonez ce dépôt :
   ```bash
   git clone https://github.com/HIRATRA/Projet-Final-donne2.git
   ```
2. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```
3. Configurez Airflow et exécutez les DAGs depuis le dossier `airflow_dags/`.

## Utilisation

- Exécutez les scripts ETL dans le dossier `etl/` pour préparer les données.
- Lancez les notebooks dans `notebooks/` pour l'analyse exploratoire.
- Consultez les tableaux de bord dans le dossier `dashboard/`.

## Auteurs

- Hiratra Danarson
