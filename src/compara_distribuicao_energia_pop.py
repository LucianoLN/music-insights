import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import utils

os.makedirs("imagens", exist_ok=True)

url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-01-21/spotify_songs.csv"
df = pd.read_csv(url)

df_unico = utils.unicos_ordenados(df)

fig, axs = plt.subplots(1, 2, figsize=(14, 6))

sns.histplot(df_unico['track_popularity'], bins=30, ax=axs[0], color='skyblue')
axs[0].set_title('Distribuição da Popularidade')
axs[0].set_xlabel('Popularidade')
axs[0].set_ylabel('Número de Músicas')

sns.histplot(df_unico['energy'], bins=30, ax=axs[1], color='lightgreen')
axs[1].set_title('Distribuição da Energia')
axs[1].set_xlabel('Energia')
axs[1].set_ylabel('Número de Músicas')

plt.tight_layout()
plt.savefig("imagens/comparativo_distribuicoes_popularidade_energia.png")
