import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. Configuration de la page
st.set_page_config(page_title="Dashboard Cinéma", layout="wide")

# 2. Fonction pour charger les données avec Cache (évite de relire le CSV à chaque clic)
@st.cache_data
def charger_donnees():
    # Remplace par le nom exact de ton fichier compressé
    df = pd.read_csv('movies_metadata.csv', low_memory=False)
    # Conversion de la date en format datetime
    df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
    df['year'] = df['release_date'].dt.year
    # Calcul du Profit Net
    df['profit'] = df['revenue'] - df['budget']
    return df

df = charger_donnees()

# 3. Création du Formulaire dans la barre latérale (Sidebar)
with st.sidebar.form(key='filtres_recherche'):
    st.header("🔍 Filtres de recherche")
    
    # Sélecteur de genres (Multi-choix)
    genres_disponibles = sorted(df['genres'].dropna().unique())
    genres_selectionnes = st.multiselect("Sélectionnez les genres :", genres_disponibles, default=None)
    
    # Slider pour l'année
    annee_min, annee_max = int(df['year'].min()), int(df['year'].max())
    periode = st.slider("Période (Années) :", annee_min, annee_max, (2000, 2024))
    
    # Slider pour le Profit Minimum (en Millions)
    profit_min = st.slider("Profit minimum (M$)", 0, 3000, 500)
    
    # BOUTON DE VALIDATION (Obligatoire dans un formulaire)
    submit_button = st.form_submit_button(label='Appliquer les filtres')

# 4. Logique de filtrage (ne s'active que si on clique sur le bouton ou au chargement)
df_filtre = df[(df['year'] >= periode[0]) & (df['year'] <= periode[1])]
df_filtre = df_filtre[df_filtre['profit'] >= (profit_min * 1_000_000)]

if genres_selectionnes:
    # Filtre simple si le genre est présent dans la colonne
    df_filtre = df_filtre[df_filtre['genres'].astype(str).str.contains('|'.join(genres_selectionnes))]

# 5. Affichage des résultats au centre
st.title("🏆 Analyse des Films les plus Rentables")

# Mise en page avec des colonnes pour des statistiques rapides
col1, col2, col3 = st.columns(3)
col1.metric("Films trouvés", len(df_filtre))
col2.metric("Profit Moyen", f"{df_filtre['profit'].mean() / 1_000_000:.1f} M$")
col3.metric("Année max", int(df_filtre['year'].max()) if not df_filtre.empty else "N/A")

st.write("---")

# Affichage du Tableau (Top 10)
st.subheader(f"Top 10 des Films ({periode[0]} - {periode[1]})")
top_10 = df_filtre.sort_values(by='profit', ascending=False).head(10)

# Formatage pour l'affichage
top_10_display = top_10[['title', 'profit', 'year']].copy()
top_10_display['profit'] = (top_10_display['profit'] / 1_000_000).map('{:,.1f} M$'.format)
st.table(top_10_display)

# Bouton de téléchargement
csv = df_filtre.to_csv(index=False).encode('utf-8')
st.download_button(
    label="📥 Télécharger les données filtrées (CSV)",
    data=csv,
    file_name='films_filtres.csv',
    mime='text/csv',
)