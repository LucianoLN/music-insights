# Music Insights

## 🎵 Spotify Data Analysis

Este projeto analisa dados de músicas populares no Spotify entre 2010 e 2019. Utilizamos Python com Pandas, Seaborn e Matplotlib para extrair insights visuais sobre gêneros, energia, popularidade e muito mais.

### 🔍 Objetivos

- Visualizar os gêneros mais comuns
- Analisar correlações entre atributos musicais
- Destacar relações fortes entre características como popularidade, energia e valência

### 📁 Estrutura

- `src/`: Scripts principais
- `utils/`: Funções auxiliares
- `imagens/`: Gráficos gerados
- `data/`: CSVs locais, se necessário

### 🛠️ Tecnologias

- Python 3.10+
- Pandas
- Matplotlib
- Seaborn

### ▶️ Como rodar

1. Clone o repositório:
```bash
git clone https://github.com/LucianoLN/music-insights
cd music-insights
```

2. Instale as dependências:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
``` 

3. Rode o menu principal:
```bash
python3 -m src.main
``` 

### 📁 Estrutura do projeto

```bash
spotify-data-analysis/
├── src/                   # Scripts principais do projeto
│   ├── main.py            # Menu interativo
│   ├── graficos.py        # Geração de gráficos
│   ├── analise_basica.py  # Geração de informações
├── utils/                 # Funções auxiliares
│   └── helpers.py
├── imagens/               # Gráficos gerados
├── data/                  # Dataset local (se necessário)
├── README.md              # Este arquivo
├── requirements.txt       # Dependências
└── .gitignore
```

### Dataset utilizado:
- Fonte: Spotify Hit Songs - Kaggle/TidyTuesday



_Este projeto é de uso livre para fins de aprendizado e apresentação._

