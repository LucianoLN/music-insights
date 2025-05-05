def unicos_ordenados(df):
    df_ordenado = df.sort_values(by="track_popularity", ascending=False)
    df_unico = df_ordenado.drop_duplicates(subset=['track_name', 'track_artist'], keep='first')
    return df_unico

def buscar_musica(df, nome_musica, nome_artista):
    resultado = df[
        (df['track_name'].str.lower() == nome_musica.strip().lower()) &
        (df['track_artist'].str.lower() == nome_artista.strip().lower())
    ]
    return resultado