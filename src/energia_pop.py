import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import utils

os.makedirs("imagens", exist_ok=True)

url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-01-21/spotify_songs.csv"
df = pd.read_csv(url)

df_unico = utils.unicos_ordenados(df)

plt.figure(figsize=(12, 6))
sns.scatterplot(data=df, x="energy", y="track_popularity", alpha=0.6)

plt.title('Relação entre Energia e Popularidade Musical', fontsize=16)
plt.xlabel('Energia')
plt.ylabel('Popularidade')

plt.tight_layout()
plt.savefig("imagens/energia_popularidade.png")
