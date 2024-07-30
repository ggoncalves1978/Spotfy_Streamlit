import streamlit as st
import pandas as pd
import time

#ajustar tamnho pagina
st.set_page_config(
    layout="wide",
    page_title="spotify songs"
)

# Utilizado para operações pesadas
@st.cache_data
def load_data():
    df = pd.read_csv("01 Spotify.csv")
    time.sleep(5)
    return df

df = load_data()
st.session_state["df_spotify"] = df




df.set_index("Track", inplace=True)


artists = df["Artist"].value_counts().index
artist = st.sidebar.selectbox("Artista", artists) # Criar caixa multi seleção
df_filtered = df[df["Artist"] == artist]

# display = st.checkbox('Display')   # Cria um checkbox para visualizar ou não o gráfico qdo estiver ativo
# if display:
#     st.bar_chart(df_filtered['Stream'])

albuns = df_filtered["Album"].value_counts().index
album = st.selectbox("Album", albuns)

df_filtered2 = df[df["Album"] == album]

col1, col2 = st.columns([0.7, 0.3])

col1.bar_chart(df_filtered2["Stream"])
col2.line_chart(df_filtered2["Danceability"])

st.write(artist)
st.sidebar.button("test")

