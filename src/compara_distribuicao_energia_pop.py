import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Criar a pasta imagens se não existir
os.makedirs("imagens", exist_ok=True)

# Carregar o dataset
url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-01-21/spotify_songs.csv"
df = pd.read_csv(url)

# Criar a figura e os subplots (2 gráficos lado a lado)
fig, axs = plt.subplots(1, 2, figsize=(14, 6))

# Primeiro Gráfico - Popularidade
sns.histplot(df['track_popularity'], bins=200, ax=axs[0], color='skyblue')
axs[0].set_title('Distribuição da Popularidade')
axs[0].set_xlabel('Popularidade')
axs[0].set_ylabel('Número de Músicas')

# Segundo Gráfico - Energia
sns.histplot(df['energy'], bins=200, ax=axs[1], color='lightgreen')
axs[1].set_title('Distribuição da Energia')
axs[1].set_xlabel('Energia')
axs[1].set_ylabel('Número de Músicas')

# Ajustar layout e salvar
plt.tight_layout()
plt.savefig("imagens/distribuicoes_popularidade_energia.png")
