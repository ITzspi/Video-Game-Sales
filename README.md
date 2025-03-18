# 🎮 Video Game Sales
Esta é uma aplicação de conceitos iniciais estudados em Python para análise de vendas de jogos.

[Clique aqui para acessar o projeto!]()

---

## **Linguagens e Bibliotecas**

- **Linguagens**: Python
- **Bibliotecas**: `streamlit`, `pandas`, `plotly`

---

## **Dataset da Análise**

O dataset utilizado nesta análise contém informações sobre vendas de jogos em diferentes regiões (América do Norte, Europa, Japão e outras). Ele pode ser encontrado no site [Kaggle](https://www.kaggle.com). Você pode acessá-lo clicando [aqui](https://www.kaggle.com/datasets/gregorut/videogamesales).

---

## **Instruções do Projeto**

### 1. **Instalação do Python e Bibliotecas**
   - Certifique-se de ter o Python instalado em sua máquina. Você pode baixá-lo [aqui](https://www.python.org/).
   - Instale as bibliotecas necessárias executando o seguinte comando no terminal:
     ```bash
     pip install streamlit pandas plotly
     ```

### 2. **Executando o Projeto**
   - Dentro da raiz do projeto, execute o seguinte comando no terminal:
     ```bash
     streamlit run Home.py
     ```
   - Isso abrirá uma interface no navegador onde você poderá interagir com a análise de vendas de jogos.

---

## **Funcionalidades do Projeto**

- **Filtros Interativos**: Use sliders na sidebar para filtrar jogos por vendas em diferentes regiões.
- **Gráficos Dinâmicos**: Visualize gráficos para entender a distribuição de vendas.
- **Estatísticas**: Veja métricas como média, mediana e moda das vendas globais e por região.

---

## **Estrutura do Projeto**

- **Home.py**: Arquivo principal que contém a interface do Streamlit e a lógica de análise.
- **Games.py**: Página secundária que exibe detalhes específicos de cada jogo.
- **datasets/vgsales.csv**: Dataset contendo as informações de vendas dos jogos.

---
