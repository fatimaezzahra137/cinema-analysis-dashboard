import pandas as pd
import numpy as np
import ast 

def charger_donnees(chemin_fichier='movies_metadata.csv'):
    try:
        df = pd.read_csv(chemin_fichier, low_memory=False)
        return df
    except FileNotFoundError:
        return None

def nettoyer_dataframe(df):
    # 1. Conversion numérique
    for col in ['budget', 'revenue']:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    df[['budget', 'revenue']] = df[['budget', 'revenue']].fillna(0)

    # 2. Calcul du profit
    df['profit'] = df['revenue'] - df['budget']

    # 3. Nettoyage des genres (Extraction du nom principal)
    def extraire_genre(x):
        try:
            if isinstance(x, str) and x.startswith('['):
                liste = ast.literal_eval(x)
                return liste[0]['name'] if len(liste) > 0 else 'Inconnu'
            return 'Inconnu'
        except:
            return 'Inconnu'

    df['genres'] = df['genres'].apply(extraire_genre)
    
    # 4. Dates et Années
    df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
    df['annee'] = df['release_date'].dt.year.fillna(0).astype(int)

    # Filtrage pour l'analyse financière
    return df[(df['budget'] > 0) & (df['revenue'] > 0)].copy()