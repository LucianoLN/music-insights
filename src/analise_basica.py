import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Precisamos do link do dadaset para termos acesso aos dados
url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-01-21/spotify_songs.csv"

# Depois precisamos carregar o dataset. Como fazemos isso? Atribuiremos a variável df a leitura do arquivo csv
df = pd.read_csv(url)

# Ordena por popularidade (do maior para o menor)
df_ordenado = df.sort_values(by='track_popularity', ascending=False)

# Remove duplicadas, mantendo apenas a mais popular
df_unico = df_ordenado.drop_duplicates(subset=['track_name', 'track_artist'], keep='first')

# df_unico = df.drop_duplicates(subset=['track_name', 'track_artist'])

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

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
# ver o top 10 mais popular
top_popular = df_unico.sort_values(by='track_popularity', ascending=False).head(10)
print(top_popular[['track_name', 'track_artist', 'track_popularity']])
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# Isso mostra média, mediana, mínimo e máximo de popularidade, tempo, duração etc.
print(df.describe())

top_popular_unico = df_unico.sort_values(by='track_popularity', ascending=False).head(10)
print(top_popular_unico[['track_name', 'track_artist', 'track_popularity']])


nome_musica = "Dance Monkey"
nome_artista = "Tones and I"
existe = nome_musica in df_unico['track_name'].values
musica2 = df_unico[(df['track_artist'] == nome_artista) & (df['track_name'] == nome_musica)]
musica = df_unico[df['track_name'] == nome_musica]
print(existe)
print(musica)
print(musica2)



print(len(df))

print(len(df_unico))