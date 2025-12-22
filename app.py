import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from nettoyage import charger_donnees, nettoyer_dataframe 
from analyse import analyser_par_genre, analyser_par_annee, obtenir_top_10_films

# CONFIGURATION PAGE
st.set_page_config(layout="wide", page_title="Cinéma Analytics", page_icon="🎬")
plt.style.use('dark_background') # Style sombre pour les graphiques

# CHARGEMENT CACHÉ
@st.cache_data
def load_all_data():
    raw = charger_donnees()
    if raw is None: return None, None, None, None
    clean = nettoyer_dataframe(raw)
    return clean, analyser_par_genre(clean), analyser_par_annee(clean), obtenir_top_10_films(clean)

df_clean, df_genre, df_annee, df_top10 = load_all_data()

# BARRE LATÉRALE
with st.sidebar:
    st.title("⚙️ Filtres & Export")
    genres_liste = sorted(df_genre['genres'].unique())
    selected_genres = st.multiselect("Genres à afficher :", options=genres_liste, default=genres_liste[:6])
    
    st.divider()
    # Bouton de téléchargement
    csv = df_clean[df_clean['genres'].isin(selected_genres)].to_csv(index=False).encode('utf-8')
    st.download_button("📥 Télécharger les données (CSV)", data=csv, file_name='films_extraits.csv', mime='text/csv')

# TITRE ET MÉTRIQUES
st.title("🎬 MovieInsight : Tableau de Bord Stratégique")
m1, m2, m3 = st.columns(3)
m1.metric("🎥 Films Analysés", f"{len(df_clean):,}")
m2.metric("🏆 Genre n°1", df_genre.iloc[0]['genres'])
m3.metric("💰 Profit Max Moyen", f"{(df_genre.iloc[0]['profit_moyen']/10**6):.1f} M$")

st.divider()

# AFFICHAGE 2 COLONNES
c1, c2 = st.columns(2)

with c1:
    st.header("💎 Rentabilité par Genre")
    df_f = df_genre[df_genre['genres'].isin(selected_genres)]
    if not selected_genres:
        st.warning("Choisissez un genre dans le menu.")
    else:
        fig, ax = plt.subplots(figsize=(10, 5))
        colors = plt.cm.viridis(np.linspace(0, 1, len(df_f)))
        ax.bar(df_f['genres'], df_f['profit_moyen']/10**6, color=colors)
        plt.setp(ax.get_xticklabels(), rotation=45, ha='right')
        st.pyplot(fig)

with c2:
    st.header("📈 Évolution des Notes")
    fig2, ax2 = plt.subplots(figsize=(10, 5))
    ax2.plot(df_annee['annee'], df_annee['note_moyenne'], color='#00b4d8', linewidth=2)
    ax2.fill_between(df_annee['annee'], df_annee['note_moyenne'], color='#00b4d8', alpha=0.2)
    st.pyplot(fig2)

# TOP 10 DES FILMS (TABLEAU)
st.divider()
st.header("🏆 Top 10 des Films les plus Rentables")
df_top_disp = df_top10.copy()
df_top_disp['profit'] = (df_top_disp['profit']/10**6).map('{:,.0f} M$'.format)
st.table(df_top_disp[['title', 'profit', 'annee']].rename(columns={'title':'Film', 'profit':'Profit Net', 'annee':'Année'}))