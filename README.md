# 🎬 Movie Data Analytics & Dashboard

Ce projet propose une solution complète d'analyse de données cinématographiques basée sur le dataset **Movies Metadata**. Il combine des scripts d'analyse statistique, de nettoyage de données et un dashboard interactif moderne.

## 🚀 Fonctionnalités

### 📊 1. Analyse Technique (Scripts Python)
- **Nettoyage automatisé** : Conversion des budgets/revenus, extraction des genres et gestion des dates.
- **Analyse de rentabilité** : Calcul du profit moyen par genre et par année.
- **Identification des leaders** : Extraction du Top 10 des films les plus rentables.
- **Visualisations** : Génération de graphiques stylisés (Matplotlib) montrant les tendances de notation et de profit.

### 🌐 2. Dashboard Interactif (Streamlit)
- **Filtres dynamiques** : Recherche par genre, période (Slider) et profit minimum.
- **Indicateurs Clés (KPIs)** : Affichage en temps réel du nombre de films et du profit moyen.
- **Exploration** : Tableau de données filtrées et bouton de téléchargement CSV.

## 📂 Structure du Projet

- `app.py` : Point d'entrée du dashboard interactif Streamlit.
- `main.py` : Script principal pour l'analyse en ligne de commande (Console).
- `nettoyage.py` : Module de traitement et de préparation des données.
- `analyse.py` : Logique de calcul (Top 10, moyennes par genre).
- `visualisation.py` : Génération des graphiques Matplotlib.
- `compacter.py` : Utilitaire pour réduire la taille du fichier CSV original.
- `requirements.txt` : Liste des dépendances Python.

## 🛠️ Installation

1. **Cloner le projet** :
   ```bash
   git clone [https://github.com/votre-nom/cinema-analysis-dashboard.git](https://github.com/votre-nom/cinema-analysis-dashboard.git)
   cd cinema-analysis-dashboard
