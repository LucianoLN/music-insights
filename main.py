import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Precisamos do link do dadaset para termos acesso aos dados
url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-01-21/spotify_songs.csv"

# Depois precisamos carregar o dataset. Como fazemos isso? Atribuiremos a variável df a leitura do arquivo csv
df = pd.read_csv(url)

# Para ver as primeiras linhas
print(df.head())

# Para ver informaçoes gerais do dataset
print(df.info())

# Para verificar se tem valores nulos
print(df.isnull().sum())

# Para ver quais generos existem
print(df['playlist_genre'].unique())

# Para ver quantas musicas tem por genero
print(df['playlist_genre'].value_counts())

# ver o top 10 mais popular
top_popular = df.sort_values(by='track_popularity', ascending=False).head(10)
print(top_popular[['track_name', 'track_artist', 'track_popularity']])

print(df.describe())
