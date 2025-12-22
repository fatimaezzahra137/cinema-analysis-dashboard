# analyse.py
import pandas as pd
import numpy as np

def analyser_par_genre(df_nettoye):
    """
    Calcule le profit moyen et le nombre de films par genre.
    """
    print("⏳ Analyse par genre en cours...")
    
    # Regroupement par 'genres'
    # On calcule la moyenne du profit et on compte le nombre de titres
    analyse_genre = df_nettoye.groupby('genres').agg(
        profit_moyen=('profit', "mean"), 
        nombre_films=('title', 'size')
    ).reset_index()
    
    # Filtrage : On ne garde que les genres avec au moins 50 films pour la fiabilité
    analyse_genre = analyse_genre[analyse_genre['nombre_films'] >= 50]
    
    # Tri par profit moyen décroissant
    return analyse_genre.sort_values(by='profit_moyen', ascending=False)


def analyser_par_annee(df_nettoye):
    """
    Calcule le nombre de films et la note moyenne par année.
    """
    print("⏳ Analyse par année en cours...")
    
    # Regroupement par 'annee'
    analyse_annee = df_nettoye.groupby('annee').agg(
        nombre_films=('title', 'size'),
        note_moyenne=('vote_average', "mean") 
    ).reset_index()
    
    # Filtrage des années pertinentes (1950 à 2017)
    analyse_annee = analyse_annee[
        (analyse_annee['annee'] >= 1950) & 
        (analyse_annee['annee'] <= 2017)
    ]
    
    return analyse_annee


def obtenir_top_10_films(df_nettoye):
    """
    Identifie les 10 films individuels ayant généré le plus de profit.
    """
    print("⏳ Extraction du Top 10 des films les plus rentables...")
    
    # Tri des films par profit décroissant
    top_10 = df_nettoye.sort_values(by='profit', ascending=False).head(10)
    
    # On retourne seulement les colonnes utiles pour l'affichage
    return top_10[['title', 'budget', 'revenue', 'profit', 'annee']]