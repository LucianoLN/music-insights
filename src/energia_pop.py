import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-01-21/spotify_songs.csv"
df = pd.read_csv(url)


df_ordenado = df.sort_values(by="track_popularity", ascending=False)
df_unico = df_ordenado.drop_duplicates(subset=['track_name', 'track_artist'], keep='first')

plt.figure(figsize=(12, 6))
sns.scatterplot(data=df, x="energy", y="track_popularity", alpha=0.6)

plt.title('Energia da Música vs Popularidade', fontsize=16)
plt.xlabel('Energia')
plt.ylabel('Popularidade')

plt.tight_layout()
plt.savefig("imagens/energia_vs_popularidade_anterior.png")