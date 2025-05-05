def gerar_grafico_generos(df_unico):
    import matplotlib.pyplot as plt
    import seaborn as sns
    import sys
    import os
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    os.makedirs("imagens", exist_ok=True)

    generos_contagem = df_unico['playlist_genre'].value_counts()

    plt.figure(figsize=(12, 6))

    sns.barplot(x=generos_contagem.values, y=generos_contagem.index)

    plt.title('Gráfico dos Gêneros', fontsize=16)
    plt.xlabel('Número de Músicas')
    plt.ylabel('Gênero Musical')

    plt.tight_layout()
    plt.savefig("imagens/grafico_generos.png")


def gerar_heatmap(df_unico):
    import matplotlib.pyplot as plt
    import seaborn as sns
    import sys
    import os
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    os.makedirs("imagens", exist_ok=True)
    colunas_numericas = [
    'track_popularity', 'danceability', 'energy', 'loudness',
    'speechiness', 'acousticness', 'instrumentalness',
    'liveness', 'valence', 'tempo', 'duration_ms'
    ]
    df_numerico = df_unico[colunas_numericas]

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


def gerar_comparacao_energia_pop(df_unico):
    import matplotlib.pyplot as plt
    import seaborn as sns
    import sys
    import os
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    os.makedirs("imagens", exist_ok=True)

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
