import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import utils

os.makedirs("imagens", exist_ok=True)

url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-01-21/spotify_songs.csv"
df = pd.read_csv(url)

df_unico = utils.unicos_ordenados(df)

generos_contagem = df['playlist_genre'].value_counts().head(10)

plt.figure(figsize=(12, 6))

sns.barplot(x=generos_contagem.values, y=generos_contagem.index)

plt.title('Top 10 Gêneros com Mais Músicas no Dataset', fontsize=16)
plt.xlabel('Número de Músicas')
plt.ylabel('Gênero Musical')

plt.tight_layout()
plt.savefig("imagens/grafico_top_generos.png")