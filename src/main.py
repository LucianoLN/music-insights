import pandas as pd

from utils.helpers import buscar_musica
from utils.helpers import unicos_ordenados
from src import graficos


df = pd.read_csv("data/spotify_musicas.csv")
df_unico = unicos_ordenados(df)

def menu():
    while True:
        print("\n MENU PRINCIPAL")
        print("1. Ver número total de músicas")
        print("2. Gerar gráfico de gêneros")
        print("3. Gerar heatmap de correlação")
        print("4. Comparação de energia e popularidade")
        print("5. Buscar uma música por nome e artista")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print(f"Total de músicas no dataset: {len(df)}")

        elif opcao == "2":
            graficos.gerar_grafico_generos(df_unico)
            print("Gráfico de gêneros salvo em imagens/.")

        elif opcao == "3":
            graficos.gerar_heatmap(df_unico)
            print("Gráfico de heatmap salvo em imagens/.")

        elif opcao == "4":
            graficos.gerar_comparacao_energia_pop(df_unico)
            print("Gráfico de comparação salvo em imagens/.")

        elif opcao == "5":
            nome = input("Nome da música: ")
            artista = input("Nome do artista: ")
            resultado = buscar_musica(df, nome, artista)
            print(resultado if not resultado.empty else "Música não encontrada.")

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
