import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import utils

os.makedirs("imagens", exist_ok=True)

url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-01-21/spotify_songs.csv"
df = pd.read_csv(url)

df_unico = utils.unicos_ordenados(df)

colunas_numericas = [
    'track_popularity', 'danceability', 'energy', 'loudness',
    'speechiness', 'acousticness', 'instrumentalness',
    'liveness', 'valence', 'tempo', 'duration_ms'
]
df_numerico = df[colunas_numericas]

matriz_correlacao = df_numerico.corr()

plt.figure(figsize=(12, 10))

sns.heatmap(
    matriz_correlacao,
    annot=True,        
    fmt=".2f",         
    cmap="Blues",   
    square=True     
)

plt.title("Mapa de Calor das Correlações Entre Variáveis", fontsize=16)

plt.tight_layout()
plt.savefig("imagens/heatmap_correlacoes.png")
