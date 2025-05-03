import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Garantir que a pasta 'imagens' exista
os.makedirs("imagens", exist_ok=True)

# Carregar o dataset diretamente da internet
url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-01-21/spotify_songs.csv"
df = pd.read_csv(url)

# Selecionar colunas numéricas relevantes para correlação
colunas_numericas = [
    'track_popularity', 'danceability', 'energy', 'loudness',
    'speechiness', 'acousticness', 'instrumentalness',
    'liveness', 'valence', 'tempo', 'duration_ms'
]
df_numerico = df[colunas_numericas]

# Calcular a matriz de correlação entre essas colunas
matriz_correlacao = df_numerico.corr()

# Criar a figura do gráfico
plt.figure(figsize=(12, 10))

# Criar o heatmap com Seaborn
sns.heatmap(
    matriz_correlacao,
    annot=True,        # mostrar os valores dentro das células
    fmt=".2f",         # formatar os números com 2 casas decimais
    cmap="Blues",   # cores do azul (negativo) ao vermelho (positivo)
    square=True        # células quadradas
)
# Transformar a matriz de correlação em formato de tabela (pares de variáveis)
correlacoes = matriz_correlacao.stack().reset_index()
correlacoes.columns = ['Variavel_1', 'Variavel_2', 'Correlacao']

# Remover as linhas onde a variável está correlacionada com ela mesma (correlação 1.0)
correlacoes = correlacoes[correlacoes['Variavel_1'] != correlacoes['Variavel_2']]

# Remover duplicados (ex: energia x popularidade é igual a popularidade x energia)
correlacoes['Pair'] = correlacoes.apply(lambda row: tuple(sorted([row['Variavel_1'], row['Variavel_2']])), axis=1)
correlacoes = correlacoes.drop_duplicates(subset='Pair')

# Agora filtramos as correlações fortes:
correlacoes_fortes = correlacoes[(correlacoes['Correlacao'] >= 0.7) | (correlacoes['Correlacao'] <= -0.7)]

# Exibir resultados
print("\nCORRELAÇÕES FORTES (>= 0.7 ou <= -0.7):\n")
print(correlacoes_fortes[['Variavel_1', 'Variavel_2', 'Correlacao']].sort_values(by='Correlacao', ascending=False))
# Título do gráfico
plt.title("Mapa de Calor das Correlações Entre Variáveis", fontsize=16)

# Ajustar layout e salvar imagem
plt.tight_layout()
plt.savefig("imagens/heatmap_correlacoes.png")
