import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import utils

url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-01-21/spotify_songs.csv"
df = pd.read_csv(url)

df_unico = utils.unicos_ordenados(df)

print("PRIMEIRAS LINHAS DO DATASET:")
print(df_unico.head())

print("\nINFORMAÇÕES GERAIS DO DATASET:")
print(df_unico.info())

print("\nVALORES NULOS POR COLUNA:")
print(df_unico.isnull().sum())

print("\nQUAIS GÊNEROS EXISTEM:")
print(df_unico['playlist_genre'].unique())

print("\nQUANTAS MÚSICAS TEM POR GÊNERO:")
print(df_unico['playlist_genre'].value_counts())

print("\nTOP 10 MÚSICAS MAIS POPULARES")
top_popular = df_unico.sort_values(by='track_popularity', ascending=False).head(10)
print(top_popular[['track_name', 'track_artist', 'track_popularity']])

print("\nVERIFICAR ESTATÍSTICAS NUMÉRICAS")
print(df_unico.describe())
