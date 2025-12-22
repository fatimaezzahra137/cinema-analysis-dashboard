# visualisation.py
import matplotlib.pyplot as plt
import numpy as np

def creer_visualisations_combinees(df_genre, df_annee):
    """
    Crée une figure avec deux graphiques stylisés : 
    1. Barres colorées pour les genres.
    2. Aire remplie pour l'évolution temporelle.
    """
    print("⏳ Création des graphiques stylisés...")
    
    # Appliquer un style (optionnel, 'ggplot' ou 'dark_background')
    plt.style.use('dark_background')
    
    # Création de la figure à 2 colonnes
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(18, 7))
    
    # --- Graphique 1 : Genres (Dégradé de couleurs) ---
    df_top_genre = df_genre.head(10)
    # Palette de couleurs moderne
    couleurs = plt.cm.viridis(np.linspace(0.2, 0.8, len(df_top_genre)))
    
    axes[0].bar(df_top_genre['genres'], df_top_genre['profit_moyen'] / 10**6, color=couleurs)
    axes[0].set_title('Top 10 Genres par Profit Moyen', fontsize=14, fontweight='bold', pad=20)
    axes[0].set_ylabel('Profit Moyen (Millions USD)')
    
    # Rotation des noms de genres
    plt.setp(axes[0].get_xticklabels(), rotation=45, ha='right')

    # --- Graphique 2 : Années (Area Chart / Courbe remplie) ---
    axes[1].plot(df_annee['annee'], df_annee['note_moyenne'], color='#00b4d8', linewidth=2.5)
    # Remplissage sous la ligne pour un look moderne
    axes[1].fill_between(df_annee['annee'], df_annee['note_moyenne'], color='#00b4d8', alpha=0.3)
    
    axes[1].set_title('Tendance de la Note Moyenne (1950-2017)', fontsize=14, fontweight='bold', pad=20)
    axes[1].set_xlabel('Année de Sortie')
    axes[1].set_ylabel('Note Moyenne (sur 10)')
    axes[1].grid(axis='y', linestyle='--', alpha=0.2)

    plt.tight_layout()
    print("✅ Graphiques générés avec succès.")
    return plt