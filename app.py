import streamlit as st
import pandas as pd

st.title("🎬 Meilleurs Films AlloCiné")

df = pd.read_excel("data/AlloCiné_Classement_Film.xlsx")
st.dataframe(df)

st.download_button("📥 Télécharger le fichier Excel", "data/AlloCiné_Classement_Film.xlsx")